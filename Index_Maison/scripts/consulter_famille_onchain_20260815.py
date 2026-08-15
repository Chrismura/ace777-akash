#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — design branchement ONCHAIN (baleines BTC) vers Cortana + Ada.
Avis seulement, rien n'est appliqué."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_ONCHAIN_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — BRANCHEMENT ONCHAIN (BALEINES BTC) → CORTANA + ADA

=== ÉTAT ACTUEL (vérifié) ===
- Module `surveiller_whales.py` : scan mempool.space toutes les 5 min (daemon /tmp/lancer_whales.py,
  PID vivant depuis 14/08 21:47Z). Détecte : GROS_BLOC (tx ≥1000 BTC) + FRAGMENTATION
  (cumul ≥500 BTC depuis la même source sur ≤3 blocs — attrape les baleines qui splittent).
  Croise avec whales.json (4 adresses vérifiées double : Binance hot/cold, Bitfinex cold, Genesis/Satoshi).
  Écrit : data/whales_scan_latest.json + data/whales_mouvements.jsonl (append-only).
- PROBLÈME 1 : rien n'injecte ces données dans le contexte. Cortana lit live.json (LEXIQUE +
  CONTEXT_KEYS dans cortana_analyse.py) — elle a whaleN/whaleUsd MAIS c'est un AUTRE proxy
  (gros prints aggTrades ≥500k$), pas le scan onchain réel. Ada (ada_gardienne.py) calcule
  ses pressions (bleed/storm/reversal) depuis live.json — elle ne voit pas les mouvements onchain.
- PROBLÈME 2 : le lanceur est un daemon /tmp (double-fork) → NE SURVIT PAS au reboot du Mac
  (contrairement aux plists launchd comme la discipline 07h15).

=== DESIGN PROPOSÉ (à affiner) ===
1. PONT `pont_onchain.py` : lit whales_scan_latest.json + whales_mouvements.jsonl →
   injecte des clés onchain dans thermo/live.json (fichier déjà lu par Cortana ET Ada) :
   - whaleBlocsN (nb gros blocs 24h/scan récent), whaleBlocsBtc (Σ BTC)
   - whaleFragN, whaleFragBtc
   - whaleDir ("inflow"/"outflow"/"neutral" si provenance/étiquette exchange connue)
   - whaleAlerte (bool + texte si ≥1 gros bloc ou fragmentation récente)
   Écriture ATOMIQUE, kill-switch respecté, idempotent, ne touche PAS aux autres clés.
2. CORTANA : déclarer les nouvelles clés dans LEXIQUE + CONTEXT_KEYS (cortana_analyse.py)
   → elle les reçoit dans son contexte d'analyse (elle pourra dire « gros bloc 1200 BTC
   depuis Binance → direction X »).
3. ADA : lire les clés onchain → ajuster les pressions (ex. sortie massive d'exchange =
   pression vendeuse → voilure réduite ; inflow = accumulation → voilure stable).
   Reste dans sa philosophie : voilure CONTINUE (pas de saut IF/THEN brutal), elle ne
   touche jamais au moteur.
4. PÉRENNISER : remplacer le daemon /tmp par une plist launchd (StartInterval=300) →
   survit aux reboots, visible dans launchctl, réversible proprement.

=== VOTRE MISSION ===
1. Le design du pont est-il le bon (injecter dans live.json plutôt qu'un fichier dédié) ?
   Risques de saturation/confusion avec le proxy aggTrades existant (whaleN/whaleUsd) ?
2. Les clés proposées sont-elles les bonnes ? Manque-t-il quelque chose (ex. cumulative
   24h, écart au seuil, étiquettes source) ?
3. ADA : comment intégrer l'onchain SANS casser sa philosophie (voilure continue,
   jamais de blocage, seuil X relatif auto-appris) ? Quelle pondération raisonnable ?
4. CORTANA : à 44% de justesse, l'ajout d'un indice onchain améliore-t-il ou brouille-t-il
   son signal ? (Elle est déjà mauvaise sur funding/fearGreed — indices bruités.)

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur le design onchain)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
SYNTHÈSE (5 lignes max) : design retenu + pondération Ada + mode d'ajout Cortana.

Factuel, concis, français. Info manquante → « information insuffisante ». Vous DONNEZ UN
AVIS, ne touchez à rien."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for model in MODELS:
        out_file = os.path.join(OUT, f"AVIS_{model}.md")
        if os.path.exists(out_file):
            print(f"[SKIP] {model} déjà répondu")
            continue
        try:
            content, provider, dur = ask(model)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# AVIS {model} (provider {provider}, {dur}s)\n\n{content}\n")
            print(f"[OK] {model} ({dur}s)")
        except Exception as e:
            print(f"[ERREUR] {model}: {e}")


if __name__ == "__main__":
    main()
