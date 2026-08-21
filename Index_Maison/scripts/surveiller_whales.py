#!/usr/bin/env python3
"""
SURVEILLER_WHALES.py — surveillance des gros mouvements BTC (proxy onchain gratuit).

Principe : mempool.space (API gratuite sans cle). Deux signaux :
  1. GROS BLOC : une transaction >= seuil_gros_bloc_btc (defaut 1000 BTC)
  2. FRAGMENTATION : cumul >= seuil_fragmentation_btc (defaut 500 BTC) emis
     par la MEME source en < seuil_fragmentation_blocs (defaut 3) blocs
     -> attrape les baleines qui splittent (les malins font des petits mouvements)

Croise avec Index_Maison/data/whales.json (portefeuilles etiquetes).
Ecrit : Index_Maison/data/whales_scan_latest.json (dernier scan)
        Index_Maison/data/whales_mouvements.jsonl (historique append-only)
Usage : python3 surveiller_whales.py [--once] [--loop N]
        --once : un seul passage (pour cron / test)
        --loop N : boucle N passages (defaut: 1)
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
WHALES = os.path.join(DATA, "whales.json")
SCAN = os.path.join(DATA, "whales_scan_latest.json")
HISTO = os.path.join(DATA, "whales_mouvements.jsonl")

MEMPOOL = "https://mempool.space/api"
SEUIL_GROS_BLOC_BTC = 1000.0
SEUIL_FRAG_BTC = 500.0
SEUIL_FRAG_BLOCS = 3


def get_json(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "ACE777-whales/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def sats_to_btc(sats):
    return sats / 1e8


def charger_base():
    if not os.path.exists(WHALES):
        return [], {}
    d = json.load(open(WHALES, encoding="utf-8"))
    portefeuilles = d.get("portefeuilles", [])
    # index adresse -> label
    labels = {p["address"]: p["label"] for p in portefeuilles}
    # index adresse -> type
    types = {p["address"]: p.get("type", "inconnu") for p in portefeuilles}
    return portefeuilles, labels, types


def scan_bloc_recent(dernier_hauteur):
    """Analyse les tx récentes des adresses surveillées (whales.json).

    FIX 21/08 : l'ancien scan ne regardait que les 50 premières tx de 6 blocs
    (≈1,3 % d'un bloc de 4000 tx) avec un seuil ≥1000 BTC en une tx → il ne
    voyait jamais rien (0 détection depuis le 14/08), et whaleDir restait
    toujours neutral → la couleur régime restait figée en ORANGE.
    Nouvelle méthode : on interroge directement chaque adresse surveillée
    (4 appels API au lieu de 300+) et on filtre par récence (48 h).
    """
    try:
        tip = get_json(f"{MEMPOOL}/blocks/tip/height")
    except Exception:
        return [], 0
    portefeuilles, labels, types = charger_base()
    gros = []
    # bornes de récence : ~2 blocs/min → 48 h ≈ 5760 blocs
    borne_min = tip - 5760
    for p in portefeuilles:
        addr = p.get("address")
        if not addr:
            continue
        try:
            txs = get_json(f"{MEMPOOL}/address/{addr}/txs")
        except Exception:
            continue
        for tx in txs:
            statut = tx.get("status") or {}
            hauteur = statut.get("block_height")
            if hauteur is None or hauteur < borne_min:
                continue
            out_total = sum(sats_to_btc(v.get("value", 0)) for v in tx.get("vout", []))
            if out_total < SEUIL_GROS_BLOC_BTC:
                continue
            # provenance (vins) + cibles (vouts significatifs)
            sources = set()
            for vin in tx.get("vin", []):
                a = (vin.get("prevout") or {}).get("scriptpubkey_address")
                if a:
                    sources.add(a)
            cibles = []
            for vout in tx.get("vout", []):
                a = vout.get("scriptpubkey_address")
                if a and sats_to_btc(vout.get("value", 0)) >= SEUIL_GROS_BLOC_BTC * 0.1:
                    cibles.append({"adresse": a, "btc": round(sats_to_btc(vout.get("value", 0)), 2)})
            gros.append({
                "type": "GROS_BLOC",
                "txid": tx.get("txid"),
                "hauteur": hauteur,
                "btc": round(out_total, 2),
                "sources": list(sources)[:5],
                "cibles": cibles[:5],
                "adresse_surveillee": addr,
                "label": labels.get(addr, "inconnu"),
            })
    return gros, tip


def fragmenter(mouvements_recents, dernier_bloc_traite):
    """Detecte la fragmentation : cumul >= seuil par source sur les 3 derniers blocs."""
    par_source = {}
    for m in mouvements_recents:
        if m["type"] != "GROS_BLOC":
            continue
        for s in m["sources"]:
            par_source[s] = par_source.get(s, 0) + m["btc"]
    alerts = []
    for src, cumul in par_source.items():
        if cumul >= SEUIL_FRAG_BTC and cumul < SEUIL_GROS_BLOC_BTC:
            alerts.append({
                "type": "FRAGMENTATION",
                "source": src,
                "btc": round(cumul, 2),
                "sur_blocs": dernier_bloc_traite,
            })
    return alerts


def scanner(once=True):
    portefeuilles, labels, types = charger_base()
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    try:
        gros, tip = scan_bloc_recent(0)
    except Exception as e:
        print(f"[{ts}] ERREUR scan: {e}")
        return
    # etiquetage
    for g in gros:
        g["sources_label"] = [labels.get(s, "inconnu") for s in g["sources"]]
        g["sources_type"] = [types.get(s, "inconnu") for s in g["sources"]]
    # fragmentation (a partir des gros blocs du scan)
    alerts_frag = fragmenter(gros, tip)
    resultat = {
        "ts": ts,
        "hauteur_tip": tip,
        "gros_blocs": gros,
        "fragmentations": alerts_frag,
        "nb_surveilles": len(portefeuilles),
    }
    os.makedirs(DATA, exist_ok=True)
    with open(SCAN, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=2)
    # historique append-only des alertes
    for g in gros:
        with open(HISTO, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": ts, **g}, ensure_ascii=False) + "\n")
    for a in alerts_frag:
        with open(HISTO, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": ts, **a}, ensure_ascii=False) + "\n")
    print(f"[{ts}] Scan OK — tip={tip}, gros blocs={len(gros)}, fragmentations={len(alerts_frag)}")
    for g in gros:
        print(f"  GROS_BLOC {g['btc']} BTC (hauteur {g['hauteur']}) src={g['sources_label']} -> {g['cibles'][:2]}")
    for a in alerts_frag:
        print(f"  FRAGMENTATION {a['btc']} BTC depuis {a['source'][:20]}...")
    return resultat


if __name__ == "__main__":
    once = "--once" in sys.argv
    loop = 1
    if "--loop" in sys.argv:
        i = sys.argv.index("--loop")
        loop = int(sys.argv[i + 1])
    for _ in range(loop):
        scanner(once=once)
        if loop > 1 and _ < loop - 1:
            time.sleep(60)
