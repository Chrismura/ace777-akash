#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE DU STOP SERRÉ — ce qu'un PLAFOND de stop aurait donné (23/09/2026)
============================================================================
Exigence de la FAMILLE (session ouverte, tour 1) :
  · Gemini  : « la justification exacte de la formule qui fixe le stop de RIZE à 44 % » et
              « un test montrant un stop exécuté à −10 % max sur une paire volatile » ;
  · DeepSeek : « backtest avec stop ≤ 15 % sur RIZE » (fait tranchant).

FORMULE EXACTE DU STOP (lue dans le code, pas devinée) — `paper_diprip.py` :
    stop = max( stop_floor ; cadence × STOP_CADENCE_MULT )
  stop_floor          = profil.calib.stop_pct  (RIZE 8,0 · EDEL 10,3 · CHIP 7,0 · RED/BTC 6/5)
  STOP_CADENCE_MULT   = **LU dans config/defaults.env au moment de tourner** (0.80 le 23/09)

⚠ CORRECTION E18 (23/09, découverte en produisant les mesures du jury) : ce fichier AFFIRMAIT
  « STOP_CADENCE_MULT = 0.70 (config) » — c'était le **DÉFAUT du code**, pas la config, et 8 scripts
  et documents ont repris ce chiffre. La valeur n'est plus écrite nulle part : elle est LUE.
  cadence             = agitation mesurée de la PAIRE (≠ d'une paire à l'autre)
⇒ Le stop n'est pas « 8 % » : il est **proportionnel à l'agitation de la paire**. Pour RIZE
(cadence ≈ 60 %) ça donne 39-44 % ; pour BTC (cadence faible) ça donne le plancher de 5 %.

CE QUE CHIFFRE CET INSTRUMENT (contre-factuel mesuré, pas une opinion)
----------------------------------------------------------------------
Pour chaque trade des 10 derniers jours, sur les bougies 1 min MEXC :
  · niveau de stop RÉEL de la machine (lu dans ses motifs) → PnL tel qu'il a eu lieu ;
  · puis on PLAFONNE le stop à L ∈ {10 · 15 · 20 · 25 %} : on cherche LA PREMIÈRE minute où le
    marché touche entry × (1−L) ; si elle existe, la sortie se fait à ce niveau ; sinon on garde
    la sortie réelle enregistrée. On recalcule le PnL (quantité réelle, frais estimés).
  · On rapporte : combien de trades changent, le PnL brut/net avant/après, par paire.

CE QUE CE CHIFFRAGE NE FAIT PAS (déclaré, R8 — sinon c'est un mensonge par omission)
------------------------------------------------------------------------------------
1. **Aucune ré-entrée simulée** : le cash libéré plus tôt n'est pas remployé. Un stop plus serré
   change donc AUSSI ce qui aurait été acheté après — non simulé ici.
2. **Sortie au niveau exact** du plafond (pas de glissement) : le chiffre est OPTIMISTE pour le
   stop serré ; un remplissage réel serait un peu pire.
3. Les sorties trailing/rip enregistrées restent la référence quand le plafond n'est pas touché.
4. Aucun ordre, aucune écriture moteur, 0 €.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import importlib.util
import json
import re
import sys
from datetime import datetime, timedelta, timezone

RACINE = Path(__file__).resolve().parent.parent
RUNS = RACINE / "runs"
FRAIS_BPS_COTE = 5.0
PLAFONDS = [10.0, 15.0, 20.0, 25.0]


def _cfg() -> dict:
    """Lit config/defaults.env — la VALEUR EFFECTIVE, jamais le défaut du code (E18)."""
    out = {}
    p = Path(__file__).resolve().parent.parent / "config" / "defaults.env"
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def _oracle(pair: str, de_ms: int, a_ms: int):
    spec = importlib.util.spec_from_file_location("oracle2", RACINE / "scripts" / "oracle_independant.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["oracle2"] = mod
    spec.loader.exec_module(mod)
    return mod.klines(pair, de_ms, a_ms, False)


def ts_ms(s):
    return int(datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() * 1000)


def iso(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=float, default=10.0)
    ap.add_argument("--json", default=None)
    ap.add_argument("--txt", default=None)
    a = ap.parse_args()
    b = datetime.now(timezone.utc) - timedelta(days=a.jours)
    depuis = b.replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")

    j = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda x: x.stat().st_mtime)[-1]
    seqs: dict[str, list] = {}
    for r in csv.reader(j.open(newline="", encoding="utf-8", errors="replace")):
        if len(r) < 11 or r[0] == "ts" or r[0] < depuis:
            continue
        if r[2] not in ("BUY", "SELL", "SELL_PARTIAL", "STOP"):
            continue
        seqs.setdefault(r[1], []).append({"ts": r[0], "event": r[2], "price": float(r[4] or 0),
                                          "qty": float(r[6] or 0), "pnl": float(r[7] or 0),
                                          "reason": r[10]})
    _c = _cfg()
    _mu = _c.get("STOP_CADENCE_MULT", "0.70")            # DÉFAUT du code, remplacé par la config
    _fl = _c.get("STOP_FLOOR_PCT", "4.0")
    print(f"CHIFFRAGE STOP SERRÉ — {a.jours:g} j · source : bougies 1 min MEXC + journal horodaté")
    print(f"Formule du stop, LUE à l'exécution : stop = max(calib.stop_pct ; cadence × {_mu})  "
          f"[STOP_FLOOR_PCT global = {_fl}]\n")

    trades, par_paire = [], {}
    for paire in sorted(seqs):
        cur = None
        seq_l: list = []
        for e in seqs[paire]:
            if e["event"] == "BUY":
                if cur and cur["sorties"]:
                    seq_l.append(cur)
                cur = {"buy": e, "sorties": []}
            elif cur is not None:
                cur["sorties"].append(e)
        if cur and cur["sorties"]:
            seq_l.append(cur)
        if not seq_l:
            continue
        ts_all = [ts_ms(s["buy"]["ts"]) for s in seq_l] + \
                 [ts_ms(o["ts"]) for s in seq_l for o in s["sorties"]]
        kl = _oracle(paire, min(ts_all) - 3600_000, max(ts_all) + 6 * 3600_000)

        def pnl_plafond(p_b, p_s_reel, qty, t_b, t_s_reel, spread, niveau):
            """Sortie au PREMIER contact du niveau (bougies 1 min), sinon sortie réelle."""
            seuil = p_b * (1 - niveau / 100)
            cont = next((k for k in kl if t_b <= int(k[0]) < t_s_reel and float(k[3]) <= seuil), None)
            if cont is None:
                return p_s_reel, None
            return seuil, iso(int(cont[0]))

        for s in seq_l:
            bq, sorties = s["buy"], s["sorties"]
            qty = sum(o["qty"] for o in sorties)
            if qty <= 0:
                continue
            p_b = bq["price"]
            p_s = sum(o["price"] * o["qty"] for o in sorties) / qty
            t_b, t_s = ts_ms(bq["ts"]), ts_ms(sorties[-1]["ts"])
            brut = sum(o["pnl"] for o in sorties)
            spread = 0.0
            nom = None
            for o in sorties:
                m = re.search(r"spread=([0-9.]+)bps", o["reason"])
                if m:
                    spread = float(m.group(1))
                m2 = re.search(r"stop[_-]([0-9.]+)%", o["reason"])
                if m2 and nom is None:
                    nom = float(m2.group(1))
            couts = qty * ((p_b + p_s) / 2) * (2 * FRAIS_BPS_COTE + spread) / 10000.0
            ligne = {"paire": paire, "achat": bq["ts"], "mise_usdt": round(qty * p_b, 2),
                     "stop_machine_pct": nom, "brut_reel": round(brut, 4),
                     "net_reel": round(brut - couts, 4), "plafonds": {}}
            for L in PLAFONDS:
                if nom is not None and nom <= L:
                    ligne["plafonds"][f"cap_{L:g}"] = {"inchange": "stop machine déjà ≤ plafond"}
                    continue
                p_new, t_new = pnl_plafond(p_b, p_s, qty, t_b, t_s, spread, L)
                brut_new = qty * (p_new - p_b)
                couts_new = qty * ((p_b + p_new) / 2) * (2 * FRAIS_BPS_COTE + spread) / 10000.0
                ligne["plafonds"][f"cap_{L:g}"] = {
                    "touche": t_new is not None, "sortie_au_plafond": t_new,
                    "brut": round(brut_new, 4), "net": round(brut_new - couts_new, 4),
                    "delta_net": round((brut_new - couts_new) - (brut - couts), 4),
                }
            trades.append(ligne)
            st = par_paire.setdefault(paire, {"n": 0, "net_reel": 0.0, "stop_max_pct": 0.0,
                                              "cap15": {"touche": 0, "net": 0.0}})
            st["n"] += 1
            st["net_reel"] += brut - couts
            if nom:
                st["stop_max_pct"] = max(st["stop_max_pct"], nom)
            c15 = ligne["plafonds"].get("cap_15") or {}
            if c15.get("touche"):
                st["cap15"]["touche"] += 1
                st["cap15"]["net"] += c15["net"]
            else:
                st["cap15"]["net"] += brut - couts

    tot = {"net_reel": round(sum(t["net_reel"] for t in trades), 2)}
    for L in PLAFONDS:
        s = 0.0
        n_touche = 0
        for t in trades:
            c = t["plafonds"].get(f"cap_{L:g}") or {}
            if c.get("inchange"):
                s += t["net_reel"]
            else:
                s += c.get("net", t["net_reel"])
                n_touche += 1 if c.get("touche") else 0
        tot[f"cap_{L:g}"] = {"net": round(s, 2), "trades_qui_changent": n_touche,
                             "delta_vs_reel": round(s - tot["net_reel"], 2)}

    L_ = [f"CHIFFRAGE DU STOP SERRÉ — {len(trades)} trades · {len(par_paire)} paires · {a.jours:g} j",
          f"Formule du stop (LUE dans config/defaults.env) : stop = max(calib.stop_pct ; "
          f"cadence de la paire × {_mu})", "",
          "=== 1. LE NIVEAU QUE LA MACHINE SE DONNE (lu dans ses motifs), et ce qu'un PLAFOND aurait donné ===",
          f"{'paire':<12}{'n':>4}{'stop max':>10}{'net réel $':>12}{'net si cap 15 %':>18}{'trades touchés':>16}"]
    for p in sorted(par_paire, key=lambda x: -par_paire[x]["stop_max_pct"]):
        d = par_paire[p]
        L_.append(f"{p:<12}{d['n']:>4}{d['stop_max_pct']:>9.2f}%{d['net_reel']:>12.2f}"
                  f"{d['cap15']['net']:>18.2f}{d['cap15']['touche']:>16}")
    L_ += ["", "=== 2. TOTAL 10 JOURS — le NET selon le plafond de stop ===",
           "  (sortie au niveau exact du plafond, sans ré-entrée : chiffre OPTIMISTE pour le plafond)", ""]
    for L in PLAFONDS:
        d = tot[f"cap_{L:g}"]
        L_.append(f"  plafond {L:>4.0f} % : net {d['net']:>8.2f} $  "
                  f"(réel {tot['net_reel']:>8.2f} $) · écart {d['delta_vs_reel']:>+7.2f} $ · "
                  f"{d['trades_qui_changent']} trade(s) sorti(s) plus tôt")
    L_ += ["", "=== 3. CE QUE CE CHIFFRE NE DIT PAS (déclaré) ===",
           "  · aucune ré-entrée simulée : le cash libéré plus tôt n'est pas remployé ;",
           "  · sortie supposée AU niveau du plafond (pas de glissement) → OPTIMISTE ;",
           "  · les sorties trailing/rip enregistrées restent la référence hors contact.",
           "", "Lecture seule · 0 ordre · 0 €."]
    texte = "\n".join(L_)
    print("\n" + texte)
    if a.txt:
        Path(a.txt).write_text(texte + "\n", encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps({
            "instrument": "chiffrage_stop_serre.py",
            "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "depuis": depuis,
            "formule_stop": f"max(calib.stop_pct ; cadence × STOP_CADENCE_MULT {_mu})",
            "formule_source": "config/defaults.env (lu à l'exécution — plus jamais un défaut de code, E18)",
            "totaux": tot, "par_paire": par_paire, "trades": trades,
            "limites_declarees": [
                "Aucune ré-entrée simulée (le cash libéré plus tôt n'est pas remployé).",
                "Sortie supposée au niveau exact du plafond → chiffre OPTIMISTE.",
                "Sorties trailing/rip enregistrées conservées hors contact du plafond.",
            ],
            "lecture_seule": True, "ordres": 0,
        }, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
