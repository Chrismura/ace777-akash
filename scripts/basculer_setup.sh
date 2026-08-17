#!/usr/bin/env bash
# Bascule de setup ACE777 en UNE commande — plus de mise à jour manuelle.
#
# Usage:
#   ./scripts/basculer_setup.sh A        # setup A : rollback complet (revenge permanent)
#   ./scripts/basculer_setup.sh B        # setup B : TTL revenge 120s
#   ./scripts/basculer_setup.sh C        # setup C : FIX-LAST-LOSS
#   ./scripts/basculer_setup.sh           # état actuel + liste des setups
#
# Ce que ça fait :
#   1. Sauvegarde le champion actuel (BAK horodaté) — réversible à tout moment
#   2. Copie le bon manifest vers LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt
#   3. Écrit le préfixe md5 dans Index_Maison/strategie/CHAMPION_ACTIF
#      (la source de vérité unique lue par superviseur, pulse, checkup, verif,
#      preflight, GO_VORTEX, bridge — AUCUN redémarrage nécessaire)
#
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

CHAMPION="LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt"
CENTRAL="Index_Maison/strategie/CHAMPION_ACTIF"

# --- Description / fichier source / préfixe par setup (bash 3.2 : pas de tableaux associatifs)
info_setup() {
  case "$1" in
    A) echo "A|Rollback complet — revenge armé en permanence (avant fix heartbeat 15/08)|genesis_manifest.txt.BAK_avant_fix_heartbeat_20260815-152847|fe2a7bcc" ;;
    B) echo "B|Fix 15/08 conservé — TTL revenge 20→120s (DUO_EVENT_TTL_SEC=120 au lancement)||95d93d50" ;;
    C) echo "C|FIX-LAST-LOSS — TTL revenge 120s sur last_loss_ts + price stasis (16/08)|LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_setupC_fix_last_loss_20260817|8bce77b1" ;;
    *) echo "" ;;
  esac
}

if [ $# -eq 0 ]; then
  echo "=== SETUP ACTUEL ==="
  echo "champion md5 : $(md5 -q "$CHAMPION" 2>/dev/null | cut -c1-8)"
  echo "central      : $(cat "$CENTRAL" 2>/dev/null || echo 'ABSENT')"
  echo ""
  echo "=== SETUPS DISPONIBLES ==="
  for s in A B C; do
    IFS='|' read -r _ _ _ prefix <<< "$(info_setup "$s")"
    echo "  $s) $(info_setup "$s" | cut -d'|' -f2)  →  préfixe $prefix"
  done
  echo ""
  echo "Usage : ./scripts/basculer_setup.sh [A|B|C]"
  exit 0
fi

S="$(echo "$1" | tr '[:lower:]' '[:upper:]')"
IFS='|' read -r _ desc src prefix <<< "$(info_setup "$S")"
if [ -z "$src" ] || [ ! -f "$src" ]; then
  echo "FAIL: setup $S non disponible (fichier source introuvable : ${src:-vide})"
  exit 1
fi

echo "=== BASCULE VERS SETUP $S ==="
echo "  $desc"

# 1. Backup du champion actuel
BAK="${CHAMPION}.BAK_avant_setup${S}_$(date +%Y%m%d-%H%M%S)"
cp "$CHAMPION" "$BAK" && echo "  backup : $BAK"

# 2. Copie du manifest cible
cp "$src" "$CHAMPION"

# 3. Vérification md5
_MD5="$(md5 -q "$CHAMPION")"
if [[ "$_MD5" != "$prefix"* ]]; then
  echo "  FAIL: md5=$_MD5 attendu $prefix… — rollback du backup"
  cp "$BAK" "$CHAMPION"
  exit 1
fi

# 4. Mise à jour de la source de vérité centrale
echo "$prefix" > "$CENTRAL"
echo "  central : $prefix (source de vérité mise à jour)"

# 5. Rappel pour le setup B (variable d'env au lancement)
if [ "$S" = "B" ]; then
  echo ""
  echo "  ⚠️ Setup B : lancer avec  export DUO_EVENT_TTL_SEC=120  avant GO_VORTEX_V2"
fi

echo "  ✅ Setup $S actif — les vérifications suivront automatiquement (aucun redémarrage)"
