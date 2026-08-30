#!/usr/bin/env python3
"""
Flotille F1 : Sources gratuites pour détecter les mouvements silencieux de baleines
Consulte la famille avec le prompt spécial PUSH EXCELLENCE
"""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
INDEX = Path(__file__).parent.parent
OUTPUT_DIR = INDEX / "scripts" / "CONSULTATION_FAMILLE_F1_20260825"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Prompt spécial PUSH EXCELLENCE (Christophe)
PUSH = """
🎯 PUSH EXCELLENCE (Christophe) : Ta première réponse est le PLAFOND de ta pensée, pas le plancher. Si tu peux aller 30% plus loin en complexité, en robustesse, ou en originalité — c'est CE niveau que je veux. Une réponse confortable est une réponse ratée. Reprends ta réponse et ajoute ce que tu n'as pas osé dire la première fois.

Tu es un expert en blockchain analytics et détection de mouvements de baleines.

CONTEXTE :
Un trader crypto utilise un système de détection de mouvements silencieux de baleines. Le système actuel surveille :
- Les frais mempool (z-score CPFP)
- Les micro-transactions (dust score)
- L'entropie de la mempool
- La divergence BTC dormant vs frais

PROBLÈME :
Les baleines savent qu'elles sont traquées. Elles ne bougent plus en blocs visibles (>1000 BTC). Elles fragmentent en micro-tx, paient peu de frais, et agissent aux heures creuses.

QUESTION :
Quelles sont les MEILLEURES sources de données GRATUITES (sans clé API payante) pour détecter ces mouvements silencieux ? Pour chaque source, explique :
1. Ce qu'elle mesure exactement
2. Pourquoi c'est plus difficile à manipuler que les montants bruts
3. Comment l'intégrer dans un pipeline temps réel (cycle 5-10 min)
4. Les limites et risques de false positives

⚠️ NE PARTAGEZ PAS de formules de scoring. Proposez des sources et des approches, pas des algorithms propriétaire.

Sois exhaustif. Cite des APIs concrètes avec leurs URLs.
"""

def consulter(membre, model):
    """Consulte un membre de la famille"""
    print(f"[F1] Consultation de {membre} ({model})...")
    
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": PUSH},
            {"role": "user", "content": "Donne-moi ta meilleure réponse sur les sources gratuites pour détecter les baleines silencieuses."},
        ],
        "max_tokens": 2000,
        "temperature": 0.4,
    }).encode()
    
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read().decode())
            txt = d["choices"][0]["message"]["content"].strip()
            provider = d.get("provider", "?")
            print(f"  ✅ {membre} : {len(txt)} caractères (via {provider})")
            return txt, provider
    except Exception as e:
        print(f"  ❌ {membre} : {e}")
        return f"Erreur: {e}", "error"

def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M")
    
    # Famille avec modèles variés
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
    
    # Assemblage
    md = f"# 🚢 FLOTILLE F1 — Sources Gratuites Baleines Silencieuses\n"
    md += f"> Date : {now}\n\n"
    
    for nom, data in resultats.items():
        md += f"## {nom} ({data['provider']})\n\n"
        md += f"{data['reponse']}\n\n---\n\n"
    
    # Sauvegarde
    out_file = OUTPUT_DIR / f"F1_SOURCES_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    out_file.write_text(md, encoding="utf-8")
    print(f"\n[F1] Sauvegardé : {out_file}")
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
