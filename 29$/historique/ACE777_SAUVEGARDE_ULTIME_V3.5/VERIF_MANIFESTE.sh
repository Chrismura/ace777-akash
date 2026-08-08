#!/usr/bin/env bash
# ACE777 — Audit intégrité manifeste V3.5 (reproductible)
set -uo pipefail

ROOT="${ACE777_ROOT:-/Users/christophe/ace777-test-day1}"
VAULT="$ROOT/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5"
MONO="$ROOT/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5.md"
FAIL=0

ok()  { echo "  OK: $1"; }
bad() { echo "  FAIL: $1"; FAIL=1; }

echo "=== AUDIT ACE777_SAUVEGARDE_ULTIME_V3.5 ==="
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

echo "1. Scripts coffre = sources vivantes (md5)"
for f in preflight_total_365j.sh verif_sterilite.sh; do
  if [ -f "$VAULT/scripts/$f" ] && [ -f "$ROOT/scripts/$f" ]; then
    c="$(md5 -q "$VAULT/scripts/$f")"
    s="$(md5 -q "$ROOT/scripts/$f")"
    [ "$c" = "$s" ] && ok "$f identique ($c)" || bad "$f DIFFÈRE coffre=$c source=$s"
  else
    bad "$f manquant"
  fi
done

echo ""
echo "2. Genesis champion md5 = 37fca367"
g="$(md5 -q "$ROOT/genesis_manifest.txt" 2>/dev/null || echo ERR)"
[[ "$g" == 37fca367* ]] && ok "genesis actif $g" || bad "genesis actif $g (attendu 37fca367...)"

echo ""
echo "3. Enveloppe annexe monolithe = snapshot (663 lignes)"
python3 - <<PY || bad "python audit annex"
import re, sys
mono=open("$MONO").read()
snap=open("$VAULT/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh").read()
# Annexe = bloc bash sous "## ANNEXE — Enveloppe NUAGE"
m=re.search(r'## ANNEXE — Enveloppe NUAGE.*?\`\`\`bash\n(.*?)\`\`\`', mono, re.S)
annex=m.group(1) if m else ""
if annex==snap and len(snap.splitlines())==663:
    print("  OK: annexe monolithe byte-identique snapshot (663 L)")
else:
    print("  FAIL: annexe diffère snapshot")
    sys.exit(1)
PY

echo ""
echo "4. duo_hunter_signal PARTIE_02 = genesis L996-1103"
diff -q <(sed -n '996,1103p' "$ROOT/genesis_manifest.txt") \
        <(sed -n '/^duo_hunter_signal() {/,/^}$/p' "$VAULT/parties/PARTIE_02_SEMANTIQUE.md") \
  && ok "duo_hunter_signal 108 lignes identiques" \
  || bad "duo_hunter_signal DIFFÈRE"

echo ""
echo "5. Faits chiffrés vs CSV disque"
a="$(grep '2026-07-14T12:47:29Z,219' "$ROOT/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv" 2>/dev/null | cut -d, -f9)"
b="$(grep '2026-07-10T20:29:56Z,19' "$ROOT/runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv" 2>/dev/null | cut -d, -f9)"
[ "$a" = "32.06952000" ] && ok "trade 14/07 ALPHA pnl=$a" || bad "trade 14/07 pnl=$a (attendu 32.06952000)"
[ "$b" = "22.86432000" ] && ok "trade 204206 best pnl=$b" || bad "trade 204206 pnl=$b (attendu 22.86432000)"

echo ""
echo "6. Avertissements (valeurs contextuelles, pas code)"
echo "  INFO: 39872 swapouts = mesure session 14/07 — re-vérifier: vm_stat | grep swap"
echo "  INFO: 1785.9 USDT / 444ms ping = exemples preflight — varient à chaque run"
echo "  INFO: date jalon = 2026-07-10 (204206), pas juin"

echo ""
echo "7. Sceaux binaires de certification"
PF_LINES=$(wc -l < "$ROOT/scripts/preflight_total_365j.sh" | tr -d ' ')
RUN_MD5=$(sed -n '437,476p' "$VAULT/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh" | md5 -q)
GEN_L1041=$(sed -n '1041p' "$ROOT/genesis_manifest.txt")
[ "$PF_LINES" = "173" ] && ok "SCEAU_1 COMPTEUR_LIGNES preflight = $PF_LINES" || bad "SCEAU_1 attendu 173, obtenu $PF_LINES"
[ "$RUN_MD5" = "7436d4584082c02ac63397dfe0e3b679" ] && ok "SCEAU_2 MD5 run_unit() = $RUN_MD5" || bad "SCEAU_2 MD5 run_unit = $RUN_MD5"
echo "  SCEAU_3 VERROU_GENESIS L1041: $GEN_L1041"
grep -qF 'suffer = (status == "OPEN") && (bps <= suffer_bps || pnl <= suffer_usdt)' "$MONO" \
  && ok "SCEAU_3 présent dans monolithe" || bad "SCEAU_3 absent du monolithe"

echo ""
if [ "$FAIL" -eq 0 ]; then
  echo "=== VERDICT: AUDIT OK — code et faits CSV cohérents ==="
  exit 0
else
  echo "=== VERDICT: AUDIT NOK — corriger les FAIL ci-dessus ==="
  exit 1
fi
