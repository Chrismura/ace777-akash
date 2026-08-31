#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""short_btc.py — SHORT BTC PAPER piloté par le protocole divergence (31/08, GO Christophe).

POURQUOI CE MODULE
------------------
Christophe, 31/08 : « cherche-moi un actif en contre-tendance… l'idée c'est de
contrer BTC » → conclusion de l'audit : il n'existe PAS d'actif long qui monte
quand BTC baisse (tout est corrélé, beta positif partout). La SEULE vraie
contre-tendance exploitable = SHORT BTC quand le marché est en sommet.
Ce module l'implémente en PAPER (zéro risque, zéro argent réel).

SOURCE DE VÉRITÉ : ZÉRO APPEL RÉSEAU
------------------------------------
Le moteur Hulk (paper_diprip.py) écrit `runs/croisement_contexte.jsonl` à chaque
tick (~1 point/pair/minute, prix + m6_pct + régime…). Ce module LIT ce fichier
(comme analyse_divergence.py) → même source de prix que Hulk, cohérent,
robuste, aucun timeout réseau possible.

SIGNAL (score composite 0..10) — entrée short si score >= SCORE_ENTREE
---------------------------------------------------------------------
  A. CONTEXTE SOMMET (protocole divergence, angle 3) : corr(m6 BTC à H,
     delta panier H→H+4h) sur toute la base. Si <= -0.15 → +3 ; <= -0.10 → +2 ;
     <= -0.05 → +1. C'est le « BTC pompe, le marché baisse ensuite ».
  B. SURCHAUFFE INSTANTANÉE : % des paires actives avec m6 > +3% (dernière
     heure). >= 60% → +3 ; >= 40% → +2 ; >= 25% → +1. Euphorie généralisée.
  C. BTC EN SURCHAUFFE : m6 BTC >= +2.0% → +2 ; >= +1.0% → +1.
  D. MOMENTUM 24H BTC : move24 >= +3.0% → +2 ; >= +1.5% → +1.

SORTIE (première condition atteinte)
------------------------------------
  - TAKE PROFIT : prix <= entrée × (1 - TP_PCT/100)
  - STOP LOSS   : prix >= entrée × (1 + SL_PCT/100)
  - SIGNAL ÉTEINT : score < SCORE_SORTIE (le sommet s'est dissipé)
  - TIME-OUT    : position ouverte depuis > TTL_H heures

GARDES-FOUS
-----------
  - Gating temporel (Cortana tour 5, validé par nos données) : entrée UNIQUEMENT
    en session 08-17h UTC. La nuit = bruit.
  - Données fraîches obligatoires : si le dernier point de BTC a plus de
    FRAIS_MAX_AGE_MIN minutes → PAS d'entrée (et pas de décision de sortie
    non plus : on garde la position et on le signale).
  - Fail-open total : toute erreur de lecture → on ne fait RIEN (ni entrée ni
    sortie forcée), on l'écrit dans live.json.
  - Taille réduite : NOTIONAL_USDT = 5 (1/4 de la base 20$ de Hulk). C'est une
    ceinture de sécurité, pas un moteur de PnL.

ARCHIVAGE (audit complet)
-------------------------
  - runs/short_btc_state.json    : état persistant (position, capital, trades)
  - runs/short_btc_live.json     : état courant pour le cockpit (pont /shortbtc)
  - runs/short_btc_journal.csv   : journal des trades (comme le moteur)
  - runs/short_btc_signaux.jsonl : TOUS les signaux calculés (audit de la
    qualité du signal avant toute utilisation réelle)

PLANIFICATION : launchd com.ace777.short-btc (StartInterval 300s) — voir
docs/SPEC_SHORT_BTC_20260831.md pour le protocole de validation (3 jours de
stabilité avant toute idée de passage réel, comme le protocole divergence).

USAGE : python3 scripts/short_btc.py [--once]
        (sans --once : boucle toutes les LOOP_SEC secondes)
"""
from __future__ import annotations

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
SRC = RUNS / "croisement_contexte.jsonl"
STATE = RUNS / "short_btc_state.json"
LIVE = RUNS / "short_btc_live.json"
JOURNAL = RUNS / "short_btc_journal.csv"
SIGNAUX = RUNS / "short_btc_signaux.jsonl"

# ---- paramètres (modifiables, cohérents avec l'esprit du moteur) ----
NOTIONAL_USDT = 5.0        # taille d'un short (1/4 de la base 20$)
CAPITAL0 = 100.0           # capital virtuel de la ligne short (lisibilité %)
SCORE_ENTREE = 5           # score minimal pour ouvrir un short
SCORE_SORTIE = 2           # score sous lequel on coupe (signal éteint)
TP_PCT = 2.0               # take profit : BTC -2% depuis l'entrée
SL_PCT = 1.5               # stop loss : BTC +1.5% contre nous
TTL_H = 24.0               # time-out d'une position (heures)
SESSION_START_UTC, SESSION_END_UTC = 8, 17   # gating temporel (08-17h UTC)
FRAIS_MAX_AGE_MIN = 15.0   # données plus vieilles → pas de décision
LOOP_SEC = 300             # boucle (5 min ; le moteur écrit ~1 point/min)
PIC_SEUIL = 3.0            # seuil « pompe » pour la surchauffe instantanée (%)
FWD_H = 4                  # horizon du signal directionnel (protocole divergence)


def utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def now_h() -> int:
    return int(time.time()) // 3600


def load_rows() -> list[dict]:
    rows = []
    with open(SRC, encoding="utf-8") as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            try:
                rows.append(json.loads(l))
            except Exception:
                pass
    return rows


def hourly_m6(rows) -> dict[str, dict[int, float]]:
    """Série horaire (moyenne du m6_pct) par paire."""
    acc: dict[str, dict[int, list]] = {}
    for r in rows:
        p, ts, m6 = r.get("pair"), r.get("ts"), r.get("m6_pct")
        if p is None or ts is None or m6 is None:
            continue
        h = ts - (ts % 3600)
        acc.setdefault(p, {}).setdefault(h, []).append(float(m6))
    return {p: {h: sum(v) / len(v) for h, v in hv.items()} for p, hv in acc.items()}


def corr(xs: list[float], ys: list[float]):
    n = len(xs)
    if n < 5:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    return num / (dx * dy) if dx > 0 and dy > 0 else None


def dernier_point(rows, pair: str):
    """Dernier point (ts, prix, m6) de la paire."""
    best = None
    for r in rows:
        if r.get("pair") == pair:
            ts = r.get("ts")
            if best is None or ts > best[0]:
                best = (ts, r.get("price"), r.get("m6_pct"))
    return best


def calculer_signal(rows) -> dict:
    """Score composite + détails. Retourne aussi la fraîcheur des données."""
    out = {"ok": False, "detail": ""}
    if not rows:
        out["detail"] = "aucune donnée"
        return out
    last = dernier_point(rows, "BTCUSDT")
    if last is None:
        out["detail"] = "pas de point BTC"
        return out
    age_min = (time.time() - last[0]) / 60.0
    out["frais"] = age_min <= FRAIS_MAX_AGE_MIN
    out["age_min"] = round(age_min, 1)

    hb = hourly_m6(rows)
    hours = sorted(set().union(*[set(v.keys()) for v in hb.values()]))
    if "BTCUSDT" not in hb or len(hours) < 10:
        out["detail"] = "historique insuffisant"
        return out
    pan = {}
    for h in hours:
        vals = [hb[p][h] for p in hb if h in hb[p]]
        pan[h] = sum(vals) / len(vals) if vals else None

    # A. corr directionnelle BTC (protocole divergence, angle 3)
    xs, ys = [], []
    for h in hours:
        if h not in hb["BTCUSDT"] or pan.get(h) is None or pan.get(h + FWD_H * 3600) is None:
            continue
        xs.append(hb["BTCUSDT"][h])
        ys.append(pan[h + FWD_H * 3600] - pan[h])
    corr_dir_btc = corr(xs, ys) if len(xs) >= 5 else None
    score_a = 0
    if corr_dir_btc is not None:
        if corr_dir_btc <= -0.15:
            score_a = 3
        elif corr_dir_btc <= -0.10:
            score_a = 2
        elif corr_dir_btc <= -0.05:
            score_a = 1

    # B. surchauffe instantanée : % paires dont le DERNIER point (frais) a m6 > +PIC_SEUIL
    #    (plus réactif que le bucket horaire qui peut être à moitié vide)
    derniers_m6: dict[str, float] = {}
    for r in rows:
        p, m6 = r.get("pair"), r.get("m6_pct")
        if p and m6 is not None:
            ts = r.get("ts") or 0
            if p not in derniers_m6 or ts > derniers_m6[p][0]:
                derniers_m6[p] = (ts, float(m6))
    frais_ts = time.time() - FRAIS_MAX_AGE_MIN * 60
    pompes = [v for (ts, v) in derniers_m6.values() if ts >= frais_ts and v > PIC_SEUIL]
    total_frais = [v for (ts, v) in derniers_m6.values() if ts >= frais_ts]
    pct_pompe = 100.0 * len(pompes) / len(total_frais) if total_frais else 0.0
    if pct_pompe >= 60:
        score_b = 3
    elif pct_pompe >= 40:
        score_b = 2
    elif pct_pompe >= 25:
        score_b = 1
    else:
        score_b = 0

    # C. BTC en surchauffe (dernier m6 connu du dernier point BTC)
    m6_btc = last[2]
    m6_btc = float(m6_btc) if m6_btc is not None else 0.0
    score_c = 2 if m6_btc >= 2.0 else (1 if m6_btc >= 1.0 else 0)

    # D. momentum 24h BTC (prix now vs prix ~24h avant, depuis les points bruts)
    prix_now = last[1]
    cible = time.time() - 24 * 3600
    best_old = None
    for r in rows:
        if r.get("pair") == "BTCUSDT":
            ts = r.get("ts")
            if ts <= cible and (best_old is None or ts > best_old[0]):
                best_old = (ts, r.get("price"))
    move24 = 0.0
    if best_old and best_old[1]:
        move24 = 100.0 * (prix_now / best_old[1] - 1)
    score_d = 2 if move24 >= 3.0 else (1 if move24 >= 1.5 else 0)

    score = score_a + score_b + score_c + score_d
    hr = datetime.now(timezone.utc).hour
    session_ok = SESSION_START_UTC <= hr < SESSION_END_UTC

    out.update({
        "ok": True,
        "frais": age_min <= FRAIS_MAX_AGE_MIN,
        "score": score,
        "corr_dir_btc": round(corr_dir_btc, 3) if corr_dir_btc is not None else None,
        "pct_pompe": round(pct_pompe, 1),
        "m6_btc": round(m6_btc or 0, 2),
        "move24_btc": round(move24, 2),
        "session_ok": session_ok,
        "session_utc": hr,
        "prix_btc": prix_now,
        "ts_prix": last[0],
        "n_paires": len(hb),
        "detail": (f"score {score} = contexte {score_a} (corr_dir {corr_dir_btc and round(corr_dir_btc,2)}) "
                   f"+ surchauffe {score_b} ({pct_pompe:.0f}% paires >{PIC_SEUIL}%) "
                   f"+ btc {score_c} (m6 {m6_btc and round(m6_btc,2)}%) "
                   f"+ momentum {score_d} (24h {move24:+.2f}%)"),
    })
    return out


def charger_state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"capital": CAPITAL0, "pnl_total": 0.0, "n_trades": 0, "trades": [], "position": None}


def sauver_state(st: dict) -> None:
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")


def journaliser_trade(st: dict, trade: dict) -> None:
    st.setdefault("trades", []).append(trade)
    st["trades"] = st["trades"][-50:]  # garder les 50 derniers
    nouveau = not JOURNAL.exists()
    with open(JOURNAL, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nouveau:
            w.writerow(["ts_entree", "prix_entree", "ts_sortie", "prix_sortie",
                        "notional", "pnl_usd", "pnl_pct", "raison_sortie",
                        "score_entree", "detail_signal"])
        w.writerow([trade.get("ts_entree"), trade.get("prix_entree"),
                    trade.get("ts_sortie"), trade.get("prix_sortie"),
                    trade.get("notional"), round(trade.get("pnl_usd", 0), 4),
                    round(trade.get("pnl_pct", 0), 3), trade.get("raison_sortie"),
                    trade.get("score_entree"), trade.get("detail_signal")])


def gerer(sig: dict, st: dict) -> None:
    pos = st.get("position")
    prix = sig.get("prix_btc")
    frais = sig.get("frais", False)
    score = sig.get("score", 0)

    if pos:
        # ---- SORTIE ----
        entree = pos["prix_entree"]
        ts0 = pos["ts_entree_epoch"]
        raison = None
        if frais:
            if prix <= entree * (1 - TP_PCT / 100):
                raison = "TP"
            elif prix >= entree * (1 + SL_PCT / 100):
                raison = "SL"
            elif score < SCORE_SORTIE:
                raison = "SIGNAL_ETEINT"
            elif (time.time() - ts0) / 3600 >= TTL_H:
                raison = "TIME_OUT"
        if raison:
            pnl_usd = (entree - prix) / entree * pos["notional"]
            pnl_pct = 100.0 * (entree - prix) / entree
            trade = {
                "ts_entree": pos["ts_entree"], "prix_entree": entree,
                "ts_sortie": utc(), "prix_sortie": prix,
                "notional": pos["notional"], "pnl_usd": pnl_usd, "pnl_pct": pnl_pct,
                "raison_sortie": raison, "score_entree": pos.get("score_entree"),
                "detail_signal": pos.get("detail_signal"),
            }
            st["pnl_total"] = round(st.get("pnl_total", 0.0) + pnl_usd, 4)
            st["capital"] = round(st.get("capital", CAPITAL0) + pnl_usd, 4)
            st["n_trades"] = st.get("n_trades", 0) + 1
            st["position"] = None
            journaliser_trade(st, trade)
            print(f"[SHORT-BTC] SORTIE {raison} @ {prix} — pnl {pnl_usd:+.2f}$ ({pnl_pct:+.2f}%)")
        return

    # ---- ENTRÉE ----
    if score >= SCORE_ENTREE and frais and sig.get("session_ok"):
        st["position"] = {
            "ts_entree": utc(), "ts_entree_epoch": time.time(),
            "prix_entree": prix, "notional": NOTIONAL_USDT,
            "score_entree": score, "detail_signal": sig.get("detail"),
        }
        print(f"[SHORT-BTC] ENTRÉE short @ {prix} (score {score}) — {sig.get('detail')}")


def ecrire_live(sig: dict, st: dict) -> None:
    pos = st.get("position")
    live = {
        "ok": sig.get("ok", False),
        "ts": utc(),
        "frais": sig.get("frais", False),
        "signal": {k: sig.get(k) for k in (
            "score", "corr_dir_btc", "pct_pompe", "m6_btc", "move24_btc",
            "session_ok", "session_utc", "prix_btc", "detail")},
        "position": pos,
        "pnl_total": st.get("pnl_total", 0.0),
        "capital": st.get("capital", CAPITAL0),
        "n_trades": st.get("n_trades", 0),
        "dernieres_trades": st.get("trades", [])[-5:],
    }
    LIVE.write_text(json.dumps(live, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(SIGNAUX, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": utc(),
            "score": sig.get("score"),
            "corr_dir_btc": sig.get("corr_dir_btc"),
            "pct_pompe": sig.get("pct_pompe"),
            "m6_btc": sig.get("m6_btc"),
            "move24_btc": sig.get("move24_btc"),
            "session_ok": sig.get("session_ok"),
            "prix_btc": sig.get("prix_btc"),
            "frais": sig.get("frais"),
            "position": bool(pos),
        }, ensure_ascii=False) + "\n")


def run_once() -> int:
    try:
        rows = load_rows()
    except Exception as e:
        print(f"[SHORT-BTC] ERR lecture {SRC}: {e}")
        return 1
    sig = calculer_signal(rows)
    st = charger_state()
    gerer(sig, st)
    sauver_state(st)
    ecrire_live(sig, st)
    pos = st.get("position")
    print(f"[SHORT-BTC] score={sig.get('score')} frais={sig.get('frais')} "
          f"session={sig.get('session_ok')} position={'OUVERTE @ '+str(pos['prix_entree']) if pos else 'aucune'} "
          f"pnl_total={st.get('pnl_total'):+.2f}$")
    return 0


def main() -> int:
    if "--once" in sys.argv:
        return run_once()
    while True:
        try:
            run_once()
        except Exception as e:
            print(f"[SHORT-BTC] ERR {e}")
        time.sleep(LOOP_SEC)
    return 0


if __name__ == "__main__":
    sys.exit(main())
