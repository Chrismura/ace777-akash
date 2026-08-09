#!/usr/bin/env bash
# Début de session Index — checklist, PAS de GO trading.
# Usage:
#   bash session_debut.sh           # auto (détecte VOL vs FROID)
#   bash session_debut.sh --froid   # force checks pré-run
#   bash session_debut.sh --vol     # lecture seule pendant run
#   bash session_debut.sh --open    # + ouvre cockpit (app native si dispo)
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
WS="$ROOT/Index_Maison"
PY=/usr/bin/python3
MODE="auto"
DO_OPEN=0
for a in "$@"; do
  case "$a" in
    --froid|--cold) MODE="froid" ;;
    --vol|--hot) MODE="vol" ;;
    --open) DO_OPEN=1 ;;
    -h|--help) sed -n '2,8p' "$0"; exit 0 ;;
  esac
done

# --- BOOT UNIQUE (ADDITIF, NON BLOQUANT) — A1b, integre 09/08 ---
# Appelle le boot unique boot.sh. Ne bloque JAMAIS la session : absent ou en echec -> WARN.
if [[ -x "$ROOT/scripts/boot.sh" ]]; then
  echo "7) BOOT UNIQUE — $ROOT/scripts/boot.sh"
  if bash "$ROOT/scripts/boot.sh"; then
    echo "BOOT=OK (voir $WS/BOOT_STATUS.md)"
  else
    echo "BOOT=WARN — echec non bloquant, session continue"
  fi
else
  echo "BOOT=SKIP — boot.sh absent"
fi
# Fin BOOT UNIQUE

ace_alive=0
if pgrep -f 'ace777_launch|launch_vide_froid|GO_USINE_NUAGE|ALPHA_X13|BETA_X5' >/dev/null 2>&1; then
  ace_alive=1
fi
live_fresh=0
LIVE=$(ls -t "$ROOT"/runs/*_LIVE_COLOR.log 2>/dev/null | head -1 || true)
if [[ -n "${LIVE:-}" ]]; then
  age=$(( $(date +%s) - $(stat -f %m "$LIVE") ))
  if [[ "$age" -le 90 ]]; then live_fresh=1; fi
fi

if [[ "$MODE" == "auto" ]]; then
  if [[ "$ace_alive" -eq 1 || "$live_fresh" -eq 1 ]]; then MODE="vol"; else MODE="froid"; fi
fi

echo "=== SESSION DÉBUT — mode=$MODE ==="
echo "heure: $(date -u +%Y-%m-%dT%H:%MZ) / $(date '+%H:%M:%S %Z')"
echo

echo "1) État Mac"
bash "$WS/scripts/etat_mac.sh" 2>&1 | head -40 || true
echo

echo "2) Hygiène RAM (orphelins WebKit)"
if [[ "$MODE" == "froid" ]]; then
  bash "$ROOT/scripts/hygiene_mac_ram.sh" 2>&1 | tail -12 || true
else
  bash "$ROOT/scripts/hygiene_mac_ram.sh" --check 2>&1 | tail -10 || true
  echo "(VOL: pas de purge agressive)"
fi
echo

echo "3) Stérilité / vol"
if [[ "$MODE" == "froid" ]]; then
  if "$ROOT/scripts/verif_sterilite.sh" --pre-run; then
    echo "STERILE=OK"
  else
    echo "STERILE=NOK — corriger avant GO trading"
  fi
else
  echo "MODE VOL — skip verif_sterilite --pre-run (ACE déjà en marche)"
  [[ "$ace_alive" -eq 1 ]] && echo "ACE process: ON" || echo "ACE process: ? (LIVE frais=$live_fresh)"
  [[ -n "${LIVE:-}" ]] && echo "LIVE: $(basename "$LIVE") age=${age:-?}s"
fi
echo "GENESIS: $(md5 -q "$ROOT/genesis_manifest.txt" 2>/dev/null | head -c 12)…"
echo

echo "4) Cockpit / thermo / pont"
"$PY" "$WS/scripts/thermo_quotidien_free.py" 2>&1 | tail -8 || true
if [[ "$MODE" == "froid" ]]; then
  bash "$WS/scripts/cockpit_hygiene_check.sh" || true
else
  # pendant vol: refresh feed sans exiger pont pour exit 0
  "$PY" "$WS/scripts/cockpit_mission_feed.py" 2>&1 | tail -6 || true
  if curl -sS --max-time 2 "http://127.0.0.1:17777/status" >/tmp/ace777_session_pont.json 2>/dev/null; then
    echo "PONT=ON"
    "$PY" -c 'import json;d=json.load(open("/tmp/ace777_session_pont.json"));a=d.get("ace") or {};n=d.get("net") or {};print("ACE",a.get("label"),"age",a.get("ageSec"),"| NET",n.get("label"),n.get("ms"),"ms")' 2>/dev/null || true
  else
    echo "PONT=OFF — python3 $WS/scripts/cortana_cockpit_bridge.py  OU  bash $WS/scripts/cockpit_up.sh --daemons"
  fi
fi
echo

echo "5) Plan / console (1 écran)"
echo "--- PLAN_DE_VOL (tête) ---"
head -n 25 "$WS/PLAN_DE_VOL.md" 2>/dev/null || true
echo
echo "--- CONSOLE (tête) ---"
head -n 20 "$WS/CONSOLE_GENERALE.md" 2>/dev/null || true
echo

if [[ "$DO_OPEN" -eq 1 ]]; then
  echo "6) Ouverture cockpit"
  if [[ -x "$WS/scripts/open_cockpit_app.sh" ]] || [[ -f "$WS/scripts/open_cockpit_app.sh" ]]; then
    bash "$WS/scripts/open_cockpit_app.sh" &
  elif [[ -f "$WS/scripts/open_cockpit_app.py" ]]; then
    "$PY" "$WS/scripts/open_cockpit_app.py" &
  else
    open "$WS/cockpit/index.html"
  fi
fi

# --- Réveil matin : sync vault + pont + hub + REVEIL_BUFFY (produit par Gemini, intégré Ada 07/08) ---
reveil_matin() {
    set -uo pipefail
    local vault="$HOME/Documents/Obsidian_ACE777"
    local outbox_script="$HOME/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh"
    local buffy_script="$vault/scripts/buffy_reveil.py"
    local v_status="NOK"
    if [ -d "$vault/.git" ]; then
        git -C "$vault" pull --rebase --autostash >/dev/null 2>&1 && v_status="OK" || v_status="NOK (err)"
    else
        v_status="N/A"
    fi
    local p_status="NOK"
    if [ -x "$outbox_script" ]; then
        "$outbox_script" >/dev/null 2>&1 && p_status="OK" || p_status="NOK (err)"
    else
        p_status="ABSENT"
    fi
    local h_status="NOK"
    curl -s --max-time 2 "http://127.0.0.1:11435/health" >/dev/null 2>&1 && \
    curl -s --max-time 2 "http://127.0.0.1:11434/api/tags" >/dev/null 2>&1 && h_status="OK"
    if [ -f "$buffy_script" ]; then
        "$PY" "$buffy_script" >/dev/null 2>&1 || true
    fi
    echo "--- RÉSUMÉ RÉVEIL MATIN ---"
    echo "VAULT : [$v_status] Obsidian_ACE777"
    echo "PONT  : [$p_status] OUTBOX_OBSIDIAN"
    echo "HUB   : [$h_status] Ollama (:11434) & Hub (:11435)"
}
reveil_matin

echo "=== SESSION DÉBUT FIN — mode=$MODE ==="
"$PY" "$WS/scripts/memoire_log.py" session_debut "★" "session" "début mode=$MODE" >/dev/null 2>&1 || true
echo "Rappel validation: portes P0 hygiène → P1 outils → P2 run test (PROTOCOLE_VALIDATION_TEST_AVANT_REEL)"
echo "Suite: GO trading = commande manuelle · backlog = CHOSES_A_FINIR_REVOIR (cosmétique = finition)"
echo "Docs: Index_Maison/PROTOCOLE_SESSION_DEBUT_FIN.md"
exit 0
