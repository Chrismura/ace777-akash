#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE DE LA SORTIE D'UNE PAIRE — « pourquoi la paire qui monte perd »
=========================================================================
Demande Christophe 23/09/2026 (GO 1) : RIZE a des jambes à +37 % et c'est **la seule
perdante** de la fenêtre (−1,04 $ en 23 ventes). Si ce n'est pas l'entrée, c'est la
SORTIE. Cet instrument la décompose, sur les trades RÉELS du journal du run :

  1. LE RÉSULTAT : PnL réellement encaissé (colonne `pnl` écrite par le moteur), nombre
     de clôtures, et les frais estimés (5 bps/côté sur le prix et la quantité réels).
  2. OÙ ÇA PART — par MOTIF DE SORTIE (le moteur écrit toujours sa raison) :
     n, PnL, et le **GB (giveback) moyen calculé par différence de PRIX** :
     `pic atteint pendant la détention − prix de sortie`, en points et en $ réels.
  3. LA RÉ-ENTRÉE AU SOMMET : combien de BUY ont été passés **plus haut** que la dernière
     vente (le va-et-vient qui coûte), et ce que CES trades-là ont donné.
  4. LE JUGEMENT ABSENT : « acheter et garder » sur la même fenêtre, même base ($ engagés
     réels) — pour savoir si le problème est la sortie ou la paire elle-même.

LECTURE SEULE · 0 ordre · 0 € · aucune écriture moteur.
Usage : python3 chiffrage_sortie_paire.py --paire RIZEUSDT [--depuis 2026-08-01T00:00]
"""
import argparse
import os
import sys
from datetime import datetime, timezone

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from chiffrage_pump_manque import parse, csv_actuel, charger_tout  # noqa: E402

FEE = 0.0005  # 5 bps par côté (convention de la maison)


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lire_ops(paire):
    """Toutes les opérations de la paire, dans l'ordre du journal (une seule vérité)."""
    ops = []
    with open(csv_actuel(), encoding="utf-8", errors="ignore") as f:
        for l in f:
            c = l.rstrip("\n").split(",")
            if len(c) < 11 or c[1] != paire or c[2] not in (
                    "BUY", "SELL", "SELL_PARTIAL", "BAG_SELL", "DUST_SWEEP"):
                continue
            try:
                ts = parse(c[0].strip())
            except Exception:
                continue
            ops.append({"ts": ts, "utc": c[0], "event": c[2], "prix": float(c[4] or 0),
                        "qty": float(c[6] or 0), "pnl": float(c[7] or 0),
                        "cadence": float(c[9] or 0) if c[9].strip() else 0.0,
                        "raison": (c[10] or "").strip()})
    ops.sort(key=lambda o: o["ts"])
    return ops


def chemin(paire, t0, t1):
    """Chemin de prix dense (log + archives) sur [t0, t1] — pour le pic réel."""
    tout = charger_tout().get(paire) or []
    return [(ts, px) for ts, px, _reg in tout if t0 <= ts <= t1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paire", default="RIZEUSDT")
    ap.add_argument("--depuis", default="")
    a = ap.parse_args()
    depuis = parse(a.depuis) if a.depuis else 0.0
    ops = lire_ops(a.paire)
    if not ops:
        print(f"[ERR] aucune opération {a.paire} dans le journal du run")
        return 2
    # On lit TOUT le journal (un BUY antérieur à la fenêtre explique la clôture qui suit)
    # et on ne filtre que les CLÔTURES pour l'analyse.
    buys = [o for o in ops if o["event"] == "BUY"]
    sells = [o for o in ops if o["event"] != "BUY" and (not depuis or o["ts"] >= depuis)]
    if not sells:
        print(f"[ERR] aucune clôture {a.paire} depuis la date demandée")
        return 2
    # pics/creux : on interroge le chemin dense UNE fois sur toute la fenêtre
    tout = charger_tout().get(a.paire) or []
    def pic_creux(t0, t1):
        seg = [px for ts, px, _ in tout if t0 <= ts <= t1]
        return (max(seg), min(seg)) if seg else (None, None)

    print(f"SOURCE : journal du run (opérations réelles) + chemin de prix dense (log + archives)")
    print(f"PAIRE  : {a.paire} · {len(sells)} clôture(s) analysée(s) ·"
          f" {sells[0]['utc']} → {sells[-1]['utc']}"
          f" · {len(buys)} BUY dans tout le journal")
    pnl = sum(o["pnl"] for o in sells)
    frais = sum(o["qty"] * o["prix"] * FEE for o in sells if o["qty"] and o["prix"])
    print(f"\n== 1. LE RÉSULTAT RÉEL ==")
    print(f"  BUY {len(buys)} · clôtures {len(sells)} · PnL encaissé (colonne pnl du moteur)"
          f" = {pnl:+.4f} $")
    print(f"  frais estimés (5 bps × 2 × qty × prix réels) = −{frais:.4f} $  "
          f"→ variation de prix nette ≈ {pnl + frais:+.4f} $")

    print(f"\n== 2. OÙ ÇA PART — par MOTIF DE SORTIE (pic réel pendant la détention) ==")
    par, par_gb = {}, {}
    for s in sells:
        # la VRAIE entrée = le dernier BUY antérieur à la clôture (pas un index)
        b = None
        for cand in buys:
            if cand["ts"] < s["ts"]:
                b = cand
            else:
                break
        t0 = b["ts"] if b else s["ts"] - 3600
        pic, creux = pic_creux(t0, s["ts"])
        motif = (s["raison"].split(" ")[0] or "?")[:18]
        d = par.setdefault(motif, {"n": 0, "pnl": 0.0, "pts": 0.0, "usd": 0.0})
        d["n"] += 1
        d["pnl"] += s["pnl"]
        if pic:
            d["pts"] += (pic / s["prix"] - 1) * 100
            d["usd"] += (pic - s["prix"]) * (s["qty"] or 0)
    print(f"  {'motif':20}{'n':>4}{'PnL $':>11}{'GB moyen':>11}{'$ laissés au pic':>18}")
    for m, d in sorted(par.items(), key=lambda kv: -kv[1]["n"]):
        gb = d["pts"] / d["n"] if d["n"] else 0.0
        print(f"  {m:20}{d['n']:>4}{d['pnl']:>+11.2f}{gb:>10.2f}%{d['usd']:>17.2f} $")

    print(f"\n== 3. LA RÉ-ENTRÉE (le va-et-vient) ==")
    hautes, pnl_hautes = 0, 0.0
    for i, b in enumerate(buys):
        prec = [s for s in sells if s["ts"] < b["ts"]]
        if not prec:
            continue
        if b["prix"] > prec[-1]["prix"]:
            hautes += 1
            suiv = [s for s in sells if s["ts"] > b["ts"]]
            if suiv:
                pnl_hautes += suiv[0]["pnl"]
    print(f"  BUY passés PLUS HAUT que la dernière vente : {hautes}/{len(buys)}"
          f"   → PnL des clôtures qui ont suivi : {pnl_hautes:+.2f} $")

    print(f"\n== 4. LE JUGE QUE PERSONNE NE REGARDE : « acheter et garder » ==")
    p0, p1 = tout[0][1] if tout else 0, tout[-1][1] if tout else 0
    if tout:
        print(f"  prix {tout[0][0] and iso(tout[0][0])} {p0:.6g} → {iso(tout[-1][0])}"
              f" {p1:.6g} = {(p1 / p0 - 1) * 100:+.1f} %")
    eng = sum(o["qty"] * o["prix"] for o in buys if not depuis or o["ts"] >= depuis)
    print(f"  montant réellement engagé à l'achat (Σ qty × prix) : {eng:.2f} $")
    if tout and p0 > 0:
        net_hold = eng * (p1 / p0 - 1) - eng * FEE * 2
        print(f"  même argent simplement GARDÉ : {net_hold:+.2f} $"
              f"   vs moteur {pnl:+.2f} $   → écart {pnl - net_hold:+.2f} $")
    print("  ⚠️ PORTÉE : le « garder » suppose d'être entré au PREMIER instant du chemin"
          " (pas au même instant que le moteur) — c'est un ordre de grandeur du bêta de"
          " la paire, pas un P&L concurrent (E8).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
