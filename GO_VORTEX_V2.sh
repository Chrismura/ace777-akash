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
# 16/08 : re-scellé 3d760592 = 95d93d50 + FIX-LAST-LOSS (TTL revenge sur last_loss_ts, DUO_REVENGE_TTL_SEC=120)
EXPECT_MD5_PREFIX="3d760592"

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
