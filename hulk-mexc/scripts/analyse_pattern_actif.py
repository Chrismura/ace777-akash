#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyse_pattern_actif.py — Profil de comportement par actif (30/08/2026).

Applique à CHAQUE actif la même analyse que celle faite manuellement sur RED :
pattern intraday (creux/pic par heure UTC), volatilité, régimes, murs, poussière,
corrélations BTC/ETH, signal divergence. Sort un rapport markdown par actif.

Usage : python3 analyse_pattern_actif.py [PAIRE1 PAIRE2 ...]   (défaut : toutes les paires du state)
Ne modifie RIEN dans Hulk : lecture seule de croisement_contexte.jsonl + DIVERGENCE_ETAT.
"""
import json
import os
import statistics
import sys
from collections import Counter, defaultdict

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CROIS = os.path.join(RUNS, "croisement_contexte.jsonl")
ETAT = os.path.join(RUNS, "DIVERGENCE_ETAT.json")
OUT = os.path.join(RUNS, "profils_actifs")
os.makedirs(OUT, exist_ok=True)


def load_all():
    dat = defaultdict(list)
    for line in open(CROIS, encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        dat[d["pair"]].append(d)
    for p in dat:
        dat[p].sort(key=lambda x: x["ts"])
    return dat


def resolve_pairs():
    import glob
    files = sorted(glob.glob(os.path.join(RUNS, "PAPER_*_state.json")), key=os.path.getmtime)
    if not files:
        return []
    d = json.load(open(files[-1], encoding="utf-8"))
    pairs = set((d.get("positions") or {}).keys())
    pairs |= set((d.get("bags") or {}).keys())
    pairs |= set((d.get("pair_cash") or {}).keys())
    return sorted(pairs)


def signal_div(pair):
    try:
        if os.path.exists(ETAT):
            etat = json.load(open(ETAT, encoding="utf-8"))
            leaders = etat.get("leaders") or []
            pompes = etat.get("pompes_pieges") or []
            stab = (etat.get("stabilite") or {}).get(pair)
            cls = "LEADER" if pair in leaders else ("POMPE_PIEGE" if pair in pompes else "neutre")
            return f"{cls} (stab {stab})"
    except Exception:
        pass
    return "—"


def corr_pair(a_list, b_list):
    n = min(len(a_list), len(b_list))
    if n < 6:
        return None
    a, b = a_list[-n:], b_list[-n:]
    ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
    return num / den if den else None


def analyse(pair, dat):
    pts = dat.get(pair, [])
    if len(pts) < 30:
        return None  # pas assez de données (paires fraîches)
    prices = [d["price"] for d in pts]
    first_ts, last_ts = pts[0]["utc"], pts[-1]["utc"]

    # pattern intraday : moyenne par heure UTC
    by_hour = defaultdict(list)
    for d in pts:
        by_hour[int(d["utc"][11:13])].append(d["price"])
    hour_avg = {h: sum(v) / len(v) for h, v in by_hour.items()}
    if not hour_avg:
        return None
    # creux / pic (heure où la moyenne est minimale / maximale)
    h_creux = min(hour_avg, key=hour_avg.get)
    h_pic = max(hour_avg, key=hour_avg.get)
    # phases regroupées
    def avg_hours(hs):
        vals = [hour_avg[h] for h in hs if h in hour_avg]
        return sum(vals) / len(vals) if vals else None
    matin = avg_hours(range(8, 14))
    creux_phase = avg_hours(range(14, 18))
    soiree = avg_hours(range(18, 21))
    nuit = avg_hours(list(range(21, 24)) + list(range(0, 5)))

    # volatilité
    dd15 = [d.get("dd15_pct") for d in pts if isinstance(d.get("dd15_pct"), (int, float))]
    m6 = [abs(d.get("m6_pct") or 0) for d in pts]
    range_total = (max(prices) - min(prices)) / min(prices) * 100

    # régimes
    regimes = Counter(d["regime"] for d in pts)
    impulse_by_hour = defaultdict(int)
    for d in pts:
        if d["regime"] == "IMPULSE":
            impulse_by_hour[int(d["utc"][11:13])] += 1
    top_impulse = sorted(impulse_by_hour.items(), key=lambda x: -x[1])[:3]

    # murs / poussière
    mur_max = max((d.get("mur_bid_max_usd") or 0) for d in pts)
    spoof = statistics.mean([d.get("mur_spoof_pct") or 0 for d in pts])
    poussiere = statistics.mean([d.get("poussiere_taux_fantome") or 0 for d in pts])

    # corrélations horaires (prix moyens par heure, alignés sur les heures communes)
    def hourly_series(pair2):
        by = defaultdict(list)
        for d in dat[pair2]:
            by[d["utc"][:13]].append(d["price"])
        ks = sorted(by)
        return [sum(by[k]) / len(by[k]) for k in ks]
    my_series = hourly_series(pair)
    corr_btc = corr_pair(my_series, hourly_series("BTCUSDT")) if dat.get("BTCUSDT") else None
    corr_eth = corr_pair(my_series, hourly_series("ETHUSDT")) if dat.get("ETHUSDT") else None

    sig = signal_div(pair)

    # interprétation du pattern horaire
    ecart_phases = {}
    if nuit and creux_phase:
        ecart_phases["nuit_vs_creux"] = (nuit - creux_phase) / creux_phase * 100 if creux_phase else 0
    if matin and creux_phase:
        ecart_phases["matin_vs_creux"] = (matin - creux_phase) / creux_phase * 100 if creux_phase else 0

    rep = {
        "pair": pair,
        "pts": len(pts),
        "first": first_ts, "last": last_ts,
        "prix_min": min(prices), "prix_max": max(prices), "prix_last": prices[-1],
        "range_total_pct": round(range_total, 2),
        "h_creux": h_creux, "h_pic": h_pic,
        "niveau_matin": round(matin, 5) if matin else None,
        "niveau_creux14_17": round(creux_phase, 5) if creux_phase else None,
        "niveau_soir": round(soiree, 5) if soiree else None,
        "niveau_nuit": round(nuit, 5) if nuit else None,
        "dd15_moy": round(sum(dd15) / len(dd15), 2) if dd15 else None,
        "m6_moy": round(sum(m6) / len(m6), 2) if m6 else None,
        "regimes": dict(regimes.most_common(3)),
        "impulse_top": [(f"{h}h", n) for h, n in top_impulse],
        "mur_max_usd": round(mur_max, 0),
        "spoof_moy": round(spoof, 2),
        "poussiere_moy": round(poussiere, 1),
        "corr_btc": round(corr_btc, 2) if corr_btc is not None else None,
        "corr_eth": round(corr_eth, 2) if corr_eth is not None else None,
        "signal_div": sig,
        "ecart_nuit_creux_pct": round(ecart_phases.get("nuit_vs_creux", 0), 2),
        "ecart_matin_creux_pct": round(ecart_phases.get("matin_vs_creux", 0), 2),
    }
    return rep


def render(r):
    lines = [
        f"# 📊 PROFIL COMPORTEMENT — {r['pair']} ({r['pts']} points, {r['first']} → {r['last']})",
        "",
        "Généré automatiquement par `analyse_pattern_actif.py` — même méthode que RED.",
        "",
        "## 📈 PRIX & AMPLITUDE",
        f"| min | max | dernier | range total |",
        f"|---|---|---|---|",
        f"| {r['prix_min']} | {r['prix_max']} | {r['prix_last']} | {r['range_total_pct']}% |",
        "",
        "## 🕐 PATTERN INTRAday (moyenne par heure UTC)",
        f"| creux | pic | niveau matin 8-13h | niveau creux 14-17h | niveau soir 18-20h | niveau nuit 21-04h |",
        f"|---|---|---|---|---|---|",
        f"| {r['h_creux']}h | {r['h_pic']}h | {r['niveau_matin']} | {r['niveau_creux14_17']} | {r['niveau_soir']} | {r['niveau_nuit']} |",
        "",
        f"**Écart nuit vs creux : {r['ecart_nuit_creux_pct']}% · matin vs creux : {r['ecart_matin_creux_pct']}%**",
        "",
        "## ⚡ VOLATILITÉ & RÉGIMES",
        f"| dd15 moyen | move6 moyen | régimes dominants | rafales IMPULSE (top) |",
        f"|---|---|---|---|",
        f"| {r['dd15_moy']}% | {r['m6_moy']}% | {r['regimes']} | {r['impulse_top']} |",
        "",
        "## 🧱 MURS & POUSSIÈRE",
        f"| mur bid max | spoof moyen | poussière moyenne |",
        f"|---|---|---|",
        f"| {r['mur_max_usd']}$ | {r['spoof_moy']}% | {r['poussiere_moy']}% |",
        "",
        "## 🔗 CORRÉLATIONS & SIGNAL",
        f"| corr BTC | corr ETH | signal divergence |",
        f"|---|---|---|",
        f"| {r['corr_btc'] if r['corr_btc'] is not None else '—'} | {r['corr_eth'] if r['corr_eth'] is not None else '—'} | {r['signal_div']} |",
        "",
        "_Rapport automatique — à compléter avec le set-up individuel (prochaine étape)._",
    ]
    return "\n".join(lines)


def main():
    pairs = sys.argv[1:] or resolve_pairs()
    if not pairs:
        print("[ERR] aucune paire")
        sys.exit(1)
    dat = load_all()
    for pair in pairs:
        r = analyse(pair, dat)
        if r is None:
            print(f"[SKIP] {pair}: pas assez de données ({len(dat.get(pair, []))} pts)")
            continue
        fn = os.path.join(OUT, f"PROFIL_{pair}.md")
        with open(fn, "w", encoding="utf-8") as fh:
            fh.write(render(r))
        # aussi en JSON pour les outils en aval (zéro regex fragile)
        with open(os.path.join(OUT, f"PROFIL_{pair}.json"), "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=1)
        print(f"[OK] {pair}: creux {r['h_creux']}h / pic {r['h_pic']}h · range {r['range_total_pct']}% · "
              f"nuit-creux {r['ecart_nuit_creux_pct']}% · corr BTC {r['corr_btc']} · {r['signal_div']}")


if __name__ == "__main__":
    main()