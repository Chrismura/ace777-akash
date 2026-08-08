#!/usr/bin/env bash
# État Mac — température / RAM / disque / bots (lecture seule)
set -euo pipefail
echo "=== ÉTAT MAC ==="
echo "heure : $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo

echo "--- CPU / charge ---"
uptime
sysctl -n machdep.cpu.brand_string 2>/dev/null || true
echo

echo "--- RAM ---"
# pages libres approx
python3 - <<'PY'
import subprocess
try:
  ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
  ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
  if ":" not in line: continue
  k,v = line.split(":",1)
  try: d[k.strip()] = int(v.strip().rstrip("."))
  except Exception: pass
free = (d.get("Pages free",0)+d.get("Pages speculative",0))*ps/1024/1024
inact = d.get("Pages inactive",0)*ps/1024/1024
wired = d.get("Pages wired down",0)*ps/1024/1024
print(f"approx libre : {free:.0f} Mo")
print(f"inactive     : {inact:.0f} Mo")
print(f"wired        : {wired:.0f} Mo")
print("RAM=OK" if free >= 400 else ("RAM=TIGHT" if free >= 200 else "RAM=CRITIQUE"))
PY
echo
echo "Top RAM (processus) :"
ps -axo rss,pid,comm 2>/dev/null | sort -nr | head -8 | awk '{printf "  %6.0f Mo  pid=%s  %s\n", $1/1024, $2, $3}'
echo

echo "--- Disque ---"
df -h /Users/christophe 2>/dev/null | tail -1
echo

echo "--- Température (si dispo) ---"
if command -v osx-cpu-temp >/dev/null 2>&1; then
  osx-cpu-temp
elif command -v sudo >/dev/null 2>&1 && powermetrics --help >/dev/null 2>&1; then
  echo "(powermetrics demande sudo — skip ici)"
else
  # thermal pressure macOS
  if command -v pmset >/dev/null 2>&1; then
    pmset -g therm 2>/dev/null || echo "pas de capteur simple — regarde les ventilateurs / chaleur du chassis"
  fi
fi
echo

echo "--- Bots (doivent être OFF sans GO) ---"
if pgrep -lf 'GO_USINE|ace777_launch|paper_diprip|ollama serve' >/tmp/_etat_bots.txt 2>/dev/null; then
  cat /tmp/_etat_bots.txt
else
  echo "OK — rien qui tourne (ACE/Hulk/Ollama)"
fi
echo
echo "=== FIN ÉTAT MAC ==="
