#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter la FAMILLE sur les FONDATIONS DES ACTEURS (15/08/2026).

Protocole §C : #9 Multi-Perspective (technique / impact / risque) +
#5 Confidence-Weighted (verdict + confiance 0-100% + hypothèses + ce qui
changerait l'avis) + demandes d'AMÉLIORATIONS (coutume stacking functions).
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_FONDATIONS_ACTEURS_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — VALIDER LES FONDATIONS DE L'ÉQUIPE D'ACTEURS ACE777

=== LE SYSTÈME ===
ACE777 (Mac Air 8 Go) = cockpit de trading + 4 acteurs IA :
- Ada  : gardienne horizon (saison, bascule de tendance, voilure) — déjà construit, lecture seule
- Cortana : cerveau/dashboard + analyste court terme (voix Rust + scripts Python via hub)
- Qwen : apprentie junior locale (Ollama), propose jamais ne décide — en pause actuellement
- MiroFish : simulation sociale multi-agents (scénarios, jamais d'exécution) — en pause
- Hub (prise-ia) : aiguilleur unique + rotation auto des modèles (routing.json)

Contraintes non négociables : champion genesis intouchable · jamais de LLM dans la boucle
d'ordre (C2/C3) · 8 Go · 1 chantier = 1 GO humain · vérité = CSV/fichiers, pas le récit.

=== CONSTAT (preuves code vérifiées) ===
1. La justesse (score_justesse.py) note TOUTES les analyses contre le prix BTC uniquement :
   une analyse de funding/fearGreed est jugée HIT/MISS selon que le BTC a monté/descendu 24h
   plus tard. L'indice analysé n'est jamais vérifié contre lui-même. NEUTRE non noté
   (échappatoire). Seuil de victoire trop lâche (+0,05 %). Score actuel 57,1 % (32/56 sur 93).
2. Cortana a 3 cerveaux voix parallèles et incohérents : hub→mission→puter-grok (402 mort),
   Claude sonnet-5, Ollama qwen2.5:3b (obsolète). Le prompt voix (persona.rs) dit encore
   « peut exécuter des ordres Binance dictés à la voix » alors qu'elle n'est autorisée à RIEN.
3. Cortana (analyste) ne lit que les indices BTC ; elle ne couvre ni les fills ACE ni Hulk.
4. Aucun acteur n'incarne ACE777 au démarrage (pas de carte d'identité commune).

=== LES 5 FONDATIONS PROPOSÉES ===
F1 — Réparer la justesse : juger chaque indice contre SA propre évolution (pas tout vs BTC),
     noter aussi le NEUTRE, seuil réaliste (~0,3 %), corriger le bug « dernière analyse ».
     Lecture seule, zéro impact trading.
F2 — Carte d'identité ACE777 (1 fichier canon : carrosserie/moteur/philosophie/stratégie)
     + 1 prompt canon par acteur (Ada/Cortana/Qwen) injecté au boot. Documentation + prompts.
F3 — Cortana = dashboard : étendre cortana_analyse.py aux fills ACE (runs CSV) + Hulk (paper),
     et unifier la voix sur le hub. Lecture seule, zéro ordre.
F4 — Un seul aiguilleur : le Rust (brain.rs) n'appelle QUE le hub (rotation déjà dedans),
     supprimer sa logique parallèle Gemini/Ollama ; aligner app.toml. Repli hors-ligne conservé.
F5 — Nettoyer le prompt voix : retirer « exécute des ordres », greffer la carte d'identité
     et le rôle dashboard. L'autonomie viendra plus tard (garde-fous déterministes C7), pas ici.

=== VOTRE MISSION (format EXACT exigé) ===
Pour CHACUNE des 5 fondations (F1 à F5), analysez sous 4 angles :
  • Technique (faisabilité sur 8 Go, stdlib, risques de casser un consommateur)
  • Impact (ce que ça apporte au cockpit / à l'équipe)
  • Risque/Sécurité (respecte-t-elle C2/C3, le champion intouchable, le GO humain ?)
  • Ordre de priorité (que faire en premier, que reporter)
Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (réserve à préciser)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : les 2-3 hypothèses sous-jacentes
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes pour renforcer la fondation (ou « aucune »)

Terminez par une SYNTHÈSE (5 lignes max) : l'ordre d'exécution recommandé + le risque n°1.

Répondez factuel, concis, en français. Si une information manque pour trancher, dites
« information insuffisante » au lieu d'inventer. Ne touchez à rien : vous DONNEZ UN AVIS."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2600, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        try:
            content, provider, secs = ask(m)
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)


if __name__ == "__main__":
    main()
