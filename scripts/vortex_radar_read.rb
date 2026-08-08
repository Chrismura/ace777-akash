#!/usr/bin/env ruby
# frozen_string_literal: true
# Lit vortex_control.json → variables cycle_radar_* (1 appel / cycle genesis, hot path 64ms)
# Usage: eval "$(ruby scripts/vortex_radar_read.rb runs/vortex_control.json)"
#
# Fail-closed: JSON absent, stale, invalid_v9_json → baseline config_active (ENV) ou profils CHOP.

require "json"
require "time"

path = ARGV[0] || ENV.fetch("VORTEX_CONTROL_FILE", "runs/vortex_control.json")
max_age = (ENV["VORTEX_JSON_MAX_AGE_SEC"] || "90").to_i
max_age = 90 if max_age < 15

PROFILES = {
  "TREND" => {
    beta_conf: 0.22, alpha_conf: 0.20,
    beta_mom: 0.006, alpha_mom: 0.005,
    max_spread: 12.0
  },
  "CHOP" => {
    beta_conf: 0.40, alpha_conf: 0.35,
    beta_mom: 0.015, alpha_mom: 0.012,
    max_spread: 5.0
  }
}.freeze

def clamp(v, lo, hi)
  [[v.to_f, lo].max, hi].min
end

def env_f(key, default)
  v = ENV[key]
  return default if v.nil? || v.to_s.strip.empty?

  Float(v)
rescue StandardError
  default
end

def baseline_from_env
  {
    beta_conf: env_f("RADAR_MIN_CONF_BETA", env_f("RADAR_MIN_CONF", 0.30)),
    alpha_conf: env_f("RADAR_MIN_CONF_ALPHA", env_f("RADAR_MIN_CONF", 0.25)),
    beta_mom: env_f("RADAR_MIN_MOM_BPS_BETA", env_f("RADAR_MIN_MOM_BPS", 0.01)),
    alpha_mom: env_f("RADAR_MIN_MOM_BPS_ALPHA", env_f("RADAR_MIN_MOM_BPS", 0.008)),
    max_spread: env_f("RADAR_MAX_SPREAD_BPS", 8.0)
  }
end

def stale?(j, max_age)
  return false if j["emergency_override"] == true

  ts = j["ts"].to_s
  return true if ts.empty?

  age = Time.now.utc - Time.parse(ts).utc
  age > max_age
rescue StandardError
  true
end

def invalid_json?(j)
  msg = j["message"].to_s
  return true if msg == "invalid_v9_json"

  mode = (j["mode"] || j["regime"]).to_s.upcase
  !%w[TREND CHOP].include?(mode)
end

def build_out(mode, j, source)
  prof = PROFILES.fetch(mode, PROFILES["CHOP"])
  base = baseline_from_env
  fallback = source == "baseline"
  emergency = j["emergency_override"] == true ? 1 : 0
  cohesion = (j["swarm_cohesion"] || 0.618).to_f
  cohesion = [[cohesion, 0.2].max, 1.0].min

  beta_conf = j["radar_min_conf_beta"] || j["radar_min_conf"]
  alpha_conf = j["radar_min_conf_alpha"] || j["radar_min_conf"]
  beta_mom = j["radar_min_mom_bps_beta"] || j["radar_min_mom_bps"]
  alpha_mom = j["radar_min_mom_bps_alpha"] || j["radar_min_mom_bps"]
  max_spread = j["radar_max_spread_bps"]

  if fallback
    beta_conf = base[:beta_conf]
    alpha_conf = base[:alpha_conf]
    beta_mom = base[:beta_mom]
    alpha_mom = base[:alpha_mom]
    max_spread = base[:max_spread]
    mode = "OFF"
  else
    beta_conf ||= prof[:beta_conf]
    alpha_conf ||= prof[:alpha_conf]
    beta_mom ||= prof[:beta_mom]
    alpha_mom ||= prof[:alpha_mom]
    max_spread ||= prof[:max_spread]
  end

  {
    mode: mode,
    source: source,
    emergency: emergency,
    cohesion: cohesion,
    beta_conf: clamp(beta_conf, 0.15, 0.45),
    alpha_conf: clamp(alpha_conf, 0.15, 0.45),
    beta_mom: clamp(beta_mom, 0.003, 0.02),
    alpha_mom: clamp(alpha_mom, 0.003, 0.02),
    max_spread: clamp(max_spread, 4.0, 16.0)
  }
end

def emit(out)
  puts "export cycle_vortex_mode=#{out[:mode]}"
  puts "export cycle_radar_source=#{out[:source]}"
  puts "export cycle_radar_min_conf_beta=#{format('%.8f', out[:beta_conf])}"
  puts "export cycle_radar_min_conf_alpha=#{format('%.8f', out[:alpha_conf])}"
  puts "export cycle_radar_min_mom_beta=#{format('%.8f', out[:beta_mom])}"
  puts "export cycle_radar_min_mom_alpha=#{format('%.8f', out[:alpha_mom])}"
  puts "export cycle_radar_max_spread_bps=#{format('%.8f', out[:max_spread])}"
  puts "export cycle_vortex_emergency_override=#{out[:emergency]}"
  puts "export cycle_swarm_cohesion=#{format('%.6f', out[:cohesion])}"
end

begin
  unless File.file?(path)
    emit(build_out("OFF", {}, "baseline"))
    exit 0
  end

  j = JSON.parse(File.read(path))
  if invalid_json?(j) || stale?(j, max_age)
    emit(build_out("OFF", {}, "baseline"))
    exit 0
  end

  mode = (j["mode"] || j["regime"] || "CHOP").to_s.upcase
  mode = "CHOP" unless %w[TREND CHOP].include?(mode)
  emit(build_out(mode, j, "vortex_json"))
rescue StandardError
  emit(build_out("OFF", {}, "baseline"))
end
