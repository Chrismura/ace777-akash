#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier_predictions.py — La vérification du banc d'essai (11/08)
=================================================================
Relit le REGISTRE_PREDICTIONS.md, trouve les prédictions échues (date limite
passée, statut EN ATTENTE), et les re-vérifie contre les données réelles via
le hub (Gemini), puis marque : ✅ VRAIE / ❌ FAUSSE / ⚠️ NON VÉRIFIABLE.

Usage :
  python3 verifier_predictions.py              # vérifie les échues
  python3 verifier_predictions.py --tout       # vérifie aussi les non-échues
  python3 verifier_predictions.py --dry        # montre ce qui serait vérifié, ne touche à rien

Le but : à la fin du banc d'essai, on sait QUI avait raison (le youtuber ? l'IA ?).
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

REGISTRE_PATH = os.path.expanduser("~/Documents/Obsidian_ACE777/Evaluations/REGISTRE_PREDICTIONS.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
HEALTH = HUB.replace("/v1/chat/completions", "/health")
TASK = "veille.youtube"
AUJOURDHUI = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def extraire_predictions():
    """[(chaine, titre, url, date_limite, texte_pred, statut)] depuis le registre."""
    if not os.path.isfile(REGISTRE_PATH):
        print(f"[X] Registre introuvable : {REGISTRE_PATH}", file=sys.stderr)
        sys.exit(1)
    preds = []
    cur = {"chaine": "", "titre": "", "url": ""}
    for raw in open(REGISTRE_PATH, encoding="utf-8"):
        line = raw.strip()
        m = re.match(r"^### (\S+) — (.+?) : (.+)$", line)
        if m:
            cur = {"chaine": m.group(2), "titre": m.group(3), "url": ""}
            continue
        m = re.match(r"^Lien : (\S+)", line)
        if m:
            cur["url"] = m.group(1)
            continue
        m = re.match(r"^- (✅ VRAIE|❌ FAUSSE|⚠️ NON VÉRIFIABLE|⏳ EN ATTENTE) \| (.*)$", line)
        if m:
            statut, texte = m.group(1), m.group(2)
            dlim = re.search(r"\[(\d{4}-\d{2}-\d{2})\]", texte)
            preds.append({
                "chaine": cur["chaine"], "titre": cur["titre"], "url": cur["url"],
                "date_limite": dlim.group(1) if dlim else None,
                "texte": texte, "statut": statut,
            })
    return preds


def appeler_hub(texte):
    payload = {
        "task": TASK,
        "messages": [
            {"role": "system", "content": (
                "Tu es le juge du banc d'essai de veille de la maison ACE777. "
                "Tu reçois UNE prédiction faite dans le passé, avec la date d'aujourd'hui. "
                "Décide si elle est : ✅ VRAIE (s'est réalisée), ❌ FAUSSE (ne s'est pas réalisée), "
                "ou ⚠️ NON VÉRIFIABLE (pas de critère clair ou données insuffisantes). "
                "Réponds UNIQUEMENT par une ligne : <verdict> | <explication en 1 phrase, factuelle>."
            )},
            {"role": "user", "content": texte},
        ],
        "max_tokens": 200,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?")


def mettre_a_jour_registre(preds):
    """Réécrit le registre avec les nouveaux statuts."""
    # reconstruction simple : on repart du fichier et on remplace les lignes ⏳/✅/❌
    lignes = open(REGISTRE_PATH, encoding="utf-8").read().splitlines(keepends=True)
    idx = 0
    for p in preds:
        if p["statut"] in ("✅ VRAIE", "❌ FAUSSE", "⚠️ NON VÉRIFIABLE"):
            continue  # déjà vérifiée
        for i in range(idx, len(lignes)):
            if re.match(r"^- ⏳ EN ATTENTE \|", lignes[i].strip()) and p["texte"] in lignes[i]:
                lignes[i] = re.sub(r"^- ⏳ EN ATTENTE \|", f"- {p['nouveau_statut']} |", lignes[i])
                idx = i + 1
                break
    with open(REGISTRE_PATH, "w", encoding="utf-8") as f:
        f.writelines(lignes)


def main():
    ap = argparse.ArgumentParser(description="Vérification des prédictions du banc d'essai")
    ap.add_argument("--tout", action="store_true", help="vérifier aussi les non-échues")
    ap.add_argument("--dry", action="store_true", help="afficher sans modifier")
    args = ap.parse_args()

    try:
        with urllib.request.urlopen(HEALTH, timeout=5) as r:
            json.loads(r.read().decode())
    except Exception:
        print("[X] Hub :11435 injoignable. Lance le hub, puis relance.", file=sys.stderr)
        sys.exit(1)

    preds = extraire_predictions()
    echues = []
    for p in preds:
        if p["statut"] != "⏳ EN ATTENTE":
            continue
        if not args.tout and p["date_limite"] and p["date_limite"] > AUJOURDHUI:
            continue  # pas encore échue
        echues.append(p)

    if not echues:
        print(f"[i] Aucune prédiction échue à vérifier (registre : {len(preds)} prédictions).")
        return

    print(f"[i] {len(echues)} prédiction(s) échue(s) à vérifier ...", flush=True)
    for p in echues:
        print(f"   • [{p['chaine']}] {p['texte'][:80]}", flush=True)
        if args.dry:
            continue
        texte = (
            f"Prédiction faite le {p['date_limite'] or '?'} (échue aujourd'hui {AUJOURDHUI}) :\n"
            f"{p['texte']}\n"
            f"Chaîne : {p['chaine']} — titre : {p['titre']} — {p['url']}"
        )
        try:
            verdict, provider = appeler_hub(texte)
        except Exception as e:
            print(f"   [X] vérification impossible : {e}", file=sys.stderr)
            continue
        v = "✅ VRAIE" if verdict.startswith("✅") else ("❌ FAUSSE" if verdict.startswith("❌") else "⚠️ NON VÉRIFIABLE")
        p["nouveau_statut"] = v
        print(f"      → {verdict} ({provider})", flush=True)

    if not args.dry:
        mettre_a_jour_registre(echues)
        print(f"[OK] Registre mis à jour : {REGISTRE_PATH}")


if __name__ == "__main__":
    main()
