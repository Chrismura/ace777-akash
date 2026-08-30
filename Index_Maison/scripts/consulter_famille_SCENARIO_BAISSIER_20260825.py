#!/usr/bin/env python3
"""
Consultation famille : analyse du scénario baissier et signaux non-mainstream
"""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
INDEX = Path(__file__).parent.parent
OUTPUT_DIR = INDEX / "scripts" / "CONSULTATION_FAMILLE_SCENARIO_BAISSIER_20260825"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PUSH = """
🎯 PUSH EXCELLENCE (Christophe) : Ta première réponse est le PLAFOND de ta pensée, pas le plancher.

Tu es un expert en macroéconomie, géopolitique et marchés crypto.

CONTEXTE :
On analyse la situation actuelle du BTC ($79K) et on envisage un scénario baissier pour les raisons suivantes :
1. **Kevin Warsh** (nouveau directeur Fed) est hawkish — "La Fed ne sauvera pas Bitcoin"
2. **Historique** : 4 directeurs sur 6 ont eu -20%+ en 1ère année
3. **Fear/Greed à 74** (Greed) — la foule est trop optimiste
4. **Baleines bearish** (court terme) — mouvements vers Coinbase
5. **Jackson Hole + Pleine Lune + Éclipse le 28 août** — convergence
6. **Dé-dollarisation** — le système financier mondial change

MAIS il y a aussi des raisons d'être haussier :
1. **Dé-dollarisation** = le BTC comme alternative au dollar
2. **Bitcoin Strategic Reserve** — les USA accumulent ?
3. **Adoption institutionnelle** croissante
4. **Offre limitée** (21M BTC) vs impression monétaire

QUESTION :
Qu'est-ce qu'on ne voit PAS ? Quels sont les signaux non-mainstream qui pourraient changer la donne ? Y a-t-il des fuites, des rumeurs, des données que le marché ignore ?

Pour chaque signal, donne :
1. La source (si possible)
2. Pourquoi c'est important
3. L'impact potentiel sur le prix
4. Le timing (quand ça pourrait arriver)

⚠️ Sois EXHAUSTIF. On veut voir ce que le marché ne voit pas.
"""

def consulter(membre, model):
    print(f"[BAISSIER] Consultation de {membre} ({model})...")
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": PUSH},
            {"role": "user", "content": "Qu'est-ce qu'on ne voit pas dans le marché crypto actuel ? Quels sont les signaux non-mainstream ?"},
        ],
        "max_tokens": 2500,
        "temperature": 0.4,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read().decode())
            txt = d["choices"][0]["message"]["content"].strip()
            prov = d.get("provider", "?")
            print(f"  ✅ {membre} : {len(txt)} caractères")
            return txt, prov
    except Exception as e:
        print(f"  ❌ {membre} : {e}")
        return f"Erreur: {e}", "error"

def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M")
    famille = [
        ("GEMINI", "google"),
        ("DEEPSEEK", "deepseek"),
        ("GROK", "grok"),
        ("INFERX", "inferx"),
        ("ULTRA", "ultra"),
        ("JUGE", "juge"),
    ]
    resultats = {}
    for nom, model in famille:
        txt, prov = consulter(nom, model)
        resultats[nom] = {"reponse": txt, "provider": prov}
    
    md = f"# 🔍 SCÉNARIO BAISSIER — ANALYSE FAMILLE\n"
    md += f"> Date : {now}\n\n"
    md += "## Question\n"
    md += "Qu'est-ce qu'on ne voit pas ? Quels sont les signaux non-mainstream ?\n\n"
    for nom, data in resultats.items():
        md += f"## {nom} ({data['provider']})\n\n{data['reponse']}\n\n---\n\n"
    
    out_file = OUTPUT_DIR / f"SCENARIO_BAISSIER_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    out_file.write_text(md, encoding="utf-8")
    print(f"\n[BAISSIER] Sauvegardé : {out_file}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
