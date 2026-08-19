#!/usr/bin/env bash
# Cortana — résumé horaire indices + avis sentiment (voix optionnelle).
# Lecture seule. Ne lance PAS ACE.
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH"

CMD=(/usr/bin/python3 "$ROOT/Index_Maison/scripts/cortana_thermo.py" horaire)
# Par défaut : parler. Désactiver : CORTANA_HORAIRE_SAY=0
if [ "${CORTANA_HORAIRE_SAY:-1}" = "1" ]; then
  CMD+=(--say)
fi

# (fix 19/08 : tableau jamais vide → évite « SAY_FLAG[@]: unbound variable »
#  sous set -u + bash 3.2 quand le mode silencieux n'ajoute pas --say)
"${CMD[@]}" >>"$ROOT/Index_Maison/thermo/cortana_horaire_run.log" 2>&1
