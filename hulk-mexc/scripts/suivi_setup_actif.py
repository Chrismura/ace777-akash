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
import datetime
import glob
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


# ============================================================================
# HISTORIQUE DES CYCLES PAR ACTIF (21/09, consigne Christophe : « chaque actif a
# sa fiche et tout doit être écrit »). Le log continu du moteur
# (croisement_contexte.jsonl) porte le prix de CHAQUE paire à CHAQUE cycle :
# c'est l'histoire de l'actif, écrite par le moteur lui-même. On n'invente rien.
# ============================================================================
SEUIL_SWING_PCT = 15.0   # en dessous, c'est le bruit du carnet, pas un cycle
EVENTS_VENTE = ("SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH", "STOP", "STOP_ALL")


def swings(serie, seuil=SEUIL_SWING_PCT):
    """Zigzag : ne garde que les retournements >= seuil %. Retourne (pivots,
    état), pivots alternés creux/pic du plus ancien au plus récent, état =
    (direction, ts, prix) de l'extrême courant (le cycle EN COURS)."""
    out = []
    if len(serie) < 2:
        return out, None
    direction = 0
    piv_t, piv_p = serie[0]
    for ts, px in serie[1:]:
        if direction >= 0:
            if px > piv_p:
                piv_t, piv_p = ts, px
            elif px <= piv_p * (1 - seuil / 100.0):
                out.append(("pic", piv_t, piv_p))
                direction, piv_t, piv_p = -1, ts, px
        else:
            if px < piv_p:
                piv_t, piv_p = ts, px
            elif px >= piv_p * (1 + seuil / 100.0):
                out.append(("creux", piv_t, piv_p))
                direction, piv_t, piv_p = 1, ts, px
    return out, (direction, piv_t, piv_p)


def journal_moteur():
    """Journal du moteur, 2 fichiers les plus récents, DÉDOUBLONNÉS.
    Le moteur COPIE son journal à chaque --resume : sans dédoublonnage on compte
    l'histoire deux fois (incident mesuré le 21/09 : +46 $ au lieu de +25 $)."""
    import csv
    rows, seen = [], set()
    fichiers = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")),
                      key=os.path.getmtime)[-2:]
    for f in fichiers:
        try:
            with open(f, newline="", encoding="utf-8", errors="ignore") as fh:
                for r in csv.DictReader(fh):
                    k = tuple(r.items())
                    if k in seen:
                        continue
                    seen.add(k)
                    rows.append(r)
        except OSError:
            continue
    return rows


_JOURNAL = None


def journal():
    """Journal du moteur chargé UNE fois pour toutes les paires de la passe."""
    global _JOURNAL
    if _JOURNAL is None:
        _JOURNAL = journal_moteur()
    return _JOURNAL


def bilan_moteur(pair, rows, serie):
    """Ce que le moteur a RÉELLEMENT capté sur cet actif, et l'angle mort mesuré.
    MFE = meilleur prix atteint pendant la détention : ce qu'on a vu sans le prendre."""
    import datetime as _dt
    ev = [r for r in rows if r.get("pair") == pair]
    if not ev:
        return None
    ev.sort(key=lambda r: r.get("ts") or "")

    def T(s):
        return _dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
    path = [(T(s), p) for s, p in serie]
    realized = 0.0
    buys = sum(1 for r in ev if r.get("event") == "BUY")
    ventes = 0
    donnes = []
    ouverts = []
    for r in ev:
        e = r.get("event")
        if e == "BUY":
            ouverts.append(r)
        if e in EVENTS_VENTE:
            realized += float(r.get("pnl_usdt") or 0)
            if e == "SELL_PARTIAL":
                continue
            ventes += 1
            if ouverts:
                o = ouverts.pop(0)
                try:
                    t0, t1 = T(o["ts"]), T(r["ts"])
                    pi, po = float(o["price"]), float(r["price"])
                    seg = [p for (t, p) in path if t0 <= t <= t1]
                    mfe = max(seg) if seg else max(pi, po)
                    donnes.append((mfe / pi - 1) * 100 - (po / pi - 1) * 100)
                except Exception:
                    pass
    return {
        "realise_usd": round(realized, 2),
        "entrees": buys,
        "sorties": ventes,
        "mfe_donne_moy_pct": round(sum(donnes) / len(donnes), 1) if donnes else None,
        "mfe_donne_max_pct": round(max(donnes), 1) if donnes else None,
        "dernier_evt": ev[-1]["ts"],
    }


def specs_actif(pair):
    """Setups DÉCLARÉS pour cet actif (backtest/spec écrits, ex. EDEL_SPEC_V2).
    Ils existaient sur le disque et AUCUN code ne les lisait : orphelins. La fiche
    les porte désormais — le travail d'un actif ne peut plus se perdre."""
    import datetime as _dt
    base = pair.replace("USDT", "")
    out = []
    for pat in (f"*{base}*SETUP_BACKTEST*.json", f"*{base}*SPEC*.json", f"*{base}*SIMU*.json"):
        for f in sorted(glob.glob(os.path.join(RUNS, pat))):
            info = {"fichier": os.path.basename(f),
                    "date": _dt.datetime.fromtimestamp(
                        os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M")}
            try:
                d = json.load(open(f, encoding="utf-8"))
                for cherche in (("spec_antigravity", "resultat"), ("resultat",)):
                    noeud = d
                    for k in cherche:
                        noeud = (noeud or {}).get(k) if isinstance(noeud, dict) else None
                    if isinstance(noeud, dict) and noeud.get("net") is not None:
                        info["net"] = noeud.get("net")
                        info["n"] = noeud.get("n_complet")
                        info["wr"] = noeud.get("wr")
                        break
            except Exception:
                pass
            if info not in out:
                out.append(info)
    return out


def sources_contexte():
    """Le log continu + ses archives tournées, du plus ANCIEN au plus récent.
    La rotation ne garde que ~24 h dans le fichier vivant : lire le seul fichier
    vivant, c'est perdre l'histoire de l'actif (leçon 20/09 : après une rotation,
    le signal short BTC est resté aveugle ~10 h sans qu'aucun organe ne crie).
    Ici l'archive est lue, donc les cycles (pump/repli) survivent à la rotation.
    """
    archives = sorted(glob.glob(CROIS + ".*.gz"), reverse=True)  # .2.gz puis .1.gz
    for f in archives:
        yield f, True
    if os.path.exists(CROIS):
        yield CROIS, False


def _lignes(fichier, gz):
    if gz:
        import gzip
        with gzip.open(fichier, "rt", encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                yield line
    else:
        with open(fichier, encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                yield line


_PAIRES_VOULUES = set()


def load_points(pairs):
    global _PAIRES_VOULUES
    _PAIRES_VOULUES = set(pairs)
    dat = defaultdict(list)
    vus = set()
    for fichier, gz in sources_contexte():
        try:
            for line in _lignes(fichier, gz):
                _ingere(dat, vus, line)
        except (OSError, EOFError, ValueError):
            continue
    for p in dat:
        dat[p].sort(key=lambda x: x["ts"])
    return dat


def _ingere(dat, vus, line):
    try:
        d = json.loads(line)
    except Exception:
        return
    if d.get("pair") in _PAIRES_VOULUES:
        cle = (d.get("pair"), d.get("ts"), d.get("price"))
        if cle in vus:
            return
        vus.add(cle)
        dat[d["pair"]].append(d)


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
    # ── HISTORIQUE DES CYCLES DE L'ACTIF (21/09 : la fiche doit TOUT porter) ──
    serie = [(d["utc"], float(d["price"])) for d in (dat.get(pair) or []) if d.get("price")]
    pivots, courant = swings(serie)
    lines.append("")
    lines.append("## 🔁 HISTORIQUE DES CYCLES DE L'ACTIF (zigzag ≥ %.0f %%, log continu du moteur)"
                 % SEUIL_SWING_PCT)
    if serie:
        lines.append("")
        lines.append(f"_Fenêtre mesurée : du {serie[0][0]} au {serie[-1][0]} "
                     f"({len(serie)} points) — archives de rotation incluses._")
    if len(pivots) < 2:
        lines.append("")
        lines.append("_Pas encore deux retournements ≥ %.0f %% dans l'historique mesuré._"
                     % SEUIL_SWING_PCT)
    else:
        lines.append("")
        lines.append("| # | De | prix | Vers | prix | Amplitude | Durée |")
        lines.append("|---|---|---|---|---|---|---|")
        for i in range(len(pivots) - 1):
            k0, t0, p0 = pivots[i]
            k1, t1, p1 = pivots[i + 1]
            amp = (p1 / p0 - 1) * 100 if p0 else 0.0
            try:
                h = (datetime.datetime.strptime(t1, "%Y-%m-%dT%H:%M:%SZ")
                     - datetime.datetime.strptime(t0, "%Y-%m-%dT%H:%M:%SZ")).total_seconds() / 3600
                duree = f"{h:.0f} h ({h / 24:.1f} j)"
            except Exception:
                duree = "—"
            lines.append(f"| {i + 1} | {k0} {t0} | {p0} | {k1} {t1} | {p1} | "
                         f"{'🔺' if k1 == 'pic' else '🔻'} {amp:+.1f} % | {duree} |")
    if courant and serie:
        sens, c_t, c_p = courant
        px_now = serie[-1][1]
        lines.append("")
        if sens == 0:
            # Pas encore de retournement ≥ seuil dans la fenêtre : on DECRIT la
            # fenêtre telle qu'elle est (bas → maintenant) au lieu d'inventer un sens.
            t_min, p_min = min(serie, key=lambda x: x[1])
            amp = (px_now / p_min - 1) * 100 if p_min else 0.0
            lines.append(f"**Cycle en cours : pas encore de retournement ≥ {SEUIL_SWING_PCT:.0f} % "
                         f"dans la fenêtre** — du plus bas {t_min} à {p_min} → {px_now} "
                         f"= **{amp:+.1f} %**")
        else:
            # Le cycle en cours part du DERNIER pivot confirmé (pas de l'extrême
            # courant, sinon on comparerait le prix à lui-même).
            k_last, t_last, p_last = pivots[-1]
            amp = (px_now / p_last - 1) * 100 if p_last else 0.0
            lines.append(f"**Cycle EN COURS : {'HAUSSE' if sens > 0 else 'BAISSE'} depuis le "
                         f"{k_last} du {t_last} à {p_last} → {px_now} = **{amp:+.1f} %**** "
                         f"(extrême courant {c_p})")

    # ── CE QUE LE MOTEUR A CAPTÉ (et l'angle mort mesuré) ──
    bilan = bilan_moteur(pair, journal(), serie)
    lines.append("")
    lines.append("## 💰 CE QUE LE MOTEUR A CAPTÉ SUR CET ACTIF")
    lines.append("")
    if bilan:
        lines.append(f"- **Réalisé : {bilan['realise_usd']:+.2f} $** sur {bilan['entrees']} entrée(s) / "
                     f"{bilan['sorties']} sortie(s) — dernier événement {bilan['dernier_evt']}")
        if bilan["mfe_donne_moy_pct"] is not None:
            lines.append(f"- **MFE donné en moyenne : {bilan['mfe_donne_moy_pct']:+.1f} pts** par tour "
                         f"(pire tour : {bilan['mfe_donne_max_pct']:+.1f}) — le meilleur prix atteint "
                         f"pendant la détention, jamais encaissé")
    else:
        lines.append("_Aucun événement du moteur sur cet actif dans le journal._")

    # ── SETUPS DÉCLARÉS POUR CET ACTIF (orphelins branchés à la fiche) ──
    specs = specs_actif(pair)
    if specs:
        lines.append("")
        lines.append("## 🧪 SETUPS DÉCLARÉS (écrits pour CET actif — la fiche les branche)")
        lines.append("")
        for s in specs:
            extra = ""
            if s.get("net") is not None:
                extra = f" — backtest **{s['net']:+.2f} $** · n={s.get('n')} · WR={s.get('wr')} %"
            lines.append(f"- `{s['fichier']}` ({s['date']}){extra}")

    lines.append("")
    lines.append("_Règle : on compare les lignes entre elles (même heure de mesure = comparable). On ne supprime rien._")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"[OK] {pair} {utc} -> {len(rows)} ligne(s) | {verdict}")


if __name__ == "__main__":
    main()