#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — affinage du design « couche de connaissance » ACE777.
Soumet le design (base par projet + collecteur + injecteur) à la famille pour
affinage avant implémentation. Avis seulement, rien n'est appliqué."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_CONNAISSANCE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — DESIGN « COUCHE DE CONNAISSANCE » ACE777

=== LE PROBLÈME IDENTIFIÉ ===
Notre prototype ACE777 (hub IA local + Cortana analyste + Hulk bot paper MEXC) accumule
des pépites (audits famille, signets X triés « garder », thèses de Christophe) MAIS :
1. Aucune base structurée PAR PROJET ne consolide cette connaissance.
2. Rien ne l'injecte automatiquement dans le contexte famille/Cortana quand c'est pertinent.
3. Le superviseur réécrit le contexte à la main à chaque consultation famille (perte de
   temps + incohérence). La famille et Cortana ne voient JAMAIS les signets « garder ».

=== CE QUI EXISTE DÉJÀ (inventaire) ===
- SIGNETS_RESUMES.json : 200 signets X résumés par IA, triés (avis: garder/poubelle/lu),
  jamais injectés nulle part.
- Audits famille éphémères (ex. dossier CONSULTATION_FAMILLE_SMALLCAPS_CANTON_20260815 :
  verdict GO-AVEC-RÉSERVE, 70/72%, 2 classes de paires) — perdus après consultation.
- Discipline quotidienne (launchd 07h15) : note Cortana + dérive mémoire + Kelly ombre.
- Contrat Cortana ADVISORY : Cortana propose, le moteur log, rien d'appliqué <60%.
- 2 classes de paires Hulk : Classe A core liquides / Classe B bags (BAG_PAIRS, vide par
  défaut, premier bag CCUSDT prêt).

=== LE DESIGN PROPOSÉ (à affiner) ===
1. BASE PAR PROJET — Index_Maison/strategie/CONNAISSANCE_PROJETS.json, schéma par projet :
   {
     "CCUSDT": {
       "nom": "Canton Network",
       "these": "...",                       # thèse de Christophe
       "faits_verifies": ["...", "..."],     # faits sourcés (institutionnels, tokenomics)
       "statut_verification": "AUDIT FAMILLE 15/08 (GO-AVEC-RÉSERVE 70/72%)",
       "lecons": ["..."],                    # sizing, horizon, stops, garde-fous
       "signets_cles": ["id1", "id2"],       # références signets gardés
       "updated": "2026-08-15"
     }
   }
2. COLLECTEUR — construire_connaissance.py : ingère les verdicts famille existants +
   signets « garder » → consolide dans la base. Connaissance seulement, zéro touche moteur.
3. INJECTEUR — injecter_connaissance.py : quand on consulte famille/Cortana sur un sujet,
   extrait automatiquement la fiche pertinente + signets gardés → l'ajoute au BRIEF.
   Fini le contexte réécrit à la main.
4. PREMIER CONTENU : Canton (audité ✅) + signets gardés les plus solides. Les autres
   projets de la liste seront nourris au fil des audits.

=== VOTRE MISSION (affinage, pas validation béate) ===
1. Le schéma de la base (champs manquants ? trop ? ex. horizon bag, statut fondamental,
   lien avec les 2 classes ?).
2. Le risque d'ENGRASSEMENT : comment éviter que la base devienne un cimetière de
   faits non vérifiés ? (critère d'entrée d'un fait ? date de péremption ?)
3. L'INJECTION : comment injecter SANS saturer le contexte (taille max, sélection par
   pertinence, rotation) ? Lequel des 3 : (a) tout le temps, (b) à la demande, (c) hybride ?
4. Faut-il scorer la base elle-même (ex. fiabilité par source) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur le design couche de connaissance)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
SYNTHÈSE (5 lignes max) : design retenu + critères d'entrée + mode d'injection.

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
