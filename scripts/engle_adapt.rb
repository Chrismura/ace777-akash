#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8
#
# B2 — Engle adapt LOG-ONLY — ZÉRO impact moteur / pas de SKIP live.
#
# Env:
#   ENGLE_ADAPT=0     (défaut) → usine pure, message OFF
#   ENGLE_ADAPT=log   → calcule posture IRM, écrit runs/engle_adapt_posture.json
#
# Usage:
#   ruby scripts/engle_adapt.rb boot [BETA_CSV] [N=50]
#   ruby scripts/engle_adapt.rb status

require "json"
require "time"
require "fileutils"

root = File.expand_path("..", __dir__)
load File.join(root, "scripts", "irm_tension.rb")

module EngleAdapt
  module_function

  def mode
    m = ENV.fetch("ENGLE_ADAPT", "0").to_s.strip.downcase
    return "0" if m.empty? || m == "off" || m == "false"
    return "log" if %w[log 1 true yes].include?(m)

    m
  end

  def posture_for(regime)
    case regime
    when "COMPRESSE"
      {
        code: "WAIT_COLD",
        advice: "calme — ne pas assouplir; momentum_too_small attendu",
        knobs: {}
      }
    when "TRANSITOIRE"
      {
        code: "WATCH",
        advice: "bruit — usine inchangée",
        knobs: {}
      }
    when "CLUSTER"
      {
        code: "HUNT_WINDOW",
        advice: "cluster proxy — B3 knobs futurs seulement après GO",
        knobs: {}
      }
    else
      {
        code: "UNKNOWN",
        advice: "n/a",
        knobs: {}
      }
    end
  end

  def boot_line(csv_path, window = 50)
    m = mode
    if m == "0"
      return "ENGLE_ADAPT=OFF — posture usine pure (B2 inactif, rétroactif)"
    end

    unless m == "log"
      return "ENGLE_ADAPT=#{m} — mode inconnu (utiliser 0|log) — usine pure forcée"
    end

    rows = IrmTension.load_rows(csv_path)
    if rows.empty?
      payload = {
        mode: "log",
        applied: false,
        motor_impact: false,
        regime: nil,
        posture: "NO_DATA",
        advice: "pas encore de cycles BETA",
        knobs: {},
        ts_utc: Time.now.utc.iso8601,
        csv: csv_path.to_s
      }
      write_posture(payload)
      return "ENGLE_ADAPT=log — NO_DATA (IRM vide) · applied=false · moteur intact"
    end

    slice = rows.last(window)
    s = IrmTension.summarize(slice)
    p = posture_for(s[:current])
    payload = {
      mode: "log",
      applied: false,
      motor_impact: false,
      regime: s[:current],
      regime_label: IrmTension.label_fr(s[:current]),
      posture: p[:code],
      advice: p[:advice],
      knobs: p[:knobs],
      irm_pct: s[:pct],
      irm_mean: s[:mean],
      window: slice.size,
      ts_utc: Time.now.utc.iso8601,
      csv: File.basename(csv_path.to_s)
    }
    write_posture(payload)
    format(
      "ENGLE_ADAPT=log — posture=%s (%s) · COMPRESSÉ %.0f%% · applied=false · moteur intact",
      p[:code],
      IrmTension.label_fr(s[:current]),
      s[:pct]["COMPRESSE"]
    )
  end

  def write_posture(payload)
    run_dir = File.expand_path(ENV.fetch("RUN_DIR", "runs"), root_path)
    FileUtils.mkdir_p(run_dir)
    path = File.join(run_dir, "engle_adapt_posture.json")
    File.write(path, JSON.pretty_generate(payload))
    path
  end

  def root_path
    File.expand_path("..", __dir__)
  end

  def status_line
    path = File.join(root_path, ENV.fetch("RUN_DIR", "runs"), "engle_adapt_posture.json")
    return "ENGLE_ADAPT status: pas de fichier posture (#{mode})" unless File.file?(path)

    data = JSON.parse(File.read(path))
    format(
      "ENGLE_ADAPT status: posture=%s regime=%s applied=%s motor_impact=%s ts=%s",
      data["posture"],
      data["regime"],
      data["applied"],
      data["motor_impact"],
      data["ts_utc"]
    )
  end
end

if $PROGRAM_NAME == __FILE__
  cmd = ARGV[0] || "boot"
  case cmd
  when "boot"
    csv = ARGV[1] || ENV.fetch("IRM_BETA_CSV", File.join(EngleAdapt.root_path, "runs", "NUAGE_PROD_4H_BETA_X5.csv"))
    n = (ARGV[2] || ENV.fetch("IRM_WINDOW", "50")).to_i
    n = 50 if n <= 0
    puts EngleAdapt.boot_line(csv, n)
  when "status"
    puts EngleAdapt.status_line
  else
    warn "Usage: engle_adapt.rb boot|status"
    exit 1
  end
end
