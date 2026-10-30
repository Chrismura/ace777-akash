#!/usr/bin/env python3
"""CARNET FANTÔME du chuchoteur — papier, lecture seule, ZÉRO ordre réel.

Lit les chuchotements (Index_Maison/data/sommet_proche_hist.jsonl) + les prix
bruts (thermo/history.jsonl) et rejoue : entrée short virtuelle au chuchotement
quand flat, sortie TP −2 % / SL +1,5 % / TTL 24 h (mêmes chiffres que les
vrais shorts — même règle, pas de doublon de paramètres).

Ne touche JAMAIS aux states des vrais shorts. Sortie :
hulk-mexc/runs/short_shadow_journal.jsonl (une ligne par trade fermé).
"""
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# appelé depuis ace777-test-day1 : RACINE = ce dossier
if os.path.basename(RACINE) != "ace777-test-day1":
    RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

TP_PCT = 2.0
SL_PCT = 1.5
TTL_H = 24.0

HIST = os.path.join(RACINE, "Index_Maison", "thermo", "history.jsonl")
WHIS = os.path.join(RACINE, "Index_Maison", "data", "sommet_proche_hist.jsonl")
JOUR = os.path.join(RACINE, "hulk-mexc", "runs", "short_shadow_journal.jsonl")


def charger_marks():
    rows = []
    with open(HIST, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r.get("tsUnix") is not None and r.get("mark") is not None:
                rows.append((float(r["tsUnix"]), float(r["mark"])))
    rows.sort()
    return rows


def deja_joue():
    joues = set()
    try:
        with open(JOUR, encoding="utf-8") as f:
            for line in f:
                try:
                    joues.add(json.loads(line).get("ts_entree"))
                except Exception:
                    pass
    except FileNotFoundError:
        pass
    return joues


def main():
    marks = charger_marks()
    whis = [json.loads(l) for l in open(WHIS, encoding="utf-8") if l.strip()]
    whis.sort(key=lambda w: float(w["tsUnix"]))
    joues = deja_joue()
    n_nouveaux = 0
    # une seule position virtuelle à la fois (comme les vrais shorts) :
    # les chuchotements suivants pendant un trade ouvert sont ignorés.
    occupe_jusqua = 0.0
    with open(JOUR, "a", encoding="utf-8") as fj:
        for w in whis:
            t0 = float(w["tsUnix"])
            cle = w.get("ts")
            if cle in joues or t0 < occupe_jusqua:
                continue
            e0 = float(w["prix"])
            issue = None
            for (t, p) in marks:
                if t <= t0:
                    continue
                if p <= e0 * (1 - TP_PCT / 100):
                    issue = ("TP", t, p, round(100 * (e0 - p) / e0, 2))
                    break
                if p >= e0 * (1 + SL_PCT / 100):
                    issue = ("SL", t, p, round(100 * (e0 - p) / e0, 2))
                    break
                if (t - t0) / 3600 >= TTL_H:
                    issue = ("TTL", t, p, round(100 * (e0 - p) / e0, 2))
                    break
            if issue is None:
                continue  # trade encore ouvert : on attend, pas d'invention
            occupe_jusqua = issue[1]  # sortie connue → prochaine entrée après
            motif, ts, ps, pnl = issue
            from datetime import datetime, timezone
            fj.write(json.dumps({
                "ts_entree": cle, "prix_entree": e0,
                "ts_sortie": datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "prix_sortie": ps, "raison": motif, "pnl_pct": pnl,
                "contextes": w.get("contextes", []),
            }, ensure_ascii=False) + "\n")
            print(f"  fantôme {cle} @ {e0:.0f} → {motif} @ {ps:.0f} ({pnl:+.2f}%)")
            n_nouveaux += 1
    # bilan
    pnls = []
    for line in open(JOUR, encoding="utf-8"):
        try:
            pnls.append(float(json.loads(line)["pnl_pct"]))
        except Exception:
            pass
    if pnls:
        print(f"fantômes : n={len(pnls)} TP={sum(1 for x in pnls if x>0)} "
              f"médiane={sorted(pnls)[len(pnls)//2]:+.2f}% cumul={sum(pnls):+.2f}%")
    else:
        print("aucun trade fermé pour l'instant")
    return 0


if __name__ == "__main__":
    sys.exit(main())
