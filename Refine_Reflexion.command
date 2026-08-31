#!/bin/bash
# Refine_Reflexion.command — Mini-/refine ACE777 (à lancer à la fin d'une mission)
# Pour déclencher la volonté: clic sur cette fichier, renseigne ta réflexion, 
# le bloc part dans la daily note Obsidian (Cahier/YYYY-MM-DD) via le pont.
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT/Index_Maison/scripts"

echo "================================================================="
echo " REFINE — reflexion de fin de mission (inspire de PrimeAgent /refine)"
echo "================================================================="
echo "Ce qui a MARCHE (une ligne) :"
read -r MARCHE
echo "Ce qui est a AMELIORER (une ligne) :"
read -r AMEL
echo "Rollback eventuel (R-<id>: ..., ou laisser vide) :"
read -r ROLL

ARGS=(--agent "manuel" --marche "$MARCHE" --ameliore "$AMEL")
if [ -n "$ROLL" ]; then ARGS+=(--rollback "$ROLL"); fi

/usr/bin/python3 refine_maison.py "${ARGS[@]}"
echo "------------------------------------------------------"
echo " Refine journalise dans la daily note. Statut ci-dessus."
echo " (Obsidian doit etre ouvert pour l'ecriture directe.)"
echo "================================================================="