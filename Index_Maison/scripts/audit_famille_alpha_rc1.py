#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — ALPHA rc=1 : pourquoi ALPHA se tue silencieusement en cours de run.
Chaque membre : (1) verdict sur le diagnostic, (2) la commande la plus probablement fautive,
(3) une amélioration logique/perf/stabilité (3 coups une pierre)."""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_ALPHA_RC1_2026-08-14"
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit. Diagnostic forensique = ton terrain."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées par le code."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = """\
AUDIT FAMILLE — POURQUOI ALPHA SE TUE EN rc=1 (enquête forensique ACE777)

CONTEXTE HUMAIN (Christophe) : « Alpha se tue, et voilà — c'était déjà le chantier de ce matin.
On a passé des heures à réparer des réparations. Je veux comprendre la cause racine, pas un pansement. »

1) FAITS DU RUN (MASTER_VORTEX_V2_COLLAB_4H, session 18:12:39→20:37:04Z) :
- PNL total +1.3718 USDT (BETA +0.5452, ALPHA +0.8266). Run terminé à SA fin planifiée.
- ALPHA (x13, HUNTER, DUO_ROLE=HUNTER) : PROCESS_EXIT rc=1 à 18:25:42Z — 13 min après le départ,
  juste après le fill cycle 81 (18:25:34, +0.13168, shock_inversion_stop). AUCUNE relance ensuite.
- BETA (x5, SCOUT) : a survécu jusqu'à 20:37:09 (rc=0, fin planifiée). 212 E-DUO (désynchro duo
  scout/hunter) causés par la mort d'ALPHA.
- RÉCURRENT : ALPHA meurt en rc=1 à presque chaque session (16:39, 17:11, 17:30, 17:42, 18:08, 18:25).
  BETA survit systématiquement. C'est spécifique à ALPHA (x13/BURST13/HUNTER).

2) ARCHITECTURE :
- Lanceur (launch_test_master_base_v8_5_impact_GEMINI_TEST.sh) : run_unit() pipe
  `tail -n +85 ./genesis_manifest.txt | bash -s 2>&1 | while read ...` ; rc=${PIPESTATUS[1]}.
  Si le bot sort en rc=1, le lanceur log PROCESS_EXIT et N'RELANCE PAS (wait $PID_ALPHA).
- Le bot (genesis_manifest.txt, ligne 86) tourne avec `set -euo pipefail`.
  → TOUTE commande qui échoue = mort rc=1 SILENCIEUSE si son stderr est avalé (ex: `x="$(cmd 2>/dev/null)"`).
- Les 2 seuls `exit 1` du code sont des checks de DÉMARRAGE (BASE_URL testnet, erreur levier) → exclus
  (Alpha a tourné 13 min avant de mourir).
- Le chemin de fermeture de position est robuste (|| true, EXIT_ERROR loggé, continue) → vérifié ligne
  par ligne, la mort n'y est pas.
- Le log du run montre le fill à 18:25:34 puis RIEN jusqu'au PROCESS_EXIT à 18:25:42 (8s de silence :
  un « curl tolérant » fait 3 tentatives × 5s de pause, soit jusqu'à 15s sans sortie — un helper
  json_get / num_* / ruby -e peut échouer sous set -e pendant ce silence).

3) CE QUI A ÉTÉ FAIT (diagnostic déjà en place) :
- Trap ERR posé (ligne 89) : au prochain rc=1, le log écrira `FATAL_RC1 ligne=N cmd=[...]` + fichier
  /tmp/ace777_fatal_rc1.log. Testé : fonctionne. Zéro changement de comportement.
- L'étape suivante prévue : relancer un run pour attraper la ligne exacte, puis corriger la racine.
- Chantier proposé en parallèle : auto-relance de l'unité morte par le lanceur (max 3, avec pause).

TA MISSION (3 coups une pierre) :
1. Verdict sur le DIAGNOSTIC : cohérent ? il manque quelque chose ? (réponds GO / GO AVEC RESERVES / NON
   avec une raison courte, sauf le JUGE qui tranche formellement).
2. La commande la PLUS PROBABLEMENT fautive dans ce contexte (set -euo pipefail, mort ~13 min après le
   départ, juste après un fill, silence de 8s) — donne le mécanisme précis (ex: substitution avalée,
   helper bash qui échoue, appel API non tolérant, variable non bornée sous set -u…).
3. UNE amélioration concrète de logique/perf/stabilité (pas cosmétique) — ex: rendre TOUTES les
   commandes critiques tolérantes, auto-relance, garde-fou anti-session-à-une-jambe…
Réponds en français, format court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 700,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}"


if __name__ == "__main__":
    import sys
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    print(f"=== AUDIT FAMILLE — ALPHA rc=1 ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
