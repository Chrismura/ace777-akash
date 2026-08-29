#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_theorie_suppression_nucleaire.py
==========================================
Consultation FAMILLE + CORTANA (29/08, GO Christophe) sur sa théorie :
« les technologies nucléaires compactes/mobiles (type batterie-œuf transportable)
qui aideraient énormément les populations ont été sorties du marché par les
géants de l'énergie — l'histoire est pleine de super inventions anéanties pour
les intérêts de peu. »

On soumet à la famille (GEMINI + DEEPSEEK) et à Cortana (session poussée) :
  1. La thèse de Christophe (en ses propres mots)
  2. Les FAITS VÉRIFIÉS (croisement de ce matin) :
     - Cas DOCUMENTÉ de technologies étouffées : Cartel Phoebus (ampoules, obsolescence programmée) — RÉEL.
     - MAIS le retard des SMR est documenté comme un problème de COÛT, pas de complot :
       NuScale projet annulé, coût passé de 5 à 9 Md$ ; petits réacteurs fuient plus de neutrons donc plus chers par MW.
     - Le vrai micro-réacteur qui existe : ZEUS de NANO Nuclear (tient dans un conteneur maritime, brevets USPTO, subvention DOE/Idaho). RÉEL mais développement.
     - L'« œuf » qui a fait le buzz (Enron Egg : batterie de poche 10 ans à 19 000 $) = PARODIE marketing, pas un vrai produit.
  3. Consigne : chercher la SOURCE, pas avoir raison ; distinguer « vrai cas historique » de « fantasme ».

PHASE 1 — GEMINI + DEEPSEEK en parallèle.
PHASE 2 — CORTANA en session unifiée multi-tours poussée.
PHASE 3 — récap Buffy.

Usage : python3 consulter_theorie_suppression_nucleaire.py
"""
import json
import os
import sys
import threading
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INDEX = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison"))
SCRIPTS = INDEX / "scripts"
HUB = "http://127.0.0.1:11435/v1/chat/completions"
IDENTITE = INDEX / "identity" / "prompts" / "famille.json"
CHATS_LOG = INDEX / "data" / "cortana_chats.jsonl"
OUT = SCRIPTS / "CONSULTATION_FAMILLE_SUPPRESSION_NUCLEAIRE_20260829"
MAX_TOURS_CORTANA = 4
MARK_SATURATION = (
    "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
    "rien à ajouter", "rien d'autre", "je n'ai rien", "je n'ai plus rien",
    "on ne peut pas aller plus loin", "on ne peut aller plus loin",
)


def load_system_prompt(nom: str) -> str:
    if nom in ("GEMINI", "DEEPSEEK"):
        try:
            data = json.loads(IDENTITE.read_text(encoding="utf-8"))
            for m in data.get("membres", []):
                if m.get("nom") == nom:
                    return m.get("prompt", "")
        except Exception:
            pass
        return f"Tu es {nom}, membre de la famille ACE777. Réponds en français, factuel, concis."
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


def task_pour(nom: str) -> str:
    return {"GEMINI": "gemini.analyse", "DEEPSEEK": "deepseek.analyse", "CORTANA": "cortana.analyse"}.get(nom, "cortana.analyse")


def ask(task: str, system: str, user: str, max_tokens: int = 2200, essais: int = 3) -> tuple:
    payload = json.dumps({
        "task": task,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "max_tokens": max_tokens, "temperature": 0.35,
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
            print(f"  [ask {task}] essai {e}/{essais} échoué: {type(ex).__name__}: {ex}", flush=True)
            if e < essais:
                time.sleep(10)
    raise RuntimeError(f"Hub injoignable: {dernier_err}")


def ask_messages(task: str, messages: list, max_tokens: int = 2000, essais: int = 3) -> tuple:
    payload = json.dumps({
        "task": task,
        "messages": messages,
        "max_tokens": max_tokens, "temperature": 0.42,
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
            print(f"  [ask_messages] essai {e}/{essais} échoué: {type(ex).__name__}: {ex}", flush=True)
            if e < essais:
                time.sleep(10)
    raise RuntimeError(f"Hub injoignable: {dernier_err}")


def journalise_cortana(session_id, question, reponse, provider, tour):
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


def contexte() -> str:
    return (
        "=== LA THÈSE DE CHRISTOPHE (mot pour mot, vulgarisée) ===\n"
        "« Franchement, entre toi et moi, je n'ai pas les preuves, mais je serais "
        "prêt à parier qu'ils ont tout fait pour sortir cette technologie du "
        "marché, car elle aurait énormément aidé les populations. Imagine les "
        "géants de l'énergie : tu crois qu'ils laisseraient une telle technologie "
        "à disposition des gens ? Non. Et l'histoire est pleine d'exemples de "
        "super inventions anéanties pour les intérêts de peu. Le monde des hommes "
        "est pervers et impitoyable, et complètement illogique — mais aussi tout "
        "son contraire. »\n\n"
        "La technologie en question : le nucléaire COMPACT / MOBILE (réacteurs "
        "petits et transportables, type SMR, micro-réacteurs, batteries "
        "atomiques) qui pourrait alimenter l'IA et les populations sans dépendre "
        "des grands réseaux.\n\n"
        "=== LES FAITS VÉRIFIÉS CE MATIN (croisement, règle des 2 sources) ===\n"
        "1. [VRAI — historique]. Il existe des cas DOCUMENTÉS de technologies "
        "étouffées : le Cartel Phoebus (1924-1939, Philips/GE/Osram) a limité "
        "volontairement la durée de vie des ampoules à 1 000 h — l'obsolescence "
        "programmée, démontrée.\n"
        "2. [MAIS — le contre-argument clé]. Le retard des SMR est documenté comme "
        "un problème de COÛT, pas comme un complot : le projet NuScale a été "
        "ANNULÉ (2023) après un coût passé de 5 à 9 Md$ (+75 %) ; les petits "
        "réacteurs fuient plus de neutrons donc sont PLUS CHERS par MW que les "
        "grands. C'est la physique et l'économie, pas une supposée main cachée.\n"
        "3. [RÉEL]. Il existe un vrai micro-réacteur : ZEUS de NANO Nuclear Energy — "
        "cœur « batterie » scellé tenant dans UN conteneur maritime standard, "
        "brevets USPTO déposés, subvention DOE/Idaho National Lab. Mais c'est du "
        "développement, pas un produit de marché.\n"
        "4. [PARODIE]. La « batterie-œuf » qui a fait le buzz (Enron Egg : "
        "alimenter une maison 10 ans pour 19 000 $) — c'est un canular marketing "
        "d'Enron, PAS un vrai produit. Ne pas confondre avec le point 3.\n\n"
        "Consigne : on cherche la VÉRITÉ, pas à avoir raison. Distingue clairement "
        "les VRAIS cas historiques de suppression technologique (point 1) d'une "
        "théorie du complot sans preuve. Sois honnête, factuel, sourcé."
    )


def brief_membre(nom: str) -> str:
    return contexte() + (
        "\n\n=== CE QU'ON TE DEMANDE ===\n"
        "1) Qu'est-ce qui, dans la thèse de Christophe, est VRAI (sourcé) ? "
        "Donne les cas documentés de technologies étouffées par des intérêts "
        "établis (pas seulement Phoebus).\n"
        "2) Qu'est-ce qui est FAUX ou EXAGÉRÉ ? Pourquoi le nucléaire compact ne "
        "s'impose pas AUSSI pour des raisons techniques/économiques honnêtes ?\n"
        "3) Le cœur de la question : pour alimenter l'IA ET les populations, la "
        "voie nucléaire compacte/mobile est-elle réprimée par les géants de "
        "l'énergie, ou freinée par des contraintes réelles ? Donne LA source qui "
        "le prouve (pas une opinion).\n"
        "4) Un trader retail pourrait-il investir là-dedans réellement (actions, "
        "ETF) — et lesquelles ?\n"
        "Termine par : VERDICT : ... / CE QUI EST VRAI : ... / CE QUI EST FAUX : ... "
        "/ SOURCE : ... / CONFIANCE : ..."
    )


def phase_membres():
    OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    results = {}

    def run(nom):
        try:
            txt, prov = ask(task_pour(nom), load_system_prompt(nom), brief_membre(nom), max_tokens=2200)
            results[nom] = (txt, prov)
            (OUT / f"AVIS_{nom}.md").write_text(
                f"# AVIS {nom} — suppression nucléaire (task {task_pour(nom)} · {prov} · {now})\n\n{txt}\n",
                encoding="utf-8")
            print(f"[OK] {nom} ({prov}) — {len(txt)} chars", flush=True)
        except Exception as e:
            results[nom] = (f"[INJOIGNABLE] {e}", "?")
            print(f"[ERREUR] {nom}: {e}", flush=True)

    ths = [threading.Thread(target=run, args=(n,)) for n in ("GEMINI", "DEEPSEEK")]
    for t in ths:
        t.start()
    for t in ths:
        t.join()
    return results


def phase_cortana(avis_membres: dict) -> str:
    session_id = "suppression-nuc-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    avis_texte = "\n\n".join(
        f"=== {n} ===\n{avis_membres.get(n, ('', ''))[0]}"
        for n in ("GEMINI", "DEEPSEEK") if n in avis_membres)

    user1 = (
        "=== LA THÈSE DE CHRISTOPHE ===\n" + contexte() +
        "\n\n=== CE QUE GEMINI ET DEEPSEEK EN DISENT ===\n" + avis_texte +
        "\n\n=== CE QU'ON TE DEMANDE (tour 1) ===\n"
        "En master analyste impitoyable : 1) la thèse de Christophe (suppression "
        "du nucléaire compact par les géants de l'énergie) est-elle crédible, et "
        "à QUEL pourcentage ? Donne les cas documentés ET les raisons techniques "
        "pures qui expliquent le retard SANS complot. 2) Où est la SOURCE qui "
        "prouve l'une ou l'autre thèse ? 3) Distingue strictement 'intérêt "
        "économique des grands acteurs' (vrai mécanisme de marché) de 'complot "
        "suppressif' (difficile à prouver). Sois précise.\n"
        "Termine par : CRÉDIBILITÉ (0-100%) : ... / MÉCANISME RÉEL : ... / SOURCE : ..."
    )
    messages = [{"role": "system", "content": load_system_prompt("CORTANA")},
                {"role": "user", "content": user1}]

    prev = []
    prov = "?"
    for tour in range(1, MAX_TOURS_CORTANA + 1):
        print(f"\n----- CORTANA TOUR {tour} -----", flush=True)
        rep, prov = ask_messages("cortana.analyse", messages, max_tokens=2000)
        messages.append({"role": "assistant", "content": rep})
        journalise_cortana(session_id, messages[-2]["content"], rep, prov, tour)
        print(f"[{prov}] " + rep.replace("\n", " ")[:700] + "\n", flush=True)

        b = rep.lower()
        if any(k in b for k in MARK_SATURATION) and tour >= 2:
            print("[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = ("Pousse-toi : Christophe dit « l'histoire est pleine de "
                      "super inventions anéanties pour les intérêts de peu, mais "
                      "aussi tout son contraire ». Explorer les DEUX faces : 1) "
                      "cite 3 vrais cas historiques documentés de technologie "
                      "étouffée (au-delà de Phoebus, vérifiables) ET 2) le "
                      "contre-exemple : une technologie qui a percé malgré le "
                      "lobby (solaire ? lithium ?). Laquelle de tes remarques "
                      "ferait changer Christophe d'avis sur 30 % de sa thèse ?\n"
                      "Réponds : 3 CAS VRAIS + 1 CONTRE-EXEMPLE + CE QUI "
                      "CHANGERAIT SON AVIS.")
        elif tour == 2:
            next_q = ("Concrètement pour Christophe : s'il veut miser sur le "
                      "nucléaire compact SANS tomber dans une arnaque ou une "
                      "parodie (Enron Egg), quels sont les vrais véhicules "
                      "d'investissement réglementés (actions cotées, ETF) ? "
                      "Nomme-les précisément, avec la source. Et dis honnêtement "
                      "le risque (beaucoup sont des micro-caps spéculatives).")
        elif tour == 3:
            next_q = ("Dernière passe — le jugement : 1) en une phrase, ta "
                      "réponse à Christophe sur sa théorie du complot "
                      "énergétique. 2) Quelle EST la vraie barrière au nucléaire "
                      "compact (argent, régulation, physique, ou lobby) — "
                      "quantifiée ? 3) Un conseil actionnable pour lui demain "
                      "matin.\n"
                      "Réponds : VERDICT (une phrase) + BARRIÈRE RÉELLE (chiffrée) "
                      "+ ACTION DEMAIN.")
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:200]}")

    cr = (f"SESSION suppression nucléaire : {session_id}\nPROVIDER : {prov}\nTOURS : {len(prev)}\n\n"
          + "\n\n".join(prev) + "\n")
    (OUT / "CORTANA_SESSION.md").write_text(
        "# CORTANA — suppression nucléaire (poussée)\n\n" + cr, encoding="utf-8")
    print("\n=== FIN SESSION CORTANA ===", flush=True)
    return session_id


def main() -> int:
    print("=== CONSULTATION FAMILLE + CORTANA — THÉORIE SUPPRESSION NUCLÉAIRE ===\n", flush=True)
    results = phase_membres()
    session = phase_cortana(results)

    lignes = ["# SYNTHÈSE — SUPPRESSION NUCLÉAIRE (29/08)", "",
              "| Membre | Statut |", "|---|---|"]
    for n in ("GEMINI", "DEEPSEEK"):
        lignes.append(f"| {n} | {'OK' if n in results else 'absente'} |")
    lignes.append(f"| CORTANA | session {session} |")
    (OUT / "SYNTHESE.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("\n".join(lignes))
    print(f"\nArchive : {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())