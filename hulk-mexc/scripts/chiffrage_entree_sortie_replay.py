#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE ENTREE/SORTIE — REPLAY SUR LE LOG DU MOTEUR (21/09/2026, Buffy)
=========================================================================
GO Christophe 21/09 : « comment as-tu fait le set-up d'EDEL sans savoir ça ? ça touche
l'amplitude et le compounding, nos deux leviers principaux. Refais tous les calculs. »

  GO 1 — l'ENTRÉE : chiffrer une entrée SANS repli en régime IMPULSE
                    (aujourd'hui : `impulse_entry = max(dip, 5 %, 0,30 × move6)` —
                     un pump en ligne droite ne remplit jamais cette condition :
                     IMPULSE_WAIT = « le pump est là, on attend le repli »).
  GO 2 — la SORTIE : chiffrer une sortie qui ne liquide PAS le seed sous un multiple
                     (aujourd'hui : rip 50 % à +rip_pct, puis stop dur à −stop_pct,
                     puis trailing arm/giveback — le seed d'EDEL est mort à son 1er double).

POURQUOI CE REPLAY EST LE BON
  On ne réinvente pas les entrées : on rejoue les DÉCISIONS du moteur sur SES PROPRES
  données. Le log continu (runs/croisement_contexte.jsonl + les archives de rotation)
  porte, à chaque cycle, le PRIX, le RÉGIME, m6 et dd15 de chaque paire — c'est-à-dire
  les intrants exacts de la règle d'entrée. Le seul reconstruit est dd6 (repli depuis le
  sommet 6 h), calculé sur le chemin de prix ; c'est noté.

CE QU'ON MESURE
  Entrées :  E0 ACTUEL (repli ≥ max(dip, 5, 0,30·m6))  ·  E1 repli ≥ 2 %  ·  E2 sans repli
  Sorties :  X0 ACTUEL (rip 50 % + stop dur + trailing)  ·  X1 1er palier à ×2 (le seed ne
             meurt plus sous un multiple) + trailing  ·  X2 trailing seul
  Neuf combinaisons. Juge sur la 2e moitié (hors échantillon). Frais 5 bps/côté.
  Mise FIXE 30 $ pour toutes les variantes : on isole l'EFFET DE RÈGLE (le mur est mesuré
  à part, cf. chiffrage_compounding.py).

Aucun ordre, aucun €. Lecture seule, aucune écriture moteur.
"""
import gzip
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CROIS = os.path.join(RUNS, "croisement_contexte.jsonl")
FEE = 0.0005          # 5 bps par côté
MISE = 30.0           # mise fixe, identique pour toutes les variantes
IMPULSE_PCT = 8.0     # IMPULSE_PCT de defaults.env : m6 mini pour une rafale
PULLBACK_FRAC = 0.30  # IMPULSE_PULLBACK_FRAC
PULLBACK_MIN = 5.0    # IMPULSE_PULLBACK_MIN_PCT
# CORRECTION 23/09/2026 (classe F) : ce terme était ABSENT des trois calculs de seuil de
# cet instrument, alors qu'il DOMINE sur les paires vives (EDEL 13,20 % · RIZE 8,44 % de
# repli exigé, contre 4,2 % au profil). Valeur lue dans config/defaults.env.
DIP_CADENCE_MULT = 0.50  # DIP_CADENCE_MULT
SEUIL_SWING = 15.0    # amplitude minimale d'un cycle (comme la fiche par actif)

PAIRES = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT", "WUSDT",
          "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT", "TELUSDT", "CHIPUSDT",
          "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT", "RWAUSDT", "MNSRYUSDT"]


def profils():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                     "strategie", "universe_profils.json")
    raw = json.load(open(p, encoding="utf-8"))
    out = {}
    for k, v in raw.items():
        if not isinstance(v, dict):
            continue
        c = v.get("calib") or {}
        if c:
            out[k] = c
    return out


def sources():
    """Log vivant + archives, du plus ancien au plus récent."""
    for f in sorted(__import__("glob").glob(CROIS + ".*.gz"), reverse=True):
        yield f, True
    if os.path.exists(CROIS):
        yield CROIS, False


def charger():
    dat = defaultdict(list)
    vus = set()
    for f, gz in sources():
        try:
            fabrique = (gzip.open(f, "rt", encoding="utf-8", errors="ignore")
                        if gz else open(f, encoding="utf-8", errors="ignore"))
            with fabrique as fh:
                for line in fh:
                    if '"pair"' not in line:
                        continue
                    try:
                        d = json.loads(line)
                    except Exception:
                        continue
                    pair = d.get("pair")
                    if pair not in PAIRES or not d.get("price"):
                        continue
                    cle = (pair, d.get("ts"))
                    if cle in vus:
                        continue
                    vus.add(cle)
                    dat[pair].append(d)
        except (OSError, EOFError):
            continue
    for p in dat:
        dat[p].sort(key=lambda x: x["ts"])
    return dat


def avec_dd6(points):
    """Ajoute dd6 (repli depuis le sommet des 6 h précédentes) — reconstruit du chemin.
    Les 6 h suivent la convention du moteur (fenêtre glissante en secondes)."""
    out = []
    for i, d in enumerate(points):
        t, px = d["ts"], float(d["price"])
        j = i
        haut = px
        while j >= 0 and points[j]["ts"] >= t - 6 * 3600:
            haut = max(haut, float(points[j]["price"]))
            j -= 1
        out.append({**d, "px": px, "dd6": (1 - px / haut) * 100.0 if haut > 0 else 0.0})
    return out


# ── la porte « fenêtre d'entrée » (ENTREE_FENETRE_ON, câblée 21/09) ───────────
FENETRE_MODE = "--fenetre" in sys.argv
_CARTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                      "strategie", "carte_fenetres_entree.json")

def fenetres():
    try:
        c = json.load(open(_CARTE, encoding="utf-8"))
    except Exception:
        return {}
    return {p: [str(h) for h in (v or {}).get("fenetre_entree_utc") or []]
            for p, v in (c.get("paires") or {}).items()}


_FEN = fenetres()


# ── conditions d'entrée ─────────────────────────────────────────────────────
def entree(variante, p, cal, pair=None):
    m6 = float(p.get("m6_pct") or 0)
    dd6 = p["dd6"]
    if m6 < IMPULSE_PCT:
        return False
    if FENETRE_MODE and pair:
        f = _FEN.get(pair) or []
        if f and str(p.get("utc", ""))[11:13] not in f:
            return False
    # LE SEUIL RÉEL (corrigé le 23/09 : le terme `0,50 × cadence` manquait)
    dip = max(float(cal.get("dip_pct") or 5.0),
              float(p.get("cadence") or 0.0) * DIP_CADENCE_MULT)
    seuil_repli = max(dip, PULLBACK_MIN, m6 * PULLBACK_FRAC)
    if variante == "E0":                       # ACTUEL
        return dd6 >= seuil_repli
    if variante == "E1":                       # repli léger (2 %)
        return dd6 >= 2.0
    if variante == "E2":                       # sans repli
        return True
    return False


# ── moteur d'exécution ──────────────────────────────────────────────────────
def simuler(points, cal, variante_e, variante_x, pair=None):
    """Simule une paire. Une position à la fois, mise fixe, frais par côté."""
    stop = float(cal.get("stop_pct") or 10.0)
    rip = float(cal.get("rip_pct") or 4.0)
    arm = float(cal.get("trail_arm_pct") or 8.0)
    gb = float(cal.get("trail_giveback_pct") or 3.0)
    trades = []
    i, n = 0, len(points)
    while i < n:
        p = points[i]
        if not entree(variante_e, p, cal, pair):
            i += 1
            continue
        if i + 1 >= n:                              # pas de look-ahead : on entre au tick suivant
            break
        entree_px = points[i + 1]["px"]
        qty = MISE / entree_px
        reste = qty
        encaisse = 0.0
        haut = entree_px
        vendu1 = False
        j = i + 1
        while j < n and reste > 1e-12:
            px = points[j]["px"]
            haut = max(haut, px)
            g = (px / entree_px - 1) * 100
            gp = (haut / entree_px - 1) * 100
            # ---- SORTIES ----
            if variante_x == "X0":                  # ACTUEL
                if g <= -stop:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
                if not vendu1 and g >= rip:
                    v = reste * 0.5
                    encaisse += v * px * (1 - FEE); reste -= v; vendu1 = True
                elif vendu1 and gp >= arm and (gp - g) >= gb:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
                elif not vendu1 and gp >= arm and (gp - g) >= gb:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
            elif variante_x == "X1":                # 1er palier à ×2 (jamais sous un multiple)
                if not vendu1 and g >= 100.0:
                    v = reste * 0.5
                    encaisse += v * px * (1 - FEE); reste -= v; vendu1 = True
                elif vendu1 and gp >= arm and (gp - g) >= gb:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
                elif g <= -40.0:                    # garde-fou catastrophe (testé, déclaré)
                    encaisse += reste * px * (1 - FEE); reste = 0; break
            elif variante_x == "X2":                # trailing seul
                if gp >= arm and (gp - g) >= gb:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
                elif g <= -40.0:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
            elif variante_x == "X4":
                # ACTUEL RÉEL pour une paire À PROFIL TRAILING (EDEL 10/4, RIZE 11,4/4,55…).
                # Vérifié dans paper_diprip.py manage_open() : si trail_arm_pct/trail_giveback_pct
                # existent, le moteur fait STOP DUR + TRAILING, sans rip 50 % ni 2×.
                # (Mon X0 modélisait le rip 50 % de la branche standard : ce n'était PAS
                #  le comportement d'EDEL — erreur de fidélité corrigée le 21/09.)
                if g <= -stop:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
                elif gp >= arm and (gp - g) >= gb:
                    encaisse += reste * px * (1 - FEE); reste = 0; break
            elif variante_x == "X3":                # CONSERVATEUR : stop gardé, rip 50 % retiré
                if g <= -stop:                       # le stop dur reste en place
                    encaisse += reste * px * (1 - FEE); reste = 0; break
                elif gp >= arm and (gp - g) >= gb:   # on court jusqu'au trailing
                    encaisse += reste * px * (1 - FEE); reste = 0; break
            j += 1
        if reste > 1e-12:                           # fin de fenêtre : on solde
            px = points[min(j, n - 1)]["px"]
            encaisse += reste * px * (1 - FEE)
        net = encaisse - MISE * (1 + FEE)
        trades.append({"t0": points[i + 1]["utc"], "px0": entree_px, "net": net,
                       "close": points[min(j, n - 1)]["utc"]})
        i = j + 1
    return trades


# ── source 2 : klines 1 h (90 j, 20 paires) — reproduit m6/dd6 du moteur ──────
KL_MODE = "--klines" in sys.argv


def iso(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def charger_klines():
    """Reproduit les intrants de la règle IMPULSE depuis des bougies 1 h :
    m6 = variation sur 6 bougies, dd6 = repli depuis le plus haut des 6 bougies.
    APPROXIMATION DÉCLARÉE : le moteur calcule m6/dd6 sur ses propres ticks et
    applique aussi des portes (mur, volume, fenêtre) qu'on ne rejoue pas ici.
    On isole donc l'EFFET DES DEUX RÈGLES testées, pas le P&L absolu du moteur."""
    dat = {}
    for p in PAIRES:
        f = os.path.join(RUNS, f"SIMU_KL_{p}_90d.json")
        if not os.path.exists(f):
            continue
        bars = json.load(open(f))
        cl = [float(b[4]) for b in bars]
        hi = [float(b[2]) for b in bars]
        lo = [float(b[3]) for b in bars]
        pts = []
        for i, b in enumerate(bars):
            seg = cl[max(0, i - 6):i + 1]
            c = cl[i]
            haut = max(seg)
            # CADENCE — CORRECTION 23/09/2026 : le seuil d'entrée dépend de
            # `dip = max(dip_pct ; DIP_CADENCE_MULT × cadence)` (score_pair, l.566) et
            # cet instrument l'IGNORAIT (il ne lisait que dip_pct → 5 %, au lieu de
            # 13,20 % sur EDEL). On reproduit la cadence EXACTEMENT comme le moteur :
            # médiane des ranges de blocs de 24 h sur la fenêtre 15 j glissante.
            sh, sl = hi[max(0, i - 359):i + 1], lo[max(0, i - 359):i + 1]
            rng = []
            for k in range(0, len(sh), 24):
                ch, clw = sh[k:k + 24], sl[k:k + 24]
                if ch and clw and min(clw) > 0:
                    rng.append((max(ch) / min(clw) - 1.0) * 100.0)
            rng.sort()
            if rng:
                cad = rng[len(rng) // 2]
            elif sh and min(sl) > 0:
                cad = max(((max(sh) / min(sl) - 1.0) * 100.0) / 5.0, 3.0)
            else:
                cad = 3.0
            pts.append({"ts": b[0] // 1000, "utc": iso(b[0]), "px": c,
                        "m6_pct": (c / seg[0] - 1) * 100 if seg[0] > 0 else 0.0,
                        "dd6": (1 - c / haut) * 100 if haut > 0 else 0.0,
                        "cadence": cad})
        dat[p] = pts
    return dat


def stats(trades):
    if not trades:
        return {"n": 0, "net": 0.0, "wr": None, "pire": 0.0}
    net = sum(t["net"] for t in trades)
    g = [t["net"] for t in trades if t["net"] > 0]
    return {"n": len(trades), "net": net,
            "wr": 100.0 * len(g) / len(trades),
            "pire": min(t["net"] for t in trades)}


def episodes(dd, cal_all):
    """LA STATISTIQUE ROBUSTE (n = épisodes, pas trades) : combien de rafales
    IMPULSE le moteur ne PEUT PAS prendre, quelle que soit sa vitesse de réaction ?

    Un épisode = une suite de ticks où m6 ≥ IMPULSE_PCT (rafale en cours).
    Il est INACCESSIBLE si, pendant TOUT l'épisode, dd6 n'atteint jamais le seuil
    exigé (dd6 ≥ max(dip, 5, 0,30·m6)) : la condition d'entrée est alors
    mathématiquement insatisfiable à mesure que la rafale accélère — c'est le
    « pump en ligne droite ». On mesure l'amplitude qu'on ne prend pas.
    """
    lignes = []
    for p, pts in dd.items():
        cal = cal_all.get(p) or {}
        if not cal:
            continue
        dip_plancher = float(cal.get("dip_pct") or 5.0)
        i, n = 0, len(pts)
        while i < n:
            if float(pts[i].get("m6_pct") or 0) < IMPULSE_PCT:
                i += 1
                continue
            j = i
            while j + 1 < n and float(pts[j + 1].get("m6_pct") or 0) >= IMPULSE_PCT:
                j += 1
            seg = pts[i:j + 1]
            p0 = pts[i]["px"]
            pic = max(x["px"] for x in seg)
            amp = (pic / p0 - 1) * 100 if p0 else 0.0
            accessible = any(
                x["dd6"] >= max(dip_plancher,
                                float(x.get("cadence") or 0.0) * DIP_CADENCE_MULT,
                                PULLBACK_MIN,
                                float(x.get("m6_pct") or 0) * PULLBACK_FRAC)
                for x in seg
            )
            if amp >= 5.0:      # on ne compte que les rafales qui ont réellement monté
                lignes.append({"pair": p, "t0": pts[i]["utc"], "duree_h": (j - i + 1),
                               "amp": amp, "accessible": accessible})
            i = j + 1
    return lignes


def main():
    cal_all = profils()
    if KL_MODE:
        dd = charger_klines()
    else:
        dat = charger()
        dd = {p: avec_dd6(v) for p, v in dat.items() if v}
    if not dd:
        print("[ERR] log continu introuvable/vide"); return 2
    t_min = min(v[0]["ts"] for v in dd.values())
    t_max = max(v[-1]["ts"] for v in dd.values())
    f = "%Y-%m-%d %H:%MZ"
    print(f"SOURCE : {'klines 1 h (90 j)' if KL_MODE else 'log continu du moteur'} · "
          f"{len(dd)} paires · du {datetime.fromtimestamp(t_min, timezone.utc):{f}} "
          f"au {datetime.fromtimestamp(t_max, timezone.utc):{f}}")
    print(f"(mise fixe {MISE:.0f} $ · frais 5 bps/côté · pas de look-ahead · "
          f"fenêtre d'entrée : {'APPLIQUÉE' if FENETRE_MODE else 'non appliquée'})\n")
    coupure = t_min + (t_max - t_min) * 0.60
    res = {}
    for ve in ("E0", "E1", "E2"):
        for vx in ("X0", "X1", "X2", "X3", "X4"):
            tr_in, tr_out = [], []
            for p, pts in dd.items():
                cal = cal_all.get(p) or {}
                if not cal:
                    continue
                tr = simuler(pts, cal, ve, vx, p)
                for t in tr:
                    ts = datetime.strptime(t["t0"], "%Y-%m-%dT%H:%M:%SZ").replace(
                        tzinfo=timezone.utc).timestamp()
                    (tr_in if ts < coupure else tr_out).append(t)
            res[(ve, vx)] = (stats(tr_in), stats(tr_out))
    print("== GO 1 (ENTRÉE) × GO 2 (SORTIE) — X4 = LE VRAI ACTUEL des paires à profil trailing ==")
    print(f"{'entrée':8}{'sortie':8}{'n(test)':>9}{'net test':>11}{'WR test':>9}"
          f"{'pire':>9}   {'net 1re moitié (n)':>22}")
    base = res[("E0", "X4")]
    for ve in ("E0", "E1", "E2"):
        for vx in ("X0", "X4", "X1", "X2", "X3"):
            a, b = res[(ve, vx)]
            marque = "  ← actuel" if (ve, vx) == ("E0", "X0") else ""
            wr = f"{b['wr']:.0f} %" if b["wr"] is not None else "—"
            print(f"{ve:8}{vx:8}{b['n']:>9}{b['net']:>+11.2f}{wr:>9}"
                  f"{b['pire']:>+9.2f}   {a['net']:>+15.2f} ({a['n']:>3}){marque}")
    d0 = base[1]["net"]
    print("\n== LECTURE (test hors échantillon) ==")
    for ve in ("E0", "E1", "E2"):
        for vx in ("X1", "X2", "X3"):
            b = res[(ve, vx)][1]
            a = res[(ve, vx)][0]
            ok = (b["net"] > base[1]["net"]) and (a["net"] > base[0]["net"])
            print(f"  {ve}+{vx} : net test {b['net']:+.2f} $ ({b['net'] - d0:+.2f} $ vs actuel) · "
                  f"1re moitié {a['net']:+.2f} $ · {'✅ cohérent' if ok else '⚠️ incohérent'}")
    print("\n== GO 1 : LES RAFALES STRUCTURELLEMENT INACCESSIBLES (n = épisodes) ==")
    eps = episodes(dd, cal_all)
    inacc = [e for e in eps if not e["accessible"]]
    acc = [e for e in eps if e["accessible"]]
    print(f"  rafales relevées (m6 ≥ {IMPULSE_PCT:.0f} % et amplitude ≥ 5 %) : {len(eps)}")
    print(f"  ACCESSIBLES : {len(acc):>3}  amplitude moyenne "
          f"{sum(e['amp'] for e in acc) / len(acc):+.1f} %" if acc else "  ACCESSIBLES : 0")
    if inacc:
        print(f"  INACCESSIBLES : {len(inacc):>3}  amplitude moyenne "
              f"{sum(e['amp'] for e in inacc) / len(inacc):+.1f} %")
        par = defaultdict(float)
        for e in inacc:
            par[e["pair"]] += e["amp"]
        top = sorted(par.items(), key=lambda x: -x[1])[:6]
        print("     top paires (somme des amplitudes manquées) : "
              + " · ".join(f"{k.replace('USDT','')} {v:.0f} %" for k, v in top))
        part = len(inacc) / len(eps) * 100
        print(f"     PART des rafales inaccessibles : {part:.0f} %"
              + ("  ⚠️ la règle de repli ferme la majorité des rafales" if part >= 50
                 else ""))

    print("\n== L'ACTUEL RÉEL (X4) vs les variantes — LA comparaison qui compte ==")
    print(f"{'entrée':8}{'sortie':8}{'1re moitié':>13}{'test':>10}{'n(test)':>9}"
          f"{'top paire (test)':>20}")
    for ve in ("E0", "E1", "E2"):
        for vx in ("X4", "X1", "X2"):
            a, b = res[(ve, vx)]
            par = {}
            for p, pts in dd.items():
                cal = cal_all.get(p) or {}
                if not cal:
                    continue
                tr = [t for t in simuler(pts, cal, ve, vx, p)
                      if datetime.strptime(t["t0"], "%Y-%m-%dT%H:%M:%SZ").replace(
                          tzinfo=timezone.utc).timestamp() >= coupure]
                if tr:
                    par[p] = sum(t["net"] for t in tr)
            tot = sum(par.values())
            top = sorted(par.items(), key=lambda x: -x[1])[:1]
            part = (top[0][1] / tot * 100) if tot else 0
            conc = f"{top[0][0].replace('USDT','')} {part:.0f} %" if tot > 0 else "—"
            marque = "  ← ACTUEL" if (ve, vx) == ("E0", "X4") else ""
            print(f"{ve:8}{vx:8}{a['net']:>+13.2f}{b['net']:>+10.2f}{b['n']:>9}{conc:>20}{marque}")

    print("\n== VARIANTE CONSERVATRICE X3 (stop gardé, rip 50 % retiré) ==")
    print(f"{'entrée':8}{'sortie':8}{'1re moitié':>13}{'test':>10}{'n(test)':>9}"
          f"{'concentration top paire':>26}")
    for ve in ("E0", "E1", "E2"):
        a = res[(ve, "X3")][0]
        b = res[(ve, "X3")][1]
        par = {}
        for p, pts in dd.items():
            cal = cal_all.get(p) or {}
            if not cal:
                continue
            tr = [t for t in simuler(pts, cal, ve, "X3", p)
                  if datetime.strptime(t["t0"], "%Y-%m-%dT%H:%M:%SZ").replace(
                      tzinfo=timezone.utc).timestamp() >= coupure]
            if tr:
                par[p] = sum(t["net"] for t in tr)
        tot = sum(par.values())
        top = sorted(par.items(), key=lambda x: -x[1])[:1]
        part = (top[0][1] / tot * 100) if tot else 0
        conc = f"{top[0][0].replace('USDT','')} {part:.0f} %" if tot > 0 else "—"
        print(f"{ve:8}{'X3':8}{a['net']:>+13.2f}{b['net']:>+10.2f}{b['n']:>9}{conc:>26}")

    print("\n== CONCENTRATION DES GAINS (test) — un gain porté par UNE paire n'est pas un levier ==")
    for ve, vx in (("E0", "X0"), ("E0", "X1"), ("E2", "X0"), ("E2", "X1"), ("E2", "X2")):
        par_paire = {}
        for p, pts in dd.items():
            cal = cal_all.get(p) or {}
            if not cal:
                continue
            tr = [t for t in simuler(pts, cal, ve, vx, p)
                  if datetime.strptime(t["t0"], "%Y-%m-%dT%H:%M:%SZ").replace(
                      tzinfo=timezone.utc).timestamp() >= coupure]
            if tr:
                par_paire[p] = sum(t["net"] for t in tr)
        tot = sum(par_paire.values())
        if not tot:
            continue
        top = sorted(par_paire.items(), key=lambda x: -x[1])[:3]
        part = top[0][1] / tot * 100 if tot > 0 else 0
        pos = sum(1 for v in par_paire.values() if v > 0)
        print(f"  {ve}+{vx} : net test {tot:+.2f} $ · {pos}/{len(par_paire)} paires gagnantes · top3 "
              + " · ".join(f"{k.replace('USDT','')} {v:+.2f}" for k, v in top)
              + f" · 1re paire = {part:.0f} %"
              + ("  ⚠️ CONCENTRÉ" if part >= 70 else ""))

    print("\n== EDEL DÉTAILLÉ — TOUTES LES SORTIES, LES DEUX ENTRÉES EXTRÊMES ==")
    print(f"{'':10}" + "".join(f"{vx:>12}" for vx in ("X4", "X0", "X1", "X2")))
    for ve in ("E0", "E1", "E2"):
        ligne = f"  {ve:8}"
        for vx in ("X4", "X0", "X1", "X2"):
            tr = simuler(dd.get("EDELUSDT", []), cal_all.get("EDELUSDT", {}), ve, vx,
                         "EDELUSDT")
            s = stats(tr)
            ligne += f"{s['net']:>+10.2f}  " if s["n"] else f"{'—':>12}"
        print(ligne)
    print("  (EDEL seul, mise fixe 30 $, frais 5 bps/côté)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
