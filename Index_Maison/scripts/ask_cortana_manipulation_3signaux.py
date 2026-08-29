#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_manipulation_3signaux.py — APPROFONDIR LES 3 SIGNAUX DE MANIPULATION.

Christophe, 29/08 : « approndir les 3 signaux, deepdive. »

On soumet à Cortana les 3 signaux approfondis avec les sources web (chartscout,
arXiv CentraleSupélec, CryptoQuant) + nos données maison (murs/spoof/drop).
Boucle "trouve" jusqu'à saturation, archivage onglet VOL.

Usage:
  python3 ask_cortana_manipulation_3signaux.py
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
MAX_TOURS = 4


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


def contexte() -> str:
    return (
        "CONTEXTE COMPLET — LES 3 SIGNAUX DE MANIPULATION APPROFONDIS (29/08/2026) :\n\n"
        "=== NOS DONNÉES MAISON (réelles) ===\n"
        "1) murs_observations.json (15:09Z) : 63 611 mesures, 27 paires. BTC : spoof_pct 4,87% "
        "(11 spoofs), drop 26, spread 0,06 bps. CHIP : spoof 3,9%, drop 53. RED : spoof 1,7%, "
        "drop 212. QAIT : spoof 0,7%, drop 142, spread 71 bps. ETH : spoof 2,94%.\n"
        "2) croisement_contexte.jsonl (24 913 points, 2j) : mur_spoof_pct, wall_strength, "
        "poussiere_taux_fantome, sdi, rbf, fee_pressure par paire.\n"
        "3) LACUNE : AUCUNE donnée funding/OI dans nos fichiers (signal 1 non couvert).\n"
        "4) bloc privatisé : taux_fantome 12% (565 tx cachées), mode actif.\n"
        "5) whales : 29 gros blocs en 6j, Binance hot->cold 45 910 BTC, Bitbank 20 755 BTC "
        "(consolidations internes, pas des ventes).\n\n"
        "=== LES 3 SIGNAUX (ce que tu as livré, session onchain-verif-20260829-150805 tour 4) ===\n"
        "SIGNAL 1 — FAKE-BREAKOUT FUNDING : OI qui monte >5% en 15 min SANS volume spot "
        "proportionnel = manipulation de levier pour piéger. Détection : divergence "
        "vitesse/volume. Seuils : OI +5%/15min vs volume spot < moy20.\n"
        "SIGNAL 2 — POUSSIÈRE INSTITUTIONNELLE : gros transferts fracturés en micro-tx "
        "déguisées en retail, OU simulation d'un gros transfert cold un vendredi soir pour "
        "paniquer. Détection : ratio d'inertie mempool (z-score du délai de minage) + delta "
        "carnet spot : si le volume on-chain explose mais le carnet spot reste plat = "
        "manipulation visuelle.\n"
        "SIGNAL 3 — SQUEEZE DU LIVRE ÉCORCHÉ (iceberg & order-book void) : mur iceberg fictif "
        "d'un côté, retrait de la liquidité réelle derrière, puis suppression du mur = trou "
        "d'air. Détection : Depth Void Index (profondeur 0-1% qui fond ≥45% en 3 min pendant "
        "que le volume spot est sous moy20), déséquilibre bid/ask book >0,85 ou <0,15 "
        "contredit par un prix immobile.\n\n"
        "=== SOURCES WEB (lues en profondeur le 29/08) ===\n"
        "1) chartscout.io « How to spot fake breakouts » (confirme signal 1) : le fakeout "
        "classique = mèche qui perce + clôture dans le range, volume qui s'effondre. Les 4 "
        "cas : wick-only, succeeded-then-failed (mèche + pas de continuation), pre-news "
        "(jamais entrer 30 min avant un print macro CPI/FOMC), liquidation-cascade (funding "
        "extrême plusieurs jours + OI qui monte + heatmap liquidations + mèche 3-6% puis "
        "recovery). Le funding à l'extrême plusieurs jours + OI qui grimpe DANS la mèche = "
        "le piège parfait.\n"
        "2) arXiv 2504.15908 (CentraleSupélec, août 2026, « Learning the Spoofability of "
        "LOB ») : 31% des grosses ordres peuvent spoof le marché (mesuré 4 jours réels). Les "
        "spoofers placent leurs ordres PROFOND dans le carnet (jamais au best price = trop "
        "risqué), en ajustant la DISTANCE de placement pour maximiser l'impact et minimiser "
        "l'exécution. Le vacuuming (absorber puis annuler = gaps de liquidité) = exactement "
        "le livre écorché. Le déséquilibre simple Vb-Va/Vb+Va est INADAPTÉ (les spoofers "
        "n'occupent pas le best) — il faut un déséquilibre multi-niveaux pondéré par la "
        "distance.\n"
        "3) CryptoQuant/CoinMarketCap : whale inflow ratio 0,64 = plus haut depuis 2015 "
        "(fév 2026) ; 17/08/2026 : dépôts whale Binance ont surgi, whale inflow ratio monte ; "
        "dépôts altcoin ~49 000/jour en 2026 (+22% vs 40 000).\n\n"
        "=== CE QU'ON TE DEMANDE ===\n"
        "1) Pour CHACUN des 3 signaux : valide/conteste avec les sources, affine les seuils, "
        "et donne la FORMULE DE CODAGE concrète (variables, calcul, seuil, alerte) utilisable "
        "avec NOS données (murs/spoof/drop dispo, funding/OI à ajouter).\n"
        "2) Quelles données faut-il ajouter à notre sonde pour couvrir le signal 1 (funding/OI) "
        "et le signal 2 (mempool) ? (ex: API Binance funding, CryptoQuant ?)\n"
        "3) Le signal 3 est-il déjà calculable avec murs_observations (spoof_pct, drop) ? "
        "Comment en faire un Depth Void Index maison ?\n"
        "4) Priorise : lequel des 3 est le plus utile pour notre portefeuille small caps Hulk ?"
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
    print("=== SESSION CORTANA — APPROFONDIR LES 3 SIGNAUX DE MANIPULATION ===", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "manip-3signaux-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    user1 = (
        "Voici le CONTEXTE COMPLET des 3 signaux de manipulation approfondis (nos données + "
        "sources web). Pour chacun : valide/conteste, affine les seuils, donne la FORMULE DE "
        "CODAGE concrète avec nos données. Priorise à la fin :\n\n" + contexte()
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
            "on ne peut pas aller plus loin"))
        if satur and tour >= 2:
            print("\n[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = (
                "Regard critique : ces 3 signaux sont-ils FIABLES ou des artefacts ? Trouve "
                "les FAUSSES ALARMES possibles de chacun (ex: le spoof peut être un vrai "
                "institutionnel qui recharge ses ordres ; le drop peut être une vraie "
                "absorption). Puis TROUVE 2-3 améliorations concrètes : comment éviter les "
                "faux positifs, et quels seuils seraient robustes sur nos small caps "
                "illiquides (spread 30-70 bps) ?"
            )
        elif tour == 2:
            next_q = (
                "Tu as proposé : " + " | ".join(prev) +
                ". TROUVE maintenant les AMÉLIORATIONS DIFFÉRENTES et plus profondes : le "
                "codage exact de chaque signal dans notre veille (variables, seuils, fenêtre), "
                "la hiérarchie des 3 signaux pour nos small caps, et les données à ajouter "
                "(funding/OI). Refuse-toi de répéter ce que tu as déjà dit."
            )
        elif tour == 3:
            next_q = (
                "Dernière passe : TROUVE encore UNE chose nouvelle et déterminante — le "
                "croisement entre ces 3 signaux de manipulation et NOS patterns maison "
                "(divergence CHIP/QAIT, bloc privatisé, cycle QAIT) ? Comment un signal de "
                "manipulation détecté sur BTC se propage-t-il à nos small caps ? Réponds "
                "seulement APRÈS avoir vraiment cherché. Puis donne le verdict final en 5 "
                "lignes : que coder en premier ?"
            )
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:150]}")

    print("\n=== FIN DE SESSION (archivée, session " + session_id + ") ===", flush=True)


if __name__ == "__main__":
    main()