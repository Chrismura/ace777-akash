#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_horodatage_prix.py — les 22 prix qui ne tombent PAS dans leur minute
==========================================================================

POURQUOI CE FICHIER (23/09/2026, GO Christophe « compare une par une toutes les séquences »)
-------------------------------------------------------------------------------------------
`audit_sequences_trades.py` a trouvé que, sur 100 séquences vérifiables, **22 ont un prix
inscrit qui n'existe dans le [low, high] d'AUCUNE minute autour** — ou plutôt : qui n'est pas
dans SA minute. Deux causes possibles, et elles n'ont pas du tout la même conséquence :

  A. RETARD D'HORODATAGE — le prix est celui d'une AUTRE minute proche (le journal écrit
     l'heure de flush, pas celle de la décision). Le prix est vrai, l'heure est fausse :
     ça fausse tous les post-mortems (« qu'a fait le prix après ? ») sans rien fausser au PnL.
  B. PRIX PÉRIMÉ — le prix n'existe dans aucune minute proche (feed en retard d'une minute
     ou plus, ou prix lu sur un autre marché). Là, **on a paper-tradé un prix qui n'existait
     plus** : la justesse du remplissage est en cause, pas seulement l'écriture.

L'instrument tranche entre A et B, séquence par séquence, en relisant ± 6 minutes de klines
1 min MEXC et en cherchant l'écart (en minutes) qui contient le prix inscrit.

LECTURE SEULE, 0 ordre. Sortie : runs/AUDIT_HORODATAGE_PRIX_*.json/.txt
"""

from __future__ import annotations

import json
import statistics as stats
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
RUNS = RACINE / "runs"
SEQ = RUNS / "AUDIT_SEQUENCES_20260923.json"
TAG = datetime.now(timezone.utc).strftime("%Y%m%d")
UA = {"User-Agent": "hulk-audit/1.0"}


def http_json(url, timeout=15.0, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:                       # noqa: BLE001
            last = e
            time.sleep(0.5 * (i + 1))
    raise RuntimeError(f"HTTP KO {url} : {last}")


def ms(ts_iso: str) -> int:
    return int(datetime.strptime(ts_iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() * 1000)


def main() -> int:
    data = json.loads(SEQ.read_text(encoding="utf-8"))
    seqs = data.get("sequences") or []
    suspects: list[tuple[dict, str, dict]] = []
    for s in seqs:
        m = s.get("mexc") or {}
        if not m.get("ok"):
            continue
        for cote, lst in (("entrée", m.get("entrees") or []), ("sortie", m.get("sorties") or [])):
            for c in lst:
                if c.get("verifie") is False:
                    suspects.append((s, cote, c))
    print(f"=== POURQUOI {len(suspects)} PRIX INSCRITS NE TOMBENT PAS DANS LEUR MINUTE ===")
    print()

    offs = Counter()
    lignes = []
    for s, cote, c in suspects:
        t = ms(c["ts"])
        try:
            q = urllib.parse.urlencode({"symbol": s["pair"], "interval": "1m",
                                        "startTime": t - 6 * 60_000, "endTime": t + 6 * 60_000, "limit": 20})
            ks = http_json(f"https://api.mexc.com/api/v3/klines?{q}")
        except Exception as e:                       # noqa: BLE001
            lignes.append({"pair": s["pair"], "cote": cote, "ts": c["ts"], "prix": c["px"],
                           "erreur": str(e)[:100]})
            continue
        time.sleep(0.12)
        trouve = None
        for k in ks:
            lo, hi = float(k[3]), float(k[2])
            if lo <= c["px"] <= hi:
                trouve = int(round((int(k[0]) - (t // 60_000 * 60_000)) / 60_000))
                break
        # distance du prix au [low, high] de sa minute (en bps)
        dfin = None
        if c.get("bas") is not None:
            if c["px"] > c["haut"]:
                dfin = round((c["px"] - c["haut"]) / c["haut"] * 10000, 1)
            elif c["px"] < c["bas"]:
                dfin = round((c["bas"] - c["px"]) / c["bas"] * 10000, 1)
        item = {"pair": s["pair"], "cote": cote, "ts": c["ts"], "prix": c["px"],
                "minute_bas": c.get("bas"), "minute_haut": c.get("haut"),
                "hors_range_bps": dfin, "minute_ou_le_prix_existe_decalage": trouve}
        lignes.append(item)
        if trouve is not None:
            offs[trouve] += 1

    n_trouve = sum(1 for x in lignes if x.get("minute_ou_le_prix_existe_decalage") is not None)
    print(f"prix retrouvés dans une AUTRE minute proche : {n_trouve}/{len(suspects)}")
    print(f"distribution du décalage (minutes) : {dict(sorted(offs.items()))}")
    hors = [x for x in lignes if x.get("minute_ou_le_prix_existe_decalage") is None and "erreur" not in x]
    print(f"prix introuvables dans les ±6 min (classe « PRIX PÉRIMÉ ») : {len(hors)}")
    print()
    print(f"{'paire':<11}{'côté':<8}{'ts':<21}{'prix':>14}{'min bas':>14}{'min haut':>14}"
          f"{'hors bps':>10}{'décal. min':>11}")
    for x in sorted(lignes, key=lambda y: -abs(y.get("hors_range_bps") or 0))[:25]:
        if "erreur" in x:
            print(f"{x['pair']:<11}{x['cote']:<8}{x['ts']:<21}   (erreur: {x['erreur'][:40]})")
            continue
        dec = x["minute_ou_le_prix_existe_decalage"]
        print(f"{x['pair']:<11}{x['cote']:<8}{x['ts']:<21}{x['prix']:>14.8f}"
              f"{(x['minute_bas'] or 0):>14.8f}{(x['minute_haut'] or 0):>14.8f}"
              f"{(x['hors_range_bps'] or 0):>10.1f}{('—' if dec is None else f'{dec:+d}'):>11}")

    verdict = ("A. RETARD D'HORODATAGE (le prix est vrai, l'heure est fausse)"
               if n_trouve >= 0.7 * max(1, len(suspects)) else
               "B. PRIX PÉRIMÉ (le prix inscrit n'existait plus au moment écrit) — à trancher au cas par cas")
    print()
    print(f"VERDICT PROVISOIRE : {verdict}")
    rapport = {
        "instrument": "audit_horodatage_prix.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": SEQ.name, "n_suspects": len(suspects),
        "n_retrouves_autre_minute": n_trouve, "decalage_minutes": dict(sorted(offs.items())),
        "n_introuvables_pm6": len(hors), "verdict_provisoire": verdict, "cas": lignes,
        "lecture_seule": True, "ordres": 0,
    }
    (RUNS / f"AUDIT_HORODATAGE_PRIX_{TAG}.json").write_text(
        json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    text = "\n".join([
        f"AUDIT HORODATAGE vs PRIX — {rapport['ts_utc']}",
        f"suspects {len(suspects)} · retrouvés dans une autre minute {n_trouve} · "
        f"introuvables ±6 min {len(hors)}",
        f"décalages (min) : {dict(sorted(offs.items()))}",
        f"VERDICT : {verdict}",
    ] + [f"  {x.get('pair')} {x.get('cote')} {x.get('ts')} hors {x.get('hors_range_bps')} bps "
         f"décal {x.get('minute_ou_le_prix_existe_decalage')}" for x in lignes])
    (RUNS / f"AUDIT_HORODATAGE_PRIX_{TAG}.txt").write_text(text, encoding="utf-8")
    print(f"écrit : AUDIT_HORODATAGE_PRIX_{TAG}.json/.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
