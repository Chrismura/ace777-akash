#!/usr/bin/env ruby
# frozen_string_literal: true
# Superviseur Vortex v2 — chop_score_v2 + hystérésis → JSON radar
# Usage: ruby scripts/vortex_regime_compute.rb LOG_BETA.csv [STATE.json]

require "json"
require "net/http"
require "time"
require "uri"

log_path = ARGV[0]
state_path = ARGV[1] || "runs/vortex_regime_state.json"
control_path = ENV.fetch("VORTEX_CONTROL_FILE", "runs/vortex_control.json")
symbol = ENV.fetch("SYMBOL", "BTCUSDT")
hy_high = (ENV["VORTEX_HYSTERESIS_HIGH"] || "0.65").to_f
hy_low = (ENV["VORTEX_HYSTERESIS_LOW"] || "0.45").to_f
lookback = (ENV["VORTEX_KLINES_LOOKBACK_MIN"] || "15").to_i

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

def parse_rows(path)
  rows = []
  File.foreach(path).with_index do |ln, i|
    next if i.zero?

    cols = ln.strip.split(",", -1)
    next if cols.size < 10

    msg = cols[10].to_s
    tension = (msg[/tension=([0-9.]+)/, 1] || "0").to_f
    tension = (msg[/mom_sig=([0-9.-]+)/, 1] || "0").to_f if tension.zero?
    rows << {
      ts: cols[0], status: cols[3], tension: tension,
      skip: cols[3] == "SKIPPED"
    }
  end
  rows
end

def fetch_klines(symbol)
  uri = URI("https://fapi.binance.com/fapi/v1/klines?symbol=#{symbol}&interval=1m&limit=#{lookback + 5}")
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.open_timeout = 5
  http.read_timeout = 15
  res = http.get(uri.request_uri)
  return [] unless res.is_a?(Net::HTTPSuccess)

  JSON.parse(res.body)
rescue StandardError
  []
end

def kline_metrics(candles)
  return { trend_bps: 0.0, range_bps: 20.0, vol_bps: 5.0 } if candles.nil? || candles.size < 3

  slice = candles.last(lookback + 1)
  op = slice.first[1].to_f
  cl = slice.last[4].to_f
  hi = slice.map { |k| k[2].to_f }.max
  lo = slice.map { |k| k[3].to_f }.min
  mid = (hi + lo) / 2.0
  trend_bps = op.positive? ? ((cl - op) / op) * 10_000.0 : 0.0
  range_bps = mid.positive? ? ((hi - lo) / mid) * 10_000.0 : 0.0
  rets = []
  slice.each_cons(2) do |a, b|
    rets << ((b[4].to_f - a[4].to_f).abs / [a[4].to_f, 1.0].max) * 10_000.0
  end
  vol_bps = rets.empty? ? 0.0 : rets.sum / rets.size
  { trend_bps: trend_bps, range_bps: range_bps, vol_bps: vol_bps }
end

def chop_score_v2(window, km)
  tensions = window.map { |r| r[:tension] }.select { |t| t.positive? }
  tension_ma = tensions.empty? ? 0.0 : tensions.sum / tensions.size
  trend_chop = 1.0 - [km[:trend_bps].abs / 25.0, 1.0].min
  range_chop = if km[:range_bps] < 10.0
                 1.0
               elsif km[:range_bps] < 20.0
                 0.5
               else
                 0.0
               end
  tension_chop = 1.0 - [tension_ma / 1.0, 1.0].min
  vol_chop = km[:vol_bps] < 3.0 ? 0.8 : 0.2
  (0.30 * trend_chop + 0.25 * range_chop + 0.30 * tension_chop + 0.15 * vol_chop).clamp(0.0, 1.0)
end

rows = parse_rows(log_path)
window = rows.last(80)
km = kline_metrics(fetch_klines(symbol))
score = chop_score_v2(window, km)

state = { "mode" => "CHOP", "chop_score" => score }
if File.file?(state_path)
  begin
    state = JSON.parse(File.read(state_path))
  rescue StandardError
    state = { "mode" => "CHOP", "chop_score" => score }
  end
end

mode = state["mode"] || "CHOP"
mode = "CHOP" if score > hy_high
mode = "TREND" if score < hy_low
state["mode"] = mode
state["chop_score"] = score.round(4)
state["updated_at"] = Time.now.utc.iso8601
File.write(state_path, JSON.pretty_generate(state))

prof = PROFILES[mode]
out = {
  "mode" => mode,
  "chop_score" => score.round(4),
  "trend_bps_15m" => km[:trend_bps].round(4),
  "range_bps" => km[:range_bps].round(4),
  "message" => "v2_chop_#{score.round(2)}_#{mode.downcase}",
  "ts" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
  "confiance_structure" => (1.0 - score).round(4),
  "justification" => "rule_chop_#{score.round(2)}_#{mode.downcase}"
}.merge(prof)

File.write("#{control_path}.tmp", JSON.pretty_generate(out))
File.rename("#{control_path}.tmp", control_path)
puts JSON.generate(out)
