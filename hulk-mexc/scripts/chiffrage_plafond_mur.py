#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE DU PLAFOND DE MISE — « 2 % du mur » : combien ça nous coûte, et à quel risque
=======================================================================================
GO Christophe 23/09/2026 : « la TAILLE d'abord ». Aucun ordre, aucun €, lecture seule.

LE MÉCANISME (lu dans le code RÉEL, paper_diprip.buy(), l.2060-2071)
  La mise annoncée (`current_notional`, compounding) traverse une CHAÎNE :
     × bag 0,5 · × tier B 0,25 · × mur adaptatif 0,6-1,2 · × fusible étage 2 · × slip gate 0,5
  puis le **PLAFOND PAR PROFONDEUR DE MUR** :
     `cap = mur_live(bid) × mise_max_pct_mur (défaut 0,02)`  — repli sur le mur du profil
     si la sonde live est absente. Raison du plafond : « EDEL 909 $ ne peut pas absorber
     20 $ sans slippage ».
  C'est ce dernier plafond qu'on mesure ici, sur les TRADES RÉELS.

CE QUE L'INSTRUMENT MESURE
  1. OÙ LE PLAFOND MORD : combien d'achats sortent AT au plafond, par paire, et de combien
     la mise est rabotée (engagé vs annoncé, annoncé lu dans le log du moteur).
  2. LE PRIX DU PLAFOND (chiffre brut) : si la mise avait été celle ANNONCÉE (plafond levé),
     ce que ces trades auraient rapporté — **même %**, même sortie, aucun trade inventé :
        ΔPnL = PnL_réalisé × (misé_visée / misé_engagée − 1)
     Puis le PnL du moteur dans la même fenêtre, pour situer l'ordre de grandeur.
  3. LE COÛT EN FACE (R18 : le risque se chiffre AVANT) : payer plus de spread sur le
     supplément de taille (spread médian MESURÉ du profil, croisé une fois par côté) et
     la profondeur de mur que chaque paire peut absorber. Le reste — l'IMPACT — n'est
     PAS mesurable avec le journal actuel : c'est déclaré, pas contourné.

LIMITES DÉCLARÉES (E8)
  · Le ΔPnL est BRUT : il suppose que le prix ne bouge pas parce qu'on prend plus gros.
    C'est FAUX au-delà de ce que le carnet absorbe — c'est précisément le coût manquant.
  · Appariement acheteur→ventes FIFO par paire (comme chiffrage_compounding.py) ; un tour
    avec DCA/2× est scalé d'un bloc.
  · Le mur est mesuré à un instant (sonde) ; la profondeur réelle varie.
Usage : python3 chiffrage_plafond_mur.py [--jours 5]
"""
import argparse
import gzip
import json
import os
from collections import deque
from datetime import datetime, timezone

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CSV = os.path.join(RUNS, "PAPER_V1_20260922_090430.csv")
LOGS = [os.path.join(RUNS, "PAPER_WATCHDOG_STDOUT.log"),
        os.path.join(RUNS, "PAPER_WATCHDOG_STDOUT.log.1.gz")]
PROFILS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "strategie", "universe_profils.json")


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s):
    s = s.strip().rstrip("Z")
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc).timestamp()
        except ValueError:
            continue
    return None


def profils():
    raw = json.load(open(PROFILS, encoding="utf-8"))
    return {k: v for k, v in raw.items() if isinstance(v, dict) and "USDT" in k}


def lire_plafonds():
    """Les lignes « plafonnée » du moteur : la SEULE source qui dit ce qu'on visait et
    ce que le mur a autorisé. On garde par paire le mur le plus récent vu et le cap."""
    out = {}
    for chemin in LOGS:
        if not os.path.exists(chemin):
            continue
        ouvre = gzip.open(chemin, "rt", errors="ignore") if chemin.endswith(".gz") \
            else open(chemin, encoding="utf-8", errors="ignore")
        with ouvre as f:
            for l in f:
                if "plafonnée" not in l:
                    continue
                # [2026-09-19T15:18:46Z] RWAINCUSDT mise 28.53$ → plafonnée 27.75$ (mur live 1,387$)
                try:
                    ts = parse(l[1:l.index("]")])
                    apres = l[l.index("]") + 1:]
                    pair = apres.strip().split(" ")[0]
                    vise = float(apres.split("mise ")[1].split("$")[0])
                    cap = float(apres.split("plafonnée ")[1].split("$")[0])
                    mur = float(apres.split("mur ")[1].replace("$", "").replace(")", "")
                                .replace("live", "").replace("profil", "")
                                .replace("médian", "").replace(",", "").strip())
                except Exception:
                    continue
                d = out.setdefault(pair, {"n": 0, "mur": 0.0, "cap": 0.0, "vise_max": 0.0,
                                          "dernier": None, "vise_moy": 0.0, "somme_vise": 0.0})
                d["n"] += 1
                if ts and (d["dernier"] is None or ts > d["dernier"]):
                    d["dernier"] = ts
                    d["mur"], d["cap"] = mur, cap
                d["vise_max"] = max(d["vise_max"], vise)
                d["somme_vise"] += vise
                d["vise_moy"] = d["somme_vise"] / d["n"]
    return out


def lire_trades(depuis):
    """Trades réels du journal du run : chaque BUY apparié FIFO à ses ventes."""
    par_paire = {}
    with open(CSV, encoding="utf-8", errors="ignore") as f:
        for l in f:
            c = l.split(",")
            if len(c) < 4:
                continue
            pair = c[1]
            try:
                ts = parse(c[0])
            except Exception:
                ts = None
            if ts is None or ts < depuis:
                continue
            par_paire.setdefault(pair, []).append(
                {"ts": ts, "type": c[2], "px": float(c[4] or 0), "qty": float(c[6] or 0),
                 "pnl": float(c[7] or 0), "raison": c[-1].strip()})
    return par_paire


def apparier(trades):
    """FIFO : rend les BUY avec le PnL réalisé et le % du tour (somme des ventes)."""
    sorties, file = [], deque()
    for t in trades:
        if t["type"] == "BUY" and t["qty"] > 0:
            file.append({"ts": t["ts"], "px": t["px"], "qty": t["qty"], "pnl": 0.0,
                         "vendu": 0.0, "raisons": []})
        elif t["type"] in ("SELL", "SELL_PARTIAL", "DUST_SWEEP", "BAG_SELL") and file:
            q = t["qty"]
            while q > 1e-12 and file:
                b = file[0]
                pris = min(q, b["qty"] - b["vendu"])
                if pris <= 0:
                    file.popleft()
                    continue
                part = pris / t["qty"] if t["qty"] else 0.0
                b["pnl"] += t["pnl"] * part
                b["vendu"] += pris
                b["raisons"].append(t["raison"])
                q -= pris
                if b["vendu"] >= b["qty"] - 1e-12:
                    sorties.append(file.popleft())
    for b in file:  # positions encore ouvertes au dernier cycle
        b["ouverte"] = True
        sorties.append(b)
    return sorties


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=float, default=5.0)
    a = ap.parse_args()
    maintenant = datetime.now(timezone.utc).timestamp()
    depuis = maintenant - a.jours * 86400
    prof = profils()
    plaf = lire_plafonds()
    trades = lire_trades(depuis)
    buys = {p: apparier(t) for p, t in trades.items()}

    print("SOURCE : journal du run (trades réels) + log du moteur (lignes « plafonnée »)")
    print(f"FENÊTRE : {a.jours:.0f} derniers jours — depuis {iso(depuis)}\n")

    print("== 1. OÙ LE PLAFOND MORD (ce que le moteur a écrit lui-même) ==")
    print(f"  {'paire':12}{'mur (dernier vu)':>18}{'cap 2 %':>10}{'mise visée (moy)':>18}"
          f"{'raboté':>9}{'lignes log':>11}")
    print("  (une « ligne log » n'est PAS un achat : le moteur réécrit ce message à chaque"
          " cycle où la mise est rabotée — seule la section 2 compte des ACHATS)")
    for p, d in sorted(plaf.items(), key=lambda x: -(x[1]["vise_moy"] - x[1]["cap"])):
        if d["cap"] <= 0 or d["vise_moy"] <= 0:
            continue
        rab = (1 - d["cap"] / d["vise_moy"]) * 100
        print(f"  {p.replace('USDT', ''):12}{d['mur']:>18,.0f}{d['cap']:>10.2f}"
              f"{d['vise_moy']:>18.2f}{rab:>8.0f}%{d['n']:>9}")
    print("  → le plafond ne mord QUE sur les petites profondeurs (le carnet impose sa taille)")

    print("\n== 2. LE PRIX DU PLAFOND — sur les trades RÉELS, à plat au plafond ==")
    print(f"  {'paire':12}{'achats au cap':>14}{'engagé':>9}{'% réalisé':>11}{'PnL réel':>10}"
          f"{'visée':>9}{'ΔPnL si levé':>14}")
    tot_reel = tot_d = 0.0
    lignes = []
    for p, achats in sorted(buys.items()):
        cap = (plaf.get(p) or {}).get("cap") or 0.0
        vise = (plaf.get(p) or {}).get("vise_moy") or 0.0
        au_cap = [b for b in achats if cap > 0 and b["px"] * b["qty"] >= cap * 0.98]
        if not au_cap:
            continue
        engage = sum(b["px"] * b["qty"] for b in au_cap)
        reel = sum(b["pnl"] for b in au_cap)
        pct = (reel / engage * 100) if engage else 0.0
        d_pnl = sum(b["pnl"] * (vise / (b["px"] * b["qty"]) - 1)
                    for b in au_cap if b["px"] * b["qty"] > 0) if vise else 0.0
        tot_reel += reel
        tot_d += d_pnl
        lignes.append((p, len(au_cap), engage, pct, reel, vise, d_pnl))
        print(f"  {p.replace('USDT', ''):12}{len(au_cap):>14}{engage:>9.2f}{pct:>+10.1f}%"
              f"{reel:>+10.2f}{vise:>9.2f}{d_pnl:>+14.2f}")
    if not lignes:
        print("  (aucun achat au plafond sur la fenêtre)")
    print(f"  {'TOTAL':12}{'':>14}{'':>9}{'':>11}{tot_reel:>+10.2f}{'':>9}{tot_d:>+14.2f}")

    print("\n== 3. LE COÛT EN FACE (R18 : le risque se chiffre AVANT) ==")
    print(f"  {'paire':12}{'spread méd.':>13}{'profondeur mur':>16}{'suppl. à prendre':>18}"
          f"{'spread payé en +':>18}")
    tot_spread = 0.0
    for p, n, engage, pct, reel, vise, d in lignes:
        cal = (prof.get(p) or {}).get("calib") or {}
        sp = float((prof.get(p) or {}).get("spread_bps_med") or 0.0)
        mur = float((prof.get(p) or {}).get("mur_bid_med") or 0.0)
        suppl = max(0.0, (vise - engage / max(1, n)) * n)
        # le spread se croise une fois à l'achat : coût = supplément × spread (en bps / 1e4)
        cout = suppl * sp / 10000.0
        tot_spread += cout
        print(f"  {p.replace('USDT', ''):12}{sp:>12.1f}bps{mur:>16,.0f}{suppl:>18.2f}"
              f"{cout:>18.2f}")
    print(f"  {'TOTAL':12}{'':>13}{'':>16}{'':>18}{tot_spread:>18.2f}")
    print(f"\n  BILAN BRUT : gain chiffré {tot_d:+.2f} $ · coût de spread chiffré "
          f"{-tot_spread:+.2f} $ → net {tot_d - tot_spread:+.2f} $")
    print(f"  ⚠️ MESURE MANQUANTE ET NOMMÉE : l'IMPACT du supplément de taille sur le prix.")
    print(f"     On sait mesurer le spread (ci-dessus) et la profondeur du carnet ; on ne sait")
    print(f"     PAS mesurer ce que prend le prix quand on croque 10-20 % du mur au lieu de 2 %.")
    print(f"     Le moteur est en PAPER : les remplissages sont au prix observé, donc l'impact")
    print(f"     est structurellement absent du journal. Tant que ce chiffre n'existe pas, le")
    print(f"     gain ci-dessus est une BORNE HAUTE, pas une promesse (R18).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
