#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Codeur — traque de la ligne exacte du rc=1 (dossier coherent 14/08)."""
import json, time, urllib.request, os

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/TRACK_RC1_CODEUR_2026-08-14"
os.makedirs(OUT, exist_ok=True)

CONTEXTE = (
    "Tu es le CODEUR de la famille ACE777 (task code.ia). Ta mission : TRAQUER LA LIGNE EXACTE "
    "qui fait sortir le moteur en rc=1 silencieux, en plein cycle, sans aucun message. "
    "Tu as deja valide l'hypothese (avec la famille 8/8) : un exit/retour explicite ou une "
    "commande en contexte non couvert par trap ERR. Maintenant, trouve LA ligne.\n\n"
    "CLAUDE PERMANENTE (Christophe, 14/08 — a respecter a CHAQUE intervention) :\n"
    "« Prouve la meilleure logique et applique-la dans la correction et l'amelioration si "
    "possible. »\n"
    "-> Ne propose PAS une rustine : PROUVE la cause racine avec les preuves, et propose UNE "
    "amelioration si elle est prouvee (mesurable, bornee).\n\n"
    "================ CONTEXTE — LE MOTEUR VAUT LA PEINE (preuves) ================\n\n"
    "Ce moteur est RENTABLE — c'est pour cela qu'on ne casse rien et qu'on cherche la cause "
    "exacte, pas un patch. PNL cumule ALPHA+BETA (rapports officiels RAPPORT_PNL_AUTO) :\n"
    "- 09/07 : +21.21 | 10/07 : +88.52 (champion +29.41 en une session) | 11/07 : +11.95 | "
    "12/07 : +16.49 | 13/07 : -19.75 (tempete barriere) | 12/08 : +5.36 | 13/08 : +12.29 | "
    "14/08 : +3.22\n"
    "- Cumul sur ~9 jours actifs : +126 USDT+ (ALPHA+BETA uniquement). Sur un testnet, "
    "des profits constants sur plusieurs jours, c'est RARE — ce moteur a une vraie logique.\n"
    "- Il tourne TOUT SUR TESTNET (testnet.binancefuture.com), duo BETA (SCOUT x5 SHORT) + "
    "ALPHA (HUNTER x13 LONG), genesis_manifest.txt, master launch_test_master_base_v8_5_impact.sh\n\n"
    "================ LE PROBLEME — 4 MORTS rc=1 SILENCIEUSES (14/08) ================\n\n"
    "Le run 4H du 14/08 a fait 4 morts, meme signature EXACTE :\n"
    "1) BETA #1 : dernier cycle logge 08:49:26 #92 SKIP -> mort 08:49:29 (3 s de silence)\n"
    "2) ALPHA #1 : dernier cycle logge 08:52:18 #108 SKIP -> mort 08:52:26 (8 s)\n"
    "3) ALPHA #2 : dernier cycle logge 09:24:57 #203 SKIP -> mort 09:25:05 (8 s)\n"
    "4) BETA #2 : dernier cycle logge 09:29:13 #214 SKIP -> mort 09:29:20 (7 s)\n"
    "=> Chaque mort survient PENDANT le cycle suivant (jamais logge), 3-8 s apres le dernier "
    "log. PROCESS_EXIT.log : how=pipe_run_unit why=rc_1 rc=1.\n\n"
    "================ PREUVES D'ABSENCE (ce qui NE s'est PAS passe) ================\n\n"
    "- ZERO FATAL_RC1 : le trap ERR (ligne ~90 du genesis, actif dans la partie executee "
    "tail -n +85) n'a JAMAIS tire -> aucune commande simple n'a echoue sous set -e.\n"
    "- ZERO WARN safe_call du run. /tmp/ace777_stderr_debug.log = 0 octet.\n"
    "- Pas de echoes « Done. » avant les morts -> pas une fin naturelle de boucle.\n"
    "- Les 2 seuls `exit 1` du code execute (ligne 367 BASE_URL, ligne 1492 leverage) sont "
    "dans l'INIT, pas dans la boucle — le run a tourne 100+ cycles, donc pas eux.\n"
    "- Le master lance : `tail -n +85 genesis | bash -s 2>&1 | while read` avec pipefail "
    "ACTIF -> le rc capte est bien le rc du bash -s (test machine prouve).\n\n"
    "================ FAIT MACHINE DECISIF (deja prouve) ================\n\n"
    "- TEST D (superviseur) : un `exit 1` EXPLICITE ne declenche JAMAIS le trap ERR "
    "(contrairement a un echec de commande). -> rc=1 silencieux, zéro log, stderr vide.\n"
    "- TEST instrumente (trap EXIT + DEBUG, valide famille+codeur, testé en machine) : "
    "l'instrumentation capture bien rc + derniere commande. Elle est en place dans le master.\n"
    "- Le run de capture de 20 min (10:32Z, détaché) a fini PROPREMENT rc=0 — la cause n'a "
    "pas encore ete recapturee (les 2 premiers runs ont ete tues par l'outil terminal du "
    "superviseur, pas par le moteur — prouve).\n\n"
    "================ STRUCTURE DU CODE A ANALYSER ================\n\n"
    "Boucle principale : `while true` autour des lignes 2146-2520 du genesis. A l'interieur :\n"
    "- calcul tension/momentum (lignes ~1560-1660) avec calls API + `sleep`\n"
    "- `safe_call` (lignes ~692-720) : fait `set -e` / `set +e` autour des appels — correctif "
    "anti-mort valide (genesis d6977337)\n"
    "- `duo_global_stop_hit` : arret en chaine du duo\n"
    "- divers `continue`/`break`/`sleep` et des helpers ruby qui retournent 0/1\n"
    "- le master fait `set +e` autour du pipeline mais PAS `set +o pipefail`\n\n"
    "Zone de sortie : apres `done` (ligne ~2520), la fin du script fait des echoes « Done. » "
    "— ABSENTS avant les morts, donc la sortie n'est pas passee par la.\n\n"
    "================ QUESTION ================\n"
    "1) Ou est LA ligne (ou la combinaison de lignes) qui fait sortir le bash -s en rc=1 "
    "PENDANT un cycle, 3-8 s apres le dernier log, sans log du cycle suivant, sans declencher "
    "le trap ERR ? Analyse la structure : `while true` + `sleep` + appels réseau + `|| true` "
    "+ helpers ruby + safe_call. Le `while read` du master et la fermeture de pipe sont-ils "
    "en cause ? Un `read` qui consomme le stdin ? Un sous-shell `$(...)` qui meurt ? Un "
    "SIGPIPE masque ? Un signal pendant le `sleep` ?\n"
    "2) Donne le correctif d'observation le plus court qui CAPTURERA la ligne exacte au "
    "prochain rc=1 (ex: trap EXIT avec $BASH_COMMAND + $BASH_LINENO, PS4 sur la fenetre du "
    "cycle, wrapper du pipeline master pour logger le rc reel du bash -s).\n"
    "3) Meilleure logique prouvee (clause permanente) : UNE amelioration mesurable et bornee.\n"
    "4) Reserves.\n\n"
    "Perimetre impose : genesis INTACT (pas de modification de logique), lanceur INTACT pour "
    "l'instant — uniquement instrumentation d'observation + analyse. Le moteur est RENTABLE, "
    "on ne le casse pas.\n\n"
    "Reponds : (1) ligne/combinaison exacte + raisonnement ligne par ligne sur les preuves ; "
    "(2) correctif d'observation court ; (3) meilleure logique prouvee ; (4) reserves."
)

def ask():
    payload = {
        "task": "code.ia",
        "messages": [{"role": "user", "content": CONTEXTE}],
        "max_tokens": 1400,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?")

def main():
    try:
        content, provider = ask()
    except Exception as e:
        content, provider = f"ERREUR: {e}", "?"
    fn = f"{OUT}/CODEUR_TRACK_RC1.md"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(f"# CODEUR — traque ligne exacte rc=1 (14/08)\n\nProvider: {provider}\n\n{content}\n")
    print(f"CODEUR ({provider}) -> {len(content)} chars -> {fn}")

if __name__ == "__main__":
    main()
