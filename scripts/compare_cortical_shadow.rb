#!/usr/bin/env ruby
# frozen_string_literal: true
# Compare Qwen live vs GLM shadow — à lancer en fin de session 4h.
# Usage: ruby scripts/compare_cortical_shadow.rb

require "json"
require "time"

live_path = ENV.fetch("VORTEX_CONTROL_FILE", "runs/vortex_control.json")
shadow_path = ENV.fetch("CORTICAL_SHADOW_FILE", "runs/vortex_control.json.shadow")
shadow_log = ENV.fetch("CORTICAL_SHADOW_LOG", "runs/cortical_shadow_glm.log")

def read_json(path)
  return nil unless File.file?(path)

  JSON.parse(File.read(path))
rescue StandardError
  nil
end

live = read_json(live_path)
shadow = read_json(shadow_path)

puts "=== COMPARAISON CORTICAL LIVE vs SHADOW ==="
puts "live:   #{live_path}"
puts "shadow: #{shadow_path}"
puts

unless live
  puts "LIVE: fichier absent ou illisible"
  exit 1
end

unless shadow
  puts "SHADOW: fichier absent — lancer ./scripts/start_cortical_shadow_glm.sh"
  exit 1
end

%w[mode swarm_cohesion chop_score justification ts].each do |k|
  lv = live[k]
  sv = shadow[k]
  delta = k == "swarm_cohesion" ? (sv.to_f - lv.to_f).round(4) : nil
  line = "  #{k.ljust(18)} live=#{lv.inspect} shadow=#{sv.inspect}"
  line += " delta=#{delta}" if delta
  puts line
end

puts "  #{'market_phase'.ljust(18)} live=n/a shadow=#{shadow['market_phase'].inspect}"
puts "  #{'shadow_status'.ljust(18)} #{shadow['shadow_status']} api_ok=#{shadow['api_ok']} elapsed=#{shadow['llm_elapsed_sec']}s"
puts "  #{'engine'.ljust(18)} #{shadow['engine']} (#{shadow['provider']})"
puts

if File.file?(shadow_log)
  lines = File.readlines(shadow_log).grep(/SHADOW/)
  ok = lines.count { |l| l.include?("shadow_status") || l.match?(/\bok\b|partial_ok|slow_ok/) }
  fb = lines.count { |l| l.include?("fallback") }
  puts "Log shadow: #{lines.size} entrées (#{shadow_log})"
  puts "  dernières lignes:"
  lines.last(5).each { |l| puts "    #{l.strip}" }
end

puts
mode_match = live["mode"] == shadow["mode"]
coh_diff = (shadow["swarm_cohesion"].to_f - live["swarm_cohesion"].to_f).abs
puts "Verdict rapide:"
puts "  mode aligné: #{mode_match ? 'OUI' : 'NON'}"
puts "  |Δ cohesion| dernière passe: #{coh_diff.round(4)}"
puts "  → Phase D si shadow cohérent sur plusieurs runs ET api_ok majoritaire"
