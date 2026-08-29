#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_geostrategie_round2_vision.py
========================================
Consultation ROUND 2 (29/08, GO Christophe) — « reprendre le discours mais
qu'ils développent mieux leur vision, car en grande partie ils ont raison. »

Constat du round 1 : la consigne « démontre-nous que tu es à mon niveau » les
a poussés à CRITIQUER (impitoyables et convergents — narrative washing,
pont de valeur absent, force ÉNERGIE manquante) mais pas à PROPOSER.

Consigne round 2 : on leur rend leur PROPRE avis du round 1 + la synthèse, et
on les force à développer la VISION : concrètement, qu'est-ce qu'on fait ?
  • Amélioration du cadre (version 2.0)
  • Le setup/portefeuille idéal (positions, tailles, horizons, critères)
  • Les indicateurs/sondes à ajouter
  • La réponse à la question de Christophe : « tu ferais quoi si tu devais
    gagner de l'argent pour vivre ? »

PHASE 1 — GEMINI + DEEPSEEK en parallèle (chacun reçoit SON avis + la synthèse)
PHASE 2 — CORTANA en session unifiée multi-tours poussée (reçoit son avis +
          les 2 avis membres + la synthèse)
PHASE 3 — SYNTHÈSE finale (moi, Buffy)

Usage : python3 consulter_geostrategie_round2_vision.py
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
CRYPTO = INDEX / "OUTBOX_OBSIDIAN" / "Crypto_Projet"
ROUND1_DIR = SCRIPTS / "CONSULTATION_GEOSTRATEGIE_20260829"
SYNTHESE = CRYPTO / "CONSULTATION_GEOSTRATEGIE_SYNTHESE_20260829.md"
OUT = SCRIPTS / "CONSULTATION_GEOSTRATEGIE_ROUND2_VISION_20260829"
MAX_TOURS_CORTANA = 4
MARK_SATURATION = (
    "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
    "rien à ajouter", "rien d'autre", "je n'ai rien", "je n'ai plus rien",
    "on ne peut pas aller plus loin", "on ne peut aller plus loin",
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


def ask(task: str, system: str, user: str, max_tokens: int = 2400, essais: int = 3) -> tuple:
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


def ask_messages(task: str, messages: list, max_tokens: int = 2200, essais: int = 3) -> tuple:
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


def consigne_commune() -> str:
    return (
        "\n\n=== LA DEMANDE DE CHRISTOPHE (round 2) ===\n"
        "« Le round 1 était une demande de critique — vous avez été impitoyables "
        "et, en grande partie, vous avez raison. Mais un bon analyste ne fait pas "
        "que démolir : il construit. Développe ta vision. Concrètement :\n"
        "  1) AMÉLIORATION — donne la version 2.0 de ce qu'on doit faire.\n"
        "  2) CONSEILS CONCRETS — pas des généralités : positions, tailles, "
        "horizons, critères d'entrée/sortie, indicateurs à ajouter à nos sondes.\n"
        "  3) RÉPONDS à la question de Christophe : si tu devais vivre de ça, "
        "gagner de l'argent pour payer ta vie, que ferais-tu exactement avec ce "
        "portefeuille (BTC, PAXG, QAIT, CHIP, RIZE + les autres du panier) ?\n"
        "  4) Qu'est-ce qui, dans 12 mois, prouvera que TON conseil était bon ? "
        "(le critère de vérification)\n"
        "Sois précis, actionnable, codable. Termine par : VISION : ... / "
        "PREMIÈRE ACTION : ... / CRITÈRE DE VÉRIFICATION (12 mois) : ..."
    )


def brief_membre(nom: str, avis_perso: str, synthese: str) -> str:
    return (
        "=== ROUND 1 : TON PROPRE AVIS (que tu as donné, relis-le) ===\n"
        + avis_perso +
        "\n\n=== SYNTHÈSE DU ROUND 1 (consensus des 3 IA + verdict Buffy) ===\n"
        + synthese +
        consigne_commune()
    )


def phase_membres(synthese: str):
    OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    results = {}

    def run(nom):
        avis_perso = lire(ROUND1_DIR / f"AVIS_{nom}.md")
        try:
            txt, prov = ask(task_pour(nom), load_system_prompt(nom),
                            brief_membre(nom, avis_perso, synthese), max_tokens=2400)
            results[nom] = (txt, prov)
            (OUT / f"VISION_{nom}.md").write_text(
                f"# VISION {nom} — ROUND 2 (task {task_pour(nom)} · {prov} · {now})\n\n{txt}\n",
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


def phase_cortana(synthese: str, avis_membres: dict) -> str:
    session_id = "geostrat-r2-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    avis_texte = "\n\n".join(
        f"=== AVIS/VISION {n} (round 1 + round 2) ===\n"
        f"{lire(ROUND1_DIR / f'AVIS_{n}.md')}\n\n--- ROUND 2 :\n{avis_membres.get(n, ('', ''))[0]}"
        for n in ("GEMINI", "DEEPSEEK") if n in avis_membres)

    user1 = (
        "=== ROUND 2 — DÉVELOPPE TA VISION ===\n"
        "Au round 1, tu as été impitoyable (narrative washing, pont de valeur "
        "absent, supercherie mathématique d'échelle, force ÉNERGIE manquante). "
        "Christophe valide : « en grande partie vous avez raison ». Mais il te "
        "demande maintenant de CONSTRUIRE, pas de démolir.\n\n"
        "Voici ce que les 2 membres de la famille développent au round 2 :\n"
        + avis_texte +
        "\n\n=== TON RÔLE ===\n" +
        "En master analyste, développe TA vision complète et différenciée : "
        "1) le cadre v2.0 (forces à garder, à ajouter, à jeter), 2) la "
        "construction de portefeuille concrète que TU ferais (positions, "
        "tailles, horizons, et surtout : que faire des micro-caps QAIT/CHIP/RIZE "
        "qu'on a critiquées ?), 3) les indicateurs/sondes que tu ajouterais à "
        "notre système pour mesurer ces forces, 4) ta réponse à la question de "
        "Christophe : vivre de ça, concrètement. Sois précise et assumée."
        + consigne_commune()
    )
    messages = [{"role": "system", "content": load_system_prompt("CORTANA")},
                {"role": "user", "content": user1}]

    prev = []
    prov = "?"
    for tour in range(1, MAX_TOURS_CORTANA + 1):
        print(f"\n----- CORTANA TOUR {tour} -----", flush=True)
        rep, prov = ask_messages("cortana.analyse", messages, max_tokens=2200)
        messages.append({"role": "assistant", "content": rep})
        journalise_cortana(session_id, messages[-2]["content"], rep, prov, tour)
        print(f"[{prov}] " + rep.replace("\n", " ")[:800] + "\n", flush=True)

        b = rep.lower()
        if any(k in b for k in MARK_SATURATION) and tour >= 2:
            print("[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = ("Pousse-toi : tes collègues donnent des conseils concrets. "
                      "Développe le TIEN, plus tranché. Donne le plan d'action "
                      "exact des 30 prochains jours (quoi, quand, seuils). Et "
                      "contredis-les sur AU MOINS un point où tu penses qu'ils "
                      "ont tort. Pas de complaisance.\n"
                      "Réponds : PLAN 30 JOURS + DÉSACCORD ASSUMÉ.")
        elif tour == 2:
            next_q = ("Maintenant la question de Christophe en entier : « si tu "
                      "devais faire des plus-values pour payer les frais de ton "
                      "existence, tu ferais quoi ? » Réponds en te mettant à SA "
                      "place (capital limité, déjà exposé à ces jetons, paper "
                      "d'abord). Quelles positions exactes, quelles tailles, "
                      "quelles règles de sortie ? Sois pragmatique et honnête "
                      "sur le risque de tout perdre.")
        elif tour == 3:
            next_q = ("Dernière passe — le jugement final : 1) lequel des "
                      "conseils (le tien + GEMINI + DEEPSEEK) est le plus "
                      "actionnable cette semaine ? 2) quelle est LA chose que "
                      "Christophe devrait faire demain matin, et LA chose à "
                      "absolument NE PAS faire ? 3) ton verdict final en 5 "
                      "lignes maximum. VISION : ... / PREMIÈRE ACTION : ... / "
                      "CRITÈRE DE VÉRIFICATION (12 mois) : ...")
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:220]}")

    cr = (f"SESSION geostrat round2 : {session_id}\nPROVIDER : {prov}\nTOURS : {len(prev)}\n\n"
          + "\n\n".join(prev) + "\n")
    (OUT / "CORTANA_SESSION.md").write_text(
        "# CORTANA — round 2 vision (poussée)\n\n" + cr, encoding="utf-8")
    print("\n=== FIN SESSION CORTANA ROUND 2 ===", flush=True)
    return session_id


def main() -> int:
    print("=== CONSULTATION GÉOSTRATÉGIE ROUND 2 — DÉVELOPPER LA VISION ===\n", flush=True)
    synthese = lire(SYNTHESE)
    if not synthese or synthese.startswith("(introuvable"):
        print("Synthèse round 1 introuvable — abandon.", file=sys.stderr)
        return 1

    results = phase_membres(synthese)
    session = phase_cortana(synthese, results)

    lignes = ["# SYNTHÈSE ROUND 2 GÉOSTRATÉGIE — 29/08", "",
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
