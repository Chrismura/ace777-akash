#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_famille_hub.py — CONSULTER LA FAMILLE via le hub local (0 €, providers gratuits).

POURQUOI CE SCRIPT EXISTE : la maison écrivait un script jetable par consultation
(`consulter_famille_<sujet>_<date>.py`) — 30+ copies, chacune à réécrire. Ici, un seul
outil : on lui donne un brief, il repose la question sous PLUSIEURS ANGLES (pour obtenir
des avis complémentaires, pas trois fois le même accord) et il archive chaque réponse
avec le provider qui a réellement répondu.

RÈGLE DE LA MAISON (rappel) : la famille est invitée à CONTREDIRE, pas à valider.
D'où les angles : critique · contre-argument · simplification.

USAGE
  python3 consulter_famille_hub.py <dossier_sortie> <brief.md> [--n 3] [--task analyse.profonde]

SORTIE
  <dossier_sortie>/AVIS_<n>_<provider>.md   (réponse + provider + modèle + durée)
  <dossier_sortie>/SYNTHESE.md             (tableau récapitulatif, à compléter par l'agent)

Stdlib uniquement. Aucun ordre, aucune écriture ailleurs que dans <dossier_sortie>.
Gemini/Gravity hors quota (19/09) : c'est le hub qui porte la famille — même chemin d'appel.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
TIMEOUT_S = 300

ANGLES = [
    ("CRITIQUE", "Analyse le plan ci-dessus en ingénieur système. Est-il SENSÉ et RÉALISABLE ? "
                 "Nomme précisément ce qui MANQUE ou ce qui est faux. Sois concret, pas de généralités. "
                 "Termine par : CE QUI MANQUE = ..."),
    ("CONTRE", "Contredis le plan ci-dessus. Quelle est LA faiblesse qui le ferait échouer en vrai "
               "(panne, oubli, complexité, coût) ? Propose la correction la plus simple possible. "
               "Termine par : LE PIÈGE = ..."),
    ("SIMPLE", "Propose une version PLUS SIMPLE du plan ci-dessus qui atteint le même but avec MOINS de "
               "mouvement (moins d'agents, moins de fichiers, moins de vigilance humaine). "
               "Termine par : VERSION MINIMALE = ..."),
]


def appel_hub(brief: str, angle: str, instruction: str, task: str):
    """Un appel au hub. Retourne (texte, provider, model, duree_s)."""
    prompt = (
        "Tu es un membre de la FAMILLE ACE777 (système de trading/recherche personnel, 0 €, "
        "macOS 8 Go, agents launchd, mémoire Obsidian). On te demande un AVIS, pas une validation.\n\n"
        "=== BRIEF ===\n" + brief + "\n\n=== TA MISSION (" + angle + ") ===\n" + instruction + "\n"
    )
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": "Tu réponds en français, concis et concret. "
                                          "Tu contredis quand il faut. Aucune flatterie."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
        "max_tokens": 1200,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(HUB, data=data, headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
        rep = json.loads(r.read().decode("utf-8"))
    duree = round(time.time() - t0, 1)
    texte = rep["choices"][0]["message"]["content"]
    return texte, rep.get("provider", "?"), rep.get("model", "?"), duree


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = 3
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    task = "analyse.profonde"
    if "--task" in sys.argv:
        task = sys.argv[sys.argv.index("--task") + 1]

    if len(args) < 2:
        print(__doc__)
        return 1
    sortie, brief_path = args[0], args[1]
    os.makedirs(sortie, exist_ok=True)
    brief = open(brief_path, encoding="utf-8").read()

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    resultats = []
    for i in range(n):
        angle, instruction = ANGLES[i % len(ANGLES)]
        print(f"[famille] {i+1}/{n} — angle {angle} (task {task})…", flush=True)
        try:
            texte, prov, model, duree = appel_hub(brief, angle, instruction, task)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, ValueError) as e:
            print(f"[famille] {i+1}/{n} ÉCHEC : {e}")
            resultats.append({"angle": angle, "provider": "ÉCHEC", "model": "-", "duree": 0,
                              "fichier": None, "erreur": str(e)})
            continue
        nom = f"AVIS_{i+1}_{angle}_{prov}.md"
        chemin = os.path.join(sortie, nom)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(f"---\nangle: {angle}\nprovider: {prov}\nmodel: {model}\n"
                    f"consulte: {ts}\nbrief: {os.path.basename(brief_path)}\n---\n\n{texte}\n")
        print(f"[famille] {i+1}/{n} OK — {prov} / {model} en {duree}s")
        resultats.append({"angle": angle, "provider": prov, "model": model,
                          "duree": duree, "fichier": nom})

    lignes = [
        f"# Consultation famille — {os.path.basename(brief_path).replace('.md','')}",
        "",
        f"> Consultée le **{ts}** via le **hub** (`{task}`) · {n} avis · **0 €**",
        "> (Gemini/Gravity hors quota le 19/09 : la famille passe par le hub, mêmes providers gratuits.)",
        "",
        "| # | Angle | Provider | Modèle | Durée | Avis |",
        "|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(resultats, 1):
        lignes.append(f"| {i} | {r['angle']} | {r['provider']} | {r['model']} | "
                      f"{r['duree']}s | {('`' + r['fichier'] + '`') if r['fichier'] else 'échec'} |")
    lignes += ["", "## À compléter par l'agent", "",
               "Synthèse : ce qui est retenu, ce qui est contredit, ce qui est écarté (avec la raison)."]
    with open(os.path.join(sortie, "SYNTHESE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")

    print(f"[famille] avis écrits dans {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
