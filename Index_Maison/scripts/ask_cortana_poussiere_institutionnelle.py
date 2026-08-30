#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_poussiere_institutionnelle.py — APPROFONDIR LA POUSSIÈRE INSTITUTIONNELLE.

Christophe, 29/08 : « avant d'approfondir poussière institutionnelle, on doit
comprendre effectivement ce que cortana a comme vision. »

Session CIBLÉE sur le Signal 2 (poussière institutionnelle / camouflage des
gros porteurs) : on pousse Cortana à expliciter SA vision complète — qu'est-ce
que la poussière institutionnelle POUR ELLE, quels mécanismes, comment la
détecter, comment la distinguer du vrai bruit, et comment elle s'articule avec
nos autres sondes (bloc privatisé, whales, fee_pressure). Boucle "trouve"
jusqu'à saturation, archivage onglet VOL.

Usage:
  python3 ask_cortana_poussiere_institutionnelle.py
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
        "CONTEXTE COMPLET — LA POUSSIÈRE INSTITUTIONNELLE (29/08/2026, session ciblée) :\n\n"
        "=== CE QUE TU AS DIT (session manip-3signaux-20260829-152046, tour 1) ===\n"
        "Signal 2 — POUSSIÈRE INSTITUTIONNELLE & CAMOUFLAGE CPFP :\n"
        "- gros transferts fracturés en milliers de micro-tx déguisées en activité retail ;\n"
        "- OU simulation d'un gros transfert cold un vendredi soir pour paniquer le retail ;\n"
        "- détection : ratio d'inertie de la mempool (z-score du délai de minage) + delta du\n"
        "  carnet spot plat (si le volume on-chain explose mais que le carnet spot reste plat\n"
        "  = manipulation visuelle) ;\n"
        "- formule : z_score_mempool_delay > 2.0 & taux_fantome >= 0.12 & abs(spot_book_delta) < 0.01.\n\n"
        "=== NOS DONNÉES MAISON (réelles, à croiser) ===\n"
        "1) poussiere_taux_fantome + poussiere_nb_cachees dans croisement_contexte.jsonl\n"
        "   (24 913 points, 2 jours, par paire) — le taux de tx « fantômes ».\n"
        "2) bloc_privatise_hist.jsonl (4 767 points 21-29/08) : taux_fantome 12% (565 tx cachées\n"
        "   sur 4692), pics à 89-99%, 112 alertes (taux>=10% ET volume>=500 BTC), le 26/08 =\n"
        "   298 682 BTC en 30 alertes.\n"
        "3) whales_mouvements.jsonl : 29 gros blocs en 6j (Binance hot->cold 45 910 BTC, Bitbank\n"
        "   20 755 BTC — consolidations internes, PAS des ventes).\n"
        "4) fee_pressure dans croisement_contexte (fastest/halfHour/hour/economy) + rbf (score,\n"
        "   ratio) + ipt (micro_tx_ratio, z_fee, entropy) + sdi — des signaux on-chain fins.\n\n"
        "=== SOURCES WEB (lues le 29/08) ===\n"
        "1) CryptoQuant : whale inflow ratio 0,64 = plus haut depuis 2015 (fév 2026) ; le 17/08\n"
        "   les dépôts whale Binance ont surgi ; dépôts altcoin ~49 000/jour en 2026 (+22%).\n"
        "2) arXiv 2504.15908 : 31% des grosses ordres peuvent spoof ; les spoofers placent leurs\n"
        "   ordres profond dans le carnet, jamais au best price.\n\n"
        "=== CE QU'ON TE DEMANDE — EXPLICITE TA VISION COMPLÈTE ===\n"
        "1) Que signifie EXACTEMENT « poussière institutionnelle » pour toi ? Définis-la\n"
        "   précisément : qu'est-ce qui distingue une vraie micro-tx institutionnelle (fragmentée\n"
        "   pour masquer) d'une vraie poussière de retail (ordinals, inscriptions, spam) ?\n"
        "2) Quels sont les MÉCANISMES précis que les gros porteurs utilisent ? (fragmentation,\n"
        "   timing, CPFP, blocs privés, OTC...) Classe-les par fiabilité de détection.\n"
        "3) Comment la détecter avec NOS données : poussiere_taux_fantome, bloc_privatise,\n"
        "   fee_pressure, rbf, ipt, sdi ? Quelle est la combinaison de signaux la plus\n"
        "   discriminante ? Donne la formule de codage complète.\n"
        "4) Comment la distinguer d'une VRAIE accumulation/distribution ? Quels faux positifs\n"
        "   guettent (le bloc privatisé à 12% = DATUM structurel, on l'a appris) ?\n"
        "5) Comment la poussière institutionnelle se relie-t-elle à nos patterns maison\n"
        "   (hivernage Binance, cycle QAIT, divergence CHIP) ?"
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
    print("=== SESSION CORTANA — APPROFONDIR LA POUSSIÈRE INSTITUTIONNELLE ===", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "poussiere-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    user1 = (
        "Explicite ta VISION COMPLÈTE de la poussière institutionnelle : définition précise,\n"
        "mécanismes, détection avec nos données, faux positifs, lien avec nos patterns maison.\n"
        "Réponds point par point, de façon opérationnelle (formules incluses) :\n\n" + contexte()
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
                "Regard critique : cette vision de la poussière institutionnelle est-elle\n"
                "FIABLE ou sur-interprétée ? On a déjà eu une leçon : le taux fantôme élevé\n"
                "des blocs = surtout du minage DATUM structurel, pas de l'obfuscation.\n"
                "Trouve les FAUSSES ALARMES de ta propre vision, puis les 2-3 améliorations\n"
                "concrètes qui rendraient la détection robuste sur nos small caps."
            )
        elif tour == 2:
            next_q = (
                "Tu as proposé : " + " | ".join(prev) +
                ". TROUVE maintenant des éléments DIFFÉRENTS et plus profonds :\n"
                "- un mécanisme de poussière institutionnelle que tu n'as pas encore cité\n"
                "- la SIGNATURE LA PLUS DISCRIMINANTE à coder en premier (parmi nos données)\n"
                "- comment la poussière se distingue-t-elle d'une vraie accumulation ?\n"
                "Refuse-toi de répéter ce que tu as déjà dit."
            )
        elif tour == 3:
            next_q = (
                "Dernière passe : TROUVE encore UNE chose nouvelle et déterminante — un détail\n"
                "que tout le monde rate dans la poussière institutionnelle (le lien avec le\n"
                "fee_pressure ? le rbf ? le ipt micro_tx_ratio ? le sdi ? le timing de session ?\n"
                "la corrélation avec le bloc privatisé ?). Réponds seulement APRÈS avoir\n"
                "vraiment cherché. Puis donne ta VISION EN 5 LIGNES : qu'est-ce que la\n"
                "poussière institutionnelle, en une phrase, et que coder en premier ?"
            )
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:150]}")

    print("\n=== FIN DE SESSION (archivée, session " + session_id + ") ===", flush=True)


if __name__ == "__main__":
    main()