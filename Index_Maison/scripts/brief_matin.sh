#!/usr/bin/env bash
# brief_matin.sh — le lecteur du matin (GO plomberie 07/08, autogestion E3)
# Lit l'état live (tout TCC-safe dans ~/ace777-test-day1) + dernière analyse
# du chief, écrit le brief du jour dans ~/prise-ia/reports/ (launchd ne peut
# pas écrire dans ~/Documents — leçon 07/08).
set -uo pipefail
TS=$(date -u +%Y-%m-%dT%H:%MZ)
OUT="$HOME/prise-ia/reports/BRIEF_MATIN.md"
mkdir -p "$HOME/prise-ia/reports"
{
  echo "# ☀️ BRIEF MATIN — $TS"
  echo
  echo "## Feu tricolore"
  grep -A 8 'Feu tricolore' "$HOME/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/CONSOLE_GENERALE.md" 2>/dev/null | head -10 || echo "(console indisponible)"
  echo
  echo "## Thermo (dernier)"
  head -14 "$HOME/ace777-test-day1/Index_Maison/THERMO_DERNIER.md" 2>/dev/null || echo "(thermo indisponible)"
  echo
  echo "## Justesse de l'analyste"
  python3 -c "import json;d=json.load(open('$HOME/ace777-test-day1/Index_Maison/scripts/justesse_cockpit.json'));print('n=',d.get('n'),'hits=',d.get('total_hit'),'pct=',d.get('pct'))" 2>/dev/null || echo "(pas encore noté)"
  echo
  echo "## Dernière analyse du chief"
  LATEST=$(ls -t "$HOME/ace777-test-day1/Index_Maison/thermo/analyses/"*.jsonl 2>/dev/null | head -1)
  if [ -n "$LATEST" ]; then
    tail -1 "$LATEST" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('indice','?'),'| avis_ok:',d.get('avis_ok')); print((d.get('analyse') or '')[:500])" 2>/dev/null || echo "(pas encore)"
  else
    echo "(pas encore)"
  fi
  echo
  echo "## Mémoire récente (coffre)"
  grep -E '^\| 2026' "$HOME/Documents/Obsidian_ACE777/MEMOIRE_COLLAB.md" 2>/dev/null | head -3 || echo "(coffre illisible en launchd — lire dans Obsidian)"
} > "$OUT"
echo "BRIEF_MATIN -> $OUT"
