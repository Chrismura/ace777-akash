#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
# Simulation Vortex SHADOW — compare timing / intelligence sans toucher le live
# Usage: ruby scripts/vortex_shadow_sim.rb [tag1 tag2 ...]
#        ruby scripts/vortex_shadow_sim.rb   # tous les tags récents connus

require "json"
require "time"
require "fileutils"

Encoding.default_external = Encoding::UTF_8

root = File.expand_path("..", __dir__)
RUN_DIR = File.join(root, "runs")

DEFAULT_TAGS = %w[
  MASTER_BASE_V8_5_IMPACT_4H
  MASTER_BASE_V8_5_IMPACT_C2
  MASTER_HYBRID_VF_20260708
  MASTER_TENDANCE_SENTINELLE_INVERSION_8H00
].freeze

CHOP_RADAR = 0.85
TREND_RADAR = 0.618
BASELINE_RADAR = 0.85

Row = Struct.new(
  :ts, :cycle, :side, :status, :pnl, :reason, :msg,
  :tension, :mom_bps, :spread_bps, :unit, :vortex_mode
)

def parse_row(cols, unit)
  ts, cycle, side, status, _entry, _exit_px, _qty, _bps, pnl, reason, _hold, msg = cols
  msg ||= ""
  tension = msg[/tension=([0-9.]+)/, 1]&.to_f || 0.0
  mom_bps = msg[/raw_mom_bps=([0-9.-]+)/, 1]&.to_f || msg[/mom_sig=([0-9.-]+)/, 1]&.to_f || 0.0
  spread = msg[/spread_bps=([0-9.]+)/, 1]&.to_f || 0.0
  vortex = msg[/vortex_mode=([A-Z]+)/, 1] || ""
  Row.new(ts, cycle.to_i, side, status, pnl.to_f, reason, msg, tension, mom_bps, spread, unit, vortex)
end

def load_unit_csv(path, unit, min_ts: nil)
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

def load_tag_rows(tag)
  beta = Dir.glob(File.join(RUN_DIR, "#{tag}_BETA*.csv")).max_by { |f| File.mtime(f) }
  alpha = Dir.glob(File.join(RUN_DIR, "#{tag}_ALPHA*.csv")).max_by { |f| File.mtime(f) }
  meta = File.join(RUN_DIR, "#{tag}_run_meta.json")
  min_ts = nil
  if File.file?(meta)
    min_ts = JSON.parse(File.read(meta))["start_utc"] rescue nil
  end
  rows = []
  rows.concat(load_unit_csv(beta, "BETA", min_ts: min_ts)) if beta
  rows.concat(load_unit_csv(alpha, "ALPHA", min_ts: min_ts)) if alpha
  rows.sort_by(&:ts)
end

def parse_ts(ts)
  Time.parse(ts)
rescue StandardError
  Time.at(0)
end

def regime_pnl_rule(filled_pnls)
  if filled_pnls.empty?
    { mode: "CHOP", radar: CHOP_RADAR, adj: 0.05, msg: "rule_no_trades" }
  else
    net = filled_pnls.sum
    if net > 0
      { mode: "TREND", radar: TREND_RADAR, adj: -0.05, msg: "rule_pnl_pos" }
    else
      { mode: "CHOP", radar: CHOP_RADAR, adj: 0.05, msg: "rule_pnl_neg" }
    end
  end
end

def regime_features(window_rows, filled_pnls)
  tensions = window_rows.map(&:tension).select { |t| t.positive? }
  tension_ma = tensions.empty? ? 0.0 : tensions.sum / tensions.size
  skip_rate = window_rows.empty? ? 1.0 : window_rows.count { |r| r.status == "SKIPPED" }.to_f / window_rows.size

  trend_proxy = 0.0
  if tensions.size >= 5
    first = tensions.first(tensions.size / 2).sum / (tensions.size / 2)
    last = tensions.last(tensions.size / 2).sum / (tensions.size - tensions.size / 2)
    trend_proxy = last - first
  end

  chop_score = (0.45 * (1.0 - [tension_ma / 1.2, 1.0].min)) +
               (0.35 * skip_rate) +
               (0.20 * (1.0 - [trend_proxy.abs / 0.5, 1.0].min))

  radar = (0.55 + 0.35 * chop_score).clamp(0.55, 0.90)
  mode = radar >= 0.75 ? "CHOP" : "TREND"
  adj = mode == "CHOP" ? 0.05 : -0.05
  { mode: mode, radar: radar.round(4), adj: adj, msg: "feat_chop=#{chop_score.round(3)}" }
end

def apply_adj(radar, adj)
  (radar + adj).clamp(0.20, 2.00).round(4)
end

def build_timeline(rows, interval_sec:, strategy:)
  return [] if rows.empty?

  t0 = parse_ts(rows.first.ts)
  t1 = parse_ts(rows.last.ts)
  slots = []
  t = t0
  while t <= t1
    slots << t
    t += interval_sec
  end

  filled_pnls = []
  window = []
  idx = 0

  slots.map do |slot_t|
    while idx < rows.size && parse_ts(rows[idx].ts) <= slot_t
      r = rows[idx]
      window << r
      window.shift while window.size > 120
      filled_pnls << r.pnl if r.status == "FILLED"
      filled_pnls.shift while filled_pnls.size > 40
      idx += 1
    end

    base = case strategy
           when :pnl then regime_pnl_rule(filled_pnls)
           when :features then regime_features(window, filled_pnls)
           when :static_trend then { mode: "TREND", radar: TREND_RADAR, adj: 0.0, msg: "static_trend" }
           when :static_chop then { mode: "CHOP", radar: CHOP_RADAR, adj: 0.0, msg: "static_chop" }
           when :baseline then { mode: "OFF", radar: BASELINE_RADAR, adj: 0.0, msg: "baseline_off" }
           else { mode: "CHOP", radar: CHOP_RADAR, adj: 0.0, msg: "unknown" }
           end

    eff = apply_adj(base[:radar], base[:adj])
    base.merge(effective_radar: eff, slot_ts: slot_t.utc.iso8601)
  end
end

def attach_thresholds(rows, timeline)
  return rows.map { |r| [r, BASELINE_RADAR, "OFF"] } if timeline.empty?

  out = []
  slot_i = 0
  cur = timeline.first
  rows.each do |row|
    rt = parse_ts(row.ts)
    while slot_i + 1 < timeline.size && parse_ts(timeline[slot_i + 1][:slot_ts]) <= rt
      slot_i += 1
      cur = timeline[slot_i]
    end
    out << [row, cur[:effective_radar], cur[:mode]]
  end
  out
end

def static_timeline(rows, strategy)
  base = case strategy
         when :static_trend then { mode: "TREND", radar: TREND_RADAR, adj: 0.0, msg: "static_trend" }
         when :static_chop then { mode: "CHOP", radar: CHOP_RADAR, adj: 0.0, msg: "static_chop" }
         else { mode: "OFF", radar: BASELINE_RADAR, adj: 0.0, msg: "baseline_off" }
         end
  eff = apply_adj(base[:radar], base[:adj])
  ts = rows.first ? rows.first.ts : Time.now.utc.iso8601
  [base.merge(effective_radar: eff, slot_ts: ts)]
end

def flip_stats(timeline)
  return { flips: 0, chop_pct: 0.0, trend_pct: 0.0, slots: 0 } if timeline.size < 2

  flips = 0
  timeline.each_cons(2) { |a, b| flips += 1 if a[:mode] != b[:mode] }
  chop = timeline.count { |s| s[:mode] == "CHOP" }
  trend = timeline.count { |s| s[:mode] == "TREND" }
  n = timeline.size.to_f
  { flips: flips, chop_pct: (chop / n * 100).round(1), trend_pct: (trend / n * 100).round(1), slots: timeline.size }
end

def nearest_filled_pnl(rows, from_idx, horizon_sec: 90)
  base_t = parse_ts(rows[from_idx].ts)
  ((from_idx + 1)...rows.size).each do |j|
    r = rows[j]
    next unless r.status == "FILLED"

    dt = parse_ts(r.ts) - base_t
    return r.pnl if dt >= 0 && dt <= horizon_sec
  end
  nil
end

def simulate_policy(rows, timeline)
  actual_pnl = rows.select { |r| r.status == "FILLED" }.sum(&:pnl)
  filled = rows.count { |r| r.status == "FILLED" }

  vacuum_skips = []
  extra_entries = []
  attached = attach_thresholds(rows, timeline)

  attached.each_with_index do |(row, th, _mode), idx|
    if row.reason == "vacuum_filter"
      if row.tension >= th
        proxy = nearest_filled_pnl(rows, idx)
        extra_entries << { row: row, proxy_pnl: proxy, threshold: th }
      end
      vacuum_skips << row
    end
  end

  shadow_pnl_filled = 0.0
  blocked_wins = 0.0
  blocked_losses = 0.0
  blocked_count = 0

  attached.each do |row, th, _mode|
    next unless row.status == "FILLED"

    if row.tension.positive? && row.tension < th
      blocked_count += 1
      blocked_losses += row.pnl.abs if row.pnl < 0
      blocked_wins += row.pnl if row.pnl > 0
    else
      shadow_pnl_filled += row.pnl
    end
  end

  proxy_extra_pnl = extra_entries.sum { |e| e[:proxy_pnl] || 0.0 }
  proxy_known = extra_entries.count { |e| !e[:proxy_pnl].nil? }
  tactic_rows = rows.count { |r| r.reason == "tactic_mismatch" }

  {
    actual_pnl: actual_pnl,
    filled: filled,
    vacuum_skips: vacuum_skips.size,
    extra_vacuum_pass: extra_entries.size,
    proxy_extra_pnl: proxy_extra_pnl,
    proxy_known: proxy_known,
    shadow_pnl_filled: shadow_pnl_filled,
    blocked_filled: blocked_count,
    blocked_wins: blocked_wins,
    blocked_losses: blocked_losses,
    tactic_mismatch: tactic_rows,
    shadow_pnl_total: shadow_pnl_filled + proxy_extra_pnl
  }
end

POLICIES = [
  { key: "baseline_off", label: "Sans Vortex (0.85 fixe)", interval: nil, strategy: :baseline },
  { key: "static_trend", label: "Radar fixe 0.618 (TREND permanent)", interval: nil, strategy: :static_trend },
  { key: "static_chop", label: "Radar fixe 0.85 (CHOP permanent)", interval: nil, strategy: :static_chop },
  { key: "v60_pnl", label: "Vortex 60s — PnL rule", interval: 60, strategy: :pnl },
  { key: "v15_pnl", label: "Vortex 15s — PnL rule", interval: 15, strategy: :pnl },
  { key: "v5_pnl", label: "Vortex 5s — PnL rule", interval: 5, strategy: :pnl },
  { key: "v5_features", label: "Vortex 5s — features marché", interval: 5, strategy: :features },
  { key: "v15_features", label: "Vortex 15s — features marché", interval: 15, strategy: :features }
].freeze

def run_tag(tag)
  rows = load_tag_rows(tag)
  return nil if rows.empty?

  duration_h = ((parse_ts(rows.last.ts) - parse_ts(rows.first.ts)) / 3600.0).round(2)
  results = {}

  POLICIES.each do |pol|
    timeline = if pol[:interval]
                 build_timeline(rows, interval_sec: pol[:interval], strategy: pol[:strategy])
               else
                 static_timeline(rows, pol[:strategy])
               end
    stats = flip_stats(timeline)
    sim = simulate_policy(rows, timeline)
    results[pol[:key]] = { policy: pol, timeline: timeline, flip: stats, sim: sim }
  end

  { tag: tag, rows: rows, duration_h: duration_h, results: results }
end

tags = ARGV.empty? ? DEFAULT_TAGS : ARGV
all = tags.map { |t| run_tag(t) }.compact

if all.empty?
  warn "Aucune donnée CSV pour les tags: #{tags.join(', ')}"
  exit 1
end

out_path = File.join(RUN_DIR, "VORTEX_SHADOW_SIM_#{Time.now.utc.strftime('%Y%m%d_%H%M%S')}.md")
link = File.join(RUN_DIR, "VORTEX_SHADOW_DERNIER.md")

lines = []
lines << "# Vortex SHADOW — simulation timing & intelligence"
lines << ""
lines << "> Mode **lecture seule** — replay CSV, pas de modification live"
lines << "> Généré: `#{Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ')}`"
lines << ""
lines << "## Méthode"
lines << ""
lines << "1. **Régime** recalculé toutes les N secondes (5 / 15 / 60) ou statique."
lines << "2. **PnL rule** : derniers FILLED → TREND si net > 0, sinon CHOP (comme supervisor V9)."
lines << "3. **Features** : tension moyenne + taux SKIP + dérivée tension → `radar_target` continu 0.55–0.90."
lines << "4. **Impact vacuum** : lignes `vacuum_filter` qui passeraient le nouveau seuil."
lines << "5. **Proxy PnL** : pour entrées supplémentaires, PnL du prochain FILLED dans les 90s (oracle optimiste/pessimiste selon corrélation)."
lines << "6. **Contrefactuel FILLED** : trades réels bloqués si tension < seuil vortex à ce moment."
lines << ""
lines << "_Limite : le radar domine souvent avant vacuum — impact vortex peut être faible sur vide froid actuel._"
lines << ""

all.each do |pack|
  tag = pack[:tag]
  rows = pack[:rows]
  filled = rows.count { |r| r.status == "FILLED" }
  actual = rows.select { |r| r.status == "FILLED" }.sum(&:pnl)
  vacuum = rows.count { |r| r.reason == "vacuum_filter" }
  radar = rows.count { |r| r.reason == "radar_block" }

  lines << "## `#{tag}`"
  lines << ""
  lines << "- Durée replay: **#{pack[:duration_h]} h** | Lignes: #{rows.size} | FILLED: #{filled} | PnL réel: **#{format('%.4f', actual)} USDT**"
  lines << "- SKIP radar_block: #{radar} | SKIP vacuum_filter: #{vacuum}"
  lines << ""
  lines << "### Comparatif politiques"
  lines << ""
  lines << "| Politique | Flips régime | %CHOP | %TREND | Extra vacuum pass | Proxy PnL extra | Shadow FILLED | Delta vs réel |"
  lines << "|-----------|--------------|-------|--------|-------------------|-----------------|---------------|---------------|"

  base_actual = actual
  pack[:results].each_value do |res|
    pol = res[:policy]
    f = res[:flip]
    s = res[:sim]
    delta = s[:shadow_pnl_total] - base_actual
    flip_s = pol[:interval] ? f[:flips].to_s : "—"
    chop_s = pol[:interval] ? "#{f[:chop_pct]}%" : "—"
    trend_s = pol[:interval] ? "#{f[:trend_pct]}%" : "—"
    lines << "| #{pol[:label]} | #{flip_s} | #{chop_s} | #{trend_s} | #{s[:extra_vacuum_pass]} (#{s[:proxy_known]} proxy) | #{format('%+.4f', s[:proxy_extra_pnl])} | #{format('%.4f', s[:shadow_pnl_filled])} | **#{format('%+.4f', delta)}** |"
  end

  lines << ""
  lines << "### Stabilité régime (5s vs 60s)"
  lines << ""
  %w[v5_pnl v15_pnl v60_pnl v5_features].each do |k|
    next unless pack[:results][k]

    f = pack[:results][k][:flip]
    pol = pack[:results][k][:policy]
    lines << "- **#{pol[:label]}** : #{f[:flips]} bascules / #{f[:slots]} slots (~#{(f[:flips] / [pack[:duration_h], 0.1].max).round(1)} /h)"
  end

  lines << ""
  best = pack[:results].max_by { |_, v| v[:sim][:shadow_pnl_total] - base_actual }
  worst = pack[:results].min_by { |_, v| v[:sim][:shadow_pnl_total] - base_actual }
  lines << "### Lecture rapide"
  lines << ""
  if vacuum.zero?
    lines << "- **Peu ou pas de `vacuum_filter`** sur ce cycle → le Vortex n'aurait presque pas changé les SKIP (radar en amont)."
  end
  lines << "- Meilleur scénario shadow: **#{best[1][:policy][:label]}** (#{format('%+.4f', best[1][:sim][:shadow_pnl_total] - base_actual)} USDT vs réel)."
  lines << "- Pire scénario shadow: **#{worst[1][:policy][:label]}** (#{format('%+.4f', worst[1][:sim][:shadow_pnl_total] - base_actual)} USDT vs réel)."
  lines << ""
end

lines << "## Synthèse globale"
lines << ""

deltas = {}
flip_rates = {}
all.each do |pack|
  pack[:results].each do |k, res|
    deltas[k] ||= []
    deltas[k] << res[:sim][:shadow_pnl_total] - pack[:rows].select { |r| r.status == "FILLED" }.sum(&:pnl)
    next unless res[:policy][:interval]

    flip_rates[k] ||= []
    flip_rates[k] << res[:flip][:flips] / [pack[:duration_h], 0.1].max
  end
end

lines << "| Politique | Delta PnL moyen (vs réel) | Flips/h moyen |"
lines << "|-----------|---------------------------|---------------|"
POLICIES.each do |pol|
  key = pol[:key]
  next unless deltas[key]&.any?

  avg_d = deltas[key].sum / deltas[key].size
  flip_s = if flip_rates[key]&.any?
             (flip_rates[key].sum / flip_rates[key].size).round(1).to_s
           else
             "—"
           end
  lines << "| #{pol[:label]} | **#{format('%+.4f', avg_d)}** USDT | #{flip_s} |"
end

lines << ""
lines << "## Recommandation simulation"
lines << ""

avg_v5 = deltas["v5_features"]&.sum.to_f / [deltas["v5_features"]&.size.to_i, 1].max
avg_v60 = deltas["v60_pnl"]&.sum.to_f / [deltas["v60_pnl"]&.size.to_i, 1].max
avg_trend = deltas["static_trend"]&.sum.to_f / [deltas["static_trend"]&.size.to_i, 1].max
flip5 = flip_rates["v5_pnl"]&.sum.to_f / [flip_rates["v5_pnl"]&.size.to_i, 1].max
flip60 = flip_rates["v60_pnl"]&.sum.to_f / [flip_rates["v60_pnl"]&.size.to_i, 1].max

if avg_trend < -1.0
  lines << "- **TREND permanent (0.618)** dégrade le PnL en moyenne → ne pas abaisser le radar en permanence."
elsif avg_trend > 0.5
  lines << "- **TREND permanent** améliore le shadow → le radar 0.85 est peut-être trop strict sur ces cycles."
else
  lines << "- **TREND permanent** : impact marginal en moyenne — le goulot n'est pas le seuil vacuum seul."
end

if flip5 > flip60 * 2
  lines << "- **5s vs 60s** : #{flip5.round(1)} flips/h vs #{flip60.round(1)} → accélérer sans hystérésis = plus nerveux."
end

if avg_v5 > avg_v60 + 0.3
  lines << "- **Features 5s** bat **PnL 60s** en moyenne → prioriser signaux marché plutôt que PnL retardé."
elsif avg_v5 < avg_v60 - 0.3
  lines << "- **Features 5s** sous-performe **PnL 60s** → les features proxy sont trop bruitées sur ces CSV."
else
  lines << "- **Features 5s vs PnL 60s** : différence faible — valider sur cycle dédié avant choix."
end

lines << "- **Prochaine étape suggérée** : cycle testnet A/B `VORTEX_CONTROL_ENABLED=TRUE` avec supervisor **15s features + hystérésis**, pas 5s PnL seul."
lines << ""

File.write(out_path, lines.join("\n"))
FileUtils.cp(out_path, link)

puts "VORTEX_SIM_OK: #{out_path}"
all.each do |pack|
  actual = pack[:rows].select { |r| r.status == "FILLED" }.sum(&:pnl)
  best = pack[:results].max_by { |_, v| v[:sim][:shadow_pnl_total] - actual }
  puts "#{pack[:tag]}: actual=#{format('%.4f', actual)} best=#{best[1][:policy][:label]} delta=#{format('%+.4f', best[1][:sim][:shadow_pnl_total] - actual)}"
end
