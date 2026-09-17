#!/bin/bash
# v2conf_live.sh — vue LIVE colors du moteur V2-CONFIRMATION (papier, zéro ordre)
# lecture seule — Ctrl-C pour quitter
TH="$HOME/ace777-test-day1/Index_Maison/thermo"
G="\033[0;32m"; R="\033[0;31m"; Y="\033[0;33m"; C="\033[0;36m"; M="\033[0;35m"; B="\033[1m"; N="\033[0m"

while true; do
  clear
  echo -e "${B}════════ DUO ORIGINEL LIVE — RUN PAPIER (zéro ordre) ════════${N}"
  echo -e "  spec scellée : E32 (commit e4dbab98a9) · Scout 200\$ SL 16bps · Hunter 800\$ opposé hard-stop 32bps · fin 07h00 locale"
  echo ""

  # état courant
  if [ -f "$TH/v2conf_etat.json" ]; then
    python3 - "$TH/v2conf_etat.json" << 'PYEOF'
import json, sys
from datetime import datetime, timezone
d = json.load(open(sys.argv[1]))
c = d.get("contexte", {})
G, R, Y, C, M, B, N = "\033[0;32m", "\033[0;31m", "\033[0;33m", "\033[0;36m", "\033[0;35m", "\033[1m", "\033[0m"
reg = c.get("regime")
rc = G if reg == "HAUSSIER" else (R if reg == "BAISSIER" else Y)
print(f"  {B}MARCHÉ MAINTENANT{N}")
print(f"    régime de fond  : {rc}{reg}{N}")
f = c.get("funding")
zm = f is not None and f <= 0
fc = R if zm else G
print(f"    funding réel    : {fc}{f:.3e}{N} {'· VETO NÉGATIF actif (funding<=0)' if zm else '· veto non déclenché'}")
print(f"    flux nets 48 h  : {C}{c.get('flux48_btc', 0):+.1f} BTC{N} (seuil ±5)")
print(f"    BTC 24 h        : {c.get('chg24_pct', 0):+.2f} % · prix réf {c.get('prix_ref', 0):,.2f} $")
s = c.get("sigma_jour")
if s: print(f"    σ du jour       : {M}{s*100:.2f} %{N} · trailing arm ±{1.0*s*100:.2f} %")
print(f"    dernier cycle   : {d.get('dernier_cycle', '?')}")
print()
pos = d.get("position")
if pos:
    print(f"  {B}POSITION PAPIER OUVERTE{N}")
    pc = G if pos["dir"] > 0 else R
    print(f"    {pc}{pos['side']}{N} entrée {pos['entree']:,.2f} $ · arm {pos['arm']:,.2f} $ · depuis {pos['jour']}")
    for p in pos.get("confirmations", []):
        print(f"      ✓ {p}")
else:
    print(f"  {B}POSITION : aucune (silence — règle des 2 sources){N}")
print()
tr = d.get("trades", [])
print(f"  {B}CARNET : {len(tr)} trade(s) papier{N}")
for t in tr[-8:]:
    tc = G if t["net"] > 0 else R
    print(f"    {t['entree_j']} {t['side']:5} net {tc}{t['net']:+7.2f}${N} · {t['raison']}")
PYEOF
  fi

  echo ""
  echo -e "${B}── derniers événements (log live) ──${N}"
  tail -6 "$TH/v2conf_log.jsonl" 2>/dev/null | python3 -c "
import json, sys
for line in sys.stdin:
    try: d = json.loads(line)
    except: continue
    m = d.get('msg','')
    ts = d.get('ts','')[11:19]
    if 'OUVERT' in m: print(f'\033[0;35m  {ts} ▲ {m}\033[0m')
    elif 'FERMÉ' in m: print(f'\033[0;33m  {ts} ■ {m}\033[0m')
    elif 'ERREUR' in m: print(f'\033[0;31m  {ts} ✗ {m}\033[0m')
    elif 'aucune entrée' in m: print(f'  {ts} · {m[:110]}')
    elif 'cycle OK' in m: print(f'\033[0;32m  {ts} ✓ cycle OK — {d.get(\"regime\")} · funding {d.get(\"funding\"):.2e} · flux {d.get(\"flux48\"):+.1f} BTC · {d.get(\"prix_ref\")} $\033[0m')
    else: print(f'  {ts} {m[:110]}')
"
  echo ""
  echo -e "  \033[2mrafraîchi toutes les 10 s · Ctrl-C pour quitter · $(date -u +%H:%M:%SZ)\033[0m"
  sleep 10
done
