#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
#
# B1 — Journal Engle post-run / à la demande — ZÉRO impact moteur.
# Usage:
#   ruby scripts/engle_journal.rb
#   STATE_TAG=NUAGE_PROD_4H ruby scripts/engle_journal.rb
#
# Sortie: engle/journal/ENGLE_JOURNAL_<TAG>_<stamp>.md + ENGLE_JOURNAL_DERNIER.md

require "json"
require "time"
require "fileutils"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

root = File.expand_path("..", __dir__)
run_dir = File.expand_path(ENV.fetch("RUN_DIR", "runs"), root)
journal_dir = File.join(root, "engle", "journal")
FileUtils.mkdir_p(journal_dir)

load File.join(root, "scripts", "irm_tension.rb")

tag = ENV["STATE_TAG"] || ENV["TEST_TAG_OVERRIDE"]
unless tag
  latest_beta = Dir.glob(File.join(run_dir, "*_BETA_X5.csv")).max_by { |f| File.mtime(f) }
  tag = if latest_beta
          File.basename(latest_beta).sub(/_BETA_X5\.csv\z/, "")
        else
          "NUAGE_PROD_4H"
        end
end

beta_csv = ENV["BETA_CSV"] || File.join(run_dir, "#{tag}_BETA_X5.csv")
alpha_csv = ENV["ALPHA_CSV"] || File.join(run_dir, "#{tag}_ALPHA_X13_BURST13.csv")
meta_path = File.join(run_dir, "#{tag}_run_meta.json")
session_start = ENV["RUN_START_UTC"]
if (!session_start || session_start.empty?) && File.file?(meta_path)
  session_start = begin
    JSON.parse(File.read(meta_path))["start_utc"]
  rescue StandardError
    nil
  end
end

SKIP_KEYS = %w[
  momentum_too_small wall_not_collapsed radar_block impulse_resonance_wait
  direction_unclear tension_stale duo_wait stase_ecoute tactic_mismatch
  soft_anomaly
].freeze

def analyze_unit(path, min_ts: nil)
  out = {
    present: File.file?(path),
    cycles: 0, filled: 0, skips: 0, net: 0.0,
    skip_reasons: Hash.new(0),
    first_ts: nil, last_ts: nil
  }
  return out unless out[:present]

  File.foreach(path).with_index do |line, idx|
    next if idx.zero?

    cols = line.strip.split(",", -1)
    next if cols.size < 10

    ts = cols[0].to_s
    next if min_ts && !ts.empty? && ts < min_ts

    out[:cycles] += 1
    out[:first_ts] ||= ts
    out[:last_ts] = ts if !ts.empty?

    side = cols[2].to_s
    status = cols[3].to_s
    reason = cols[9].to_s
    msg = cols[11].to_s
    blob = "#{reason} #{msg} #{cols[10]}"

    if status == "SKIPPED" || side == "SKIP"
      out[:skips] += 1
      key = "other"
      SKIP_KEYS.each do |k|
        if blob.include?(k)
          key = k
          break
        end
      end
      if key == "other" && !reason.empty?
        key = reason.split(/[\s,|]/).first.to_s[0, 48]
        key = "other" if key.empty?
      end
      out[:skip_reasons][key] += 1
      next
    end

    next unless status == "FILLED"

    out[:filled] += 1
    out[:net] += cols[8].to_f
  end
  out
end

def top_n(hash, n = 8)
  hash.sort_by { |_, v| -v }.first(n)
end

def posture_for(regime)
  case regime
  when "COMPRESSE"
    ["WAIT_COLD", "Marché calme — ne pas assouplir les seuils ; usine pure recommandée."]
  when "TRANSITOIRE"
    ["WATCH", "Bruit retail — observer ; pas de knobs B3."]
  when "CLUSTER"
    ["HUNT_WINDOW", "Tension haute (proxy) — candidature future B3 gate/soft, pas encore appliqué."]
  else
    ["UNKNOWN", "Régime indéterminé."]
  end
end

beta = analyze_unit(beta_csv, min_ts: session_start)
alpha = analyze_unit(alpha_csv, min_ts: session_start)

irm_rows = IrmTension.load_rows(beta_csv, min_ts: session_start)
irm = IrmTension.summarize(irm_rows)
posture_code, posture_txt = posture_for(irm[:current])

adapt = ENV.fetch("ENGLE_ADAPT", "0")
now = Time.now.utc
stamp = now.strftime("%Y%m%d_%H%M%S")
out_path = File.join(journal_dir, "ENGLE_JOURNAL_#{tag}_#{stamp}.md")
latest = File.join(journal_dir, "ENGLE_JOURNAL_DERNIER.md")

lines = []
lines << "# JOURNAL ENGLE — #{tag}"
lines << ""
lines << "- Généré: `#{now.iso8601}` (UTC)"
lines << "- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=#{adapt}`"
lines << "- Session start (filtre): `#{session_start || "n/a"}`"
lines << "- CSV: `#{File.basename(beta_csv)}` · `#{File.basename(alpha_csv)}`"
lines << "- Base: usine V2.2.1 + champion 37fca367 — **non modifié**"
lines << ""
lines << "## Régime IRM (proxy)"
lines << ""
if irm[:n].zero?
  lines << "*Pas assez de cycles BETA pour IRM.*"
else
  lines << "| Régime | Cycles | % | Fills | PnL fills |"
  lines << "|--------|--------|---|-------|-----------|"
  IrmTension::REGIMES.each do |name|
    lines << format(
      "| %s | %d | %.1f%% | %d | %+.4f |",
      IrmTension.label_fr(name),
      irm[:counts][name],
      irm[:pct][name],
      irm[:fills_by][name],
      irm[:pnl_by][name]
    )
  end
  lines << ""
  lines << format(
    "- Courant (proxy): **%s** · μ=%.4f · σ=%.4f · n=%d",
    IrmTension.label_fr(irm[:current]),
    irm[:mean],
    irm[:std],
    irm[:n]
  )
end
lines << ""
lines << "## Posture recommandée (conseil — pas appliquée)"
lines << ""
lines << "- Code: `#{posture_code}`"
lines << "- #{posture_txt}"
lines << "- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié."
lines << ""
lines << "## Activité session"
lines << ""
lines << "| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |"
lines << "|-------|--------|-------|-------|------------------|---------|"
[
  ["BETA", beta],
  ["ALPHA", alpha]
].each do |label, u|
  win = if u[:first_ts]
          "`#{u[:first_ts]}` → `#{u[:last_ts]}`"
        else
          "—"
        end
  lines << format(
    "| %s | %d | %d | %d | %+.4f | %s |",
    label, u[:cycles], u[:filled], u[:skips], u[:net], win
  )
end
total_net = beta[:net] + alpha[:net]
lines << format("| **TOTAL** | | %d | | **%+.4f** | |", beta[:filled] + alpha[:filled], total_net)
lines << ""

[["BETA", beta], ["ALPHA", alpha]].each do |label, u|
  lines << "## SKIP #{label} (top)"
  lines << ""
  if u[:skip_reasons].empty?
    lines << "*Aucun SKIP classé.*"
  else
    lines << "| Raison | Nb | % skips |"
    lines << "|--------|-----|---------|"
    sk = [u[:skips], 1].max
    top_n(u[:skip_reasons]).each do |r, c|
      lines << format("| `%s` | %d | %.1f%% |", r, c, 100.0 * c / sk)
    end
  end
  lines << ""
end

lines << "## Lecture courte (marché calme)"
lines << ""
if irm[:pct]["COMPRESSE"].to_f >= 60.0
  lines << "1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent."
  lines << "2. **Ne pas baisser les barrières** pour « forcer » des fills en calme."
  lines << "3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel)."
elsif irm[:pct]["CLUSTER"].to_f >= 25.0
  lines << "1. Part de **CLUSTER** non négligeable — candidature future B3 (un knobs)."
  lines << "2. Comparer fills ALPHA vs runs calmes avant tout GO knobs."
else
  lines << "1. Régime mixte — journaliser encore 1–2 runs 4h avant B3."
end
lines << "4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`."
lines << ""
lines << "---"
lines << ""
lines << "*B1 engle_journal.rb — zéro ordre, zéro genesis.*"

content = lines.join("\n") + "\n"
File.write(out_path, content)
File.write(latest, content)

# JSON léger pour outils
json_path = File.join(journal_dir, "ENGLE_JOURNAL_DERNIER.json")
File.write(
  json_path,
  JSON.pretty_generate(
    tag: tag,
    generated_utc: now.iso8601,
    session_start: session_start,
    engle_adapt: adapt,
    irm_current: irm[:current],
    irm_pct: irm[:pct],
    posture: posture_code,
    beta: { cycles: beta[:cycles], filled: beta[:filled], skips: beta[:skips], net: beta[:net] },
    alpha: { cycles: alpha[:cycles], filled: alpha[:filled], skips: alpha[:skips], net: alpha[:net] },
    total_net: total_net,
    markdown: File.basename(out_path)
  )
)

puts "ENGLE_JOURNAL_OK: #{out_path}"
puts "ENGLE_JOURNAL_LATEST: #{latest}"
puts "ENGLE_POSTURE: #{posture_code} (IRM=#{irm[:current] || 'n/a'})"
