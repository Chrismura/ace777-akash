#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_famille_evenements_croises.py
=======================================
Consultation FAMILLE (30/08, GO Christophe) : « crée la fiche et on interroge
la famille, mais avant cherchons d'autres sources d'événements particuliers,
même d'ordre climatique (car géoingénierie, armes de dissuasion, c'est une
réalité — c'est prouvé). »

Contexte : mouvement on-chain massif (87 344 BTC sortis des coffres froids,
bloc de 20 755 BTC ≈ 1,8 Md$, poussière max, CPFP actif) + visite CIA-Moscou
(25/08, première depuis 2022) + refonte financière du Vatican (11-20/08) +
été climatique extrême + géoingénierie solaire qui démarre (Stardust) + CME
solaire M6.9 du 25/08 (tempête G1-G2 27-29/08, en cours).

Mode : spéculation/recherche. AUCUNE décision de trade.

Trio maison : GEMINI (analyste) / DEEPSEEK (technique) / LE JUGE (tranche).
Réponses complètes écrites dans le dossier de sortie + journalisées.
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
OUT = SCRIPTS / "CONSULTATION_FAMILLE_EVENEMENTS_CROISES_20260830"

ROLES = {
    "audit.protocol": (
        "Tu es GEMINI, analyste senior de la maison ACE777. Donne un avis "
        "STRUCTURÉ mais concis : les risques, les angles morts, ce qu'on "
        "pourrait rater dans l'analyse croisée des événements. Important : "
        "notre système tourne sur macOS (pas Windows). Réponds en français. "
        "Termine par : MA LECTURE : ... / CE QU'ON POURRAIT RATER : ..."
    ),
    "mission": (
        "Tu es DEEPSEEK, expert technique de la maison ACE777. Donne un avis "
        "STRUCTURÉ mais concis : la cohérence du raisonnement, ce qui peut "
        "casser, la faisabilité de la méthode (observer la destination des "
        "fonds, dérivés, persistance CPFP). Important : notre système tourne "
        "sur macOS (pas Windows). Réponds en français. Termine par : CE QUI "
        "TIENT : ... / CE QUI PEUT CASSER : ... / CE QU'ON DEVRAIT AJOUTER : ..."
    ),
    "signets.juge": (
        "Tu es le JUGE de la maison ACE777. Après avoir pesé les arguments, "
        "TRANCHE la décision de façon claire et concise : OUI / NON / SOUS "
        "CONDITION. Ici la question n'est pas une action de trade mais : "
        "devons-nous considérer ce croisement d'événements comme un signal de "
        "préparation institutionnelle majeure, ou comme une coïncidence sans "
        "valeur opérationnelle ? Important : notre système tourne sur macOS "
        "(pas Windows). Réponds en français. Termine par : VERDICT : ... / "
        "CONDITION : ..."
    ),
}

TASKS = ["audit.protocol", "mission", "signets.juge"]
NOMS = ["GEMINI (analyste)", "DEEPSEEK (technique)", "LE JUGE tranche"]


def lire_fiche() -> str:
    """Charge le résumé du contexte depuis la fiche (ou texte de secours)."""
    f = INDEX / "OUTBOX_OBSIDIAN" / "Crypto_Projet" / "FICHE_RECHERCHE_EVENEMENTS_CROISES_20260830.md"
    if f.exists():
        txt = f.read_text(encoding="utf-8")
        return txt[:6000]
    return "Fiche non trouvée — voir contexte dans la demande."


def contexte() -> str:
    return (
        "=== CONTEXTE (vérifié, sources croisées) ===\n"
        "1) ON-CHAIN (notre brut) : CPFP actif, poussière 45-50/50, bloc de "
        "20 755 BTC ≈ 1,8 Md$ (z-score 71,8), 87 344 BTC sortis des coffres "
        "froids de Binance + Bitbank (15 gros blocs), direction NEUTRE, prix "
        "calme, blocs privatisés ~7 %. La signature PERSISTE.\n"
        "2) GÉOPOLITIQUE : le directeur de la CIA (John Ratcliffe) s'est "
        "rendu à Moscou le 25/08 — PREMIÈRE visite d'un patron de la CIA en "
        "Russie depuis 2022, secrète, révélée après coup, en pleine escalade "
        "Ukraine. Le Vatican (pape Léon XIV) refond sa finance interne : "
        "8 nouveaux membres au Conseil pour l'Économie (11/08) + retrait à la "
        "banque du Vatican de son autorité exclusive sur les investissements "
        "(20/08).\n"
        "3) CLIMAT : été 2026 historiquement extrême en Europe (5e canicule "
        "en France, feux hors norme, sécheresse inédite). Géo-ingénierie "
        "active : Stardust Solutions (start-up US-israélienne) lance des "
        "expériences solaires en extérieur dès avril 2026 ; vide de "
        "gouvernance mondiale (écocide law débattue).\n"
        "4) SOLAIRE : éruption M6.9 le 25/08 à 10:02 UTC (Active Region "
        "4513) avec CME dirigée vers la Terre ; veille NOAA G1-G2 du 27 au "
        "29/08 — EN COURS maintenant.\n\n"
        "=== LE CROISEMENT TEMPOREL ===\n"
        "Le 25/08 : CIA à Moscou + éruption M6.9 avec CME. Dans la fenêtre "
        "25-29/08 : 87 344 BTC déplacés en camouflage + Vatican en refonte "
        "financière + été climatique le plus extrême. La question de "
        "Christophe : « on ne peut pas croire qu'on est en mode spéculation "
        "sans chercher à mieux comprendre ce qui se passe » — les événements "
        "conjoints sont-ils anodins ou pas ?\n\n"
        "=== LA CONSIGNE ===\n"
        "Mode SPÉCULATION/RECHERCHE — AUCUNE décision de trade. Donne ton "
        "avis croisé : ces événements simultanés sont-ils une coïncidence ou "
        "le signe d'une phase de préparation mondiale ? Que faut-il surveiller "
        "pour trancher ? Sois franc, sans langue de bois, en distinguant "
        "toujours ce qui est vérifié de ce qui est conjoncture."
    )


def ask(task: str, user: str, max_tokens: int = 900, essais: int = 3) -> tuple:
    payload = json.dumps({
        "task": task,
        "messages": [{"role": "system", "content": ROLES[task]},
                     {"role": "user", "content": user}],
        "temperature": 0.3, "max_tokens": max_tokens,
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
            print(f"  [ask {task}] essai {e}/{essais} échoué: {ex}", flush=True)
            if e < essais:
                time.sleep(10)
    raise RuntimeError(f"Hub injoignable ({task}): {dernier_err}")


def journalise(session_id, membre, question, reponse, provider):
    try:
        os.makedirs(CHATS_LOG.parent, exist_ok=True)
        with open(CHATS_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "session": session_id, "membre": membre, "ts": time.time(),
                "ts_iso": datetime.now(timezone.utc).isoformat(),
                "question": question, "reponse": reponse,
                "provider": f"famille:{provider}",
            }, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main() -> int:
    print("=== CONSULTATION FAMILLE — ÉVÉNEMENTS CROISÉS ===\n", flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    session_id = "famille-evenements-croises-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    ctx = contexte()

    parties = []
    for i, task in enumerate(TASKS):
        print(f"\n----- {NOMS[i]} -----", flush=True)
        try:
            rep, prov = ask(task, ctx)
        except Exception as ex:
            print(f"  ÉCHEC: {ex}", flush=True)
            rep, prov = "", "?"
        parties.append((NOMS[i], rep, prov))
        print(f"[{prov}] " + rep.replace("\n", " ")[:600] + "\n", flush=True)
        journalise(session_id, task, ctx, rep, prov)

    ts = datetime.now().isoformat(timespec="seconds")
    md = [
        "# CONSULTATION FAMILLE — ÉVÉNEMENTS CROISÉS (30/08/2026)",
        "",
        f"Session : `{session_id}`",
        f"Date : {ts}",
        "",
        "## Contexte soumis (résumé)",
        "",
        "Mouvement on-chain massif (87 344 BTC coffres froids, bloc 20 755 BTC ≈ 1,8 Md$, "
        "poussière max, CPFP actif) + visite CIA-Moscou (25/08) + refonte financière du "
        "Vatican + été climatique extrême + géoingénierie (Stardust) + CME M6.9 du 25/08 "
        "(tempête G1-G2 en cours). Mode spéculation/recherche, aucune décision de trade.",
        "",
        "## Avis des membres",
        "",
    ]
    for nom, rep, prov in parties:
        md.append(f"### {nom} — [{prov}]")
        md.append("")
        md.append(rep.strip())
        md.append("")

    (OUT / "FAMILLE_SESSION.md").write_text("\n".join(md), encoding="utf-8")
    print("\n=== FIN CONSULTATION ===", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
