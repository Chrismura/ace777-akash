#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: utf-8

require "json"
require "time"
require "fileutils"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

root = File.expand_path("..", __dir__)
run_dir = File.expand_path(ENV.fetch("RUN_DIR", "runs"), root)

tag = ENV["STATE_TAG"] || ENV["TEST_TAG_OVERRIDE"]
unless tag
  latest = Dir.glob(File.join(run_dir, "*_ALPHA_X13_BURST13.csv")).max_by { |f| File.mtime(f) }
  tag = latest ? File.basename(latest).sub(/_ALPHA_X13_BURST13\.csv\z/, "") : "MASTER_BASE_V8_5_IMPACT_4H"
end

alpha_csv = ENV["ALPHA_CSV"] || File.join(run_dir, "#{tag}_ALPHA_X13_BURST13.csv")
beta_csv = ENV["BETA_CSV"] || File.join(run_dir, "#{tag}_BETA_X5.csv")
out_path = File.join(run_dir, "DIAG_ALPHA_#{Time.now.utc.strftime('%Y%m%d_%H%M%S')}.md")
latest_link = File.join(run_dir, "DIAG_ALPHA_DERNIER.md")

def load_session_start(run_dir, tag)
  return ENV["RUN_START_UTC"] if ENV["RUN_START_UTC"] && !ENV["RUN_START_UTC"].empty?

  meta_path = File.join(run_dir, "#{tag}_run_meta.json")
  return nil unless File.file?(meta_path)

  JSON.parse(File.read(meta_path))["start_utc"]
rescue StandardError
  nil
end

session_start = load_session_start(run_dir, tag)

def parse_rows(path, min_ts: nil)
  rows = { skips: Hash.new(0), filled: 0, wins: 0, losses: 0, net: 0.0,
           exit_reasons: Hash.new(0), duo_sub: Hash.new(0), duo_modes: Hash.new(0) }
  return rows unless File.file?(path)

  File.foreach(path).with_index do |line, idx|
    next if idx.zero?

    cols = line.strip.split(",", -1)
    next if cols.size < 10

    _ts, _cycle, side, status, _e, _x, _q, _bps, pnl, reason, detail = cols
    next if min_ts && _ts && !_ts.empty? && _ts < min_ts

    if status == "SKIPPED" || side == "SKIP"
      key = reason.to_s.empty? ? "unknown" : reason
      rows[:skips][key] += 1
      if key == "duo_wait" && detail
        sub = detail[/reason=([^\s]+)/, 1] || "unknown"
        mode = detail[/mode=([^\s]+)/, 1] || "none"
        rows[:duo_sub][sub] += 1
        rows[:duo_modes][mode] += 1
      end
      next
    end
    next unless status == "FILLED"

    pnl_f = pnl.to_f
    rows[:filled] += 1
    rows[:net] += pnl_f
    rows[:wins] += 1 if pnl_f > 0
    rows[:losses] += 1 if pnl_f < 0
    exit_key = reason.to_s.empty? ? "unknown" : reason.split(",", 2).first
    rows[:exit_reasons][exit_key] += 1
  end
  rows
end

def pct(part, total)
  return "0.0%" if total.zero?

  format("%.1f%%", (part.to_f / total) * 100.0)
end

def top_lines(h, n = 8)
  h.sort_by { |_, v| -v }.first(n).map { |k, v| "- `#{k}` — **#{v}**" }
end

alpha = parse_rows(alpha_csv, min_ts: session_start)
beta = parse_rows(beta_csv, min_ts: session_start)
alpha_total_skips = alpha[:skips].values.sum
beta_total_skips = beta[:skips].values.sum
duo_wait_total = alpha[:skips]["duo_wait"] || 0

duo_ttl = ENV.fetch("DUO_EVENT_TTL_SEC", "20")
require_sl = ENV.fetch("DUO_HUNTER_REQUIRE_STOP_LOSS", "TRUE")
suffer_bps = ENV.fetch("DUO_SCOUT_SUFFER_BPS", "-5")
suffer_usdt = ENV.fetch("DUO_SCOUT_SUFFER_USDT", "-0.50")

# BETA exit reasons for hunter trigger analysis
beta_exits = beta[:exit_reasons]
shock_exits = (beta_exits["shock_inversion_stop"] || 0) + (beta_exits["shock_exit_10bps"] || 0)
stop_loss_exits = beta_exits["stop_loss"] || 0

now = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")

verdict = if alpha[:filled].zero?
            "CRITIQUE — ALPHA n'a exécuté aucun trade"
          elsif alpha[:filled] < 10
            "ALERTE — ALPHA quasi dormante"
          else
            "OK — ALPHA active"
          end

lines = []
lines << "# DIAGNOSTIC ALPHA — #{tag}"
lines << ""
lines << "> Généré: `#{now}` | Verdict: **#{verdict}**"
lines << ""
lines << "## Résumé"
lines << ""
lines << "| Métrique | ALPHA | BETA (référence) |"
lines << "|----------|-------|------------------|"
lines << "| FILLED | #{alpha[:filled]} | #{beta[:filled]} |"
lines << "| PnL net | #{format('%.4f', alpha[:net])} USDT | #{format('%.4f', beta[:net])} USDT |"
lines << "| SKIP total | #{alpha_total_skips} | #{beta_total_skips} |"
lines << "| duo_wait | #{duo_wait_total} (#{pct(duo_wait_total, alpha_total_skips)} des SKIP ALPHA) | #{beta[:skips]['duo_wait'] || 0} |"
lines << ""
lines << "## Entonnoir des gates — ALPHA"
lines << ""
lines << "Ordre dans `genesis_manifest.txt` : radar → tension/vacuum → tactic → stase → **duo** → qty → llm_gate → execute"
lines << ""
top_lines(alpha[:skips]).each { |l| lines << l }
lines << ""
lines << "## duo_wait — sous-raisons (cause #2 après radar)"
lines << ""
if duo_wait_total.zero?
  lines << "_Aucun duo_wait._"
else
  alpha[:duo_sub].sort_by { |_, v| -v }.each do |sub, count|
    lines << "- `#{sub}` — **#{count}** (#{pct(count, duo_wait_total)} des duo_wait)"
  end
end
lines << ""
lines << "### Lecture technique"
lines << ""
lines << "| Sous-raison | Signification |"
lines << "|-------------|---------------|"
lines << "| `stale_state` | `duo_state.json` trop vieux (> `DUO_EVENT_TTL_SEC=#{duo_ttl}s`) |"
lines << "| `no_trigger` | SCOUT pas en mode suffer/revenge/vacuum_strike |"
lines << "| `no_state` | fichier `duo_state.json` absent ou illisible |"
lines << "| `no_true_vacuum` | `DUO_HUNTER_REQUIRE_TRUE_VACUUM=TRUE` non satisfait |"
lines << ""
lines << "## Cause racine probable"
lines << ""
if require_sl == "TRUE"
  lines << "### 1. `DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE` (bloquant)"
  lines << ""
  lines << "Le HUNTER ne déclenche **revenge** que si le SCOUT ferme avec `reason=stop_loss`."
  lines << "Or les sorties BETA dominantes sont :"
else
  lines << "### 1. `DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE` (actif — revenge élargi)"
  lines << ""
  lines << "Revenge autorisé au-delà de `stop_loss` (shock / fluid / sentinel)."
  lines << "Sorties BETA observées :"
end
lines << ""
beta_exits.sort_by { |_, v| -v }.first(5).each { |r, c| lines << "- `#{r}` — #{c} trades" }
lines << ""
lines << "- Sorties `shock_inversion_stop` : **#{shock_exits}**"
lines << "- Sorties `stop_loss` : **#{stop_loss_exits}**"
lines << ""
if require_sl == "TRUE" && shock_exits > stop_loss_exits * 10
  lines << "**→ Le HUNTER attend des `stop_loss` que le SCOUT ne produit presque jamais.**"
  lines << "**→ Résultat : `no_trigger` sur #{alpha[:duo_sub]['no_trigger'] || 0} cycles.**"
end
lines << ""
lines << "### 2. `DUO_EVENT_TTL_SEC=#{duo_ttl}` (stale_state)"
lines << ""
lines << "Quand le SCOUT ne rafraîchit pas `duo_state.json` dans les #{duo_ttl}s, le HUNTER skip avec `stale_state`."
lines << "Observé : **#{alpha[:duo_sub]['stale_state'] || 0}** fois (#{pct(alpha[:duo_sub]['stale_state'] || 0, duo_wait_total)} des duo_wait)."
lines << ""
lines << "### 3. radar_block en amont (#{alpha[:skips]['radar_block'] || 0} SKIP)"
lines << ""
lines << "Même si le duo était parfait, #{pct(alpha[:skips]['radar_block'] || 0, alpha_total_skips)} des cycles ALPHA meurent au radar avant d'atteindre le HUNTER."
lines << ""
lines << "## Paramètres duo actifs (config)"
lines << ""
lines << "| Variable | Valeur |"
lines << "|----------|--------|"
lines << "| DUO_EVENT_TTL_SEC | `#{duo_ttl}` |"
lines << "| DUO_HUNTER_REQUIRE_STOP_LOSS | `#{require_sl}` |"
lines << "| DUO_SCOUT_SUFFER_BPS | `#{suffer_bps}` |"
lines << "| DUO_SCOUT_SUFFER_USDT | `#{suffer_usdt}` |"
lines << "| DUO_HUNTER_REQUIRE_TRUE_VACUUM | `#{ENV.fetch('DUO_HUNTER_REQUIRE_TRUE_VACUUM', 'FALSE')}` |"
lines << ""
lines << "## Recommandations (NON APPLIQUÉES — ordre requis)"
lines << ""
lines << "| Priorité | Action | Impact attendu |"
lines << "|----------|--------|----------------|"
lines << "| **P0** | `DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE` ou accepter `shock_inversion_stop` en revenge | Débloque revenge sur sorties BETA réelles |"
lines << "| **P1** | `DUO_EVENT_TTL_SEC=60` (ou 120) | Réduit `stale_state` |"
lines << "| **P2** | Rafraîchir `ts_ms` dans `duo_state.json` à chaque cycle SCOUT (même SKIP) | Élimine stale_state structurel |"
lines << "| **P3** | Revoir seuils radar ALPHA (`VACUUM_TENSION_THRESHOLD_ALPHA`) | Réduit radar_block en amont |"
lines << ""
lines << "## Fichiers analysés"
lines << ""
lines << "- `#{File.basename(alpha_csv)}`"
lines << "- `#{File.basename(beta_csv)}`"
lines << "- `runs/duo_state.json` (état live au moment du diag)"
lines << ""
lines << "---"
lines << "_Généré par `scripts/diagnostic_alpha.sh` — aucune constante modifiée._"

content = lines.join("\n") + "\n"
File.write(out_path, content)
File.write(latest_link, content)
puts "DIAG_ALPHA_OK: #{out_path}"
puts "DIAG_VERDICT: #{verdict}"
