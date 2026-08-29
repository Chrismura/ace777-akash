#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_onchain_short.py — CAVALERIE : deepdive on-chain BTC + potentiel short.

Christophe, 29/08 : « faire recherche croisée sur mouvement onchain btc en deepdive,
potentiel gros short, envois la cavallerie, si tu vois reponse insuffisante ou de
salon relance même fenêtre go ».

Même mécanique que ask_cortana_divergence.py : session UNIFIÉE (messages cumulés,
contexte fondamental), boucle « TROUVE » jusqu'à saturation, archivage onglet VOL
(cortana_chats.jsonl). Le CONTEXTE ici = nos données on-chain MAISON (whales,
Binance hot→cold, bloc privatisé, macro_tempete) CROISÉES avec les sources web
(short squeeze d'août, réveil des vieux BTC, ETF inflows).

Usage:
  python3 ask_cortana_onchain_short.py
"""
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SCRIPTS = os.path.join(INDEX, "scripts")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
CHATS_LOG = os.path.join(INDEX, "data", "cortana_chats.jsonl")
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


def charge_contexte_onchain() -> str:
    """CONTEXTE COMPLET : nos données maison croisées avec les sources web."""
    return (
        "CONTEXTE COMPLET — DEEPDIVE ON-CHAIN BTC + POTENTIEL GROS SHORT (29/08/2026, ACE777) :\n\n"
        "=== A. NOS DONNÉES MAISON (réelles, runs/whales_mouvements.jsonl + data/) ===\n"
        "1) Flux Binance sur 6 jours (dédupliqué par txid, 29 gros blocs uniques) :\n"
        "   - 9 mouvements Binance Hot Wallet #2 -> Binance Cold Storage #2 = 45 910 BTC "
        "retirés du hot wallet (source bc1qm34... = Binance Hot Wallet #2, cible 3M219K... = "
        "Binance Cold Storage #2, étiquetés dans whales.json). Paquets de 2 000-7 700 BTC "
        "espacés de ~8h à ~50h. => HIBERNATION de supply (les BTC sortent de la circulation "
        "de trading, ne peuvent plus être vendus facilement). Pas de vente : au contraire, "
        "réduction de l'offre liquide.\n"
        "   - 1 mouvement Bitbank Cold -> Bitbank Cold (20 755 BTC, consolidation interne).\n"
        "   - blocs récents 963xxx : paquets de ~100,1 BTC depuis adresses inconnues "
        "(distribution fine, daté 20/08).\n"
        "   - ATTENTION : le scan whales est FIGÉ depuis le 28/08 14:11Z (mempool.space DOWN, "
        "erreur DNS/timeout). Les blocs 27-29/08 ne sont PAS couverts par nos données.\n"
        "2) Bloc privatisé (14:47Z) : taux_fantome 12,04% (nb_tx_cachees 565 / 4692), "
        "mode actif — haut niveau de transactions « fantômes » (poussière/obfuscation ?).\n"
        "3) macro_tempete (14:48Z) : INACTIF — chg24 -1,95%, volume x0,71. Pas de tempête.\n"
        "4) Marché Hulk (MEXC spot, DIGEST 14:49Z) : BTC 77 699 $, le panier est calme "
        "(IDLE quasi partout), chg24 des small caps entre -0,18% et +0,11%.\n\n"
        "=== B. SOURCES WEB (lues en profondeur le 29/08) ===\n"
        "1) Short squeeze violent mi-août : BTC est passé de ~62k à 81k en moins d'une semaine "
        "(+22,7% hebdo, plus grosse hausse hebdo en $ de l'histoire), ~5 Mds$ de positions "
        "détruites en 72h (2,74 Mds$ de shorts liquidés à la hausse, puis 1,82 Mds$ de longs "
        "liquidés en retour). Catalyst : le Trésor US a doublé ses rachats de liquidité le "
        "19/08 (au moins 4 Mds$ par opération) -> dollar en baisse, BTC et or en hausse.\n"
        "2) Le marché est passé de « short crowdé » à « LONG CROWDÉ » : funding redevenu "
        "positif (0,013% prédit = plus haut depuis janvier), open interest ~58 Mds$ (vs 49 "
        "au début de la semaine), RSI journalier ~82 = plus haut depuis 2,5 ans (surobt), "
        "59% des options OI en calls.\n"
        "3) RÉVEIL DES VIEUX BTC (août 2026) : wallet dormant 7 mois a bougé 16 400 BTC "
        "(1,04 Mds$) le 03/08 — MAIS vers un wallet NEUF, pas un exchange (custody reshuffle "
        "/ OTC, pas de vente). Un wallet dormant 11 ans a bougé 1 214 BTC (86 M$) le 20/08 — "
        "vers des adresses sans lien exchange connu. Un dormant 8 ans a bougé 5 908 BTC "
        "(383 M$) mi-juillet — sans passer par un exchange. Leçon des analystes : ce qui "
        "compte n'est PAS la taille du transfert mais S'il finit en dépôt exchange (vente) "
        "ou pas (reshuffle).\n"
        "4) ETF spot US : ~1,92 Mds$ d'inflows la semaine du 21/08 (meilleure semaine depuis "
        "oct 2025), volume de trading 22,1 Mds$ (vs 6,9 la semaine avant), 608 M$ d'inflows "
        "en une journée -> demande RÉELLE, pas que de la liquidation.\n"
        "5) Niveaux techniques : 80k tenu (support), résistance 81,5-83k, puis 85-90k. "
        "50-week EMA ~81,2k. ATH octobre 2025 = 126 198 $ ; le marché est ~50% sous l'ATH ; "
        "BTC à ~77-78k aujourd'hui.\n\n"
        "=== CE QU'ON TE DEMANDE ===\n"
        "La question de Christophe : y a-t-il un potentiel GROS SHORT sur BTC maintenant ? "
        "Croise TOUT (on-chain maison + web + technique + macro) et donne ton avis :\n"
        "- FAITS + LECTURE + INTERPRÉTATION + PATTERN + OPINION + AVIS STRICT + HORIZON + CONFIANCE\n"
        "- Les arguments POUR un short (RSI extrême, longs crowdés, surobt, résistance 83k,\n"
        "  réveil des vieux BTC comme supply future potentielle)\n"
        "- Les arguments CONTRE un short (45 910 BTC hivernés par Binance = offre réduite,\n"
        "  ETF inflows records = demande réelle, dollar faible, pas de dépôt exchange massif)\n"
        "- Le verdict : short maintenant / attendre un signal précis / pas de short du tout ?\n"
        "  Avec un scénario chiffré (entrée, stop, cible, taille, durée) SI tu penses short.\n"
        "- Puis tes 2-3 premières recommandations concrètes pour Hulk (mode ADVISORY)."
    )


def appeler(messages) -> tuple:
    payload = {
        "task": "cortana.analyse",
        "messages": messages,
        "temperature": 0.4,
        "max_tokens": 1100,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=240) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    content = data["choices"][0]["message"]["content"].strip()
    return content, data.get("provider", "?")


def journalise(session_id, question, reponse, provider, tour):
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
    print("=== SESSION CORTANA — ON-CHAIN BTC / POTENTIEL GROS SHORT (cavalerie) ===", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "onchain-short-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    constat = charge_contexte_onchain()

    user1 = (
        "Voici le CONTEXTE COMPLET du deepdive on-chain BTC (nos données MAISON réelles "
        "croisées avec les sources web, rien n'est inventé). Analyse en profondeur et donne "
        "ton avis détaillé (FAITS, LECTURE, INTERPRÉTATION, PATTERN, OPINION, AVIS STRICT, "
        "HORIZON, CONFIANCE), avec le verdict short/attente/pas-short chiffré, puis tes 2-3 "
        "premières recommandations concrètes pour Hulk :\n\n" + constat
    )
    messages = [{"role": "system", "content": sys_prompt},
                {"role": "user", "content": user1}]

    prev_propositions = []
    for tour in range(1, MAX_TOURS + 1):
        print(f"\n--- TOUR {tour} ---", flush=True)
        rep, prov = appeler(messages)
        journalise(session_id, messages[-1]["content"], rep, prov, tour)
        messages.append({"role": "assistant", "content": rep})
        print(rep[:500], flush=True)

        b = rep.lower()
        satur = any(k in b for k in (
            "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
            "aucune autre amélioration", "plus d'amélioration", "rien à ajouter",
            "rien d'autre", "on ne peut pas aller plus loin", "on ne peut aller plus loin",
            "je n'ai rien", "je n'ai plus rien", "ai rien de plus", "rien de plus à"))
        if satur:
            print("\n[FIN] Saturation détectée — on ne peut pas aller plus loin.", flush=True)
            break

        if tour == 1:
            next_q = (
                "Prends maintenant un REGARD CRITIQUE : le short est-il vraiment jouable ou "
                "est-ce un piège (RSI élevé mais marché neuf haussier, offre réduite par "
                "l'hivernage Binance) ? Trouve tes arguments CONTRE ton propre verdict, puis "
                "TROUVE 2-3 améliorations concrètes : quels SIGNAUX PRÉCIS déclencheraient "
                "un vrai short (niveau, funding, netflow exchange, dépôt des vieux BTC) ?"
            )
        elif tour == 2:
            next_q = (
                "Tu as proposé : " + " | ".join(prev_propositions) +
                ". TROUVE maintenant des recommandations DIFFÉRENTES et plus PROFONDES "
                "(mécanique de trade, sizing, couverture du portefeuille Hulk, arbitrage "
                "petites caps vs BTC, timing intraday). Chacune chiffrée/prouvable, bornée, "
                "sans effet de bord. Refuse-toi de répéter ce que tu as déjà dit."
            )
        elif tour == 3:
            next_q = (
                "Creuse encore : TROUVE la ROOT CAUSE du mouvement actuel (qui est vraiment "
                "derrière le rally d'août : le Trésor US ? les ETF ? les shorts ?) et "
                "l'utilisation la plus DÉTERMINANTE pour notre portefeuille small caps. "
                "Rappel déjà proposé : " + " | ".join(prev_propositions[-6:]) + ". "
                "Trouve au moins UNE chose nouvelle."
            )
        elif tour == 4:
            next_q = (
                "Dernière passe : TROUVE encore autre chose de NOUVEAU, même petit — un détail "
                "que tout le monde rate (le bloc privatisé à 12% de fantômes ? le scan whales "
                "figé ? le timing de session ? le lien avec nos patterns divergence CHIP/QAIT ?). "
                "Réponds seulement APRÈS avoir vraiment cherché."
            )
        messages.append({"role": "user", "content": next_q})
        prev_propositions.append(f"[tour{tour}] {rep.strip()[:160]}")

    print("\n=== FIN DE SESSION (archivée dans cortana_chats.jsonl, session " + session_id + ") ===", flush=True)


if __name__ == "__main__":
    main()