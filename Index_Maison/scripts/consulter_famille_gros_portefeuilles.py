#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter la FAMILLE (flotille) : recherche pour construire une base de donnees
des PLUS GROS PORTEFEUILLES BTC a surveiller (mouvements de baleines).

Contexte utilisateur : il veut voir tous les gros mouvements du BTC. Les baleines
modernes sont malines : elles fragmentent, elles evitent les gros mouvements
flagrants -> seuil de surveillance = 100 M$ (et non 1000 BTC flagrants).
But : se constituer une base de portefeuilles/adresses a surveiller (whale watch)."""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "RECHERCHE_FAMILLE_GROS_PORTEFEUILLES_20260814")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 14/08/2026) :

Christophe veut VOIR TOUS LES GROS MOUVEMENTS DU BTC (mouvements de baleines,
transferts majeurs, entrees/sorties d'exchanges). Son intuition : les grosses
baleines sont devenues malines — elles fragmentent leurs transactions pour
eviter les alertes flagrantes. Un seuil a 1000 BTC (≈ 63 M$ aujourd'hui) ou
100 M$ est plus pertinent qu'un seuil grossier.

OBJECTIF DE LA RECHERCHE (pour la flotille) :
On veut construire une BASE DE DONNEES de portefeuilles/adresses BTC a surveiller
(whale watch), croisable avec mempool.space (API gratuite, sans cle, deja testee :
/api/address/<addr>, /api/mempool/recent, /api/v1/fees). La base alimentera :
- un module de surveillance des gros mouvements (entree/sortie d'exchange etiquete)
- ADA (tendances + avertissements de gros mouvements)
- le cockpit (panneau onchain)

QUESTIONS (repondez brievement mais precisement) :
1) QUELLES ADRESSES/ENTITES sont les plus importantes a suivre pour capter les
   gros mouvements BTC ? Donnez des exemples CONCRETS : adresses connues des gros
   exchanges (Binance hot/cold, Coinbase, Kraken, Bitfinex, OKX...), ETF (BlackRock
   IBIT, Fidelity FBTC, Grayscale GBTC...), gros holders historiques (adresses
   Sats, mineurs), gouvernements (US, DE, UK...), fonds (MicroStrategy, Tether...).
   Pour chaque : le NOM + POURQUOI c'est important de le surveiller.
2) OU trouver ces adresses de facon fiable et GRATUITE (listes publiques, explorers,
   sources documentees) — sans cles payantes ?
3) Quelle METHODE pour detecter un mouvement significatif : entree exchange (vente
   probable) vs sortie exchange (accumulation) vs transfert interne ? Comment
   estimer la fragmentation (une grosse entite qui split en 10-50 tx) ?
4) Quel seuil recommandez-vous (BTC / USD) pour 'gros mouvement' en 2026, sachant
   que Christophe propose 100 M$ ?
5) Recommandation d'architecture : base locale simple (json/csv) suffit-elle pour
   demarrer ? Comment la faire evoluver proprement ?

Contrainte : reponses libres, vous etes la flotille qui s'amuse et cherche — mais
restez FACTUEL : ne pas inventer d'adresses, indiquer clairement quand une adresse
doit etre VERIFIEE avant d'entrer dans la base (anti-hallucination)."""

MODELS = ["gemini", "grok", "nvidia", "deepseek", "juge", "ultra", "oss20"]

def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 1800, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)

def main():
    results = {}
    for m in MODELS:
        try:
            content, provider, secs = ask(m)
            results[m] = content
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} -> {f} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)
    print(f"\n=== SYNTHESE ===")
    print(f"Consultation terminee : {len(results)}/{len(MODELS)} avis dans {OUT}")

if __name__ == "__main__":
    main()
