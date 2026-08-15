#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC AGORA au CODEUR (task codeur via hub)."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_AGORA_2026-08-15.md")).read()

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
- NE PAS toucher au moteur Hulk (paper_diprip.py) ni à ada_gardienne.py (Ada reste INCHANGÉE).

=== LIVRABLES DEMANDÉS ===
1. Index_Maison/scripts/lecons_auto.py (NOUVEAU) — §3 de la spec :
   - `--scan` : lit strategie/justesse_v2.json (par_indice : hit/n par indice, pct global)
     + l'historique des analyses notées ; écrit strategie/lecons_brutes.json (STAGING) :
     constats bruts par indice (hit, n, taux) classés par fiabilité. NE TOUCHE PAS à la base.
   - `--valider` : lit le staging, construit les AXIOMES au format
     « [indice] → [constat] → [action recommandée] » (≤20 mots, PAS de chiffres bruts),
     seuils : n ≥ 5 analyses et (taux < 70% → « corroborer » ; taux > 75% → « confiance »),
     TTL 7 jours (champ ttl_expire), fusionne dans CONNAISSANCE_PROJETS.json sous
     section « lecons_agora » avec namespace "cortana". Idempotent.
2. Index_Maison/scripts/cortana_analyse.py (MODIF MINIMALE) — §5 :
   - contexte_systeme() injecte aussi les leçons de lecons_agora pertinentes (≤3,
     synthèse pré-mâchée, PAS de chiffres bruts).
   - Donne-moi le diff EXACT (avant/après, quelques lignes).
3. Index_Maison/scripts/construire_connaissance.py (MODIF MINIMALE si besoin) — §4 :
   - le schéma doit supporter namespace ("cortana"/"ada") et lecons_agora.
   - Donne-moi le diff EXACT (avant/après) OU explique pourquoi c'est inutile (lecons_auto
     écrit directement).

=== FORMAT DE RÉPONSE EXIGÉ ===
- Pour chaque fichier : bloc ```python complet et fermé, précédé du chemin.
- Pour les MODIFS : bloc ```diff EXACT (avant → après) fermé.
- Une seule section « NOTES » finale : choix faits, points d'attention.
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
print("Envoi de la spec AGORA au codeur...", flush=True)
t0 = time.time()
with urllib.request.urlopen(req, timeout=None) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
dur = round(time.time() - t0, 1)
out = os.path.expanduser("~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_AGORA_2026-08-15.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(f"# Réponse codeur — chantier AGORA (provider {d.get('provider','?')}, {dur}s)\n\n{content}\n")
print(f"[OK] Réponse écrite ({dur}s) : {out}")
