#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC couche de connaissance au CODEUR (task codeur via hub)."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_CONNAISSANCE_2026-08-15.md")).read()

PROMPT = f"""Tu es le CODEUR ACE777. Une SPEC approuvée famille + supervision t'est confiée.
Lis-la ATTENTIVEMENT puis produis le code demandé.

=== RÈGLES DE CODE ACE777 ===
- Python 3.9+, stdlib uniquement (pas de dépendances externes).
- Encodage UTF-8, docstring de rôle en tête de chaque fichier.
- Écriture ATOMIQUE (mkstemp + os.replace) pour tout fichier JSON.
- Kill-switch : vérifier Index_Maison/strategie/STOP et ~/ace777-test-day1/Index_Maison/STOP_ALL
  avant toute écriture.
- Robustesse : aucun crash si fichier manquant/corrompu (repli propre).
- Idempotence : relançable sans doublons.
- NE PAS toucher au moteur Hulk (paper_diprip.py) — chantier 100% connaissance.

=== LIVRABLES DEMANDÉS ===
1. Index_Maison/strategie/CONNAISSANCE_PROJETS.json — structure initiale conforme §3
   (version, updated, projets vides OU avec exemple CCUSDT si pertinent — dis-moi).
2. Index_Maison/scripts/construire_connaissance.py — collecteur §4 :
   - parse les VERDICT_FAMILLE.md (dossiers CONSULTATION_FAMILLE_*) → faits/leçons/statut,
   - consolide les signets « garder » (SIGNETS_RESUMES.json) → signets_cles par projet,
   - applique les règles anti-engraissement (§3 règles 1-6 : critère d'entrée, péremption
     90/30j, quota 50, scoring fiabilité par source, auto-nettoyage hebdo, archive >90j),
   - génère thermo/SANTE_CONNAISSANCE.md (dashboard santé).
3. Index_Maison/scripts/injecter_connaissance.py — injecteur §5 :
   - --projet SYMBOLE (extrait fiche ≤500 tokens, SANS leçons) et --lecons (ajoute les leçons),
   - --sujet TEXTE (détection auto de projet dans la base par symbole/nom),
   - --max-tokens N, --fichier out.md (optionnel),
   - rotation si >3 projets (2 plus récents + 1 aléatoire),
   - ne filtre QUE les faits etat=="verifie" ET score >= 0.6.

=== FORMAT DE RÉPONSE EXIGÉ ===
- Pour chaque fichier : bloc ```python (ou ```json) complet et fermé, précédé du chemin.
- Une seule section « NOTES » finale : choix faits, points d'attention, dépendances.
Réponds en français, factuel."""

payload = json.dumps({
    "model": "gemini",
    "messages": [
        {"role": "system", "content": "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste."},
        {"role": "user", "content": PROMPT},
    ],
    "max_tokens": 8000, "temperature": 0.2,
}).encode()

req = urllib.request.Request(HUB, data=payload,
                             headers={"Content-Type": "application/json"}, method="POST")
t0 = time.time()
with urllib.request.urlopen(req, timeout=None) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
print(f"Réponse codeur reçue ({round(time.time()-t0,1)}s, {len(content)} chars)")

out = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_CONNAISSANCE_2026-08-15.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Écrit : {out}")
