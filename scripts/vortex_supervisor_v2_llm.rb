#!/usr/bin/env ruby
# frozen_string_literal: true
# MACRO Vortex v2 — 15-20s async supervisor
# 1) chop_score_v2 + hystérésis 0.65 / 0.45 (rule-based mode)
# 2) Qwen 1.5B via Ollama (format JSON, num_predict 30, budget 1.0s)
# 3) emergency_override si LLM > 1.5s ou échec (hot path bypass micro LLM gate)
# 4) Écrit runs/vortex_control.json (structure stricte v2)
#
# Usage: ruby scripts/vortex_supervisor_v2_llm.rb LOG_BETA.csv

require "json"
require "net/http"
require "time"
require "uri"

log_path = ARGV[0] || ENV.fetch("LOG_BETA", "runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv")
control_path = ENV.fetch("VORTEX_CONTROL_FILE", "runs/vortex_control.json")
ollama_url = ENV.fetch("LLM_OLLAMA_URL", "http://127.0.0.1:11434")
model = ENV.fetch("SUPERVISOR_MODEL", ENV.fetch("LLM_MODEL", "qwen2.5-coder:1.5b"))
max_predict = (ENV["VORTEX_LLM_MAX_PREDICT"] || "45").to_i
llm_budget_sec = (ENV["VORTEX_LLM_BUDGET_SEC"] || "1.2").to_f
tail_lines = (ENV["SUPERVISOR_TAIL_LINES"] || "15").to_i
ollama_threads = (ENV["OLLAMA_NUM_THREAD"] || "4").to_i

PROFILES = {
  "TREND" => {
    "radar_min_conf_beta" => 0.22, "radar_min_conf_alpha" => 0.20,
    "radar_min_mom_bps_beta" => 0.006, "radar_min_mom_bps_alpha" => 0.005,
    "radar_max_spread_bps" => 12.0
  },
  "CHOP" => {
    "radar_min_conf_beta" => 0.40, "radar_min_conf_alpha" => 0.35,
    "radar_min_mom_bps_beta" => 0.015, "radar_min_mom_bps_alpha" => 0.012,
    "radar_max_spread_bps" => 5.0
  }
}.freeze

def clamp(v, lo, hi)
  [[v.to_f, lo].max, hi].min
end

def apply_clamps(h)
  {
    "radar_min_conf_beta" => clamp(h["radar_min_conf_beta"], 0.15, 0.45).round(4),
    "radar_min_conf_alpha" => clamp(h["radar_min_conf_alpha"], 0.15, 0.45).round(4),
    "radar_min_mom_bps_beta" => clamp(h["radar_min_mom_bps_beta"], 0.003, 0.02).round(4),
    "radar_min_mom_bps_alpha" => clamp(h["radar_min_mom_bps_alpha"], 0.003, 0.02).round(4),
    "radar_max_spread_bps" => clamp(h["radar_max_spread_bps"], 4.0, 16.0).round(2)
  }
end

def rule_regime_json(log_path)
  raw = `ruby "#{File.expand_path("vortex_regime_compute.rb", __dir__)}" "#{log_path}" 2>/dev/null`
  JSON.parse(raw)
rescue StandardError
  prof = PROFILES["CHOP"]
  {
    "mode" => "CHOP",
    "chop_score" => 0.55,
    "message" => "rule_fallback",
    "justification" => "regime_compute_failed"
  }.merge(prof)
end

def ollama_fast_options(max_predict, num_thread)
  {
    num_predict: max_predict,
    temperature: 0.0,
    top_p: 1.0,
    num_thread: num_thread
  }
end

def tail_context(log_path, n = 15)
  return "no_data" unless File.file?(log_path)

  File.readlines(log_path).last(n).map do |ln|
    cols = ln.strip.split(",", -1)
    next unless cols.size >= 10

    ten = cols[10].to_s[/tension=([0-9.]+)/, 1] || "0"
    "c=#{cols[1]} #{cols[3]} pnl=#{cols[8]} ten=#{ten}"
  end.compact.join(" | ")
end

def parse_cohesion_response(raw, default_cohesion, fallback_mode)
  c = JSON.parse(raw)
  [c, false]
rescue JSON::ParserError
  coh = raw[/swarm_cohesion["\s:]+([0-9.]+)/, 1]
  mod = raw[/mode["\s:]+"([A-Z]+)"/, 1]
  return [nil, true] if coh.nil?
  [{ "swarm_cohesion" => coh.to_f, "mode" => (mod || fallback_mode), "justification" => "partial" }, true]
end

def ollama_cohesion(mode, context, budget_sec, ollama_url, model, max_predict, default_cohesion, num_thread)
  prompt = "{\"swarm_cohesion\":0.5,\"mode\":\"#{mode}\"}"

  uri = URI("#{ollama_url}/api/generate")
  body = {
    model: model,
    prompt: prompt,
    stream: false,
    format: "json",
    options: ollama_fast_options(max_predict, num_thread)
  }
  started = Time.now
  http = Net::HTTP.new(uri.host, uri.port)
  # ADDITIF pont-hub (12/08) : délais configurables par ENV, défauts = valeurs historiques
  http.open_timeout = (ENV["VORTEX_LLM_OPEN_TIMEOUT"] || "1").to_f
  http.read_timeout = (ENV["VORTEX_LLM_READ_TIMEOUT"] || "2.0").to_f
  res = http.post(uri.path, body.to_json, "Content-Type" => "application/json")
  elapsed = Time.now - started
  return [nil, elapsed, "http_fail"] unless res.is_a?(Net::HTTPSuccess)

  txt = JSON.parse(res.body)["response"].to_s
  c, partial = parse_cohesion_response(txt, default_cohesion, mode)
  return [nil, elapsed, "parse_fail"] if c.nil?

  cohesion = clamp(c["swarm_cohesion"] || default_cohesion, 0.2, 1.0)
  m = (c["mode"] || mode).to_s.upcase
  m = mode unless %w[TREND CHOP].include?(m)
  just = partial ? "partial_parse" : "llm_wind"
  tag = elapsed > budget_sec ? "slow" : "ok"
  [{ "swarm_cohesion" => cohesion.round(4), "mode" => m, "justification" => just }, elapsed, tag]
rescue StandardError => e
  elapsed = Time.now - (started rescue Time.now)
  [nil, elapsed, e.class.name]
end

def ollama_radar(mode, prof, context, budget_sec, ollama_url, model, max_predict, num_thread)
  started = Time.now
  prompt = "JSON only mode+radar clamps.rule=#{mode} ctx:#{context}"

  uri = URI("#{ollama_url}/api/generate")
  body = {
    model: model,
    prompt: prompt,
    stream: false,
    format: "json",
    options: ollama_fast_options(max_predict, num_thread)
  }
  http = Net::HTTP.new(uri.host, uri.port)
  # ADDITIF pont-hub (12/08) : délais configurables par ENV, défauts = valeurs historiques
  http.open_timeout = (ENV["VORTEX_LLM_OPEN_TIMEOUT"] || "1").to_f
  http.read_timeout = (ENV["VORTEX_LLM_READ_TIMEOUT"] || "2.0").to_f
  res = http.post(uri.path, body.to_json, "Content-Type" => "application/json")
  elapsed = Time.now - started
  return [nil, elapsed, "http_fail"] unless res.is_a?(Net::HTTPSuccess)

  txt = JSON.parse(res.body)["response"].to_s
  c = JSON.parse(txt)
  m = (c["mode"] || mode).to_s.upcase
  m = mode unless %w[TREND CHOP].include?(m)
  merged = prof.merge(
    "mode" => m,
    "radar_min_conf_beta" => c["radar_min_conf_beta"] || prof["radar_min_conf_beta"],
    "radar_min_conf_alpha" => c["radar_min_conf_alpha"] || prof["radar_min_conf_alpha"],
    "radar_min_mom_bps_beta" => c["radar_min_mom_bps_beta"] || prof["radar_min_mom_bps_beta"],
    "radar_min_mom_bps_alpha" => c["radar_min_mom_bps_alpha"] || prof["radar_min_mom_bps_alpha"],
    "radar_max_spread_bps" => c["radar_max_spread_bps"] || prof["radar_max_spread_bps"],
    "justification" => c["justification"].to_s[0, 120]
  )
  tag = elapsed > budget_sec ? "slow_ok" : "ok"
  [apply_clamps(merged), elapsed, tag]
rescue StandardError
  elapsed = Time.now - started
  [nil, elapsed, "error"]
end

rule = rule_regime_json(log_path)
mode = (rule["mode"] || "CHOP").to_s.upcase
mode = "CHOP" unless %w[TREND CHOP].include?(mode)
base = PROFILES[mode].merge(
  "mode" => mode,
  "chop_score" => rule["chop_score"],
  "trend_bps_15m" => rule["trend_bps_15m"],
  "range_bps" => rule["range_bps"],
  "confiance_structure" => rule["confiance_structure"]
)

ctx = tail_context(log_path, tail_lines)
macro_only = ENV.fetch("SWARM_LLM_MACRO_ONLY", "TRUE") == "TRUE"
rule_chop = rule["chop_score"].to_f
default_cohesion = clamp(1.0 - rule_chop, 0.3, 0.95)

# === JUGE ÉCLAIRÉ (24/08, SPEC_JUGE_ECLAIRE_20260824) : verrou anti-doublon + appel sur événement ===
# ATTENTION (25/08, découvert au test) : `rule_regime_json` appelle en interne
# `vortex_regime_compute.rb` qui RÉÉCRIT vortex_control.json (le fichier lu par le
# moteur) avant notre lecture → on ne peut pas s'en servir comme mémoire de la
# dernière décision LLM (toujours frais, sans swarm_cohesion). On mémorise donc la
# décision dans un fichier DÉDIÉ jamais écrasé par le compute : vortex_llm_last.json.
# - Verrou fichier (flock): si un autre superviseur tient le verrou, PAS d'appel
#   hub (on réutilise la dernière décision écrite) — plus jamais de doublon qui
#   martèle le hub quand plusieurs moteurs tournent (cas du 24/08 : 4 426 appels).
# - Événementiel : pas d'appel réseau si la décision existante est fraîche (< 30 s)
#   ET que chop_score n'a pas bougé (>= 0.06) ni le mode changé — le moteur relit
#   la même décision à 0 ms. Le format écrit dans vortex_control.json reste le même (v2).
llm_last_path = ENV.fetch("VORTEX_LLM_LAST_FILE", "runs/vortex_llm_last.json")
precedent = nil
begin
  precedent = JSON.parse(File.read(llm_last_path)) if File.file?(llm_last_path)
rescue StandardError
  precedent = nil
end

call_llm = true
if precedent && precedent["ts"]
  begin
    age = Time.now.to_f - Time.parse(precedent["ts"].to_s).to_f
    delta_chop = (precedent["chop_score"].to_f - rule["chop_score"].to_f).abs
    meme_mode = (precedent["mode"] || "").to_s.upcase == mode
    stable = age <= (ENV["VORTEX_LLM_MAX_AGE_S"] || "30").to_f && delta_chop < 0.06 && meme_mode
    call_llm = !stable
  rescue StandardError
    call_llm = true
  end
end

lock_fh = nil
begin
  lock_path_var = ENV.fetch("VORTEX_LLM_LOCK", "runs/vortex_llm.lock")
  lock_fh = File.open(lock_path_var, File::RDWR | File::CREAT, 0o644)
  lock_prend = lock_fh.flock(File::LOCK_EX | File::LOCK_NB)
  # flock retourne 0 (succes) ou false (LOCK_NB) — normaliser en booleen pour
  # que call_llm reste true/false (sinon il devient 0, truthy mais trompeur).
  call_llm &&= (lock_prend != false)
rescue StandardError
  # jamais bloquant : si le verrou est impossible, on garde le comportement historique
  call_llm = true
  lock_fh = nil
end
if ENV["JUGE_DEBUG"] == "1"
  begin
    age_db = precedent && precedent["ts"] ? (Time.now.to_f - Time.parse(precedent["ts"].to_s).to_f).round(1) : "n/a"
  rescue StandardError => e_db
    age_db = "err:#{e_db.class}"
  end
  STDERR.puts "[debug-juge] call_llm=#{call_llm} last=#{llm_last_path} ts=#{precedent ? precedent["ts"].to_s : "nil"} age=#{age_db} coh=#{precedent ? precedent["swarm_cohesion"].to_s : "nil"}"
end

if macro_only
  if call_llm
    llm, llm_elapsed, llm_tag = ollama_cohesion(
      mode, ctx, llm_budget_sec, ollama_url, model, max_predict, default_cohesion, ollama_threads
    )
  else
    # Événementiel : aucune consultation réseau, on réutilise la décision écrite.
    llm = nil
    llm_elapsed = 0.0
    llm_tag = "reuse"
    if precedent && precedent["swarm_cohesion"]
      llm = { "swarm_cohesion" => precedent["swarm_cohesion"],
               "mode" => precedent["mode"] || mode,
               "justification" => "reuse_fraiche" }
    end
  end
  emergency_override = llm.nil? || llm_elapsed > llm_budget_sec
  cohesion = llm ? llm["swarm_cohesion"] : default_cohesion
  mode = llm ? llm["mode"] : mode
  if llm && !emergency_override
    justification = llm["justification"].to_s
    justification = "llm_wind_#{mode.downcase}" if justification.empty?
  elsif llm
    justification = "llm_slow_#{llm_tag}"
  else
    justification = "llm_fail_#{llm_tag}_#{mode.downcase}"
  end
  metrics = PROFILES[mode].merge("swarm_cohesion" => cohesion)
else
  if call_llm
    llm, llm_elapsed, llm_tag = ollama_radar(
      mode, base, ctx, llm_budget_sec, ollama_url, model, max_predict, ollama_threads
    )
  else
    llm = nil
    llm_elapsed = 0.0
    llm_tag = "reuse"
    if precedent && precedent["swarm_cohesion"]
      llm = { "swarm_cohesion" => precedent["swarm_cohesion"],
               "mode" => precedent["mode"] || mode,
               "justification" => "reuse_fraiche" }
    end
  end
  emergency_override = llm.nil? || llm_elapsed > llm_budget_sec
  justification = "rule_#{mode.downcase}"
  metrics = base
  if llm
    metrics = base.merge(llm)
    justification = llm["justification"].to_s
    justification = "llm_#{mode.downcase}" if justification.empty?
    justification = "#{justification}_#{llm_tag}" if emergency_override
  else
    justification = "llm_fail_rule_#{mode.downcase}"
  end
  cohesion = default_cohesion
end

out = apply_clamps(metrics).merge(
  "mode" => mode,
  "chop_score" => rule["chop_score"],
  "trend_bps_15m" => rule["trend_bps_15m"],
  "range_bps" => rule["range_bps"],
  "confiance_structure" => rule["confiance_structure"],
  "swarm_cohesion" => cohesion,
  "message" => emergency_override ? "v2_emergency_rule_#{mode.downcase}" : (macro_only ? "v2_swarm_wind_#{mode.downcase}" : "v2_llm_#{mode.downcase}"),
  "ts" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
  "justification" => justification,
  "emergency_override" => emergency_override,
  "llm_elapsed_sec" => llm_elapsed.round(3)
)

lock_fh.close if lock_fh  # libère le verrou (flock) après l'écriture

# Mémoire de la décision LLM (pour l'événementiel) : fichier dédié, jamais écrasé
# par le compute. Le moteur, lui, lit toujours vortex_control.json (contrat v2).
begin
  llm_tmp = "#{llm_last_path}.tmp"
  File.write(llm_tmp, JSON.generate({
    "mode" => mode, "chop_score" => rule["chop_score"],
    "swarm_cohesion" => cohesion, "justification" => justification,
    "ts" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
  }))
  File.rename(llm_tmp, llm_last_path)
rescue StandardError
  # jamais fatal : le long last est une optimisation, pas un contrat
end

tmp = "#{control_path}.tmp"
File.write(tmp, JSON.pretty_generate(out))
File.rename(tmp, control_path)
`ruby "#{File.expand_path("swarm_telemetry.rb", __dir__)}" set_cohesion --value #{cohesion} 2>/dev/null`
puts JSON.generate(out)
