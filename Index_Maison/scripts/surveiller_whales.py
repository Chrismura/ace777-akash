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
VUE = os.path.join(DATA, "whales_vue_ensemble.json")

MEMPOOL = "https://mempool.space/api"
SEUIL_GROS_BLOC_BTC = 1000.0
SEUIL_FRAG_BTC = 500.0
SEUIL_FRAG_BLOCS = 3


def get_json(url, timeout=12):
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


def charger_tx_par_adresse(portefeuilles):
    """1 appel API par adresse surveillée → {adresse: txs}. Pause anti-429."""
    out = {}
    for p in portefeuilles:
        addr = p.get("address")
        if not addr:
            continue
        try:
            out[addr] = get_json(f"{MEMPOOL}/address/{addr}/txs")
        except Exception:
            continue
        # 24/08 (Buffy) : pause entre adresses — la base est passe de 4 a ~29
        # adresses, une rafale sans pause declenchait des 429 (rate-limit
        # mempool.space ~1 req/s) et des adresses sautees silencieusement.
        time.sleep(0.3)
    return out


def scan_bloc_recent(tx_par_adresse, tip):
    """Analyse les tx récentes des adresses surveillées (whales.json).

    FIX 21/08 : l'ancien scan ne regardait que les 50 premières tx de 6 blocs
    (≈1,3 % d'un bloc de 4000 tx) avec un seuil ≥1000 BTC en une tx → il ne
    voyait jamais rien (0 détection depuis le 14/08), et whaleDir restait
    toujours neutral → la couleur régime restait figée en ORANGE.
    Nouvelle méthode : on interroge directement chaque adresse surveillée
    (4 appels API au lieu de 300+) et on filtre par récence (48 h).
    """
    portefeuilles, labels, types = charger_base()
    gros = []
    # bornes de récence : ~2 blocs/min → 48 h ≈ 5760 blocs
    borne_min = tip - 5760
    for addr, txs in tx_par_adresse.items():
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
    return gros


def vue_ensemble(tx_par_adresse, tip, portefeuilles):
    """VUE D'ENSEMBLE 24h (24/08, GO Christophe) : in / out / net par entité.

    Logique vulgarisée : un portefeuille ne fait que recevoir (entree) ou
    envoyer (sortie). On ignore les mouvements INTERNES (entre adresses
    surveillées — ex: Binance cold -> Binance hot) qui ne disent rien sur le
    marché. net = entrées - sorties vers l'extérieur.
      net > 0  -> les portefeuilles surveillés absorbent -> accumulation
      net < 0  -> ils relâchent vers le marché -> distribution
      net ~ 0  -> neutre
    Simplification assumée : une cible non surveillée est comptée « vers
    l'extérieur » (on ne distingue pas exchange/hot/inconnu hors base).
    """
    surveillees = set(tx_par_adresse.keys())
    entity_par_addr = {p["address"]: p.get("entity", "?") for p in portefeuilles}
    typo_par_addr = {p["address"]: p.get("type", "?") for p in portefeuilles}
    borne_min = tip - 2880  # 24 h ≈ 2880 blocs
    par_entite = {}

    for addr, txs in tx_par_adresse.items():
        in_b, out_b, n = 0.0, 0.0, 0
        internes = 0
        for tx in txs:
            statut = tx.get("status") or {}
            hauteur = statut.get("block_height")
            if hauteur is None or hauteur < borne_min:
                continue
            vins = [(vin.get("prevout") or {}).get("scriptpubkey_address") for vin in tx.get("vin", [])]
            est_source = addr in vins
            vouts = tx.get("vout", [])
            if est_source:
                # sortie : vouts qui ne reviennent pas a l'adresse elle-meme (hors change)
                externe = False
                for vout in vouts:
                    a = vout.get("scriptpubkey_address")
                    if not a or a == addr:
                        continue
                    if a in surveillees:
                        internes += 1
                    else:
                        externe = True
                        out_b += sats_to_btc(vout.get("value", 0))
                if externe or internes:
                    n += 1
            else:
                # entree : vouts vers l'adresse surveillee
                # SYMETRIE 24/08 : si TOUTES les entrees viennent d'adresses
                # surveillees (ex: Binance hot -> Binance cold), c'est un flux
                # INTERNE -> ignore du net (comme cote sortie deja fait).
                # Avant ce fix, les consolidations internes gonflaient le net
                # (Cold #2 affichait +28 951 BTC d'"accumulation" alors que
                # c'etait Binance qui deplacait ses propres fonds hot -> cold).
                vins_propres = [a for a in vins if a]
                tout_interne = bool(vins_propres) and all(a in surveillees for a in vins_propres)
                for vout in vouts:
                    if vout.get("scriptpubkey_address") == addr:
                        if tout_interne:
                            internes += 1
                        else:
                            in_b += sats_to_btc(vout.get("value", 0))
                            n += 1
        par_entite[addr] = {
            "label": None, "entity": entity_par_addr.get(addr, "?"),
            "type": typo_par_addr.get(addr, "?"),
            "in_btc": round(in_b, 2), "out_btc": round(out_b, 2),
            "net_btc": round(in_b - out_b, 2), "n_mouvements": n,
            "n_internes": internes,
        }

    # labels (apres coup, via charger_base)
    portefeuilles_b, labels, types = charger_base()
    for addr, d in par_entite.items():
        d["label"] = labels.get(addr, "inconnu")

    in_total = sum(d["in_btc"] for d in par_entite.values())
    out_total = sum(d["out_btc"] for d in par_entite.values())
    net = round(in_total - out_total, 2)
    if net > 25:
        lecture = "ACCUMULATION"
    elif net < -25:
        lecture = "DISTRIBUTION"
    else:
        lecture = "NEUTRE"
    return {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "fenetre": "24h",
        "total": {"in_btc": round(in_total, 2), "out_btc": round(out_total, 2),
                   "net_btc": net, "lecture": lecture},
        "par_entite": sorted(par_entite.values(), key=lambda d: -abs(d["net_btc"])),
    }


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
        tip = get_json(f"{MEMPOOL}/blocks/tip/height")
    except Exception as e:
        print(f"[{ts}] ERREUR tip: {e}")
        return
    # UNE seule passe d'appels API, partagée alertes + vue d'ensemble (anti-boucle)
    tx_par_adresse = charger_tx_par_adresse(portefeuilles)
    try:
        gros = scan_bloc_recent(tx_par_adresse, tip)
    except Exception as e:
        print(f"[{ts}] ERREUR scan: {e}")
        return
    # vue d'ensemble 24h (24/08, GO Christophe)
    vue = vue_ensemble(tx_par_adresse, tip, portefeuilles)
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
    with open(VUE, "w", encoding="utf-8") as f:
        json.dump(vue, f, ensure_ascii=False, indent=2)
    # historique append-only des alertes
    for g in gros:
        with open(HISTO, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": ts, **g}, ensure_ascii=False) + "\n")
    for a in alerts_frag:
        with open(HISTO, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": ts, **a}, ensure_ascii=False) + "\n")
    t = vue["total"]
    print(f"[{ts}] Scan OK — tip={tip}, gros blocs={len(gros)}, fragmentations={len(alerts_frag)}")
    print(f"  VUE 24h: in {t['in_btc']:,.0f} / out {t['out_btc']:,.0f} / net {t['net_btc']:+,.0f} BTC — {t['lecture']}")
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
