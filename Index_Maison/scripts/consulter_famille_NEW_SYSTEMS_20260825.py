#!/usr/bin/env python3
"""
Consultation famille : quels sont les meilleurs systèmes IA open source de ce mois ?
On cherche des outils MEILLEURS que DeerFlow, Semble, Graphify pour notre architecture.
"""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
INDEX = Path(__file__).parent.parent
OUTPUT_DIR = INDEX / "scripts" / "CONSULTATION_FAMILLE_NEW_SYSTEMS_20260825"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PUSH = """
🎯 PUSH EXCELLENCE (Christophe) : Ta première réponse est le PLAFOND de ta pensée, pas le plancher. Si tu peux aller 30% plus loin — c'est CE niveau que je veux.

Tu es un expert en IA open source, frameworks d'agents, et architecture de systèmes autonomes.

CONTEXTE :
On évalue des outils IA open source pour un système de trading crypto autonome qui doit tourner 72h+ sans intervention. On a déjà trouvé :
- **DeerFlow** (ByteDance) : orchestrateur multi-agents, sous-agents, mémoire, sandboxes
- **Semble** : recherche de code par anglais naturel (99% moins de tokens)
- **Graphify** : knowledge graph local du codebase
- **System-Atlas** : cartes isométriques exploratoires
- **Ollama** : modèles locaux (Qwen 3.5 4B, etc.)

PROBLÈME :
Ces outils datent de quelques semaines/mois. Le domaine évolue VITE. On veut savoir :
1. Quels sont les NOUVEAUX systèmes (août 2026) qui ont émergé ?
2. Y a-t-il des alternatives MEILLEURES à DeerFlow ?
3. Y a-t-il des outils de mémoire/agent qui ont fait des bonds en avant ?
4. Qu'est-ce qu'on rate comme innovation récente ?

QUESTION :
Quels sont les 5 meilleurs systèmes IA open source de août 2026 pour :
1. L'orchestration d'agents (alternative à DeerFlow)
2. La mémoire long terme pour agents
3. La recherche de code intelligente
4. L'automatisation de tâches complexes
5. L'exécution de code en sandbox sécurisée

Pour chaque outil, donne :
- Nom et repo GitHub
- Pourquoi c'est mieux que ce qu'on a
- Date de sortie (si récent)
- Taille / ressources nécessaires

⚠️ Sois EXHAUSTIF. On ne veut pas rater la prochaine pépite.
"""

def consulter(membre, model):
    print(f"[NEW-SYSTEMS] Consultation de {membre} ({model})...")
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": PUSH},
            {"role": "user", "content": "Quels sont les meilleurs systèmes IA open source de août 2026 pour l'orchestration d'agents, la mémoire, et l'automatisation ?"},
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
    
    md = f"# 🔍 CONSULTATION FAMILLE — NOUVEAUX SYSTÈMES IA AOÛT 2026\n"
    md += f"> Date : {now}\n\n"
    md += "## Question\n"
    md += "Quels sont les meilleurs systèmes IA open source de août 2026 pour l'orchestration, la mémoire, et l'automatisation ?\n\n"
    for nom, data in resultats.items():
        md += f"## {nom} ({data['provider']})\n\n{data['reponse']}\n\n---\n\n"
    
    out_file = OUTPUT_DIR / f"NEW_SYSTEMS_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    out_file.write_text(md, encoding="utf-8")
    print(f"\n[NEW-SYSTEMS] Sauvegardé : {out_file}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
