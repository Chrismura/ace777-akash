# [PARTIE 2] — BILAN SÉMANTIQUE ET PARAMÈTRES DU SETUP DE BASE (SHORT/LONG)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  
**ADN:** genesis md5 `37fca367`

---

## 2.1. Code d'Usine et Cloisonnement Directionnel

### Exports BETA — SCOUT strictement SHORT x5 (200 USDT)

```bash
launch_beta() {
  (
    trap '' PIPE
    set +o pipefail
    export LOG_FILE="$LOG_BETA"
    export STOP_FILE="STOP_BETA"
    export DUO_STATE_FILE DUO_SESSION_FILE VORTEX_CONTROL_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export LEVERAGE="${BETA_LEVERAGE_OVERRIDE:-5}"
    export BUY_USDT="${BUY_USDT_BETA:-200}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_BETA:-0.70}"
    export FORCE_ENTRY_SIDE="SELL"
    export POSITION_SIDE="SHORT"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_BETA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export DUO_V63_ALARM_BPS="-3"
    run_unit "BETA_X5"
  ) &
  PID_BETA_WRAPPER=$!
  echo "$PID_BETA_WRAPPER" > "${RUN_DIR}/beta_wrapper.pid"
}
```

### Exports ALPHA — HUNTER strictement LONG x13 fixe (800 USDT)

```bash
launch_alpha() {
  NUAGE_ALPHA_BOOT_EPOCH="$(date +%s)"
  date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}"

  (
    export LOG_FILE="$LOG_ALPHA"
    export STOP_FILE="STOP_ALPHA"
    export DUO_STATE_FILE DUO_SESSION_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
    export ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
    export LEVERAGE="13"
    export LEVERAGE_RAMP_ENABLED="TRUE"
    export LEVERAGE_RAMP_START="13"
    export LEVERAGE_RAMP_END="13"
    export LEVERAGE_RAMP_CYCLES="180"
    export BUY_USDT="${BUY_USDT_ALPHA:-800}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_ALPHA:-0.50}"
    export FORCE_ENTRY_SIDE="BUY"
    export POSITION_SIDE="LONG"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"
    export DUO_V6_BURST_X13="TRUE"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_ALPHA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export RUN_STATE_ENABLED="TRUE"
    export RUN_STATE_LINK_TOTAL_PNL="TRUE"
    run_unit "ALPHA_X13_BURST13"
  ) &
  PID_ALPHA_WRAPPER=$!
  echo "$PID_ALPHA_WRAPPER" > "${RUN_DIR}/alpha_wrapper.pid"
}
```

### Règle mathématique anti-cannibalisation

| Agent | `FORCE_ENTRY_SIDE` | `POSITION_SIDE` | `DUO_ROLE` | Masse × Levier | Effet |
|---|---|---|---|---|---|
| BETA | SELL | SHORT | SCOUT | 200 × x5 | Éclaireur vendeur — publie `duo_state.json` |
| ALPHA | BUY | LONG | HUNTER | 800 × x13 | Chasseur acheteur — lit duo, ne vend jamais en scout |

**Conflit éradiqué:** BETA SHORT + ALPHA LONG → jamais deux ordres même sens sur même jambe hedge.  
ALPHA ne peut pas « manger » la position BETA ; elle **réagit** au signal duo après publication RAM.

**Formule gate:** `allow_revenge ⟺ (status=CLOSED ∧ pnl < 0 ∧ reason ∈ revenge_reasons)`  
**Formule blocage flat:** `pnl = 0 → closed_loss = false → allow = false, reason = no_trigger`

---

## 2.2. La Physique du Transfert d'Énergie (The Shockwave)

### Séquence d'armement

```
1. BETA entre SELL @ tension élevée
2. BETA sort avec pnl < 0 (closed_loss) + reason ∈ revenge_reasons
3. duo_publish_state() → /tmp/ace777_ram_exchange/duo_state.json
4. swarm_broadcast_shockwave() → swarm_telemetry.json
5. ALPHA lit duo_hunter_signal() → mode=revenge, mult=1.5x
6. nuage_cloud_tension_gate() → age duo_state < 800ms
7. ALPHA BUY hunter_revenge au prix de marché post-choc
```

### `nuage_cloud_tension_gate()` — preamble NUAGE

```bash
nuage_cloud_tension_gate() {
  local cycle="$1"
  local max_age="${NUAGE_TENSION_MAX_AGE_MS:-800}"
  local age_ms path
  duo_is_hunter || return 0
  path="${DUO_STATE_FILE:-runs/duo_state.json}"
  age_ms="$(ruby -rjson -e '
    path = ARGV[0]
    begin
      j = JSON.parse(File.read(path))
      ts = (j["ts_ms"].to_i rescue 0)
      age = ((Time.now.to_f * 1000).to_i - ts)
      age = 0 if age < 0
      print(age)
    rescue
      print(999999)
    end
  ' -- "$path" 2>/dev/null || echo 999999)"
  if [ "$age_ms" -gt "$max_age" ]; then
    echo "$(date -u +%FT%TZ),${cycle},SKIP,SKIPPED,,,,,0,tension_stale,reason=nuage_age_ms=${age_ms} thresh=${max_age}" >> "$LOG_FILE"
    sk_lev="$C_C"; num_ge "$current_leverage" "13" && sk_lev="$C_G"; num_le "$current_leverage" "5" && sk_lev="$C_Y"
    echo "${C_C}$(date -u +%H:%M:%S)${C_N} ${sk_lev}x$current_leverage${C_N} ${C_C}#${cycle}${C_N} SKIP ${C_Y}| tension_stale age=${age_ms}ms>${max_age}ms (NUAGE)${C_N}"
    alpha_touch_heartbeat
    return 1
  fi
  return 0
}
```

### `swarm_broadcast_shockwave()` — genesis_manifest.txt

```bash
swarm_broadcast_shockwave() {
  local cycle="$1" reason="$2"
  [ "$SWARM_COUPLING_ENABLED" = "TRUE" ] || return 0
  local key
  key="$(swarm_agent_key)"
  [ "$key" = "solo" ] && return 0
  SWARM_TELEMETRY_FILE="$SWARM_TELEMETRY_FILE" SWARM_SHOCKWAVE_CYCLES="$SWARM_SHOCKWAVE_CYCLES" \
    ruby "./scripts/swarm_telemetry.rb" shockwave \
      --from "$key" --cycle "$cycle" --duration "$SWARM_SHOCKWAVE_CYCLES" 2>/dev/null || true
  echo "${C_Y}SWARM shockwave${C_N} ${C_N}| $key -> neighbor (${reason})${C_N}"
}
```

### `duo_hunter_signal()` — genesis_manifest.txt (INTÉGRAL)

```bash
duo_hunter_signal() {
  duo_is_hunter || {
    echo "allow=true mode=disabled forced=AUTO mult=1.0 reason=duo_off"
    return 0
  }
  ruby -rjson -e '
    path=ARGV[0]
    ttl=(Integer(ARGV[1]) rescue 20)
    suffer_bps=(Float(ARGV[2]) rescue -5.0)
    suffer_usdt=(Float(ARGV[3]) rescue -0.5)
    require_sl=(ARGV[4] == "TRUE")
    revenge_mult=ARGV[5]
    force_opp=(ARGV[6] == "TRUE")
    sens_boost=(ARGV[7] == "TRUE")
    fast_death_sec=(Integer(ARGV[8]) rescue 30)
    boost_mult=(Float(ARGV[9]) rescue 0.5)
    boost_ttl_sec=(Integer(ARGV[10]) rescue 40)
    burst_on=(ARGV[11] == "TRUE")
    burst_mult=ARGV[12]
    burst_min_loss=(Float(ARGV[13]) rescue 15.0)
    burst_min_speed=(Float(ARGV[14]) rescue 0.5)
    burst_cooldown=(Integer(ARGV[15]) rescue 188)
    burst_file=ARGV[16]
    require_true_vacuum=(ARGV[17] == "TRUE")
    begin
      j=JSON.parse(File.read(path))
    rescue
      puts "allow=false mode=none forced=AUTO mult=1.0 reason=no_state boost=1.0 scout_bps=0 scout_hold=0"
      exit 0
    end
    age=((Time.now.to_f*1000).to_i - (j["ts_ms"].to_i rescue 0))
    if age > ttl*1000
      puts "allow=false mode=none forced=AUTO mult=1.0 reason=stale_state boost=1.0 scout_bps=0 scout_hold=0"
      exit 0
    end
    side=j["side"].to_s
    forced="AUTO"
    if force_opp
      forced = (side == "BUY" ? "SELL" : (side == "SELL" ? "BUY" : "AUTO"))
    end
    status=j["status"].to_s
    bps=(Float(j["bps"]) rescue 0.0)
    pnl=(Float(j["pnl_usdt"]) rescue 0.0)
    reason=j["reason"].to_s
    hold_sec=(Integer(j["hold_sec"]) rescue 0)
    suffer = (status == "OPEN") && (bps <= suffer_bps || pnl <= suffer_usdt)
    closed_loss = (status == "CLOSED") && pnl < 0.0
    revenge_reasons = %w[stop_loss shock_inversion_stop shock_exit_10bps fluid_exit_inversion fluid_exit_brake beta_sentinel_cut]
    revenge = closed_loss && (!require_sl || revenge_reasons.include?(reason))
    fast_death = closed_loss && hold_sec > 0 && hold_sec <= fast_death_sec
    speed_bps_s = hold_sec > 0 ? (bps.abs / hold_sec.to_f) : 0.0
    out_mode="none"
    out_mult="1.0"
    out_reason="no_trigger"
    out_allow=false
    out_boost=1.0
    vacuum_strike = (status == "OPEN" && reason == "true_vacuum")
    if require_true_vacuum && !vacuum_strike
      puts "allow=false mode=none forced=AUTO mult=1.0 reason=no_true_vacuum boost=1.0 scout_bps=#{bps} scout_hold=#{hold_sec}"
      exit 0
    end
    if vacuum_strike
      out_allow=true
      out_mode="vacuum_strike"
      out_mult="1.0"
      out_reason=reason
      puts "allow=#{out_allow} mode=#{out_mode} forced=#{forced} mult=#{out_mult} reason=#{out_reason} boost=#{out_boost} scout_bps=#{bps} scout_hold=#{hold_sec}"
      exit 0
    end
    if revenge
      out_allow=true
      out_mode="revenge"
      out_mult=revenge_mult
      out_reason=reason
      if burst_on && bps <= -burst_min_loss && speed_bps_s >= burst_min_speed
        cooldown_ok=true
        begin
          bj=JSON.parse(File.read(burst_file))
          last_ms=(bj["last_burst_ms"].to_i rescue 0)
          now_ms=(Time.now.to_f*1000).to_i
          cooldown_ok = ((now_ms - last_ms) >= burst_cooldown*1000)
        rescue
          cooldown_ok=true
        end
        if cooldown_ok
          out_mode="burst"
          out_mult=burst_mult
          out_reason="burst_x13"
          begin
            File.write(burst_file, JSON.generate({"last_burst_ms"=>(Time.now.to_f*1000).to_i}))
          rescue
          end
        else
          out_reason="cooldown_revenge"
        end
      end
      if sens_boost && fast_death && age <= boost_ttl_sec*1000
        out_boost=boost_mult
      end
    elsif suffer
      out_allow=true
      out_mode="suffer"
      out_mult="1.0"
      out_reason=reason
    end
    puts "allow=#{out_allow} mode=#{out_mode} forced=#{forced} mult=#{out_mult} reason=#{out_reason} boost=#{out_boost} scout_bps=#{bps} scout_hold=#{hold_sec}"
  ' -- "$DUO_STATE_FILE" "$DUO_EVENT_TTL_SEC" "$DUO_SCOUT_SUFFER_BPS" "$DUO_SCOUT_SUFFER_USDT" "$DUO_HUNTER_REQUIRE_STOP_LOSS" "$DUO_HUNTER_REVENGE_MULT" "$DUO_FORCE_OPPOSITE" "$DUO_V6_SENSITIVITY_BOOST" "$DUO_V6_FAST_DEATH_SEC" "$DUO_V6_BOOST_MULT" "$DUO_V6_BOOST_TTL_SEC" "$DUO_V6_BURST_X13" "$DUO_V6_BURST_MULT" "$DUO_V6_BURST_MIN_LOSS_BPS" "$DUO_V6_BURST_MIN_SPEED_BPS_PER_SEC" "$DUO_V6_BURST_COOLDOWN_SEC" "$DUO_V6_BURST_FILE" "$DUO_HUNTER_REQUIRE_TRUE_VACUUM"
}
```

### Trade du 14 juillet 2026 — 12:47 UTC (+32,07 USDT en 7 s)

**LIVE log** (`logs_meches/trade_20260714_1247_LIVE.log`):

```
[ALPHA_X13_BURST13] [1;36m12:47:10[0m [1;32mx13[0m [1;36m#218[0m SKIP tension=[1;31m6.03930286[0m [0m| spread_too_wide [1;33mconf=0.5[0m
[ALPHA_X13_BURST13] [1;36m12:47:10[0m [1;32mx13[0m [1;36m#218[0m SKIP tension=[1;31m6.03930286[0m [0m| spread_too_wide [1;33mconf=0.5[0m
[ALPHA_X13_BURST13] [1;36m12:47:10[0m [1;32mx13[0m [1;36m#218[0m SKIP tension=[1;31m6.03930286[0m [0m| spread_too_wide [1;33mconf=0.5[0m
[BETA_X5] [1;36mentry=12:47:05@63553.30000000[0m [1;33mx5[0m [1;36m#490[0m [1;31mSELL[0m tension=[1;31m6.38500207[0m hold=[1;36m10[0ms sec=[1;36m10[0m [0m| exit=63566.90000000 [1;32mconf=0.9862[0m [1;36mexit_time=12:47:15[0m [1;31mpnl=-0.10472000 bps=-2.13993609 pct=-0.02139936% total=2.0492600000000003[0m
[BETA_X5] [1;36m12:47:24[0m [1;33mx5[0m [1;36m#491[0m SKIP tension=[1;36m0.33455436[0m [0m| wall_not_collapsed
[ALPHA_X13_BURST13] [1;36mentry=12:47:22@63582.60000000[0m [1;32mx13[0m [1;36m#219[0m [1;32mBUY[0m tension=[1;31m7.87418878[0m hold=[1;36m7[0ms sec=[1;36m7[0m [0m| exit=63663.40000000 [1;33mconf=0.6324[0m [1;36mexit_time=12:47:29[0m [1;32mpnl=32.06952000 bps=12.70787920 pct=0.12707879% total=34.11878[0m
```

**CSV BETA (déclencheur):**

```
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:16Z,490,SELL,FILLED,63553.30000000,63566.90000000,0.00770000,-2.13993609,-0.10472000,shock_inversion_stop,radar=long conf=0.9862 size_note=strong_conf_full+entry_25_75_full soft=1 pct=-0.02139936 tension=6.38500207 bid_drop=0.00049106 ask_drop=41.50251347
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:24Z,491,SKIP,SKIPPED,,,,,0,impulse_resonance_wait,reason=wall_not_collapsed tension=0.33455436 bid_drop=0.20909809 ask_drop=2.17460332
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:32Z,492,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.3032 mom_sig=0.36379311 raw_mom_bps=0.00000000 spread_bps=17.22790000 tension=0.36379311 bid_drop=0.08512811 ask_drop=2.36465524 swarm=1
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:40Z,493,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0009 mom_sig=0.00106305 raw_mom_bps=0.00000000 spread_bps=30.80390000 tension=0.00106305 bid_drop=0.00690980 ask_drop=0.00000000 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:47Z,494,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=1.00264671 raw_mom_bps=-29.51828734 spread_bps=15.15780000 tension=1.00264671 bid_drop=0.00003553 ask_drop=6.51720359 swarm=0
```

**CSV ALPHA (percussion):**

```
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:00Z,217,SKIP,SKIPPED,,,,,0,radar_block,reason=direction_unclear conf=0.0121 mom_sig=0.08388063 raw_mom_bps=0.62943258 spread_bps=1.48020000 tension=0.08388063 bid_drop=0.54522409 ask_drop=0.00000000 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:09Z,218,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=6.03930286 raw_mom_bps=0.00000000 spread_bps=11.04170000 tension=6.03930286 bid_drop=0.00000000 ask_drop=39.25546858 swarm=1
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:29Z,219,BUY,FILLED,63582.60000000,63663.40000000,0.39690000,12.70787920,32.06952000,shock_inversion_stop,radar=long conf=0.6324 size_note=hunter_revenge_1.5x+entry_25_75_full soft=0 pct=0.12707879 tension=7.87418878 bid_drop=0.00000000 ask_drop=51.18222707
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:38Z,220,SKIP,SKIPPED,,,,,0,radar_block,reason=direction_unclear conf=0.2383 mom_sig=0.19511999 raw_mom_bps=0.00000000 spread_bps=2.13740000 tension=0.19511999 bid_drop=0.00000000 ask_drop=1.26827996 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:46Z,221,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=0.92707116 raw_mom_bps=0.00000000 spread_bps=15.37780000 tension=0.92707116 bid_drop=0.00222078 ask_drop=6.02596256 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:55Z,222,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=1.24979589 raw_mom_bps=0.00000000 spread_bps=29.68630000 tension=1.24979589 bid_drop=0.07786069 ask_drop=8.12367326 swarm=0
```

**Chronologie:** BETA perte 12:47:15 → SWARM shockwave → ALPHA entry 12:47:22 → exit +32,07 12:47:29 (hold 7s, hunter_revenge_1.5x).

---

## 2.3. L'Impact des Sorties à l'Équilibre (Flat pnl=0)

### Condition code (`duo_hunter_signal`)

```ruby
closed_loss = (status == "CLOSED") && pnl < 0.0
revenge = closed_loss && (!require_sl || revenge_reasons.include?(reason))
```

**Si BETA sort flat (pnl=0.0):** `closed_loss = false` → `revenge = false` → `allow=false reason=no_trigger`.

### Observation soir 14/07 (tension 6+ mais duo bloqué)

```
[ALPHA_X13_BURST13] tension=7.15369223 | duo no_trigger
[ALPHA_X13_BURST13] tension=2.10859007 | duo no_trigger
```

**Explication:** la tension locale V8 (mur carnet) ≠ signal duo. ALPHA lit **`duo_state.json`** (état BETA post-trade), pas la tension instantanée. BETA peut afficher tension 6+ en SKIP radar tout en ayant dernier `duo_state` avec `pnl=0` ou sortie flat → **protection capital** : pas de chasse sans « cadavre » scout.

Exemple BETA flat même session (05:21 UTC 15/07):

```
2026-07-15T05:21:11Z,189,SELL,FILLED,64651.80000000,64651.80000000,...,-0.00000000,shock_inversion_stop,...
```

→ ALPHA reste en `duo no_trigger` malgré SWARM si pnl=0.
