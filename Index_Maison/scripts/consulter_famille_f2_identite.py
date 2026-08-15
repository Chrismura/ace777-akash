#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter la FAMILLE sur F2 — Carte d'identité ACE777 + prompts canon (15/08/2026).

Protocole §C : #9 Multi-Perspective + #5 Confidence-Weighted + demandes d'améliorations.
Contenu injecté intégralement (#6 Context Injection).
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_F2_IDENTITE_20260815")
os.makedirs(OUT, exist_ok=True)

ID_ROOT = os.path.join(os.path.dirname(ROOT), "identity")


def rd(rel):
    p = os.path.join(ID_ROOT, rel)
    try:
        return open(p, encoding="utf-8").read()
    except Exception as e:
        return f"(lecture impossible: {e})"


CORE = rd("ace777_core.md")
P_ADA = rd("prompts/ada.md")
P_CORTANA = rd("prompts/cortana.md")
P_QWEN = rd("prompts/qwen.md")

BRIEF = f"""CONTEXTE (superviseur Buffy, 15/08/2026) — VALIDER LA CARTE D'IDENTITÉ ACE777 (F2)

=== LE SYSTÈME ===
ACE777 (Mac Air 8 Go) = cockpit de trading + équipe d'acteurs IA (Ada=horizon/voilure,
Cortana=cerveau/dashboard court terme, Qwen=apprentie junior, MiroFish=simulation, hub=aiguilleur).
Contraintes non négociables : champion intouchable (C1) · 0 LLM dans le chemin d'ordre (C2) ·
1 GO=1 vol humain (C3) · CSV=vérité (C4) · 8 Go (C5) · 1 place/info (C6).

=== BUT ===
Une carte d'identité unique + 1 prompt canon par acteur, injectés au boot, pour que chaque
acteur « incarne » ACE777 dès la première seconde (fini les personas génériques/contradictoires).
Ces fichiers sont DOCUMENTATION/PROMPTS : ils ne touchent ni au moteur ni aux ordres.

=== LIVRABLES À JUGER (contenu intégral) ===

--- ace777_core.md (carte d'identité) ---
{CORE}

--- prompts/ada.md ---
{P_ADA}

--- prompts/cortana.md ---
{P_CORTANA}

--- prompts/qwen.md ---
{P_QWEN}

=== QUESTIONS ===
1) La carte d'identité est-elle FIDÈLE à l'architecture ACE777 (carrosserie/moteur/philosophie/
   stratégie) ? Y a-t-il une erreur factuelle, un oubli, ou un élément qui prête à confusion ?
2) Les 3 prompts sont-ils COHÉRENTS entre eux (pas de contradiction de rôle) et respectent-ils
   C2/C3 (lecture seule, aucune autonomie, propose jamais ne décide) ?
3) La carte est-elle assez COMPACTE pour être injectée au boot sans saturer le contexte d'un
   petit modèle local (Qwen 4b) ? Sinon, proposez la coupe / la version compacte.
4) Pour chaque fichier, proposez 1-3 AMÉLIORATIONS concrètes (précision, harmonie, traçabilité).

=== FORMAT DE RÉPONSE EXIGÉ ===
VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (global)
CONFIANCE : 0-100 %
Pour chaque fichier (core/ada/cortana/qwen) : 1 ligne de verdict + la 1ʳᵉ amélioration.
HYPOTHÈSES / CE QUI CHANGERAIT L'AVIS : en 2-3 lignes.
Puis : AMÉLIORATIONS (classées, GO-sized).

Répondez factuel, concis, en français. Si une info manque pour trancher, dites
« information insuffisante » au lieu d'inventer. Vous DONNEZ UN AVIS, vous ne modifiez rien."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2200, "temperature": 0.3,
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
