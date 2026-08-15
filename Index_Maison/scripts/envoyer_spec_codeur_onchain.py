#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC onchain au CODEUR (task codeur via hub)."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_ONCHAIN_2026-08-15.md")).read()

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
- NE PAS toucher au moteur Hulk (paper_diprip.py) — chantier veille/contexte.

=== LIVRABLES DEMANDÉS ===
1. Index_Maison/scripts/pont_onchain.py (NOUVEAU) — §3 de la spec :
   - lit data/whales_scan_latest.json + data/whales_mouvements.jsonl (24h glissantes),
   - calcule : whaleBlocsN/Btc, whaleFragN/Btc, whaleCumul24hBtc, whaleDir
     (inflow/outflow/neutral via étiquettes whales.json), whaleSource, whaleEcartSeuil,
     whaleAlerte (bool + texte), dernierEvtMin, synthèse (phrase pré-mâchée),
   - injecte UNIQUEMENT une sous-section "onchain" dans thermo/live.json (ne touche à
     AUCUNE autre clé, écriture atomique, kill-switch, idempotent).
2. Index_Maison/scripts/cortana_analyse.py (MODIF MINIMALE) — §4 :
   - déclare la section onchain dans le LEXIQUE (mention « scan réel mempool — PAS le
     proxy aggTrades »),
   - ajoute la synthèse textuelle + whaleSource + whaleDir au contexte (PAS les chiffres bruts).
   Donne-moi le diff EXACT (avant/après, quelques lignes).
3. Index_Maison/scripts/ada_gardienne.py (MODIF MINIMALE) — §5 :
   - facteur_onchain ∈ [0.8, 1.2] modulateur de la voilure (plafond ±10%),
   - règle : cumul 24h > 2× moyenne mobile 7j ET outflow → facteur 0.92-0.95 ; inflow
     massif → 1.05 max ; sinon 1.0. JAMAIS de blocage, jamais de saut brutal.
   Donne-moi le diff EXACT (avant/après, quelques lignes).
4. Index_Maison/plists/com.ace777.whales.plist (NOUVEAU) — §6 :
   StartInterval=300, python3 .../surveiller_whales.py --once, logs /tmp/whales_launchd.

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
t0 = time.time()
with urllib.request.urlopen(req, timeout=None) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
print(f"Réponse codeur reçue ({round(time.time()-t0,1)}s, {len(content)} chars)")

out = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_ONCHAIN_2026-08-15.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Écrit : {out}")
