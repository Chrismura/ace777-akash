# SPEC — REVUE EXPERT des scripts anti-timeout (par Ada, 10/08)

CONTEXTE : Ada a ecrit ces scripts (contraire a la loi 1quinquies : tu codes, Ada specifie).
Tu es l'EXPERT : REVOIS le code CI-DESSOUS (colle integralement, c'est le code REEL) et
corrige les failles. Reponds avec : 1) VERDICT OK ou CORRECTIONS NECESSAIRES
2) pour chaque correction : fichier + bloc avant/apres exact. Python 3.9 stdlib, macOS.

===== FICHIER 1 : soumettre_hub_illimite.py =====
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""soumettre_hub_illimite.py — SOUMISSION HUB IN-CASSABLE (10/08, Christophe).

Le problème qu'on élimine : les timeouts qui tuent les appels IA en plein
milieu (basher 30 s par défaut, clamp 600 s, nohup tué avec le shell...).
Chaque appel coupé = temps ET crédits gaspillés inutilement.

LA SOLUTION DURABLE :
- timeout=None dans le script (aucune limite)
- lancé détaché avec `setsid nohup` : survit à tout, même si le lanceur meurt
- écrit la réponse dans un fichier .done au fur et à mesure (pollable)
- relance automatiquement si le hub renvoie une erreur réseau (retry 3x, large)

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

HUB = "http://127.0.0.1:11435/v1/chat/completions"
RETRIES = 3
RETRY_DELAY = 30  # secondes entre 2 essais (large)


def main():
    if len(sys.argv) < 4:
        print("Usage: soumettre_hub_illimite.py <task> <mission.txt> <sortie.md> [max_tokens]")
        sys.exit(2)
    task, mission_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    max_tokens = int(sys.argv[4]) if len(sys.argv) > 4 else 4000

    with open(mission_path, encoding="utf-8") as f:
        mission = f.read()

    payload = {
        "task": task,
        "messages": [{"role": "user", "content": mission}],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")

    # Trace de démarrage (savoir que c'est parti, même si tout meurt après)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# SOUMISSION HUB (task %s) — démarrée %s\n\n" % (
            task, time.strftime("%Y-%m-%dT%H:%M:%S")))
        f.write("_Appel lancé. Réponse en cours… (timeout illimité)_\n")

    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
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
        except Exception as e:
            last_err = e
            print("[essai %d/%d] erreur réseau: %s — nouvel essai dans %ds"
                  % (attempt, RETRIES, e, RETRY_DELAY), file=sys.stderr)
            time.sleep(RETRY_DELAY)

    with open(out_path, "a", encoding="utf-8") as f:
        f.write("\n\n## ERREUR APRÈS %d ESSAIS\n\n%s\n" % (RETRIES, last_err))
    print("[ECHEC] après %d essais: %s" % (RETRIES, last_err), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())


===== FICHIER 2 : lancer_detache.py =====
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lancer_detache.py — lance un processus DÉTACHÉ sur macOS (10/08).

`setsid` n'existe pas sur macOS. L'équivalent natif est
`subprocess.Popen(..., start_new_session=True)` qui crée une nouvelle
session (exactement comme setsid sous Linux) : le processus survit à la
mort du shell qui l'a lancé. C'est LE correctif du problème
« nohup tué avec le basher » qui nous a fait perdre des appels IA entiers.

USAGE :
    python3 lancer_detache.py <commande...>

EXEMPLE :
    python3 lancer_detache.py python3 soumettre_hub_illimite.py code.ia mission.txt reponse.md

Le PID du processus détaché est imprimé. La commande retourne immédiatement.
"""
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: lancer_detache.py <commande...>")
    sys.exit(2)

cmd = sys.argv[1:]
try:
    # start_new_session=True : nouvelle session, détaché du process group du parent
    p = subprocess.Popen(
        cmd,
        start_new_session=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("[OK] processus détaché (PID %d) : %s" % (p.pid, " ".join(cmd)))
except Exception as e:
    print("[ECHEC] %s" % e, file=sys.stderr)
    sys.exit(1)


===== FICHIER 3 : deleguer_codeur.py =====
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deleguer_codeur.py — LE CODEUR DU HUB CODE, PAS MOI (loi 1quinquies).

Déclaration Christophe (10/08) : « ce que je voulais, c'est faire coder au
codeur, pas TOI. C'est clair, il est l'expert. »

LE FLUX OBLIGATOIRE (gravé dans CONTRAT_AUTOGESTION 1quinquies) :
    1. SPEC par Ada (quoi + contraintes + pièges) — jamais de code sans spec
    2. CHOIX du modèle : task code.ia (inferx-coder Qwen3-Coder, fallback nvidia)
    3. Le codeur du hub ÉCRIT le code
    4. Ada INTÈGRE + teste en réel
    5. Audit tiers famille différente (1quater)
    6. GO Christophe

CE SCRIPT : point d'entrée UNIQUE pour déléguer au codeur. Incassable :
- timeout=None (soumettre_hub_illimite.py)
- lancé DÉTACHÉ (lancer_detache.py, start_new_session) → survit à tout
- max_tokens 8000 minimum (une réponse tronquée = code inutilisable)

USAGE :
    python3 deleguer_codeur.py <fichier_spec.md> <fichier_sortie.md> [max_tokens]
    # lance le codeur DÉTACHÉ, retourne immédiatement
    # poller <fichier_sortie.md> pour la réponse (réponse HUB dedans)

EXEMPLE :
    python3 deleguer_codeur.py SPEC_ma_fonction.md CODE_ma_fonction.md 8000
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SOUMETTRE = os.path.join(ROOT, "soumettre_hub_illimite.py")
LANCER = os.path.join(ROOT, "lancer_detache.py")


def main():
    if len(sys.argv) < 3:
        print("Usage: deleguer_codeur.py <spec.md> <sortie.md> [max_tokens]")
        sys.exit(2)
    spec_path = os.path.abspath(sys.argv[1])
    out_path = os.path.abspath(sys.argv[2])
    max_tokens = sys.argv[3] if len(sys.argv) > 3 else "8000"

    if not os.path.exists(spec_path):
        print(f"[ECHEC] spec introuvable: {spec_path}", file=sys.stderr)
        sys.exit(1)

    # En-tête de la spec : rappel du rôle (le codeur code, pas Ada)
    with open(spec_path, encoding="utf-8") as f:
        spec = f.read()
    header = (
        "SYSTEME ACE777 - loi 1quinquies : TU ES LE CODEUR DU HUB (expert).\n"
        "Ada (orchestratrice) SPECIFIE, TU CODES. Produis du code Python 3.9\n"
        "stdlib / bash macOS, non fatal, commentaires en francais, pret a copier.\n"
        "Une seule mission, rien d'autre. Contrat de sortie : le code complet.\n\n"
        "=== SPEC (par Ada) ===\n"
    )
    mission_path = spec_path + ".mission.txt"
    with open(mission_path, "w", encoding="utf-8") as f:
        f.write(header + spec)

    # Lancement détaché : retourne immédiatement, le codeur travaille en paix
    r = subprocess.run(
        [sys.executable, LANCER, sys.executable, SOUMETTRE,
         "code.ia", mission_path, out_path, max_tokens],
        capture_output=True, text=True, timeout=30)
    print(r.stdout.strip() or r.stderr.strip())
    print(f"[OK] codeur lancé détaché → poll {out_path}")


if __name__ == "__main__":
    main()


===== FIN =====

Contrat de sortie :
1. VERDICT : OK / CORRECTIONS NECESSAIRES (liste numerotee)
2. Pour chaque correction : le code exact a remplacer (fichier + bloc avant/apres)
3. Si OK : confirme simplement. Ne reecris pas inutilement. Reponds en francais.
