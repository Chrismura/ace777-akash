#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""replay_flux_fenetre_courte.py — REJEU 02/11 (GO Christophe).

Question : la fenetre 48h est trop lisse pour la rumeur — une fenetre 1-2h
aurait-elle crie la ou la 48h dormait (29/10 15h40) ?
Methode : MEMES fonctions que flux_nets_exchanges.py (dedupe txid, direction
vs registre, premiere detection = date d'evenement), agregees sur
[T-1h, T], [T-2h, T], [T-48h, T]. Lecture seule, 0 ordre, 0 ecriture.
"""
import os
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flux_nets_exchanges import charger_registre, charger_ledger_dedup, _agreger

EX = charger_registre()
MVT, STATS = charger_ledger_dedup()
print(f"ledger : {STATS['lignes']} lignes, {STATS['txid_uniques']} txid uniques")


def fmt_ts(dt):
    return dt.strftime("%Y-%m-%dT%H:%M")


def rejouer(nom, t_iso):
    t = datetime.fromisoformat(t_iso.replace("Z", "+00:00"))
    print(f"\n=== {nom} (T={t_iso}) ===")
    for h in (1, 2, 48):
        t0 = fmt_ts(t - timedelta(hours=h))
        w = _agreger(MVT, EX, t0, fmt_ts(t))
        s, e = w["btc_sortant"], w["btc_entrant"]
        net = s - e
        tot = s + e
        if tot <= 0:
            print(f"  {h:3d}h : n={w['n']} S=0 E=0 -> SILENCE (aucun mouvement observable)")
            continue
        ratio = abs(net) / tot
        sens = "SORTANT(retraits)" if net > 0 else "ENTRANT(depots)"
        flag = " ***" if ratio >= 0.20 and h <= 2 else ""
        print(f"  {h:3d}h : n={w['n']:3d} (S={w['n_sortant']} E={w['n_entrant']}) "
              f"S={s:9.0f} E={e:8.0f} net={net:+9.0f} |ratio|={ratio:.0%} {sens}{flag}")


# 29/10 : la soiree du crash (ledger OK : 13/10 -> now)
rejouer("29/10 veille chuchoteur", "2026-10-29T15:40:00Z")
rejouer("29/10 top 16h09", "2026-10-29T16:09:00Z")
rejouer("29/10 17h00 (pleine chute)", "2026-10-29T17:00:00Z")
rejouer("30/10 creux 12h", "2026-10-30T12:00:00Z")
rejouer("31/10 plat 12h (faux positif fantome)", "2026-10-31T12:00:00Z")
