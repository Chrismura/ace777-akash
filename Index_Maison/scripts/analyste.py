#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyste.py — L'ANALYSTE STRATÉGIQUE (brique 1, ACE777).

Réveillée par la vigie (alerte) ou par commande (--semaine / --tendance).
Injecte sa mémoire froide (STRATEGIE, MEMOIRE, dernière analyse, mission.json),
appelle le hub (tâche analyste.strategie), écrit ses analyses et produit
optionnellement un avis vocal (Vivienne, edge-tts).

Code initial : codeur du hub (code.ia). Corrections d'intégration (Buffy) :
- STRATEGIE.md : sections conservées (ne pas écraser les horizons non concernés)
- REGISTRE / MEMOIRE : APPEND uniquement (jamais d'écrasement)
- chemin mission.json corrigé (~/ace777-test-day1/Index_Maison/cockpit)
- erreurs hub : exit 1 sans écriture de fausses analyses

Usage :
    python3 analyste.py --alerte strategie/alarme.json [--speak]
    python3 analyste.py --semaine
    python3 analyste.py --tendance
"""

import os
import sys
import json
import argparse
import subprocess
import time
from datetime import datetime

# --- Configuration ---------------------------------------------------------
OUTPUT_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")
HISTORY_DIR = os.path.join(OUTPUT_DIR, "historique_analyses")
COCKPIT_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/cockpit")
HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "analyste.strategie"
MAX_TOKENS = 1500

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)


def read_file(path, default="(vide)"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default
    except OSError:
        return default


def append_file(path, content):
    """APPEND uniquement — ne jamais écraser (règle mémoire)."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def call_hub(prompt):
    try:
        data = json.dumps({
            "task": TASK,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": MAX_TOKENS,
        }).encode("utf-8")
        req = urllib_request(HUB_URL, data)
        return req
    except Exception as e:
        print(f"Erreur hub: {e}", file=sys.stderr)
        sys.exit(1)


def urllib_request(url, data):
    import urllib.request
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    return d["choices"][0]["message"]["content"]


# --- Construction du contexte (mémoire froide) -----------------------------
def build_context(alerte_path=None):
    ctx = {
        "strategie": read_file(os.path.join(OUTPUT_DIR, "STRATEGIE.md")),
        "memoire": read_file(os.path.join(OUTPUT_DIR, "MEMOIRE_ANALYSTE.md")),
        "derniere": read_file(os.path.join(OUTPUT_DIR, "derniere_analyse.md")),
        "mission": read_file(os.path.join(COCKPIT_DIR, "mission.json")),
        "alerte": read_file(alerte_path) if alerte_path else "(aucune alerte)",
    }

    # === mission.json ALLÉGÉ : le dump brut fait ~100 Ko (tokens gaspillés).
    # On ne garde que les clés utiles + les résumés des bots (sans les tableaux 'last').
    ctx_mission_texte = ctx["mission"]
    try:
        m_obj = json.loads(ctx["mission"])
        m_trim = {k: m_obj[k] for k in (
            "ts", "alert", "run", "sessionSince", "comboPnl", "comboArrow",
            "swarmCycle", "thrust", "portfolio", "thermo",
        ) if k in m_obj}
        for k in ("alpha", "beta", "hulk"):
            b = m_obj.get(k) or {}
            m_trim[k] = {kk: b.get(kk) for kk in (
                "file", "pnl", "fills", "skips", "pnlLifetime", "fillsLifetime",
                "trades", "positions", "bags",
            ) if kk in b}
        ctx_mission_texte = json.dumps(m_trim, ensure_ascii=False)
    except Exception:
        pass

    # === JOURNAL D'INTENTION (brique ADA) : section dédiée, jamais bloquante ===
    intention_texte = "(pas de journal d'intention)"
    try:
        mission_obj = json.loads(ctx["mission"])
        intention = mission_obj.get("intention") or {}
        if intention:
            lignes = []
            bots = intention.get("bots") or {}
            story = intention.get("story") or []
            for bot in ("alpha", "beta"):
                b = bots.get(bot) or {}
                if not b:
                    continue
                lignes.append(
                    "%s (%s) : %s fills, %s skips, pnl %+.2f $, %s revenge 1.5x, "
                    "long/short %s" % (
                        bot.upper(), b.get("surnom", "?"), b.get("fills", 0),
                        b.get("skips", 0), b.get("pnl", 0.0), b.get("revenge", 0),
                        b.get("direction", {}),
                    )
                )
            intention_texte = "\n".join(lignes) + "\nSTORY:\n" + "\n".join("- " + s for s in story)
    except Exception:
        intention_texte = "(pas de journal d'intention)"
    prompt = f"""ROLE : Tu es l'analyste stratégique senior de la maison ACE777,
experte des marchés et des machines de trading, avec 20 ans d'expérience.
CONTEXTE (uniquement ce qui suit, ne pas inventer hors contexte) :
[STRATEGIE.md]
{ctx["strategie"]}
[MEMOIRE_ANALYSTE.md]
{ctx["memoire"]}
[derniere_analyse.md]
{ctx["derniere"]}
[mission.json]
{ctx_mission_texte}
[INTENTION]
{intention_texte}
[ALERTE]
{ctx["alerte"]}
RÈGLES D'INTERPRÉTATION (indispensables) :
- Alpha = LE SNIPER : la patience est sa discipline. Des milliers de "skips" = il attend
  que le mur du carnet s'effondre. Le "mode revenge 1.5x" = il reprend l'avantage après une claque.
- Beta = L'ÉCLAIREUR : il sonde le marché pour renseigner Alpha. NE JAMAIS juger Beta sur
  son PnL — juger la qualité des infos qu'il transmet.
- Utilise la section [INTENTION] pour interpréter les chiffres de [mission.json].
RAISONNEMENT :
[UNDERSTAND] Reformule la situation en 1 phrase
[ANALYZE] Décompose : tendance, momentum, risque, contexte
[STRATEGIZE] 2-3 approches possibles
[EXECUTE] Verdict final
SORTIE EXACTE :
- Verdict : <une phrase claire>
- Confiance : <0-100%>
- Hypothèses clés : <2-3>
- Ce qui changerait la réponse : <1>
- Alternative si confiance < 80% : <1 phrase>
- Prédictions vérifiables : <0-2, uniquement si réelles> au format EXACT :
  [AAAA-MM-JJ] SYMBOLE COMPARATEUR CIBLE
  (ex : [2026-08-12] BTCUSDT >= 61000.0 — SYMBOLE : BTCUSDT|ETHUSDT,
   COMPARATEUR : >= | <=, CIBLE : nombre à 4 décimales max)
  Interdiction de sortir une prédiction sans symbole/comparateur/cible.
"""
    return prompt


# --- Sorties ---------------------------------------------------------------
def process_analysis(analysis, alerte_path=None, mode="alerte"):
    ts = datetime.utcnow().isoformat() + "Z"
    trigger = {"alerte": "alerte", "semaine": "commande-semaine",
               "tendance": "commande-tendance"}.get(mode, "commande")

    # 1. STRATEGIE.md : nettoyer les en-têtes empilés, mettre à jour la
    #    section de l'horizon, conserver les autres sections intactes.
    sp = os.path.join(OUTPUT_DIR, "STRATEGIE.md")
    old = read_file(sp, "")
    if old == "(vide)":
        old = ""
    section = {
        "alerte": "COURT TERME",
        "semaine": "SEMAINE",
        "tendance": "TENDANCE",
    }.get(mode, "COURT TERME")
    new_bloc = f"## {section} — {ts}\n\n{analysis.strip()}\n"

    # Découpe en sections existantes (## COURT TERME / SEMAINE / TENDANCE)
    import re
    sections = {}
    for m in re.finditer(r"(?m)^## (COURT TERME|SEMAINE|TENDANCE) — (.*)$", old):
        name = m.group(1)
        start = m.start()
        end = len(old)
        nxt = re.search(r"(?m)^## (COURT TERME|SEMAINE|TENDANCE) —", old[m.end():])
        if nxt:
            end = m.end() + nxt.start()
        sections[name] = old[start:end].rstrip()

    sections[section] = new_bloc  # remplace (ou ajoute) la section concernée

    corps = "\n\n".join(sections[name] for name in
                          ("COURT TERME", "SEMAINE", "TENDANCE")
                          if name in sections)
    with open(sp, "w", encoding="utf-8") as f:
        f.write(f"# STRATEGIE — {ts}\n\n{corps}\n")

    # 2. dernière analyse
    write_file(os.path.join(OUTPUT_DIR, "derniere_analyse.md"),
               f"# ANALYSE — {ts} ({trigger})\n\n{analysis}\n")

    # 3. archive
    af = os.path.join(HISTORY_DIR, f"ANALYSE_{ts.replace(':', '-')}.md")
    write_file(af, f"# ANALYSE — {ts} ({trigger})\n\n{analysis}\n")

    # 4. REGISTRE_PREDICTIONS.md : APPEND des prédictions vérifiables
    #    Format EXACT 6 champs (compatible scoreur_predictions.py) :
    #    - ⏳ EN ATTENTE | <ts_creation> | <ts_limite> | <SYMBOLE> | <COMP> | <CIBLE>
    registre_path = os.path.join(OUTPUT_DIR, "REGISTRE_PREDICTIONS.md")
    motif_pred = re.compile(
        r"^\[(\d{4}-\d{2}-\d{2})\] (BTCUSDT|ETHUSDT) (>=|<=) ([\d.]+)$")
    for line in analysis.split("\n"):
        m = motif_pred.match(line.strip())
        if not m:
            continue
        date_str, symbole, comparateur, cible = m.groups()
        ts_limite = f"{date_str}T00:00:00Z"
        if not os.path.exists(registre_path):
            with open(registre_path, "w", encoding="utf-8") as f:
                f.write("# Registre des prédictions (mécanique)\n\n")
        append_file(registre_path,
                    f"- ⏳ EN ATTENTE | {ts} | {ts_limite} | {symbole} | "
                    f"{comparateur} | {cible}\n")

    # 5. MEMOIRE_ANALYSTE.md : APPEND du résumé
    verdict = _extract(analysis, "Verdict")
    conf = _extract(analysis, "Confiance")
    append_file(os.path.join(OUTPUT_DIR, "MEMOIRE_ANALYSTE.md"),
                f"- {ts} | {trigger} | {verdict} | conf={conf}\n")

    return verdict


def _extract(analysis, key):
    for line in analysis.split("\n"):
        if line.strip().startswith(f"- {key} :") or \
           line.strip().startswith(f"- {key}:"):
            return line.split(":", 1)[1].strip()
    return "?"


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# --- Voix (Vivienne) -------------------------------------------------------
def speak(text):
    try:
        subprocess.run(["python3", "-m", "edge_tts", "--voice",
                        "fr-FR-VivienneMultilingualNeural", "--rate=-15%",
                        "--text", text, "--write-media", "/tmp/voix.mp3"],
                       check=True, timeout=60)
        subprocess.run(["killall", "say"], check=False, capture_output=True)  # une seule piste (règle maison)
        subprocess.run(["killall", "afplay"], check=False, capture_output=True)
        time.sleep(0.05)
        subprocess.run(["afplay", "/tmp/voix.mp3"], check=True, timeout=120)
    except Exception as e:
        print(f"Erreur voix: {e}", file=sys.stderr)


# --- Main ------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alerte", help="Chemin du fichier d'alerte")
    parser.add_argument("--semaine", action="store_true")
    parser.add_argument("--tendance", action="store_true")
    parser.add_argument("--speak", action="store_true")
    args = parser.parse_args()

    if args.semaine:
        mode = "semaine"
    elif args.tendance:
        mode = "tendance"
    elif args.alerte:
        mode = "alerte"
    else:
        print("Erreur: spécifiez --alerte, --semaine ou --tendance",
              file=sys.stderr)
        sys.exit(1)

    prompt = build_context(args.alerte)
    analysis = call_hub(prompt)
    if not analysis or not analysis.strip():
        print("Erreur: réponse hub vide — pas d'écriture de fausse analyse",
              file=sys.stderr)
        sys.exit(1)

    verdict = process_analysis(analysis, args.alerte, mode)
    print(f"✅ Analyse écrite — verdict : {verdict}")

    # La famille (trio) arbitre en certaines occasions — jamais bloquant
    if mode == "alerte":
        try:
            import famille_session
            famille_session.consulter()
        except Exception:
            pass

    if args.speak:
        speak(verdict)


if __name__ == "__main__":
    main()
