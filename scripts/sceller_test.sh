#!/usr/bin/env bash
# SCELLER un CSV de test : copie immuable + signature sha256 (mécanisme d'audit).
# Usage:
#   ./scripts/sceller_test.sh <tag> <unit> [dossier_source]
#   ex: ./scripts/sceller_test.sh MASTER_VORTEX_V2_COLLAB_4H ALPHA_X13_BURST13
#   ex: ./scripts/sceller_test.sh MASTER_VORTEX_V2_COLLAB_4H BETA_X5
#
# Produit (dans runs/SCELLE/):
#   <tag>_<unit>_<horodatage>.csv            ← copie scellée, chmod 444 (lecture seule)
#   <tag>_<unit>_<horodatage>.SIGNATURE.txt  ← sha256 + métadonnées (md5 genesis, nb lignes, config)
#
# Vérification ensuite : ./scripts/verifier_test.sh <fichier_signature>

set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tag="${1:?usage: sceller_test.sh <tag> <unit> [source_dir]}"
unit="${2:?usage: sceller_test.sh <tag> <unit> [source_dir]}"
src_dir="${3:-$root/runs}"

src_csv="${src_dir}/${tag}_${unit}.csv"
if [ ! -f "$src_csv" ]; then
  echo "ERREUR: CSV introuvable: $src_csv" >&2
  exit 1
fi

out_dir="$root/runs/SCELLE"
mkdir -p "$out_dir"
stamp="$(date -u +%Y%m%d-%H%M%SZ)"
out_csv="${out_dir}/${tag}_${unit}_${stamp}.csv"
sig_file="${out_csv%.csv}.SIGNATURE.txt"

# 1. Copie scellée en lecture seule
cp "$src_csv" "$out_csv"
chmod 444 "$out_csv"

# 2. Métadonnées
genesis_md5="$(md5 -q "$root/genesis_manifest.txt" 2>/dev/null || echo "inconnu")"
nl="$(wc -l < "$src_csv" | tr -d ' ')"
genesis_line="$(grep -m1 '^CONFIG' "$root/config_active.env" 2>/dev/null || true)"
nb_filled="$(awk -F',' '$4=="FILLED" {n++} END {print n+0}' "$src_csv")"
pnl_total="$(awk -F',' '$4=="FILLED" {s+=$9} END {printf "%.4f", s+0}' "$src_csv")"

# 3. Signature
{
  echo "=== SCELLEMENT DE TEST ACE777 ==="
  echo "tag=${tag} unit=${unit}"
  echo "date_scellement=$(date -u +%FT%TZ)"
  echo "fichier_scelle=$(basename "$out_csv")"
  echo "lignes=${nl}"
  echo "trades_filled=${nb_filled}"
  echo "pnl_total_usdt=${pnl_total}"
  echo "genesis_md5=${genesis_md5}"
  echo "config=${genesis_line}"
  echo "sha256=$(shasum -a 256 "$out_csv" | awk '{print $1}')"
  echo "md5=$(md5 -q "$out_csv")"
  echo "=== FIN SIGNATURE ==="
} > "$sig_file"
chmod 444 "$sig_file"

echo "SCELLE_OK: $out_csv"
echo "SIGNATURE: $sig_file"
echo "sha256: $(grep '^sha256=' "$sig_file" | cut -d= -f2)"
echo "md5:    $(grep '^md5=' "$sig_file" | cut -d= -f2)"
