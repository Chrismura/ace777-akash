#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8

require "json"
require "time"
require "fileutils"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

root = File.expand_path("..", __dir__)
run_dir = File.expand_path(ENV.fetch("RUN_DIR", "runs"), root)
tag = ENV["STATE_TAG"] || ENV["TEST_TAG_OVERRIDE"]
unless tag
  latest_beta = Dir.glob(File.join(run_dir, "*_BETA_X5.csv")).max_by { |f| File.mtime(f) }
  if latest_beta
    tag = File.basename(latest_beta).sub(/_BETA_X5\.csv\z/, "")
  else
    tag = "MASTER_BASE_V8_5_IMPACT_4H"
  end
end
phase = ENV.fetch("STATE_PHASE", "unknown")
out_path = File.join(run_dir, "STATE.md")

beta_csv = ENV["BETA_CSV"] || File.join(run_dir, "#{tag}_BETA_X5.csv")
alpha_csv = ENV["ALPHA_CSV"] || File.join(run_dir, "#{tag}_ALPHA_X13_BURST13.csv")
def read_json(path)
  return {} unless File.file?(path)

  JSON.parse(File.read(path))
rescue StandardError
  {}
end

run_meta = read_json(File.join(run_dir, "#{tag}_run_meta.json"))
sidecars = Dir.glob(File.join(run_dir, "#{tag}_*_session.json")).sort_by { |path| File.mtime(path) }
sidecar = sidecars.empty? ? {} : read_json(sidecars.last)
run_id = sidecar["run_id"] || run_meta["run_id"] || run_meta["runId"] || tag
fee_reconciliation = sidecar["fee_reconciliation"] || run_meta["fee_reconciliation"] || "UNMATCHED_BINANCE_FEES"

def load_session_start(run_dir, tag)
  return ENV["RUN_START_UTC"] if ENV["RUN_START_UTC"] && !ENV["RUN_START_UTC"].empty?

  meta_path = File.join(run_dir, "#{tag}_run_meta.json")
  return nil unless File.file?(meta_path)

  JSON.parse(File.read(meta_path))["start_utc"]
rescue StandardError
  nil
end

session_start = load_session_start(run_dir, tag)

def read_json(path)
  return {} unless File.file?(path)

  JSON.parse(File.read(path))
rescue StandardError
  {}
end

def csv_stats(path, min_ts: nil)
  stats = {
    filled: 0, wins: 0, losses: 0, flats: 0, gross: 0.0, fees: 0.0, net: 0.0,
    skips: 0, skip_reasons: Hash.new(0),
    last_ts: nil, last_filled: nil
  }
  return stats unless File.file?(path)

  File.foreach(path).with_index do |line, idx|
    next if idx.zero?

    cols = line.strip.split(",", -1)
    next if cols.size < 10

    ts, _cycle, side, status, entry, exit_px, _qty, _bps, pnl, fee_usdt, pnl_net, reason = cols
    next if min_ts && ts && !ts.empty? && ts < min_ts

    stats[:last_ts] = ts if ts && !ts.empty?

    if status == "SKIPPED" || side == "SKIP"
      stats[:skips] += 1
      key = reason.to_s.empty? ? "unknown" : reason.split(",", 2).first
      stats[:skip_reasons][key] += 1
      next
    end

    next unless status == "FILLED"

    pnl_f = pnl.to_f
    # feeUsdt and pnlNet are per-fill only when both fields are present.
    # Missing fields mean legacy gross-only data; do not invent fees.
    has_net_fields = !fee_usdt.to_s.empty? && !pnl_net.to_s.empty?
    fee_f = has_net_fields ? fee_usdt.to_f : 0.0
    net_f = has_net_fields ? pnl_net.to_f : pnl_f
    stats[:filled] += 1
    stats[:gross] += pnl_f
    stats[:fees] += fee_f
    stats[:net] += net_f
    stats[:wins] += 1 if net_f > 0
    stats[:losses] += 1 if net_f < 0
    stats[:flats] += 1 if net_f == 0
    stats[:last_filled] = {
      ts: ts, side: side, entry: entry, exit: exit_px,
      pnl: net_f, gross: pnl_f, fee: fee_f, reason: reason
    }
  end
  stats
end

def top_skips(skip_reasons, n = 5)
  skip_reasons.sort_by { |_, v| -v }.first(n)
end

def winrate(filled, wins)
  return "0.00" if filled.zero?

  format("%.1f", (wins.to_f / filled) * 100.0)
end

def running?(pid_file)
  return false unless File.file?(pid_file)

  pid = File.read(pid_file).strip.to_i
  return false if pid <= 0

  Process.kill(0, pid)
  true
rescue Errno::ESRCH, Errno::EPERM
  false
end

def latest_erreur_ai(root)
  dir = File.join(root, "ERREURS_AI")
  return nil unless File.directory?(dir)

  files = Dir.glob(File.join(dir, "*.md")).max_by { |f| File.mtime(f) }
  return nil unless files

  base = File.basename(files)
  first_line = File.readlines(files, encoding: "UTF-8").find { |l| l.strip.start_with?("#") }&.strip
  first_line = first_line&.encode("UTF-8", invalid: :replace, undef: :replace) || base
  { file: base, title: first_line }
end

beta = csv_stats(beta_csv, min_ts: session_start)
alpha = csv_stats(alpha_csv, min_ts: session_start)
total_net = beta[:net] + alpha[:net]
total_filled = beta[:filled] + alpha[:filled]

duo_state = read_json(File.join(run_dir, "duo_state.json"))
duo_session = read_json(File.join(run_dir, "duo_session.json"))
vortex = read_json(File.join(run_dir, "vortex_control.json"))

master_running = running?(File.join(run_dir, "master.pid"))
beta_running = running?(File.join(run_dir, "beta.pid"))
alpha_running = running?(File.join(run_dir, "alpha.pid"))

# Phase explicite prioritaire (sinon master.pid encore présent en fin de run → faux RUNNING)
run_status = if phase == "ended"
               "ENDED"
             elsif phase == "stopped"
               "STOPPED"
             elsif master_running || beta_running || alpha_running
               "RUNNING"
             else
               "IDLE"
             end

config_name = ENV["ACE777_CONFIG_NAME"] || "non_charge"
config_version = ENV["ACE777_CONFIG_VERSION"] || "?"
llm_enabled = ENV.fetch("LLM_GATE_ENABLED", "?")
llm_fail_closed = ENV.fetch("LLM_GATE_FAIL_CLOSED", "?")
buy_beta = ENV.fetch("BUY_USDT_BETA", "?")
buy_alpha = ENV.fetch("BUY_USDT_ALPHA", "?")

now = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
erreur = latest_erreur_ai(root)

lines = []
lines << "# ACE777 — STATE"
lines << ""
lines << "> Généré automatiquement — ne pas éditer à la main"
lines << "> Phase: `#{phase}` | Statut: `#{run_status}` | MAJ: `#{now}`"
lines << ""
lines << "## Config active"
lines << ""
lines << "| Paramètre | Valeur |"
lines << "|-----------|--------|"
lines << "| Profil | `#{config_name}` v`#{config_version}` |"
lines << "| Masse BETA / ALPHA | `#{buy_beta}` / `#{buy_alpha}` USDT |"
lines << "| LLM gate | enabled=`#{llm_enabled}` fail_closed=`#{llm_fail_closed}` |"
lines << "| Modèle LLM | `#{ENV.fetch("LLM_MODEL", "?")}` |"
lines << "| Tag session | `#{tag}` |"
lines << "| run_id | `#{run_id}` |"
lines << "| Frais Binance | `#{fee_reconciliation}` |"
lines << ""
lines << "## PnL session"
lines << ""
lines << "| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |"
lines << "|-------|--------|-----|------|------|------|------|----------|------|"
lines << "| BETA | #{beta[:filled]} | #{beta[:wins]} | #{beta[:losses]} | #{winrate(beta[:filled], beta[:wins])}% | #{format('%.4f', beta[:gross])} | #{format('%.4f', beta[:fees])} | #{format('%.4f', beta[:net])} | #{beta[:skips]} |"
lines << "| ALPHA | #{alpha[:filled]} | #{alpha[:wins]} | #{alpha[:losses]} | #{winrate(alpha[:filled], alpha[:wins])}% | #{format('%.4f', alpha[:gross])} | #{format('%.4f', alpha[:fees])} | #{format('%.4f', alpha[:net])} | #{alpha[:skips]} |"
lines << "| **TOTAL** | **#{total_filled}** | — | — | — | **#{format('%.4f', beta[:gross] + alpha[:gross])}** | **#{format('%.4f', beta[:fees] + alpha[:fees])}** | **#{format('%.4f', total_net)}** | **#{beta[:skips] + alpha[:skips]}** |"
lines << ""

if duo_session.any?
  roles = duo_session["roles"] || {}
  lines << "## Duo session (`duo_session.json`)"
  lines << ""
  lines << "- SCOUT PnL: `#{roles['scout']}` USDT"
  lines << "- HUNTER PnL: `#{roles['hunter']}` USDT"
  lines << "- Total session: `#{duo_session['total_pnl']}` USDT"
  lines << ""
end

if duo_state.any?
  lines << "## Duo live (`duo_state.json`)"
  lines << ""
  lines << "| Champ | Valeur |"
  lines << "|-------|--------|"
  %w[role status side bps pnl_usdt reason cycle hold_sec].each do |k|
    lines << "| #{k} | `#{duo_state[k]}` |" if duo_state.key?(k)
  end
  lines << ""
end

lines << "## Top SKIP — BETA"
lines << ""
if beta[:skip_reasons].empty?
  lines << "_Aucun SKIP ou CSV absent._"
else
  top_skips(beta[:skip_reasons]).each_with_index do |(reason, count), i|
    lines << "#{i + 1}. `#{reason}` — #{count}"
  end
end
lines << ""
lines << "## Top SKIP — ALPHA"
lines << ""
if alpha[:skip_reasons].empty?
  lines << "_Aucun SKIP ou CSV absent._"
else
  top_skips(alpha[:skip_reasons]).each_with_index do |(reason, count), i|
    lines << "#{i + 1}. `#{reason}` — #{count}"
  end
end
lines << ""

if vortex.any?
  lines << "## Vortex (`vortex_control.json`)"
  lines << ""
  lines << "- Mode: `#{vortex['mode']}`"
  lines << "- Message: `#{vortex['message']}`"
  lines << "- TS: `#{vortex['ts']}`"
  lines << ""
end

lines << "## Processus"
lines << ""
lines << "- master.pid: `#{master_running ? 'RUNNING' : 'stopped'}`"
lines << "- beta.pid: `#{beta_running ? 'RUNNING' : 'stopped'}`"
lines << "- alpha.pid: `#{alpha_running ? 'RUNNING' : 'stopped'}`"
lines << ""
lines << "## Fichiers"
lines << ""
lines << "- BETA CSV: `#{File.basename(beta_csv)}` #{File.file?(beta_csv) ? '(ok)' : '(absent)'}"
lines << "- ALPHA CSV: `#{File.basename(alpha_csv)}` #{File.file?(alpha_csv) ? '(ok)' : '(absent)'}"
lines << ""

if erreur
  lines << "## Dernière leçon ERREURS_AI"
  lines << ""
  lines << "- Fichier: `#{erreur[:file]}`"
  lines << "- Titre: #{erreur[:title]}"
  lines << ""
end

lines << "---"
lines << "_Généré par `scripts/update_state_md.sh`_"

FileUtils.mkdir_p(run_dir)
File.write(out_path, lines.join("\n") + "\n")
puts "STATE_OK: #{out_path} (#{run_status} #{phase})"
