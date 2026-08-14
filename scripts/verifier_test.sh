#!/usr/bin/env bash
# VERIFIER l'intégrité d'un CSV scellé (produit par sceller_test.sh).
# Usage:
#   ./scripts/verifier_test.sh <fichier_signature.txt>
#   ex: ./scripts/verifier_test.sh runs/SCELLE/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13_20260814-184100Z.SIGNATURE.txt
#
# Sortie: INTACT (les hashes correspondent) ou MODIFIE (falsification détectée).

set -uo pipefail

sig="${1:?usage: verifier_test.sh <fichier_signature.txt>}"
if [ ! -f "$sig" ]; then
  echo "ERREUR: signature introuvable: $sig" >&2
  exit 1
fi

sig_dir="$(cd "$(dirname "$sig")" && pwd)"
csv_name="$(grep -m1 '^fichier_scelle=' "$sig" | cut -d= -f2)"
csv="${sig_dir}/${csv_name}"

if [ ! -f "$csv" ]; then
  echo "MODIFIE: CSV scellé introuvable: $csv"
  echo "  (le fichier a été supprimé ou déplacé)"
  exit 1
fi

sig_sha="$(grep -m1 '^sha256=' "$sig" | cut -d= -f2)"
sig_md5="$(grep -m1 '^md5=' "$sig" | cut -d= -f2)"
cur_sha="$(shasum -a 256 "$csv" | awk '{print $1}')"
cur_md5="$(md5 -q "$csv")"

perm="$(stat -f '%Sp' "$csv")"
perm_ok="no"
case "$perm" in
  -r--r--r--*|-r--------*) perm_ok="yes" ;;
esac

echo "=== VERIFICATION INTEGRITE ==="
echo "csv:        $csv"
echo "permissions: $perm (lecture seule attendue: ${perm_ok})"
echo ""
echo "sha256 signature: $sig_sha"
echo "sha256 actuel:    $cur_sha"
echo "md5   signature: $sig_md5"
echo "md5   actuel:    $cur_md5"
echo ""

if [ "$sig_sha" = "$cur_sha" ] && [ "$sig_md5" = "$cur_md5" ]; then
  echo "RESULTAT: ✅ INTACT — le CSV n'a pas été modifié depuis le scellement."
  exit 0
else
  echo "RESULTAT: ❌ MODIFIE — les hashes ne correspondent PAS."
  echo "  Le fichier a été altéré depuis le scellement (falsification détectée)."
  exit 1
fi
