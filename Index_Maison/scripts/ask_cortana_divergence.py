#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_divergence.py — Soumission du PATTERN DIVERGENCE à Cortana.

Même mécanique que ask_cortana_boucle.py (session UNIFIÉE, messages cumulés,
juste milieu crédit, saturation, archivage onglet VOL) mais le CONTEXTE est le
protocole divergence du 29/08 : les 3 angles (divergence actuelle, timing
avance/retard, signal directionnel) + le deepdive CHIP (USD.AI).

Christophe, 29/08 : « faut que hulk et cortana considèrent ce pattern qu'on a
trouvé » → cette session donne à Cortana le pattern COMPLET et lui demande son
avis indépendant + comment l'utiliser (Hulk ADVISORY) + ce qu'elle valide/réfute.

Usage:
  python3 ask_cortana_divergence.py
"""
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SCRIPTS = os.path.join(INDEX, "scripts")
HULK = os.path.expanduser("~/ace777-test-day1/hulk-mexc")
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


def charge_contexte_divergence() -> str:
    """CONTEXTE COMPLET du pattern divergence (certitude : le contexte est fondamental)."""
    return (
        "CONTEXTE COMPLET — PATTERN DIVERGENCE AVANCE/RETARD (maison ACE777, HULK MEXC, 17 paires, "
        "données 27/08→29/08/2026, ~23 000 points horodatés dans runs/croisement_contexte.jsonl) :\n\n"
        "1) MÉTHODE (protocole, voir hulk-mexc/docs/PROTOCOLE_DIVERGENCE_20260829.md) :\n"
        "   - chaque crypto a une série horaire m6_pct (mouvement 6h). On la compare à la MOYENNE "
        "du panier (les 17 paires).\n"
        "   - 3 angles : (a) divergence actuelle (6h récentes vs 30h passées), (b) timing = "
        "corrélation croisée horaire crypto vs panier (lag -4h..+4h → qui PRÉCÈDE / qui SUIT), "
        "(c) signal directionnel = corr(m6 crypto à H, delta panier H→H+4h) → + = précède HAUSSE "
        "(LEADER), - = précède BAISSE (POMPE-PIÈGE).\n"
        "   - protocole rejouable : scripts/analyse_divergence.py + journal toutes les 6h (plist "
        "com.ace777.divergence) + alerte anti-oubli (DIVERGENCE_ETAT.json : FRAIS/STALE/ALERTE).\n\n"
        "2) RÉSULTATS DU 29/08 (première passe, 2 jours de données — À CONFIRMER sur 1-2 semaines) :\n"
        "   - 🟢 CHIP (USD.AI) : DIV +3.6 vs panier, corr directionnelle +0.27 → LEADER, la SEULE "
        "crypto qui PRÉCÈDE les hausses du panier. Surperforme durablement, volume HOT (vol_spike "
        "2.78x), gros murs stables (33k$ bid), trailing armé. 36 jours de suivi : 47 BUY, 44 partiels "
        "+8.00$, 8 SELL full -0.37$ = le moteur gagne 21x plus qu'il ne perd dessus.\n"
        "   - 🔴 POMPES-PIÈGES (leurs pics précèdent des BAISSES du panier, corr <= -0.15) : "
        "EDEL (-0.47, 8/8 pics → panier en baisse +2h ET +4h), QAIT (-0.45, m24 +38% surchauffée), "
        "TEL (-0.42), RED (-0.15), KITE (-0.15).\n"
        "   - 🟡 légers / neutres : XRP, RIZE, CC, PYTH (+0.05..+0.09) ; BTC, ETH, W alignés.\n"
        "   - 📉 sousperforment durablement : HBAR, TEL, RWAINC (retardataires, lag +1..+2h).\n\n"
        "3) DEEP-DIVE CHIP (l'« arbre qui cache la forêt » selon Christophe) :\n"
        "   - projet : USD.AI, protocole de lending permissionless qui finance l'infrastructure IA, "
        "lancé 21/04/2026 (4 mois), listé Binance, volume 24h ~51M$. Secteur AI×DeFi porteur.\n"
        "   - nos données : m6 MOYEN 10.17% (min 4.2/max 17.9) = volatilité constante à 2 chiffres ; "
        "575 pics m6>10% en 2 jours ; pics concentrés 8h-17h UTC (sessions EU/US = vraie activité) ; "
        "prix 0.0375→0.0472 ; actuellement 0.0403, IMPULSE, move24 +20.5%, chg24 -8.5% = baisse sur "
        "tendance forte.\n"
        "   - lecture Christophe : « ça pourrait être l'arbre qui cache la forêt » (le meneur qui "
        "annonce le mouvement secteur AI, pas juste son propre mouvement).\n\n"
        "4) LIEN AVEC LE FIX SELL FULL (déployé 29/08) : coupe 100% interdite si move24>12% sans "
        "invalidation → vente partielle 50% en cascade. Les POMPES-PIÈGES (EDEL/QAIT) sont des "
        "positions surchauffées où ce fix protège exactement comme il faut.\n\n"
        "=== CE QU'ON TE DEMANDE ===\n"
        "Le pattern divergence avance/retard est-il FIABLE ou un artefact de 2 jours ? "
        "Que penses-tu du deepdive CHIP (leader sectoriel ou hasard de volatilité) ? "
        "Comment Hulk devrait-il utiliser ce signal (mode ADVISORY, sizing, priorités) ? "
        "Trouve tes arguments CONTRE, puis propose des améliorations concrètes."
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
    print("=== SESSION CORTANA — PATTERN DIVERGENCE (boucle contextuelle unifiée) ===", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "divergence-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    constat = charge_contexte_divergence()

    user1 = (
        "Voici le CONTEXTE COMPLET du pattern divergence (tout est vrai, rien n'est inventé, "
        "chiffres réels). Analyse-le en profondeur et donne ton avis détaillé "
        "(FAITS, LECTURE, INTERPRÉTATION, PATTERN, OPINION, AVIS STRICT, HORIZON, CONFIANCE), "
        "puis propose tes 2-3 premières recommandations concrètes pour Hulk :\n\n" + constat
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
                "Prends maintenant un REGARD CRITIQUE sur ce pattern : est-il FIABLE ou un "
                "artefact de 2 jours de données ? Trouve tes arguments CONTRE (notamment sur "
                "CHIP : leader sectoriel ou hasard de volatilité extrême ?), puis TROUVE 2-3 "
                "améliorations concrètes pour que Hulk utilise ce signal sans risque."
            )
        elif tour == 2:
            next_q = (
                "Tu as proposé : " + " | ".join(prev_propositions) +
                ". TROUVE maintenant des recommandations DIFFÉRENTES et plus PROFONDES "
                "(mécanique moteur, sizing, ADVISORY→application, priorités entre LEADER et "
                "POMPE-PIÈGE, DCA). Chacune chiffrée/prouvable, bornée, sans effet de bord. "
                "Refuse-toi de répéter ce que tu as déjà dit."
            )
        elif tour == 3:
            next_q = (
                "Creuse encore : TROUVE la ROOT CAUSE de ce pattern (pourquoi certaines cryptos "
                "précèdent et d'autres suivent ?) et l'utilisation la plus DÉTERMINANTE pour Hulk. "
                "Rappel déjà proposé : " + " | ".join(prev_propositions[-6:]) + ". "
                "Trouve au moins UNE chose nouvelle."
            )
        elif tour == 4:
            next_q = (
                "Dernière passe : TROUVE encore autre chose de NOUVEAU, même petit — un détail "
                "que tout le monde rate dans ce pattern (frais, timing de session, volume, "
                "corrélation avec le fix SELL full, mode dégradé). Réponds seulement APRÈS avoir "
                "vraiment cherché."
            )
        messages.append({"role": "user", "content": next_q})
        prev_propositions.append(f"[tour{tour}] {rep.strip()[:160]}")

    print("\n=== FIN DE SESSION (archivée dans cortana_chats.jsonl, session " + session_id + ") ===", flush=True)


if __name__ == "__main__":
    main()
