#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Famille 8/8 — sensibilité moteur sur testnet + morts rc=1 (14/08, preuves à l'appui)."""
import json, time, urllib.request, os

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/CONSTAT_SENSIBILITE_8_2026-08-14"
os.makedirs(OUT, exist_ok=True)

# Famille 8 membres — noms courts routés par le hub (gratuits)
FAMILY = [
    ("famille", "gemini"),
    ("famille", "deepseek"),
    ("famille", "juge"),
    ("famille", "ultra"),
    ("famille", "inferx"),
    ("famille", "grok"),
    ("famille", "nvidia"),
    ("famille", "oss20"),
]

CONTEXTE = (
    "CONSTATATION SENSIBILITE MOTEUR + MORTS RC=1 (14/08) — tu es membre de la famille ACE777. "
    "On ne te demande PAS de valider un patch : on te demande ton DIAGNOSTIC SUR DEUX QUESTIONS "
    "LIEES, avec les preuves, puis ta recommandation (réglage et/ou correctif, borné).\n\n"
    "CLAUDE PERMANENTE (Christophe, 14/08 — à respecter à CHAQUE intervention) :\n"
    "« Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible. »\n"
    "-> Ne propose PAS une rustine : PROUVE avec les preuves, et propose UNE amélioration si elle "
    "est prouvée (mesurable, bornée).\n\n"
    "================ CONTEXTE (vérifié superviseur, 14/08) ================\n\n"
    "TOUT EST SUR TESTNET (décision Christophe : pas de feed réel). Le moteur (genesis) tourne "
    "via master v8_5 / GEMINI_TEST, duo BETA (SCOUT, x5, SHORT) + ALPHA (HUNTER, x13, LONG).\n\n"
    "QUESTION 1 — SENSIBILITE :\n"
    "- La tension est calculée comme chute de mur du book / 6.5 (IMPULSE_RESONANCE_WALL_DROP_PCT), "
    "entre 2 snapshots de depth à ~128 ms d'écart (IMPULSE_RESONANCE_DT_MS).\n"
    "- Le serveur testnet est LENT : 1.35 s/requête en moyenne (20 mesures, max 9.7 s) vs api réel "
    "464 ms. Les cycles du bot prennent ~8 s au lieu de ~1 s.\n"
    "- Le testnet bouge PAR VAGUES (pas un désert) : 526 FILLED le 13/08, 87 le 14/08, tensions "
    "1-12 vues par ALPHA ce matin. Preuve 10:41:56 : BETA voit chute de mur 70% (tension 10.8) "
    "et trade ; ALPHA 1 s après ne voit plus que 6% (tension 0.95) -> SKIP. La fenêtre de 128 ms "
    "rate la plupart des rafales.\n"
    "- Constat : quand le testnet bouge, le moteur trade et bien (BETA 16 fills à 10h, ALPHA 3 fills "
    "à 09:21-09:22 avec tension jusqu'à 6.26). Le 0.000000 vu dans les CSV = accalmies du testnet + "
    "fenêtre trop courte.\n"
    "- La connexion wifi/carte téléphonique de Christophe n'est PAS la cause (ping 0% perte, api "
    "réel rapide, testnet lent côté serveur).\n\n"
    "QUESTION 2 — MORTS RC=1 SILENCIEUSES (l'anomalie restante) :\n"
    "- Le run 4H du 14/08 (session #1 08:31Z et #2 08:52Z) a fait 4 morts rc=1, même signature : "
    "dernier cycle loggé -> 3-8 s de silence -> mort PENDANT le cycle suivant (jamais loggé).\n"
    "- ZERO FATAL_RC1 (trap ERR actif jamais tiré), ZERO WARN safe_call du run, stderr = 0 octet, "
    "pas de « Done. » avant les morts (donc pas une fin naturelle). Le master a pipefail actif ; "
    "le bash -s sort réellement rc=1 sans message.\n"
    "- L'instrumentation trap EXIT+DEBUG (validée 6/6 + codeur, testée en machine) est en place "
    "dans le master, mais les 2 premiers runs de capture ont été tués par l'outil terminal du "
    "superviseur (erreur outillage, prouvée), pas par le moteur. Le run de 20 min détaché (10:32Z) "
    "a fini PROPREMENT rc=0 (ALPHA +115.67, BETA +10.96, zéro PROCESS_EXIT rc=1) — donc la cause "
    "n'a pas encore été recapturée.\n\n"
    "================ QUESTION ================\n"
    "1) CAUSE RACINE du 0.000000 (faible taux de fill) : la fenêtre 128 ms + seuil 6.5% sont-ils "
    "adaptés à un testnet LENT qui bouge par vagues ? PROPOSE un réglage précis (DT_MS ? seuil "
    "wall_drop ? autre) avec la justification chiffrée.\n"
    "2) CAUSE RACINE probable des morts rc=1 silencieuses (à 8 s du dernier cycle loggé, sans "
    "échec de commande ni exit explicite) : quelle hypothèse est la plus probable, et quel "
    "correctif d'observation/correctif le plus court pour la capturer à coup sûr ?\n"
    "3) Meilleure logique prouvée (clause permanente) : UNE amélioration mesurable et bornée.\n"
    "4) Réserves éventuelles.\n\n"
    "Périmètre imposé : genesis INTACT (pas de modification de logique), lanceur INTACT pour "
    "l'instant — uniquement réglages de paramètres (variables d'environnement) + instrumentation "
    "d'observation + analyse.\n\n"
    "Réponds : (1) cause racine + réglage précis chiffré ; (2) cause des morts + correctif court ; "
    "(3) meilleure logique prouvée ; (4) réserves."
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
            f.write(f"# DIAG FAMILLE {model.upper()} — sensibilité + morts rc=1 (14/08)\n\nProvider: {provider}\n\n{content}\n")
        results.append((model, provider, len(content)))
        print(f"[{model.upper()}] {provider} -> {len(content)} chars")
        time.sleep(1)
    with open(f"{OUT}/SYNTHESE.md", "w", encoding="utf-8") as f:
        f.write("# SYNTHESE FAMILLE 8/8 — sensibilité + morts rc=1 (14/08)\n\n")
        for m, p, c in results:
            f.write(f"- {m.upper()} ({p}) : {c} chars\n")
    print("\n=== SYNTHESE ===")
    for m, p, c in results:
        print(f"{m.upper():9s} {p} ({c} chars)")

if __name__ == "__main__":
    main()
