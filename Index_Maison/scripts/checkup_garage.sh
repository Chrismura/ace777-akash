#!/usr/bin/env bash
# Checkup garage — fantômes PID / stérilité / RAM (lecture + rapport)
# Ne lance PAS ACE/Hulk.
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
TS="$(date -u +%Y%m%dT%H%MZ)"
OUT_DIR="$ROOT/Index_Maison"
REPORT="$OUT_DIR/CHECKUP_${TS}.md"
LATEST="$OUT_DIR/CHECKUP_DERNIER.md"
FAIL=0
FANTOMES_OK=1

{
  echo "# Checkup garage — $TS"
  echo
  echo "**But :** détecter process fantômes / PID orphelins / état Mac avant tout GO."
  echo
  echo "Références :"
  echo "- \`plaintes/PROTOCOLE_STERILITE_BINAIRE_20260714.md\` (protocole officiel)"
  echo "- \`scripts/verif_sterilite.sh\`"
  echo "- \`ERREURS_AI/RAPPORT_IA_FANTOME_3_POINTS.md\` (phénomènes IA fantôme)"
  echo "- \`hulk-mexc/docs/PROTOCOLE_GHOST.md\` (watchdog Hulk « Ghost » ≠ parasite ACE)"
  echo
  echo "## 1 — Stérilité ACE"
} > "$REPORT"

if ./scripts/verif_sterilite.sh >> "$REPORT" 2>&1; then
  echo "- Verdict : **STERILE=OK**" >> "$REPORT"
else
  echo "- Verdict : **STERILE=NOK**" >> "$REPORT"
  FAIL=1
  FANTOMES_OK=0
fi

{
  echo
  echo "## 2 — Chasse aux fantômes (pgrep élargi)"
  echo
  echo '```'
} >> "$REPORT"

PATTERNS=(
  'GO_USINE_NUAGE'
  'ace777_launch'
  'launch_vide_froid'
  'launch_vortex'
  'watchdog_ace'
  'paper_diprip'
  'digest_watch'
  'watchdog_hulk'
  'ollama serve'
  'nuit_ghost'
  'supervisor_v9'
)

FOUND_ANY=0
for pat in "${PATTERNS[@]}"; do
  hits="$(pgrep -lf "$pat" 2>/dev/null || true)"
  if [[ -n "$hits" ]]; then
    FOUND_ANY=1
    echo "### MATCH: $pat" >> "$REPORT"
    echo "$hits" >> "$REPORT"
    echo >> "$REPORT"
    FAIL=1
    FANTOMES_OK=0
  fi
done
# caffeinate lié ACE
hits="$(pgrep -lf 'caffeinate' 2>/dev/null | grep -iE 'GO_USINE|ace777|NUAGE' || true)"
if [[ -n "$hits" ]]; then
  FOUND_ANY=1
  echo "### MATCH: caffeinate ACE" >> "$REPORT"
  echo "$hits" >> "$REPORT"
  FAIL=1
  FANTOMES_OK=0
fi

if [[ "$FOUND_ANY" -eq 0 ]]; then
  echo "(aucun match — OK)" >> "$REPORT"
fi
echo '```' >> "$REPORT"

{
  echo
  echo "## 3 — Fichiers PID / cœur RAM"
  echo
} >> "$REPORT"

check_absent() {
  local f="$1"
  if [[ -e "$f" ]]; then
    echo "- **PRÉSENT** \`$f\`" >> "$REPORT"
    if [[ -f "$f" ]]; then
      echo "  contenu: \`$(tr '\n' ' ' < "$f" | head -c 80)\`" >> "$REPORT"
    fi
    FAIL=1
    FANTOMES_OK=0
  else
    echo "- absent OK : \`$f\`" >> "$REPORT"
  fi
}

check_absent "runs/master.pid"
check_absent "runs/nuit_ghost_loop.pid"
check_absent "/tmp/alpha_heartbeat.txt"

if [[ -d /tmp/ace777_ram_exchange ]]; then
  n="$(find /tmp/ace777_ram_exchange -type f 2>/dev/null | wc -l | tr -d ' ')"
  echo "- \`/tmp/ace777_ram_exchange\` existe ($n fichiers)" >> "$REPORT"
else
  echo "- \`/tmp/ace777_ram_exchange\` absent (sera recréé au prochain run)" >> "$REPORT"
fi

{
  echo
  echo "## 4 — Fichiers STOP (au repos = OK s’ils existent)"
} >> "$REPORT"
for f in STOP STOP_ALPHA STOP_BETA; do
  if [[ -f "$f" ]]; then
    echo "- OK \`$f\`" >> "$REPORT"
  else
    echo "- manquant \`$f\` (à \`touch\` avant pre-run)" >> "$REPORT"
  fi
done

{
  echo
  echo "## 5 — Champion"
} >> "$REPORT"
_actual="$(md5 -q genesis_manifest.txt 2>/dev/null || true)"
_champ_ref="$(cat "$ROOT/Index_Maison/strategie/CHAMPION_ACTIF" 2>/dev/null || echo UNKNOWN)"
if [[ "$_actual" == "$_champ_ref"* ]]; then
  echo "- OK genesis md5=\`$_actual\` (préfixe $_champ_ref — source de vérité CHAMPION_ACTIF)" >> "$REPORT"
else
  echo "- **FAIL** genesis md5=\`$_actual\`" >> "$REPORT"
  FAIL=1
fi

{
  echo
  echo "## 6 — RAM Mac"
} >> "$REPORT"
eval "$(python3 - <<'PY'
import subprocess
try:
  ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
  ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
  if ":" not in line: continue
  k, v = line.split(":", 1)
  try: d[k.strip()] = int(v.strip().rstrip("."))
  except Exception: pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"FREE_MB={free:.0f}")
if free >= 400:
  print("RAM_LABEL=OK")
  print("RAM_CODE=0")
elif free >= 200:
  print("RAM_LABEL=TIGHT")
  print("RAM_CODE=1")
else:
  print("RAM_LABEL=CRITIQUE")
  print("RAM_CODE=2")
PY
)"
echo "- approx libre : **${FREE_MB} Mo**" >> "$REPORT"
echo "- RAM=${RAM_LABEL}" >> "$REPORT"
if [[ "${RAM_CODE:-0}" -ge 2 ]]; then
  echo "- → pas de GO trading tant que RAM critique" >> "$REPORT"
  FAIL=1
elif [[ "${RAM_CODE:-0}" -eq 1 ]]; then
  echo "- → déconseillé pour ACE (mieux ≥400 Mo)" >> "$REPORT"
fi

{
  echo
  echo "## 7 — Top process RAM (info)"
  echo
  echo '```'
  ps -axo rss,pid,comm 2>/dev/null | sort -nr | head -10 | awk '{printf "%6.0f Mo  pid=%s  %s\n", $1/1024, $2, $3}'
  echo '```'
  echo
  echo "## 8 — Cockpit indicateurs (zone test)"
  echo
  echo '```'
} >> "$REPORT"
bash "$OUT_DIR/scripts/cockpit_hygiene_check.sh" >> "$REPORT" 2>&1 || true
{
  echo '```'
  echo
  echo "## Verdict global"
} >> "$REPORT"

if [[ "$FAIL" -eq 0 && "${RAM_CODE:-0}" -eq 0 ]]; then
  echo "**CHECKUP=OK** — garage propre, pas de fantôme, RAM OK (≥400 Mo)." >> "$REPORT"
  VERDICT="CHECKUP=OK"
elif [[ "$FANTOMES_OK" -eq 1 && "${RAM_CODE:-0}" -eq 1 ]]; then
  echo "**CHECKUP=OK_FANTÔMES / RAM=TIGHT** — propre côté process, mais RAM faible (déconseillé ACE)." >> "$REPORT"
  VERDICT="CHECKUP=OK_FANTÔMES / RAM=TIGHT"
  FAIL=0
elif [[ "$FANTOMES_OK" -eq 1 ]]; then
  echo "**CHECKUP=NOK** — pas de fantôme process, mais **RAM trop basse**." >> "$REPORT"
  VERDICT="CHECKUP=NOK (RAM)"
else
  echo "**CHECKUP=NOK** — fantôme / PID / stérilité à traiter avant GO." >> "$REPORT"
  VERDICT="CHECKUP=NOK"
fi

cp "$REPORT" "$LATEST"
OB="$OUT_DIR/OUTBOX_OBSIDIAN"
mkdir -p "$OB/Index_Maison"
cp "$LATEST" "$OB/CHECKUP_DERNIER.md"
cp "$LATEST" "$OB/Index_Maison/CHECKUP_DERNIER.md"

echo "$VERDICT"
echo "rapport: $LATEST"
exit "$FAIL"
