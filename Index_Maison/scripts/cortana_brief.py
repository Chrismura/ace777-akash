#!/usr/bin/env python3
"""cortana_brief.py — briefs vocaux RÉELS générés par IA du hub (Prise IA)
========================================================================
Le brief est construit à partir des DONNÉES RÉELLES de la maison :
  - live.json       (marché BTC : mark, funding, OI, long/short, chg24)
  - mission.json    (cockpit : portefeuille ACE/Beta/Hulk, thermo, run)
  - state.json      (système : services launchd, hub, RAM, feeds)
Puis une IA du hub (task=cortana.brief -> Gemini, repli NVIDIA ; Qwen local
uniquement en dernier recours offline) rédige un brief vocal EN FRANÇAIS.

Usage :
  python3 cortana_brief.py                  # brief réel (IA du hub, sortie JSON)
  python3 cortana_brief.py --speak          # + lecture vocale Vivienne
  python3 cortana_brief.py --model gemini   # force Gemini
  python3 cortana_brief.py --text "..."     # enrichir un texte arbitraire

Sortie stdout (JSON) :
  {"resume": "texte vocal...", "donnees": {...}, "provider": "...", "ts": "..."}
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import tempfile
import urllib.request

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
MAISON = os.path.expanduser("~/ace777-test-day1/Index_Maison")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

SYSTEM = (
    "Tu es Cortana, l'assistante vocale de la maison ACE777. "
    "Réponds TOUJOURS en français, quel que soit le contexte. "
    "À partir des données réelles fournies (marché + cockpit + système), "
    "rédige un brief vocal de 3-4 phrases naturelles, vivantes et concises, "
    "prêt à être lu à voix haute. Garde les chiffres clés mais évite les listes "
    "techniques. Pas de préambule, pas de markdown, pas d'emoji."
)


def load_json(path, default):
    """Lecture sûre d'un JSON — jamais de panne si absent ou corrompu."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def speak_text(text, voice="fr-FR-VivienneMultilingualNeural", rate="-15%"):
    """Voix Vivienne via python3 -m edge_tts (meme mecanisme que cortana_voice)."""
    if not text or not text.strip():
        return 1
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        path = f.name
    cmd = [
        "python3", "-m", "edge_tts",
        "--voice", voice,
        f"--rate={rate}",
        "--text", text,
        "--write-media", path,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=90, check=False)
    if proc.returncode != 0 or not os.path.exists(path) or os.path.getsize(path) < 100:
        print("  ✘ generation voix echouee", file=sys.stderr)
        if os.path.exists(path):
            os.unlink(path)
        return 1
    subprocess.run(["afplay", path], check=False, timeout=180)
    os.unlink(path)
    return 0


def rule_brief():
    """Repli : brief brut par règles si les données réelles sont absentes."""
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "cortana_thermo.py"), "horaire"],
        capture_output=True, text=True, timeout=180,
    )
    return (r.stdout or "").strip() or "(brief horaire indisponible)"


def collect_data():
    """Rassemble les données RÉELLES marché + cockpit + système (JSON compact)."""
    mission = load_json(os.path.join(MAISON, "cockpit", "mission.json"), {})
    live = load_json(os.path.join(MAISON, "thermo", "live.json"), {})
    state = load_json(os.path.join(MAISON, "system", "state.json"), {})
    data = {}
    if live:
        data["marche_btc"] = {
            "mark": live.get("mark"),
            "chg24": live.get("chg24"),
            "chg1h": live.get("chg1h"),
            "chg4h": live.get("chg4h"),
            "funding": live.get("funding"),
            "fundingAvg30": live.get("fundingAvg30"),
            "openInterest": live.get("oi"),
            "longShort": live.get("longShort"),
            "volQuote": live.get("volQuote"),
        }
    if mission:
        data["cockpit"] = {
            "run": mission.get("run"),
            "sessionSince": mission.get("sessionSince"),
            "swarmCycle": mission.get("swarmCycle"),
            "alert": mission.get("alert"),
            "portfolio": mission.get("portfolio"),
            "thermo": mission.get("thermo"),
            "alpha_pnl": (mission.get("alpha") or {}).get("pnl"),
            "beta_pnl": (mission.get("beta") or {}).get("pnl"),
            "hulk_pnl": (mission.get("hulk") or {}).get("pnl"),
        }
    if state:
        data["systeme"] = {
            "status": state.get("status"),
            "services": state.get("services"),
            "hub": state.get("hub"),
        }
    return data


def call_hub(prompt_user, force_gemini=False):
    payload = {
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt_user},
        ],
        "temperature": 0.5,
        "max_tokens": 400,
    }
    if force_gemini:
        payload["model"] = "gemini"
    else:
        payload["task"] = "cortana.brief"  # routage : Gemini -> NVIDIA -> (offline) Qwen local
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=None) as resp:
        data = json.load(resp)
    content = data["choices"][0]["message"]["content"]
    return content, data.get("provider", "?")


def main():
    ap = argparse.ArgumentParser(description="Brief Cortana réel (IA du hub, JSON)")
    ap.add_argument("--model", choices=["auto", "gemini"], default="auto",
                    help="auto = routage du hub (Gemini->NVIDIA) ; gemini = force Gemini")
    ap.add_argument("--text", default=None, help="texte arbitraire à enrichir (repli)")
    ap.add_argument("--speak", action="store_true", help="lire le resume a voix haute (Vivienne)")
    a = ap.parse_args()

    if a.text:
        prompt_user = a.text
        donnees = {}
    else:
        donnees = collect_data()
        if donnees:
            prompt_user = (
                "Voici les données réelles actuelles de la maison, au format JSON :\n"
                + json.dumps(donnees, ensure_ascii=False)[:6000]
            )
        else:
            prompt_user = rule_brief()

    try:
        content, provider = call_hub(prompt_user, force_gemini=(a.model == "gemini"))
    except Exception as e:
        # Jamais de panne sèche : repli voix-règles + JSON d'erreur.
        print(json.dumps({"resume": rule_brief(), "donnees": donnees,
                          "provider": "repli-regles", "error": str(e)[:200]},
                         ensure_ascii=False), file=sys.stderr)
        return 1

    print("[provider: %s]" % provider, file=sys.stderr)
    # donnees compactees : meme projection que le prompt (sortie legerement)
    def _compact(d):
        return d
    out = {"resume": content.strip(), "donnees": _compact(donnees), "provider": provider,
           "ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds")}
    if a.speak:
        print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
        rc = speak_text(content)
        print(json.dumps(out, ensure_ascii=False))
        return rc
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
