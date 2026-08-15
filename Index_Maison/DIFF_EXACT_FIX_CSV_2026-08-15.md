# DIFF EXACT — correctif CSV (16 lignes) — généré depuis le fichier réel

Règle : insérer un champ après le 10e (exitReason).
FILLED → `$hold_done` · autres → champ vide.

## L1523  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,gap_guard_pause,reason=battery_wake pause_sec=${rem}" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,gap_guard_pause,,reason=battery_wake pause_sec=${rem}" >> "$LOG_FILE"
```

## L1537  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,duo_partner_pause,reason=partner_stale pause_sec=${rem} neighbor_age=${swarm_neighbor_age_sec:-?}" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,duo_partner_pause,,reason=partner_stale pause_sec=${rem} neighbor_age=${swarm_neighbor_age_sec:-?}" >> "$LOG_FILE"
```

## L1706  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,hashrate_block,reason=$hr_reason delta_pct=$hr_delta" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,hashrate_block,,reason=$hr_reason delta_pct=$hr_delta" >> "$LOG_FILE"
```

## L1801  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,radar_block,reason=$radar_reason conf=$radar_conf mom_sig=$momentum_signal raw_mom_bps=$mom_bps spread_bps=$spread_bps tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct swarm=$swarm_velocity_boost_active" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,radar_block,,reason=$radar_reason conf=$radar_conf mom_sig=$momentum_signal raw_mom_bps=$mom_bps spread_bps=$spread_bps tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct swarm=$swarm_velocity_boost_active" >> "$LOG_FILE"
```

## L1813  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,impulse_resonance_wait,reason=wall_not_collapsed tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,impulse_resonance_wait,,reason=wall_not_collapsed tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct" >> "$LOG_FILE"
```

## L1821  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,vacuum_filter,reason=cold_absolute tension=$tension_score threshold=$cycle_vacuum_threshold vortex_mode=$vortex_mode" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,vacuum_filter,,reason=cold_absolute tension=$tension_score threshold=$cycle_vacuum_threshold vortex_mode=$vortex_mode" >> "$LOG_FILE"
```

## L1835  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,tactic_mismatch,mom=$mom_direction structure=$structure_direction" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,tactic_mismatch,,mom=$mom_direction structure=$structure_direction" >> "$LOG_FILE"
```

## L1851  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,stase_ecoute,reason=spread_or_volat_not_cold spread_bps=$spread_bps volat=$impulse_abs_bps_s" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,stase_ecoute,,reason=spread_or_volat_not_cold spread_bps=$spread_bps volat=$impulse_abs_bps_s" >> "$LOG_FILE"
```

## L1869  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,OBSERVE,NA,$p1,$p2,0,$mom_bps,0,observe_only,mom_sig=$momentum_signal impulse_bps_s=$impulse_bps_s angle=$rupture_angle_deg" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,OBSERVE,NA,$p1,$p2,0,$mom_bps,0,observe_only,,mom_sig=$momentum_signal impulse_bps_s=$impulse_bps_s angle=$rupture_angle_deg" >> "$LOG_FILE"
```

## L1931  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,duo_wait,reason=$duo_reason mode=$duo_mode_note" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,duo_wait,,reason=$duo_reason mode=$duo_mode_note" >> "$LOG_FILE"
```

## L1981  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,$side,$p2,,$qty,0,0,qty_too_small,min=$lot_min" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,$side,$p2,,$qty,0,0,qty_too_small,,min=$lot_min" >> "$LOG_FILE"
```

## L2039  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,llm_gate,reason=${llm_gate_reason} status=${llm_gate_status} tension=$tension_score" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,llm_gate,,reason=${llm_gate_reason} status=${llm_gate_status} tension=$tension_score" >> "$LOG_FILE"
```

## L2067  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,ENTRY_ERROR,$side,$p2,,$qty_25,0,0,entry_error,code=$entry_code msg=$msg" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,ENTRY_ERROR,$side,$p2,,$qty_25,0,0,entry_error,,code=$entry_code msg=$msg" >> "$LOG_FILE"
```

## L2119  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,ENTRY_ERROR,$side,$p2,,$qty,0,0,entry_error,code=$entry_code msg=$msg" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,ENTRY_ERROR,$side,$p2,,$qty,0,0,entry_error,,code=$entry_code msg=$msg" >> "$LOG_FILE"
```

## L2441  (insertion vide, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,EXIT_ERROR,$side,$entry_price,,$qty,$current_bps,0,$reason,code=$exit_code msg=$msg" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,EXIT_ERROR,$side,$entry_price,,$qty,$current_bps,0,$reason,,code=$exit_code msg=$msg" >> "$LOG_FILE"
```

## L2507  (insertion $hold_done, +1 virgule: OK)
```diff
-echo "$(date -u +%FT%TZ),$i,$side,FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,radar=$radar_direction conf=$radar_conf size_note=$dynamic_size_note soft=$cycle_soft_mode pct=$pct tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct" >> "$LOG_FILE"
+echo "$(date -u +%FT%TZ),$i,$side,FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,$hold_done,radar=$radar_direction conf=$radar_conf size_note=$dynamic_size_note soft=$cycle_soft_mode pct=$pct tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct" >> "$LOG_FILE"
```
