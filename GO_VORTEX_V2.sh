#!/usr/bin/env bash
# =============================================================================
# ACE777 — GO VORTEX V2 (test A/B) — réversible
#
# Charge config_profiles/vortex_v2_collab.env puis lance le launcher officiel.
# Ne touche PAS genesis / pas de rewrite usine NUAGE.
# Retour usine après stop : ./GO_USINE_NUAGE.sh
#
# Usage:
#   ./GO_VORTEX_V2.sh              # 4h
#   ./GO_VORTEX_V2.sh 04:00:00
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

DURATION="${1:-04:00:00}"
# Source de vérité : Index_Maison/strategie/CHAMPION_ACTIF (mis à jour par scripts/basculer_setup.sh)
EXPECT_MD5_PREFIX="$(cat "$ROOT/Index_Maison/strategie/CHAMPION_ACTIF" 2>/dev/null || echo UNKNOWN)"

fail() { echo "FAIL: $*" >&2; exit 1; }

echo "=== GO_VORTEX_V2 — profil radar pilot (A/B vs usine) ==="
echo "ROOT=$ROOT DURATION=$DURATION"

case "$DURATION" in
  *720*|*168:*) fail "durée type mois/720h refusée — blocs 4h seulement." ;;
esac

[ -e "$ROOT/genesis_manifest.txt" ] || fail "genesis_manifest.txt manquant"
_md5="$(md5 -q "$ROOT/genesis_manifest.txt")"
echo "genesis md5=$_md5"
[[ "$_md5" == "$EXPECT_MD5_PREFIX"* ]] || fail "champion ≠ $EXPECT_MD5_PREFIX…"

[ -f "$ROOT/config_profiles/vortex_v2_collab.env" ] || fail "profil vortex manquant"
[ -x "$ROOT/launch_vortex_v2_collab_4h_binance.sh" ] || fail "launch_vortex_v2_collab_4h_binance.sh manquant"

# Libérer les STOP posés par hygiène (sinon fortress ne part pas)
rm -f STOP STOP_ALPHA STOP_BETA

# ============================================================
# FAIL-FAST SUPERVISION (exigence famille, consultation canonique 20/08) —
# « Ne jamais lancer le moteur si les garde-fous de surveillance ne sont pas
# réellement actifs » (DEEPSEEK + INFERX + JUGE). C'est exactement le trou du
# 19/08 : le run a tourné alors que la vigie était morte et les plists de
# relance jamais chargées. Ici, on REFUSE le départ si un filet manque.
# C1 : genesis intact — vérification dans le wrapper uniquement.
# ============================================================
_PLISTS_SUPERVISION="com.ace777.sante-index com.ace777.veille-degradation com.ace777.dms-veille com.ace777.superviseur-core com.ace777.vigie-live"
# NB pipefail : `launchctl list | grep -q` échoue FAUX (grep -q se ferme dès
# qu'il trouve → launchctl reçoit SIGPIPE 141 → pipefail → pipeline ≠ 0).
# On capture la sortie d'abord, puis on compare sans pipe (bug 20/08 15:xx,
# découvert au lancement du run 72h — le fail-fast rejetait des plists chargées).
_launchctl_out="$(launchctl list 2>/dev/null || true)"
_absents=""
for _p in $_PLISTS_SUPERVISION; do
  case "$_launchctl_out" in
    *"$_p"*) : ;;
    *) _absents="$_absents $_p" ;;
  esac
done
if [ -n "$_absents" ]; then
  fail "FAIL-FAST SUPERVISION: plist(s) de garde-fou NON CHARGÉE(S):$_absents — refuse de lancer le moteur sans filet (leçon 19/08). Lance-les d'abord: launchctl load ~/Library/LaunchAgents/..."
fi
echo "[FAIL-FAST] supervision OK: 5/5 plists de garde-fou chargées."

# ============================================================
# GARDE-FOU FILET STOP_MARKET (leçon 5, 20/08) — C1 : molettes uniquement.
# Le filet est DÉSACTIVÉ par défaut (FALSE dans le genesis). S'il est activé
# (ACE_STOP_MARKET_ENABLED=TRUE), on IMPOSE une distance minimale sûre :
#   - 8 bps → Binance rejette « -2021 Order would immediately trigger » sur un
#     marché volatil (trigger déjà atteint à la pose) → positions SANS filet.
#   - On refuse ici le lancement en fausse sécurité : filet actif mais trop serré.
# Réactivable proprement : ACE_STOP_MARKET_ENABLED=TRUE ACE_STOP_MARKET_BPS=20
#   (20 bps = 0,20 % — filet anti-crash, PAS un scalpel).
# ============================================================
if [ "${ACE_STOP_MARKET_ENABLED:-FALSE}" = "TRUE" ]; then
  _sm_bps="${ACE_STOP_MARKET_BPS:-8}"
  _sm_min="${ACE_STOP_MARKET_BPS_MIN:-20}"
  if [ "$_sm_bps" -lt "$_sm_min" ]; then
    fail "FILET STOP_MARKET: ACE_STOP_MARKET_BPS=$_sm_bps < $_sm_min — refusé (sinon -2021 Binance → fausse sécurité). Active avec ACE_STOP_MARKET_BPS>=$_sm_min ou retire ACE_STOP_MARKET_ENABLED=TRUE."
  fi
  echo "[FILET] STOP_MARKET activé: ${ACE_STOP_MARKET_BPS} bps (min ${_sm_min}) — garde-fou leçon 5 OK."
fi

# Météo hors moteur
export ENGLE_ADAPT="${ENGLE_ADAPT:-0}"
_tag="MASTER_VORTEX_V2_COLLAB_4H"
_irm_csv="$ROOT/runs/${_tag}_BETA_X5.csv"
echo "=== IRM (lecture seule) ==="
ruby "$ROOT/scripts/irm_tension.rb" boot "$_irm_csv" 50 2>/dev/null || echo "IRM: n/a (ok au boot)"
echo "=== ENGLE_ADAPT=${ENGLE_ADAPT} ==="
ruby "$ROOT/scripts/engle_adapt.rb" boot "$_irm_csv" 50 2>/dev/null || true

echo "=== BOOT VORTEX — attendu: VORTEX_V2_RADAR_PILOT + tag ${_tag} ==="
echo "Retour usine après ce test: stop puis ./GO_USINE_NUAGE.sh"
exec ./launch_vortex_v2_collab_4h_binance.sh --duration "$DURATION"
