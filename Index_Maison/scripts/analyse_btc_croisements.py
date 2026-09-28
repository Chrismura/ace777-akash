#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : analyse_btc_croisements.py
Projet       : ACE777 (analyse pattern BTC — croisements M50/M200 + RSI, GO Christophe 09/09)
Rôle         : 1) historique COMPLET paginé (MEXC, 2018+) de tous les golden/death crosses
               SMA50/SMA200 + rendements 30/90 j après chacun
               2) RSI(14) jour/semaine/mois, horizons RAMENÉS EN JOURS (30 j pour les
               trois échelles — fix du bug « 30 bougies mensuelles = 2,5 ans »)
               3) patterns COMBINÉS (état du cross × zone RSI mensuel), période de
               réchauffement des MM exclue (artefact)
               4) l'as : pattern « digestion » (pump 30 j > 20 % puis 7 j plat) —
               fréquence et suites historiques
               5) où en est BTC ce soir selon cette grammaire.
Stdlib pur. Sortie lisible + JSON. Ne trade pas (C3). Lecture seule.
"""
import json
import time
import urllib.request
from pathlib import Path

OUT_JSON = Path(__file__).resolve().parent.parent / "data" / "btc_pattern_analysis.json"
BASE = "https://api.mexc.com/api/v3/klines?symbol=BTCUSDT"
WARMUP = 200  # jours exclus du début (MM200 pas encore significative)


def fetch_one(interval, limit, end_time=None):
    url = f"{BASE}&interval={interval}&limit={limit}"
    if end_time:
        url += f"&endTime={end_time}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                return json.load(r)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1.5 * (attempt + 1))


QUIRK_MEXC = True  # startTime OU endTime seuls sont ignorés → il faut les DEUX bornes
JOUR_MS = 86_400_000


def fetch_pagine(interval, cible_min_ts, limit=500):
    """Page en arrière par fenêtres BORNÉES (startTime+endTime) — quirk MEXC :
    une seule borne est ignorée, l'API renvoie alors les plus récentes."""
    tout = []
    fin = None  # None = maintenant
    while True:
        if fin is None:
            lot = fetch_one(interval, limit, None)
        else:
            debut = fin - limit * JOUR_MS  # fenêtre assez large pour remplir
            lot = fetch_two_bounds(interval, debut, fin, limit)
        if not lot:
            break
        tout = lot + tout
        premier = int(lot[0][0]) // 1000
        if premier <= cible_min_ts:
            break
        fin = premier * 1000 - 1
        time.sleep(0.3)
    vu, propre = set(), []
    for r in tout:
        k = int(r[0])
        if k not in vu:
            vu.add(k)
            propre.append(r)
    return propre


def fetch_two_bounds(interval, start_ms, end_ms, limit):
    url = f"{BASE}&interval={interval}&limit={limit}&startTime={start_ms}&endTime={end_ms}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                return json.load(r)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1.5 * (attempt + 1))
    # dédoublonner par open-time
    vu, propre = set(), []
    for r in tout:
        k = int(r[0])
        if k not in vu:
            vu.add(k)
            propre.append(r)
    return propre


def fetch(interval, limit):
    return fetch_one(interval, limit)


def sma(closes, n, i):
    if i + 1 < n:
        return None
    return sum(closes[i - n + 1:i + 1]) / n


def rsi_series(closes, n=14):
    if len(closes) < n + 1:
        return [None] * len(closes)
    gains, losses = [], []
    for i in range(1, len(closes)):
        d = closes[i] - closes[i - 1]
        gains.append(max(0.0, d))
        losses.append(max(0.0, -d))
    ag = sum(gains[:n]) / n
    al = sum(losses[:n]) / n
    out = [None] * n + [100.0 if al == 0 else 100 - 100 / (1 + ag / al)]
    for i in range(n + 1, len(closes)):
        ag = (ag * (n - 1) + gains[i - 1]) / n
        al = (al * (n - 1) + losses[i - 1]) / n
        out.append(100.0 if al == 0 else 100 - 100 / (1 + ag / al))
    return out


def rendement(closes, i, horizon):
    j = i + horizon
    if j >= len(closes):
        return None
    return (closes[j] / closes[i] - 1) * 100.0


def fmt(x):
    return "—" if x is None else f"{x:+.1f}%"


def stats(liste):
    vals = sorted(v for v in liste if v is not None)
    if not vals:
        return "—"
    med = vals[len(vals) // 2]
    return f"médiane {med:+.1f}% (min {vals[0]:+.1f} / max {vals[-1]:+.1f} · {len(vals)} cas)"


def max_dd(closes, i, horizon):
    """Pire drawdown dans les `horizon` jours après i (0 = jamais négatif)."""
    fin = min(i + horizon, len(closes) - 1)
    pic = closes[i]
    pire = 0.0
    for j in range(i + 1, fin + 1):
        pic = max(pic, closes[j])
        pire = min(pire, (closes[j] / pic - 1) * 100.0)
    return pire


def main():
    # ---------- 1. DAILY paginé : tous les croisements ----------
    annee_2017 = int(time.mktime(time.strptime("2017-01-01", "%Y-%m-%d")))
    k = fetch_pagine("1d", annee_2017)
    t = [int(r[0]) // 1000 for r in k]
    c = [float(r[4]) for r in k]
    dates = [time.strftime("%d/%m/%y", time.gmtime(x)) for x in t]
    n = len(c)
    m50 = [sma(c, 50, i) for i in range(n)]
    m200 = [sma(c, 200, i) for i in range(n)]

    cross_age = [None] * n
    dernier = None
    for i in range(n):
        if m50[i] is not None and m200[i] is not None and i >= WARMUP:
            etat = "GC" if m50[i] > m200[i] else "DC"
            if dernier is None or etat != dernier[0]:
                dernier = (etat, i)
        cross_age[i] = (dernier[0], i - dernier[1]) if dernier else None

    print("═" * 74)
    print("1 · LES CROISEMENTS SMA50/SMA200 — HISTORIQUE PAGINÉ MEXC")
    print("═" * 74)
    print(f"historique daily : {dates[0]} → {dates[-1]} ({n} jours · réchauffement MM exclu : {WARMUP} j)")
    evenements = []
    for i in range(1, n):
        if m50[i] and m200[i] and m50[i - 1] and m200[i - 1] and i >= WARMUP:
            etat_prec = "GC" if m50[i - 1] > m200[i - 1] else "DC"
            etat = "GC" if m50[i] > m200[i] else "DC"
            if etat != etat_prec:
                r30 = rendement(c, i, 30)
                r90 = rendement(c, i, 90)
                evenements.append({"date": dates[i], "type": etat, "i": i, "r30": r30, "r90": r90})
                print(f"  {dates[i]}  {'GOLDEN cross' if etat == 'GC' else 'DEATH  cross'}"
                      f"   30j {fmt(r30)} · 90j {fmt(r90)}")
    for typ in ("GC", "DC"):
        r30 = [e["r30"] for e in evenements if e["type"] == typ]
        r90 = [e["r90"] for e in evenements if e["type"] == typ]
        nom = "GOLDEN" if typ == "GC" else "DEATH "
        print(f"  {nom} cross → 30j : {stats(r30)}")
        print(f"  {nom} cross → 90j : {stats(r90)}")

    # ---------- 2. RSI jour / semaine / mois — horizons EN JOURS ----------
    print("═" * 74)
    print("2 · RSI(14) — JOUR / SEMAINE / MOIS (horizon futur : 30 JOURS pour les trois)")
    print("═" * 74)
    kw = fetch("1W", 500)
    km = fetch("1M", 500)
    cw = [float(r[4]) for r in kw]
    cm = [float(r[4]) for r in km]
    rj = rsi_series(c)
    rw = rsi_series(cw)
    rm = rsi_series(cm)
    print(f"  RSI jour : {rj[-1]:.1f} · semaine : {rw[-1]:.1f} · mois : {rm[-1]:.1f}")
    print(f"  (bougies disponibles — mois : {len(cm)}, semaine : {len(cw)})")

    def zone(r):
        return "<30" if r < 30 else "30-50" if r < 50 else "50-70" if r < 70 else ">70"

    def zones_rsi(rs, pas_jours, label):
        """pas_jours = jours de futur par bougie (1d→30, 1W→28, 1M→30)."""
        hb = max(1, round(30 / pas_jours))  # ~30 jours de futur
        b = {"<30": [], "30-50": [], "50-70": [], ">70": []}
        for i, r in enumerate(rs):
            if r is None:
                continue
            rr = rendement(cm if pas_jours == 30 else cw if pas_jours == 28 else c, i, hb) \
                if pas_jours != 30 else None
            if pas_jours == 30:
                rr = rendement(cm, i, hb)  # 1 bougie mensuelle ≈ 30 j
            if rr is None:
                continue
            b[zone(r)].append(rr)
        print(f"  Rendements ~30j après chaque bougie {label} (≈{hb} bougie(s)) :")
        for z in ["<30", "30-50", "50-70", ">70"]:
            print(f"    RSI {z:>5} : {stats(b[z])}")

    zones_rsi(rm, 30, "MOIS")
    zones_rsi(rw, 28, "SEMAINE")
    zones_rsi(rj, 1, "JOUR")

    # ---------- 3. Pattern combiné cross × RSI mensuel (hors réchauffement) ----------
    print("═" * 74)
    print("3 · PATTERN COMBINÉ (état du cross × zone RSI du mois) — artefact exclu")
    print("═" * 74)
    tm = [int(r[0]) // 1000 for r in km]

    def rsi_mensuel_a(ts_d):
        for j in range(len(tm) - 2, -1, -1):
            if tm[j] <= ts_d:
                return rm[j]
        return None

    buckets = {}
    for i in range(WARMUP, n):
        ca = cross_age[i]
        r = rsi_mensuel_a(t[i])
        if ca is None or r is None:
            continue
        buckets.setdefault((ca[0], zone(r)), []).append(
            (rendement(c, i, 30), rendement(c, i, 90)))
    print(f"  {'config':<18}{'n jours':>8}{'r30 méd':>9}{'r90 méd':>9}{'r90 min':>9}")
    for cle in sorted(buckets, key=lambda x: (x[0], x[1])):
        v = buckets[cle]
        r30s = sorted(x[0] for x in v if x[0] is not None)
        r90s = sorted(x[1] for x in v if x[1] is not None)
        med30 = f"{r30s[len(r30s)//2]:+.1f}%" if r30s else "—"
        med90 = f"{r90s[len(r90s)//2]:+.1f}%" if r90s else "—"
        min90 = f"{r90s[0]:+.1f}%" if r90s else "—"
        label = ("GOLDEN" if cle[0] == "GC" else "DEATH") + " + RSI " + cle[1]
        print(f"  {label:<18}{len(v):>8}{med30:>9}{med90:>9}{min90:>9}")

    # ---------- 4. L'as : pattern DIGESTION (pump 30j > 20% puis 7j plat) ----------
    print("═" * 74)
    print("4 · L'AS — PATTERN « DIGESTION » : pump 30 j > +20 % PUIS 7 j plat (< ±3 %)")
    print("═" * 74)
    episodes = []
    en_episode = False
    for i in range(WARMUP + 30, n - 90):
        r30 = (c[i] / c[i - 30] - 1) * 100.0
        r7 = (c[i] / c[i - 7] - 1) * 100.0
        ok = r30 > 20.0 and abs(r7) < 3.0
        if ok and not en_episode:
            en_episode = True
            episodes.append({"date": dates[i], "i": i,
                             "rsi_m": rsi_mensuel_a(t[i]),
                             "r30_fwd": rendement(c, i, 30),
                             "r90_fwd": rendement(c, i, 90),
                             "dd30_fwd": max_dd(c, i, 30)})
        elif not ok:
            en_episode = False
    print(f"  épisodes détectés ({dates[0]} → {dates[-1]}) : {len(episodes)}")
    for e in episodes:
        rm_s = f"{e['rsi_m']:.0f}" if e.get("rsi_m") is not None else "—"
        print(f"   · {e['date']}  RSI mois {rm_s:>3} → +30j {fmt(e['r30_fwd'])} · +90j {fmt(e['r90_fwd'])}"
              f" · pire dd 30j {e['dd30_fwd']:+.1f}%")
    if episodes:
        print(f"  +30j : {stats([e['r30_fwd'] for e in episodes])}")
        print(f"  +90j : {stats([e['r90_fwd'] for e in episodes])}")
        print(f"  pire drawdown 30j : {stats([e['dd30_fwd'] for e in episodes])}")
        # FILTRE DU JUGE : les digestions ratées ont-elles un RSI mensuel reconnaissable ?
        pour = [(e["rsi_m"], e["r90_fwd"]) for e in episodes
                if e.get("rsi_m") is not None and e["r90_fwd"] is not None]
        if len(pour) >= 8:
            bas = sorted(r for rsi, r in pour if rsi < 55)
            haut = sorted(r for rsi, r in pour if rsi >= 55)
            print(f"  FILTRE RSI mensuel au moment de la digestion (sépare continuation / sommet) :")
            print(f"    RSI < 55 : {stats(bas)}  ({len(bas)} cas)")
            print(f"    RSI ≥ 55 : {stats(haut)}  ({len(haut)} cas)")

    # ---------- 5. Aujourd'hui ----------
    print("═" * 74)
    print("5 · OÙ EN EST BTC CE SOIR ?")
    print("═" * 74)
    ca = cross_age[-1]
    etat, age = ca if ca else ("?", 0)
    nb_gc = sum(1 for e in evenements if e["type"] == "GC")
    nb_dc = sum(1 for e in evenements if e["type"] == "DC")
    r30 = (c[-1] / c[-31] - 1) * 100.0
    r7 = (c[-1] / c[-8] - 1) * 100.0
    dig = r30 > 20.0 and abs(r7) < 3.0
    print(f"  cross : {'GOLDEN' if etat == 'GC' else 'DEATH'} depuis {age} j"
          f" · historique complet : {nb_gc} golden / {nb_dc} death")
    print(f"  RSI jour {rj[-1]:.1f} · semaine {rw[-1]:.1f} · mois {rm[-1]:.1f}")
    print(f"  pump30 {r30:+.1f}% · 7j {r7:+.1f}% → pattern digestion : {'OUI' if dig else 'non'}")
    cle = (etat, zone(rm[-1]) if rm[-1] is not None else "?")
    hist = buckets.get(cle, [])
    if hist:
        r90s = sorted(x[1] for x in hist if x[1] is not None)
        print(f"  config historique ({len(hist)} j) : rendement 90j médian {r90s[len(r90s)//2]:+.1f}%"
              f" (pire {r90s[0]:+.1f}%)")
    else:
        print("  configuration sans précédent dans l'historique disponible")

    out = {
        "ts": int(time.time()),
        "per": {"debut": dates[0], "fin": dates[-1], "n_jours": n, "warmup_exclu": WARMUP},
        "crosses": evenements,
        "rsi": {"jour": round(rj[-1], 1), "semaine": round(rw[-1], 1), "mois": round(rm[-1], 1)},
        "etat_cross": {"type": etat, "age_jours": age},
        "digestion": {"aujourdhui": dig, "n_episodes": len(episodes),
                      "episodes": episodes[-8:]},
        "buckets_combines": {"|".join(k2): len(v) for k2, v in buckets.items()},
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nsauvé : {OUT_JSON.name}")


if __name__ == "__main__":
    main()
