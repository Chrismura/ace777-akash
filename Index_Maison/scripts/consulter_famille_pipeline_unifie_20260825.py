#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — PIPELINE DONNÉES UNIFIÉ (25/08/2026).
Avis seulement, rien n'est appliqué. Clause permanente gravée (16/08).
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_PIPELINE_20260825")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon pragmatique de la famille ACE777. Tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

BRIEF = """CONTEXTE (superviseur Buffy, 25/08/2026) — PIPELINE DONNÉES UNIFIÉ ACE777

=== LE PROBLÈME (Christophe + Buffy, diagnostic complet) ===
Le cockpit affiche des données via live.json (thermo), mais le pipeline est FRAGILE :

1. RACE CONDITION : 3 scripts écrivent dans live.json séparément :
   - thermo_quotidien_free.py (market: BTC, OI, funding, GEX, Fear/Greed) → cycle 5 min
   - pont_onchain.py (whales, cpfp, dust, blocs privatisés) → cycle 5 min
   - thermos间接 via d'autres scripts
   → Quand thermo écrit SANS pont_onchain, live.json.onchain = NULL pendant 5 min
   → Cortana/Ada voient des données vides et prennent des décisions à l'aveugle

2. DONNÉES NULL : GEX (Deribit) timeout parfois → ok:False → cockpit affiche "pas de mur"
   deriv_corr.json contient des données correctes MAIS n'est PAS dans live.json
   → 36 scripts lisent live.json, 0 ne lisent deriv_corr.json

3. AUTO-RÉPARATION ABSENTE : si un script crash, personne ne le relance
   sauf launchd (qui vérifie juste le PID, pas la qualité des données)
   → sante_index vérifie les fichiers MAIS pas la COMPLÉTUDE de live.json

4. COMPLEXITÉ : 3 scripts + 3 plists + 3 cycles = trop de moving parts
   pour une donnée qui doit être TOUJOURS fraîche et complète.

=== CE QUI EXISTE (vérifié) ===
- thermo_quotidien_free.py : 1120 lignes, fetch_fear_greed, fetch_liquidations_24h,
  fetch_etf_flows, fetch_gex_deribit, fetch_volume_caches, + scoring + write live.json
- pont_onchain.py : 300 lignes, lit whales_scan_latest.json + cpfp live + bloc privatisé
  → injecte section onchain dans live.json (原子ique)
- gen_deriv_corr.py : 200 lignes, corrélations 30j + carte liquidités → deriv_corr.json
- sante_index.py : vérifie 10 chaînes (maillon par maillon) → thermo/sante_index.json

=== LA CIBLE PROPOSÉE (Buffy) ===
UN SEUL script : thermo_live_unified.py qui :
1. Appelle TOUTES les sources en parallèle (Binance, Deribit, mempool, whales)
2. Écrit live.json en UNE SEULE opération atomique (jamais partiel)
3. Ajoute un champ "pipeline_health" avec l'état de chaque source :
   {"gex": "ok", "whales": "ok", "deriv": "stale", "cpfp": "error"}
4. Si une source échoue, garde la dernière valeur connue + flag "stale"
5. Sauto-revérifie : si live.json est vieux > 10 min → se relance
6. Intègre deriv_corr.json DANS live.json (plus de fichier séparé)

=== QUESTIONS POUR LA FAMILLE ===
1. Est-ce réaliste de fusionner 3 scripts en 1 sans casser les 36 consommateurs ?
2. Le parallel fetching est-il possible avec stdlib seule (urllib + threading) ?
3. Faut-il garder deriv_corr.json séparé (certains scripts le lisent) ?
4. Comment garantir que le pipeline ne JAMAIS écrit de données partielles ?
5. Le "pipeline_health" est-il suffisant ou faut-il un mécanisme plus robuste ?
6. Y a-t-il un piège que je ne vois pas dans cette fusion ?
"""


def appel_membre(membre, brief, timeout=60):
    nom, model, system = membre
    try:
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system + "\n\n" + CLAUSE},
                {"role": "user", "content": brief},
            ],
            "temperature": 0.3,
            "max_tokens": 2000,
        }).encode()
        req = urllib.request.Request(
            HUB,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=timeout) as r:
            resp = json.loads(r.read())
        duree = time.time() - t0
        texte = resp["choices"][0]["message"]["content"]
        return {"nom": nom, "ok": True, "texte": texte, "duree": round(duree, 1)}
    except Exception as e:
        return {"nom": nom, "ok": False, "texte": str(e), "duree": 0}


def main():
    print(f"=== CONSULTATION FAMILLE — PIPELINE DONNÉES UNIFIÉ ===")
    print(f"Membres : {len(MEMBRES)}")
    print()
    resultats = []
    for membre in MEMBRES:
        print(f"  → {membre[0]}...", end="", flush=True)
        r = appel_membre(membre, BRIEF)
        resultats.append(r)
        if r["ok"]:
            print(f" ✅ {r['duree']}s")
        else:
            print(f" ❌ {r['texte'][:80]}")
        time.sleep(0.5)

    # Sauvegarde
    out_data = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sujet": "Pipeline données unifié — race condition + données NULL + auto-réparation",
        "resultats": resultats,
    }
    out_path = os.path.join(OUT, "avis.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    # Rapport markdown
    md_lines = [
        "# CONSULTATION FAMILLE — PIPELINE DONNÉES UNIFIÉ",
        f"> {out_data['ts']}",
        "",
    ]
    for r in resultats:
        md_lines.append(f"## {r['nom']} {'✅' if r['ok'] else '❌'}")
        md_lines.append("")
        if r["ok"]:
            md_lines.append(r["texte"])
        else:
            md_lines.append(f"Erreur : {r['texte']}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_path = os.path.join(OUT, "AVIS PIPELINE UNIFIÉ_20260825.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== SAUVEGARDÉ ===")
    print(f"  {out_path}")
    print(f"  {md_path}")

    # Résumé rapide
    print(f"\n=== RÉSUMÉ ===")
    for r in resultats:
        if r["ok"]:
            premiere_ligne = r["texte"].split("\n")[0][:100]
            print(f"  {r['nom']}: {premiere_ligne}")


if __name__ == "__main__":
    main()
