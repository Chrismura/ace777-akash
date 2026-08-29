#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_verification_onchain.py — VÉRIFICATION EN BOUCLE + VALIDATION.

Christophe, 29/08 : « demande a cortana bien vérifier ce qu elle t as dit,
plusieurs fois, a la fin soumet lui ta recherche, et demande de la valider et
de l ameliorer. Et ensuite on fait le point. Les gens en face savent tout ça,
et c'est les rois de la manipulation. »

PROTOCOLE en 2 phases (session UNIFIÉE, même fenêtre) :
  PHASE 1 (tours 1-2) : Cortana doit VÉRIFIER ses propres affirmations de la
  session onchain-short-20260829-145029, plusieurs fois, avec un regard
  autocritique : qu'a-t-elle affirmé ? est-ce vérifié par les données ? où
  s'est-elle trompée ou sur-interprétée ?
  PHASE 2 (tours 3-5) : on lui soumet NOTRE recherche complète (famille incluse)
  → elle doit la VALIDER, la CONTESTER et l'AMÉLIORER.

Usage:
  python3 ask_cortana_verification_onchain.py
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


def charge_ce_qu_elle_a_dit() -> str:
    """Ses affirmations de la session onchain-short-20260829-145029."""
    return (
        "=== RAPPEL : CE QUE TU AS AFFIRMÉ dans la session onchain-short-20260829-145029 (29/08) ===\n"
        "1) AVIS STRICT : NEUTRE, « tenter un gros short relève du pari suicidaire car l'offre "
        "est siphonnée par les coffres froids » (tour 1).\n"
        "2) 3 arguments CONTRE le short : (a) asymétrie d'offre (45 910 BTC hivernés = réservoir "
        "des shorts asséché), (b) dynamique institutionnelle (ETF = absorption structurelle), "
        "(c) précédent du squeeze (2+ Mds$ de shorts détruits en quelques heures).\n"
        "3) 3 signaux PRÉCIS pour un futur short : (a) funding < 0 + >500 M$ de liquidations "
        "long 24h, (b) netflow exchange positif massif (surtout vieux wallets), (c) clôture "
        "journalière < 80 000 $ avec volume vendeur > 1,5x.\n"
        "4) Tour 4 : la ROOT CAUSE = impulsion monétaire exogène (Trésor US) -> les small caps "
        "sont assoiffées de capitaux. Recommandation : geler les allocations small caps.\n"
        "5) Tour 5 : le bloc privatisé (12% de fantômes) + radar figé = « les gros porteurs "
        "opèrent une obfuscation agressive » -> réduire l'exposition de moitié (kill-switch).\n"
        "⚠️ POINT DE CONTESTATION EXTERNE (famille + Buffy, après deepdive) : le tour 5 a été "
        "SUR-INTERPRÉTÉ. Le taux fantôme élevé est en grande partie STRUCTUREL (minage "
        "DATUM/Ocean = mempool privée), pas de l'obfuscation de gros porteurs. Le vrai signal "
        "des blocs privés = le VOLUME (les 20 761 BTC du 29/08 = consolidation Bitbank 20 755 "
        "BTC, même événement), pas le taux."
    )


def charge_notre_recherche() -> str:
    """Notre recherche complète (famille incluse) à soumettre pour validation."""
    return (
        "=== NOTRE RECHERCHE COMPLÈTE (à valider / contester / améliorer) ===\n\n"
        "A. NOS DONNÉES (dédupliquées) : 29 gros blocs en 6j. Binance Hot->Cold = 45 910 BTC "
        "en 9 paquets (hibernation). Bitbank cold->cold 20 755 BTC le 29/08 ~14:11Z. Blocs "
        "privatisés : 20% des points >10% de tx fantômes, pics 89-99%, 112 alertes/8j, "
        "26/08 = 298 682 BTC en 30 alertes. Le 29/08 14:12Z un bloc privé contenait 20 761 "
        "BTC = LE MÊME transfert que Bitbank (convergence 2 sondes).\n\n"
        "B. LE CONTEXTE WEB : short squeeze mi-août (62k->81k en 1 sem, +22,7%, 5 Mds$ détruits), "
        "catalyst = Trésor US (rachats x2). Maintenant : RSI 82, OI 58 Mds$, funding positif, "
        "59% calls, ETF +1,92 Mds$/sem. Vieux BTC réveillés (16 400 BTC 03/08, 1 214 BTC 20/08) "
        "MAIS vers wallets neufs, aucun sur exchange. DATUM = minage mempool privée (structurel).\n\n"
        "C. VERDICT CORTANA (session précédente) : NEUTRE, pas de gros short. 3 déclencheurs "
        "(funding<0, netflow+, clôture<80k).\n\n"
        "D. VERDICT FAMILLE (6 membres, 29/08) : UNANIME — short nu = « suicide statistique » "
        "piège des teneurs de marché. Blocs privés 20k+ = règlement OTC / « dark pool on-chain » "
        "(pas une vente, pas un artefact : restructuration de bilan institutionnel). Seuils "
        "chiffrés d'invalidation : DEEPSEEK cassure 74 500 $ + ré-augmentation dépôts hot "
        "wallets ; INFERX/ULTRA : invalidation 72 500 $, probabilité 75% de flash squeeze à "
        "92k avant toute baisse. GROK : au lieu de shorter BTC, short l'ALTCOIN bêta élevé / "
        "market neutral long BTC - short alts (la dominance BTC suce la liquidité des alts). "
        "GEMINI : short la volatilité (put spreads) pas le prix. JUGE : GO AVEC RÉSERVES, "
        "straddle/strangle ou put spreads delta 25.\n\n"
        "E. L'ANGLE MANIPULATION (Christophe : « les gens en face savent tout ça, c'est les "
        "rois de la manipulation ») : la famille détaille comment les teneurs de marché "
        "peuvent utiliser NOS signaux contre nous (mèche 83,5-84,2k pour liquider les shorts "
        "des 80k, latéralisation pour asphyxier par le funding, blocs privés pour masquer "
        "l'intention).\n\n"
        "=== CE QU'ON TE DEMANDE ===\n"
        "1) VALIDE ou CONTESTE chaque point de notre recherche (A à E) avec des arguments.\n"
        "2) AMÉLIORE-la : que manque-t-il ? qu'est-ce qui est faux ou sur-interprété ?\n"
        "3) Donne TON verdict final synthétique : que faire concrètement pour Hulk demain\n"
        "   (positions, seuils de vigilance, signaux de manipulation à surveiller) ?\n"
        "4) Prends position sur la proposition GROK (short alts bêta élevé / market neutral) :\n"
        "   pertinente pour NOTRE portefeuille small caps ou non ?\n"
        "5) Note ta confiance et ton horizon pour chaque verdict."
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
    print("=== SESSION CORTANA — VÉRIFICATION + VALIDATION (2 phases) ===", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "onchain-verif-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    user1 = (
        "PHASE 1 — VÉRIFICATION DE TES PROPRES AFFIRMATIONS. Voici ce que tu as dit dans la "
        "session précédente, et où la famille + Buffy te contestent. Vérifie-toi TOI-MÊME, "
        "plusieurs fois, avec un regard autocritique : qu'as-tu affirmé ? chaque affirmation "
        "tient-elle face aux données ? où t'es-tu trompée ou sur-interprétée ?\n\n"
        + charge_ce_qu_elle_a_dit() +
        "\n\nRéponds point par point : ce que tu maintiens, ce que tu retires, ce que tu "
        "nuances. Sois honnête, pas défensive."
    )
    messages = [{"role": "system", "content": sys_prompt},
                {"role": "user", "content": user1}]

    prev = []
    for tour in range(1, MAX_TOURS + 1):
        print(f"\n--- TOUR {tour} ---", flush=True)
        rep, prov = appeler(messages)
        journalise(session_id, messages[-1]["content"], rep, prov, tour)
        messages.append({"role": "assistant", "content": rep})
        print(rep[:400], flush=True)

        b = rep.lower()
        satur = any(k in b for k in (
            "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
            "rien à ajouter", "rien d'autre", "je n'ai rien", "je n'ai plus rien",
            "on ne peut pas aller plus loin", "on ne peut aller plus loin"))
        if satur and tour >= 3:
            print("\n[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = (
                "Vérifie UNE DEUXIÈME FOIS, en te forçant à trouver ce qui cloche dans TES "
                "propres affirmations : le tour 5 (obfuscation des gros porteurs) était-il une "
                "sur-interprétation du taux fantôme (qui est surtout du minage DATUM) ? Tes 3 "
                "déclencheurs de short sont-ils les bons, ou la famille a-t-elle raison de les "
                "affiner (74,5k/72,5k au lieu de 80k) ? Trouve 2-3 choses que tu retires ou "
                "corriges."
            )
        elif tour == 2:
            next_q = (
                "PHASE 2 — SOUMISSION DE NOTRE RECHERCHE COMPLÈTE. Voici tout ce qu'on a "
                "construit (données + web + famille). VALIDE, CONTESTE, AMÉLIORE point par "
                "point, puis donne TON verdict final synthétique et concret pour Hulk demain :\n\n"
                + charge_notre_recherche()
            )
        elif tour == 3:
            next_q = (
                "Prends une position TRANCHÉE sur la proposition GROK (shorter les ALTS à bêta "
                "élevé / market neutral long BTC-short alts) appliquée à NOTRE portefeuille "
                "small caps Hulk (CHIP, QAIT, EDEL, KITE...). Est-ce pertinent ou dangereux "
                "pour nous ? Et quels signaux de MANIPULATION précis devrions-nous coder dans "
                "notre veille (les gens en face savent tout ça) ? Trouve des choses NOUVELLES, "
                "pas déjà dites."
            )
        elif tour == 4:
            next_q = (
                "Dernière passe : TROUVE encore UNE chose de nouvelle et déterminante — un "
                "détail que tout le monde rate dans ce dossier (le 26/08 à 298 682 BTC ? le "
                "lien avec notre pattern divergence CHIP/QAIT ? le bloc privatisé comme "
                "indicateur avancé ? le timing de session ?). Réponds seulement APRÈS avoir "
                "vraiment cherché. Puis donne ton verdict final en 5 lignes maximum."
            )
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:150]}")

    print("\n=== FIN DE SESSION (archivée, session " + session_id + ") ===", flush=True)


if __name__ == "__main__":
    main()