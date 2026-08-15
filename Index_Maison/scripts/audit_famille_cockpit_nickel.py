#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — COCKPIT NICKEL 14/08 : les 7 correctifs appliqués le matin
(validation rétroactive de la passe de supervision de Buffy, comme exigé par Christophe :
« passe par le codeur et fais valider par la famille, même si tu es meilleur en code,
tu dois tout superviser »).

Chaque membre : (1) verdict par correctif (GO / GO AVEC RÉSERVES / NON + raison courte),
(2) le risque résiduel le plus important, (3) UNE amélioration concrète GO-sized.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_COCKPIT_NICKEL_2026-08-14"
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = """\
AUDIT FAMILLE — COCKPIT NICKEL 14/08 : 7 correctifs appliqués ce matin par Buffy (superviseur),
validés en réel (preuves ci-dessous). Contexte : journée du 13/08 désastreuse (coupure batterie →
position orpheline → réparations en cascade), le cockpit mentait ou était lourd. Christophe a ordonné :
« avant d'attaquer le moteur, le cockpit doit être fluide et nickel ; passe par le codeur et fais valider
par la famille — tu dois tout superviser ». Buffy a corrigé DIRECTEMENT (faute reconnue) puis soumet
rétroactivement à la famille. Vérifie chaque correctif et dis si ça tient debout.

LES 7 CORRECTIFS (avec fichiers + preuves mesurées) :

1. PONT /mission TTL 30s (cortana_cockpit_bridge.py)
   AVANT : do_mission relançait cockpit_mission_feed.py (sous-processus) à CHAQUE appel /mission.
   La page cockpit poll /mission toutes les 10s → feed relancé toutes les ~10s (1,1s CPU + écritures).
   APRÈS : si mission.json a <30s → lecture cache ; sinon régénération. PREUVE : 2e appel à 2s → ageSec=2
   (pas de régénération), mission.json régénéré ~toutes les 33s au lieu de ~12s.

2. ada_saison : archive JSONL au lieu d'1 fichier/scan (ada_saison.py)
   AVANT : ecrire_sorties() créait SAISON_<ts>.json à CHAQUE scan → 28 542 fichiers accumulés (~1/10s).
   APRÈS : append compact dans historique_saisons.jsonl + rotation à ~5000 lignes.
   Purge : 28 542 fichiers → 2011 lignes utiles conservées (dont 12 bascules de saison) + archive tar
   de sécurité /tmp/backups-cockpit-nickel-20260814-081440/historique_saisons_avant_purge.tar.gz.
   PREUVE : 0 fichier SAISON créé en 60s d'observation.

3. cortana_urgent_poll.sh TTL 30s (cortana_urgent_poll.sh, launchd toutes les 10s)
   AVANT : le poll relançait cockpit_mission_feed.py à CHAQUE exécution (~10s) — 2e source de spam.
   APRÈS : le feed ne tourne que si mission.json a >30s (stat -f %m).

4. Conflit de pont résolu (open_cockpit_app.py + launchd com.ace777.cockpit-pont)
   AVANT : open_cockpit_app avait lancé un bridge orphelin (PID 23500) qui tenait le port 17777 ;
   le job launchd (KeepAlive) échouait 7 611 fois en « OSError: Address already in use ».
   Risque : si l'orphelin mourait, plus de pont du tout (le job launchd était en boucle d'échec).
   APRÈS : orphelin tué → launchd reprend la main (state=running, pid, parent=launchd, KeepAlive).
   PREUVE : /status et /mission répondent, pont stable.

5. MUTE aligné sur les 5 chemins voix (cortana_brief.py, cortana_analyse.py, brief_offres.py,
   analyste.py, cortana_yeux.py)
   AVANT : seuls cortana_voice.py + bridge respectaient /tmp/ace777_swarm_pids/.cortana_mute ;
   les 5 chemins locaux parlaient quand même.
   APRÈS : chaque fonction speak_text/parler_texte/speak vérifie le fichier mute (retour muet).
   analyste.py garde le bypass urgent CORTANA_MUTE_ALLOW_URGENT (même convention que cortana_voice).
   PREUVE : test réel → cortana_brief.speak_text('test') → 1 « [voix:MUETTE] ».

6. Cortana dit la vérité (cortana_thermo.py, E-10)
   AVANT : le résumé horaire lisait mission.json/live.json directement → pouvait raconter le dernier
   run comme s'il tournait encore.
   APRÈS : etat_moteurs() interroge http://127.0.0.1:17777/status (ace.state) ; si pont injoignable,
   aucune phrase moteur (on ne devine pas). PREUVE : « Les moteurs sont à l'arrêt. Dernier run :
   MASTER_VORTEX_V2_COLLAB_4H. »

7. Graph + hub résidus (cockpit/index.html + hub_prise_ia.py)
   - z-index du bouton ↻ (cosmos-refresh) 10 → 30 : le panneau .cosmos-detail (z-20, top:12 right:12,
     largeur 260px) le recouvrait → « la fenêtre info IA s'ouvre sur le bouton rafraîchissement » (E-13).
   - hub : /events et /usage utilisaient readlines()[-N:] (lecture complète non atomique) →
     nouveau _tail_jsonl() (lecture par la fin, buffer borné 256 Ko) ; only_model typé
     (isinstance str) pour éviter un TypeError si payload.model est un dict/liste.
   PREUVE : /events → 25 lignes, /usage → 50, appel chat réel OK, hub redémarré proprement.

GARDE-FOUS RESPECTÉS : backups datés AVANT chaque modif (/tmp/backups-cockpit-nickel-20260814-081440),
compilation Python OK sur tous les fichiers, tests réels mesurés, ligne gravée MEMOIRE_COLLAB.

TA MISSION (3 coups une pierre) :
1. Verdict PAR CORRECTIF (1 à 7) : GO / GO AVEC RESERVES / NON + raison en une ligne.
2. Le risque résiduel le PLUS important de cet ensemble (à surveiller en priorité).
3. UNE amélioration concrète GO-sized (pas cosmétique) pour fiabiliser ce qui vient d'être fait.
Réponds en français, format court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1000,
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
    print(f"=== AUDIT FAMILLE — COCKPIT NICKEL ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
