#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Famille + Codeur — MÉTA-ANALYSE des audits (20/08, demande Christophe).

Envoie INDEX_AUDITS_ET_META_ANALYSE (classes de trous + pattern) à :
- 1 CODEUR : proposer la brique générique « détection de dégradation » (C1)
- 6 membres FAMILLE : confirmer/infirmer le pattern, affiner la correction systémique
Sorties : Index_Maison/META_AUDIT_2026-08-20/{CODEUR,DIAG_*}.md + SYNTHESE.md
"""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
OUT = f"{ROOT}/Index_Maison/META_AUDIT_2026-08-20"
os.makedirs(OUT, exist_ok=True)

META = open(f"{ROOT}/Index_Maison/INDEX_AUDITS_ET_META_ANALYSE_2026-08-20.md",
            encoding="utf-8").read()

FAMILY = [
    ("famille", "gemini"),
    ("famille", "deepseek"),
    ("famille", "juge"),
    ("famille", "ultra"),
    ("famille", "inferx"),
    ("famille", "grok"),
]

CONTEXTE = (
    "MÉTA-ANALYSE DES AUDITS ACE777 (20/08) — tu es membre de la famille ACE777. "
    "Nous avons fait 484 documents d'audit (109 propres + 375 avis famille) depuis "
    "le 29/07. Nous avons croisé les CAUSES RACINES et dégagé 4 classes de trous :\n"
    "1. DÉGRADATION SILENCIEUSE : chaque organe peut tomber ou se tromper sans que "
    "rien ne crie (mort rc=1 sans alerte 14/08, vigie morte 19/08, filet qui échoue "
    "loggé mais invisible, champion patché en plein run chargé silencieusement).\n"
    "2. GARDE-FOU ÉCRIT MAIS PAS ACTIF : plists vigie-live, superviseur-process, "
    "superviseur-core écrites mais JAMAIS chargées ; sante_index oubliait la vigie "
    "marché.\n"
    "3. FAUSSE SÉCURITÉ : filet à 8 bps refusé par Binance (-2021) mais le bot CROIT "
    "être protégé ; indicateur blocs privatisés mal calibré (résolution 10 min) "
    "affichait 34 % de bruit ; PnL BRUT +14 alors que NET −278.\n"
    "4. VUE PARTIELLE : 109 audits propres et AUCUN index unique — le pattern était "
    "invisible faute de vue d'ensemble (créé aujourd'hui).\n\n"
    "PATTERN EN UNE PHRASE : « Nous créons beaucoup, vérifions peu, et les "
    "défaillances sont silencieuses : chaque organe peut tomber ou se tromper sans "
    "alerte, avec une fausse sécurité issue de mesures mal calibrées. »\n\n"
    "CLAUDE PERMANENTE (Christophe) : « Prouve la meilleure logique et applique-la "
    "dans la correction et l'amélioration si possible. » Pas de rustine : PROUVE.\n\n"
    "================ MÉTA-ANALYSE COMPLÈTE ================\n"
    f"{META}\n\n"
    "QUESTION FAMILLE : (1) Le pattern des 4 classes est-il juste et complet ? "
    "(2) Quelle classe est la PLUS dangereuse et pourquoi ? (3) Quelle correction "
    "SYSTÉMIQUE (pas rustine) recommandes-tu, mesurable et bornée ? "
    "(4) Réserves. Périmètre : genesis INTACT (C1), wrappers/molettes seulement.\n"
    "Réponds en français, factuel, 4 sections."
)

CONTEXTE_CODEUR = (
    "MÉTA-ANALYSE DES AUDITS ACE777 (20/08) — tu es le CODEUR senior ACE777. "
    "Le pattern dominant trouvé après 484 audits : DÉGRADATION SILENCIEUSE — chaque "
    "organe (vigie, filet, champion, indicateur) peut tomber ou se tromper sans "
    "alerte, avec une fausse sécurité issue de mesures mal calibrées.\n\n"
    "================ MÉTA-ANALYSE COMPLÈTE ================\n"
    f"{META}\n\n"
    "RÈGLES DE CODE ACE777 : Python 3.9+ stdlib uniquement, écriture ATOMIQUE, "
    "kill-switch (Index_Maison/strategie/STOP + Index_Maison/STOP_ALL), robustesse "
    "sans crash, idempotence, NE PAS toucher au genesis (C1) ni au moteur Hulk.\n\n"
    "TÂCHE : propose une brique GÉNÉRIQUE et LÉGÈRE (un script + plist launchd, "
    "pattern existant) de « DÉTECTION DE DÉGRADATION » qui vérifie en continu :\n"
    "  (a) les plists critiques attendues sont CHARgÉES (launchctl) — classe 2 ;\n"
    "  (b) les fichiers heartbeat/état sont FRAIS (âge ≤ seuil) — classe 1 ;\n"
    "  (c) les indicateurs actifs sont dans leur plage de calibration (déviation "
    "  anormale → alerte) — classe 3 ;\n"
    "  (d) sort un rapport JSON lisible par sante_index/cockpit (1 place/info).\n"
    "Donne : chemin du fichier, bloc ```python complet, et NOTES (choix, seuils, "
    "coût, intégration). Réponds en français."
)

def ask(task, model, max_tokens):
    payload = {
        "task": task,
        "messages": [{"role": "user", "content": CONTEXTE if task == "famille"
                      else CONTEXTE_CODEUR}],
        "max_tokens": max_tokens,
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
    # 1) CODEUR
    try:
        content, provider = ask("codeur", "code", 6000)
        with open(f"{OUT}/CODEUR.md", "w", encoding="utf-8") as f:
            f.write(f"# CODEUR — brique détection de dégradation (20/08)\n\nProvider: {provider}\n\n{content}\n")
        results.append(("CODEUR", provider, len(content)))
        print(f"[CODEUR] {provider} -> {len(content)} chars")
    except Exception as e:
        print(f"[CODEUR] ERREUR: {e}")
    time.sleep(2)
    # 2) FAMILLE
    for task, model in FAMILY:
        try:
            content, provider = ask(task, model, 1400)
        except Exception as e:
            content, provider = f"ERREUR: {e}", "?"
        with open(f"{OUT}/DIAG_{model.upper()}.md", "w", encoding="utf-8") as f:
            f.write(f"# DIAG FAMILLE {model.upper()} — méta-analyse audits (20/08)\n\nProvider: {provider}\n\n{content}\n")
        results.append((model.upper(), provider, len(content)))
        print(f"[{model.upper()}] {provider} -> {len(content)} chars")
        time.sleep(1)
    with open(f"{OUT}/SYNTHESE.md", "w", encoding="utf-8") as f:
        f.write("# SYNTHESE — méta-analyse audits (famille + codeur) 20/08\n\n")
        for m, p, c in results:
            f.write(f"- {m} ({p}) : {c} chars\n")
    print("\n=== SYNTHESE ===")
    for m, p, c in results:
        print(f"{m:9s} {p} ({c} chars)")

if __name__ == "__main__":
    main()
