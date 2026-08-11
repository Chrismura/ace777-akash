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
import threading

import barge_in  # micro : coupe la parole si on parle (natif, ffmpeg)
import oral_fr  # nombres -> toutes lettres (voix propre, pas de « neuf neuf »)
import tempfile
import urllib.request

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
MAISON = os.path.expanduser("~/ace777-test-day1/Index_Maison")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

SYSTEM = (
    "Tu es Cortana, l'assistante vocale de la maison ACE777. "
    "Réponds TOUJOURS en français, quel que soit le contexte. "
    "CE QU'EST LA MAISON : ACE777 est un système de trading crypto qui orchestre "
    "des moteurs automatiques — ALPHA (moteur haute fréquence, très sélectif), "
    "BETA (moteur secondaire) et HULK (gestionnaire de portefeuille à positions "
    "longues). Un RADAR de sécurité (vigie) peut BLOQUER les moteurs "
    "(radar_block) : c'est une PROTECTION, pas une panne. "
    "RÈGLES DE LECTURE OBLIGATOIRES : "
    "1) Tiens compte de TOUTES les positions et de leur ÉTAT : active, à l'arrêt "
    "ou bloquée par le radar. Ne dis JAMAIS « rien ne se passe » ou « tout est "
    "calme » sans expliquer POURQUOI (ex. : moteur bloqué par le radar, "
    "portefeuille Hulk sans position ouverte). "
    "2) Si un moteur est bloqué ou à l'arrêt, signale-le EXPLICITEMENT avec la "
    "cause (skips radar_block, zéro position Hulk, etc.). "
    "3) Rédige ensuite un brief vocal de 3-4 phrases naturelles, vivantes et "
    "concises, prêt à être lu à voix haute. Garde les chiffres clés (PnL, "
    "positions, état des moteurs) mais évite les listes techniques. "
    "CHIFFRES À L'ORAL : quand un nombre a des décimales UTILES, lis-les "
    "CORRECTEMENT (ex. -8,5387 → « moins huit virgule cinq quatre » ; 0,7463 → "
    "« zéro virgule sept cinq »). Ne compresse en « quasi nul » que les valeurs "
    "vraiment infimes (funding < 0,0001). Ne lis JAMAIS une longue suite de "
    "zéros (ex. 0,000087 → « quasi nul »). 3486 → « trois mille quatre cent "
    "quatre-vingt-six ». "
    "Pas de préambule, pas de markdown, pas d'emoji."
)


def load_json(path, default):
    """Lecture sûre d'un JSON — jamais de panne si absent ou corrompu."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def speak_text(text, voice=None, rate=None):
    voice = voice or os.environ.get("EDGE_TTS_VOICE", "fr-FR-VivienneMultilingualNeural")
    rate = rate or os.environ.get("EDGE_TTS_RATE", "-25%")  # style Cortana : plus calme
    """Voix Vivienne via python3 -m edge_tts (meme mecanisme que cortana_voice)."""
    if not text or not text.strip():
        return 1
    text = oral_fr.oraliser(text)  # 99,99 -> « quatre-vingt-dix-neuf virgule quatre-vingt-dix-neuf »
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        path = f.name
    if barge_in.activ():
        barge_in.preparer()  # calibration ambiant EN SILENCE, pendant la generation
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
    # BARGE-IN : touche (clavier) OU micro (barge_in.py) coupent la parole
    player = subprocess.Popen(["afplay", path])
    if barge_in.activ():
        threading.Thread(target=barge_in.surveiller, args=(player,), daemon=True).start()
    _couper_si_touche(player)
    try:
        player.wait(timeout=180)
    except subprocess.TimeoutExpired:
        player.kill()
    try:
        os.unlink(path)
    except Exception:
        pass
    return 0


def _couper_si_touche(player):
    """Surveille le clavier : tout appui = coupe la voix (barge-in terminal)."""
    import select
    import termios
    import tty
    fd = sys.stdin.fileno()
    try:
        old = termios.tcgetattr(fd)
    except Exception:
        return
    try:
        tty.setcbreak(fd)
        while player.poll() is None:
            r, _, _ = select.select([sys.stdin], [], [], 0.15)
            if r:
                sys.stdin.read(1)
                player.terminate()
                break
    except Exception:
        pass
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        except Exception:
            pass


def rule_brief():
    """Repli : brief brut par règles si les données réelles sont absentes."""
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "cortana_thermo.py"), "horaire"],
        capture_output=True, text=True, timeout=180,
    )
    return (r.stdout or "").strip() or "(brief horaire indisponible)"


def _vocal_funding(v):
    """Tout petit nombre -> 'quasi nul' ; sinon valeur arrondie lisible à l'oral."""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return v
    if abs(f) < 1e-4:
        return "quasi nul"
    return round(f, 4)


def etat_moteur(moteur):
    """État explicite d'un moteur : actif / très prudent / bloqué par le radar."""
    skips = (moteur or {}).get("skips") or 0
    fills = (moteur or {}).get("fills") or 0
    if fills == 0 and skips > 200:
        return "BLOQUE par le radar (radar_block) — %d skips, 0 fill" % skips
    if skips > 500:
        return "tres prudent — %d skips pour %d fills" % (skips, fills)
    return "actif"


def collect_data():
    """Rassemble les données RÉELLES marché + cockpit + système (JSON compact).
    Inclut TOUTES les positions et leur ÉTAT (actif, à l'arrêt, bloqué radar)
    pour que Cortana ne rate jamais un moteur à l'arrêt ou une position ouverte."""
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
            "funding_vocal": _vocal_funding(live.get("funding")),
            "fundingAvg30": live.get("fundingAvg30"),
            "openInterest": live.get("oi"),
            "longShort": live.get("longShort"),
            "volQuote": live.get("volQuote"),
        }
    if mission:
        alpha = mission.get("alpha") or {}
        beta = mission.get("beta") or {}
        hulk = mission.get("hulk") or {}
        hulk_pos = hulk.get("positions") or []
        data["cockpit"] = {
            "run": mission.get("run"),
            "sessionSince": mission.get("sessionSince"),
            "swarmCycle": mission.get("swarmCycle"),
            "alert": mission.get("alert"),
            "portfolio": mission.get("portfolio"),
            "thermo": mission.get("thermo"),
            # --- ALPHA : positions + état complet (pas seulement le PnL) ---
            "alpha": {
                "pnl": alpha.get("pnl"),
                "fills": alpha.get("fills"),
                "skips": alpha.get("skips"),
                "etat": etat_moteur(alpha),
            },
            # --- BETA ---
            "beta": {
                "pnl": beta.get("pnl"),
                "fills": beta.get("fills"),
                "skips": beta.get("skips"),
                "etat": etat_moteur(beta),
            },
            # --- HULK : portefeuille (positions longues, même à l'arrêt) ---
            "hulk": {
                "pnl": hulk.get("pnl"),
                "trades": hulk.get("trades"),
                "nb_positions": len(hulk_pos),
                "positions": hulk_pos[:5],
                "bags": hulk.get("bags"),
                "notional": hulk.get("notional"),
                "base": hulk.get("base"),
                "etat": ("AUCUNE position (a l'arret)" if not hulk_pos
                          else "%d position(s) ouverte(s)" % len(hulk_pos)),
            },
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
                + json.dumps(donnees, ensure_ascii=False)[:9000]
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
