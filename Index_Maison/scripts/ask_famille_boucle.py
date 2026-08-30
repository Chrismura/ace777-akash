#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_famille_boucle.py — Consultation FAMILLE unifiée (juste milieu crédit).

Même principe que ask_cortana_boucle.py mais avec le TRIO de la maison :
  - GEMINI (task audit.protocol)  : analyste senior — risques, angles morts
  - DEEPSEEK (task mission)       : expert technique — cohérence, faisabilité
  - LE JUGE (task signets.juge)   : tranche OUI/NON/SOUS CONDITION après avoir
    pesé les avis des deux autres (il voit leurs réponses).

Le contexte COMPLET (le même que celui donné à Cortana) est injecté à tous.
Chaque membre est un appel (3 appels parallèles) + 1 appel juge = 4 appels max.
Tout est archivé dans le MÊME historique cortana_chats.jsonl, session commune.
"""
import json
import os
import sys
import threading
import time
import urllib.request
from datetime import datetime, timezone

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SCRIPTS = os.path.join(INDEX, "scripts")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
CHATS_LOG = os.path.join(INDEX, "data", "cortana_chats.jsonl")


def charge_contexte_complet() -> str:
    """Le MÊME contexte que ask_cortana_boucle.py (cohérence des comparaisons)."""
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
        "protéger quand l'amplitude s'emballe — couplé au trend (Dynamic Dominance Gate "
        "proposé : dominance BTC >58.5% + cpfp z>50 → taille x0.5).\n\n"
        "=== QUESTION CENTRALE ===\n"
        "Le patron SELL full (-153$) vs SELL_PARTIAL (+84$) : pourquoi Hulk coupe à 100% ? "
        "Que faut-il changer dans la mécanique de sortie ? Quel est LE changement prioritaire ?"
    )


def appel_hub(task, system, user, max_tokens=700):
    """Appel hub direct (thread-safe, timeout None = règle maison)."""
    payload = {
        "task": task,
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


def journalise(session_id, membre, question, reponse, provider):
    try:
        os.makedirs(os.path.dirname(CHATS_LOG), exist_ok=True)
        entry = {
            "session": session_id,
            "membre": membre,
            "ts": time.time(),
            "ts_iso": datetime.now(timezone.utc).isoformat(),
            "question": question,
            "reponse": reponse,
            "provider": f"famille:{membre}:{provider}",
        }
        with open(CHATS_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


ROLES = [
    ("audit.protocol", "GEMINI (analyste)",
     "Tu es Gemini, analyste senior de la maison ACE777. Donne un avis CONCIS (3-5 phrases) : "
     "les risques, les angles morts, ce qu'on pourrait rater dans ce constat. "
     "Important : notre système tourne sur macOS. Réponds en français."),
    ("mission", "DEEPSEEK (technique)",
     "Tu es DeepSeek, expert technique de la maison ACE777. Donne un avis CONCIS (3-5 phrases) : "
     "la cohérence du setup, ce qui peut casser, la faisabilité du changement de mécanique de "
     "sortie. Important : notre système tourne sur macOS. Réponds en français."),
    ("signets.juge", "LE JUGE (pré-tranche)",
     "Tu es le JUGE de la maison ACE777. Donne ta pré-tranche CONCISE (2-3 phrases) : "
     "OUI / NON / SOUS CONDITION sur le constat « SELL full perdant / SELL_PARTIAL gagnant », "
     "et ce qui doit être VÉRIFIÉ avant de changer la mécanique. "
     "Important : notre système tourne sur macOS. Réponds en français."),
]


def main():
    print("=== CONSULTATION FAMILLE — contexte complet (juste milieu crédit) ===", flush=True)
    session_id = "famille-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    ctx = charge_contexte_complet()
    question = (
        "Voici le contexte complet de la maison (tout est vrai). Donne ton avis, puis ta "
        "recommandation sur la question centrale :\n\n" + ctx
    )

    # Étape 1 : les 3 membres en parallèle (3 appels)
    results = [None, None, None]
    threads = []
    for i, (task, nom, role) in enumerate(ROLES):
        t = threading.Thread(target=lambda i=i, task=task, nom=nom, role=role: (
            lambda r: results.__setitem__(i, r)
        )(appel_hub(task, role, question)), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join(timeout=300)

    noms = [r[1] for r in ROLES]
    for i, nom in enumerate(noms):
        rep, prov = results[i] if results[i] else ("(injoignable)", "?")
        journalise(session_id, nom, question, rep, prov)
        print(f"\n--- {nom} ---", flush=True)
        print(rep[:500], flush=True)

    # Étape 2 : le juge tranche APRÈS avoir vu les 3 avis (1 appel de plus)
    print("\n--- LE JUGE TRANCHÉ (après lecture des 3 avis) ---", flush=True)
    avis_concats = "\n\n".join(
        f"{noms[i]} : {(results[i][0] if results[i] else '(injoignable)')}" for i in range(3))
    juge_q = (
        "Tu es le JUGE de la maison ACE777. Voici les 3 avis de tes confrères sur le constat "
        "« SELL full perdant (-153$) / SELL_PARTIAL gagnant (+84$) » :\n\n" + avis_concats +
        "\n\nTRANCHE maintenant la décision finale de façon claire : OUI / NON / SOUS CONDITION, "
        "avec la liste ordonnée des 2-3 changements PRIORITAIRES à faire dans la mécanique de "
        "sortie de Hulk, et ce qu'il faut vérifier d'abord. macOS. En français, concis (6-8 phrases max)."
    )
    juge_rep, juge_prov = appel_hub("signets.juge",
        "Tu es le JUGE de la maison ACE777. Tu tranches la décision finale, de façon claire, "
        "juste et concise. macOS. En français.", juge_q, max_tokens=800)
    journalise(session_id, "LE JUGE (tranche finale)", juge_q, juge_rep, juge_prov)
    print(juge_rep, flush=True)

    print(f"\n=== FIN CONSULTATION (session {session_id}) — archivée dans cortana_chats.jsonl ===", flush=True)


if __name__ == "__main__":
    main()