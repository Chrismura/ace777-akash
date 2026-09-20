#!/bin/bash
# Lanceur du Superviseur L2 passif — GO famille 11/09 (choix 1 : ressusciter).
# Rôle : garder superviseur_l2.py en permanence, avec un fichier L2_<date> TOUJOURS
# à la date du jour (le script fige `day` au démarrage → on le relance à minuit UTC).
# Arrêt propre : touch ~/ace777-test-day1/runs/STOP_L2  (le script s'arrête,
# puis le lanceur s'arrête aussi — aucun redémarrage forcé).
# Test possible : L2_TEST_SEC=8 ./lanceur_superviseur_l2.sh  (session courte)

RUNS="$HOME/ace777-test-day1/runs"
STOP="$RUNS/STOP_L2"
SCRIPT="$HOME/ace777-test-day1/Index_Maison/scripts/superviseur_l2.py"

while true; do
    [ -f "$STOP" ] && { echo "[lanceur] STOP_L2 présent — arrêt du lanceur."; exit 0; }

    # Secondes restantes avant le prochain minuit UTC
    now=$(date +%s)
    midnight_utc=$(date -u -v+1d -v0H -v0M -v0S +%s 2>/dev/null || date -u -d "tomorrow 00:00" +%s)
    reste=$(( midnight_utc - now ))
    [ "$reste" -lt 10 ] && reste=10

    if [ -n "$L2_TEST_SEC" ]; then
        reste="$L2_TEST_SEC"
    fi

    echo "[lanceur] $(date -u '+%Y-%m-%dT%H:%M:%SZ') session L2 de ${reste}s (jusqu'à minuit UTC)"
    RUN_SEC="$reste" python3 "$SCRIPT"
    echo "[lanceur] session terminée (code $?) — relance dans 2 s"
    sleep 2
done
