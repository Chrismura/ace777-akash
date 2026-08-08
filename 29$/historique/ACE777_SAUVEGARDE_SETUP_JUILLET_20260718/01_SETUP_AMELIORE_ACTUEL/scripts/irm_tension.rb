#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
#
# IRM — Indice de Régime de Marché (proxy tension) — LECTURE SEULE
# A2 léger : n'écrit aucun ordre, ne touche pas genesis, pas de SKIP live.
#
# Usage:
#   ruby scripts/irm_tension.rb boot [BETA_CSV] [N=50]
#   ruby scripts/irm_tension.rb report --csv BETA_CSV [--min-ts UTC] [--markdown]
#   ruby scripts/irm_tension.rb json --csv BETA_CSV [--min-ts UTC] [--window 50]
#
# Seuils (env, optionnels) — proxy microstructure, PAS un modèle ARCH Engle:
#   IRM_T_COMPRESSED=0.05   IRM_T_CLUSTER=1.0

require "json"
require "time"

module IrmTension
  module_function

  T_COMPRESSED = (ENV["IRM_T_COMPRESSED"] || "0.05").to_f
  T_CLUSTER    = (ENV["IRM_T_CLUSTER"] || "1.0").to_f

  REGIMES = %w[COMPRESSE TRANSITOIRE CLUSTER].freeze

  def classify(tension)
    t = tension.to_f
    return "COMPRESSE" if t < T_COMPRESSED
    return "CLUSTER" if t >= T_CLUSTER

    "TRANSITOIRE"
  end

  def extract_tension(msg, exit_reason = "")
    blob = "#{msg} #{exit_reason}"
    if (m = blob.match(/tension=([0-9.eE+-]+)/))
      return m[1].to_f
    end
    0.0
  end

  # rows: [{ts:, cycle:, status:, tension:, pnl:, filled:}]
  def load_rows(path, min_ts: nil)
    rows = []
    return rows unless path && File.file?(path)

    File.foreach(path).with_index do |line, idx|
      next if idx.zero?

      cols = line.strip.split(",", -1)
      next if cols.size < 10

      ts = cols[0].to_s
      next if min_ts && !ts.empty? && ts < min_ts

      status = cols[3].to_s
      side = cols[2].to_s
      skipped = status == "SKIPPED" || side == "SKIP"
      filled = status == "FILLED"
      tension = extract_tension(cols[11].to_s, cols[9].to_s)
      # holdSec sometimes at [10], msg at [11] — also try [10] if looks like msg
      if tension.zero? && cols[10].to_s.include?("tension=")
        tension = extract_tension(cols[10].to_s, "")
      end

      rows << {
        ts: ts,
        cycle: cols[1].to_s,
        status: status,
        tension: tension,
        pnl: cols[8].to_f,
        filled: filled,
        skipped: skipped,
        regime: classify(tension)
      }
    end
    rows
  end

  def summarize(rows)
    counts = Hash.new(0)
    pnl_by = Hash.new(0.0)
    fills_by = Hash.new(0)
    rows.each do |r|
      counts[r[:regime]] += 1
      next unless r[:filled]

      fills_by[r[:regime]] += 1
      pnl_by[r[:regime]] += r[:pnl]
    end
    n = rows.size
    pct = {}
    REGIMES.each do |name|
      pct[name] = n.zero? ? 0.0 : (100.0 * counts[name] / n)
    end
    tensions = rows.map { |r| r[:tension] }
    mean = tensions.empty? ? 0.0 : tensions.sum / tensions.size
    var = if tensions.size < 2
            0.0
          else
            tensions.map { |t| (t - mean)**2 }.sum / (tensions.size - 1)
          end
    std = Math.sqrt(var)
    # régime "courant" = majorité des 10 derniers, sinon majorité globale
    tail = rows.last([10, rows.size].min)
    tail_counts = Hash.new(0)
    tail.each { |r| tail_counts[r[:regime]] += 1 }
    current = (tail_counts.max_by { |_, v| v } || ["TRANSITOIRE", 0]).first
    {
      n: n,
      counts: counts,
      pct: pct,
      pnl_by: pnl_by,
      fills_by: fills_by,
      mean: mean,
      std: std,
      current: current,
      last_ts: rows.empty? ? nil : rows.last[:ts],
      first_ts: rows.empty? ? nil : rows.first[:ts]
    }
  end

  def label_fr(regime)
    case regime
    when "COMPRESSE" then "COMPRESSÉ (attente à froid)"
    when "TRANSITOIRE" then "TRANSITOIRE (bruit retail)"
    when "CLUSTER" then "CLUSTER (tension haute — proxy)"
    else regime
    end
  end

  def boot_line(csv_path, window = 50)
    rows = load_rows(csv_path)
    if rows.empty?
      return "IRM météo: n/a (pas encore de cycles BETA dans #{File.basename(csv_path.to_s)}) — proxy tension lecture seule"
    end

    slice = rows.last(window)
    s = summarize(slice)
    format(
      "IRM météo (proxy tension, %d cycles): %s | COMPRESSÉ %.0f%% · TRANSITOIRE %.0f%% · CLUSTER %.0f%% | μ=%.4f σ=%.4f | seuils <%.2f / ≥%.2f | LECTURE SEULE",
      s[:n],
      label_fr(s[:current]),
      s[:pct]["COMPRESSE"],
      s[:pct]["TRANSITOIRE"],
      s[:pct]["CLUSTER"],
      s[:mean],
      s[:std],
      T_COMPRESSED,
      T_CLUSTER
    )
  end

  def markdown_section(csv_path, min_ts: nil)
    rows = load_rows(csv_path, min_ts: min_ts)
    s = summarize(rows)
    lines = []
    lines << "## IRM — régimes de tension (proxy, lecture seule)"
    lines << ""
    lines << "> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. " \
             "N'influence pas le moteur. Seuils: COMPRESSÉ `< #{T_COMPRESSED}` · " \
             "CLUSTER `≥ #{T_CLUSTER}` · sinon TRANSITOIRE."
    lines << ""
    if s[:n].zero?
      lines << "*Aucun cycle dans la fenêtre session — IRM indisponible.*"
      return lines.join("\n")
    end

    lines << "| Régime | Cycles | % temps | Fills | PnL fills (USDT) |"
    lines << "|--------|--------|---------|-------|------------------|"
    REGIMES.each do |name|
      lines << format(
        "| %s | %d | %.1f%% | %d | %+.4f |",
        label_fr(name),
        s[:counts][name],
        s[:pct][name],
        s[:fills_by][name],
        s[:pnl_by][name]
      )
    end
    lines << ""
    lines << format(
      "- Fenêtre: `%s` → `%s` (%d cycles) · μ(tension)=%.4f · σ=%.4f · courant(proxy)=**%s**",
      s[:first_ts],
      s[:last_ts],
      s[:n],
      s[:mean],
      s[:std],
      label_fr(s[:current])
    )
    lines << "- Source: `#{File.basename(csv_path)}`"
    lines.join("\n")
  end
end

if $PROGRAM_NAME == __FILE__
  cmd = ARGV[0] || "boot"
  case cmd
  when "boot"
    csv = ARGV[1] || ENV.fetch("IRM_BETA_CSV", "runs/NUAGE_PROD_4H_BETA_X5.csv")
    n = (ARGV[2] || ENV.fetch("IRM_WINDOW", "50")).to_i
    n = 50 if n <= 0
    puts IrmTension.boot_line(csv, n)
  when "report"
    csv = nil
    min_ts = nil
    markdown = false
    i = 1
    while i < ARGV.size
      case ARGV[i]
      when "--csv" then csv = ARGV[i + 1]; i += 2
      when "--min-ts" then min_ts = ARGV[i + 1]; i += 2
      when "--markdown" then markdown = true; i += 1
      else i += 1
      end
    end
    csv ||= ENV.fetch("IRM_BETA_CSV", "runs/NUAGE_PROD_4H_BETA_X5.csv")
    if markdown
      puts IrmTension.markdown_section(csv, min_ts: min_ts)
    else
      rows = IrmTension.load_rows(csv, min_ts: min_ts)
      puts JSON.pretty_generate(IrmTension.summarize(rows))
    end
  when "json"
    csv = ARGV[1] || ENV.fetch("IRM_BETA_CSV", "runs/NUAGE_PROD_4H_BETA_X5.csv")
    min_ts = ENV["IRM_MIN_TS"]
    rows = IrmTension.load_rows(csv, min_ts: min_ts)
    puts JSON.pretty_generate(IrmTension.summarize(rows))
  else
    warn "Usage: irm_tension.rb boot|report|json"
    exit 1
  end
end
