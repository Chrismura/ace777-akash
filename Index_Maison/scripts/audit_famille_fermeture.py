#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_famille_fermeture.py — 10/08 : AUDIT FAMILLE de la fermeture 3 étages.

Contexte : la fusion 3 étages a ajouté 4 services launchd KeepAlive=true
(watchdog, superviseur-core, cockpit-pont, cockpit-http) que l'ancienne
fermeture (stop_ace777.sh) ne connaissait pas -> impossible d'éteindre
proprement (le watchdog relançait le gardien).

Correctif CODEUR DU HUB (loi 1quinquies) intégré par Ada :
- stop_ace777.sh : section 3 étages en tête, ordre critique (watchdog en
  premier), launchctl bootout (KeepAlive), non fatal, filet kill -9.
- COMMANDES_ARRET_ACE777.md : one-liner + vérification + redémarrage.

LA FAMILLE COMPLETE (décision Christophe 10/08 : un check-up de modifications
mérite toute l'attention possible) :
  - GEMINI   -> task audit.protocol  (gemini)
  - DEEPSEEK -> task mission         (nvidia / deepseek-v4-flash-0731)
  - JUGE     -> task signets.juge    (openrouter-juge)
  - ULTRA    -> task ultra.analyse   (openrouter-ultra)

Réponses -> ~/ace777-test-day1/Index_Maison/AUDIT_FERMETURE_2026-08-10/<MEMBRE>.md
"""
import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
AUDIT_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_FERMETURE_2026-08-10"
ROOT = "/Users/christophe/ace777-test-day1"
GEMINI_TASK = "audit.protocol"
DEEPSEEK_TASK = "mission"
JUGE_TASK = "signets.juge"
ULTRA_TASK = "ultra.analyse"


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True,
                                       timeout=20).strip()
    except Exception:
        return ""


def contexte():
    c = {}
    c["stop"] = run("cat %s/stop_ace777.sh" % ROOT)
    c["doc"] = run("cat %s/ERREURS_AI/COMMANDES_ARRET_ACE777.md" % ROOT)
    c["spec"] = run("cat %s/Index_Maison/scripts/SPEC_fermeture_3etages.md" % ROOT)
    c["hub"] = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    c["services"] = run("launchctl list | grep ace777 | awk '{print $1, $2, $3}' | head -12")
    return c


BASE = """\
Systeme ACE777 - Mac 8 Go, hub 11435. LOI 1quinquies : le CODEUR DU HUB a code le correctif, Ada a integre/teste. Tu es membre de la famille ACE777, tu AUDITES le REEL (loi du brut).

LE PROBLEME CORRIGE : la fusion 3 etages a ajoute 4 services launchd KeepAlive=true (com.ace777.watchdog qui relance le gardien toutes les 2 min, com.ace777.superviseur-core le gardien, com.ace777.cockpit-pont le pont vocal/chat port 17777, com.ace777.cockpit-http le tableau de bord port 17800). L'ancien stop_ace777.sh ne les connaissait pas -> un STOP ne coupait rien (le watchdog relancait le gardien). Piège technique : KeepAlive=true -> un simple kill est INUTILE, launchd relance ; seul launchctl bootout desenregistre vraiment le service.

LE CORRECTIF A AUDITER (codeur hub + integration Ada) :
1. stop_ace777.sh : nouvelle section « ARRET SERVICES 3 ETAGES » en TETE du script, ordre CRITIQUE : watchdog EN PREMIER (sinon il relance tout), puis superviseur-core, cockpit-pont, cockpit-http. Chaque arret : launchctl bootout gui/$(id -u)/<label>, NON FATAL (absent = message informatif, on continue), filet de securite kill -9 si superviseur_core.sh traine, exit 0 garanti. Le reste du script (anciens processus vortex/genesis/master/radar, watchdog Ruby) reste INCHANGE - on ajoute, on ne remplace pas.
2. COMMANDES_ARRET_ACE777.md : one-liner complete avec les 4 bootout dans le bon ordre, section « Verifier que tout est eteint », section « Redemarrer SANS reboot » (launchctl bootstrap des 4 plists), note reboot.

REGLES D'AUDIT :
- Verifie l'ORDRE d'arret : le watchdog doit etre bootout en PREMIER, sinon le correctif est inutile.
- Verifie la methode : bootout pour KeepAlive=true (pas kill, pas unload deprecated).
- Verifie la robustesse : non fatal, exit 0 meme si deja arrete, filet kill -9.
- Verifie l'ABSENCE de regression : les anciens processus restent tues, les autres services planifies (brief-matin, gitpush, cortana.horaire...) NE doivent PAS etre touches.
- Verifie que la doc est exacte (one-liner executable tel quel).

Hub /health : %s

--- stop_ace777.sh (REEL, integre) ---
%s

--- COMMANDES_ARRET_ACE777.md (REEL) ---
%s

--- SPEC d'origine (ce qui etait demande) ---
%s

--- services launchd actuels ---
%s

Reponds en francais : verdict GO / GO AVEC RESERVES / NON, avec reserves concretes (fichier + ligne si possible).
"""


def soumettre(task, sysprompt, outfile):
    ctx = contexte()
    mission = BASE % (ctx["hub"] or "PAS DE REPONSE",
                      ctx["stop"] or "(illisible)",
                      ctx["doc"] or "(illisible)",
                      ctx["spec"] or "(illisible)",
                      ctx["services"] or "(vide)")
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": mission},
        ],
        "temperature": 0.2,
        "max_tokens": 2500,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    contenu = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    os.makedirs(AUDIT_DIR, exist_ok=True)
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("# AVIS %s (task %s)\n\nprovider: %s\n\n%s\n"
                % (os.path.basename(outfile).replace(".md", ""), task, provider, contenu))
    print("[OK] %s -> %s (%d chars)" % (outfile, provider, len(contenu)))


def main():
    print("== Soumission GEMINI (audit.protocol) ==")
    soumettre(GEMINI_TASK,
              "Tu es GEMINI, membre de la famille ACE777 (auditeur de protocole). "
              "Audite la fermeture 3 etages avec un oeil critique sur : ordre d'arret "
              "(watchdog en premier), methode bootout pour KeepAlive=true, robustesse "
              "non fatale, zero regression sur les anciens processus et les services planifies.",
              os.path.join(AUDIT_DIR, "GEMINI.md"))
    print("== Soumission DEEPSEEK (mission) ==")
    soumettre(DEEPSEEK_TASK,
              "Tu es DEEPSEEK, membre senior de la famille ACE777. Audite la fermeture "
              "3 etages. Tu es critique, factuel, tu ne valides pas par complaisance : "
              "l'ordre d'arret suffit-il reellement a empecher la relance ? Le bootout "
              "est-il la bonne methode ? La doc est-elle executable telle quelle ?",
              os.path.join(AUDIT_DIR, "DEEPSEEK.md"))
    print("== Soumission JUGE (signets.juge) ==")
    soumettre(JUGE_TASK,
              "Tu es le JUGE, verificateur independant ACE777. Tu valides ou invalides "
              "la fermeture 3 etages. Exigeant sur : le trou est-il VRAIMENT corrige "
              "(le watchdog ne peut plus relancer le gardien) ? Y a-t-il un cas ou "
              "l'arret echouerait et le systeme resterait allume ?",
              os.path.join(AUDIT_DIR, "JUGE.md"))
    print("== Soumission ULTRA (ultra.analyse) ==")
    soumettre(ULTRA_TASK,
              "Tu es ULTRA, membre de la famille ACE777 (analyse profonde). Audite la "
              "fermeture 3 etages en profondeur : architecture de l'arret, cas limites "
              "(service deja arrete, bootout echoue, processus residuel), interaction "
              "avec le redemarrage (bootstrap), risques de regression.",
              os.path.join(AUDIT_DIR, "ULTRA.md"))


if __name__ == "__main__":
    main()
