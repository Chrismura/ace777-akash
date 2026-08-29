#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_geostrategie_round3_source.py
========================================
Consultation ROUND 3 (29/08, GO Christophe) — CORROBORER la thèse, nommer
les ACTEURS, chercher la SOURCE.

Consigne de Christophe (mot pour mot) :
    « Je ne veux pas que tu leur donnes des indices. Je veux qu'ils corroborent
    leur thèse. Ils soulignent l'aspect énergétique — oui, ils ont raison. Mais
    qu'ils donnent des indications de COMMENT, et surtout QUI seront les acteurs
    qui rempliront ces trous. Pour nous c'est aussi intéressant. Il faut une
    discussion intéressante, pas chercher à avoir raison, mais chercher la
    source. »

Différence avec round 1 (critiquer) et round 2 (donner des conseils) :
ici on N'INDUIQUE PAS la réponse. Chaque IA reçoit SON propre discours des
rounds 1+2 et doit CORROBORER sa thèse :
    • la thèse (ce qu'elle a affirmé) telle quelle, sans qu'on la reformule
    • puis la PREUVE : QUI sont les acteurs concrets (noms propres) qui
      combleront les trous qu'elle a identifiés (énergie, compute, post-quantum,
      souveraineté, monnaie) ?
    • COMMENT ils le feront (mécanique concrète, pas générale) ?
    • LA SOURCE primaire (dépôt, communiqué, contrat, base de données), pas une
      synthèse de seconde main.
On ne contredit PAS, on ne valide PAS — on exige la preuve par les acteurs.

PHASE 1 — GEMINI + DEEPSEEK en parallèle.
PHASE 2 — CORTANA en session unifiée multi-tours poussée.
PHASE 3 — récap (Buffy) : on rassemble les acteurs nommés, DANS LEUR PROPRE TERMES.

Usage : python3 consulter_geostrategie_round3_source.py
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
R1_DIR = SCRIPTS / "CONSULTATION_GEOSTRATEGIE_20260829"   # AVIS du round 1
R2_DIR = SCRIPTS / "CONSULTATION_GEOSTRATEGIE_ROUND2_VISION_20260829"
SYNTHESE_R1 = INDEX / "OUTBOX_OBSIDIAN" / "Crypto_Projet" / "CONSULTATION_GEOSTRATEGIE_SYNTHESE_20260829.md"
SYNTHESE_R2 = INDEX / "OUTBOX_OBSIDIAN" / "Crypto_Projet" / "CONSULTATION_GEOSTRATEGIE_SYNTHESE_ROUND2_20260829.md"
OUT = SCRIPTS / "CONSULTATION_GEOSTRATEGIE_ROUND3_SOURCE_20260829"
MAX_TOURS_CORTANA = 4
MARK_SATURATION = (
    "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
    "rien à ajouter", "rien d'autre", "je n'ai rien", "je n'ai plus rien",
    "on ne peut pas aller plus loin", "on ne peut aller plus loin", "je n'ai pas d'autre",
)


def lire(chemin: Path) -> str:
    try:
        return chemin.read_text(encoding="utf-8")
    except OSError:
        return "(introuvable)"


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


def ask(task: str, system: str, user: str, max_tokens: int = 3000, essais: int = 3) -> tuple:
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


def ask_messages(task: str, messages: list, max_tokens: int = 2800, essais: int = 3) -> tuple:
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


def exige_la_source() -> str:
    """La consigne imposée à tous : corroborer par les ACTEURS + la SOURCE,
    SANS qu'on leur donne d'indices ni qu'on cherche à avoir raison."""
    return (
        "\n\n=== LA DEMANDE DE CHRISTOPHE (round 3) ===\n"
        "« Je ne veux pas qu'on me donne des indices. Je veux que tu CORROBORES "
        "ta thèse. Tu as souligné l'aspect énergétique — tu as raison. Mais je "
        "veux maintenant des indications de COMMENT, et surtout QUI seront les "
        "acteurs qui rempliront les trous que TU as identifiés. Pour nous c'est "
        "aussi intéressant. Il faut une discussion intéressante — pas chercher à "
        "avoir raison, mais chercher LA SOURCE. »\n\n"
        "Résumé de ce qu'il faut produire — dans TES propres termes, sans qu'on "
        "te suggère la réponse :\n"
        "  1) RAPPELLE ta thèse (ce que tu as affirmé aux rounds 1-2), telle "
        "quelle.\n"
        "  2) LES ACTEURS : pour CHAQUE trou que tu as identifié (énergie, "
        "compute, post-quantum, souveraineté, monnaie, confiance), nomme "
        "PRÉCISÉMENT les acteurs — sociétés, États, institutions, fonds, "
        "protocoles — qui vont CONCRÈTEMENT le combler. Noms propres, pas de "
        "généralités.\n"
        "  3) LE COMMENT : la mécanique concrète par laquelle chaque acteur "
        "capture la valeur (contrat, billet, décret, chaîne logistique, PPA,\n"
        "  tokenomics).\n"
        "  4) LA SOURCE PRIMAIRE : pour chaque acteur nommé, la source brute "
        "(dépôt réglementaire, communiqué officiel, contrat, base de données) — "
        "pas une synthèse de seconde main.\n"
        "Termine par : ACTEURS-CLÉS : (liste, un par ligne) / SOURCES : ... / "
        "PREUVE EN 12 MOIS : ..."
    )


def brief_source_membre(nom: str, avis_r1: str, vision_r2: str) -> str:
    return (
        "=== CE QUE TU AS AFFIRMÉ AU ROUND 1 (ton avis critique) ===\n" + avis_r1 +
        "\n\n=== CE QUE TU AS PROPOSÉ AU ROUND 2 (ta vision) ===\n" + vision_r2 +
        exige_la_source()
    )


def phase_membres():
    OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    results = {}

    def run(nom):
        avis_path = R1_DIR / f"AVIS_{nom}.md"
        if not avis_path.exists():
            avis_path = R2_DIR / f"VISION_{nom}.md"   # fallback : se caler sur sa vision r2
        avis_r1 = lire(avis_path)
        vision_r2 = lire(R2_DIR / f"VISION_{nom}.md")
        try:
            txt, prov = ask(task_pour(nom), load_system_prompt(nom),
                            brief_source_membre(nom, avis_r1, vision_r2), max_tokens=3000)
            results[nom] = (txt, prov)
            (OUT / f"SOURCE_{nom}.md").write_text(
                f"# SOURCE {nom} — round 3 (task {task_pour(nom)} · {prov} · {now})\n\n{txt}\n",
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


def phase_cortana(source_membres: dict) -> str:
    session_id = "geostrat-r3-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    souces_texte = "\n\n".join(
        f"=== {n} — ROUND 3 ===\n{source_membres.get(n, ('', ''))[0]}"
        for n in ("GEMINI", "DEEPSEEK") if n in source_membres)

    vision_r2_cortana = lire(R2_DIR / "CORTANA_SESSION.md")
    user1 = (
        "=== ROUND 3 — CORROBORE TA THÈSE PAR LES ACTEURS ===\n"
        "Aux rounds 1-2 tu as été impitoyable (narrative washing, pont de valeur "
        "absent, énergie comme force manquante, purge de survie). Christophe "
        "valide ton intuition sur l'énergie : « oui, ils ont raison ». Maintenant "
        "il veut que tu CORROBORES ta thèse, sans qu'on te donne d'indices : "
        "nomme précisément les ACTEURS qui combleront les trous que tu as "
        "identifiés, la mécanique concrète, et la SOURCE primaire.\n\n"
        "Voici ce que les 2 membres ont déjà corroboré (tu dois DIFFÉRENCIER ta "
        "réponse, pas répéter) :\n" + souces_texte +
        "\n\n=== TON PROPRE DISCOURS DES ROUNDS 1-2 ===\n" + vision_r2_cortana +
        exige_la_source() + "\n\nEn particulier : quels sont les acteurs (noms "
        "propres) qui, chez NOUS (crypto, small caps, cockpit de données MEXC), "
        "permettraient de capter cette thèse ? Lesquels ne sont pas cotables ? "
        "Sois précise sur les noms et les sources."
    )
    messages = [{"role": "system", "content": load_system_prompt("CORTANA")},
                {"role": "user", "content": user1}]

    prev = []
    prov = "?"
    for tour in range(1, MAX_TOURS_CORTANA + 1):
        print(f"\n----- CORTANA TOUR {tour} -----", flush=True)
        rep, prov = ask_messages("cortana.analyse", messages, max_tokens=2800)
        messages.append({"role": "assistant", "content": rep})
        journalise_cortana(session_id, messages[-2]["content"], rep, prov, tour)
        print(f"[{prov}] " + rep.replace("\n", " ")[:800] + "\n", flush=True)

        b = rep.lower()
        if any(k in b for k in MARK_SATURATION) and tour >= 2:
            print("[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = ("Pousse plus loin : tu as nommé des acteurs. Maintenant "
                      "creuse LA chaîne jusqu'au bout — pour CHAQUE acteur que "
                      "tu as cité, dis-nous QUI derrière (les dirigeants, les "
                      "fonds, les gouvernements) et QUELLE est la tension qui "
                      "peut les faire échouer. Entre les noms que GEMINI et "
                      "DEEPSEEK ont cités et les tiens, lequel est LE plus sous-"
                      "évalué selon toi, et pourquoi ? Donne LA source primaire "
                      "qui le prouve.\n"
                      "Réponds en priorité : ACTEUR SOUS-ÉVALUÉ + PREUVE PAGE "
                      "SPÉCIFIQUE.")
        elif tour == 2:
            next_q = ("Il manque encore quelque chose : parmi les acteurs cités, "
                      "lesquels sont accessibles à un trader crypto retail (cotés "
                      "officiellement sur une vraie bourse ou une chaîne "
                      "vérifiable) et lesquels ne le sont pas ? Et surtout : quelle est la MEILLEURE "
                      "façon (selon toi) de profiter de cette thèse sans te "
                      "mentir sur le risque — via un jeton, une action, une "
                      "tracker ? Tranche.\n"
                      "Réponds : MEILLEUR VÉHICULE.")
        elif tour == 3:
            next_q = ("Dernière passe — la vérification : donne le test DES plus "
                      "rigoureux pour savoir si ta thèse se réalise : quel "
                      "indicateur, quelle source, quelle date. Et dis-nous "
                      "honnêtement : laquelle de TES propositions, dans 12 mois, "
                      "aura le plus de chances de s'être effondrée — et pourquoi "
                      "tu continues à la défendre malgré ça ?\n"
                      "Réponds : TEST + AUTO-CONTRADICTION ASSUMÉE.")
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:220]}")

    cr = (f"SESSION geostrat round3 : {session_id}\nPROVIDER : {prov}\nTOURS : {len(prev)}\n\n"
          + "\n\n".join(prev) + "\n")
    (OUT / "CORTANA_SESSION.md").write_text(
        "# CORTANA — round 3 source (poussée)\n\n" + cr, encoding="utf-8")
    print("\n=== FIN SESSION CORTANA ROUND 3 ===", flush=True)
    return session_id


def main() -> int:
    print("=== CONSULTATION GÉOSTRATÉGIE ROUND 3 — CORROBORER PAR LES ACTEURS ===\n", flush=True)

    results = phase_membres()
    session = phase_cortana(results)

    lignes = ["# SYNTHÈSE ROUND 3 GÉOSTRATÉGIE — 29/08", "",
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