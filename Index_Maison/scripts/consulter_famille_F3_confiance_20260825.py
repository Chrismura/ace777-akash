#!/usr/bin/env python3
"""
Flotille F3 : Score de confiance — peut-on trader sur ces données ?
"""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
INDEX = Path(__file__).parent.parent
OUTPUT_DIR = INDEX / "scripts" / "CONSULTATION_FAMILLE_F3_20260825"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PUSH = """
🎯 PUSH EXCELLENCE (Christophe) : Ta première réponse est le PLAFOND de ta pensée, pas le plancher. Si tu peux aller 30% plus loin — c'est CE niveau que je veux.

Tu es un expert en risk management et data quality pour le trading algorithmique.

CONTEXTE :
Un bot de trading crypto reçoit des données de 7 sources différentes :
1. Binance API (prix, funding, OI) — latence ~100ms
2. Mempool.space (CPFP, dust, frais) — latence ~2s
3. Alternative.me (Fear/Greed) — latence ~1s, mis à jour 1x/jour
4. Deribit (options, GEX) — latence ~500ms, parfois timeout
5. Blockchain.com (BTC dormant) — latence ~3s, parfois 404
6. Google News RSS (narratif) — latence ~2s, parfois bloqué
7. SDI/IPT (calcul local) — latence ~5s

CONTRAINTE :
Le bot trade avec de l'ARGENT RÉEL. Une donnée fausse ou stale peut coûter cher.

PROBLÈME :
Certaines sources sont fiables 99% du temps (Binance), d'autres timeout aléatoirement (Deribit, Blockchain.com). Le bot doit savoir QUAND il peut faire confiance aux données et QUAND il doit s'arrêter.

QUESTION :
Comment construire un SCORE DE CONFIANCE (pipeline_health) qui évalue en temps réel la fiabilité de chaque source ? Pour chaque source, définis :
1. Le critère de fraîcheur (TTL max acceptable)
2. Le critère de cohérence (comment détecter une donnée absurde)
3. Le score de confiance (0-1) et ce qui le fait baisser
4. L'action quand le score est bas (gel trading ? réduction des tailles ? alerte ?)

⚠️ NE PARTAGEZ PAS de stratégies de trading. Proposez un SYSTÈME DE QUALITÉ DE DONNÉES.

Sois exhaustif. Les vies de trading en dépendent.
"""

def consulter(membre, model):
    print(f"[F3] Consultation de {membre} ({model})...")
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": PUSH},
            {"role": "user", "content": "Comment construire un score de confiance pipeline pour des données de trading crypto temps réel ?"},
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
    
    md = f"# 🚢 FLOTILLE F3 — Score de Confiance Pipeline\n"
    md += f"> Date : {now}\n\n"
    for nom, data in resultats.items():
        md += f"## {nom} ({data['provider']})\n\n{data['reponse']}\n\n---\n\n"
    
    out_file = OUTPUT_DIR / f"F3_CONFIANCE_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    out_file.write_text(md, encoding="utf-8")
    print(f"\n[F3] Sauvegardé : {out_file}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
