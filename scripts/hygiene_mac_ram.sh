#!/usr/bin/env bash
# hygiene_mac_ram.sh — purge WebKit.WebContent orphelins LOURDS/VIEUX (ppid=1)
# Ne touche JAMAIS Cursor / ACE777. Optionnel: --check (lecture seule).
#
# Critères kill (tous requis: ppid=1 + WebContent + stale):
#   - etime >= 30 min  OU  rss >= 100000 Ko (~100 Mo)
# Les WebContent frais (onglets Safari/Brave actifs) sont laissés.
set -euo pipefail

# Repli si ripgrep absent (constat 09/08 : rg non installe sur ce Mac)
if ! command -v rg >/dev/null 2>&1; then
  rg() { grep -E "$@"; }
fi

CHECK_ONLY=0
[[ "${1:-}" == "--check" ]] && CHECK_ONLY=1

echo "=== HYGIENE MAC RAM ==="

_mac_free_mb() {
  python3 - <<'PY'
import subprocess
try:
  ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
  ps = 16384
try:
  out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
except Exception:
  print("approx_free_MB=?")
  print("MAC_RAM=?")
  raise SystemExit(0)
d = {}
for line in out.splitlines()[1:]:
  if ":" in line:
    k, v = line.split(":", 1)
    try:
      d[k.strip()] = int(v.strip().rstrip("."))
    except Exception:
      pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"approx_free_MB={free:.0f}")
print("MAC_RAM=OK" if free >= 200 else "MAC_RAM=TIGHT")
PY
}

# etime → secondes (approx)
_etime_sec() {
  local e="$1"
  if [[ "$e" == *-* ]]; then
    local days="${e%%-*}" rest="${e#*-}"
    local h m s
    IFS=: read -r h m s <<< "$rest"
    echo $((10#$days * 86400 + 10#$h * 3600 + 10#$m * 60 + 10#$s))
  else
    local a b c
    IFS=: read -r a b c <<< "$e"
    if [[ -n "${c:-}" ]]; then
      echo $((10#$a * 3600 + 10#$b * 60 + 10#$c))
    else
      echo $((10#$a * 60 + 10#$b))
    fi
  fi
}

echo "WebContent (tous):"
ps -axo pid,ppid,pmem,rss,etime,comm 2>/dev/null | rg 'WebKit\.WebContent' || echo "(aucun)"

stale_pids=()
while read -r pid ppid rss etime; do
  [[ "$ppid" == "1" ]] || continue
  sec="$(_etime_sec "$etime")"
  if [[ "$sec" -ge 1800 || "$rss" -ge 100000 ]]; then
    echo "STALE pid=$pid rss=${rss}K etime=$etime (${sec}s)"
    stale_pids+=("$pid")
  fi
done < <(ps -axo pid=,ppid=,rss=,etime=,comm= 2>/dev/null | awk '$0 ~ /WebKit\.WebContent/ {print $1,$2,$3,$4}')

echo "stale_orphans=${#stale_pids[@]}"

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  _mac_free_mb
  exit 0
fi

killed=0
if [[ ${#stale_pids[@]} -gt 0 ]]; then
  for pid in "${stale_pids[@]}"; do
    echo "KILL stale WebContent pid=$pid"
    kill -9 "$pid" 2>/dev/null && killed=$((killed + 1)) || true
  done
fi
echo "killed=$killed"
[[ "$killed" -gt 0 ]] && sleep 1

echo "WebContent apres:"
ps -axo pid,ppid,pmem,rss,etime,comm 2>/dev/null | rg 'WebKit\.WebContent' || echo "(aucun / frais)"
_mac_free_mb
