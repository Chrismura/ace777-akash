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

# === MODE MACRO TEMPÊTE (20/08/2026, chantier n°2 validé GO) ===
# Détecteur : Index_Maison/scripts/detecteur_macro_tempete.py (launchd, ~60s)
# → écrit runs/macro_tempete.json : { active, direction: long|short|none, ... }
# Ici : choc haussier (dir=long) → SELL bloqués ; choc baissier (dir=short) → BUY bloqués.
# Script EXTERNE au genesis (C1 respecté : genesis jamais modifié).
# Fail-open : flag absent/vieux/invalide → comportement normal.
MACRO_TEMPETE_FILE = ENV.fetch("MACRO_TEMPETE_FILE", "runs/macro_tempete.json")
MACRO_TEMPETE_TTL = (ENV["MACRO_TEMPETE_TTL_SEC"] || "180").to_i

def macro_tempete_block(dir_calc)
  return false unless File.file?(MACRO_TEMPETE_FILE)
  begin
    j = JSON.parse(File.read(MACRO_TEMPETE_FILE))
    return false unless j["active"] == true
    ts = j["ts"].to_i
    return false if ts <= 0 || (Time.now.to_i - ts) > MACRO_TEMPETE_TTL
    dir_macro = j["direction"].to_s
    return false unless %w[long short].include?(dir_macro)
    # Choc haussier → SELL bloqués (pas de short contre la hausse).
    # Choc baissier → BUY bloqués (pas de long contre la baisse).
    (dir_macro == "long" && dir_calc == "short") ||
      (dir_macro == "short" && dir_calc == "long")
  rescue StandardError
    false
  end
end

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

# MACRO TEMPÊTE : bloque la direction contre le choc (avant l'allow final)
if macro_tempete_block(direction)
  allow = false
  reason = "macro_storm_block"
end

puts({
  allow: allow,
  direction: direction,
  reason: reason,
  confidence: conf.round(4),
  mom_bps: mom.round(4),
  spread_bps: spread.round(4)
}.to_json)
