#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC CPFP (onchain v2) au CODEUR (task codeur via hub)."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_CPFP_2026-08-15.md")).read()

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
- NE PAS toucher au moteur Hulk (paper_diprip.py) NI à surveiller_whales.py (scan actuel INCHANGÉ).

=== LIVRABLES DEMANDÉS ===
1. Index_Maison/scripts/detecter_cpfp.py (NOUVEAU) — §4 de la spec :
   - MODE = "observation" par défaut (SILENCIEUX, jamais d'alerte) — option --once et --bilan.
   - Carte 1 (z-score adaptatif) : re-analyse des gros blocs/fragmentations existants
     (whales_scan_latest.json + whales_mouvements.jsonl) avec moyenne mobile 7j + σ,
     déclenche à ≥3σ, plancher absolu ≥500 BTC.
   - Carte 2 (CPFP par frais) : pré-filtre API mempool.space IMPÉRATIF (ne creuser QUE si
     frais >20× médiane, backoff + cache), enfant ≥20× médiane ET parent ≤1 sat/vB ET
     total arbre ≥100 BTC.
   - Carte 3 (poussière) : transactions <2 sat/vB d'une même source, ≥1000 adresses/48h.
   - Écrit data/cpfp_detect.json : ts, tip, zscores, cartes (declenche/score/detail),
     alerte_potentielle (MAIS JAMAIS émise), confirmation (runs successifs), calibration
     (médiane frais, moyenne 7j, σ, max dust).
   - --bilan : génère data/CPFP_BILAN_7JOURS.md.
2. Index_Maison/scripts/pont_onchain.py (MODIF MINIMALE) — §5 :
   - lit AUSSI data/cpfp_detect.json ; n'enrichit la sous-section onchain QUE si
     confirmation >= 2 ET mode actif (sinon ignore) : cpfp_signal (bool+texte pré-mâché),
     cpfp_dir, cpfp_score (pondéré ×0.5).
   - Donne-moi le diff EXACT (avant/après, quelques lignes).
3. Index_Maison/scripts/cortana_analyse.py (MODIF MINIMALE) — §6 :
   - LEXIQUE (l.43) : déclarer la clé onchain v2 (CPFP/dust — « scan mempool réel, PAS le
     proxy aggTrades ») ; build_facts : synthèse TEXTUELLE uniquement (PAS de chiffres bruts).
   - Donne-moi le diff EXACT (avant/après, quelques lignes).
4. Index_Maison/scripts/ada_gardienne.py (MODIF MINIMALE) — §7 :
   - facteur_cpfp ∈ [0.8, 1.2] modulateur OPTIONNEL de calculer_voilure (plafond ±10%),
     appliqué si confirmation >= 2 : exécution CPFP → ~0.92-0.95, dust massif → ~1.05 max,
     sinon 1.0. JAMAIS de blocage. Paramètre optionnel (tests existants = 1 argument).
   - Donne-moi le diff EXACT (avant/après, quelques lignes).
5. Index_Maison/plists/com.ace777.cpfp.plist (NOUVEAU) — §8 :
   StartInterval=600, python3 .../detecter_cpfp.py --once, logs /tmp/cpfp_launchd.log,
   chemin utilisateur /Users/christophe/ace777-test-day1/ (PAS /Users/ace/).

=== FORMAT DE RÉPONSE EXIGÉ ===
- Pour chaque fichier : bloc ```python (ou ```xml) complet et fermé, précédé du chemin.
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
print("Envoi de la spec CPFP au codeur...", flush=True)
t0 = time.time()
with urllib.request.urlopen(req, timeout=None) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
dur = round(time.time() - t0, 1)
out = os.path.expanduser("~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_CPFP_2026-08-15.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(f"# Réponse codeur — chantier CPFP (provider {d.get('provider','?')}, {dur}s)\n\n{content}\n")
print(f"[OK] Réponse écrite ({dur}s) : {out}")
