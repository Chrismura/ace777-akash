#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_boucle.py — Session UNIFIÉE à Cortana (Gemini).

PRINCIPE (Christophe 29/08) : ne PAS exploser le crédit avec N appels séparés.
→ UN SEUL fil de conversation au hub, `messages` CUMULÉS (le contexte est
fondamental : chaque tour garde tout l'historique). Chaque tour s'enrichit,
jusqu'à saturation (« je n'ai plus rien de neuf »).

Toute la conversation est journalisée dans le MÊME historique que l'onglet VOL
(Index_Maison/data/cortana_chats.jsonl), chaque question+réponse liée par un
session_id commun, avec date/heure. Relisible dans le cockpit.

Usage:
  python3 ask_cortana_boucle.py
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

# Bornes de la boucle — juste milieu crédit : 5 tours max.
MAX_TOURS = 5


def load_system_prompt():
    for p in (
        os.path.join(SCRIPTS, "prompts", "PROMPT_MASTER_ANALYSTE.md"),
        os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md"),
    ):
        if os.path.exists(p):
            try:
                return open(p, encoding="utf-8").read()
            except Exception:
                pass
    return "Tu es Cortana, master analyste crypto du cockpit ACE777. Réponds en français, concis."


def charge_contexte_complet() -> str:
    """CONTEXTE COMPLET (certitude : le contexte est fondamental).
    Tout ce qu'on a découvert/vécu : le signal amplitude, les couvertures testées,
    le « rien faire », le geopol, la finalité DCA — pas seulement le croisement
    SELL/SELL_PARTIAL. C'est LA base d'un avis digne de ce nom.
    """
    return (
        "CONTEXTE COMPLET de la maison ACE777 (portefeuille paper HULK, MEXC, 15 small-caps, "
        "22/07→29/08/2026) :\n\n"
        "1) STRATÉGIE : moteur déterministe dip&rip (achat dip, vente rip, mise→2x→bag, DCA, "
        "compound). Paper trading, 786 BUY, 378 SELL_PARTIAL, 166 SELL full, 1336 trades exécutés.\n\n"
        "2) SIGNAL AMPLITUDE (move24 = range haut-bas 24h, notre indicateur maison) :\n"
        "   - patron « dormance→pic » : 54-78% du temps sous la moyenne, pics 2-5x (XRP 5.6x, "
        "   QAIT 4.2x). Médiane < moyenne = distribution étalée (ressort comprimé).\n"
        "   - l'amplitude prédit le MOUVEMENT pas la direction (après un pic, le prix continue "
        "   de monter 70-100% du temps).\n\n"
        "3) CROISEMENT SORTIES (le constat chiffré du jour) :\n"
        "   - SELL_PARTIAL (délester 30-50%) : total +83.96$, moyen +0.22, TOUJOURS gagnant "
        "   même en amplitude forte (+0.19). Meilleur en régime IMPULSE_WAIT (252 trades).\n"
        "   - SELL full (couper 100%) : total -153.24$, moyen -0.92, TOUJOURS perdant, "
        "   pire en amplitude forte (-1.57$). Pire en COOLING (61) et IMPULSE (42).\n"
        "   - fearGreed moyen identique (~68) aux deux types de sortie → le biais est mécanique, "
        "   pas émotionnel.\n\n"
        "4) COUVERTURES TESTÉES : short perp partiel sur pic d'amplitude = CONTRE-PRODUCTIF "
        "(le prix monte après les pics) ; sortie sur régime+plus-value = a fonctionné "
        "(QAIT vendu avant la chute, +1.38$). Le « rien faire » (tenir) est battu par la gestion "
        "seulement quand la sortie est partielle et bien placée.\n\n"
        "5) GÉOPOL : module news biaisé (5 requêtes toutes négatives → ratio 82% vs 15% neutre) "
        "corrigé en tension relative. Tensions réelles Iran/Ukraine en ce moment.\n\n"
        "6) FINALITÉ : on cherche le MEILLEUR SETUP pour accumuler (DCA) quand c'est calme et "
        "protéger quand l'amplitude s'emballe — couplé au trend (Cortana suggère Dynamic Dominance "
        "Gate : dominance BTC >58.5% + cpfp z>50 → taille x0.5).\n\n"
        "=== LE CROISEMENT À ANALYSER EN PRIORITÉ ===\n"
        "Le patron SELL full (-153$) vs SELL_PARTIAL (+84$) : pourquoi Hulk coupe à 100% ? "
        "Que faut-il changer dans la mécanique de sortie ? (le contexte ci-dessus est là pour ça)"
    )


def appeler(messages) -> tuple:
    """Un appel au hub( task=cortana.analyse -> Gemini/Cortana ), messages cumulés."""
    payload = {
        "task": "cortana.analyse",
        "messages": messages,
        "temperature": 0.4,
        "max_tokens": 900,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=240) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    content = data["choices"][0]["message"]["content"].strip()
    provider = data.get("provider", "?")
    return content, provider


def journalise(session_id, question, reponse, provider, tour):
    """Append question+réponse dans le MÊME historique (onglet VOL)."""
    try:
        os.makedirs(os.path.dirname(CHATS_LOG), exist_ok=True)
        entry = {
            "session": session_id,
            "tour": tour,
            "ts": time.time(),
            "ts_iso": datetime.now(timezone.utc).isoformat(),
            "question": question,
            "reponse": reponse,
            "provider": f"cortana:{provider}",
        }
        with open(CHATS_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main():
    print("=== SESSION CORTANA — boucle contextuelle unifiée (juste milieu crédit) ===", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "boucle-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    constat = charge_contexte_complet()

    user1 = (
        "Voici le CONTEXTE COMPLET de la maison (tout est vrai, rien n'est inventé). "
        "Analyse-le en profondeur et donne ton avis détaillé "
        "(FAITS, LECTURE, INTERPRÉTATION, PATTERN, OPINION, AVIS STRICT, HORIZON, CONFIANCE), "
        "puis propose tes 2-3 premières améliorations concrètes :\n\n"
        + constat
    )
    messages = [{"role": "system", "content": sys_prompt},
                {"role": "user", "content": user1}]

    prev_propositions = []  # ce qu'elle a déjà proposé (pour forcer la nouveauté)

    for tour in range(1, MAX_TOURS + 1):
        print(f"\n--- TOUR {tour} ---", flush=True)
        rep, prov = appeler(messages)
        journalise(session_id, messages[-1]["content"], rep, prov, tour)
        messages.append({"role": "assistant", "content": rep})
        print(rep[:400], flush=True)

        # Détection de saturation : l'IA dit qu'elle n'a plus rien de neuf.
        b = rep.lower()
        satur = any(k in b for k in (
            "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
            "aucune autre amélioration", "plus d'amélioration", "rien à ajouter",
            "rien d'autre", "on ne peut pas aller plus loin", "on ne peut aller plus loin",
            "je n'ai rien", "je n'ai plus rien", "ai rien de plus", "rien de plus à"))
        if satur:
            print("\n[FIN] Saturation détectée — on ne peut pas aller plus loin.", flush=True)
            break

        # Tour suivant : on pousse plus loin (améliorations / critique / profondeur).
        if tour == 1:
            next_q = (
                "Prends maintenant un REGARD CRITIQUE sur ton propre constat : ce patron "
                "(SELL full perdant, SELL_PARTIAL gagnant) est-il FIABLE ou pourrait-il être un "
                "artefact ? Trouve tes arguments CONTRE, puis TROUVE 2-3 améliorations concrètes "
                "pour la gestion, différentes de celles du tour 1."
            )
        elif tour == 2:
            next_q = (
                "Tu as proposé : " + " | ".join(prev_propositions) +
                ". TROUVE maintenant des améliorations DIFFÉRENTES et plus PROFONDES "
                "(mécanique du moteur, sizing, sorties, régime, DCA) que tu n'as pas encore "
                "mentionnées. Chacune doit être chiffrée/prouvable, bornée, sans effet de bord. "
                "Refuse-toi de répéter ce que tu as déjà dit."
            )
        elif tour == 3:
            next_q = (
                "Creuse encore plus loin : TROUVE la ROOT CAUSE systémique (pourquoi Hulk coupe "
                "à 100% ?) et l'amélioration la plus DÉTERMINANTE à faire en priorité. "
                "Rappel déjà proposé : " + " | ".join(prev_propositions[-6:]) + ". "
                "Trouve au moins UNE chose nouvelle."
            )
        elif tour == 4:
            next_q = (
                "Dernière passe : TROUVE encore autre chose de NOUVEAU, même petit, même "
                "imparfait — un détail que tout le monde rate. Cherche dans les interstices "
                "(frais, slippage, taille de lot, timing, cadence). Réponds seulement APRÈS "
                "avoir vraiment cherché."
            )
        messages.append({"role": "user", "content": next_q})
        prev_propositions.append(f"[tour{tour}] {rep.strip()[:160]}")

    print("\n=== FIN DE SESSION (archivée dans cortana_chats.jsonl, session " + session_id + ") ===", flush=True)


if __name__ == "__main__":
    main()