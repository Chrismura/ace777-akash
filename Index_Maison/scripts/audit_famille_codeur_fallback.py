#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — CORRECTION CHAINE CODEUR (fallback inferx-coder mort).

Contexte (demande Christophe 14/08) : puter-grok (grok-4.3) est le codeur
principal du task code.ia mais a HALLUCINE 2 livrables sur 3 (SPEC v1, v2).
Le fallback officiel inferx-coder (Qwen3-Coder-Next) repond 502 (mort).
Test comparatif reel du superviseur : mistral codestral-latest = joignable,
3/3 lignes exactes sur la tache de controle anti-hallucination.

Question : corriger la chaine code.ia — remplacer le fallback mort par
codestral (dispo, gratuit essai, specialise code) — et en parallele rechercher
un meilleur modele codeur gratuit. La famille tranche la correction.

Chaque membre : (1) verdict, (2) la nouvelle chaine proposee (puter-grok ->
codestral -> gemini) est-elle la bonne ?, (3) faut-il promouvoir codestral en
PRINCIPAL (remplacer puter-grok) vu ses hallucinations ?, (4) reserves, (5)
prochaine etape (re-test SPEC v3 avec la chaine corrigee).
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
OUT = os.path.join(ROOT, "Index_Maison", "AUDIT_CODEUR_FALLBACK_2026-08-14")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

# CLAUSE PERMANENTE (gravée 16/08 par Christophe — applicable à TOUS les prompts).
CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CONTEXTE = """\
CORRECTION DE LA CHAINE CODEUR — le codeur principal hallucine, le fallback
est mort. A toi de trancher la correction (et la recherche d'un meilleur
codeur gratuit se fait en parallele par le superviseur).

================
FAITS VERIFIES (Buffy, pas un recit)
================
1. HALLUCINATIONS du codeur principal : puter-grok (grok-4.3, task code.ia)
   a livre 2 patches de FICTION sur 3 (SPEC v1 : $book, calc_entry invente ;
   SPEC v2 : "bid" au lieu de "bidPrice"). Rejetes par le superviseur. La
   SPEC v3 (diff EXACT imposé) a enfin produit un livrable conforme — mais
   c'est le superviseur qui a du fournir les lignes exactes, pas le codeur.
2. FALLBACK MORT : inferx-coder (Qwen3-Coder-Next, 2e codeur specialiste du
   task code.ia) repond 502 Bad Gateway (test force, 14/08). En pratique tout
   le task retombe sur puter-grok.
3. TEST COMPARATIF reel (14/08, tache de controle : recopier 3 lignes bash
   exactes, le piege qui fait halluciner puter-grok) :
   - mistral codestral-latest : 3/3 lignes exactes, JOIGNABLE, enabled:true
     mais 0 appel/24h (jamais utilise, pas branche sur code.ia)
   - puter-grok : 3/3, joignable
   - gemini : 3/3, joignable
   - inferx-coder : 502 INJOIGNABLE
4. ROUTING ACTUEL (routing.json) : code.ia -> provider: puter-grok,
   fallback: inferx-coder, secondary: gemini.
5. CONTRAINTES : tout passe par le hub (C9, jamais de local) · budget 194/624
   (reste 430) · codestral = essai gratuit Mistral · clause permanente
   Christophe : prouver la meilleure logique.

================
TA MISSION (5 reponses nettes)
================
1. VERDICT : GO / GO AVEC RESERVES / NON sur la correction de la chaine
   code.ia (remplacer le fallback mort inferx-coder).
2. NOUVELLE CHAINE : puter-grok -> codestral -> gemini (remplacement simple
   du fallback) : valide ? Ou autre ordre ?
3. FAUT-IL PROMOUVOIR codestral en PRINCIPAL (devant puter-grok) vu les
   hallucinations repetees de grok-4.3 ? Tranche avec critere objectif.
4. RESERVES (GO-sized) avant modification du routing.
5. PROCHAINE ETAPE : re-soumettre la SPEC v3 au codeur via la chaine corrigee,
   puis appliquer + re-scellement + retest ? Confirme le circuit.
Reponds en francais, court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system + "\n\n" + CLAUSE},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1300,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}"


if __name__ == "__main__":
    import sys
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    print(f"=== AUDIT FAMILLE — CORRECTION CHAINE CODEUR ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
