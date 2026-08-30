#!/usr/bin/env python3
"""
Consultation famille : comment DeerFlow peut intégrer et améliorer le cockpit ACE
"""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
INDEX = Path(__file__).parent.parent
OUTPUT_DIR = INDEX / "scripts" / "CONSULTATION_FAMILLE_DEERFLOW_20260825"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PUSH = """
🎯 PUSH EXCELLENCE (Christophe) : Ta première réponse est le PLAFOND de ta pensée, pas le plancher. Si tu peux aller 30% plus loin — c'est CE niveau que je veux.

Tu es un expert en architecture de systèmes de trading et d'automatisation IA.

CONTEXTE :
On a un système de trading crypto (ACE777) avec :
- Un pipeline de données (thermo → live.json) qui tourne toutes les 5 min
- Un bot de trading (Hulk) qui gère 15 positions
- Un système d'analyse (Cortana) qui évalue les signaux
- Des alertes vocales quand il y a un danger
- Des consultations famille pour les décisions importantes

On a trouvé **DeerFlow** (https://github.com/bytedance/deer-flow) — un super agent open source de ByteDance qui peut :
- Investiguer à fond des sujets
- Écrire et exécuter du code
- Créer des présentations, vidéos, images
- Automatiser des tâches complexes multi-étapes
- Utiliser des sous-agents en parallèle
- Travailler dans des sandboxes isolées
- Mémoire à long terme
- Fonctionne avec des modèles locaux (Ollama) ou en cloud

PROBLÈME :
Notre système fonctionne mais il est composé de beaucoup de scripts séparés. DeerFlow pourrait potentiellement :
1. Simplifier l'architecture (moins de scripts, plus de cohérence)
2. Améliorer la fiabilité (sandbox, mémoire, sous-agents)
3. Rendre le système "incassable" (auto-réparation, supervision)

QUESTION :
Comment DeerFlow peut-il nous aider concrètement ? Pour chaque composant, explique :
1. Ce que DeerFlow pourrait remplacer ou améliorer
2. L'architecture d'intégration (comment le brancher)
3. Les risques et les garde-fous
4. Le gain attendu (fiabilité, performance, simplicité)

⚠️ NE PARTAGE PAS de stratégies de trading. Propose des ARCHITECTURES d'intégration.

Sois exhaustif. Pense à la stabilité à long terme (72h+ de prod sans intervention).
"""

def consulter(membre, model):
    print(f"[DEERFLOW] Consultation de {membre} ({model})...")
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": PUSH},
            {"role": "user", "content": "Comment DeerFlow peut-il intégrer et améliorer notre système de trading crypto ?"},
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
    
    md = f"# 🦌 CONSULTATION FAMILLE — DEERFLOW × ACE777\n"
    md += f"> Date : {now}\n\n"
    md += "## Question\n"
    md += "Comment DeerFlow peut-il intégrer et améliorer notre système de trading crypto ?\n\n"
    for nom, data in resultats.items():
        md += f"## {nom} ({data['provider']})\n\n{data['reponse']}\n\n---\n\n"
    
    out_file = OUTPUT_DIR / f"DEERFLOW_CONSULTATION_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    out_file.write_text(md, encoding="utf-8")
    print(f"\n[DEERFLOW] Sauvegardé : {out_file}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
