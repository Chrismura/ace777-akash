#!/usr/bin/env ruby
require "json"
require "optparse"

opts = {
  mom_bps: 0.0,
  spread_bps: 0.0,
  min_conf: 0.55,
  min_mom_bps: 0.5,
  dir_bps: 0.2,
  max_spread_bps: 2.0
}

OptionParser.new do |o|
  o.on("--mom-bps V", Float) { |v| opts[:mom_bps] = v }
  o.on("--spread-bps V", Float) { |v| opts[:spread_bps] = v }
  o.on("--min-conf V", Float) { |v| opts[:min_conf] = v }
  o.on("--min-mom-bps V", Float) { |v| opts[:min_mom_bps] = v }
  o.on("--dir-bps V", Float) { |v| opts[:dir_bps] = v }
  o.on("--max-spread-bps V", Float) { |v| opts[:max_spread_bps] = v }
end.parse!(ARGV)

mom = opts[:mom_bps].to_f
spread = opts[:spread_bps].to_f
abs_mom = mom.abs

direction = if mom >= opts[:dir_bps]
  "long"
elsif mom <= -opts[:dir_bps]
  "short"
else
  "neutral"
end

spread_penalty = [spread / [opts[:max_spread_bps], 0.0001].max, 1.0].min
mom_score = [abs_mom / [opts[:dir_bps] * 2.0, 0.0001].max, 1.5].min / 1.5
conf = (mom_score * (1.0 - spread_penalty * 0.5)).clamp(0.0, 1.0)

# In flat micro-momentum phases, keep a small baseline confidence
# (if spread is healthy) to avoid blocking 100% of cycles.
if abs_mom == 0.0 && spread <= opts[:max_spread_bps]
  conf = [conf, 0.35 * (1.0 - spread_penalty * 0.5)].max
end

allow = true
reason = "ok"

if spread > opts[:max_spread_bps]
  allow = false
  reason = "spread_too_wide"
elsif abs_mom < opts[:min_mom_bps]
  allow = false
  reason = "momentum_too_small"
elsif direction == "neutral"
  allow = false
  reason = "direction_unclear"
elsif conf < opts[:min_conf]
  allow = false
  reason = "low_confidence"
end

puts({
  allow: allow,
  direction: direction,
  reason: reason,
  confidence: conf.round(4),
  mom_bps: mom.round(4),
  spread_bps: spread.round(4)
}.to_json)
