#!/usr/bin/env bash
# analyste_cadence.sh — le chief parle 2x/jour (GO plomberie 07/08)
# Indices cœurs : radar (climat global), funding (levier), fearGreed (sentiment), geopol.
#
# ══════════════════════════════════════════════════════════════════════════════
# RÉACTIVATION DES INDICES — 19/09/2026 (GO Christophe). RÉVISÉ 19/09 (GO « go 1,2,3 »)
# ══════════════════════════════════════════════════════════════════════════════
# CONSTAT : des indices étaient MORTS (plus aucune analyse) non par panne mais parce
# qu'ils n'étaient PLUS DANS LA ROTATION. Ils restaient FROID/CRITIQUE à vie dans
# derive_memoire (alarme permanente → plus personne ne croyait l'alarme).
#
# R15 « TOUJOURS BRANCHER » : tout ce qu'on AFFICHE doit être BRANCHÉ. Les 15 bulles
# de l'app Indices (cockpit/indices.html) sont désormais couvertes : 13 par la
# rotation ci-dessous, 2 déclarées « affichage seul » (justesse, ace) dans
# strategie/branchements_declares.json. Le vérificateur R15 mesure cet écart.
#
# CORRECTIF : on RAFAÎCHIT sans toucher à la cadence des 4 cœurs (analysés à CHAQUE
# passage, 2x/jour). 3 indices « réactivés » par passage, EN ROTATION (stateless :
# 1 tick = 12 h) → cycle complet de 18 indices en 6 passages = 3 jours, très
# au-dessus du seuil de 14 j de derive_memoire et sous le seuil FROID de 7 j.
#
# COÛT : +3 appels hub par passage → 0 €, charge négligeable. AUCUNE CAPACITÉ
# RETIRÉE : on AJOUTE seulement. Réversible : remettre CORE seul dans la boucle.
set -uo pipefail
LOG=/tmp/analyste_cadence.log
echo "=== $(date -u +%FT%TZ) ===" >> "$LOG"
cd ~/ace777-test-day1/Index_Maison/scripts || exit 1

CORE="radar funding fearGreed geopol"
# Indices réactivés le 19/09 (ordre = ordre de rotation, pas de priorité)
REVIVES="btc oi onchain indice_onchain sdi verre bassine altSeason liq24Usd gexPutCall etfEthM etfXrpM chg24 rbf pipeline_health longShort etfBtcM score"
N=$(echo $REVIVES | wc -w | tr -d ' ')
K=3                                        # indices réactivés par passage
TICK=$(( $(date -u +%s) / 43200 ))         # 1 tick = 12 h = 1 passage (08h30 / 20h30)
BASE=$(( (TICK * K) % N ))
REVIVE_LIST=""
for off in $(seq 0 $((K - 1))); do
  REVIVE_LIST="$REVIVE_LIST $(echo $REVIVES | cut -d' ' -f $(( (BASE + off) % N + 1 )))"
done
echo "-- rotation réactivés ($K/$N) :$REVIVE_LIST" >> "$LOG"

for indice in $CORE $REVIVE_LIST; do
  echo "-- $indice" >> "$LOG"
  python3 cortana_analyse.py "$indice" >> "$LOG" 2>&1 || echo "[$indice] ECHEC" >> "$LOG"
  sleep 3   # ménage le hub (évite les 429 en rafale)
done
