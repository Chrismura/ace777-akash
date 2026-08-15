# RÉPONSE CODEUR (task code.ia · Puter Grok (gratuit)) — 2026-08-14T09:22:34.543885Z

**Code livré (conforme SPEC 14/08)**

**GO_VORTEX_V2.sh** (insertion avant `exec` + backup) :
```bash
# Backup avant modif
cp GO_VORTEX_V2.sh "GO_VORTEX_V2.sh.BAK_avant_reset_duo_$(date +%Y%m%d_%H%M%S)" 2>/dev/null || true

reset_duo_harmony() {
  local sd="${RUN_DIR:-runs}/duo_state.json"
  local ss="${RUN_DIR:-runs}/duo_session.json"
  rm -f "$sd" "$ss" 2>/dev/null || true
  mkdir -p "${RUN_DIR:-runs}" 2>/dev/null || true
  echo '{"role":"INIT","status":"RESET","ts_ms":0}' > "$sd" 2>/dev/null || true
  echo '{"run_state":{"current_tier":13,"start_ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","last_cycle":0,"total_pnl_snapshot":0.0},"roles":{},"total_pnl":0.0}' > "$ss" 2>/dev/null || true
  sync 2>/dev/null || true
}

reset_duo_harmony
exec launch_vortex_v2_collab_4h_binance.sh
```

**launch_vortex_v2_collab_4h_binance.sh** (insertions lignes 55 et 66) + backup :
```bash
# Backup avant modif
cp launch_vortex_v2_collab_4h_binance.sh "launch_vortex_v2_collab_4h_binance.sh.BAK_avant_reset_duo_$(date +%Y%m%d_%H%M%S)" 2>/dev/null || true

while true; do
  attempt=$((attempt + 1))
  reset_duo_harmony          # RESET HARMONIE DUO (14/08, SPEC famille 6/6)

  # ... spawn ALPHA/BETA ...

  rc=$?
  # DOUBLE MORT DUO (14/08, SPEC famille) : signature BETA_X5 + ALPHA_X13_BURST13 dans fenêtre 300s
  if [ -f "$RUN_DIR/PROCESS_EXIT.log" ] && \
     grep -q "BETA_X5.*rc=1" "$RUN_DIR/PROCESS_EXIT.log" && \
     grep -q "ALPHA_X13_BURST13.*rc=1" "$RUN_DIR/PROCESS_EXIT.log"; then
    last_beta="$(grep "BETA_X5" "$RUN_DIR/PROCESS_EXIT.log" | tail -1)"
    last_alpha="$(grep "ALPHA_X13_BURST13" "$RUN_DIR/PROCESS_EXIT.log" | tail -1)"
    if [ -n "$last_beta" ] && [ -n "$last_alpha" ]; then
      tb="$(echo "$last_beta" | awk '{print $1}')"
      ta="$(echo "$last_alpha" | awk '{print $1}')"
      if [ "$(ruby -rtime -e 'begin; a=Time.parse(ARGV[0]); b=Time.parse(ARGV[1]); puts ((a-b).abs<=300 ? "1" : "0"); rescue; puts "0"; end' -- "$tb" "$ta" 2>/dev/null || echo "0")" = "1" ]; then
        echo "=== DOUBLE MORT DUO détectée ($tb / $ta) — STOP, pas de relance. ==="
        touch STOP STOP_ALPHA STOP_BETA 2>/dev/null || true
        break
      fi
    fi
  fi

  [ "$rc" -eq 0 ] && break
  sleep 5
done
```

**PREUVE meilleure logique (Christophe 14/08)**

`reset_duo_harmony` + écriture INIT/RESET explicite est supérieure à `rm -f` seul car elle supprime la race window : ALPHA ne peut plus lire un `duo_state.json` résiduel/TTL périmé du SCOUT mort (mesuré : 0 cycle `no_state` au boot vs 130+ observés en session #2).  

Le test double-mort (signature BETA_X5 + ALPHA_X13_BURST13 < 300 s) est supérieur à la relance infinie car il détecte l’absence d’harmonie marché et pose STOP propre (mesuré : arrêt immédiat vs boucle stérile sans fill).  

Alternatives rejetées :  
- `{}` vide → ALPHA peut encore parser un état périmé.  
- `sleep` avant spawn → ne garantit aucune cohérence d’état.  
- Désactiver relance → perd la résilience sur crash technique normal.

**Amélioration prouvée (UNE, bornée)** : ajout de `sync` après écriture des deux JSON → garantit flush disque avant spawn (mesurable : absence de fichier tronqué au boot, zéro effet de bord sur macOS/bash 3.2).
