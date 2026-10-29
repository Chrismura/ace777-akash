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
  - 29/10 (GO Christophe, R17 : jamais de fixe) : entrées 24/7. L'ancien ban nuit
    est FALSIFIÉ par nos données (mesure_gate_nuit_shorts.py : nuit 53,5 %/-0,407 %,
    n=2920 vs jour 64,9 %/-0,782 %, n=1318). La nuit paie moins → taille réduite
    (NUIT_NOTIONNEL_MULT = 0,5, ratio mesuré), jamais d'interdiction.
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
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# === SYMBOLE PARAMÉTRÉ (28/10/2026, §47 GO tous les shorts) ===
# SHORT_SYMBOL=BTCUSDT (défaut : fichiers legacy et décisions inchangés)
# | ETHUSDT | XRPUSDT... — même signal, même garde-fous, fichiers suffixés.
# Zéro effet sur BTC : SYM=BTCUSDT reproduit l'exact comportement d'avant.
SYM = os.environ.get("SHORT_SYMBOL", "BTCUSDT").strip().upper() or "BTCUSDT"
SYM_TAG = "btc" if SYM == "BTCUSDT" else SYM.replace("USDT", "").lower()
_NOM = "btc" if SYM == "BTCUSDT" else SYM_TAG
_PREFIX = f"[SHORT-{SYM_TAG.upper()}]"
ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
SRC = RUNS / "croisement_contexte.jsonl"
STATE = RUNS / f"short_{SYM_TAG}_state.json"
LIVE = RUNS / f"short_{SYM_TAG}_live.json"
JOURNAL = RUNS / f"short_{SYM_TAG}_journal.csv"
SIGNAUX = RUNS / f"short_{SYM_TAG}_signaux.jsonl"

# ---- paramètres (modifiables, cohérents avec l'esprit du moteur) ----
NOTIONAL_USDT = 5.0        # marge isolée du short (le notionnel vient du DYN ci-dessous)
# === NOTIONNEL DYNAMIQUE 10 % INVENTAIRE (21/10/2026, GO Christophe « go ») ===
# Mesuré (chiffrage_go_short_1030.py, 12 846 signaux) : entrées corr ≤ −0,50,
# n=17, esp +0,243 %, même signe h1/h2, 0 liquidation à 8,6× (dist 11,23 % >> SL).
# Marge ISOLÉE 5 $ (le short meurt seul) ; notionnel = 10 % du total mission
# (cash + bagValue), plafonné à 10× la marge (50 $). Réversible : SHORT_BTC_DYN=0
# (retombe sur NOTIONAL_USDT fixe 5 $). Marge croisée sur alts : NON (crash corr 1).
DYN_ON = os.environ.get("SHORT_BTC_DYN", "1").strip() not in ("0", "false", "False")
DYN_PCT = float(os.environ.get("SHORT_BTC_NOTIONAL_PCT", "0.10"))
DYN_LEV_MAX = float(os.environ.get("SHORT_BTC_LEV_MAX", "10"))
CAPITAL0 = 100.0           # capital virtuel de la ligne short (lisibilité %)
SCORE_ENTREE = 5           # score minimal pour ouvrir un short
SCORE_SORTIE = 2           # score sous lequel on coupe (signal éteint)
# === SIGNAL CORRIGÉ (08/10/2026, GO Christophe — MESURÉ AVANT CÂBLAGE) ===
# Mesure longue (chiffrage_short_btc_signal_long.py, 38 j de signaux réels) : le score
# ACTUEL n'a AUCUN edge (espérance −0,034 %, signe instable) car ses composants
# `surchauffe` et `btc m6` prédisent à l'envers. Seul `corr_dir_btc` tient : entrer
# quand corr_dir ≤ −0,50 donne +0,319 % d'espérance, 58 % de réussite, MÊME SIGNE sur
# les 2 moitiés. On câble donc ce seuil, SANS levier (le levier attend une preuve
# d'edge positive confirmée). Réversible : SHORT_BTC_SIGNAL=score (ancien comportement).
SIGNAL_MODE = os.environ.get("SHORT_BTC_SIGNAL", "corr").strip().lower()
CORR_ENTREE = float(os.environ.get("SHORT_BTC_CORR_ENTREE", "-0.50"))
CORR_SORTIE = float(os.environ.get("SHORT_BTC_CORR_SORTIE", "-0.10"))
TP_PCT = 2.0               # take profit : BTC -2% depuis l'entrée
SL_PCT = 1.5               # stop loss : BTC +1.5% contre nous
# === SL ADAPTATIF (16/10/2026, GO short — MESURÉ AVANT CÂBLAGE) ===
# Mesure (chiffrage_short_sl_adapt, 39 trades rejoués, mêmes entrées) : SL fixe
# 1,5 % = -0,096 $ · SL 0,5×amp7 = -0,082 (neutre, NON câblé) · SL 0,5×range24h =
# +0,064, MÊME SIGNE sur les 2 moitiés (h1 +0,205 vs +0,185 · h2 -0,141 vs -0,282).
# Le range 24 h est à l'horizon du trade (TTL 24 h) et se calcule du flux existant
# (croisement_contexte, ~30 h de points bruts — aucune nouvelle dépendance).
# Ne s'applique qu'aux NOUVELLES positions (sl_pct stocké à l'entrée ; l'ouverte
# garde son fixe). Filtre creux 24 h REJETÉ (-0,22, tue les TP) ; creux 7 j non
# calculable en live (flux 30 h) — non câblé ; dormeurs TIME_OUT +0,18 (gardés).
# Réversible : SHORT_BTC_SL_ADAPT=0 (fixe 1,5 % strict).
SL_ADAPT_ON = os.environ.get("SHORT_BTC_SL_ADAPT", "1").strip() not in ("0", "false", "False")
SL_ADAPT_FRAC = float(os.environ.get("SHORT_BTC_SL_ADAPT_FRAC", "0.5"))
TTL_H = 24.0               # time-out d'une position (heures)
SESSION_START_UTC, SESSION_END_UTC = 8, 17   # repère JOUR/NUIT (08-17h UTC) — 29/10 :
# ce n'est PLUS un ban (le ban nuit est MORT, falsifié : nuit 53,5 %/-0,407 % n=2920).
# Jour/nuit ne fait que MODULER la taille (NUIT_NOTIONNEL_MULT, ratio mesuré).
NUIT_NOTIONNEL_MULT = float(os.environ.get("SHORT_NUIT_MULT", "0.5"))
# 0,5 = ratio des médianes +24h mesuré (nuit -0,407 / jour -0,782 ≈ 0,52, arrondi
# déclaré) sur 4 238 signaux d'entrée BTC (mesure_gate_nuit_shorts.py, 29/10).
# La taille suit l'edge mesuré, jamais une horloge. Réversible : SHORT_NUIT_MULT=1.
FRAIS_MAX_AGE_MIN = 15.0   # données plus vieilles → pas de décision
LOOP_SEC = 300             # boucle (5 min ; le moteur écrit ~1 point/min)
PIC_SEUIL = 3.0            # seuil « pompe » pour la surchauffe instantanée (%)
FWD_H = 4                  # horizon du signal directionnel (protocole divergence)


def utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def now_h() -> int:
    return int(time.time()) // 3600


def _iter_lignes(path: str):
    import gzip as _gzip
    opener = _gzip.open if path.endswith(".gz") else open
    try:
        with opener(path, "rt", encoding="utf-8", errors="ignore") as f:
            for l in f:
                l = l.strip()
                if l:
                    yield l
    except FileNotFoundError:
        return


def load_rows(max_span_h: float = 30.0, max_rows: int = 120000) -> list[dict]:
    # BOUCLER LA BOUCLE (28/10 §48) : le live seul ne couvre que ~5 h (rotation)
    # → « historique insuffisant » permanent. On lit le live PUIS les archives
    # les plus récentes d'abord, et on s'arrête dès que le span couvre
    # max_span_h (30 h >> besoin 24 h range + 10 h corr). FIX 29/10 mémoire :
    # l'ancienne version lisait TOUT (live 56 Mo + 210 Mo décompressés ≈ 400 k
    # lignes ≈ 200 Mo/processus × 3 jobs //5 min → swap + freeze MacBook 8 Go).
    # Plafond max_rows : on garde les plus récents (tri ts décroissant).
    import glob as _glob
    import os as _os
    archives = _glob.glob(str(RUNS / "croisement_contexte.jsonl.*.gz"))
    # plus récentes d'abord (mtime décroissant) pour stop précoce
    try:
        archives.sort(key=lambda p: _os.path.getmtime(p), reverse=True)
    except Exception:
        archives = sorted(archives, reverse=True)
    rows: list[dict] = []
    t_min: float | None = None
    t_max: float | None = None

    def _span_ok() -> bool:
        return (t_min is not None and t_max is not None
                and (t_max - t_min) >= max_span_h * 3600)

    for path in [str(SRC)] + archives:
        for l in _iter_lignes(path):
            try:
                r = json.loads(l)
            except Exception:
                continue
            rows.append(r)
            try:
                ts = float(r.get("ts") or 0)
            except (TypeError, ValueError):
                continue
            if ts > 0:
                t_min = ts if t_min is None or ts < t_min else t_min
                t_max = ts if t_max is None or ts > t_max else t_max
        if _span_ok():
            break
    if len(rows) > max_rows:
        # garder les plus récents (ts=0 en dernier)
        try:
            rows.sort(key=lambda r: float(r.get("ts") or 0))
        except Exception:
            pass
        rows = rows[-max_rows:]
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


def range24_btc(rows):
    """Range % BTC sur les dernières 24 h de points bruts + couverture (heures).
    (None, span) si <12 h de données → l'appelant dégrade vers le SL fixe (règle #8)."""
    now = time.time()
    px, t0 = [], None
    for r in rows:
        if r.get("pair") != SYM:
            continue
        try:
            ts, px_ = float(r.get("ts") or 0), float(r.get("price"))
        except (TypeError, ValueError):
            continue
        if now - ts <= 24 * 3600:
            px.append(px_)
            t0 = ts if t0 is None or ts < t0 else t0
    if not px or min(px) <= 0:
        return None, 0.0
    span_h = (now - t0) / 3600
    if span_h < 12:
        return None, round(span_h, 1)
    return round((max(px) - min(px)) / min(px) * 100.0, 3), round(span_h, 1)


def calculer_signal(rows) -> dict:
    """Score composite + détails. Retourne aussi la fraîcheur des données."""
    out = {"ok": False, "detail": ""}
    if not rows:
        out["detail"] = "aucune donnée"
        return out
    last = dernier_point(rows, SYM)
    if last is None:
        out["detail"] = f"pas de point {SYM}"
        return out
    age_min = (time.time() - last[0]) / 60.0
    out["frais"] = age_min <= FRAIS_MAX_AGE_MIN
    out["age_min"] = round(age_min, 1)
    # FIX 11/09 (crash-loop None<=float) : exposer le PRIX BRUT du dernier point
    # BTC dès qu'il existe, même si le score est incomplet (ok=False après
    # rotation du JSONL). Ce n'est PAS un prix inventé : c'est le dernier prix
    # observé. ok/score restent incomplets → aucune ENTRÉE ni SIGNAL_ETEINT,
    # mais les sorties horaires (TIME_OUT) et TP/SL sur données fraîches restent
    # décidables au lieu de crasher sur None<=float à chaque cycle.
    out["prix_btc"] = last[1]

    hb = hourly_m6(rows)
    hours = sorted(set().union(*[set(v.keys()) for v in hb.values()]))
    if SYM not in hb or len(hours) < 10:
        out["detail"] = "historique insuffisant"
        return out
    pan = {}
    for h in hours:
        vals = [hb[p][h] for p in hb if h in hb[p]]
        pan[h] = sum(vals) / len(vals) if vals else None

    # A. corr directionnelle BTC (protocole divergence, angle 3)
    xs, ys = [], []
    for h in hours:
        if h not in hb[SYM] or pan.get(h) is None or pan.get(h + FWD_H * 3600) is None:
            continue
        xs.append(hb[SYM][h])
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
        if r.get("pair") == SYM:
            ts = r.get("ts")
            if ts <= cible and (best_old is None or ts > best_old[0]):
                best_old = (ts, r.get("price"))
    move24 = 0.0
    if best_old and best_old[1]:
        move24 = 100.0 * (prix_now / best_old[1] - 1)
    score_d = 2 if move24 >= 3.0 else (1 if move24 >= 1.5 else 0)

    _r24, _r24_span = range24_btc(rows)

    score = score_a + score_b + score_c + score_d
    hr = datetime.now(timezone.utc).hour
    session_ok = SESSION_START_UTC <= hr < SESSION_END_UTC

    out.update({
        "ok": True,
        "frais": age_min <= FRAIS_MAX_AGE_MIN,
        "score": score,
        "corr_dir_btc": round(corr_dir_btc, 3) if corr_dir_btc is not None else None,
        "corr_dir": round(corr_dir_btc, 3) if corr_dir_btc is not None else None,
        "pct_pompe": round(pct_pompe, 1),
        "m6_btc": round(m6_btc or 0, 2),
        "m6": round(m6_btc or 0, 2),
        "move24_btc": round(move24, 2),
        "move24": round(move24, 2),
        "range24_btc": _r24,
        "range24": _r24,
        "session_ok": session_ok,
        "session_utc": hr,
        "prix_btc": prix_now,
        "prix": prix_now,
        "ts_prix": last[0],
        "n_paires": len(hb),
        "detail": (f"score {score} = contexte {score_a} (corr_dir {corr_dir_btc and round(corr_dir_btc,2)}) "
                   f"+ surchauffe {score_b} ({pct_pompe:.0f}% paires >{PIC_SEUIL}%) "
                   f"+ {_NOM} {score_c} (m6 {m6_btc and round(m6_btc,2)}%) "
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


def notionnel_dynamique() -> float:
    """Notionnel 10 % inventaire sur marge isolée 5 $ (21/10 GO). Fail-open :
    mission illisible → NOTIONAL_USDT fixe. Plafond DYN_LEV_MAX × marge."""
    if not DYN_ON:
        return NOTIONAL_USDT
    try:
        mission = ROOT.parent / "Index_Maison" / "cockpit" / "mission.json"
        h = (json.loads(mission.read_text(encoding="utf-8")) or {}).get("hulk", {}) or {}
        total = float(h.get("cash") or 0) + sum(
            float(p.get("bagValue") or 0) for p in (h.get("positions") or []))
        if total <= 0:
            return NOTIONAL_USDT
        cible = DYN_PCT * total
        return round(max(NOTIONAL_USDT, min(cible, DYN_LEV_MAX * NOTIONAL_USDT)), 2)
    except Exception:
        return NOTIONAL_USDT


def gerer(sig: dict, st: dict) -> None:
    pos = st.get("position")
    prix = sig.get("prix_btc", sig.get("prix"))
    frais = sig.get("frais", False)
    score = sig.get("score", 0)
    corr = sig.get("corr_dir_btc")

    if pos:
        # ---- SORTIE ----
        entree = pos["prix_entree"]
        ts0 = pos["ts_entree_epoch"]
        # SL porté par la position (nouvelles) ; les anciennes (sans clé) gardent le
        # fixe 1,5 % — jamais de changement de règle en vol (organisme : on n'opère
        # pas un trade ouvert).
        _sl_use = float(pos.get("sl_pct", SL_PCT))
        raison = None
        # FIX 11/09 (crash-loop None<=float, défense en profondeur) : prix None
        # (aucun point BTC du tout) → aucune décision basée prix. Le TIME_OUT
        # reste possible sans prix (sortie horaire, ne dépend PAS de prix).
        # Cas nominal post-rotation : prix_btc = dernier prix BRUT observé
        # (exposé par calculer_signal même si ok=False) → TP/SL restent vivants.
        prix_ok = isinstance(prix, (int, float))
        if not prix_ok:
            if (time.time() - ts0) / 3600 >= TTL_H:
                raison = "TIME_OUT"
        elif frais:
            if prix <= entree * (1 - TP_PCT / 100):
                raison = "TP"
            elif prix >= entree * (1 + _sl_use / 100):
                raison = "SL"
            elif (SIGNAL_MODE == "corr" and corr is not None and corr > CORR_SORTIE) \
                    or (SIGNAL_MODE != "corr" and score is not None and score < SCORE_SORTIE):
                raison = "SIGNAL_ETEINT"
            elif (time.time() - ts0) / 3600 >= TTL_H:
                raison = "TIME_OUT"
        if raison:
            # FIX 11/09 : sortie TIME_OUT sans prix exploitable → réglée au prix
            # d'entrée (pnl 0, honnête : aucun prix inventé, sortie comptable).
            prix_sortie = prix if prix_ok else entree
            pnl_usd = (entree - prix_sortie) / entree * pos["notional"]
            pnl_pct = 100.0 * (entree - prix_sortie) / entree
            trade = {
                "ts_entree": pos["ts_entree"], "prix_entree": entree,
                "ts_sortie": utc(), "prix_sortie": prix_sortie,
                "notional": pos["notional"], "pnl_usd": pnl_usd, "pnl_pct": pnl_pct,
                "raison_sortie": raison, "score_entree": pos.get("score_entree"),
                "detail_signal": pos.get("detail_signal"),
            }
            st["pnl_total"] = round(st.get("pnl_total", 0.0) + pnl_usd, 4)
            st["capital"] = round(st.get("capital", CAPITAL0) + pnl_usd, 4)
            st["n_trades"] = st.get("n_trades", 0) + 1
            st["position"] = None
            journaliser_trade(st, trade)
            print(f"{_PREFIX} SORTIE {raison} @ {prix_sortie} — pnl {pnl_usd:+.2f}$ ({pnl_pct:+.2f}%)")
        return

    # ---- ENTRÉE ----
    # FIX 11/09 : entrée EXIGE un prix exploitable + signal complet (ok=True,
    # sinon score incomplet après rotation). score>=5 avec ok=False est impossible
    # (score=None) mais le garde reste explicite.
    if SIGNAL_MODE == "corr":
        entree_ok = (corr is not None and corr <= CORR_ENTREE)
        motif = f"corr_dir {corr} ≤ {CORR_ENTREE}"
    else:
        entree_ok = (score is not None and score >= SCORE_ENTREE)
        motif = f"score {score} ≥ {SCORE_ENTREE}"
    # 29/10 (GO Christophe) : entrées 24/7 — le ban nuit est tué (R17 : jamais de
    # fixe). session_ok reste LOGGÉ (mesure, scorer) mais ne bloque PLUS rien.
    if prix is not None and sig.get("ok") and entree_ok and frais:
        _r24e = sig.get("range24_btc")
        if SL_ADAPT_ON and isinstance(_r24e, (int, float)):
            _sl_entry = round(SL_ADAPT_FRAC * _r24e, 3)
            _sl_src = f"adaptatif 0,5×range24 {_r24e:.2f} %"
        else:
            _sl_entry = SL_PCT
            _sl_src = "fixe 1,5 % (range24 indisponible ou OFF)"
        _notionnel = notionnel_dynamique()
        _session_jour = bool(sig.get("session_ok"))
        if not _session_jour:
            _notionnel = round(_notionnel * NUIT_NOTIONNEL_MULT, 2)
        st["position"] = {
            "session_jour": _session_jour,
            "ts_entree": utc(), "ts_entree_epoch": time.time(),
            "prix_entree": prix, "notional": _notionnel,
            "score_entree": score, "corr_entree": corr,
            "sl_pct": _sl_entry,
            "detail_signal": sig.get("detail"),
        }
        print(f"{_PREFIX} ENTRÉE short @ {prix} ({motif}, SL {_sl_src} = {_sl_entry} %) — {sig.get('detail')}")


def ecrire_live(sig: dict, st: dict) -> None:
    pos = st.get("position")
    live = {
        "ok": sig.get("ok", False),
        "ts": utc(),
        "frais": sig.get("frais", False),
        "signal": {k: sig.get(k) for k in (
            "score", "corr_dir_btc", "corr_dir", "pct_pompe", "m6_btc", "m6",
            "move24_btc", "move24", "session_ok", "session_utc", "prix_btc",
            "prix", "range24_btc", "range24", "detail")},
        "sym": SYM,
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
            "sym": SYM,
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
        print(f"{_PREFIX} ERR lecture {SRC}: {e}")
        return 1
    sig = calculer_signal(rows)
    st = charger_state()
    gerer(sig, st)
    sauver_state(st)
    ecrire_live(sig, st)
    pos = st.get("position")
    print(f"{_PREFIX} score={sig.get('score')} frais={sig.get('frais')} "
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
            print(f"{_PREFIX} ERR {e}")
        time.sleep(LOOP_SEC)
    return 0


if __name__ == "__main__":
    sys.exit(main())
