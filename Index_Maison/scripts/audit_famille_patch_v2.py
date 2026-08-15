#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Famille 6/6 — validation du patch v2 (reset d'harmonie + double mort)."""
import json, time, urllib.request, os

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/VALIDATION_PATCH_V2_2026-08-14"
os.makedirs(OUT, exist_ok=True)

FAMILY = [
    ("famille", "gemini"),
    ("famille", "deepseek"),
    ("famille", "juge"),
    ("famille", "ultra"),
    ("famille", "inferx"),
    ("famille", "grok"),
]

CONTEXTE = (
    "VALIDATION PATCH v2 RELANCE DUO (14/08) — tu es membre de la famille ACE777 : GO / GO AVEC "
    "RESERVES / NON sur ce patch AVANT application sur le lanceur (genesis INTACT).\n\n"
    "RAPPEL du circuit : diagnostic famille 6/6 (AUDIT_RUN_DUO) -> JUGE valide la SPEC v2 -> "
    "codeur livre -> SUPERVISEUR applique la grille 1-4 en machine -> toi (famille) -> GO "
    "Christophe -> application reelle + retest.\n\n"
    "PROBLEME (constate 14/08) : la relance 4H (launch_vortex_v2_collab_4h_binance.sh) "
    "redemarrait ALPHA/BETA sans resynchroniser le contrat duo -> session #2 : ALPHA bloque en "
    "no_trigger/no_state 130+ cycles, zero fill, apres la mort en chaine de la session #1 "
    "(BETA shock_inversion_stop puis ALPHA duo stale_state).\n\n"
    "PATCH v2 (SPEC corrigee, codeur livre) :\n"
    "1) fonction reset_duo_harmony() definie DANS le lanceur (avant la boucle while true) : "
    "rm -f duo_state/duo_session + ecriture etat neutre "
    "{\"role\":\"INIT\",\"status\":\"RESET\",\"ts_ms\":0} + duo_session vierge + sync ; "
    "appelee au debut de CHAQUE iteration (juste apres attempt=$((attempt+1))).\n"
    "2) bloc double-mort apres rc=$? (avant le bloc STOP existant) : si PROCESS_EXIT.log "
    "contient BETA_X5 rc=1 ET ALPHA_X13_BURST13 rc=1 dans <300s (ruby -rtime avec rescue->0), "
    "alors touch STOP STOP_ALPHA STOP_BETA + break (pas de relance sur marche mort).\n"
    "3) AUCUN break sur rc=0 (le defaut v1 etait interdit et retire) : session propre rc=0 -> "
    "relance normale apres sleep 5 (comportement nominal inchange).\n\n"
    "POURQUOI v2 (corrections superviseur) : la v1 definissait la fonction dans GO_VORTEX_V2.sh "
    "avant `exec` -> les fonctions bash ne survivent pas a exec (prouve : command not found "
    "rc=127) -> le reset n'aurait JAMAIS eu lieu aux relances. La v2 definit la fonction dans le "
    "lanceur lui-meme : elle vit dans le meme processus que la boucle.\n\n"
    "GRILLE PASSEE EN MACHINE (superviseur, sur copie de test, vrai lanceur intouche) :\n"
    "- G1 bash -n : OK\n"
    "- G2 reset_duo_harmony CLI : duo_state={\"role\":\"INIT\",\"status\":\"RESET\",\"ts_ms\":0}, "
    "duo_session vierge, JSON valides\n"
    "- G3 double mort simulee (2 rc=1 dans <300s) : STOP + STOP_ALPHA + STOP_BETA poses, break\n"
    "- G4 session propre rc=0 simulee (harnais faux fortress) : 6 sessions relancees en boucle, "
    "ZERO STOP cree, duree atteinte -> fin propre. (Le defaut v1 aurait arrete des la session #1.)\n\n"
    "Perimetre : launch_vortex_v2_collab_4h_binance.sh UNIQUEMENT. genesis INTACT. GO_VORTEX_V2.sh "
    "INTACT. Backups .BAK_avant_reset_duo_<ts> avant application.\n\n"
    "VERIFIE : (1) le patch repond-il exactement au probleme (harmonie duo a la relance + stop sur "
    "marche mort) ? (2) la grille couvre-t-elle les risques (race window, double mort, rc=0) ? "
    "(3) y a-t-il un risque de regression sur le comportement nominal du lanceur ? "
    "(4) clause permanente : la meilleure logique est-elle prouvee (INIT/RESET > rm -f seul ; "
    "STOP sur double mort > relance infinie) ?\n\n"
    "Reponds : VERDICT (GO / GO AVEC RESERVES / NON) + reponse breve aux 4 points + reserves "
    "eventuelles (mineures = non bloquantes pour un retest)."
)

def ask(task, model):
    payload = {
        "task": task,
        "messages": [{"role": "user", "content": CONTEXTE}],
        "max_tokens": 900,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?")

def main():
    results = []
    for task, model in FAMILY:
        try:
            content, provider = ask(task, model)
        except Exception as e:
            content, provider = f"ERREUR: {e}", "?"
        verdict = "?"
        for v in ("GO AVEC RESERVES", "GO", "NON"):
            if v in content[:400]:
                verdict = v
                break
        fn = f"{OUT}/AVIS_{model.upper()}.md"
        with open(fn, "w", encoding="utf-8") as f:
            f.write(f"# AVIS FAMILLE {model.upper()} — patch v2 relance duo\n\nProvider: {provider}\n\n{content}\n")
        results.append((model, provider, verdict))
        print(f"[{model.upper()}] {provider} -> {verdict}")
        time.sleep(1)
    with open(f"{OUT}/SYNTHESE.md", "w", encoding="utf-8") as f:
        f.write("# SYNTHESE FAMILLE — patch v2 relance duo (14/08)\n\n")
        for m, p, v in results:
            f.write(f"- {m.upper()} ({p}) : {v}\n")
    print("\n=== SYNTHESE ===")
    for m, p, v in results:
        print(f"{m.upper():9s} {v}")

if __name__ == "__main__":
    main()
