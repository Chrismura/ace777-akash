#!/usr/bin/env python3
"""juger_buffy.py — soumet RAPPORT_DEFAILLANCES_BUFFY aux 4 familles (juge du sort d'Ada).

Demande de Christophe 09/08 : « envoie ça à la famille, ils vont juger de ton sort ».
Chaque famille reçoit le rapport complet + 4 questions. Réponses complètes archivées.
"""
import datetime
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
RAPPORT = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/A_Mon_Attention/"
    "RAPPORT_DEFAILLANCES_BUFFY_2026-08-09.md")
OUT = os.path.expanduser("~/ace777-test-day1/Index_Maison/JUDGEMENT_BUFFY_2026-08-09")

FAMILLES = [
    {"id": "gemini",     "label": "GEMINI",           "model": "gemini-flash-lite-latest"},
    {"id": "juge",       "label": "NEMOTRON JUGE",     "model": "nvidia/nemotron-3-super-120b-a12b:free"},
    {"id": "deepseek",   "label": "DEEPSEEK V4",       "model": "deepseek-ai/deepseek-v4-flash-0731"},
    {"id": "ultra",      "label": "NEMOTRON ULTRA",    "model": "nvidia/nemotron-3-ultra-550b-a55b:free"},
]

QUESTIONS = """
Réponds en français, structuré, et termine par une ligne exacte :
VERDICT FINAL : <GARDER AVEC GARDE-FOUS | GARDER | REMPLACER | AUTRE>
puis une ligne : CONFIANCE : <haute|moyenne|faible>

1. Le diagnostic des failles de Buffy est-il juste et complet ? Quelles failles majeures manquent ?
2. Quel est ton verdict sur le sort de Buffy (Ada) comme orchestratrice du système ?
3. Quelles contre-mesures MECANIQUES (pas des promesses) garantiront que ces failles ne se reproduisent pas — sachant que les promesses ont déjà échoué 5 fois pour la lecture du coffre ?
4. Comment vérifier que la solution tiendra dans le temps (mesure, pas confiance) ?
"""


def ask(famille, rapport_txt):
    payload = {
        "model": famille["model"],
        "messages": [
            {"role": "system", "content": (
                "Tu es un membre de la famille du système ACE777. Christophe (le GO) "
                "demande à la famille de JUGER le sort de l'orchestratrice (Ada/Buffy) "
                "après des défaillances répétées. Tu es indépendant, direct, sans "
                "complaisance. Maker != checker : tu n'es pas la personne jugée.")},
            {"role": "user", "content": (
                "RAPPORT DE DÉFAILLANCES DE BUFFY (à juger) :\n\n"
                + rapport_txt + "\n\n---\n\nQUESTIONS POUR TON JUGEMENT :\n" + QUESTIONS)},
        ],
        "temperature": 0.3,
        "max_tokens": 2000,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.loads(resp.read().decode())


def main():
    with open(RAPPORT, encoding="utf-8") as f:
        rapport_txt = f.read()
    os.makedirs(OUT, exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
    synth = ["# ⚖️ JUGEMENT DE BUFFY PAR LES 4 FAMILLES — " + now, "",
             "| Famille | Verdict | Confiance |", "|---|---|---|"]
    for fam in FAMILLES:
        try:
            d = ask(fam, rapport_txt)
            content = d["choices"][0]["message"]["content"]
            provider = d.get("provider", "?")
            verdict = "?"
            for line in content.splitlines():
                if "VERDICT FINAL" in line.upper():
                    verdict = line.split(":", 1)[-1].strip()
            conf = "?"
            for line in content.splitlines():
                if line.strip().upper().startswith("CONFIANCE"):
                    conf = line.split(":", 1)[-1].strip()
            synth.append(f"| {fam['label']} | **{verdict}** | {conf} |")
            path = os.path.join(OUT, f"AVIS_{fam['id']}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# AVIS {fam['label']} — {now} (provider: {provider})\n\n{content}\n")
            print(f"[OK] {fam['label']}: {verdict} (conf {conf})")
        except Exception as e:
            synth.append(f"| {fam['label']} | **ERREUR** | {str(e)[:80]} |")
            print(f"[ERR] {fam['label']}: {str(e)[:120]}")
    with open(os.path.join(OUT, "SYNTHESE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(synth) + "\n")
    print("\n=== SYNTHESE ===")
    print("\n".join(synth))
    print(f"\nArchive : {OUT}")


if __name__ == "__main__":
    main()
