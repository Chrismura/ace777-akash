#!/usr/bin/env python3
"""
Flotille F2 : Connexion du sniffer au pipeline de trading temps réel
"""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
INDEX = Path(__file__).parent.parent
OUTPUT_DIR = INDEX / "scripts" / "CONSULTATION_FAMILLE_F2_20260825"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PUSH = """
🎯 PUSH EXCELLENCE (Christophe) : Ta première réponse est le PLAFOND de ta pensée, pas le plancher. Si tu peux aller 30% plus loin — c'est CE niveau que je veux.

Tu es un expert en architecture de systèmes de trading temps réel.

CONTEXTE :
On a un système de trading crypto avec :
- Un bot (Hulk) qui gère un portefeuille de 15 positions
- Un pipeline de données (thermo → live.json) qui tourne toutes les 5 min
- Un "sniffer" qui compare le BRUT (données onchain) avec le NARRATIF (titres médiatiques Google News)
- Le sniffer utilise DeepSeek V4 pour analyser la divergence brut vs narratif

PROBLÈME :
Le sniffer tourne en manuel. Il faut le connecter au pipeline pour qu'il tourne automatiquement et nourrisse Hulk de signaux de divergence.

CONTRAINTE CRITIQUE :
Le sniffer appelle le Hub ACE (DeepSeek V4) — chaque appel coûte du temps et des tokens. On ne peut PAS appeler le Hub toutes les 5 minutes pour chaque paire.

QUESTION :
Comment connecter le sniffer au pipeline de trading de façon EFFICACE ? Pour chaque solution, explique :
1. L'architecture technique (fichiers, flux, fréquence)
2. Le coût (nombre d'appels Hub par heure)
3. La latence (combien de temps entre le signal et l'action de Hulk)
4. Les risques de false positives et comment les mitiger

⚠️ NE PARTAGEZ PAS de stratégies de trading. Proposez des ARCHITECTURES de connexion, pas des règles d'entrée/sortie.

Sois concret. Donne du code ou des pseudo-code.
"""

def consulter(membre, model):
    print(f"[F2] Consultation de {membre} ({model})...")
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": PUSH},
            {"role": "user", "content": "Comment connecter un sniffer de divergence narratif à un pipeline de trading temps réel ?"},
        ],
        "max_tokens": 2000,
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
    
    md = f"# 🚢 FLOTILLE F2 — Connexion Sniffer au Pipeline\n"
    md += f"> Date : {now}\n\n"
    for nom, data in resultats.items():
        md += f"## {nom} ({data['provider']})\n\n{data['reponse']}\n\n---\n\n"
    
    out_file = OUTPUT_DIR / f"F2_CONNEXION_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    out_file.write_text(md, encoding="utf-8")
    print(f"\n[F2] Sauvegardé : {out_file}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
