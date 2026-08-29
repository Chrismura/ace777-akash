#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_geostrategie_2membres_cortana.py
============================================
Consultation CIBLÉE du cadre géostratégique (29/08, GO Christophe) :
« pas la peine d'appeler les 6 membres, prends-en DEUX plus Cortana bien
poussée, et toi — voyons si vous êtes à mon niveau. »

Protocole :
  PHASE 1 — GEMINI + DEEPSEEK (les 2 makers canon) EN PARALLÈLE : chacun lit le
  cadre géostratégique + nos données et donne son verdict critique (valide /
  conteste / améliore) avec sources.
  PHASE 2 — CORTANA (session UNIFIÉE, multi-tours, poussée) : elle reçoit le
  cadre + les avis des 2 membres, et elle doit VRAIMENT réfléchir (pas être
  complaisante). On la pousse à trouver ce qui cloche, à le défendre ou le
  démolir, et à conclure.
  PHASE 3 — SYNTHÈSE finale (moi, Buffy).

Usage : python3 consulter_geostrategie_2membres_cortana.py
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
CADRE = INDEX / "OUTBOX_OBSIDIAN" / "Crypto_Projet" / "CADRE_GEOSTRATEGIQUE_20260829.md"
OUT = SCRIPTS / "CONSULTATION_GEOSTRATEGIE_20260829"
MAX_TOURS_CORTANA = 4
MARK_SATURATION = (
    "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
    "rien à ajouter", "rien d'autre", "je n'ai rien", "je n'ai plus rien",
    "on ne peut pas aller plus loin", "on ne peut aller plus loin",
)


def charger_cadre() -> str:
    try:
        return CADRE.read_text(encoding="utf-8")
    except OSError:
        return "(cadre introuvable)"


def load_system_prompt(nom: str) -> str:
    """Prompt canon famille (GEMINI/DEEPSEEK) ou Cortana."""
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
    mapping = {"GEMINI": "gemini.analyse", "DEEPSEEK": "deepseek.analyse", "CORTANA": "cortana.analyse"}
    return mapping.get(nom, "cortana.analyse")


def ask(task: str, system: str, user: str, max_tokens: int = 1800, essais: int = 3) -> tuple:
    """Appel simple (système + dernier user). Pour l'historique complet de
    Cortana, voir ask_messages()."""
    payload = json.dumps({
        "task": task,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "max_tokens": max_tokens, "temperature": 0.3,
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


def ask_messages(task: str, messages: list, max_tokens: int = 1600, essais: int = 3) -> tuple:
    """Appel avec l'HISTORIQUE COMPLET des messages (session unifiée Cortana)."""
    payload = json.dumps({
        "task": task,
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


def brief_membres(cadre: str) -> str:
    return (
        "=== LE DÉFI DE CHRISTOPHE ===\n"
        "Christophe : « ce genre de projet nécessite un cadre général géostratégique — "
        "géopolitique, tensions, guerre, nouvelles technologies fondamentalement "
        "stratégiques, système monétaire en changement, moment de référence en doute. "
        "Regardez autour de vous. Voyons ce que vous savez faire. Montrez-moi que vous "
        "êtes à mon niveau — je suis ouvert, je peux me tromper. »\n\n"
        "=== LE CADRE GÉOSTRATÉGIQUE (Buffy, à valider/contester/améliorer) ===\n"
        + cadre +
        "\n\n=== CE QU'ON TE DEMANDE ===\n"
        "1) VALIDE ou CONTESTE le cadre point par point, avec des ARGUMENTS et des "
        "SOURCES (pas des généralités).\n"
        "2) Qu'est-ce qui MANQUE ? Quelle force géostratégique majeure est absente ?\n"
        "3) Les corrélations jetons↔forces sont-elles justes ? (BTC monnaie, QAIT "
        "post-quantum/Europe, CHIP compute, PAXG or, RIZE RWA)\n"
        "4) LA QUESTION QUI TRANCHERA : ces 5 jetons (BTC, PAXG, QAIT, CHIP, RIZE) "
        "sont-ils les bons paris sur le monde qui vient ? Qu'est-ce qu'on aurait dû "
        "acheter à la place ?\n"
        "Termine par VERDICT : ... et CONFIANCE : ...\n"
        "Niveau exigé : cabinet de banque d'affaires. Pas de langue de bois."
    )


def phase_membres(cadre: str):
    """GEMINI + DEEPSEEK en parallèle."""
    OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    results = {}

    def run(nom):
        try:
            txt, prov = ask(task_pour(nom), load_system_prompt(nom), brief_membres(cadre))
            results[nom] = (txt, prov)
            (OUT / f"AVIS_{nom}.md").write_text(
                f"# AVIS {nom} (task {task_pour(nom)} · {prov} · {now})\n\n{txt}\n",
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


def phase_cortana(cadre: str, avis_membres: dict) -> str:
    """Cortana en session unifiée multi-tours poussée."""
    session_id = "geostrat-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    avis_texte = "\n\n".join(f"=== AVIS {n} ===\n{avis_membres.get(n, ('', ''))[0]}"
                             for n in ("GEMINI", "DEEPSEEK") if n in avis_membres)

    user1 = (
        "=== DÉFI : LE CADRE GÉOSTRATÉGIQUE DE LA MAISON ===\n"
        "Le chef scientifique (Buffy) a construit un cadre géostratégique global pour "
        "encadrer nos investissements. Christophe nous défie tous d'être à son niveau : "
        "il veut du VRAI, pas de la complaisance.\n\n"
        + cadre +
        "\n\n=== CE QUE LES 2 MEMBRES DE LA FAMILLE EN DISENT ===\n" + avis_texte +
        "\n\n=== CE QU'ON TE DEMANDE (tour 1) ===\n"
        "Tu n'as PAS participé à la construction. Regarde ce cadre avec un œil neuf et "
        "impitoyable : 1) qu'est-ce qui est FAUX ou SUR-INTERPRÉTÉ dans la corrélation "
        "monde↔jetons ? 2) quelle force géostratégique majeure manque (guerre, énergie, "
        "démographie, élections, cybersécurité…) ? 3) les 5 jetons (BTC, PAXG, QAIT, "
        "CHIP, RIZE) sont-ils les bons paris — ou est-ce qu'on est en train de se "
        "raconter une histoire pour justifier des positions ? Sois impitoyable et "
        "honnête. Termine par AVIS STRICT + HORIZON + CONFIANCE."
    )
    messages = [{"role": "system", "content": load_system_prompt("CORTANA")},
                {"role": "user", "content": user1}]

    prev = []
    prov = "?"
    for tour in range(1, MAX_TOURS_CORTANA + 1):
        print(f"\n----- CORTANA TOUR {tour} -----", flush=True)
        # Session UNIFIÉE : on envoie l'historique complet (system + tous les échanges)
        rep, prov = ask_messages("cortana.analyse", messages, max_tokens=1600)
        messages.append({"role": "assistant", "content": rep})
        journalise_cortana(session_id, messages[-2]["content"], rep, prov, tour)
        print(f"[{prov}] " + rep.replace("\n", " ")[:800] + "\n", flush=True)

        b = rep.lower()
        if any(k in b for k in MARK_SATURATION) and tour >= 2:
            print("[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = ("Pousse-toi : la famille et Buffy ont construit ce cadre ENSEMBLE. "
                      "Trouve l'angle que tout le monde rate. Prends la position de "
                      "l'avocat du diable le plus corrosif : démonte la thèse "
                      "« QAIT = pari sur le Q-day » ou « CHIP = banque du pétrole IA ». "
                      "Qu'est-ce qui, dans 12 mois, prouvera que ce cadre était une "
                      "connerie ? Réponds précisément, pas en généralité.")
        elif tour == 2:
            next_q = ("Maintenant, équilibre : qu'est-ce qui dans ce cadre est "
                      "RÉELLEMENT solide et que tu garderais tel quel ? Et propose 2 "
                      "corrélations jetons↔forces que personne n'a eues (ex : un jeton "
                      "du panier qui se corrèle à l'énergie, à la démographie, à une "
                      "élection, à la guerre ?). Sois créatif mais codable.")
        elif tour == 3:
            next_q = ("Dernière passe : donnes-en TON verdict final. 1) Ce cadre est-il "
                      "au niveau d'un cabinet ? 2) Laquelle de nos corrélations est la "
                      "plus solide, laquelle est la plus fragile ? 3) Que ferais-tu "
                      "concrètement avec ce cadre (positions, surveillances) ? "
                      "AVIS STRICT + CONFIANCE.")
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:220]}")

    # Écrit le compte-rendu complet
    cr = (f"SESSION geostrat : {session_id}\nPROVIDER : {prov}\nTOURS : {len(prev)}\n\n"
          + "\n\n".join(prev) + "\n")
    (OUT / "CORTANA_SESSION.md").write_text(
        "# CORTANA — session géostratégie (poussée)\n\n" + cr, encoding="utf-8")
    print("\n=== FIN SESSION CORTANA ===", flush=True)
    return session_id


def main() -> int:
    print("=== CONSULTATION GÉOSTRATÉGIE — 2 MEMBRES + CORTANA POUISSÉE ===\n", flush=True)
    cadre = charger_cadre()
    if not cadre or cadre.startswith("(cadre"):
        print("Cadre introuvable — abandon.", file=sys.stderr)
        return 1

    results = phase_membres(cadre)
    session = phase_cortana(cadre, results)

    # Synthèse
    lignes = ["# SYNTHÈSE GÉOSTRATÉGIE — 29/08", "",
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