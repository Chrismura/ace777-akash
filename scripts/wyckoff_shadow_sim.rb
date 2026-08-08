#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
# Simulation Wyckoff SHADOW — replay CSV sans modifier le moteur live
# Usage: ruby scripts/wyckoff_shadow_sim.rb [tag] [--start ISO8601]

require "json"
require "time"
require "fileutils"

Encoding.default_external = Encoding::UTF_8

root = File.expand_path("..", __dir__)
run_dir = File.join(root, "runs")
tag = ARGV[0] || "MASTER_BASE_V8_5_IMPACT_4H00"
start_filter = nil
if (i = ARGV.index("--start"))
  start_filter = ARGV[i + 1]
end

# Archive C1 session si tag 4H00
beta_csv = File.join(run_dir, "#{tag}_BETA_X5.csv")
alpha_csv = File.join(run_dir, "#{tag}_ALPHA_X13_BURST13.csv")
archive_beta = Dir.glob(File.join(run_dir, "archive", "#{tag}_BETA_*")).max_by { |f| File.mtime(f) }
archive_alpha = Dir.glob(File.join(run_dir, "archive", "#{tag}_ALPHA_*")).max_by { |f| File.mtime(f) }
beta_csv = archive_beta if archive_beta && !File.file?(beta_csv)
alpha_csv = archive_alpha if archive_alpha && !File.file?(alpha_csv)

meta_path = File.join(run_dir, "#{tag}_run_meta.json")
if !start_filter && File.file?(meta_path)
  start_filter = JSON.parse(File.read(meta_path))["start_utc"] rescue nil
end
start_filter ||= "2026-07-08T05:41:00Z" if tag.include?("4H00")

Row = Struct.new(:ts, :cycle, :side, :status, :entry, :exit_px, :pnl, :reason, :msg,
                 :tension, :mom_bps, :bid_drop, :ask_drop, :spread_bps, :unit)

def parse_row(cols, unit)
  ts, cycle, side, status, entry, exit_px, _qty, bps, pnl, reason, _hold, msg = cols
  msg ||= ""
  tension = msg[/tension=([0-9.]+)/, 1]&.to_f || 0.0
  mom_bps = msg[/raw_mom_bps=([0-9.-]+)/, 1]&.to_f || msg[/mom_sig=([0-9.-]+)/, 1]&.to_f || 0.0
  bid_drop = msg[/bid_drop=([0-9.]+)/, 1]&.to_f || 0.0
  ask_drop = msg[/ask_drop=([0-9.]+)/, 1]&.to_f || 0.0
  spread = msg[/spread_bps=([0-9.]+)/, 1]&.to_f || 0.0
  Row.new(ts, cycle.to_i, side, status, entry.to_f, exit_px.to_f, pnl.to_f, reason, msg,
          tension, mom_bps, bid_drop, ask_drop, spread, unit)
end

def load_csv(path, unit, min_ts: nil)
  rows = []
  return rows unless File.file?(path)

  File.foreach(path).with_index do |line, idx|
    next if idx.zero?

    cols = line.strip.split(",", -1)
    next if cols.size < 10
    next if min_ts && cols[0] < min_ts

    rows << parse_row(cols, unit)
  end
  rows
end

def wyckoff_phase(prices, window: 30)
  return { phase: "unknown", range_high: 0, range_low: 0, mid: 0 } if prices.size < 5

  slice = prices.last(window)
  hi = slice.max
  lo = slice.min
  mid = (hi + lo) / 2.0
  last = slice.last
  range_bps = mid.positive? ? ((hi - lo) / mid) * 10_000.0 : 0.0

  phase = if range_bps < 8.0
            "chop"
          elsif last > mid * 1.0003
            "markup"
          elsif last < mid * 0.9997
            "markdown"
          else
            "accumulation"
          end
  { phase: phase, range_high: hi, range_low: lo, mid: mid, range_bps: range_bps }
end

def wyckoff_verdict(row, ctx)
  reasons = []
  allow = true
  boost = false

  price = row.entry.positive? ? row.entry : ctx[:last_price]
  ctx[:prices] << price if price.positive?
  w = wyckoff_phase(ctx[:prices])

  # 1. Effort vs résultat (absorption)
  effort = [row.bid_drop, row.ask_drop].max
  result_bps = row.mom_bps.abs
  if effort > 5.0 && result_bps < 0.3 && row.tension > 0.8
    allow = false
    reasons << "effort_sans_resultat"
  end

  # 2. Spring (faux break bas + signal long)
  if price.positive? && price < w[:range_low] * 0.9998 && row.side == "BUY"
    boost = true
    reasons << "spring_long"
  end

  # 3. Upthrust (faux break haut + signal short)
  if price.positive? && price > w[:range_high] * 1.0002 && row.side == "SELL"
    boost = true
    reasons << "upthrust_short"
  end

  # 4. Filtre phase (shadow strict)
  if row.status == "FILLED" || row.side == "BUY" || row.side == "SELL"
    trade_side = row.side
    if trade_side == "BUY" && w[:phase] == "markdown"
      allow = false
      reasons << "phase_markdown_block_long"
    elsif trade_side == "SELL" && w[:phase] == "markup"
      allow = false
      reasons << "phase_markup_block_short"
    end
  end

  # 5. Chop = plus sélectif
  if w[:phase] == "chop" && row.tension < 1.2 && !boost
    allow = false
    reasons << "chop_low_tension"
  end

  verdict = if !allow
              "SKIP"
            elsif boost
              "BOOST"
            else
              "ALLOW"
            end
  { verdict: verdict, phase: w[:phase], reasons: reasons.uniq, range_bps: w[:range_bps] }
end

def simulate(rows)
  ctx = { prices: [], last_price: 0.0 }
  results = { actual_pnl: 0.0, shadow_pnl: 0.0, filled: 0,
              shadow_skip: 0, shadow_allow: 0, shadow_boost: 0,
              saved_losses: 0.0, missed_gains: 0.0, trades: [] }

  rows.sort_by(&:ts).each do |row|
  next unless row.status == "FILLED"

    results[:filled] += 1
    results[:actual_pnl] += row.pnl
    ctx[:last_price] = row.entry if row.entry.positive?

    w = wyckoff_verdict(row, ctx)
    shadow_pnl = if w[:verdict] == "SKIP"
                   results[:shadow_skip] += 1
                   row.pnl < 0 ? (results[:saved_losses] += row.pnl.abs) : (results[:missed_gains] += row.pnl)
                   0.0
                 else
                   results[:shadow_allow] += 1 if w[:verdict] == "ALLOW"
                   results[:shadow_boost] += 1 if w[:verdict] == "BOOST"
                   row.pnl
                 end
    results[:shadow_pnl] += shadow_pnl
    results[:trades] << {
      ts: row.ts, unit: row.unit, side: row.side, pnl: row.pnl,
      wyckoff: w[:verdict], phase: w[:phase], reasons: w[:reasons].join(",")
    }
  end
  results
end

beta_rows = load_csv(beta_csv, "BETA", min_ts: start_filter)
alpha_rows = load_csv(alpha_csv, "ALPHA", min_ts: start_filter)
all_rows = beta_rows + alpha_rows

unless all_rows.any?
  warn "Aucune donnée pour tag=#{tag} start=#{start_filter}"
  exit 1
end

res = simulate(all_rows)
out_path = File.join(run_dir, "WYCKOFF_SHADOW_#{tag}.md")

lines = []
lines << "# Wyckoff SHADOW — simulation replay"
lines << ""
lines << "> Tag: `#{tag}` | Filtre: `#{start_filter || 'aucun'}` | Mode: **lecture seule** (pas appliqué au live)"
lines << "> Généré: `#{Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ')}`"
lines << ""
lines << "## Résultat global"
lines << ""
lines << "| Métrique | Sans Wyckoff (réel) | Avec Wyckoff shadow |"
lines << "|----------|---------------------|---------------------|"
lines << "| Trades FILLED | #{res[:filled]} | #{res[:shadow_allow] + res[:shadow_boost]} exécutés, #{res[:shadow_skip]} filtrés |"
lines << "| PnL net | **#{format('%.4f', res[:actual_pnl])} USDT** | **#{format('%.4f', res[:shadow_pnl])} USDT** |"
lines << "| Delta | — | **#{format('%+.4f', res[:shadow_pnl] - res[:actual_pnl])} USDT** |"
lines << ""
lines << "- Pertes évitées (trades filtrés perdants): **#{format('%.4f', res[:saved_losses])} USDT**"
lines << "- Gains manqués (trades filtrés gagnants): **#{format('%.4f', res[:missed_gains])} USDT**"
lines << ""
lines << "## Détail des trades FILLED"
lines << ""
lines << "| TS | Unité | Side | PnL | Wyckoff | Phase | Raisons |"
lines << "|----|-------|------|-----|---------|-------|---------|"
res[:trades].each do |t|
  lines << "| #{t[:ts]} | #{t[:unit]} | #{t[:side]} | #{format('%.4f', t[:pnl])} | #{t[:wyckoff]} | #{t[:phase]} | #{t[:reasons]} |"
end
lines << ""
lines << "## Lecture"
lines << ""
delta = res[:shadow_pnl] - res[:actual_pnl]
if delta > 0.5
  lines << "**Verdict simulation : positif** — Wyckoff shadow aurait amélioré le PnL d'environ #{format('%.2f', delta)} USDT sur ce cycle."
elsif delta < -0.5
  lines << "**Verdict simulation : négatif** — Wyckoff shadow aurait **réduit** le PnL (#{format('%.2f', delta)} USDT). Trop filtrant sur ce timeframe."
else
  lines << "**Verdict simulation : neutre** — impact marginal (#{format('%+.2f', delta)} USDT). À valider sur 2–3 cycles."
end
lines << ""
lines << "_Règles shadow : effort/résultat, spring/upthrust, filtre phase markup/markdown, chop sélectif._"
lines << ""

File.write(out_path, lines.join("\n"))
link = File.join(run_dir, "WYCKOFF_SHADOW_DERNIER.md")
FileUtils.cp(out_path, link)

puts "WYCKOFF_SIM_OK: #{out_path}"
puts "ACTUAL: #{format('%.4f', res[:actual_pnl])} USDT | SHADOW: #{format('%.4f', res[:shadow_pnl])} USDT | DELTA: #{format('%+.4f', res[:shadow_pnl] - res[:actual_pnl])}"
puts "FILTERED: #{res[:shadow_skip]}/#{res[:filled]} trades"
