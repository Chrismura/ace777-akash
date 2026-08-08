#!/usr/bin/env bash
# Pulse « sous l'œil » — machine OK toute seule ? (lecture seule, jamais de GO)
# Écrit Index_Maison/SOUS_L_OEIL.md (+ OUTBOX miroir).
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
OUT="$ROOT/Index_Maison"
TS_UTC="$(date -u +%Y-%m-%dT%H:%MZ)"
TS_LOC="$(date +%Y-%m-%dT%H:%M)"
REPORT="$OUT/SOUS_L_OEIL.md"
LOG_DIR="$OUT/scripts/logs"
mkdir -p "$LOG_DIR" "$OUT/OUTBOX_OBSIDIAN/Index_Maison"

alive() { pgrep -lf "$1" >/dev/null 2>&1; }
count_p() { pgrep -lf "$1" 2>/dev/null | wc -l | tr -d ' '; }

ACE_ON=0; HULK_ON=0; OLLAMA_ON=0
alive 'GO_USINE_NUAGE|ace777_launch_v85|launch_vide_froid' && ACE_ON=1
# fallback: fortress pendant vol
[[ "$ACE_ON" -eq 0 ]] && alive 'launch_test_master_base_v8_6_fortress' && ACE_ON=1
alive 'paper_diprip' && HULK_ON=1
alive 'ollama serve' && OLLAMA_ON=1

MODE="FROID"
[[ "$ACE_ON" -eq 1 || "$HULK_ON" -eq 1 ]] && MODE="VOL"

# RAM
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
if free >= 400: print("RAM_LABEL=OK")
elif free >= 200: print("RAM_LABEL=TIGHT")
else: print("RAM_LABEL=CRITIQUE")
PY
)"

# Champion
GEN_MD5="$(md5 -q "$ROOT/genesis_manifest.txt" 2>/dev/null || echo MISSING)"
if [[ "$GEN_MD5" == 37fca367* ]]; then CHAMP="OK"; else CHAMP="FAIL"; fi

# Heartbeat / LIVE age (si vol)
HB_AGE="—"
LIVE_AGE="—"
LIVE_TAG="—"
if [[ -f /tmp/alpha_heartbeat.txt ]]; then
  HB_AGE="$(python3 - <<'PY'
import os, time
p="/tmp/alpha_heartbeat.txt"
age=int(time.time()-os.path.getmtime(p))
print(f"{age}s")
PY
)"
fi
LIVE="$(ls -t "$ROOT"/runs/*_LIVE_COLOR.log 2>/dev/null | head -1 || true)"
if [[ -n "${LIVE:-}" && -f "$LIVE" ]]; then
  LIVE_TAG="$(basename "$LIVE" _LIVE_COLOR.log)"
  LIVE_AGE="$(python3 - <<PY
import os, time
p="$LIVE"
age=int(time.time()-os.path.getmtime(p))
print(f"{age}s")
PY
)"
fi

# Hulk state frais
HULK_STATE="—"
HULK_POS="—"
STS="$(ls -t "$ROOT"/hulk-mexc/runs/PAPER_V1_*_state.json 2>/dev/null | head -1 || true)"
if [[ -n "${STS:-}" && -f "$STS" ]]; then
  HULK_STATE="$(basename "$STS")"
  HULK_POS="$(python3 - <<PY
import json
from pathlib import Path
st=json.loads(Path("$STS").read_text())
pos=st.get("positions") or {}
print(f"{len(pos)} pos · pnl={st.get('pnl_total')}")
PY
)"
fi

# Checklist + verdict
FAIL=0
WARN=0
lines=()
mark() { # ok|warn|fail | label | detail
  local s="$1" lab="$2" det="$3"
  case "$s" in
    ok)   lines+=("| ✅ | $lab | $det |") ;;
    warn) lines+=("| ⚠️ | $lab | $det |"); WARN=$((WARN+1)) ;;
    fail) lines+=("| ❌ | $lab | $det |"); FAIL=$((FAIL+1)) ;;
  esac
}

mark ok "Mode" "$MODE (auto)"
mark ok "Horodatage" "$TS_LOC local · $TS_UTC UTC"
[[ "$CHAMP" == OK ]] && mark ok "Champion" "md5 \`${GEN_MD5:0:8}…\`" || mark fail "Champion" "md5=\`$GEN_MD5\`"

if [[ "$MODE" == "VOL" ]]; then
  [[ "$ACE_ON" -eq 1 ]] && mark ok "ACE process" "ON" || mark warn "ACE process" "attendu si GO ACE — OFF"
  [[ "$HULK_ON" -eq 1 ]] && mark ok "Hulk paper" "ON" || mark warn "Hulk paper" "OFF"
  if [[ "$ACE_ON" -eq 1 ]]; then
    [[ "$OLLAMA_ON" -eq 1 ]] && mark ok "Ollama" "ON (gate)" || mark fail "Ollama" "DOWN — gate fail-closed"
    # heartbeat >120s = warn
    if [[ "$HB_AGE" == "—" ]]; then
      mark warn "Heartbeat ALPHA" "fichier absent"
    else
      age_n="${HB_AGE%s}"
      if [[ "$age_n" -le 90 ]]; then mark ok "Heartbeat ALPHA" "$HB_AGE"
      elif [[ "$age_n" -le 180 ]]; then mark warn "Heartbeat ALPHA" "$HB_AGE (stale?)"
      else mark fail "Heartbeat ALPHA" "$HB_AGE"
      fi
    fi
    if [[ "$LIVE_AGE" == "—" ]]; then
      mark warn "LIVE_COLOR" "aucun log"
    else
      age_n="${LIVE_AGE%s}"
      if [[ "$age_n" -le 120 ]]; then mark ok "LIVE_COLOR" "$LIVE_TAG · frais $LIVE_AGE"
      elif [[ "$age_n" -le 300 ]]; then mark warn "LIVE_COLOR" "$LIVE_TAG · $LIVE_AGE"
      else mark fail "LIVE_COLOR" "$LIVE_TAG · $LIVE_AGE (muet?)"
      fi
    fi
  fi
  if [[ "$HULK_ON" -eq 1 ]]; then
    mark ok "Hulk state" "$HULK_STATE · $HULK_POS"
  fi
else
  # FROID : process trading = fantôme
  [[ "$ACE_ON" -eq 0 ]] && mark ok "ACE" "OFF (attendu froid)" || mark fail "ACE" "ON hors GO — fantôme?"
  [[ "$HULK_ON" -eq 0 ]] && mark ok "Hulk" "OFF (attendu froid)" || mark warn "Hulk" "ON — session paper?"
  [[ "$OLLAMA_ON" -eq 0 ]] && mark ok "Ollama" "OFF (économie RAM)" || mark warn "Ollama" "ON — OK si veille"
fi

case "$RAM_LABEL" in
  OK) mark ok "RAM" "~${FREE_MB} Mo libre" ;;
  TIGHT) mark warn "RAM" "~${FREE_MB} Mo (tight)" ;;
  *) mark fail "RAM" "~${FREE_MB} Mo CRITIQUE" ;;
esac

if [[ "$FAIL" -gt 0 ]]; then
  VERDICT="PULSE=NOK"
  VERDICT_FR="⚠️ Machine : **anomalie** — regarde les ❌"
elif [[ "$WARN" -gt 0 ]]; then
  VERDICT="PULSE=WARN"
  VERDICT_FR="🟡 Machine : **OK avec alertes**"
else
  VERDICT="PULSE=OK"
  VERDICT_FR="🟢 Machine : **tourne seule OK**"
fi

{
  echo "# Sous l'œil — pulse machine"
  echo
  echo "> Mis à jour auto · **ne lance rien** · lit seulement."
  echo
  echo "**$VERDICT_FR** · \`$VERDICT\` · mode **$MODE**"
  echo
  echo "| | Check | Détail |"
  echo "|---|--------|--------|"
  printf '%s\n' "${lines[@]}"
  echo
  echo "## Que faire"
  echo
  if [[ "$MODE" == "VOL" ]]; then
    echo "- Vol en cours : **ne pas** lancer un 2ᵉ GO, **ne pas** tuer sans raison."
    echo "- Si ❌ Ollama / LIVE muet / heartbeat mort → ouvrir le terminal ACE, coller le log."
    echo "- Commande manuelle : \`bash Index_Maison/scripts/pulse_sous_loeil.sh\`"
  else
    echo "- Mode froid : avant un GO → \`bash Index_Maison/scripts/checkup_garage.sh\`"
    echo "- Hygiène RAM : \`bash scripts/hygiene_mac_ram.sh\`"
  fi
  echo
  echo "## Registre automations"
  echo "Voir [[AUTO_PROCESSUS]] — ce pulse = couche **veille machine**, pas trading."
  echo
  echo "---"
  echo "_généré $TS_UTC · script \`pulse_sous_loeil.sh\`_"
} > "$REPORT"

cp "$REPORT" "$OUT/OUTBOX_OBSIDIAN/SOUS_L_OEIL.md"
cp "$REPORT" "$OUT/OUTBOX_OBSIDIAN/Index_Maison/SOUS_L_OEIL.md"

echo "$VERDICT mode=$MODE ram=${FREE_MB}M ace=$ACE_ON hulk=$HULK_ON"
echo "rapport: $REPORT"
[[ "$FAIL" -eq 0 ]]
