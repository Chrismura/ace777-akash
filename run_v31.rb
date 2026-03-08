require "csv"

cfg = {}
File.readlines("vortex_v3_1.1437").each do |l|
  k, v = l.strip.split("=")
  cfg[k] = v
end

srand(cfg["RANDOM_SEED"].to_i)

thr        = cfg["MIN_PROFIT_THRESHOLD"].to_f
turbo_mult = cfg["TURBO_MULT"].to_f
fill_base  = cfg["FILL_PARTIAL_RATIO"].to_f
fill_shock = cfg["SHOCK_FILL_RATIO"].to_f
shock_thr  = cfg["SHOCK_THRESHOLD"].to_f
max_shock  = cfg["MAX_SHOCK_CONSECUTIVE"].to_i
cooldown   = cfg["COOLDOWN_CYCLES"].to_i
vent_gain  = cfg["VENTURI_GAIN"].to_f
safe_thr   = cfg["SAFE_THRESHOLD"].to_f
s_min      = cfg["S_RATIO_MIN_SHOCK"].to_f

cap = 1000.0
tg = tc = te = ta = 0.0
pass = skip = 0
shock_cycles = 0
cooldown_left = 0
shock_streak = 0
peak = cap
max_dd = 0.0

CSV.foreach("input_minute.csv", headers: true) do |r|
  e = r["entropy"].to_f
  s = 1.437 - (e * 0.5)

  base_mode =
    if e < 0.05
      "OFF"
    elsif e <= 0.15
      "NORMAL"
    elsif e <= 0.20
      "TURBO"
    elsif e <= 0.25
      "VENTURI"
    elsif e <= safe_thr
      "SHOCK"
    else
      "SAFE"
    end

  mode = base_mode

  if cooldown_left > 0
    mode = "VENTURI"
    cooldown_left -= 1
  end

  if mode == "SHOCK" && (s < s_min || shock_streak >= max_shock || e < shock_thr)
    mode = "SAFE"
    cooldown_left = cooldown
  end

  shock_streak = (mode == "SHOCK") ? shock_streak + 1 : 0
  shock_cycles += 1 if mode == "SHOCK"

  mult =
    if mode == "TURBO"
      turbo_mult
    elsif mode == "SHOCK"
      2.5
    else
      1.0
    end

  base_vent =
    if mode == "NORMAL"
      0.85
    elsif mode == "TURBO"
      0.50
    elsif mode == "VENTURI"
      0.40
    elsif mode == "SHOCK" || mode == "SAFE"
      0.30
    else
      1.0
    end

  vent = %w[TURBO VENTURI SHOCK SAFE].include?(mode) ? [base_vent, 1.0 - vent_gain].min : base_vent

  fill =
    if mode == "SHOCK"
      fill_shock
    elsif %w[TURBO VENTURI].include?(mode)
      fill_base
    elsif mode == "SAFE"
      0.0
    else
      1.0
    end

  pb = r["pnl_base"].to_f * cap
  cb = r["cost_base"].to_f * cap

  g = pb * mult * fill
  c = cb * vent
  ex = (cb * 0.4 * vent) * (1.0 + (1.0 - fill))
  a = c * 0.09

  ratio = (c + ex + a) > 0 ? g / (c + ex + a) : 999.0
  if ratio < thr
    skip += 1
    next
  end

  n = g - c - ex - a
  cap += n
  tg += g
  tc += c
  te += ex
  ta += a
  pass += 1

  peak = [peak, cap].max
  dd = (peak - cap) / peak
  max_dd = [max_dd, dd].max
end

net = cap - 1000.0
out = <<~TXT
=== ACE777 V3.1 FINAL ===
Passed: #{pass} | Skipped: #{skip}
Shock cycles: #{shock_cycles}
Net client: +$#{net.round(2)} (#{(net / 1000 * 100).round(2)}%)
Max drawdown: #{(max_dd * 100).round(2)}%
Gross: +$#{tg.round(2)} | Calories: -$#{tc.round(2)} | Exec: -$#{te.round(2)} | Architect: -$#{ta.round(2)}
Capital final: $#{cap.round(2)}
TXT

puts out
File.write("result_v3_1_final.txt", out)
