#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyse_grille_correlation.py — Grille 20×20 : qui donne le mouvement, qui anticipe,
qui décorrèle (06/09/2026, consigne Christophe).

Contrairement à analyse_divergence.py (panier, fichier live ~3h), CE script :
- charge l'HISTORIQUE COMPLET (archive .gz + live, ~9 jours) ;
- calcule la corrélation CROISÉE entre TOUTES les paires (matrice 20×20, pas seulement BTC/ETH) ;
- mesure le lead-lag par paire vs panier ET par binôme (qui précède qui, de combien d'heures) ;
- classe les paires par DÉCORRÉLATION (moyenne |corr| aux 19 autres) → les moteurs endogènes ;
- teste le signal directionnel (m6 paire → delta panier +4h) sur 9 jours (stabilité vs 29/08).

Sorties :
- runs/grille_correlation.json  (données brutes pour les fiches v3)
- runs/GRILLE_CORRELATION_<ts>.md (rapport lisible)

Usage : python3 scripts/analyse_grille_correlation.py
"""
import datetime
import gzip
import json
import os
import statistics
from collections import defaultdict

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CROIS = os.path.join(RUNS, "croisement_contexte.jsonl")
CROIS_GZ = CROIS + ".1.gz"
NOW = datetime.datetime.now(datetime.timezone.utc)

CORE_PAIRS = [
    "BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT",
    "WUSDT", "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT",
    "TELUSDT", "CHIPUSDT", "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT",
    "RWAUSDT", "MNSRYUSDT",
]

LAGS = range(-3, 4)          # lead-lag testé (heures) : négatif = A précède B
SEUIL_LAG = 0.30             # |corr| min pour déclarer une relation binôme
SEUIL_SIGNAL = 0.15          # seuil signal directionnel (comme divergence 29/08)


def nettoyer_spikes(pts):
    """Bad ticks isolés (voir analyse_pattern_actif.py, correctif 06/09)."""
    if len(pts) < 3:
        return pts
    keep = [True] * len(pts)
    n = len(pts)
    for i in range(n):
        if 0 < i < n - 1:
            a, b = pts[i - 1], pts[i + 1]
        elif i == 0:
            a, b = pts[1], pts[2]
        else:
            a, b = pts[n - 3], pts[n - 2]
        p, pa, pb = pts[i]["price"], a["price"], b["price"]
        if p <= 0 or pa <= 0 or pb <= 0:
            continue
        if abs(p - pa) / pa > 0.5 and abs(p - pb) / pb > 0.5 and abs(pa - pb) / pa < 0.1:
            keep[i] = False
    return [d for d, k in zip(pts, keep) if k]


def load_all():
    dat = defaultdict(list)
    for path in [CROIS_GZ, CROIS]:
        if not os.path.exists(path):
            continue
        op = gzip.open if path.endswith(".gz") else open
        with op(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                dat[d["pair"]].append(d)
    for p in dat:
        dat[p].sort(key=lambda x: x["ts"])
        seen, out = set(), []
        for d in dat[p]:
            k = (d.get("ts"), d.get("pair"))
            if k in seen:
                continue
            seen.add(k)
            out.append(d)
        dat[p] = out
    return dat


def corr(xs, ys):
    n = min(len(xs), len(ys))
    if n < 24:  # au moins 24 heures communes
        return None, n
    xs, ys = xs[-n:], ys[-n:]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    if dx <= 0 or dy <= 0:
        return None, n
    return num / (dx * dy), n


def hourly_buckets(dat, pair, field):
    by = defaultdict(list)
    for d in dat.get(pair, []):
        if isinstance(d.get(field), (int, float)):
            by[d["ts"] - (d["ts"] % 3600)].append(d[field])
    return {h: sum(v) / len(v) for h, v in by.items()}


def ret_series(price_by_h):
    ks = sorted(price_by_h)
    out = {}
    for i in range(1, len(ks)):
        p0, p1 = price_by_h[ks[i - 1]], price_by_h[ks[i]]
        if p0 > 0:
            out[ks[i]] = (p1 - p0) / p0 * 100.0
    return out


def main():
    dat = load_all()
    pairs = [p for p in CORE_PAIRS if dat.get(p)]
    if len(pairs) < 5:
        print("[ERR] pas assez de paires")
        return 1

    # séries horaires : rendements (%) et m6
    rets, m6s, firsts, lasts = {}, {}, {}, {}
    for p in pairs:
        pts = nettoyer_spikes(dat[p])
        firsts[p], lasts[p] = pts[0]["utc"], pts[-1]["utc"]
        price_h = hourly_buckets(dat, p, "price")
        rets[p] = ret_series(price_h)
        m6s[p] = hourly_buckets(dat, p, "m6_pct")

    hours = sorted(set().union(*[set(r.keys()) for r in rets.values()]))

    # ---- 1. Lead-lag vs PANIER (rendement moyen du panier) ----
    pan_ret = {}
    for h in hours:
        vals = [rets[p][h] for p in pairs if h in rets[p]]
        if vals:
            pan_ret[h] = sum(vals) / len(vals)
    lag_panier = {}
    for p in pairs:
        best, bestlag = None, None
        for lag in LAGS:
            xs = [rets[p][h] for h in hours if h in rets[p] and (h + lag * 3600) in pan_ret]
            ys = [pan_ret[h + lag * 3600] for h in hours if h in rets[p] and (h + lag * 3600) in pan_ret]
            c, n = corr(xs, ys)
            if c is not None and (best is None or abs(c) > abs(best)):
                best, bestlag = c, lag
        lag_panier[p] = {"corr_max": round(best, 3) if best is not None else None,
                         "lag_h": bestlag}
    leaders = sorted(pairs, key=lambda p: (lag_panier[p]["lag_h"] if lag_panier[p]["lag_h"] is not None else 99,
                                           -(lag_panier[p]["corr_max"] or 0)))

    # ---- 2. Matrice 20×20 (lag 0, rendements horaires) + meilleure relation binôme ----
    mat, binome = {}, {}
    for i, a in enumerate(pairs):
        mat[a] = {}
        for b in pairs:
            if a == b:
                mat[a][b] = 1.0
                continue
            xs = [rets[a][h] for h in hours if h in rets[a] and h in rets[b]]
            ys = [rets[b][h] for h in hours if h in rets[a] and h in rets[b]]
            c, n = corr(xs, ys)
            mat[a][b] = round(c, 3) if c is not None else None
        # meilleur lead-lag binôme (a précède b ?)
        best = None
        for lag in LAGS:
            xs = [rets[a][h] for h in hours if h in rets[a] and (h + lag * 3600) in rets[b]]
            ys = [rets[b][h + lag * 3600] for h in hours if h in rets[a] and (h + lag * 3600) in rets[b]]
            c, n = corr(xs, ys)
            if c is not None and (best is None or abs(c) > abs(best[0])):
                best = (c, lag, n)
        binome[a] = best  # (corr, lag, n) — lag<0 : a précède b de |lag| h

    # ---- 3. Décorrélation : moyenne |corr| aux 19 autres ----
    decorr = {}
    for a in pairs:
        vals = [abs(mat[a][b]) for b in pairs if b != a and mat[a][b] is not None]
        decorr[a] = round(sum(vals) / len(vals), 3) if vals else None
    endogenes = sorted(pairs, key=lambda p: (decorr[p] if decorr[p] is not None else 9))

    # ---- 4. Copains (top 3 corrélés) ----
    copains = {}
    for a in pairs:
        tops = sorted([(mat[a][b], b) for b in pairs if b != a and mat[a][b] is not None],
                      key=lambda x: -abs(x[0]))[:3]
        copains[a] = [(b, c) for c, b in tops]

    # ---- 5. Signal directionnel sur 9 jours (m6 → delta panier +4h) ----
    pan_m6 = {}
    for h in hours:
        vals = [m6s[p][h] for p in pairs if h in m6s[p]]
        if vals:
            pan_m6[h] = sum(vals) / len(vals)
    signal_dir = {}
    for p in pairs:
        xs, ys = [], []
        for h in hours:
            if h in m6s[p] and h in pan_m6 and (h + 4 * 3600) in pan_m6:
                xs.append(m6s[p][h])
                ys.append(pan_m6[h + 4 * 3600] - pan_m6[h])
        c, n = corr(xs, ys)
        signal_dir[p] = round(c, 3) if c is not None else None

    # ---- Sortie JSON ----
    out_json = {
        "generated": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fenetre": {"first": min(firsts.values()), "last": max(lasts.values())},
        "lag_panier": lag_panier,
        "matrice_lag0": mat,
        "binome_best": {a: {"corr": round(b[0], 3), "lag_h": b[1], "n_h": b[2]} for a, b in binome.items() if b},
        "decorrelation_moy": decorr,
        "copains": copains,
        "signal_directionnel_9j": signal_dir,
    }
    with open(os.path.join(RUNS, "grille_correlation.json"), "w", encoding="utf-8") as fh:
        json.dump(out_json, fh, ensure_ascii=False, indent=1)

    # ---- Rapport MD ----
    short = lambda p: p.replace("USDT", "")
    L = [f"# GRILLE CORRÉLATION 20×20 — {NOW.strftime('%Y-%m-%d %H:%MZ')}",
         f"\nFenêtre : {min(firsts.values())} → {max(lasts.values())} · rendements horaires · "
         f"lags {LAGS.start}h..{LAGS.stop - 1}h · seuils relation ±{SEUIL_LAG} / signal ±{SEUIL_SIGNAL}\n"]

    L.append("## 1. QUI DONNE LE MOUVEMENT ? (lead-lag vs panier)")
    L.append("lag négatif = PRÉCÈDE le panier (anticipe) · 0 = bouge avec · positif = SUIT")
    L.append("| PAIRE | corr max | lag (h) | lecture |")
    L.append("|---|---|---|---|")
    for p in leaders:
        d = lag_panier[p]
        c, lg = d["corr_max"], d["lag_h"]
        if c is None:
            lect = "—"
        elif lg is not None and lg < 0 and abs(c) >= SEUIL_LAG:
            lect = f"🟢 ANTICIPATEUR (précède de {abs(lg)}h)"
        elif lg == 0 and abs(c) >= SEUIL_LAG:
            lect = "⚪ synchronisé (baromètre)"
        elif lg is not None and lg > 0:
            lect = "🔶 suiveur (retardataire)"
        else:
            lect = "· faible lien"
        L.append(f"| {short(p)} | {c if c is not None else '—'} | {lg if lg is not None else '—'} | {lect} |")

    L.append("\n## 2. MATRICE 20×20 (corr lag 0, rendements horaires)")
    L.append("Lecture ligne = paire de référence. `—` = moins de 24h communes.")
    header = "| | " + " | ".join(short(p) for p in pairs) + " |"
    sep = "|---" * (len(pairs) + 1) + "|"
    L += [header, sep]
    for a in pairs:
        row = [short(a)]
        for b in pairs:
            v = mat[a][b]
            row.append("—" if v is None else (f"{v:.1f}".replace("0.", ".")))
        L.append("| " + " | ".join(row) + " |")

    L.append("\n## 3. QUI DÉCORRÈLE DU GROUPE ? (moyenne |corr| aux 19 autres — plus bas = plus endogène)")
    L.append("| PAIRE | décorr moy | top 3 copains (|corr|) | lecture |")
    L.append("|---|---|---|---|")
    for p in endogenes:
        d = decorr[p]
        tops = ", ".join(f"{short(b)} ({c:+.2f})" for b, c in copains[p])
        if d is not None and d < 0.25:
            lect = "🟣 ENDOGÈNE — moteur propre (signaux du panier peu utiles)"
        elif d is not None and d < 0.45:
            lect = "🟡 semi-endogène — un pied dans le groupe"
        else:
            lect = "🟠 corrélationné au groupe (filtre macro indispensable)"
        L.append(f"| {short(p)} | {d if d is not None else '—'} | {tops} | {lect} |")

    L.append("\n## 4. RELATIONS BINÔMES MARQUANTES (|corr| ≥ %.2f, meilleur lag)" % SEUIL_LAG)
    L.append("lag négatif = la 1ʳᵉ paire PRÉCÈDE la 2ᵉ (de |lag| h) — piste « premier qui donne le mouvement »")
    rel = []
    for a in pairs:
        b = binome.get(a)
        if not b or abs(b[0]) < SEUIL_LAG or b[1] is None or b[1] == 0:
            continue
        rel.append((a, b[0], b[1], b[2]))
    # dédoublonner les paires réciproques
    seen = set()
    for a, c, lag, n in sorted(rel, key=lambda x: -abs(x[1])):
        key = frozenset([a, "—"])
        tag = f"{short(a)} → leader sur ses copains" if lag < 0 else f"{short(a)} → suit"
        L.append(f"- **{short(a)}** : meilleure relation lag {lag:+d}h (corr {c:+.2f}, {n}h communes)")
    if not rel:
        L.append("- aucune relation binôme nette au-delà du lag 0 sur 9 jours — le groupe bouge synchronisé (lag 0)")

    L.append("\n## 5. SIGNAL PRÉCURSEUR (m6 → delta panier +4h, fenêtre 9 jours — test de stabilité du 29/08)")
    L.append("| PAIRE | corr dir | signal |")
    L.append("|---|---|---|")
    for p in sorted(pairs, key=lambda x: -(signal_dir.get(x) or 0)):
        c = signal_dir.get(p)
        sig = ("🟢 LEADER haussier" if (c or 0) >= SEUIL_SIGNAL else
               "🔴 POMPE-PIÈGE" if (c or 0) <= -SEUIL_SIGNAL else
               "🟡 léger achat" if (c or 0) > 0.05 else
               "🟠 léger sommet" if (c or 0) < -0.05 else "⚪ neutre")
        L.append(f"| {short(p)} | {c if c is not None else '—'} | {sig} |")

    L.append("\n---\n*Généré par `analyse_grille_correlation.py` — relancer pour rafraîchir. "
             "Données brutes : `runs/grille_correlation.json` (consommé par les fiches v3).*")

    fn = os.path.join(RUNS, f"GRILLE_CORRELATION_{NOW.strftime('%Y%m%d_%H%M')}.md")
    with open(fn, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("\n".join(L))
    print(f"\n[OK] {fn} + grille_correlation.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
