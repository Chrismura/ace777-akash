#!/usr/bin/env ruby
# frozen_string_literal: true
# CORTICAL SHADOW — GLM-5.2 macro layer (Phase C)
# Analyse trajectoires CSV + télémétrie essaim, écrit UNIQUEMENT vortex_control.json.shadow.
# Ne touche PAS vortex_control.json ni swarm_telemetry cohesion live.
#
# Usage:
#   OPENROUTER_API_KEY=sk-... ruby scripts/cortical_supervisor_glm.rb runs/MASTER_*_BETA*.csv
#
# Env:
#   GLM_PROVIDER=openrouter|zai          (default openrouter)
#   GLM_MODEL=z-ai/glm-5.2
#   CORTICAL_SHADOW_FILE=runs/vortex_control.json.shadow
#   CORTICAL_TAIL_LINES=30
#   CORTICAL_LLM_BUDGET_SEC=8.0
#   VORTEX_CONTROL_FILE=runs/vortex_control.json  (lecture référence Qwen live)

require "json"
require "net/http"
require "time"
require "uri"

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

MARKET_PHASES = %w[ACCUMULATION DISTRIBUTION SHOCK].freeze

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
  {
    "mode" => "CHOP",
    "chop_score" => 0.55,
    "message" => "rule_fallback",
    "justification" => "regime_compute_failed"
  }.merge(PROFILES["CHOP"])
end

def trajectory_context(log_path, n)
  return [] unless File.file?(log_path)

  File.readlines(log_path).last(n).map do |ln|
    cols = ln.strip.split(",", -1)
    next unless cols.size >= 11

    {
      "cycle" => cols[1],
      "status" => cols[3],
      "pnl" => cols[8],
      "reason" => cols[9].to_s[0, 40],
      "tension" => cols[10].to_s[/tension=([0-9.]+)/, 1] || "0"
    }
  end.compact
end

def swarm_snapshot(path)
  return {} unless File.file?(path)

  st = JSON.parse(File.read(path))
  {
    "beta" => (st["beta"] || {}).slice("tension", "conf", "direction", "cycle", "last_result", "last_pnl"),
    "alpha" => (st["alpha"] || {}).slice("tension", "conf", "direction", "cycle", "last_result", "last_pnl"),
    "swarm_cohesion_live" => st["swarm_cohesion"],
    "events" => st["events"]
  }
rescue StandardError
  {}
end

def read_live_reference(live_path)
  return {} unless File.file?(live_path)

  j = JSON.parse(File.read(live_path))
  {
    "mode" => j["mode"],
    "swarm_cohesion" => j["swarm_cohesion"],
    "chop_score" => j["chop_score"],
    "ts" => j["ts"],
    "justification" => j["justification"],
    "emergency_override" => j["emergency_override"]
  }
rescue StandardError
  {}
end

def parse_glm_json(raw)
  c = JSON.parse(raw)
  phase = (c["market_phase"] || "ACCUMULATION").to_s.upcase
  phase = "ACCUMULATION" unless MARKET_PHASES.include?(phase)
  mode = (c["mode"] || "CHOP").to_s.upcase
  mode = "CHOP" unless %w[TREND CHOP].include?(mode)
  cohesion = clamp(c["swarm_cohesion"] || 0.618, 0.2, 1.0).round(4)
  just = c["justification"].to_s[0, 120]
  just = "glm_shadow" if just.empty?
  [{ "swarm_cohesion" => cohesion, "mode" => mode, "market_phase" => phase, "justification" => just }, false]
rescue JSON::ParserError
  coh = raw[/swarm_cohesion["\s:]+([0-9.]+)/, 1]
  mod = raw[/mode["\s:]+"([A-Z]+)"/, 1]
  phase = raw[/market_phase["\s:]+"([A-Z]+)"/, 1]
  return [nil, true] if coh.nil?

  phase = (phase || "ACCUMULATION").upcase
  phase = "ACCUMULATION" unless MARKET_PHASES.include?(phase)
  mode = (mod || "CHOP").upcase
  mode = "CHOP" unless %w[TREND CHOP].include?(mode)
  [{
    "swarm_cohesion" => clamp(coh, 0.2, 1.0).round(4),
    "mode" => mode,
    "market_phase" => phase,
    "justification" => "partial_parse"
  }, true]
end

def http_post_json(uri, headers, body, open_timeout:, read_timeout:)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = uri.scheme == "https"
  http.open_timeout = open_timeout
  http.read_timeout = read_timeout
  req = Net::HTTP::Post.new(uri)
  headers.each { |k, v| req[k] = v }
  req.body = body.to_json
  res = http.request(req)
  [res, nil]
rescue StandardError => e
  [nil, e]
end

def extract_chat_content(res_body)
  j = JSON.parse(res_body)
  j.dig("choices", 0, "message", "content").to_s
rescue StandardError
  ""
end

def glm_openrouter(model, system, user, budget_sec, api_key)
  uri = URI("https://openrouter.ai/api/v1/chat/completions")
  body = {
    model: model,
    messages: [
      { role: "system", content: system },
      { role: "user", content: user }
    ],
    temperature: 0,
    max_tokens: 120,
    response_format: { type: "json_object" }
  }
  headers = {
    "Authorization" => "Bearer #{api_key}",
    "Content-Type" => "application/json",
    "HTTP-Referer" => ENV.fetch("OPENROUTER_HTTP_REFERER", "https://ace777.local"),
    "X-Title" => ENV.fetch("OPENROUTER_X_TITLE", "ACE777 Cortical Shadow")
  }
  started = Time.now
  res, err = http_post_json(uri, headers, body, open_timeout: 2, read_timeout: budget_sec)
  elapsed = Time.now - started
  return [nil, elapsed, err ? err.class.name : "http_fail"] if res.nil? || !res.is_a?(Net::HTTPSuccess)

  txt = extract_chat_content(res.body)
  parsed, partial = parse_glm_json(txt)
  return [nil, elapsed, "parse_fail"] if parsed.nil?

  tag = elapsed > budget_sec ? "slow" : "ok"
  tag = "partial" if partial
  [parsed, elapsed, tag]
end

def glm_zai(model, system, user, budget_sec, api_key)
  uri = URI(ENV.fetch("ZAI_API_URL", "https://api.z.ai/api/coding/paas/v4/chat/completions"))
  body = {
    model: model,
    messages: [
      { role: "system", content: system },
      { role: "user", content: user }
    ],
    temperature: 0,
    max_tokens: 120,
    response_format: { type: "json_object" }
  }
  headers = {
    "Authorization" => "Bearer #{api_key}",
    "Content-Type" => "application/json"
  }
  started = Time.now
  res, err = http_post_json(uri, headers, body, open_timeout: 2, read_timeout: budget_sec)
  elapsed = Time.now - started
  return [nil, elapsed, err ? err.class.name : "http_fail"] if res.nil? || !res.is_a?(Net::HTTPSuccess)

  txt = extract_chat_content(res.body)
  parsed, partial = parse_glm_json(txt)
  return [nil, elapsed, "parse_fail"] if parsed.nil?

  tag = elapsed > budget_sec ? "slow" : "ok"
  tag = "partial" if partial
  [parsed, elapsed, tag]
end

def glm_infer(provider, model, system, user, budget_sec)
  case provider
  when "zai"
    key = ENV["ZAI_API_KEY"].to_s
    return [nil, 0.0, "missing_zai_key"] if key.empty?

    glm_zai(model, system, user, budget_sec, key)
  else
    key = ENV["OPENROUTER_API_KEY"].to_s
    return [nil, 0.0, "missing_openrouter_key"] if key.empty?

    glm_openrouter(model, system, user, budget_sec, key)
  end
end

log_path = ARGV[0] || ENV.fetch("LOG_BETA", "runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv")
log_alpha = ENV["LOG_ALPHA"]
if log_alpha.to_s.strip.empty?
  log_alpha = log_path.sub("_BETA", "_ALPHA").sub("BETA_", "ALPHA_")
  log_alpha = log_path unless File.file?(log_alpha)
end

shadow_path = ENV.fetch("CORTICAL_SHADOW_FILE", "runs/vortex_control.json.shadow")
live_path = ENV.fetch("VORTEX_CONTROL_FILE", "runs/vortex_control.json")
telemetry_path = ENV.fetch("SWARM_TELEMETRY_FILE", "runs/swarm_telemetry.json")
tail_lines = (ENV["CORTICAL_TAIL_LINES"] || "30").to_i
budget_sec = (ENV["CORTICAL_LLM_BUDGET_SEC"] || "8.0").to_f
provider = ENV.fetch("GLM_PROVIDER", "openrouter").downcase
model = ENV.fetch("GLM_MODEL", "z-ai/glm-5.2")

rule = rule_regime_json(log_path)
mode = (rule["mode"] || "CHOP").to_s.upcase
mode = "CHOP" unless %w[TREND CHOP].include?(mode)
rule_chop = rule["chop_score"].to_f
default_cohesion = clamp(1.0 - rule_chop, 0.3, 0.95).round(4)

beta_traj = trajectory_context(log_path, tail_lines)
alpha_traj = File.file?(log_alpha) ? trajectory_context(log_alpha, tail_lines) : []
swarm = swarm_snapshot(telemetry_path)
live_ref = read_live_reference(live_path)

system_prompt = <<~SYS.gsub(/\s+/, " ").strip
  You are the cortical macro layer of a crypto scalping swarm (BETA scout + ALPHA hunter).
  Reply with JSON only, no markdown. Schema:
  {"swarm_cohesion":0.2-1.0,"mode":"TREND"|"CHOP","market_phase":"ACCUMULATION"|"DISTRIBUTION"|"SHOCK","justification":"max 80 chars"}
  market_phase is observational only. Prefer conservative cohesion in CHOP/SHOCK.
SYS

user_prompt = {
  "rule_regime" => rule.slice("mode", "chop_score", "trend_bps_15m", "range_bps", "confiance_structure"),
  "live_qwen_reference" => live_ref,
  "swarm_telemetry" => swarm,
  "beta_trajectory_last_n" => beta_traj,
  "alpha_trajectory_last_n" => alpha_traj
}.to_json

llm, llm_elapsed, llm_tag = glm_infer(provider, model, system_prompt, user_prompt, budget_sec)
api_ok = !llm.nil?

if llm
  cohesion = llm["swarm_cohesion"]
  mode = llm["mode"]
  market_phase = llm["market_phase"]
  justification = llm["justification"]
  shadow_status = "ok"
  shadow_status = "slow_ok" if llm_tag == "slow" || llm_tag == "slow_ok"
  shadow_status = "partial_ok" if llm_tag == "partial"
  message = "shadow_glm_#{mode.downcase}_#{market_phase.downcase}"
else
  cohesion = default_cohesion
  market_phase = rule_chop > 0.55 ? "SHOCK" : (mode == "TREND" ? "ACCUMULATION" : "DISTRIBUTION")
  justification = "shadow_fallback_#{llm_tag}"
  shadow_status = "fallback"
  message = "shadow_rule_fallback_#{mode.downcase}"
end

metrics = PROFILES[mode].merge("swarm_cohesion" => cohesion)
out = apply_clamps(metrics).merge(
  "mode" => mode,
  "chop_score" => rule["chop_score"],
  "trend_bps_15m" => rule["trend_bps_15m"],
  "range_bps" => rule["range_bps"],
  "confiance_structure" => rule["confiance_structure"],
  "swarm_cohesion" => cohesion,
  "market_phase" => market_phase,
  "message" => message,
  "ts" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
  "justification" => justification,
  "emergency_override" => false,
  "llm_elapsed_sec" => llm_elapsed.round(3),
  "shadow" => true,
  "shadow_status" => shadow_status,
  "engine" => model,
  "provider" => provider,
  "api_ok" => api_ok,
  "reference_live" => live_ref,
  "trajectory_lines" => beta_traj.size + alpha_traj.size
)

tmp = "#{shadow_path}.tmp"
File.write(tmp, JSON.pretty_generate(out))
File.rename(tmp, shadow_path)
puts JSON.generate(out)
