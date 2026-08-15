#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Famille 6/6 — constatation morts silencieuses 14/08 (preuves a l'appui)."""
import json, time, urllib.request, os

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/CONSTAT_MORTS_SILENCIEUSES_2026-08-14"
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
    "CONSTATATION MORTS SILENCIEUSES (14/08) — tu es membre de la famille ACE777. "
    "On ne te demande PAS de valider un patch : on te demande ton DIAGNOSTIC SUR LA "
    "CAUSE RACINE de morts en cascade que nos outils n'arrivent pas a intercepter, "
    "puis ta recommandation (quel correctif d'observation/correctif, borne, genesis "
    "intact).\n\n"
    "CLAUDE PERMANENTE (Christophe, 14/08 — a respecter a CHAQUE intervention) :\n"
    "« Prouve la meilleure logique et applique-la dans la correction et "
    "l'amelioration si possible. »\n"
    "-> Ne propose PAS une rustine : PROUVE la cause racine avec les preuves, et "
    "propose UNE amelioration si elle est prouvee (mesurable, bornee).\n\n"
    "================ PREUVES (verifiees superviseur, dossier AUDIT_MORT_SILENCIEUSE_2026-08-14) ================\n\n"
    "LE RUN 4H DU 14/08 (launch_vortex_v2_collab_4h_binance.sh) a fait 3 sessions :\n"
    "- Session #1 (08:31:37Z) : BETA mort 08:49:29Z rc=1, ALPHA mort 08:52:26Z rc=1\n"
    "- Session #2 (08:52:33Z) : ALPHA mort 09:25:05Z rc=1, BETA mort 09:29:20Z rc=1\n"
    "- Session #3 (09:29:xxZ) : fin propre rc=0 a 09:31Z (duree atteinte)\n\n"
    "LES 4 MORTS — MEME SIGNATURE EXACTE (extraits des crash dumps) :\n"
    "1) BETA #1 : dernier cycle logge 08:49:26 #92 SKIP -> mort 08:49:29 (3 s de silence)\n"
    "2) ALPHA #1 : dernier cycle logge 08:52:18 #108 SKIP | duo stale_state -> mort 08:52:26 (8 s)\n"
    "3) ALPHA #2 : dernier cycle logge 09:24:57 #203 SKIP -> mort 09:25:05 (8 s)\n"
    "4) BETA #2 : dernier cycle logge 09:29:13 #214 SKIP Mode Ecoute -> mort 09:29:20 (7 s)\n"
    "=> Chaque mort survient PENDANT le cycle suivant (jamais logge), 3-8 s apres le "
    "dernier cycle logge. Le PROCESS_EXIT.log confirme how=pipe_run_unit why=rc_1 rc=1.\n\n"
    "PREUVES D'ABSENCE (ce qui NE s'est PAS passe) :\n"
    "- ZERO FATAL_RC1 : le trap ERR (ligne 90 du champion, active dans la partie "
    "executee tail -n +85) n'a JAMAIS tire -> AUCUNE commande n'a echoue sous set -e.\n"
    "- ZERO WARN safe_call du run : les 3 warnings de /tmp/ace777_fatal_rc1.log sont "
    "les TESTS G2/G3 du superviseur, pas le run. /tmp/ace777_stderr_debug.log = 0 octet.\n"
    "- Les seuls exit 1 du code execute (lignes 367 BASE_URL, 1492 leverage) sont au "
    "DEMARRAGE, pas dans la boucle.\n"
    "- Le master lance les bots via tail -n +85 genesis | bash -s (pipefail actif) : "
    "le bash -s sort reellement rc=1, sans message.\n\n"
    "RESPONSABILITE SUPERVISEUR (transparence) : mon test G2 a ecrit INIT/RESET dans "
    "runs/duo_state.json a 09:24:22Z (43 s avant la mort ALPHA #2 a 09:25:05Z). Mais la "
    "session #1 (morts 08:49/08:52) est morte du MEME pattern sans AUCUNE interference "
    "-> la cause est intrinseque, independante de mon test.\n\n"
    "QUESTION : quelle est la CAUSE RACINE de ces sorties rc=1 silencieuses pendant un "
    "cycle (ni echec de commande, ni exit 1 du code, ni kill visible) ? Propose le "
    "correctif d'observation le plus court pour CAPTURER la cause (trap EXIT qui loggue "
    "rc + ligne + derniere commande ? PS4/set -x sur la fenetre du cycle ? autre ?) et "
    "la correction si tu peux la PROUVER des maintenant.\n\n"
    "Perimetre impose : genesis INTACT (pas de modification de logique), lanceur "
    "INTACT pour l'instant — uniquement instrumentation d'observation + analyse.\n\n"
    "Reponds : (1) CAUSE RACINE (hypothese + raisonnement sur les preuves) ; "
    "(2) CORRECTIF D'OBSERVATION recommande (borne, mince) ; (3) meilleure logique "
    "prouvee (clause permanente) ; (4) reserves eventuelles."
)

def ask(task, model):
    payload = {
        "task": task,
        "messages": [{"role": "user", "content": CONTEXTE}],
        "max_tokens": 1100,
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
        fn = f"{OUT}/DIAG_{model.upper()}.md"
        with open(fn, "w", encoding="utf-8") as f:
            f.write(f"# DIAG FAMILLE {model.upper()} — morts silencieuses 14/08\n\nProvider: {provider}\n\n{content}\n")
        results.append((model, provider, len(content)))
        print(f"[{model.upper()}] {provider} -> {len(content)} chars")
        time.sleep(1)
    with open(f"{OUT}/SYNTHESE.md", "w", encoding="utf-8") as f:
        f.write("# SYNTHESE FAMILLE — morts silencieuses 14/08\n\n")
        for m, p, c in results:
            f.write(f"- {m.upper()} ({p}) : {c} chars\n")
    print("\n=== SYNTHESE ===")
    for m, p, c in results:
        print(f"{m.upper():9s} {p} ({c} chars)")

if __name__ == "__main__":
    main()
