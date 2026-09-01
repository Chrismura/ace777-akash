#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8

require "json"
require "time"
require "fileutils"
require "csv"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

root = File.expand_path("..", __dir__)
run_dir = File.expand_path(ENV.fetch("RUN_DIR", "runs"), root)
pnl_archive = File.join(root, "master_base", "pnl")
index_csv = File.join(pnl_archive, "INDEX_MASTER_BASE.csv")

tag = ENV["STATE_TAG"] || ENV["TEST_TAG_OVERRIDE"]
unless tag
  latest_beta = Dir.glob(File.join(run_dir, "*_BETA_X5.csv")).max_by { |f| File.mtime(f) }
  tag = if latest_beta
          File.basename(latest_beta).sub(/_BETA_X5\.csv\z/, "")
        else
          "MASTER_BASE_V8_5_IMPACT_4H"
        end
end

run_meta = begin
  meta_path = File.join(run_dir, "#{tag}_run_meta.json")
  File.file?(meta_path) ? JSON.parse(File.read(meta_path)) : {}
rescue StandardError
  {}
end

beta_csv = ENV["BETA_CSV"] || File.join(run_dir, "#{tag}_BETA_X5.csv")
alpha_csv = ENV["ALPHA_CSV"] || File.join(run_dir, "#{tag}_ALPHA_X13_BURST13.csv")
run_id = run_meta["run_id"] || run_meta["runId"] || tag
fee_reconciliation = run_meta["fee_reconciliation"] || "UNMATCHED_BINANCE_FEES"

def load_session_start(run_dir, tag)
  return ENV["RUN_START_UTC"] if ENV["RUN_START_UTC"] && !ENV["RUN_START_UTC"].empty?

  meta_path = File.join(run_dir, "#{tag}_run_meta.json")
  return nil unless File.file?(meta_path)

  JSON.parse(File.read(meta_path))["start_utc"]
rescue StandardError
  nil
end

session_start = load_session_start(run_dir, tag)

def analyze_csv(path, unit_label, min_ts: nil)
  stats = {
    label: unit_label, path: path, present: File.file?(path),
    filled: 0, wins: 0, losses: 0, flats: 0,
    gross: 0.0, fees: 0.0, net: 0.0, gains: 0.0, losses_sum: 0.0, bps_sum: 0.0,
    skips: 0, skip_reasons: Hash.new(0), exit_reasons: Hash.new(0),
    sides: Hash.new(0), best: nil, worst: nil,
    first_ts: nil, last_ts: nil
  }
  return stats unless stats[:present]

  File.foreach(path).with_index do |line, idx|
    next if idx.zero?

    cols = line.strip.split(",", -1)
    next if cols.size < 10

    ts, _cycle, side, status, _entry, _exit_px, _qty, bps, pnl, reason, fee_usdt, pnl_net = cols
    next if min_ts && ts && !ts.empty? && ts < min_ts

    stats[:first_ts] ||= ts
    stats[:last_ts] = ts if ts && !ts.empty?

    if status == "SKIPPED" || side == "SKIP"
      stats[:skips] += 1
      key = reason.to_s.empty? ? "unknown" : reason.split(",", 2).first
      stats[:skip_reasons][key] += 1
      next
    end

    next unless status == "FILLED"

    pnl_f = pnl.to_f
    fee_f = fee_usdt.to_s.empty? ? 0.0 : fee_usdt.to_f
    net_f = pnl_net.to_s.empty? ? pnl_f - fee_f : pnl_net.to_f
    bps_f = bps.to_f
    stats[:filled] += 1
    stats[:gross] += pnl_f
    stats[:fees] += fee_f
    stats[:net] += net_f
    stats[:bps_sum] += bps_f
    stats[:sides][side] += 1 if side && !side.empty?
    exit_key = reason.to_s.empty? ? "unknown" : reason.split(",", 2).first
    stats[:exit_reasons][exit_key] += 1

    if net_f > 0
      stats[:wins] += 1
      stats[:gains] += net_f
    elsif net_f < 0
      stats[:losses] += 1
      stats[:losses_sum] += net_f
    else
      stats[:flats] += 1
    end

    stats[:best] = { pnl: net_f, ts: ts } if stats[:best].nil? || net_f > stats[:best][:pnl]
    stats[:worst] = { pnl: net_f, ts: ts } if stats[:worst].nil? || net_f < stats[:worst][:pnl]
  end
  stats
end

def fmt_usdt(v)
  sign = v >= 0 ? "+" : ""
  "#{sign}#{format('%.4f', v)}"
end

def winrate(filled, wins)
  return "—" if filled.zero?

  format("%.1f%%", (wins.to_f / filled) * 100.0)
end

def avg_bps(stats)
  return "—" if stats[:filled].zero?

  format("%.2f", stats[:bps_sum] / stats[:filled])
end

def top_hash(h, n = 5)
  h.sort_by { |_, v| -v }.first(n)
end

def direction_summary(sides)
  return "—" if sides.empty?

  sides.sort_by { |_, v| -v }.map { |s, c| "#{s} (#{c})" }.join(", ")
end

def duration_human(first_ts, last_ts)
  return "—" unless first_ts && last_ts

  a = Time.parse(first_ts)
  b = Time.parse(last_ts)
  sec = (b - a).to_i
  h = sec / 3600
  m = (sec % 3600) / 60
  "#{h}h#{format('%02d', m)}m"
rescue StandardError
  "—"
end

beta = analyze_csv(beta_csv, "BETA (SCOUT x5)", min_ts: session_start)
alpha = analyze_csv(alpha_csv, "ALPHA (HUNTER x13)", min_ts: session_start)
total_net = beta[:net] + alpha[:net]
total_filled = beta[:filled] + alpha[:filled]
total_wins = beta[:wins] + alpha[:wins]

start_ts = [beta[:first_ts], alpha[:first_ts]].compact.min
end_ts = [beta[:last_ts], alpha[:last_ts]].compact.max
now = Time.now.utc
stamp = now.strftime("%Y%m%d_%H%M%S")
report_name = "RAPPORT_PNL_AUTO_#{stamp}.md"
report_run = File.join(run_dir, report_name)
report_archive = File.join(pnl_archive, report_name)

config_name = run_meta["config"] || ENV.fetch("ACE777_CONFIG_NAME", "non_charge")
config_version = run_meta["version"] || ENV.fetch("ACE777_CONFIG_VERSION", "?")
buy_beta = ENV.fetch("BUY_USDT_BETA", "?")
buy_alpha = ENV.fetch("BUY_USDT_ALPHA", "?")
llm_enabled = ENV.fetch("LLM_GATE_ENABLED", "?")
llm_fail = ENV.fetch("LLM_GATE_FAIL_CLOSED", "?")

status_label = if total_net > 0
                 "POSITIF"
               elsif total_net < 0
                 "NEGATIF"
               else
                 "NEUTRE"
               end

def unit_section(stats)
  lines = []
  lines << "| Métrique | Valeur |"
  lines << "|----------|--------|"
  lines << "| Trades FILLED | #{stats[:filled]} |"
  lines << "| Gagnants | #{stats[:wins]} |"
  lines << "| Perdants | #{stats[:losses]} |"
  lines << "| Flat (0) | #{stats[:flats]} |"
  lines << "| Win rate | **#{winrate(stats[:filled], stats[:wins])}** |"
  lines << "| Gains totaux | #{fmt_usdt(stats[:gains])} USDT |"
  lines << "| Pertes totales | #{fmt_usdt(stats[:losses_sum])} USDT |"
  lines << "| PNL brut | #{fmt_usdt(stats[:gross])} USDT |"
  lines << "| Frais | #{fmt_usdt(stats[:fees])} USDT |"
  lines << "| **PNL net** | **#{fmt_usdt(stats[:net])} USDT** |"
  lines << "| BPS moyen | #{avg_bps(stats)} |"
  lines << ""
  if stats[:best]
    lines << "**Meilleur trade:** #{fmt_usdt(stats[:best][:pnl])} USDT"
    lines << "**Pire trade:** #{fmt_usdt(stats[:worst][:pnl])} USDT"
    lines << ""
  end
  lines << "**Direction:** #{direction_summary(stats[:sides])}"
  lines << ""
  lines << "**Raisons de sortie (exitReason):**"
  lines << "| Raison | Nb |"
  lines << "|--------|-----|"
  if stats[:exit_reasons].empty?
    lines << "| _aucun trade_ | 0 |"
  else
    top_hash(stats[:exit_reasons]).each { |r, c| lines << "| #{r} | #{c} |" }
  end
  lines << ""
  lines << "**Cycles SKIP:** #{stats[:skips]}"
  lines << "| Raison | Nb |"
  lines << "|--------|-----|"
  if stats[:skip_reasons].empty?
    lines << "| _aucun_ | 0 |"
  else
    top_hash(stats[:skip_reasons]).each { |r, c| lines << "| #{r} | #{c} |" }
  end
  lines.join("\n")
end

lines = []
lines << "# RAPPORT PNL AUTO — #{tag}"
lines << ""
lines << "**Session:** `#{tag}`"
lines << "**run_id:** `#{run_id}`"
lines << "**Frais Binance:** `#{fee_reconciliation}` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)"
lines << "**Période:** #{start_ts || '—'} → #{end_ts || '—'} (#{duration_human(start_ts, end_ts)})"
lines << "**Setup:** `#{config_name}` v`#{config_version}` | BETA `#{buy_beta}` USDT | ALPHA `#{buy_alpha}` USDT | LLM gate `#{llm_enabled}` fail_closed=`#{llm_fail}`"
lines << "**Généré:** #{now.strftime('%Y-%m-%dT%H:%M:%SZ')} UTC"
if session_start
  lines << "**Filtre session:** `ts >= #{session_start}` (lignes CSV antérieures exclues)"
end
lines << ""
lines << "---"
lines << ""
lines << "## BILAN GLOBAL"
lines << ""
lines << "| Métrique | Valeur |"
lines << "|----------|--------|"
lines << "| PNL brut BETA | #{fmt_usdt(beta[:gross])} USDT |"
lines << "| Frais BETA | #{fmt_usdt(beta[:fees])} USDT |"
lines << "| **PNL net BETA** | **#{fmt_usdt(beta[:net])} USDT** |"
lines << "| PNL brut ALPHA | #{fmt_usdt(alpha[:gross])} USDT |"
lines << "| Frais ALPHA | #{fmt_usdt(alpha[:fees])} USDT |"
lines << "| **PNL net ALPHA** | **#{fmt_usdt(alpha[:net])} USDT** |"
lines << "| **PNL SESSION TOTAL** | **#{fmt_usdt(total_net)} USDT** |"
lines << "| Statut | `#{status_label}` |"
lines << ""
lines << "---"
lines << ""
lines << "## BETA — #{beta[:label]}"
lines << ""
lines << unit_section(beta)
lines << ""
lines << "---"
lines << ""
lines << "## ALPHA — #{alpha[:label]}"
lines << ""
if alpha[:filled].zero?
  lines << "| Métrique | Valeur |"
  lines << "|----------|--------|"
  lines << "| Trades FILLED | 0 |"
  lines << "| **PNL net** | **0.0000 USDT** |"
  lines << ""
  lines << "*ALPHA n'a pas exécuté de trade — vérifier duo_wait, radar, stase, llm_gate dans les SKIP.*"
  lines << ""
  lines << "**Cycles SKIP:** #{alpha[:skips]}"
  lines << "| Raison | Nb |"
  lines << "|--------|-----|"
  top_hash(alpha[:skip_reasons]).each { |r, c| lines << "| #{r} | #{c} |" } unless alpha[:skip_reasons].empty?
else
  lines << unit_section(alpha)
end
lines << ""
lines << "---"
lines << ""
lines << "## SYNTHÈSE"
lines << ""
lines << "| Indicateur | BETA | ALPHA | TOTAL |"
lines << "|------------|------|-------|-------|"
lines << "| Trades | #{beta[:filled]} | #{alpha[:filled]} | #{total_filled} |"
lines << "| PnL | #{fmt_usdt(beta[:net])} | #{fmt_usdt(alpha[:net])} | **#{fmt_usdt(total_net)}** |"
lines << "| Win rate | #{winrate(beta[:filled], beta[:wins])} | #{winrate(alpha[:filled], alpha[:wins])} | #{winrate(total_filled, total_wins)} |"
lines << ""

# A2 — IRM régimes (lecture seule, scripts/irm_tension.rb) — hors moteur
irm_rb = File.join(root, "scripts", "irm_tension.rb")
if File.file?(irm_rb)
  load irm_rb
  if defined?(IrmTension)
    lines << IrmTension.markdown_section(beta_csv, min_ts: session_start)
    lines << ""
  end
end

# B1/B2 pointeur Engle
lines << "## Engle — couches évolutives (hors moteur)"
lines << ""
lines << "- Plan: `engle/PLAN_COUCHES_B1_B3.md`"
lines << "- Journal B1: `engle/journal/ENGLE_JOURNAL_DERNIER.md` (généré via `engle_journal.rb` / `update_state_md.sh`)"
lines << "- Adapt B2: `ENGLE_ADAPT=#{ENV.fetch('ENGLE_ADAPT', '0')}` (défaut OFF = usine pure ; `log` = posture JSON only)"
posture_json = File.join(run_dir, "engle_adapt_posture.json")
if File.file?(posture_json)
  begin
    pj = JSON.parse(File.read(posture_json))
    lines << "- Dernière posture log: `#{pj['posture']}` · régime `#{pj['regime']}` · applied=`#{pj['applied']}`"
  rescue StandardError
    lines << "- Fichier posture présent mais illisible"
  end
end
lines << ""

lines << "## CONFIG ACTIVE (snapshot)"
lines << ""
lines << "- ENTRY_25_75 BETA: `#{ENV.fetch('ENTRY_25_75_INITIAL_FRACTION_BETA', '?')}` | ALPHA: `#{ENV.fetch('ENTRY_25_75_INITIAL_FRACTION_ALPHA', '?')}`"
lines << "- SHOCK_EXIT: `#{ENV.fetch('SHOCK_EXIT_10_BPS', '?')}` bps"
lines << "- VOLATILITY_FILTER: `#{ENV.fetch('VOLATILITY_FILTER', '—')}`"
lines << "- STASE: spread=`#{ENV.fetch('STASE_DYNAMIQUE_MAX_SPREAD_BPS', '?')}` vol=`#{ENV.fetch('STASE_DYNAMIQUE_MAX_VOLATILITY', '?')}`"
lines << "- POLL_SEC: `#{ENV.fetch('POLL_SEC', '?')}`"
lines << ""
lines << "---"
lines << ""
lines << "*Rapport auto — CSV: `#{File.basename(beta_csv)}` | `#{File.basename(alpha_csv)}`*"
lines << "*STATE: `runs/STATE.md`*"

content = lines.join("\n") + "\n"
FileUtils.mkdir_p(run_dir)
FileUtils.mkdir_p(pnl_archive)
File.write(report_run, content)
File.write(report_archive, content)

# Lien latest
latest_link = File.join(run_dir, "RAPPORT_PNL_DERNIER.md")
File.write(latest_link, content)

# Index CSV
FileUtils.mkdir_p(pnl_archive)
unless File.file?(index_csv)
  File.write(index_csv, "model_file,start_utc,end_utc,tag,pnl_total_usdt,status,notes,report_file\n")
end

notes = "BETA=#{fmt_usdt(beta[:net])} ALPHA=#{fmt_usdt(alpha[:net])} TOTAL=#{fmt_usdt(total_net)}"
row = [
  ENV.fetch("ACE777_CONFIG_NAME", "config_active"),
  start_ts || "",
  end_ts || "",
  tag,
  format("%.4f", total_net),
  status_label,
  notes,
  report_name
]

CSV.open(index_csv, "a") { |csv| csv << row }

# RUN_INDEX.md — append section
run_index = File.join(root, "RUN_INDEX.md")
if File.file?(run_index)
  entry = <<~ENTRY

    ---

    ## #{now.strftime('%Y-%m-%d')} — #{tag} (auto)

    - Profil: `#{config_name}` v`#{config_version}`
    - Tag: `#{tag}`
    - Période: `#{start_ts}` → `#{end_ts}`
    - Logs:
      - `#{File.basename(beta_csv)}`
      - `#{File.basename(alpha_csv)}`
    - Paramètres clé:
      - `BUY_USDT_BETA=#{buy_beta}`
      - `BUY_USDT_ALPHA=#{buy_alpha}`
      - `LLM_GATE_ENABLED=#{llm_enabled}`
      - `LLM_GATE_FAIL_CLOSED=#{llm_fail}`
    - Résultat:
      - BETA: `#{fmt_usdt(beta[:net])} USDT` (#{beta[:filled]} trades)
      - ALPHA: `#{fmt_usdt(alpha[:net])} USDT` (#{alpha[:filled]} trades)
      - Total: `#{fmt_usdt(total_net)} USDT`
    - Rapport: `#{report_name}`
    - Verdict: `#{status_label}`

  ENTRY
  File.open(run_index, "a") { |f| f.write(entry) }
end

puts "PNL_REPORT_OK: #{report_run}"
puts "PNL_ARCHIVE_OK: #{report_archive}"
puts "PNL_TOTAL: #{fmt_usdt(total_net)} USDT (#{status_label})"
