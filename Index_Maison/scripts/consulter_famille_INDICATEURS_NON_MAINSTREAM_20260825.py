#!/usr/bin/env python3
"""
CONSULTATION FAMILLE — INDICATEURS NON-MAINSTREAM
==================================================

On est des artisans de la matière première de la donnée brute.
On moule la donnée source en indicateurs que personne ne voit.

Le Pentagon Pizza Index en est l'exemple parfait :
- Source : commandes de pizza autour du Pentagon (Google Maps)
- Logique : plus de pizza = plus d'activité militaire = événement imminent
- Résultat : a prédit la guerre du Golfe, l'invasion du Panama, les frappes en Iran

On demande à la famille : quels autres indicateurs non-mainstream existent ?
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INDEX = Path.home() / "ace777-test-day1" / "Index_Maison"
HUB = "http://127.0.0.1:11435/v1/chat/completions"

SYSTEM = """Tu es un analyste géopolitique et financier expert en indicateurs non-mainstream.

CONTEXTE :
Nous sommes des artisans de la matière première de la donnée brute. Nous moutons la donnée source en indicateurs que personne d'autre ne voit.

EXEMPLE PARFAIT — Le Pentagon Pizza Index :
- SOURCE : commandes de pizza autour du Pentagon (Google Maps Popular Times)
- LOGIQUE : plus de pizza livrée = personnel qui travaille tard = activité militaire inhabituelle
- RÉSULTAT : a PRÉDIT la guerre du Golfe (1990), l'invasion du Panama (1989), les frappes en Iran (2025), la capture de Maduro (2026)
- SITE : pizzint.watch (OSINT en temps réel)
- STATUT ACTUEL : DOUGHCON 3, spikes de +200%

NOTRE PHILOSOPHIE :
On ne cherche pas les indicateurs classiques (RSI, MACD, volume). On cherche les INDICATEURS PROXY — des données qui n'ont RIEN à voir avec le finance mais qui RÉVÈLENT des événements avant qu'ils n'arrivent.

TON RÔLE :
Trouve 5-10 indicateurs non-mainstream qui peuvent prédire des événements géopolitiques ou financiers. Pour chacun, explique :
1. La SOURCE de la donnée
2. La LOGIQUE (pourquoi ça marche)
3. L'HISTORIQUE (est-ce que ça a déjà marché ?)
4. L'IMPACT sur le BTC/marché
5. COMMENT l'obtenir en temps réel

STYLE : Direct, factuel, sans blabla. Données brutes, pas d'opinions.

PUSH EXCELLENCE : Ta première réponse est le PLAFOND de ta pensée, pas le plancher. Si tu peux aller 30% plus loin — c'est CE niveau que je veux."""


def consulter_membre(membre, model):
    """Consulte un membre de la famille."""
    user_msg = (
        "Trouve 5-10 indicateurs non-mainstream qui peuvent prédire "
        "des événements géopolitiques ou financiers. Pour chacun : "
        "source, logique, historique, impact BTC, comment l'obtenir.\n\n"
        "Le Pentagon Pizza Index est notre exemple de référence. "
        "On cherche des indicateurs du même calibre — des données brutes "
        "transformées en signaux prédictifs.\n\n"
        "Pousse ta réflexion au MAXIMUM. On veut du concret, du vérifiable, "
        "du temps réel si possible."
    )
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        "max_tokens": 2000,
        "temperature": 0.3,
    }).encode()

    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=200) as r:
            d = json.loads(r.read().decode())
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"ERREUR: {e}"


def main():
    membres = [
        ("Gemini", "gemini"),
        ("DeepSeek", "deepseek"),
        ("Grok", "grok"),
        ("INFERX", "nvidia"),
        ("ULTRA", "ultra"),
        ("JUGE", "juge"),
    ]

    print("🍕 CONSULTATION FAMILLE — INDICATEURS NON-MAINSTREAM")
    print("=" * 60)
    print(f"📅 {datetime.now().strftime('%d/%m %Y %H:%M')}")
    print(f"🎯 Objectif : trouvez des indicateurs comme le Pentagon Pizza Index")
    print()

    resultats = {}
    for nom, model in membres:
        print(f"📡 Consultation de {nom} ({model})...", flush=True)
        reponse = consulter_membre(nom, model)
        resultats[nom] = reponse
        print(f"   ✅ {nom} a répondu ({len(reponse)} caractères)")
        print(f"   📝 {reponse[:150]}...")
        print()

    # Sauvegarder
    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sujet": "Indicateurs non-mainstream (type Pentagon Pizza Index)",
        "philosophie": "Artisans de la matière première de la donnée brute",
        "reponses": resultats,
    }

    dest = INDEX / "data" / f"FAMILLE_INDICATEURS_NON_MAINSTREAM_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n💾 Sauvegardé : {dest}")

    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES RÉPONSES")
    print("=" * 60)
    for nom, rep in resultats.items():
        print(f"\n🤖 {nom} :")
        print(f"   {rep[:300]}...")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
