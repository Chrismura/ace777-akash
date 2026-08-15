#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — « graver la pépite » CPFP dans le prompt canon de Cortana.
Option A : section permanente dans PROMPT_MASTER_ANALYSTE.md (injectée à chaque analyse).
Option B : brancher la couche connaissance en auto dans contexte_systeme().
Avis seulement, rien n'est appliqué sans GO Christophe (déjà donné) + verdict famille."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_GRAVER_PEPITE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — CHANTIER « GRAVER LA PÉPITE » ACE777

=== LA DÉCOUVERTE (pépite de Christophe, validée famille ce jour : onchain v2 CPFP) ===
Les baleines peuvent déplacer des milliers de BTC SANS créer une seule transaction ≥1000 BTC :
1. LE BILLET (UTXO) : un UTXO est INDIVISIBLE — on dépense le billet entier et on reçoit
   le reste en « monnaie rendue » (change).
2. LE CAMOUFLAGE : éclatement en un ARBRE de milliers de micro-transactions de POUSSIÈRE
   (dust) à frais quasi nuls, qui dorment invisibles au fond de la mempool.
3. LE DÉCLENCHEUR (CPFP = Child Pays For Parent) : une transaction « ENFANT » à frais
   astronomiques, dépendant d'une sortie de l'arbre de poussière.
4. L'EXÉCUTION : le mineur est ÉCONOMIQUEMENT OBLIGÉ de valider tout l'arbre parent
   (même à frais zéro) pour encaisser la prime de l'enfant. Le bloc se règle d'un coup.
5. L'EXPULSION : ce bloc massif expulse les transactions des petits porteurs.
SIGNAL DE DÉTECTION : les seuils fixes sont aveugles → z-score adaptatif + signature CPFP
par frais (inaltérable : le frais astronomique EST le mécanisme).

=== LE PROBLÈME IDENTIFIÉ (limite du système) ===
Cortana (l'analyste) n'a AUCUNE mémoire entre deux appels au hub (stateless). Aujourd'hui
elle connaît la pépite parce que le superviseur l'a injectée dans la question. DEMAIN,
sans injection, elle a OUBLIÉ. La conversation ne survit pas entre les appels.

=== CE QUI EXISTE DÉJÀ ===
- PROMPT_MASTER_ANALYSTE.md (92 lignes) : le prompt canon de Cortana, LU À CHAQUE analyse
  (fichier canon dans le vault Obsidian).
- contexte_systeme() dans cortana_analyse.py : contexte vivant injecté à chaque analyse
  (système qui tourne, score de justesse, derniers HIT/MISS) — c'est la boucle d'apprentissage.
- Couche connaissance : CONNAISSANCE_PROJETS.json + injecter_connaissance.py (pilote Canton
  OK, verdict famille GO-AVEC-RÉSERVE 85/78) — MAIS PAS BRANCHÉE en automatique (outil manuel).
- Détection onchain v2 (detecter_cpfp.py) : tourne en observation, alimente la synthèse onchain.

=== LE DESIGN PROPOSÉ (2 options, à affiner) ===
OPTION A — graver dans le prompt canon (rapide, permanent) :
Ajouter une section « Connaissance onchain — le camouflage UTXO/CPFP » dans
PROMPT_MASTER_ANALYSTE.md (le mécanisme en 5 points + le principe de détection).
Résultat : injectée à CHAQUE analyse, pour toujours. Réversible (retrait de la section).

OPTION B — brancher la couche connaissance en auto (puissant, général) :
Modifier contexte_systeme() pour qu'il injecte automatiquement les fiches pertinentes de
CONNAISSANCE_PROJETS.json (ex. le sujet = le projet) + les leçons CPFP à venir.
Résultat : tout ce qu'on apprend se grave tout seul, sans action manuelle.

QUESTION 1 : Option A seule, B seule, ou A PUIS B (ordre recommandé par Buffy) ?
QUESTION 2 : Pour A, la section doit-elle être : (a) le mécanisme complet en 5 points,
ou (b) une version condensée (le principe + le signal de détection) pour ne pas alourdir
le prompt de base ?
QUESTION 3 : Risques d'une section permanente dans le prompt canon (dérive, longueur,
confusion avec les données reçues) ? Comment les atténuer ?
QUESTION 4 : Pour B, comment éviter que l'injection auto brouille Cortana à 44% de
justesse (infobésité) ? Contrainte : synthèse pré-mâchée, pas de chiffres bruts.

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur graver la pépite, A puis B)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)"""

PROVIDERS = [
    {"model": "gemini", "nom": "gemini"},
    {"model": "nvidia", "nom": "nvidia"},
]


def appeler(provider, nom):
    payload = json.dumps({
        "model": provider["model"],
        "messages": [
            {"role": "system", "content": "Tu es un membre senior de la famille ACE777 (conseil d'architecture). Avis factuel, concis, en français."},
            {"role": "user", "content": BRIEF},
        ],
        "max_tokens": 2500, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=180) as resp:
            d = json.loads(resp.read().decode())
        content = d["choices"][0]["message"]["content"]
        chemin = os.path.join(OUT, f"AVIS_{nom}.md")
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(f"# Avis {nom} — graver la pépite (provider {d.get('provider','?')}, {round(time.time()-t0,1)}s)\n\n{content}\n")
        print(f"[OK] {nom} a répondu ({round(time.time()-t0,1)}s)")
    except Exception as e:
        print(f"[ERREUR] {nom}: {e}")


if __name__ == "__main__":
    print("Consultation famille — graver la pépite CPFP...")
    for p in PROVIDERS:
        appeler(p, p["nom"])
    print("Terminé. Avis dans", OUT)
