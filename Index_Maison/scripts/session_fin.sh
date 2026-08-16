#!/usr/bin/env bash
# Fin de session Index — snapshot + OUTBOX. NE TUE PAS ACE/Hulk (sauf --stop-ace GO explicite).
# Usage:
#   bash session_fin.sh
#   bash session_fin.sh --stop-ace   # seulement si tu as dit stop (appelle stop_ace777_hard)
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
WS="$ROOT/Index_Maison"
OB="$WS/OUTBOX_OBSIDIAN"
PY=/usr/bin/python3
DO_STOP_ACE=0
for a in "$@"; do
  case "$a" in
    --stop-ace) DO_STOP_ACE=1 ;;
    -h|--help) sed -n '2,6p' "$0"; exit 0 ;;
  esac
done

DAY_ISO=$(date +%Y-%m-%d)
JOURNAL="$WS/Journal_${DAY_ISO}.md"
JOURNAL_COMPACT="$WS/Journal_$(date +%Y%m%d).md"
TS_UTC=$(date -u +%Y-%m-%dT%H:%MZ)

echo "=== SESSION FIN — $TS_UTC ==="
echo

ace_vol=0
if pgrep -f 'ace777_launch|launch_vide_froid|GO_USINE_NUAGE|launch_vortex|ALPHA_X13|BETA_X5' >/dev/null 2>&1; then
  ace_vol=1
fi

if [[ "$DO_STOP_ACE" -eq 1 ]]; then
  echo "1) STOP ACE demandé (--stop-ace)"
  bash "$ROOT/stop_ace777_hard.sh" 2>&1 | tail -20 || true
else
  echo "1) ACE/Hulk : non touchés (pas de --stop-ace)"
  if [[ "$ace_vol" -eq 1 ]]; then
    echo "   ★ MODE NUIT / VOL LAISSÉ TOURNER — pas de purge"
    echo "   ⚠ ACE encore en VOL — fin de session Index seulement"
  else
    echo "   ACE process: OFF (froid)"
  fi
fi
echo

echo "2) Snapshot journal / console"
"$PY" "$WS/scripts/journal_auto.py" 2>&1 | tail -15 || true
# append fin session dans journal ISO (canon) + miroir compact
mkdir -p "$WS"
if [[ ! -f "$JOURNAL" ]]; then
  cat >"$JOURNAL" <<EOF
# Journal — ${DAY_ISO}

Tags: #journal #swarm

## Fait
EOF
fi
{
  echo ""
  echo "## Fin session auto ($TS_UTC)"
  echo "- Script \`session_fin.sh\`"
  if [[ "$DO_STOP_ACE" -eq 1 ]]; then
    echo "- ACE stop demandé"
  else
    echo "- ACE laissé tel quel (pas de kill)"
    [[ "$ace_vol" -eq 1 ]] && echo "- ★ Vol laissé tourner (nuit / prototype)"
  fi
  LIVE=$(ls -t "$ROOT"/runs/*_LIVE_COLOR.log 2>/dev/null | head -1 || true)
  [[ -n "${LIVE:-}" ]] && echo "- Dernier LIVE: \`$(basename "$LIVE")\`"
  echo "- Suite: [[PLAN_DE_VOL]] · [[CHOSES_A_FINIR_REVOIR]] · sync \`OUTBOX_OBSIDIAN/_sync_now.sh\`"
} >>"$JOURNAL"
cp -f "$JOURNAL" "$JOURNAL_COMPACT" 2>/dev/null || true
echo "JOURNAL=$JOURNAL"
echo

echo "3) Ligne mémoire collab"
NOTE="Fin session auto"
[[ "$ace_vol" -eq 1 && "$DO_STOP_ACE" -eq 0 ]] && NOTE="Fin session · VOL LAISSÉ TOURNER"
"$PY" "$WS/scripts/memoire_log.py" session_fin "★" "Index" "$NOTE · journal + OUTBOX" 2>&1 | tail -1 || true
echo

echo "4) Miroir OUTBOX (fichiers clés)"
mkdir -p "$OB" "$OB/Index_Maison" "$OB/Cahier" "$OB/A_Mon_Attention"
for f in PLAN_DE_VOL.md CONSOLE_GENERALE.md AUTO_PROCESSUS.md MEMOIRE_COLLAB.md \
         PROTOCOLE_SESSION_DEBUT_FIN.md JOURNAL_COCKPIT.md CHOSES_A_FINIR_REVOIR.md \
         CERVEAU_GALACTIQUE.md PROTOCOLE_VALIDATION_TEST_AVANT_REEL.md; do
  [[ -f "$WS/$f" ]] && cp "$WS/$f" "$OB/$f" && echo "  OK $f"
done
[[ -f "$JOURNAL" ]] && cp "$JOURNAL" "$OB/Index_Maison/" && cp "$JOURNAL" "$OB/Cahier/" && echo "  OK $(basename "$JOURNAL")"
[[ -f "$WS/CONSOLE_GENERALE.md" ]] && cp "$WS/CONSOLE_GENERALE.md" "$OB/Index_Maison/"
ATT="$WS/A_Mon_Attention/2026-07-31_cadence_session_finition.md"
[[ -f "$ATT" ]] && cp "$ATT" "$OB/A_Mon_Attention/" && echo "  OK $(basename "$ATT")"
echo

echo "5) Sync Obsidian — à lancer dans TON Terminal (TCC) :"
echo "   bash $OB/_sync_now.sh"
echo

if [[ "$ace_vol" -eq 1 && "$DO_STOP_ACE" -eq 0 ]]; then
  echo "=== SESSION FIN OK — VOL LAISSÉ TOURNER ==="
else
  echo "=== SESSION FIN OK ==="
fi
echo "Rappel: kill-switch / validation = [[PLAN_DE_VOL]] · cosmétique = [[CHOSES_A_FINIR_REVOIR]]"
exit 0
