#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""soumettre_hub_illimite.py — SOUMISSION HUB IN-CASSABLE (10/08, Christophe).

Le problème qu'on élimine : les timeouts qui tuent les appels IA en plein
milieu (basher 30 s par défaut, clamp 600 s, nohup tué avec le shell...).
Chaque appel coupé = temps ET crédits gaspillés inutilement.

LA SOLUTION DURABLE :
- timeout=None dans le script (aucune limite)
- lancé détaché avec `start_new_session` (équivalent macOS de setsid) :
  survit à tout, même si le lanceur meurt
- écrit la réponse dans un fichier au fur et à mesure (pollable)
- relance automatiquement si le hub renvoie une erreur réseau retryable
  (429, 5xx) — les erreurs applicatives (400, 401...) ne sont PAS retryées

Revue experte du CODEUR du hub (12:11, 10/08) : 6 corrections intégrées —
1. requête reconstruite à chaque essai (état propre)
2. erreurs HTTP différenciées (retryables vs non-retryables)
3. logs du détaché vers fichier (lancer_detache.py)
4. vérification d'écriture de la mission (deleguer_codeur.py)
5. timeout lancement 60 s (deleguer_codeur.py)
6. import urllib.error ajouté

USAGE :
    python3 soumettre_hub_illimite.py <task> <fichier_mission.txt> <fichier_sortie.md> [max_tokens]
    # max_tokens optionnel (défaut 4000) — pour le CODEUR utiliser 8000+
    #   (un script long tronqué à 4500 tokens = code inutilisable, vécu le 10/08)
    # puis poller la présence de <fichier_sortie.md> — la réponse y est complète

EXEMPLE LANCEMENT DÉTACHÉ (macOS, pas de setsid) :
    python3 lancer_detache.py python3 soumettre_hub_illimite.py code.ia mission.txt reponse.md 8000
    # la commande retourne IMMEDIATEMENT. On poll <fichier_sortie.md> ensuite.
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error

HUB = "http://127.0.0.1:11435/v1/chat/completions"
RETRIES = 3
RETRY_DELAY = 30  # secondes entre 2 essais (large)


def main():
    if len(sys.argv) < 4:
        print("Usage: soumettre_hub_illimite.py <task> <mission.txt> <sortie.md> [max_tokens]")
        sys.exit(2)
    task, mission_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    max_tokens = int(sys.argv[4]) if len(sys.argv) > 4 else 4000

    # Garde explicite (correction codeur v2, faille 2) : mission doit exister,
    # être lisible et non vide — jamais de traceback brutal.
    if not os.path.exists(mission_path):
        print("ERREUR: Fichier mission introuvable: %s" % mission_path, file=sys.stderr)
        sys.exit(1)
    try:
        taille = os.path.getsize(mission_path)
        if taille == 0:
            print("ERREUR: Fichier mission vide: %s" % mission_path, file=sys.stderr)
            sys.exit(1)
    except OSError as e:
        print("ERREUR: Impossible de lire le fichier mission: %s" % e, file=sys.stderr)
        sys.exit(1)
    try:
        with open(mission_path, encoding="utf-8") as f:
            mission = f.read()
    except (IOError, UnicodeDecodeError) as e:
        print("ERREUR: Lecture impossible du fichier mission: %s" % e, file=sys.stderr)
        sys.exit(1)

    payload = {
        "task": task,
        "messages": [{"role": "user", "content": mission}],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    # Trace de démarrage (savoir que c'est parti, même si tout meurt après)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# SOUMISSION HUB (task %s) — démarrée %s\n\n" % (
            task, time.strftime("%Y-%m-%dT%H:%M:%S")))
        f.write("_Appel lancé. Réponse en cours… (timeout illimité)_\n")

    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
            # Correction 1 : reconstruire la requête à chaque essai (état propre)
            req = urllib.request.Request(
                HUB, data=json.dumps(payload).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            # timeout=None : on attend aussi longtemps qu'il faut, point final.
            with urllib.request.urlopen(req, timeout=None) as resp:
                d = json.loads(resp.read().decode())
            contenu = d["choices"][0]["message"]["content"]
            provider = d.get("provider", "?")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("# RÉPONSE HUB (task %s · via %s) — %s\n\n%s\n" % (
                    task, provider,
                    time.strftime("%Y-%m-%dT%H:%M:%S"), contenu))
            print("[OK] réponse écrite (%d chars) via %s -> %s" % (
                len(contenu), provider, out_path))
            return 0
        except urllib.error.HTTPError as e:
            last_err = e
            # Correction 2 : erreurs HTTP différenciées
            if e.code in (429, 500, 502, 503, 504):
                # retryables : rate limit + erreurs serveur
                print("[essai %d/%d] erreur HTTP %d: %s — nouvel essai dans %ds"
                      % (attempt, RETRIES, e.code, e.reason, RETRY_DELAY), file=sys.stderr)
                time.sleep(RETRY_DELAY)
            else:
                # applicatives (400, 401, 403...) : pas de retry
                print("[ECHEC] erreur HTTP %d non retryable: %s" % (e.code, e.reason), file=sys.stderr)
                with open(out_path, "a", encoding="utf-8") as f:
                    f.write("\n\n## ERREUR HTTP %d NON RETRYABLE\n\n%s\n" % (e.code, e.reason))
                return 1
        except urllib.error.URLError as e:
            # Correction famille (DEEPSEEK R3 + ULTRA 1) : erreur RESEAU pure
            # (connexion refusee, DNS, timeout) -> retryable
            last_err = e
            print("[essai %d/%d] erreur réseau: %s — nouvel essai dans %ds"
                  % (attempt, RETRIES, e, RETRY_DELAY), file=sys.stderr)
            time.sleep(RETRY_DELAY)
        except (json.JSONDecodeError, KeyError) as e:
            # Correction famille : erreur APPLICATIVE (reponse 200 invalide)
            # -> PAS de retry, on ecrit l'erreur et on sort immediatement
            print("[ECHEC] réponse hub invalide: %s" % e, file=sys.stderr)
            with open(out_path, "a", encoding="utf-8") as f:
                f.write("\n\n## ERREUR RÉPONSE INVALIDE\n\n%s\n" % e)
            return 1
        except Exception as e:
            # Garde finale conservatrice : retry
            last_err = e
            print("[essai %d/%d] erreur inattendue: %s — nouvel essai dans %ds"
                  % (attempt, RETRIES, e, RETRY_DELAY), file=sys.stderr)
            time.sleep(RETRY_DELAY)

    with open(out_path, "a", encoding="utf-8") as f:
        f.write("\n\n## ERREUR APRÈS %d ESSAIS\n\n%s\n" % (RETRIES, last_err))
    print("[ECHEC] après %d essais: %s" % (RETRIES, last_err), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
