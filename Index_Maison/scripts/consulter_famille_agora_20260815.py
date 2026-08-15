#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — design « AGORA » : canalisation de la connaissance ACE777.
Place centrale (CONNAISSANCE_PROJETS.json) + 4 portes d'entrée + 2 langues de sortie
(Cortana=texte, Ada=chiffres) + boucle des leçons HIT/MISS.
Avis seulement, rien n'est appliqué sans GO Christophe (déjà donné) + verdict famille."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_AGORA_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026 soir) — DESIGN « AGORA » : canaliser la connaissance ACE777

=== L'IDÉE DE CHRISTOPHE ===
Un système « agora » : une place centrale où toute la connaissance converge, puis se
diffuse vers les bons acteurs. Méthodologie LÉGÈRE et PERFORMANTE (pas de base de
données, pas de plomberie lourde — on est artisanal, notre richesse = bonne pratique).

=== CE QUI EXISTE DÉJÀ (inventaire réel) ===
1. Place centrale : Index_Maison/strategie/CONNAISSANCE_PROJETS.json — 1 fichier JSON,
   schéma par projet (these, faits_verifies avec etat+score, statut_verification,
   lecons, signets_cles). Pilote Canton OK (GO-AVEC-RÉSERVE 85/78).
2. Collecteur : construire_connaissance.py (ingère verdicts famille + signets gardés,
   idempotent, quotas, péremption, archive froide) + SANTE_CONNAISSANCE.md.
3. Injecteur : injecter_connaissance.py (fiche ≤500 tokens, --projet/--sujet/--lecons,
   rotation, filtre score≥0.6 + etat==verifie).
4. OPTION B BRANCHÉE CE SOIR : contexte_systeme() dans cortana_analyse.py injecte AUTO
   les fiches (plafond 3, synthèse pré-mâchée, garde-fous famille 92/78). Testé OK.
5. OPTION A BRANCHÉE CE SOIR : section <knowledge_base> CPFP gravée dans le prompt canon
   de Cortana (relue à chaque analyse). Testé OK (elle explique le mécanisme sans brief).
6. Ada : gardienne DÉTERMINISTE (pas un LLM) — reçoit des VALEURS via live.json :
   modulateur onchain ±10%, modulateur CPFP −7%, seuil X relatif auto-appris.
7. Discipline quotidienne (07h15) : note Cortana (score_justesse) + dérive mémoire +
   Kelly ombre — les HIT/MISS SONT déjà calculés mais NON réinjectés en leçons.

=== LE DESIGN PROPOSÉ (à affiner) ===
L'AGORA = la place centrale + 4 portes d'ENTRÉE + 2 langues de SORTIE + 1 boucle de VIE.

ENTRÉES (ce qui nourrit la place) :
  E1. Verdicts famille (déjà) — audits → faits_verifies.
  E2. Signets gardés (déjà) — tri X → signets_cles.
  E3. Pépites Christophe (déjà) — thèses validées → these + section gravée.
  E4. LEÇONS HIT/MISS (À CRÉER — la plus précieuse) : chaque analyse notée de Cortana
      (HIT/MISS/FLAT par indice) devient une leçon dans la base, étiquetée par indice
      (funding, fearGreed, onchain...). Boucle : erreur → leçon → réinjectée → moins d'erreurs.

SORTIES (comment la place diffuse) — 2 LANGUES :
  S1. Cortana (cerveau qui LIT) → synthèses TEXTUELLES pré-mâchées (déjà branché).
  S2. Ada (gardienne qui CALCULE) → VALEURS, jamais de texte : modulateurs + seuils
      validés famille (déjà branché via live.json). Même agora, deux langues.

BOUCLE DE VIE (hygiène) :
  - Péremption : fondamentaux 90j / marché 30j (déjà dans construire_connaissance).
  - Archive froide 180j (déjà).
  - TTL sur les fiches injectées (proposition famille gemini — à intégrer).
  - Registre des leçons : chaque HIT/MISS alimente une fiche avec tag (proposition nvidia).

=== QUESTIONS À LA FAMILLE ===
Q1 : La boucle E4 (leçons HIT/MISS auto) — architecture : (a) script dédié
    `lecons_auto.py` qui lit l'historique de justesse et écrit les leçons dans la base,
    (b) intégré dans la discipline 07h15, (c) autre ? Quelle cadence (quotidien) ?
Q2 : Comment formater UNE leçon pour qu'elle soit ACTIONNABLE pour Cortana sans la
    brouiller à 44% de justesse ? (ex. « funding positif ne veut pas toujours dire LONG
    — 7/20 juste ») Contrainte : synthèse pré-mâchée, pas de chiffres bruts.
Q3 : Deux langues (texte Cortana / chiffres Ada) : le design est-il bon ? Y a-t-il un
    risque que les leçons de Cortana biaisent les modulateurs d'Ada (confusion de
    nature) ? Comment cloisonner ?
Q4 : Légereté : 1 fichier JSON + scripts stdlib — valable pour le long terme, ou faut-il
    prévoir une évolution (ex. SQLite) quand la base grossira (100+ fiches) ?
Q5 : Comment mesurer que l'AGORA améliore RÉELLEMENT la justesse de Cortana (métrique,
    A/B) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur l'AGORA : E4 + 2 langues + boucle de vie)
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
        "max_tokens": 3000, "temperature": 0.3,
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
            f.write(f"# Avis {nom} — AGORA (provider {d.get('provider','?')}, {round(time.time()-t0,1)}s)\n\n{content}\n")
        print(f"[OK] {nom} a répondu ({round(time.time()-t0,1)}s)")
    except Exception as e:
        print(f"[ERREUR] {nom}: {e}")


if __name__ == "__main__":
    print("Consultation famille — AGORA (canalisation de la connaissance)...")
    for p in PROVIDERS:
        appeler(p, p["nom"])
    print("Terminé. Avis dans", OUT)
