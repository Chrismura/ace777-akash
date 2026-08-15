#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — VALIDATION DE LA SPEC MOTEUR (flux zéro faute, étape 2 :
le JUGE valide la SPEC avant que le codeur écrive quoi que ce soit).

Chantier : (A) run test → attraper FATAL_RC1 (la ligne qui tue Alpha en rc=1),
(B) corriger la cause racine via codeur + grille + famille, (C) auto-relance
« jamais de chasseur solitaire » (famille 6/6 déjà consultée le 13/08 : GO).

Chaque membre : (1) verdict sur la SPEC (GO / GO AVEC RESERVES / NON + raison),
(2) ce qui manque ou est mal borné dans la SPEC, (3) UNE amélioration GO-sized.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_SPEC_MOTEUR_2026-08-14"
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = """\
VALIDATION FAMILLE — SPEC MOTEUR (flux zéro faute : le JUGE valide la SPEC AVANT que le codeur écrive).

CONTEXTE HUMAIN (Christophe) : « Alpha se tue, et voilà — c'était déjà le chantier de ce matin.
On a passé des heures à réparer des réparations. Je veux la cause racine, pas un pansement. »
Le 14/08, Christophe ordonne : « on attaque le moteur pour le run test — passe par le codeur et
fais valider par la famille, tu dois tout superviser. » Le cockpit a été rendu nickel et validé
par la famille (AUDIT_COCKPIT_NICKEL_2026-08-14, 6/6 GO).

LES FAITS VÉRIFIÉS (13/08) :
- Run MASTER_VORTEX_V2_COLLAB_4H (testnet) : ALPHA meurt en PROCESS_EXIT rc=1 à 18:25:42Z,
  13 min après le départ, juste après le fill cycle 81 (18:25:34). BETA survit (rc=0 à 20:37).
- RÉCURRENT : 16:39, 17:11, 17:30, 17:42, 18:08, 18:25 — toujours ALPHA, jamais BETA.
- Le bot tourne avec set -euo pipefail → toute commande qui échoue = mort rc=1 SILENCIEUSE
  si stderr avalé (ex: x=\"$(cmd 2>/dev/null)\").
- Les 2 seuls exit 1 du code = checks de DÉMARRAGE (BASE_URL testnet, erreur levier) → exclus.
- Le chemin de fermeture de position est robuste (|| true, EXIT_ERROR loggé, continue) → vérifié
  ligne par ligne, la mort n'y est pas.
- Fenêtre de mort : fill à 18:25:34 puis RIEN jusqu'à 18:25:42 (8s de silence). Un « curl tolérant »
  fait 3 tentatives × 5s de pause (jusqu'à 15s sans sortie) ; un helper json_get / num_* / ruby -e
  peut échouer sous set -e pendant ce silence.
- Le lanceur (launch_test_master_base_v8_5_impact_GEMINI_TEST.sh) : run_unit → pipe tail -n +85
  genesis | bash → rc=${PIPESTATUS[1]} → log PROCESS_EXIT → wait $PID_ALPHA (N'RELANCE PAS).
- Trap ERR déjà posé (ligne 89) : au prochain rc=1, écrit FATAL_RC1 ligne=N cmd=[...] dans le log
  du run ET /tmp/ace777_fatal_rc1.log. Testé en réel (false → ligne exacte). Zéro changement de
  comportement. JAMAIS déclenché en réel depuis (aucun run relancé depuis hier soir).
- Marché : Futures TESTNET par défaut (BASE_URL=testnet.binancefuture.com) ; mainnet seulement si
  BINANCE_ALLOW_MAINNET=TRUE explicite. Un run test ne touche PAS d'argent réel.

LA SPEC PROPOSÉE (à valider) :
A. RUN TEST (diagnostic, zéro modification de code)
   A1. Vérifier les portes : STERILE=OK (hygiène), compte à plat (positionRisk == 0 — garde-fou C8
       posé le 13/08), champion intact (md5 vérifié par le preflight).
   A2. Lancer un run testnet court (GO Christophe, commande dans SON terminal).
   A3. Attendre la mort d'Alpha → lire FATAL_RC1 ligne=N cmd=[...] → la commande fautive exacte.
B. CORRECTION CAUSE RACINE (flux zéro faute complet)
   B1. SPEC de correction (par Buffy, superviseur) : la commande fautive identifiée en A3.
   B2. JUGE valide la SPEC. B3. CODEUR (hub code.ia — modèle choisi par mesure) écrit la correction.
   B4. JUGE écrit la grille de test AVANT (commandes + résultat attendu, par un tiers).
   B5. Exécution machine (test_chantier.sh) → résultat automatique.
   B6. Audit famille différente. B7. GO Christophe → mise en service.
   Contraintes : champion 37fca367… INTANGIBLE (wrappers/molettes only, jamais patcher genesis),
   backups datés avant modif, test de restauration prouvé, 1 GO à la fois.
C. AUTO-RELANCE (chantier parallèle, famille 6/6 consultée le 13/08 : verdicts GO)
   C1. Le lanceur relance l'unité morte en session (max 3, pause) — « jamais de chasseur solitaire ».
   C2. Passage par le même circuit : SPEC → juge → codeur → grille → famille → GO.

TA MISSION (3 coups une pierre) :
1. Verdict sur la SPEC (A+B+C) : GO / GO AVEC RESERVES / NON + raison courte et nette
   (le JUGE tranche formellement).
2. Ce qui MANQUE ou est mal borné dans cette SPEC (un angle mort que tu vois).
3. UNE amélioration concrète GO-sized (pas cosmétique) pour fiabiliser le chantier.
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
    print(f"=== AUDIT FAMILLE — SPEC MOTEUR ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
