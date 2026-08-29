#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
brief_cortana_cpfp_live.py
==========================
Demande à Cortana un BRIEF + AVIS sur l'état on-chain ACTUEL (30/08, 01h30).

Christophe a vu une signature CPFP et a raté le brief automatisé. On lui donne
le contexte RÉEL de live.json (pas des fichiers figés) et on lui demande :
  1. Le brief (que se passe-t-il, en clair)
  2. Son avis (que ferait-elle, quelle probabilité, quel suivi)
  3. Les limites de l'info (ce qu'on ne peut pas savoir)

Usage : python3 brief_cortana_cpfp_live.py
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INDEX = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison"))
SCRIPTS = INDEX / "scripts"
HUB = "http://127.0.0.1:11435/v1/chat/completions"
CHATS_LOG = INDEX / "data" / "cortana_chats.jsonl"
LIVE = INDEX / "thermo" / "live.json"
OUT = SCRIPTS / "BRIEF_CPFP_LIVE_20260830"
MAX_TOURS = 3


def load_system_prompt() -> str:
    for p in (
        SCRIPTS / "prompts" / "PROMPT_MASTER_ANALYSTE.md",
        Path.home() / "Documents" / "Obsidian_ACE777" / "PROMPT_MASTER_ANALYSTE.md",
    ):
        if p.exists():
            try:
                return p.read_text(encoding="utf-8")
            except Exception:
                pass
    return "Tu es Cortana, master analyste crypto du cockpit ACE777. Réponds en français, concis."


def ask_messages(messages: list, max_tokens: int = 1800, essais: int = 3) -> tuple:
    payload = json.dumps({
        "task": "cortana.analyse",
        "messages": messages,
        "max_tokens": max_tokens, "temperature": 0.4,
    }).encode()
    dernier_err = None
    for e in range(1, essais + 1):
        try:
            req = urllib.request.Request(HUB, data=payload,
                                         headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as resp:
                d = json.loads(resp.read().decode())
            return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
        except Exception as ex:
            dernier_err = ex
            print(f"  [ask] essai {e}/{essais} échoué: {type(ex).__name__}: {ex}", flush=True)
            if e < essais:
                time.sleep(10)
    raise RuntimeError(f"Hub injoignable: {dernier_err}")


def journalise(session_id, question, reponse, provider, tour):
    try:
        os.makedirs(CHATS_LOG.parent, exist_ok=True)
        with open(CHATS_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "session": session_id, "tour": tour, "ts": time.time(),
                "ts_iso": datetime.now(timezone.utc).isoformat(),
                "question": question, "reponse": reponse,
                "provider": f"cortana:{provider}",
            }, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main() -> int:
    print("=== BRIEF CORTANA — ÉTAT ONCHAIN ACTUEL (CPFP / POUSSIÈRE) ===\n", flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    session_id = "brief-cpfp-live-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    try:
        d = json.loads(LIVE.read_text(encoding="utf-8"))
        on = d.get("onchain", {})
    except Exception as e:
        on = {}
        print(f"WARN live.json illisible: {e}", file=sys.stderr)

    etat = {
        "cpfpDustScore": on.get("cpfpDustScore"),
        "cpfpMode": on.get("cpfpMode"),
        "index_onchain": on.get("index_onchain"),
        "whaleDir": on.get("whaleDir"),
        "blocPrivatiseTauxFantome": on.get("blocPrivatiseTauxFantome"),
        "blocPrivatiseNbCachees": on.get("blocPrivatiseNbCachees"),
        "whaleAlerteTexte": on.get("whaleAlerteTexte"),
        "synthèse": on.get("synthèse"),
        "alerte_urgente_du_jour": "POUSSIÈRE 50/50 + CPFP — baleine camoufle un déplacement (2 alertes URGENT : 21:06Z et 23:17Z ; z-score 71.82, bloc max 20 755 BTC vs normale 7j 5980 ± 4114)",
    }

    user1 = (
        "=== CONTEXTE : Christophe a vu une signature CPFP et a RATÉ ton brief "
        "automatisé. Il te demande de lui refaire le brief MAINTENANT, avec ton avis. ===\n"
        "Voici l'état RÉEL actuel (live.json, frais — pas des fichiers figés) :\n"
        + json.dumps(etat, ensure_ascii=False, indent=1) +
        "\n\n=== CE QU'ON TE DEMANDE (tour 1) ===\n"
        "1) LE BRIEF en clair : que se passe-t-il sur la chaîne en ce moment ? "
        "(poussière 50/45, CPFP, blocs privatisés, 15 gros blocs 87 344 BTC sur "
        "cold storage Binance/Bitbank). Explique simplement ce que la signature "
        "CPFP signifie, sans jargon inutile.\n"
        "2) TON AVIS : quelle est ta lecture ? (déplacement discret ? OTC ? "
        "accumulation ? distribution ?) Quelle probabilité, quel horizon ?\n"
        "3) CE QU'ON NE PEUT PAS SAVOIR : les limites de l'info (on voit des "
        "blocs, pas leur intention).\n"
        "Sois précise et honnête — pas de complaisance, pas de panique.\n"
        "Termine par : BRIEF : ... / MON AVIS : ... / INCERTITUDES : ..."
    )
    messages = [{"role": "system", "content": load_system_prompt()},
                {"role": "user", "content": user1}]

    prev = []
    prov = "?"
    for tour in range(1, MAX_TOURS + 1):
        print(f"\n----- CORTANA TOUR {tour} -----", flush=True)
        rep, prov = ask_messages(messages, max_tokens=1800)
        messages.append({"role": "assistant", "content": rep})
        journalise(session_id, messages[-2]["content"], rep, prov, tour)
        print(f"[{prov}] " + rep.replace("\n", " ")[:1000] + "\n", flush=True)

        if tour == 1:
            next_q = ("Tour 2 — APPROFONDIS : 1) La répétition des alertes "
                      "URGENT (21:06 et 23:17) est-elle un signal plus fort ou "
                      "du bruit ? 2) Le z-score 71.82 + bloc 20 755 BTC : "
                      "quantifie ce que ça représente en dollars et en % du "
                      "volume quotidien BTC — est-ce significatif ? 3) Que "
                      "faudrait-il observer pour passer de 'neutral' à "
                      "'accumulation' ou 'distribution' ?\n"
                      "Réponds : SIGNAL OU BRUIT : ... / ORDRE DE GRANDEUR : ... "
                      "/ CONFIRMATION À OBSERVER : ...")
        elif tour == 2:
            next_q = ("Tour 3 — SYNTHÈSE FINALE : donne le brief le plus utile "
                      "possible à Christophe en 8 lignes maximum : ce qui se "
                      "passe, ce que ça vaut, ce qu'on surveille, et ce qu'il "
                      "ne faut PAS faire. Termine par : BRIEF FINAL : ... / "
                      "À SURVEILLER : ... / NE PAS FAIRE : ...")
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:200]}")

    cr = (f"SESSION brief CPFP live : {session_id}\nPROVIDER : {prov}\nTOURS : {len(prev)}\n\n"
          + "\n\n".join(prev) + "\n")
    (OUT / "CORTANA_SESSION.md").write_text(
        "# CORTANA — brief CPFP live (session)\n\n" + cr, encoding="utf-8")
    print("\n=== FIN SESSION ===", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())