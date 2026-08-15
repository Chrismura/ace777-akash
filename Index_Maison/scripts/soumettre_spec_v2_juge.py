#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soumettre SPEC v2 (corrigée) au JUGE — validation avant envoi codeur."""
import json, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"

CONTEXTE = (
    "VALIDATION SPEC v2 RELANCE DUO (14/08) — tu es le JUGE : GO / GO AVEC RESERVES / NON "
    "sur cette SPEC CORRIGEE avant envoi au codeur.\n\n"
    "POURQUOI v2 (supervision, preuves) : la SPEC v1 a ete soumise au codeur ; le patch "
    "retourne avait 2 defauts. 1) La fonction reset_duo_harmony etait definie dans "
    "GO_VORTEX_V2.sh avant `exec` du lanceur — or exec remplace le processus, les fonctions "
    "bash ne survivent pas (prouve machine : command not found rc=127) -> la relance (sessions "
    "#2+) n'aurait jamais le reset. Correction : la fonction est definie DANS le lanceur, "
    "GO_VORTEX_V2.sh reste inchange. 2) Le codeur avait ajoute `[ \"$rc\" -eq 0 ] && break` "
    "hors SPEC (changement du comportement nominal : session propre rc=0 arreterait le run) -> "
    "interdit explicitement dans la v2.\n\n"
    "VERIFIE : (a) le placement de la fonction est-il correct maintenant (dans le lanceur, avant "
    "la boucle while true) ? (b) le bloc double-mort est-il bien apres rc=$? et avant le bloc "
    "STOP existant ? (c) la clause INTERDIT preserve-t-elle le comportement nominal (pas de "
    "break rc=0) ? (d) la grille de test 1-5 couvre-t-elle les 2 defauts v1 ?\n\n"
    "SPEC v2 (contenu) :\n"
    "- Cible : launch_vortex_v2_collab_4h_binance.sh UNIQUEMENT. GO_VORTEX_V2.sh : aucune "
    "modification. genesis INTANGIBLE.\n"
    "- 2.1 fonction reset_duo_harmony definie avant la boucle, appelee au debut de chaque "
    "iteration : rm -f duo_state/duo_session + ecriture etat neutre "
    "{\"role\":\"INIT\",\"status\":\"RESET\",\"ts_ms\":0} + duo_session vierge + sync.\n"
    "- 2.2 apres rc=$? : si PROCESS_EXIT.log contient BETA_X5 rc=1 ET ALPHA_X13_BURST13 rc=1 "
    "dans les 300s (ruby -rtime, rescue->0), touch STOP STOP_ALPHA STOP_BETA + break. "
    "Ruby dispo, bash 3.2, pas de mapfile/date -d.\n"
    "- INTERDIT : aucun break sur rc=0. Comportement nominal inchange (STOP -> break ; duree -> "
    "break ; sinon relance apres sleep 5).\n"
    "- Clause permanente : prouver la meilleure logique + 1 amelioration prouvee max.\n"
    "- Grille : 1) bash -n 2) reset_duo_harmony CLI -> INIT/RESET 3) double mort simulee -> STOP "
    "4) session propre rc=0 -> pas de STOP, relance inchangee 5) retest reel.\n\n"
    "Reponds : VERDICT (GO / GO AVEC RESERVES / NON) + pour chaque point (a)(b)(c)(d) : "
    "OK ou reserve. Si reserve : la correction minimale demandee. "
    "Prouve ta meilleure logique si possible, applique-la dans ta reponse."
)

def main():
    payload = {
        "task": "juge",
        "messages": [{"role": "user", "content": CONTEXTE}],
        "max_tokens": 1600,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    import os
    out = "/Users/christophe/ace777-test-day1/Index_Maison/AVIS_JUGE_SPEC_V2.md"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# AVIS JUGE — SPEC v2 relance duo\n\nProvider: {provider}\n\n{content}\n")
    print(f"[JUGE] provider={provider}")
    print(content[:3000])

if __name__ == "__main__":
    main()
