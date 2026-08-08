#!/usr/bin/env ruby
# frozen_string_literal: true
# Télémétrie essaim BETA/ALPHA — fichier volatile partagé (2 processus genesis)
# Usage:
#   ruby scripts/swarm_telemetry.rb write --agent beta --tension 1.2 --conf 0.3 --direction long --cycle 5 --mom 0.01 --result active
#   ruby scripts/swarm_telemetry.rb read --agent alpha --cycle 5
#   ruby scripts/swarm_telemetry.rb shockwave --from beta --cycle 100 --duration 10
#   ruby scripts/swarm_telemetry.rb velocity_pulse --target alpha --duration_ms 3000
#   ruby scripts/swarm_telemetry.rb resync --cycle 400 --gap_sec 152

require "json"
require "fileutils"
require "optparse"
require "time"

PATH = ENV.fetch("SWARM_TELEMETRY_FILE", "runs/swarm_telemetry.json")
VELOCITY_TENSION = (ENV["SWARM_VELOCITY_TENSION_THRESHOLD"] || "1.5").to_f
VELOCITY_MS = (ENV["SWARM_VELOCITY_BOOST_MS"] || "3000").to_i

def agent_empty
  {
    "ts_ms" => 0, "tension" => 0.0, "conf" => 0.0, "direction" => "neutral",
    "mom_bps" => 0.0, "cycle" => 0, "last_result" => "idle", "last_pnl" => 0.0
  }
end

def default_state
  {
    "beta" => agent_empty,
    "alpha" => agent_empty,
    "events" => {
      "alpha_velocity_until_ms" => 0,
      "beta_velocity_until_ms" => 0,
      "alpha_shockwave_until_cycle" => 0,
      "beta_shockwave_until_cycle" => 0
    },
    "swarm_cohesion" => 0.618,
    "updated_at" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
  }
end

def load_state
  return default_state unless File.file?(PATH)

  JSON.parse(File.read(PATH))
rescue StandardError
  default_state
end

def with_file_lock
  FileUtils.mkdir_p(File.dirname(PATH))
  File.open("#{PATH}.lock", File::RDWR | File::CREAT, 0o644) do |lf|
    lf.flock(File::LOCK_EX)
    yield
  end
end

# A1: tmp unique par PID (évite collision BETA/ALPHA sur le même .tmp)
# + flock sur read-modify-write (évite lost update sous shockwave concurrent)
def atomic_write(obj)
  obj["updated_at"] = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
  FileUtils.mkdir_p(File.dirname(PATH))
  tmp = "#{PATH}.tmp.#{$$}"
  begin
    File.write(tmp, JSON.pretty_generate(obj))
    File.rename(tmp, PATH)
  ensure
    File.delete(tmp) if File.exist?(tmp)
  end
end

def parse_kv_flags(argv)
  h = {}
  i = 0
  while i < argv.length
    if argv[i] == "--" && i + 1 < argv.length
      i += 1
      next
    end
    if argv[i].start_with?("--")
      key = argv[i][2..-1].tr("-", "_")
      h[key] = argv[i + 1]
      i += 2
    else
      i += 1
    end
  end
  h
end

def now_ms
  (Time.now.to_f * 1000).to_i
end

cmd = ARGV.shift

case cmd
when "write"
  opts = parse_kv_flags(ARGV)
  agent = (opts["agent"] || "").downcase
  abort "agent beta|alpha required" unless %w[beta alpha].include?(agent)

  with_file_lock do
    st = load_state
    st[agent] = {
      "ts_ms" => now_ms,
      "tension" => (opts["tension"] || "0").to_f,
      "conf" => (opts["conf"] || "0").to_f,
      "direction" => (opts["direction"] || "neutral").to_s,
      "mom_bps" => (opts["mom"] || opts["mom_bps"] || "0").to_f,
      "cycle" => (opts["cycle"] || "0").to_i,
      "last_result" => (opts["result"] || "active").to_s,
      "last_pnl" => (opts["pnl"] || opts["last_pnl"] || "0").to_f
    }

    tension = st[agent]["tension"]
    if agent == "beta" && tension > VELOCITY_TENSION
      st["events"]["alpha_velocity_until_ms"] = now_ms + VELOCITY_MS
    elsif agent == "alpha" && tension > VELOCITY_TENSION
      st["events"]["beta_velocity_until_ms"] = now_ms + VELOCITY_MS
    end

    if (opts["cohesion"] || "") != ""
      st["swarm_cohesion"] = [[opts["cohesion"].to_f, 0.2].max, 1.0].min
    end

    atomic_write(st)
  end

when "read"
  opts = parse_kv_flags(ARGV)
  agent = (opts["agent"] || "").downcase
  cycle = (opts["cycle"] || "0").to_i
  neighbor = agent == "beta" ? "alpha" : "beta"
  abort "agent beta|alpha required" unless %w[beta alpha].include?(agent)

  st = load_state
  n = st[neighbor] || agent_empty
  ev = st["events"] || {}
  cohesion = (st["swarm_cohesion"] || 0.618).to_f
  ms = now_ms

  vel_key = "#{agent}_velocity_until_ms"
  shock_key = "#{agent}_shockwave_until_cycle"
  velocity_active = ms < (ev[vel_key] || 0).to_i ? 1 : 0
  shock_active = cycle <= (ev[shock_key] || 0).to_i ? 1 : 0

  puts "export swarm_neighbor_tension=#{format('%.8f', n['tension'].to_f)}"
  puts "export swarm_neighbor_conf=#{format('%.8f', n['conf'].to_f)}"
  puts "export swarm_neighbor_direction=#{n['direction']}"
  puts "export swarm_neighbor_mom=#{format('%.8f', n['mom_bps'].to_f)}"
  puts "export swarm_neighbor_result=#{n['last_result']}"
  puts "export swarm_neighbor_cycle=#{n['cycle'].to_i}"
  puts "export swarm_neighbor_ts_ms=#{(n['ts_ms'] || 0).to_i}"
  neighbor_ts = (n['ts_ms'] || 0).to_i
  neighbor_age = neighbor_ts.positive? ? ((ms - neighbor_ts) / 1000.0) : 999_999.0
  puts "export swarm_neighbor_age_sec=#{format('%.3f', neighbor_age)}"
  puts "export swarm_velocity_boost_active=#{velocity_active}"
  puts "export swarm_shockwave_active=#{shock_active}"
  puts "export swarm_shockwave_until_cycle=#{(ev[shock_key] || 0).to_i}"
  puts "export swarm_cohesion=#{format('%.6f', cohesion)}"

when "shockwave"
  opts = parse_kv_flags(ARGV)
  from = (opts["from"] || "").downcase
  cycle = (opts["cycle"] || "0").to_i
  duration = (opts["duration"] || ENV["SWARM_SHOCKWAVE_CYCLES"] || "10").to_i
  target = from == "beta" ? "alpha" : "beta"
  abort "from beta|alpha required" unless %w[beta alpha].include?(from)

  until_cycle = nil
  with_file_lock do
    st = load_state
    st["events"] ||= {}
    until_cycle = cycle + duration
    st["events"]["#{target}_shockwave_until_cycle"] = until_cycle
    atomic_write(st)
  end
  puts "shockwave #{from}->#{target} until_cycle=#{until_cycle}"

when "velocity_pulse"
  opts = parse_kv_flags(ARGV)
  target = (opts["target"] || "alpha").downcase
  duration_ms = (opts["duration_ms"] || VELOCITY_MS.to_s).to_i
  with_file_lock do
    st = load_state
    st["events"] ||= {}
    st["events"]["#{target}_velocity_until_ms"] = now_ms + duration_ms
    atomic_write(st)
  end

when "set_cohesion"
  opts = parse_kv_flags(ARGV)
  with_file_lock do
    st = load_state
    st["swarm_cohesion"] = [[(opts["value"] || "0.618").to_f, 0.2].max, 1.0].min
    atomic_write(st)
  end

when "resync"
  opts = parse_kv_flags(ARGV)
  cycle = (opts["cycle"] || "0").to_i
  gap_sec = (opts["gap_sec"] || "0").to_i
  with_file_lock do
    st = load_state
    st["events"] ||= {}
    ev = st["events"]
    ms = now_ms
    ev["alpha_velocity_until_ms"] = 0 if ms >= (ev["alpha_velocity_until_ms"] || 0).to_i
    ev["beta_velocity_until_ms"] = 0 if ms >= (ev["beta_velocity_until_ms"] || 0).to_i
    %w[alpha beta].each do |ag|
      key = "#{ag}_shockwave_until_cycle"
      until_c = (ev[key] || 0).to_i
      ev[key] = cycle - 1 if until_c > 0 && cycle > 0 && until_c >= cycle
    end
    st["events"] = ev
    st["gap_resync"] = {
      "cycle" => cycle,
      "gap_sec" => gap_sec,
      "ts" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    atomic_write(st)
  end
  puts "resync cycle=#{cycle} gap_sec=#{gap_sec}"

else
  warn "Usage: swarm_telemetry.rb write|read|shockwave|velocity_pulse|set_cohesion|resync"
  exit 1
end
