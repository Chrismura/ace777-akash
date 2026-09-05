#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""suivi_setup_actif.py — Suivi quotidien du set-up par actif (30/08/2026).

Généralise `suivi_setup_red.py` à TOUS les actifs du portefeuille (doctrine gravée :
tous les actifs sont sous observation). Ajoute les 3 métriques pro de la consultation
méthode V2 (DEEPSEEK/ULTRA/codeur) :

- AMIHUD (Illiquidity Ratio) = |return| / quote_volume — « peux-tu sortir sans casser le prix »
- PARKINSON (volatilité High/Low) — capture la vraie amplitude
- TRADE SIGN DELTA (agressivité taker) = (qty acheteur − qty vendeur) / total — pression réelle

Usage : python3 suivi_setup_actif.py [PAIRE1 PAIRE2 ...]   (défaut : paires du state)
Ne modifie RIEN dans Hulk : pure mesure d'observation.
"""
import json
import math
import os
import statistics
import sys
import urllib.parse
import urllib.request
from collections import defaultdict

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CROIS = os.path.join(RUNS, "croisement_contexte.jsonl")
ETAT = os.path.join(RUNS, "DIVERGENCE_ETAT.json")
STATE = None  # résolu ci-dessous (dernier PAPER_*_state.json)

# fenêtres spécifiques par paire (heures UTC) — RED = modèle validé
FENETRES = {
    "REDUSDT": {"creux": (14, 15, 16, 17), "nuit": (21, 22, 23, 0, 1, 2, 3, 4)},
}
POUSSIERE_SEUIL = 15.0

# Portefeuille CORE (20 paires) — suivi systématique, indépendant du state paper.
# Correctif 06/09 : BTC/RIZE/CHIP/FLUID avaient cessé d'être mesurées en sortant du state.
CORE_PAIRS = [
    "BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT",
    "WUSDT", "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT",
    "TELUSDT", "CHIPUSDT", "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT",
    "RWAUSDT", "MNSRYUSDT",
]


def gj(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_json(url):
    return gj(url)


def klines(pair, interval="60m", limit=48):
    q = urllib.parse.urlencode({"symbol": pair, "interval": interval, "limit": limit})
    try:
        return gj(f"https://api.mexc.com/api/v3/klines?{q}")
    except Exception:
        return []


def trades(pair, limit=200):
    q = urllib.parse.urlencode({"symbol": pair, "limit": limit})
    try:
        return gj(f"https://api.mexc.com/api/v3/trades?{q}")
    except Exception:
        return []


def amihud(kl):
    """Amihud = |return horaire| / quote_volume (moyenne sur les klines dispo)."""
    if len(kl) < 3:
        return None
    vals = []
    for i in range(1, len(kl)):
        c0, c1 = float(kl[i - 1][4]), float(kl[i][4])
        vol = float(kl[i][7]) if len(kl[i]) > 7 and kl[i][7] not in (None, "") else float(kl[i][5]) * c1
        if c0 > 0 and vol > 0:
            vals.append(abs(c1 - c0) / c0 / vol)
    return sum(vals) / len(vals) if vals else None


def parkinson(kl):
    """Volatilité de Parkinson sur les H/L des klines (24h = 24 bougies 1h)."""
    if len(kl) < 4:
        return None
    logs = []
    for c in kl:
        h, l = float(c[2]), float(c[3])
        if h > 0 and l > 0 and h >= l:
            logs.append(math.log(h / l) ** 2)
    if not logs:
        return None
    return math.sqrt(sum(logs) / (4.0 * math.log(2) * len(logs)))


def trade_sign_delta(tr):
    """Delta = (qty acheteur agressif − qty vendeur agressif) / total.
    isBuyerMaker=True → l'acheteur a pris l'ask (vendeur agressif, pression vente)."""
    if not tr:
        return None
    buy = sell = 0.0
    for t in tr:
        q = float(t.get("qty") or 0)
        if t.get("isBuyerMaker"):
            sell += q   # maker = vendeur : l'agressif est le BUYER ? Non — isBuyerMaker=True signifie le BUYER est maker (ordre limite), donc le taker est le SELLER agressif.
        else:
            buy += q    # isBuyerMaker=False → le SELLER est maker, le taker est le BUYER agressif
    total = buy + sell
    return (buy - sell) / total if total > 0 else 0.0


def load_points(pairs):
    dat = defaultdict(list)
    if not os.path.exists(CROIS):
        return dat
    for line in open(CROIS, encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("pair") in pairs:
            dat[d["pair"]].append(d)
    for p in dat:
        dat[p].sort(key=lambda x: x["ts"])
    return dat


def resolve_state_pairs():
    import glob
    files = sorted(glob.glob(os.path.join(RUNS, "PAPER_*_state.json")), key=os.path.getmtime)
    if not files:
        return []
    d = json.load(open(files[-1], encoding="utf-8"))
    pairs = set((d.get("positions") or {}).keys())
    pairs |= set((d.get("bags") or {}).keys())
    pairs |= set((d.get("pair_cash") or {}).keys())
    return sorted(pairs)


def corr_hourly(dat, pair, ref, now_ts, hours=24):
    def hourly(p):
        by = defaultdict(list)
        for d in dat[p]:
            if now_ts - hours * 3600 <= d["ts"] <= now_ts:
                by[d["utc"][:13]].append(d["price"])
        ks = sorted(by)
        return [sum(by[k]) / len(by[k]) for k in ks]
    a, b = hourly(pair), hourly(ref)
    n = min(len(a), len(b))
    if n < 6:
        return None
    x, y = a[-n:], b[-n:]
    mx, my = statistics.mean(x), statistics.mean(y)
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = (sum((xi - mx) ** 2 for xi in x) * sum((yi - my) ** 2 for yi in y)) ** 0.5
    return num / den if den else None


def signal_divergence(pair):
    try:
        if os.path.exists(ETAT):
            etat = json.load(open(ETAT, encoding="utf-8"))
            leaders = etat.get("leaders") or []
            pompes = etat.get("pompes_pieges") or []
            stab = (etat.get("stabilite") or {}).get(pair)
            cls = "LEADER" if pair in leaders else ("POMPE_PIEGE" if pair in pompes else "neutre")
            return {"class": cls, "stabilite": stab}
    except Exception:
        pass
    return None


def main():
    pairs = sys.argv[1:] or sorted(set(CORE_PAIRS) | set(resolve_state_pairs()))
    if not pairs:
        print("[ERR] aucune paire (donner en argument ou state introuvable)")
        sys.exit(1)

    # toujours charger BTC/ETH pour les corrélations, même en run ciblé
    dat = load_points(set(pairs) | {"BTCUSDT", "ETHUSDT"})
    for pair in pairs:
        try:
            measure(pair, dat)
        except Exception as e:
            print(f"[ERR] {pair}: {e}")


def measure(pair, dat):
    now = (dat.get(pair) or [None])[-1]
    utc = now["utc"] if now else "?"
    h = int(utc[11:13]) if now else -1

    fen = "AUTRE"
    if pair in FENETRES:
        f = FENETRES[pair]
        if h in f["creux"]:
            fen = "CREUX 14-17h"
        elif h in f["nuit"]:
            fen = "NUIT 21-05h"

    prix = now["price"] if now else None
    poussiere = now.get("poussiere_taux_fantome") if now else None  # indicateur PANIER (global, pas par paire)
    mur_moy = now.get("mur_bid_moy_usd") if now else None
    mur_max = now.get("mur_bid_max_usd") if now else None
    spoof = now.get("mur_spoof_pct") if now else None
    regime = now.get("regime") if now else None
    dd15 = now.get("dd15_pct") if now else None

    # métriques pro (API MEXC) — Parkinson retiré (verdict Cortana 30/08 : bruit sur small caps)
    kl = klines(pair)
    ami = amihud(kl)
    tr = trades(pair)
    tsd = trade_sign_delta(tr)

    # corrélations (si données dispo)
    now_ts = now["ts"] if now else 0
    corr_btc = corr_hourly(dat, pair, "BTCUSDT", now_ts) if dat.get(pair) and dat.get("BTCUSDT") else None
    corr_eth = corr_hourly(dat, pair, "ETHUSDT", now_ts) if dat.get(pair) and dat.get("ETHUSDT") else None

    sig = signal_divergence(pair)

    verdict = f"prix {prix if prix is not None else '?'}"
    if poussiere is not None:
        verdict += f" · poussière(panier) {poussiere:.1f}%"
    if ami is not None:
        verdict += f" · Amihud {ami:.2e}"
    if tsd is not None:
        verdict += f" · delta {tsd:+.2f}"
    if mur_moy is not None:
        verdict += f" · mur moy {mur_moy:,.0f}$"
    if mur_max is not None:
        verdict += f" · mur max (run) {mur_max:,.0f}$"

    rec = {
        "ts": utc, "pair": pair, "prix": prix, "heure_utc": h, "fenetre": fen,
        "regime": regime, "poussiere_panier": poussiere, "mur_bid_moy_usd": mur_moy,
        "mur_bid_max_usd": mur_max,
        "spoof_pct": spoof, "dd15_pct": dd15,
        "amihud": ami, "trade_sign_delta": tsd,
        "corr_btc_24h": corr_btc, "corr_eth_24h": corr_eth,
        "signal_divergence": sig, "verdict": verdict,
    }

    jl = os.path.join(RUNS, f"SUIVI_SETUP_{pair}.jsonl")
    md = os.path.join(RUNS, f"SUIVI_SETUP_{pair}.md")
    with open(jl, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    rows = [json.loads(l) for l in open(jl, encoding="utf-8") if l.strip()]
    lines = [
        f"# 📈 SUIVI SET-UP — {pair} — historique (démarrage 30/08/2026)",
        "",
        "Consigne Christophe : mesurer aujourd'hui, mesurer demain, voir la différence.",
        "Métriques : maison (mur moy/max + régime ; poussière = indicateur PANIER) + pro (Amihud/Trade Sign Delta).",
        "",
        "| # | Date (UTC) | Heure | Fenêtre | Prix | Régime | Pouss% (panier) | Mur moy $ | Mur max $ | Amihud | Δtaker | corr BTC | corr ETH | Sig div | Verdict |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        sig = r.get("signal_divergence") or {}
        sig_txt = f"{sig.get('class','?')} (stab {sig.get('stabilite','?')})" if sig else "—"
        def fmt(x, d=2):
            return f"{x:.{d}e}" if isinstance(x, float) and abs(x) < 1e-3 else (f"{x:.{d}f}" if isinstance(x, float) else ("—" if x is None else x))
        cbtc = f"{r['corr_btc_24h']:.2f}" if r.get("corr_btc_24h") is not None else "—"
        ceth = f"{r['corr_eth_24h']:.2f}" if r.get("corr_eth_24h") is not None else "—"
        lines.append(
            f"| {i} | {r['ts']} | {r.get('heure_utc','?')}h | {r.get('fenetre','?')} | "
            f"{r.get('prix','?')} | {r.get('regime','?')} | {r.get('poussiere_panier', r.get('poussiere','?'))} | "
            f"{r.get('mur_bid_moy_usd','?')} | {r.get('mur_bid_max_usd','?')} | {fmt(r.get('amihud'))} | "
            f"{fmt(r.get('trade_sign_delta'))} | {cbtc} | {ceth} | {sig_txt} | {r.get('verdict','?')} |"
        )
    lines.append("")
    lines.append("_Règle : on compare les lignes entre elles (même heure de mesure = comparable). On ne supprime rien._")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"[OK] {pair} {utc} -> {len(rows)} ligne(s) | {verdict}")


if __name__ == "__main__":
    main()