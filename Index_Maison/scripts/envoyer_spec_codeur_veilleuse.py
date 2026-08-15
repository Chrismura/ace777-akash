#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC veilleuse/synapse au CODEUR (task codeur via hub)."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_VEILLEUSE_2026-08-15.md")).read()

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
- NE PAS toucher au moteur Hulk (paper_diprip.py) — chantier veille/alerte.
- Voix : edge_tts via `python3 -m edge_tts --voice fr-FR-VivienneMultilingualNeural` +
  `killall say` avant (une seule piste, règle maison).

=== LIVRABLES DEMANDÉS ===
1. Index_Maison/strategie/REGISTRE_SYNAPSES.json (NOUVEAU) — §3 : version, updated,
   fichier[] avec nom/role/origine/md5/maj_attendue/auto_modifiable/verif
   (md5|fraicheur) + fraicheur_max_min si verif=fraicheur. Indexe : scripts de prod
   (paper_diprip.py, surveiller_whales.py, discipline_quotidienne.py, cortana_analyse.py,
   ada_gardienne.py, thermo_quotidien_free.py, veilleuse_synapses.py), plists actives
   (com.ace777.whales.plist, com.ace777.discipline-quotidienne.plist), configs
   (config/defaults.env, strategie/cortana_pilot.json), moteur (genesis_manifest.txt),
   et données fraîcheur (thermo/live.json, data/whales_scan_latest.json). Calcule les
   md5 RÉELS des fichiers (écris le JSON avec les vrais hash). Ne mets PAS de md5 pour
   les verif=fraicheur (valeur vide ou omise).
2. Index_Maison/scripts/veilleuse_synapses.py (NOUVEAU) — §4 : charge le registre, vérifie
   (a) md5 des fichiers stables → écart non déclaré = INTRUSION, (b) process attendus
   vivants (launchctl list + pgrep — attends une liste ATTENDUS_PROCESS dans le script,
   ex. hub, cockpit-http, whales, discipline-quotidienne), (c) fraîcheur des fichiers
   verif=fraicheur (mtime < fraicheur_max_min → PANNE), (d) kill-switches présents,
   (e) auto-intégrité (md5 de soi-même — compare au registre). Écrit thermo/VEILLEUSE.md
   (rapport) + journal append-only (data/alertes/veilleuse.log) + en cas d'anomalie :
   écrit data/alertes/ALERTE_[ts].json + lance alerte_vocale.py en détaché (nohup) avec
   message distinct INTRUSION/PANNE + rc=1. Si MAINTENANCE_PREVUE existe avec date de
   fin future → ne pas alerter.
3. Index_Maison/scripts/alerte_vocale.py (NOUVEAU) — §5 : argparse --message, --id,
   --arret. Boucle STRICTE : répète le message toutes les 30s (pause 5s) via edge_tts
   (killall say avant). Extinction : si fichier STOP_ALERTE_<id> existe OU --arret →
   arrêt propre + suppression du fichier d'arrêt. Écrit data/alertes/ALERTE_[ts].json.
   Boucle infinie (pas de limite de temps — volonté Christophe).
4. Index_Maison/plists/com.ace777.veilleuse.plist (NOUVEAU) — §6 : StartInterval=600,
   python3 veilleuse_synapses.py, /tmp/veilleuse.out.log + .err.log, RunAtLoad true.
5. Index_Maison/scripts/arret_alerte.sh (NOUVEAU) — raccourci : `touch STOP_ALERTE` (tous)
   + killall edge_tts si besoin.

=== FORMAT DE RÉPONSE EXIGÉ ===
- Pour chaque fichier : bloc ```python (ou ```json ou ```xml ou ```bash) complet et fermé,
  précédé du chemin.
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
    "~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_VEILLEUSE_2026-08-15.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Écrit : {out}")
