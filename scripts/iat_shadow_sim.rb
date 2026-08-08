#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
# Simulation IAT (Malanga / Cortana) en replay CSV — shadow read-only
# Usage: ruby scripts/iat_shadow_sim.rb [tag] [--start ISO8601]

require "json"
require "net/http"
require "time"
require "fileutils"
require "uri"

Encoding.default_external = Encoding::UTF_8

TAU = 2 * Math::PI
FUNDING_SAT = 0.05
OI_SAT_RATIO = 1.20
MAJOR_CYCLE_MIN = 24.0
INFLEX_TOL = 0.05
WALL_RATIO = 3.0
ALERT_THRESHOLD = 80.0

root = File.expand_path("..", __dir__)
run_dir = File.join(root, "runs")
tag = ARGV[0] || "MASTER_HYBRID_VF_20260708"
start_filter = nil
if (i = ARGV.index("--start"))
  start_filter = ARGV[i + 1]
end

beta_csv = File.join(run_dir, "#{tag}_BETA_X5.csv")
alpha_csv = File.join(run_dir, "#{tag}_ALPHA_X13_BURST13.csv")
archive_b = Dir.glob(File.join(run_dir, "archive", "#{tag}_BETA_*")).max_by { |f| File.mtime(f) }
archive_a = Dir.glob(File.join(run_dir, "archive", "#{tag}_ALPHA_*")).max_by { |f| File.mtime(f) }
beta_csv = archive_b if archive_b && !File.file?(beta_csv)
alpha_csv = archive_a if archive_a && !File.file?(alpha_csv)

meta_path = File.join(run_dir, "#{tag}_run_meta.json")
if !start_filter && File.file?(meta_path)
  start_filter = JSON.parse(File.read(meta_path))["start_utc"] rescue nil
end

def http_get(url)
  uri = URI(url)
  Net::HTTP.start(uri.host, uri.port, use_ssl: uri.scheme == "https",
                  open_timeout: 5, read_timeout: 15) do |http|
    res = http.get(uri.request_uri)
    raise "HTTP #{res.code} #{url}" unless res.is_a?(Net::HTTPSuccess)

    res.body
  end
end

def dft(signal)
  n = signal.length
  return [] if n.zero?

  (0...n).map do |k|
    re = 0.0
    im = 0.0
    signal.each_with_index do |x, t|
      ang = -TAU * k * t / n
      re += x * Math.cos(ang)
      im += x * Math.sin(ang)
    end
  [re, im]
  end
end

def dominant_cycles(series, max_cycles = 5)
  n = series.length
  return [] if n < 4

  mean = series.sum / n.to_f
  centered = series.map { |x| x - mean }
  spec = dft(centered)
  cycles = (1...(n / 2)).map do |k|
    re, im = spec[k]
    amp = 2.0 * Math.hypot(re, im) / n
    phase = Math.atan2(im, re)
    { period: n.to_f / k, amplitude: amp, phase: phase }
  end
  cycles.sort_by { |c| -c[:amplitude] }.first(max_cycles)
end

def cycle_position(c, t)
  Math.cos(TAU * t / c[:period] + c[:phase])
end

def energy_score(funding_pct, oi, oi_avg)
  score = 0.0
  score += 50.0 if funding_pct.abs > FUNDING_SAT
  score += 50.0 if oi_avg.positive? && oi > OI_SAT_RATIO * oi_avg
  score
end

def temporal_score(cycles, sample_index)
  major = cycles.select { |c| c[:period] > MAJOR_CYCLE_MIN }
               .max_by { |c| c[:amplitude] }
  return 0.0 unless major

  closeness = cycle_position(major, sample_index).abs
  closeness >= 1.0 - INFLEX_TOL ? 100.0 : 100.0 * closeness
end

def spatial_score(wall, avg_liq)
  return 0.0 if avg_liq <= 0.0

  [100.0 * (wall / avg_liq) / WALL_RATIO, 100.0].min
end

def triadic_alignment(cycles, market)
  e = energy_score(market[:funding_pct], market[:oi], market[:oi_avg])
  t = temporal_score(cycles, market[:sample_index])
  s = spatial_score(market[:wall], market[:avg_liq])
  iat = (e + t + s) / 3.0
  { energy: e, temporal: t, spatial: s, iat: iat, alert: iat > ALERT_THRESHOLD }
end

def parse_filled(path, unit, min_ts: nil)
  rows = []
  return rows unless File.file?(path)

  File.foreach(path).with_index do |line, idx|
    next if idx.zero?

    cols = line.strip.split(",", -1)
    next if cols.size < 10
    next if min_ts && cols[0] < min_ts
    next unless cols[3] == "FILLED"

    msg = cols[10] || ""
    bid = msg[/bid_drop=([0-9.]+)/, 1]&.to_f || 0.0
    ask = msg[/ask_drop=([0-9.]+)/, 1]&.to_f || 0.0
    tension = msg[/tension=([0-9.]+)/, 1]&.to_f || 0.0
    rows << {
      ts: cols[0], unit: unit, side: cols[2], pnl: cols[8].to_f,
      entry: cols[4].to_f, bid_drop: bid, ask_drop: ask, tension: tension,
      ms: (Time.parse(cols[0]).to_f * 1000).to_i
    }
  end
  rows
end

puts "IAT_SIM: chargement données Binance..."
klines_raw = JSON.parse(http_get("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=168"))
closes = klines_raw.map { |k| k[4].to_f }

funding_raw = JSON.parse(http_get("https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=100"))
funding_by_ms = funding_raw.map { |r| [r["fundingTime"].to_i, r["fundingRate"].to_f * 100.0] }.to_h

oi_raw = JSON.parse(http_get("https://fapi.binance.com/futures/data/openInterestHist?symbol=BTCUSDT&period=1h&limit=48"))
oi_rows = oi_raw.map { |r| [r["timestamp"].to_i, r["sumOpenInterest"].to_f] }
oi_avg = oi_rows.last(24).map { |_, v| v }.sum / [oi_rows.last(24).size, 1].max

def nearest_funding(funding_by_ms, ms)
  key = funding_by_ms.keys.min_by { |k| (k - ms).abs }
  funding_by_ms[key] || 0.0
end

def nearest_oi(oi_rows, ms)
  row = oi_rows.min_by { |k, _| (k - ms).abs }
  row ? row[1] : oi_rows.last&.last || 0.0
end

def market_at(trade, closes, funding_by_ms, oi_rows, oi_avg)
  sample_index = closes.length - 1
  max_drop = [trade[:bid_drop], trade[:ask_drop]].max
  avg_drop = [trade[:bid_drop], trade[:ask_drop], trade[:tension]].map(&:abs).sum
  avg_drop = [avg_drop / 3.0, 0.1].max
  wall = max_drop.positive? ? max_drop : trade[:tension]
  wall = [wall, 0.1].max

  {
    funding_pct: nearest_funding(funding_by_ms, trade[:ms]),
    oi: nearest_oi(oi_rows, trade[:ms]),
    oi_avg: oi_avg,
    wall: wall,
    avg_liq: avg_drop,
    sample_index: sample_index
  }
end

trades = parse_filled(beta_csv, "BETA", min_ts: start_filter) +
         parse_filled(alpha_csv, "ALPHA", min_ts: start_filter)
trades.sort_by! { |t| t[:ts] }

if trades.empty?
  warn "IAT_SIM_ERR: aucun trade FILLED pour #{tag}"
  exit 1
end

actual_pnl = 0.0
shadow_pnl = 0.0
shadow_skip = 0
saved = 0.0
missed = 0.0
details = []

trades.each do |tr|
  actual_pnl += tr[:pnl]
  m = market_at(tr, closes, funding_by_ms, oi_rows, oi_avg)
  cycles = dominant_cycles(closes, 5)
  sc = triadic_alignment(cycles, m)

  # Shadow rule: SKIP entrée si IAT >= 80 (rupture triadique — fail-closed)
  filtered = sc[:alert]
  if filtered
    shadow_skip += 1
    shadow_pnl += 0.0
    tr[:pnl] < 0 ? saved += tr[:pnl].abs : missed += tr[:pnl]
    verdict = "SKIP"
  else
    shadow_pnl += tr[:pnl]
    verdict = "ALLOW"
  end

  details << tr.merge(scores: sc, verdict: verdict, funding: m[:funding_pct], oi_ratio: m[:oi_avg].positive? ? m[:oi] / m[:oi_avg] : 0)
end

delta = shadow_pnl - actual_pnl
out = File.join(run_dir, "IAT_SHADOW_#{tag}.md")
lines = []
lines << "# IAT SHADOW (Malanga) — simulation replay"
lines << ""
lines << "> Tag: `#{tag}` | Formule: Cortana `quantum::malanga` | Shadow: **SKIP si IAT ≥ 80**"
lines << "> Généré: `#{Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ')}`"
lines << ""
lines << "## Formule rappel"
lines << ""
lines << "```"
lines << "Énergie  = funding saturé (|f|>0.05%) + OI > +20% vs moy 24h"
lines << "Temps    = cycle Fourier majeur (>24h) proche extremum"
lines << "Espace   = mur carnet (proxy bid_drop/ask_drop du CSV)"
lines << "IAT      = (E + T + S) / 3  →  alerte si > 80"
lines << "```"
lines << ""
lines << "## Résultat"
lines << ""
lines << "| | Réel | Avec IAT shadow |"
lines << "|---|------|-----------------|"
lines << "| Trades | #{trades.size} | #{trades.size - shadow_skip} (+ #{shadow_skip} filtrés) |"
lines << "| PnL | **#{format('%.4f', actual_pnl)} USDT** | **#{format('%.4f', shadow_pnl)} USDT** |"
lines << "| Delta | — | **#{format('%+.4f', delta)} USDT** |"
lines << ""
lines << "- Pertes évitées: **#{format('%.4f', saved)} USDT**"
lines << "- Gains manqués: **#{format('%.4f', missed)} USDT**"
lines << ""
lines << "## Détail par trade"
lines << ""
lines << "| TS | Unité | Side | PnL | IAT | E | T | S | Funding% | OI× | Verdict |"
lines << "|----|-------|------|-----|-----|---|---|---|----------|-----|---------|"
details.each do |d|
  sc = d[:scores]
  lines << "| #{d[:ts]} | #{d[:unit]} | #{d[:side]} | #{format('%.4f', d[:pnl])} | #{format('%.1f', sc[:iat])} | #{format('%.0f', sc[:energy])} | #{format('%.0f', sc[:temporal])} | #{format('%.0f', sc[:spatial])} | #{format('%+.4f', d[:funding])} | #{format('%.2f', d[:oi_ratio])} | #{d[:verdict]}#{sc[:alert] ? ' ⚠' : ''} |"
end
lines << ""
if delta > 0.5
  lines << "**Verdict : positif** — IAT shadow aurait amélioré le PnL de ~#{format('%.2f', delta)} USDT."
elsif delta < -0.5
  lines << "**Verdict : négatif** — IAT shadow aurait coupé des trades utiles (#{format('%.2f', delta)} USDT)."
else
  lines << "**Verdict : neutre** — impact marginal sur ce cycle (#{format('%+.2f', delta)} USDT)."
end
lines << ""
lines << "_Données live Binance (funding, OI, klines 1h) + proxy spatial depuis CSV (bid_drop/ask_drop)._"
lines << ""

File.write(out, lines.join("\n"))
FileUtils.cp(out, File.join(run_dir, "IAT_SHADOW_DERNIER.md"))

puts "IAT_SIM_OK: #{out}"
puts "ACTUAL: #{format('%.4f', actual_pnl)} | SHADOW: #{format('%.4f', shadow_pnl)} | DELTA: #{format('%+.4f', delta)} | FILTERED: #{shadow_skip}/#{trades.size}"
