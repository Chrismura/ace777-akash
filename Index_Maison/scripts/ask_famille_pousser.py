#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_famille_pousser.py — Pousse la réponse de la FAMILLE jusqu'à saturation.

Même principe que ask_cortana_boucle.py mais côté famille : on fait la boucle
« TROUVE encore autre chose » avec LE JUGE (le décideur, qui a déjà lu les avis
de Gemini/DeepSeek/Juge). Un seul appel par tour (juste milieu crédit),
messages CUMULÉS (le contexte reste fondamental), arrêt automatique à la
saturation (« je n'ai plus rien de nouveau »).

Usage:
  python3 ask_famille_pousser.py
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SCRIPTS = os.path.join(INDEX, "scripts")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
CHATS_LOG = os.path.join(INDEX, "data", "cortana_chats.jsonl")

MAX_TOURS = 4


def charge_contexte_complet() -> str:
    return (
        "CONTEXTE COMPLET de la maison ACE777 (portefeuille paper HULK, MEXC, 15 small-caps, "
        "22/07→29/08/2026) :\n\n"
        "1) STRATÉGIE : moteur déterministe dip&rip (achat dip, vente rip, mise→2x→bag, DCA, "
        "compound). 786 BUY, 378 SELL_PARTIAL, 166 SELL full, 1336 trades exécutés.\n"
        "2) SIGNAL AMPLITUDE (move24 = range haut-bas 24h) : patron « dormance→pic », "
        "54-78% du temps sous la moyenne, pics 2-5x. L'amplitude prédit le MOUVEMENT pas la "
        "direction (après un pic, le prix monte 70-100% du temps).\n"
        "3) CROISEMENT : SELL_PARTIAL = +83.96$ (moy +0.22, gagnant même en amplitude forte), "
        "SELL full = -153.24$ (moy -0.92, pire en amplitude forte -1.57$, pire en COOLING/IMPULSE). "
        "fearGreed identique (~68) → biais mécanique, pas émotionnel.\n"
        "4) COUVERTURES : short perp sur pic d'amplitude = contre-productif ; sortie sur "
        "régime+plus-value = fonctionne (QAIT +1.38$). « Rien faire » battu seulement si la "
        "sortie est partielle et bien placée.\n"
        "5) GÉOPOL : module news corrigé (tension relative, plus de biais permanent). "
        "Tensions Iran/Ukraine réelles.\n"
        "6) FINALITÉ : meilleur setup pour accumuler (DCA) quand c'est calme et protéger quand "
        "l'amplitude s'emballe. Dynamic Dominance Gate proposée (dominance BTC >58.5% + cpfp "
        "z>50 → taille x0.5).\n\n"
        "=== VERDICT FAMILLE DÉJÀ RENDU (tour 1) ===\n"
        "SOUS CONDITION. Changements prioritaires : 1) interdire SELL_full en forte amplitude, "
        "2) cascade SELL_PARTIAL par paliers 30% + trailing stop + breakeven, "
        "3) activer la Dynamic Dominance Gate (taille x0.5 en saison calme). "
        "À vérifier : le seuil de SELL_full est-il un faux signal COOLING/IMPULSE ?"
    )


def appel_hub(system, user, max_tokens=800):
    payload = {
        "task": "signets.juge",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip(), \
        data.get("provider", "?")


def journalise(session_id, question, reponse, provider, tour):
    try:
        os.makedirs(os.path.dirname(CHATS_LOG), exist_ok=True)
        entry = {
            "session": session_id,
            "membre": "LE JUGE (boucle)",
            "tour": tour,
            "ts": time.time(),
            "ts_iso": datetime.now(timezone.utc).isoformat(),
            "question": question,
            "reponse": reponse,
            "provider": f"famille:juge:{provider}",
        }
        with open(CHATS_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main():
    print("=== POUSSER LA FAMILLE — boucle JUGE (TROUVE jusqu'à saturation) ===", flush=True)
    session_id = "famille-pousse-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    sys_role = (
        "Tu es le JUGE de la maison ACE777, le décideur final. Tu es rigoureux, tu ne répètes "
        "jamais ce qui a déjà été dit, tu cherches VRAIMENT plus loin à chaque tour. "
        "macOS. Réponds en français, concis (4-6 phrases)."
    )
    user1 = (
        "Voici le contexte complet et le verdict déjà rendu par la famille. "
        "TROUVE des améliorations ADDITIONNELLES au-delà du verdict : creuse plus profond "
        "(mécanique moteur, sizing, timing, frais, régimes). Chaque idée doit être "
        "chiffrée/prouvable et bornée :\n\n" + charge_contexte_complet()
    )
    messages = [{"role": "system", "content": sys_role},
                {"role": "user", "content": user1}]

    prev = []
    for tour in range(1, MAX_TOURS + 1):
        print(f"\n--- TOUR {tour} ---", flush=True)
        # Les messages sont CUMULÉS (le contexte reste fondamental — certitude) :
        # on appelle avec tout le fil, pas seulement la dernière question.
        rep, prov = appel_hub(sys_role, "\n\n".join(
            f"TOUR {i+1} ({'question' if i % 2 == 0 else 'réponse du juge'}): {m['content'][:4000]}"
            for i, m in enumerate(messages)))
        journalise(session_id, messages[-1]["content"], rep, prov, tour)
        print(rep[:450], flush=True)
        prev.append(rep)

        b = rep.lower()
        satur = any(k in b for k in (
            "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
            "aucune autre amélioration", "plus d'amélioration", "rien à ajouter",
            "rien d'autre", "on ne peut pas aller plus loin", "on ne peut aller plus loin",
            "je n'ai rien", "je n'ai plus rien", "ai rien de plus", "rien de plus à",
            "tout a déjà été", "tout a ete", "déjà tout", "deja tout"))
        if satur:
            print("\n[FIN] Saturation — on ne peut pas aller plus loin.", flush=True)
            break

        if tour == 1:
            nq = (
                "TROUVE encore des améliorations DIFFÉRENTES et plus PROFONDES que celles du "
                "verdict (mécanique de sortie, sizing, DCA, compound, frais, régime). "
                "Refuse-toi de répéter. Chiffre chacune si possible."
            )
        elif tour == 2:
            nq = (
                "Creuse la ROOT CAUSE : pourquoi le moteur coupe à 100% ? TROUVE l'amélioration "
                "la plus DÉTERMINANTE, celle qui change tout, que personne n'a encore vue. "
                "Rappel déjà proposé : " + " | ".join(x[:140] for x in prev[-3:])
            )
        elif tour == 3:
            nq = (
                "Dernière passe : TROUVE encore un détail NOUVEAU, même petit (frais, slippage, "
                "arrondis, taille de lot, cadence, timing). Cherche dans les interstices. "
                "Réponds APRÈS avoir vraiment cherché."
            )
        messages.append({"role": "user", "content": nq})

    print(f"\n=== FIN (session {session_id}) — archivée dans cortana_chats.jsonl ===", flush=True)


if __name__ == "__main__":
    main()