#!/usr/bin/env bash
# boot.sh — LE BOOT UNIQUE ACE777 (PLAN_REPARE_VALIDE.md A1, 09/08/2026)
# Additif, lecture seule + tests : ne touche AUCUN service existant, JAMAIS le moteur.
# Verdict cible < 10 s : git, hub, 8 providers (REPONSE REELLE, non bloquant), etat consolide.
# Ecrit BOOT_STATUS.md : TOUT OK ou ERREUR: [ligne exacte].
set -uo pipefail
ROOT="$HOME/ace777-test-day1"
OUT="$ROOT/Index_Maison/BOOT_STATUS.md"
HUB="http://127.0.0.1:11435"
TS=$(date -u +%Y-%m-%dT%H:%MZ)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

STATUS="TOUT OK"
ERRS=""

# 1) Git
gitn=$(git -C "$ROOT" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
gits="repo systeme : $gitn fichiers modifies (WIP normal si >0)"

# 2) Hub health
hcode=$(curl -s --max-time 3 -o /dev/null -w '%{http_code}' "$HUB/health" 2>/dev/null)
if [ "$hcode" = "200" ]; then
  hub="hub /health : OK"
else
  hub="hub /health : HTTP $hcode"
  STATUS="ERREUR"
  ERRS="$ERRS
  - hub /health HTTP $hcode"
fi

# 3) Providers — tests PARALLELES (reponse reelle, 3s chacun, non bloquant)
declare -a PT=("mission:nvidia" "cortana.brief:gemini" "chat.local:qwen-local" "signets.juge:juge" "ultra.analyse:ultra" "inferx.analyse:inferx" "code.ia:inferx-coder" "signets.lot2:oss20")
i=0
for pair in "${PT[@]}"; do
  task="${pair%%:*}"; label="${pair##*:}"
  ( curl -s --max-time 3 -X POST "$HUB/v1/chat/completions" -H 'Content-Type: application/json' \
      -d "{\"task\":\"$task\",\"messages\":[{\"role\":\"user\",\"content\":\"dis ok en 1 mot\"}],\"max_tokens\":5}" \
      -o "$TMP/p$i.json" 2>/dev/null ) &
  eval "pid$i=$!"
  i=$((i+1))
done
i=0
pstatus=""
for pair in "${PT[@]}"; do
  label="${pair##*:}"
  eval "wait \$pid$i" 2>/dev/null
  resp=$(python3 -c "import json,sys
try:
    d=json.load(open(sys.argv[1])); print((d.get('choices') or [{}])[0].get('message',{}).get('content',''))
except Exception:
    print('')" "$TMP/p$i.json" 2>/dev/null)
  if [ -n "$resp" ]; then pstatus="$pstatus
  [OK] $label"; else pstatus="$pstatus
  [WARN] $label (non repondu - bypass)"; fi
  i=$((i+1))
done

# 4) Etat consolide
if [ -f "$ROOT/Index_Maison/ETAT_CONSOLIDE.md" ]; then
  ec="ETAT_CONSOLIDE.md : present"
else
  ec="ETAT_CONSOLIDE.md : ABSENT (A2 pas encore applique)"
fi

{
  echo "# BOOT STATUS — $TS"
  echo
  echo "## Git"
  echo "  $gits"
  echo
  echo "## Hub"
  echo "  $hub"
  echo
  echo "## Providers (reponse reelle, parallele, non bloquant)"
  printf '%s\n' "$pstatus"
  echo
  echo "## Etat consolide"
  echo "  $ec"
  echo
  echo "## Verdict"
  if [ "$STATUS" = "TOUT OK" ]; then
    echo "  TOUT OK"
  else
    echo "  ERREUR:${ERRS}"
  fi
  echo
  echo "_genere $TS · boot.sh (additif, ne touche ni services ni moteur)_"
} > "$OUT"

echo "BOOT_STATUS -> $OUT"
[ "$STATUS" = "TOUT OK" ]
