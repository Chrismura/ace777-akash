#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cortana_analyse.py — analyse LIVE d'un indice par Cortana (master analyste)
=============================================================================
Chantier 3 (06/08/2026) — spec validée Christophe :
  * Chaque bulle d'indice du cockpit aura un bouton Cortana -> ce script.
  * Il prend un indice (ex: funding), assemble les FAITS live + tendances
    24h/semaine depuis l'historique, et demande l'analyse à Gemini via le hub
    (routage task=cortana.analyse -> GEMINI prioritaire, repli Qwen local).
  * L'analyse est ENREGISTRÉE dans ~/ace777-test-day1/Index_Maison/analyses/
    (exigence Christophe : comparer plus tard avec le marché réel -> score de
    justesse de l'analyste).

Usage :
  python3 cortana_analyse.py funding            # analyse de l'indice funding
  python3 cortana_analyse.py funding --speak    # + lecture vocale (Vivienne)
  python3 cortana_analyse.py --list             # liste des indices dispo

Le prompt système vit dans le vault : PROMPT_MASTER_ANALYSTE.md.
Ce script ne passe JAMAIS d'ordre — lecture et opinion uniquement.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
THERMO_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo")
LIVE_JSON = os.path.join(THERMO_DIR, "live.json")
HISTORY = os.path.join(THERMO_DIR, "history.jsonl")
ANALYSES_DIR = os.path.join(THERMO_DIR, "analyses")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

# Lexique : id live.json -> (nom lisible, unité)
LEXIQUE = {
    "funding": ("Taux de financement", "taux par période de 8h"),
    "fundingAvg30": ("Funding moyenne 30j", "taux"),
    "oi": ("Open interest", "BTC (contrats)"),
    "longShort": ("Ratio long/short", "ratio"),
    "takerRatio": ("Ratio taker", "ratio"),
    "topTraderLS": ("Ratio L/S top traders", "ratio"),
    "fearGreed": ("Fear & Greed", "/100"),
    "marketCapUsd": ("Capitalisation totale", "USD"),
    "btcDominance": ("Dominance BTC", "%"),
    "altSeason": ("Saison altcoins", "label"),
    "altSeasonScore": ("Score saison altcoins", "/100"),
    "liq24Usd": ("Liquidations 24h", "USD"),
    "chg24": ("Variation prix 24h", "%"),
    "chg1h": ("Variation prix 1h", "%"),
    "chg4h": ("Variation prix 4h", "%"),
    "panierDownPct": ("Panier en baisse", "%"),
    "whaleUsd": ("Flux baleines", "USD"),
    "whaleN": ("Baleines (≥50M$)", "compte"),
    "volQuote": ("Volume 24h", "USD"),
    "score": ("Score composite", "/100"),
    "climate": ("Climat", "label"),
    "mark": ("Prix mark BTC", "USD"),
}

# Indices toujours fournis comme contexte de mise en relation
CONTEXT_KEYS = ["mark", "chg24", "chg1h", "chg4h", "funding", "fundingAvg30",
                "oi", "longShort", "takerRatio", "topTraderLS", "fearGreed",
                "marketCapUsd", "btcDominance", "altSeason", "altSeasonScore",
                "panierDownPct", "whaleUsd", "whaleN", "volQuote", "score", "climate"]


def load_system_prompt():
    """Lit le prompt master analyste depuis le vault (canon)."""
    # NB : l'espace ace777-test-day1 est accessible par launchd (TCC) ;
    # le vault (Documents) ne l'est PAS depuis le bridge -> copie miroir ici.
    candidates = [
        os.path.join(SCRIPTS, "prompts", "PROMPT_MASTER_ANALYSTE.md"),
        os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md"),
    ]
    for p in candidates:
        if os.path.exists(p):
            s = open(p).read()
            # extraire la section SYSTEM PROMPT
            start = s.find("## SYSTEM PROMPT")
            end = s.find("---", start + 20)
            if start != -1 and end != -1:
                body = s[s.find("\n\n", start) + 2:end].strip()
                # enlever la ligne de titre du bloc
                return body
            return s
    # fallback : prompt minimal
    return ("Tu es Cortana, master analyste crypto du cockpit ACE777. "
            "Analyse l'indice reçu : faits, interpretation, mise en relation, "
            "pattern, opinion. 8-12 phrases, chiffres exacts, vulgarise.")


def load_live():
    if not os.path.exists(LIVE_JSON):
        return {}
    try:
        return json.load(open(LIVE_JSON))
    except Exception:
        return {}


def load_history():
    """Charge history.jsonl -> liste de dicts (plus ancien au plus récent)."""
    if not os.path.exists(HISTORY):
        return []
    out = []
    try:
        with open(HISTORY) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
    except Exception:
        return []
    return out


def fmt_val(v):
    if v is None:
        return "INDISPONIBLE (null)"
    if isinstance(v, float):
        if abs(v) < 1e-4 and v != 0:
            return f"{v:.2e}"
        return f"{v:,.4f}" if abs(v) < 10 else f"{v:,.2f}"
    return str(v)


def trend_pct(history, key, hours):
    """Tendance en % sur les N dernières heures à partir de history.jsonl."""
    if not history or key not in history[-1]:
        return None
    now = history[-1][key]
    if not isinstance(now, (int, float)) or now == 0:
        return None
    target_ts = history[-1].get("tsUnix", 0) - hours * 3600
    past = None
    for row in history:
        if row.get("tsUnix", 0) <= target_ts and row.get(key) is not None:
            past = row[key]
    if past is None or not isinstance(past, (int, float)) or past == 0:
        return None
    return (now - past) / abs(past) * 100.0


def build_facts(indice):
    """Assemble le JSON de faits pour l'analyste."""
    live = load_live()
    history = load_history()

    name, unit = LEXIQUE.get(indice, (indice, ""))
    facts = {
        "indice_demande": {
            "id": indice,
            "nom": name,
            "unite": unit,
            "valeur_actuelle": fmt_val(live.get(indice)),
        },
        "tendances": {
            "tendance_24h_pct": trend_pct(history, indice, 24),
            "tendance_semaine_pct": trend_pct(history, indice, 24 * 7),
        },
        "autres_indices": {},
        "historique_recent": [],
        "serie_prix_recente": [],
    }

    for k in CONTEXT_KEYS:
        if k in live and k != indice:
            facts["autres_indices"][k] = fmt_val(live.get(k))

    # historique récent de l'indice (derniers 12 points horaires)
    for row in history[-12:]:
        if indice in row:
            facts["historique_recent"].append({
                "ts": row.get("ts", "?"),
                "valeur": fmt_val(row.get(indice)),
            })

    # série de prix (closes mark) : derniers 12 points pour lecture ondulatoire
    for row in history[-12:]:
        if "mark" in row:
            facts["serie_prix_recente"].append({
                "ts": row.get("ts", "?"),
                "mark": row.get("mark"),
            })

    # valeurs brutes (non formatées) pour la comparaison ultérieure
    raw = {k: live.get(k) for k in CONTEXT_KEYS + [indice] if k in live}
    raw["ts"] = live.get("ts")
    raw["tendances"] = {
        "tendance_24h_pct": trend_pct(history, indice, 24),
        "tendance_semaine_pct": trend_pct(history, indice, 24 * 7),
    }
    return facts, raw


def call_hub(facts, indice):
    system = load_system_prompt()
    payload = {
        "task": "cortana.analyse",  # routage : Gemini prioritaire, repli Qwen
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": (
                f"Analyse l'indice suivant : {indice}.\n\n"
                f"Données :\n{json.dumps(facts, ensure_ascii=False, indent=1)}\n\n"
                "Donne ton analyse selon ta structure (FAITS, LECTURE PHYSIQUE, "
                "INTERPRÉTATION, MISE EN RELATION, PATTERN, OPINION)."
            )},
        ],
        "temperature": 0.4,
        "max_tokens": 700,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.load(resp)
    content = data["choices"][0]["message"]["content"]
    return content, data.get("provider", "?")


def journalise(indice, facts, facts_bruts, content, provider):
    """Enregistre l'analyse (exigence Christophe : comparer avec le marché)."""
    os.makedirs(ANALYSES_DIR, exist_ok=True)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(ANALYSES_DIR, f"{day}.jsonl")
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "indice": indice,
        "provider": provider,
        "faits": facts,           # valeurs formatées (lisibles)
        "faits_bruts": facts_bruts,  # valeurs brutes (pour comparer avec le marché réel)
        "analyse": content,
    }
    with open(path, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return path


def speak_text(text, voice="fr-FR-VivienneMultilingualNeural", rate="-15%"):
    """Voix Vivienne via python3 -m edge_tts (même mécanisme que cortana_voice)."""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        path = f.name
    cmd = [
        "python3", "-m", "edge_tts",
        "--voice", voice,
        f"--rate={rate}",
        "--text", text,
        "--write-media", path,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    if proc.returncode != 0 or not os.path.exists(path) or os.path.getsize(path) < 100:
        print("  ✘ generation voix echouee", file=sys.stderr)
        if os.path.exists(path):
            os.unlink(path)
        return 1
    subprocess.run(["afplay", path], check=False, timeout=240)
    os.unlink(path)
    return 0


def main():
    ap = argparse.ArgumentParser(description="Analyse live d'un indice par Cortana (master analyste)")
    ap.add_argument("indice", nargs="?", default=None, help="id de l'indice (ex: funding, oi, fearGreed)")
    ap.add_argument("--speak", action="store_true", help="lire l'analyse à voix haute (Vivienne)")
    ap.add_argument("--list", action="store_true", help="lister les indices disponibles")
    a = ap.parse_args()

    if a.list:
        for k, (name, unit) in LEXIQUE.items():
            print(f"  {k:16} {name} ({unit})")
        return 0

    if not a.indice:
        print("Usage : python3 cortana_analyse.py <indice> [--speak]  (ou --list)")
        return 2

    indice = a.indice
    if indice not in LEXIQUE:
        print(f"Indice '{indice}' inconnu. Disponibles :")
        for k in LEXIQUE:
            print(f"  {k}")
        return 2

    facts, facts_bruts = build_facts(indice)
    print(f"[analyse] {LEXIQUE[indice][0]} — envoi au hub (cortana.analyse)...", file=sys.stderr)

    try:
        content, provider = call_hub(facts, indice)
    except Exception as e:
        print(f"✘ hub injoignable ou réponse inattendue : {e}", file=sys.stderr)
        print("Repli : voici les faits bruts (pas d'analyse IA disponible) :")
        print(json.dumps(facts, ensure_ascii=False, indent=1))
        return 1

    journal = journalise(indice, facts, facts_bruts, content, provider)
    print(f"[provider: {provider}]", file=sys.stderr)
    print(f"[journal: {journal}]", file=sys.stderr)

    if a.speak:
        print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
        return speak_text(content)
    print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
