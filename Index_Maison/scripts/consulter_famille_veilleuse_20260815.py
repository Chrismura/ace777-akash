#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — design VEILLEUSE/SYNAPSE (fil logique + alerte vocale boucle).
Avis seulement, rien n'est appliqué."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_VEILLEUSE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — DESIGN « VEILLEUSE / SYNAPSE » ACE777

=== L'IDÉE DE CHRISTOPHE (exigence d'abord) ===
« Un fil logique comme une synapse : pour tout ce qu'on code, savoir d'où ça vient, ce que
c'est, qui l'a modifié, sans toujours courir pour comprendre — surtout en cas de PANNE.
+ Une VEILLEUSE qui surveille et hurle. + Voir les INTRUSIONS tout de suite. »
Exigence vocale explicite de Christophe : « Pour TOUTES les alertes : faire VOCAL EN BOUCLE
jusqu'à ce que je l'éteigne. C'est la seule façon — moi j'oublie, et les tâches automatisées
doivent être bien bouclées. »

=== CE QUI EXISTE DÉJÀ (inventaire honnête) ===
- Scellement moteur : genesis_manifest.txt + md5 (intégrité du moteur uniquement).
- Scellement CSV : sha256/md5 des runs + verifier_test.sh (runs uniquement).
- verif_sterilite.sh + preflight_total_365j.sh : process résiduels (avant/après run).
- RELEASE_RECEIPT : qui/quoi/comment revenir (par chantier).
- MEMOIRE_COLLAB + journal : fil historique MANUEL (on oublie).
- Heartbeat + discipline quotidienne (launchd 07h15) : vie process + santé IA + alertes.
- Discipline : alerte + rc≠0 (mais pas vocale).
- Vocal : speak_text (edge_tts, voix Vivienne, une seule piste killall say) dans cortana_analyse.
- Kill-switch : fichiers STOP / STOP_ALL respectés par tous les scripts.
- Le constat : les briques existent MAIS éparpillées — pas de fil unifié + alertes pas vocales.

=== DESIGN PROPOSÉ (à affiner) ===
1. REGISTRE DES SYNAPSES — Index_Maison/strategie/REGISTRE_SYNAPSES.json :
   index des composants clés (scripts de prod, plists, configs, données critiques, moteur) :
   { "nom": "paper_diprip.py", "role": "...", "origine": "chantier X",
     "md5": "...", "maj": "date", "depend": ["live.json", ...], "etat": "attendu" }
   Le RELEASE_RECEIPT d'un chantier déclare les fichiers touchés → mise à jour du registre.
2. VEILLEUSE — scripts/veilleuse_synapses.py (launchd, cadence ex. 10 min) :
   - compare les md5 actuels au registre → écart NON déclaré = INTRUSION (alerte),
   - vérifie les process attendus vivants (launchctl list) + fraîcheur des données
     (live.json, whales, alarmes) + kill-switches présents,
   - écrit log append-only + rapport thermo/VEILLEUSE.md,
   - tout écart → déclenche l'alerte vocale en boucle.
3. ALERTE VOCALE EN BOUCLE — scripts/alerte_vocale.py (CENTRAL, réutilisable par toutes
   les alertes : veilleuse, discipline, onchain, superviseur) :
   - lit un message → le répète À VOIX HAUTE (edge_tts Vivienne) en boucle avec pause,
   - tourne JUSQU'À EXTINCTION MANUELLE : `touch STOP_ALERTE` (ou kill du process),
   - une seule piste vocale à la fois (règle maison killall say) — l'alerte PRIORITAIRE.

=== VOTRE MISSION ===
1. REGISTRE : quels fichiers indexer (tous les scripts ? seulement la prod ?) et comment
   éviter les FAUX POSITIFS (un fichier qui change légitimement sans RELEASE_RECEIPT) ?
2. VEILLEUSE : quelles vérifications essentielles vs bruit ? Cadence raisonnable ?
   Comment distinguer « panne » de « intrusion » (l'alerte doit le dire) ?
3. ALERTE VOCALE EN BOUCLE : risque = nuisance permanente si personne n'est là (ex. la nuit).
   Faut-il une limite de sécurité (durée max, fenêtre horaire) OU boucle infinie stricte
   (volonté de Christophe) ? Compromis raisonnable ? Fréquence de répétition ?
4. PRIORITÉ vocale : si l'alerte hurle en boucle, elle bloque les autres voix (killall say).
   Est-ce le bon comportement (alerte = priorité absolue) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur le design veilleuse/synapse + alerte vocale boucle)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
SYNTHÈSE (5 lignes max) : registre + veilleuse + alerte vocale retenues.

Factuel, concis, français. Info manquante → « information insuffisante ». Vous DONNEZ UN
AVIS, ne touchez à rien."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for model in MODELS:
        out_file = os.path.join(OUT, f"AVIS_{model}.md")
        if os.path.exists(out_file):
            print(f"[SKIP] {model} déjà répondu")
            continue
        try:
            content, provider, dur = ask(model)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# AVIS {model} (provider {provider}, {dur}s)\n\n{content}\n")
            print(f"[OK] {model} ({dur}s)")
        except Exception as e:
            print(f"[ERREUR] {model}: {e}")


if __name__ == "__main__":
    main()
