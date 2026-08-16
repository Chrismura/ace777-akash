#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC SANTÉ DES INDEX au CODEUR (task code.ia via hub) — 17/08/2026.
Clause permanente gravée (Christophe, 16/08) : ne pas se contenter de corriger,
PROPOSER des améliorations si elles ont du sens.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"

# État réel du livrable (Buffy, vérifié — pas un récit)
FAITS = """\
=== ÉTAT RÉEL (vérifié 17/08 00:35Z) ===
1. Index_Maison/scripts/sante_index.py (NOUVEAU, tourne via plist com.ace777.sante-index toutes les 5 min) :
   - Vérifie 6 chaînes MAILLON PAR MAILLON : BALEINES (scan→pont→live.json.onchain→Ada+Cortana),
     HULK (sonde paper_diprip→CSV ASPIRATION_CALIB_*), LIVE (thermo→mission.json→cockpit),
     CPFP (détecteur→pont→Ada, mode observation 7j), SÉCURITÉ (veilleuse synapses), SAISON (6 indices).
   - Par maillon : process vivant (launchctl/pgrep) + fichier frais (âge < seuil) + clé présente chez le consommateur.
   - Écrit Index_Maison/thermo/sante_index.json + Index_Maison/cockpit/sante_live.js (window.__SANTE__).
2. Cockpit : carte 🩺 SANTÉ DES INDEX dans l'onglet thermo (index.html, renderSante() + cellule SANTÉ dans la grille).
3. Déclaré au registre veilleuse (md5) — veilleuse STABLE.

=== CE QU'IL MANQUE / À AJOUTER (la demande) ===
1. ALERTE quand une chaîne passe au rouge : aujourd'hui la carte passe 🔴 mais PERSONNE n'est prévenu.
   Ajouter : si anomalies non vides → écrire data/alertes/ALERTE_SANTE_[ts].json + lancer
   Index_Maison/scripts/alerte_vocale.py (détaché, anti-empilement comme la veilleuse) avec le nom
   des chaînes cassées. Respecter MAINTENANCE_PREVUE (ne pas alerter si maintenance en cours).
2. HISTORIQUE : garder un journal append-only (data/alertes/sante_index.log ou similaire) de chaque
   passage OK→ALERTE→OK (horodaté), pour voir les coupures passées.
3. PAGE SANTÉ complète : le cockpit n'affiche que le résumé (6 lignes + détail des anomalies).
   Si possible : un onglet ou panneau dépliable avec TOUS les maillons et leur âge réel
   (ex. « pont : vivant · scan file : âge 2 min · live.json.onchain : présente »).
4. NE PAS toucher au moteur Hulk (paper_diprip.py) ni à la logique des chaînes existantes :
   sante_index.py est le seul fichier à enrichir (avec ses données), pas les chaînes vérifiées.
"""

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

PROMPT = f"""Tu es le CODEUR ACE777. Le pré-vol SANTÉ DES INDEX existe et tourne.
Lis les FAITS puis AJOUTE les améliorations demandées.

=== RÈGLES DE CODE ACE777 ===
- Python 3.9+, stdlib uniquement (pas de dépendances externes).
- Encodage UTF-8, docstring de rôle en tête de chaque fichier.
- Écriture ATOMIQUE (mkstemp + os.replace) pour tout fichier JSON.
- Kill-switch : vérifier Index_Maison/strategie/STOP et ~/ace777-test-day1/Index_Maison/STOP_ALL
  avant toute écriture.
- Robustesse : aucun crash si fichier manquant/corrompu (repli propre).
- Idempotence : relançable sans doublons (surtout pour l'alerte vocale : anti-empilement).
- NE PAS toucher au moteur Hulk (paper_diprip.py) ni aux scripts des chaînes vérifiées.
- Voix : edge_tts via `python3 -m edge_tts --voice fr-FR-VivienneMultilingualNeural` +
  `killall say` avant (une seule piste, règle maison) — réutiliser alerte_vocale.py existant.

{FAITS}

=== LIVRABLES DEMANDÉS (dans sante_index.py + éventuels petits fichiers) ===
1. ALERTE VOCALE sur chaîne rouge : anomalies non vides → data/alertes/ALERTE_SANTE_[ts].json
   + lancer alerte_vocale.py en détaché (subprocess.Popen start_new_session) avec message
   listant les chaînes cassées. Anti-empilement (pgrep alerte_vocale.py). MAINTENANCE_PREVUE respectée.
2. HISTORIQUE append-only des transitions (data/alertes/sante_index.log) : chaque run écrit
   une ligne JSON avec ts, etat (OK|ALERTE), chaines_ok, anomalies — on pourra voir les coupures passées.
3. EXPOSITION : ajouter au rapport JSON une section « maillons » détaillée (nom + ok + détail) déjà
   présente — vérifier qu'elle est bien complète et exploitable par le cockpit pour un panneau dépliable.
4. Si utile et prouvé : propose UNE amélioration supplémentaire (mesurable, bornée) — clause permanente.

=== FORMAT DE RÉPONSE EXIGÉ ===
- Pour chaque fichier : bloc ```python (ou ```json) complet et fermé, précédé du chemin.
- Une seule section « NOTES » finale : choix faits, points d'attention, amélioration proposée.
Réponds en français, factuel.
"""

payload = json.dumps({
    "model": "gemini",
    "messages": [
        {"role": "system", "content": "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste.\n\n" + CLAUSE},
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
provider = d.get("provider", "?")
print(f"Réponse codeur reçue ({round(time.time()-t0,1)}s, provider {provider}, {len(content)} chars)")

out = os.path.join(ROOT, "REPONSE_CODEUR_SANTE_INDEX_2026-08-17.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(f"# Réponse codeur — SANTÉ DES INDEX (provider {provider}, {round(time.time()-t0,1)}s)\n\n{content}\n")
print(f"Écrit : {out}")
