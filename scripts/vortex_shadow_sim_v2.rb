#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
# Vortex SHADOW V2 — pilotage RADAR + chop_score_v2 (klines 1m + tension carnet)
# Usage: ruby scripts/vortex_shadow_sim_v2.rb [tag1 tag2 ...]
#        CHOP_SCORE_VERSION=v1 ruby ...  # ancien score (défaut: v2)

require "json"
require "net/http"
require "time"
require "fileutils"
require "uri"

Encoding.default_external = Encoding::UTF_8

root = File.expand_path("..", __dir__)
RUN_DIR = File.join(root, "runs")
CACHE_DIR = File.join(RUN_DIR, "klines_cache")
CHOP_SCORE_VERSION = ENV.fetch("CHOP_SCORE_VERSION", "v2")

DEFAULT_TAGS = %w[
  MASTER_BASE_V8_5_IMPACT_4H
  MASTER_HYBRID_VF_20260708
  MASTER_BASE_V8_5_IMPACT_C2
].freeze

HYSTERESIS_HIGH = 0.65
HYSTERESIS_LOW  = 0.45
RADAR_DIR_BPS = 0.20
PROXY_HORIZON_SEC = 90
KLINES_LOOKBACK_MIN = 15
SYMBOL = ENV.fetch("SYMBOL", "BTCUSDT")
KLINES_BASE = ENV.fetch("KLINES_BASE_URL", "https://fapi.binance.com")

# Aligné sur config_active.env + bornes sécurité
PROFILES = {
  "BASELINE" => {
    alpha_mom: 0.008, beta_mom: 0.010,
    alpha_conf: 0.25, beta_conf: 0.30,
    max_spread: 8.0
  },
  "TREND" => {
    alpha_mom: 0.003, beta_mom: 0.004,
    alpha_conf: 0.20, beta_conf: 0.22,
    max_spread: 14.0
  },
  "CHOP" => {
    alpha_mom: 0.012, beta_mom: 0.015,
    alpha_conf: 0.35, beta_conf: 0.40,
    max_spread: 5.0
  }
}.freeze

Row = Struct.new(
  :ts, :cycle, :side, :status, :pnl, :reason, :msg,
  :mom_sig, :spread_bps, :tension, :radar_sub, :unit, :idx
)

def clamp(v, lo, hi)
  [[v.to_f, lo].max, hi].min
end

def profile_for(unit, mode)
  p = PROFILES[mode]
  if unit == "ALPHA"
    {
      min_mom: clamp(p[:alpha_mom], 0.003, 0.02),
      min_conf: clamp(p[:alpha_conf], 0.15, 0.45),
      max_spread: clamp(p[:max_spread], 4.0, 16.0)
    }
  else
    {
      min_mom: clamp(p[:beta_mom], 0.003, 0.02),
      min_conf: clamp(p[:beta_conf], 0.15, 0.45),
      max_spread: clamp(p[:max_spread], 4.0, 16.0)
    }
  end
end

def parse_row(cols, unit, idx)
  ts, _cycle, _side, status, _en, _ex, _qty, _bps, pnl, reason, msg = cols
  msg = cols[10].to_s if cols.size == 11
  msg ||= ""
  mom_sig = msg[/mom_sig=([0-9.-]+)/, 1]&.to_f || 0.0
  tension = msg[/tension=([0-9.]+)/, 1]&.to_f
  tension = mom_sig if tension.nil? || tension.zero?
  spread = msg[/spread_bps=([0-9.]+)/, 1]&.to_f || 0.0
  radar_sub = msg[/reason=([^ ]+)/, 1] || ""
  Row.new(ts, cols[1].to_i, cols[2], status, pnl.to_f, reason, msg,
          mom_sig, spread, tension, radar_sub, unit, idx)
end

def load_tag_rows(tag)
  beta = Dir.glob(File.join(RUN_DIR, "#{tag}_BETA*.csv")).max_by { |f| File.mtime(f) }
  alpha = Dir.glob(File.join(RUN_DIR, "#{tag}_ALPHA*.csv")).max_by { |f| File.mtime(f) }
  meta = File.join(RUN_DIR, "#{tag}_run_meta.json")
  min_ts = File.file?(meta) ? (JSON.parse(File.read(meta))["start_utc"] rescue nil) : nil

  rows = []
  [[beta, "BETA"], [alpha, "ALPHA"]].each do |path, unit|
    next unless path && File.file?(path)

    File.foreach(path).with_index do |line, i|
      next if i.zero?

      cols = line.strip.split(",", -1)
      next if cols.size < 10
      next if min_ts && cols[0] < min_ts

      rows << parse_row(cols, unit, rows.size)
    end
  end
  rows.sort_by(&:ts)
end

def parse_ts(ts)
  Time.parse(ts)
rescue StandardError
  Time.at(0)
end

def chop_score_v1(window)
  return 0.5 if window.empty?

  tensions = window.map(&:tension).select { |t| t.positive? }
  tension_ma = tensions.empty? ? 0.0 : tensions.sum / tensions.size
  skip_rate = window.count { |r| r.status == "SKIPPED" }.to_f / window.size

  trend_proxy = 0.0
  if tensions.size >= 5
    half = tensions.size / 2
    first = tensions.first(half).sum / half
    last = tensions.last(tensions.size - half).sum / (tensions.size - half)
    trend_proxy = last - first
  end

  (0.45 * (1.0 - [tension_ma / 1.2, 1.0].min)) +
    (0.35 * skip_rate) +
    (0.20 * (1.0 - [trend_proxy.abs / 0.5, 1.0].min))
end

# --- chop_score_v2 : klines 1m (structure) + tension carnet glissante ---
class KlineCache
  def initialize(symbol: SYMBOL, base_url: KLINES_BASE)
    @symbol = symbol
    @base_url = base_url
    @by_minute = {} # epoch_min => { open, high, low, close }
  end

  def load_range!(t_start, t_end)
    FileUtils.mkdir_p(CACHE_DIR)
    cache_key = "#{@symbol}_#{t_start.utc.strftime('%Y%m%d%H')}_#{t_end.utc.strftime('%Y%m%d%H')}.json"
    cache_path = File.join(CACHE_DIR, cache_key)

    candles = if File.file?(cache_path)
                JSON.parse(File.read(cache_path))
              else
                fetch_klines(t_start, t_end).tap { |k| File.write(cache_path, JSON.generate(k)) }
              end

    candles.each do |k|
      next unless k.is_a?(Array) && k.size >= 5

      open_t = (k[0].to_i / 60_000) * 60
      @by_minute[open_t] = {
        open: k[1].to_f, high: k[2].to_f, low: k[3].to_f, close: k[4].to_f
      }
    end
    @loaded = true
  end

  def fetch_klines(t_start, t_end)
    start_ms = (t_start.to_i - KLINES_LOOKBACK_MIN * 60) * 1000
    end_ms = t_end.to_i * 1000 + 60_000
    limit = [[((end_ms - start_ms) / 60_000).ceil + 2, 1500].min, 30].max
    uri = URI("#{@base_url}/fapi/v1/klines?symbol=#{@symbol}&interval=1m&limit=#{limit}&startTime=#{start_ms}&endTime=#{end_ms}")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = uri.scheme == "https"
    http.open_timeout = 8
    http.read_timeout = 20
    res = http.get(uri.request_uri)
    raise "klines HTTP #{res.code}" unless res.is_a?(Net::HTTPSuccess)

    JSON.parse(res.body)
  rescue StandardError => e
    warn "KlineCache: #{e.message} — replay sans klines"
    []
  end

  def metrics_at(time)
    t = time.to_i
    keys = (0..KLINES_LOOKBACK_MIN).map { |i| t - i * 60 }.select { |k| @by_minute[k] }
    return { trend_bps: 0.0, range_bps: 20.0, vol_bps: 0.0 } if keys.size < 3

    slice = keys.sort.map { |k| @by_minute[k] }
    first = slice.first
    last = slice.last
    hi = slice.map { |c| c[:high] }.max
    lo = slice.map { |c| c[:low] }.min
    mid = (hi + lo) / 2.0
    op = first[:open]
    cl = last[:close]

    trend_bps = op.positive? ? ((cl - op) / op) * 10_000.0 : 0.0
    range_bps = mid.positive? ? ((hi - lo) / mid) * 10_000.0 : 0.0

    returns = []
    slice.each_cons(2) do |a, b|
      returns << ((b[:close] - a[:close]).abs / [a[:close], 1.0].max) * 10_000.0
    end
    vol_bps = returns.empty? ? 0.0 : returns.sum / returns.size

    { trend_bps: trend_bps, range_bps: range_bps, vol_bps: vol_bps }
  end
end

def chop_score_v2(window, klines, row_ts)
  return 0.5 if window.empty?

  tensions = window.map(&:tension).select { |t| t.positive? }
  tension_ma = tensions.empty? ? 0.0 : tensions.sum / tensions.size

  km = klines.metrics_at(parse_ts(row_ts))
  trend_abs = km[:trend_bps].abs
  range_bps = km[:range_bps]

  # Composantes 0..1 (1 = fort signal CHOP)
  trend_chop = 1.0 - [trend_abs / 25.0, 1.0].min
  range_chop = range_bps < 10.0 ? 1.0 : (range_bps < 20.0 ? 0.5 : 0.0)
  tension_chop = 1.0 - [tension_ma / 1.0, 1.0].min
  vol_chop = km[:vol_bps] < 3.0 ? 0.8 : 0.2

  score = (0.30 * trend_chop) + (0.25 * range_chop) + (0.30 * tension_chop) + (0.15 * vol_chop)
  score.clamp(0.0, 1.0)
end

def chop_score(window, klines, row_ts)
  if CHOP_SCORE_VERSION == "v1"
    chop_score_v1(window)
  else
    chop_score_v2(window, klines, row_ts)
  end
end

def radar_eval(mom_sig, spread_bps, prof)
  mom = mom_sig.to_f
  spread = spread_bps.to_f
  abs_mom = mom.abs
  dir_bps = RADAR_DIR_BPS
  max_spread = prof[:max_spread]
  min_mom = prof[:min_mom]
  min_conf = prof[:min_conf]

  direction = if mom >= dir_bps
              "long"
            elsif mom <= -dir_bps
              "short"
            else
              "neutral"
            end

  spread_penalty = [spread / [max_spread, 0.0001].max, 1.0].min
  mom_score = [abs_mom / [dir_bps * 2.0, 0.0001].max, 1.5].min / 1.5
  conf = (mom_score * (1.0 - spread_penalty * 0.5)).clamp(0.0, 1.0)
  conf = [conf, 0.35 * (1.0 - spread_penalty * 0.5)].max if abs_mom.zero? && spread <= max_spread

  allow = true
  reason = "ok"
  if spread > max_spread
    allow = false
    reason = "spread_too_wide"
  elsif abs_mom < min_mom
    allow = false
    reason = "momentum_too_small"
  elsif direction == "neutral"
    allow = false
    reason = "direction_unclear"
  elsif conf < min_conf
    allow = false
    reason = "low_confidence"
  end

  { "allow" => allow, "reason" => reason, "confidence" => conf.round(4) }
end

def nearest_filled_pnl(rows, from_idx)
  base_t = parse_ts(rows[from_idx].ts)
  ((from_idx + 1)...rows.size).each do |j|
    r = rows[j]
    next unless r.status == "FILLED"

    dt = parse_ts(r.ts) - base_t
    return r.pnl if dt >= 0 && dt <= PROXY_HORIZON_SEC
  end
  nil
end

def simulate_tag(rows, klines)
  window = []
  mode = "CHOP"
  flips = 0
  trend_slots = 0
  chop_slots = 0

  stats = {
    actual_pnl: 0.0,
    baseline_blocks: 0,
    v2_blocks: 0,
    reclaimed: 0,
    newly_blocked: 0,
    proxy_reclaimed_pnl: 0.0,
    saved_losses: 0.0,
    missed_gains: 0.0,
    by_subreason: Hash.new(0),
    reclaimed_by_sub: Hash.new(0),
    chop_scores: []
  }

  rows.each_with_index do |row, idx|
    window << row
    window.shift while window.size > 80

    cs = chop_score(window, klines, row.ts)
    stats[:chop_scores] << cs
    prev_mode = mode
    if mode == "CHOP" && cs < HYSTERESIS_LOW
      mode = "TREND"
    elsif mode == "TREND" && cs > HYSTERESIS_HIGH
      mode = "CHOP"
    end
    flips += 1 if mode != prev_mode
    mode == "TREND" ? trend_slots += 1 : chop_slots += 1

    next unless row.reason == "radar_block" || row.status == "FILLED"

    base_prof = profile_for(row.unit, "BASELINE")
    v2_prof = profile_for(row.unit, mode)

    base_r = radar_eval(row.mom_sig, row.spread_bps, base_prof)
    v2_r = radar_eval(row.mom_sig, row.spread_bps, v2_prof)
    base_ok = base_r["allow"] == true
    v2_ok = v2_r["allow"] == true

    if row.reason == "radar_block"
      stats[:baseline_blocks] += 1 unless base_ok
      stats[:v2_blocks] += 1 unless v2_ok
      stats[:by_subreason][row.radar_sub] += 1

      if !base_ok && v2_ok
        stats[:reclaimed] += 1
        stats[:reclaimed_by_sub][row.radar_sub] += 1
        proxy = nearest_filled_pnl(rows, idx)
        if proxy
          stats[:proxy_reclaimed_pnl] += proxy
        end
      end
    elsif row.status == "FILLED"
      stats[:actual_pnl] += row.pnl
      if base_ok && !v2_ok
        stats[:newly_blocked] += 1
        if row.pnl < 0
          stats[:saved_losses] += row.pnl.abs
        else
          stats[:missed_gains] += row.pnl
        end
      end
    end
  end

  shadow_pnl = stats[:actual_pnl] + stats[:proxy_reclaimed_pnl] - stats[:missed_gains]
  # saved_losses already counted as not lost in shadow if we block - approximate:
  shadow_pnl_v2 = stats[:actual_pnl] - stats[:missed_gains] + stats[:saved_losses] + stats[:proxy_reclaimed_pnl]

  stats.merge(
    mode_flips: flips,
    trend_pct: (rows.empty? ? 0.0 : (trend_slots.to_f / rows.size * 100).round(1)),
    chop_pct: (rows.empty? ? 0.0 : (chop_slots.to_f / rows.size * 100).round(1)),
    chop_score_avg: (stats[:chop_scores].empty? ? 0.0 : (stats[:chop_scores].sum / stats[:chop_scores].size).round(3)),
    shadow_pnl_v2: shadow_pnl_v2,
    delta_vs_actual: shadow_pnl_v2 - stats[:actual_pnl],
    final_mode: mode
  )
end

tags = ARGV.empty? ? DEFAULT_TAGS : ARGV
packed = tags.map do |t|
  rows = load_tag_rows(t)
  next nil if rows.empty?

  klines = KlineCache.new
  t0 = parse_ts(rows.first.ts)
  t1 = parse_ts(rows.last.ts)
  klines.load_range!(t0, t1)
  [t, rows, klines]
end.compact

if packed.empty?
  warn "Aucun CSV pour tags: #{tags.join(', ')}"
  exit 1
end

out_path = File.join(RUN_DIR, "VORTEX_SHADOW_V2_#{Time.now.utc.strftime('%Y%m%d_%H%M%S')}.md")
link = File.join(RUN_DIR, "VORTEX_SHADOW_V2_DERNIER.md")

lines = []
lines << "# Vortex SHADOW V2 — pilotage Radar"
lines << ""
lines << "> chop_score: **#{CHOP_SCORE_VERSION}** | Hystérésis: #{HYSTERESIS_HIGH}/#{HYSTERESIS_LOW}"
lines << "> Klines: `#{SYMBOL}` 1m (#{KLINES_LOOKBACK_MIN} min) + tension carnet glissante"
lines << "> Généré: `#{Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ')}`"
lines << ""
lines << "## Profils (bornes clampées)"
lines << ""
lines << "| Mode | BETA mom/conf/spread | ALPHA mom/conf/spread |"
lines << "|------|----------------------|------------------------|"
%w[BASELINE TREND CHOP].each do |m|
  b = profile_for("BETA", m)
  a = profile_for("ALPHA", m)
  lines << "| #{m} | #{b[:min_mom]}/#{b[:min_conf]}/#{b[:max_spread]} | #{a[:min_mom]}/#{a[:min_conf]}/#{a[:max_spread]} |"
end
lines << ""
lines << "_Proxy PnL récupéré = PnL du prochain FILLED dans #{PROXY_HORIZON_SEC}s (oracle partiel)._"
lines << ""
lines << "## chop_score_v2 (formule)"
lines << ""
lines << "```"
lines << "trend_chop  = 1 - min(|trend_bps_15m| / 25, 1)     # klines 1m"
lines << "range_chop  = 1 si range_bps < 10, 0.5 si < 20   # marché en boîte"
lines << "tension_chop = 1 - min(tension_ma_carnet / 1.0, 1)"
lines << "vol_chop    = 0.8 si vol faible, 0.2 sinon"
lines << "score = 0.30*trend + 0.25*range + 0.30*tension + 0.15*vol"
lines << "CHOP si score > 0.65 | TREND si score < 0.45 (hystérésis)"
lines << "```"
lines << ""

sim_results = packed.map { |tag, rows, klines| [tag, rows, simulate_tag(rows, klines)] }

sim_results.each do |tag, rows, s|
  lines << "## `#{tag}`"
  lines << ""
  lines << "- Lignes: #{rows.size} | FILLED réel: #{rows.count { |r| r.status == 'FILLED' }} | PnL réel: **#{format('%.4f', s[:actual_pnl])} USDT**"
  lines << "- `radar_block`: #{s[:baseline_blocks]} | Récupérés V2 (baseline block → v2 pass): **#{s[:reclaimed]}**"
  lines << "- FILLED bloqués en V2 (protection CHOP): #{s[:newly_blocked]} | Pertes évitées: #{format('%.4f', s[:saved_losses])} | Gains manqués: #{format('%.4f', s[:missed_gains])}"
  lines << "- Proxy PnL récupéré: #{format('%+.4f', s[:proxy_reclaimed_pnl])} USDT"
  lines << "- **Shadow PnL V2 estimé: #{format('%.4f', s[:shadow_pnl_v2])} USDT** | **Delta: #{format('%+.4f', s[:delta_vs_actual])} USDT**"
  lines << "- Bascules régime: #{s[:mode_flips]} | %TREND: #{s[:trend_pct]}% | %CHOP: #{s[:chop_pct]}% | chop_score moy: #{s[:chop_score_avg]}"
  lines << "- Mode final: #{s[:final_mode]}"
  lines << ""
  if s[:reclaimed_by_sub].any?
    lines << "### Récupérations par sous-raison radar"
    lines << ""
    s[:reclaimed_by_sub].sort_by { |_, v| -v }.each do |k, v|
      lines << "- `#{k.empty? ? '?' : k}`: #{v}"
    end
    lines << ""
  end
end

lines << "## Synthèse"
lines << ""
deltas = sim_results.map { |_, _, s| s[:delta_vs_actual] }
avg = deltas.sum / deltas.size
lines << "- Delta moyen V2 vs réel: **#{format('%+.4f', avg)} USDT**"
lines << "- chop_score: **#{CHOP_SCORE_VERSION}**"
if avg > 0.5
  lines << "- **Verdict: positif** — poursuivre implémentation genesis (cycle_radar_*), puis testnet A/B."
elsif avg < -0.5
  lines << "- **Verdict: négatif** — profils TREND trop permissifs sur ces cycles ; resserrer bornes."
else
  lines << "- **Verdict: marginal** — impact faible ; affiner chop_score ou profils avant live."
end
lines << ""
lines << "_Live genesis non modifié — simulation seulement. Prochaine étape si delta > 0 : `cycle_radar_*` dans genesis._"
lines << ""

File.write(out_path, lines.join("\n"))
FileUtils.cp(out_path, link)

puts "VORTEX_SIM_V2_OK: #{out_path} (chop_score=#{CHOP_SCORE_VERSION})"
sim_results.each do |tag, _, s|
  puts "#{tag}: actual=#{format('%.4f', s[:actual_pnl])} reclaimed=#{s[:reclaimed]} trend=#{s[:trend_pct]}% delta=#{format('%+.4f', s[:delta_vs_actual])}"
end
