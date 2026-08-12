#!/usr/bin/env python3
"""
Pont local cockpit ↔ Cortana + feed mission (127.0.0.1 seulement).
  python3 cortana_cockpit_bridge.py
  GET  /status /mission /alerts /refresh /preflight
  POST /mute /unmute /speak /refresh /panic

Pas d'ouverture de trade. Sortie urgence = /panic mode A|B.
CORS ouvert pour file:// cockpit.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import threading
from datetime import datetime, timezone

import barge_in  # micro : coupe la parole si on parle (natif, ffmpeg)
import oral_fr  # nombres -> toutes lettres (voix propre, pas de « neuf neuf »)
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, quote

ROOT = Path("/Users/christophe/ace777-test-day1")
SCRIPTS = ROOT / "Index_Maison" / "scripts"
MISSION_JSON = ROOT / "Index_Maison" / "cockpit" / "mission.json"
RUNS = ROOT / "runs"
HULK = ROOT / "hulk-mexc"
PANIC_LOG = ROOT / "Index_Maison" / "cockpit" / "panic.log"
PORT = 17777

# --- Voix INTERRUPTIBLE (barge-in) : le process afplay en cours, s'il existe ---
_VOICE_PROC = None
_VOICE_LOCK = threading.Lock()

# E3 (SPEC V2.1, reserve famille P4) : verif version coeur Rust — NON FATALE.
EXPECTED_RUST_VERSION = "2.1.0"
RUST_CORE_DIR = Path("/Users/christophe/crypto-voice-assistant-core")


def _ace_link() -> dict:
    """LIVE frais = ACE en marche · STALE = log froid · OFF = pas de LIVE."""
    import time

    lives = sorted(RUNS.glob("*_LIVE_COLOR.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not lives:
        return {"state": "OFF", "label": "OFF", "ageSec": None, "run": None, "live": None}
    live = lives[0]
    age = max(0, int(time.time() - live.stat().st_mtime))
    run = live.name.replace("_LIVE_COLOR.log", "")
    if age <= 45:
        state, label = "ON", "ON"
    elif age <= 180:
        state, label = "STALE", "STALE"
    else:
        state, label = "OFF", "OFF"
    return {"state": state, "label": label, "ageSec": age, "run": run, "live": live.name}


def _check_rust_version() -> None:
    """E3 (SPEC V2.1, reserve P4) : verifie la version du coeur Rust
    (hors perimetre setup, backup uniquement). Warning si version != attendue,
    error si VERSION manquant. NON FATAL : ne plante jamais le script."""
    version_file = RUST_CORE_DIR / "VERSION"
    try:
        if not version_file.exists():
            print(f"[ERROR] Fichier VERSION manquant : {version_file}",
                  file=sys.stderr)
            return
        with open(version_file, "r", encoding="utf-8") as f:
            rust_version = f.read().strip()
        if rust_version != EXPECTED_RUST_VERSION:
            print(f"[WARNING] Version Rust inattendue : {rust_version} "
                  f"(attendu : {EXPECTED_RUST_VERSION})", file=sys.stderr)
        else:
            print(f"[INFO] Version Rust OK : {rust_version}")
    except Exception as e:
        print(f"[ERROR] Erreur verification Rust : {e}", file=sys.stderr)


def _net_link() -> dict:
    """Ping public Binance futures — internet trading path."""
    import urllib.request

    url = "https://fapi.binance.com/fapi/v1/ping"
    t0 = __import__("time").time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ace777-cockpit-link/1"})
        with urllib.request.urlopen(req, timeout=2.0) as r:
            r.read(32)
        ms = int((__import__("time").time() - t0) * 1000)
        if ms < 400:
            return {"state": "OK", "label": "OK", "ms": ms}
        if ms < 1200:
            return {"state": "SLOW", "label": "SLOW", "ms": ms}
        return {"state": "SLOW", "label": "SLOW", "ms": ms}
    except Exception as e:
        return {"state": "DOWN", "label": "DOWN", "ms": None, "err": str(e)[:80]}


def run_py(*args: str, timeout: int = 180) -> str:
    cmd = [sys.executable, *[str(a) if isinstance(a, Path) else a for a in args]]
    env = os.environ.copy()
    env["CORTANA_TTS"] = "edge"
    env.setdefault("EDGE_TTS_RATE", "-18%")
    env.setdefault("EDGE_TTS_VOICE", "fr-FR-VivienneMultilingualNeural")
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), timeout=timeout, env=env)
    out = (p.stdout or "") + (p.stderr or "")
    return out.strip() or f"rc={p.returncode}"


def _run_rc(*args: str, timeout: int = 180) -> tuple[int, str]:
    """Comme run_py mais renvoie aussi le code de retour (pour le repli)."""
    cmd = [sys.executable, *[str(a) if isinstance(a, Path) else a for a in args]]
    env = os.environ.copy()
    env["CORTANA_TTS"] = "edge"
    env.setdefault("EDGE_TTS_RATE", "-18%")
    env.setdefault("EDGE_TTS_VOICE", "fr-FR-VivienneMultilingualNeural")
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), timeout=timeout, env=env)
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode, out.strip() or f"rc={p.returncode}"


def do_mute() -> str:
    return run_py(SCRIPTS / "cortana_mute.py", "on", timeout=30)


def do_unmute() -> str:
    return run_py(SCRIPTS / "cortana_mute.py", "off", timeout=30)


def do_speak() -> str:
    run_py(SCRIPTS / "cortana_mute.py", "off", timeout=30)
    # Depuis 06/08/2026 : brief ENRICHI par IA via hub Prise IA
    # (routage task=cortana.brief -> Gemini prefere, quota 20/j, repli Qwen).
    # Repli automatique sur la voix-regles historique : jamais de silence.
    rc, out = _run_rc(SCRIPTS / "cortana_brief.py", "--speak", timeout=300)
    if rc == 0 and "Traceback" not in out and "\u2718" not in out and "echouee" not in out:
        return out
    print(f"[speak] brief IA indisponible (rc={rc}) -> repli voix-regles", flush=True)
    return run_py(SCRIPTS / "cortana_thermo.py", "resume", "--say", timeout=180)


def do_analyse(indice: str) -> dict:
    """Master analyste : analyse LIVE d'un indice via cortana_analyse.py.
    Renvoie le texte (stdout) et le provider (stderr) — synchrone pour que
    le cockpit puisse afficher l'analyse."""
    cmd = [sys.executable, str(SCRIPTS / "cortana_analyse.py"), indice]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), timeout=300)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "analyse en timeout (>300s)"}
    except Exception as e:
        return {"ok": False, "error": f"erreur lancement: {e}"}
    texte = (p.stdout or "").strip()
    provider = ""
    for line in (p.stderr or "").splitlines():
        if line.startswith("[provider"):
            provider = line.strip()
    if p.returncode != 0 or not texte:
        err = (p.stderr or "analyse échouée").strip().splitlines()
        return {"ok": False, "error": (err[-1] if err else "analyse échouée")[:300], "provider": provider}
    if p.returncode == 0 and texte:
        # spec C4 : voix Vivienne en arriere-plan (n'attend pas la fin de lecture)
        threading.Thread(target=_speak_texte, args=(texte,), daemon=True).start()
    return {"ok": True, "texte": texte, "provider": provider}


def _appel_hub(task: str, prompt_role: str, sujet: str, result_list: list, idx: int) -> None:
    """Appel hub pour un membre de la famille (thread). timeout=None (règle maison)."""
    import urllib.request
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": prompt_role},
            {"role": "user", "content": sujet},
        ],
        "temperature": 0.3,
        "max_tokens": 500,
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            "http://127.0.0.1:11435/v1/chat/completions",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=None) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            result_list[idx] = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception:
        result_list[idx] = None


def do_chat(message: str) -> dict:
    """Chat cockpit -> hub (task=mission = deepseek-v4-flash = Buffy, rotation hub).
    Renvoie le texte (écrit, affiché dans le cockpit) et lance la lecture vocale
    Vivienne en arrière-plan (thread, comme do_analyse).
    Commande spéciale : « demande l'avis de la famille sur X » -> trio Gemini+DeepSeek+Juge."""
    import urllib.request

    msg = (message or "").strip()
    if not msg:
        return {"ok": False, "error": "message vide"}
    if len(msg) > 2000:
        return {"ok": False, "error": "message trop long (max 2000 caractères)"}

    # === CONSULTATION FAMILLE (avant vision) : trio Gemini + DeepSeek + Juge ===
    m_low = msg.lower().lstrip()
    trig_famille = (
        "demande l'avis de la famille", "avis de la famille", "consulte la famille",
        "interroge la famille", "la famille sur", "demande au juge", "avis du juge",
        "consulte le juge", "le juge sur",
    )
    declenche_famille = False
    for t in trig_famille:
        if m_low == t or m_low.startswith(t + " ") or m_low.startswith(t):
            declenche_famille = True
            break
    if declenche_famille:
        sujet = msg
        for t in trig_famille:
            sujet = sujet.replace(t, " ", 1)
        sujet = sujet.strip()
        for k in ("à propos", "a propos", "sur", "de", "stp", "s'il te plaît",
                  "sil te plait", "à voix", "a voix", "parle", "vocale"):
            sujet = sujet.replace(k, " ").replace("  ", " ").strip()
        sujet = sujet.strip(" ,;:.")
        if not sujet:
            sujet = "(avis général — sujet non précisé)"
        roles = [
            ("audit.protocol",
             "Tu es Gemini, analyste senior de la maison ACE777. Donne un avis CONCIS "
             "(2-3 phrases max) : les risques, les angles morts, ce qu'on pourrait rater. "
             "Important : notre système tourne sur macOS (pas Windows). Réponds en français."),
            ("mission",
             "Tu es DeepSeek, expert technique de la maison ACE777. Donne un avis CONCIS "
             "(2-3 phrases max) : la cohérence du setup, ce qui peut casser, la faisabilité. "
             "Important : notre système tourne sur macOS (pas Windows). Réponds en français."),
            ("signets.juge",
             "Tu es le JUGE de la maison ACE777. Après avoir pesé les arguments, TRANCHE la "
             "décision de façon claire et concise (2-3 phrases max) : OUI / NON / SOUS CONDITION. "
             "Important : notre système tourne sur macOS (pas Windows). Réponds en français."),
        ]
        results = [None] * 3
        threads = []
        for i, (task, role) in enumerate(roles):
            t = threading.Thread(target=_appel_hub, args=(task, role, sujet, results, i), daemon=True)
            threads.append(t)
            t.start()
        for t in threads:
            t.join(timeout=240)
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
        noms = ["GEMINI (analyste)", "DEEPSEEK (technique)", "LE JUGE tranche"]
        parties = []
        for i, nom in enumerate(noms):
            if results[i]:
                parties.append(f"• {nom} : {results[i].strip()}")
            else:
                parties.append(f"• {nom} : (injoignable)")
        texte_final = (f"🟡 CONSULTATION FAMILLE — {sujet}\n\n"
                       + "\n\n".join(parties)
                       + f"\n\n— Famille consultée, {date_str}")
        texte_final = texte_final.replace("**", "")
        if any(k in m_low for k in ("à voix", "a voix", "parle", "vocale")):
            threading.Thread(target=_speak_texte, args=(texte_final,), daemon=True).start()
        return {"ok": True, "texte": texte_final, "mode": "famille"}

    # Commande vocale VISION : DÉTECTION STRICTE en début de message pour ne
    # JAMAIS avaler une conversation normale (« j'ai une vision... », « regarde ce
    # que tu as fait »). On exige que le message COMMENCE par le mot-clé.
    m_low = msg.lower().lstrip()
    triggers = ("cortana regarde", "cortana regarde-moi", "regarde l'écran",
                "regarde ce qui est", "regarde-moi l'écran", "active la vision",
                "regarde", "regardez", "tes yeux", "vision", "capture l'écran")
    declenche = False
    for t in triggers:
        if m_low == t or m_low.startswith(t + " ") or m_low.startswith(t + " ") or m_low.startswith(t):
            declenche = True
            break
    if declenche:
        parler = any(k in m_low for k in ("a voix", "parle", "vocale", "a voix haute"))
        q = msg
        for k in ("cortana", "regarde", "regardez", "regarde-moi", "tes yeux",
                  "active la vision", "vision", "capture l'écran", "a voix",
                  "parle", "vocale", "a voix haute", "s'il te plaît",
                  "stp", "sil te plait", "l'écran", "ce qui est", "moi"):
            q = q.replace(k, " ").replace("  ", " ").strip()
        d = do_yeux(q, parler)
        d["mode"] = "yeux"
        return d
    payload = {
        "task": "mission",  # deepseek-v4-flash via NVIDIA + rotation hub (fallback)
        "messages": [
            {"role": "system", "content": (
                "Tu es Cortana, l'assistante de la maison ACE777. "
                "Réponds TOUJOURS en français, quel que soit le contexte. "
                "Sois concise, précise, sans markdown ni emoji."
            )},
            {"role": "user", "content": msg},
        ],
        "temperature": 0.4,
        "max_tokens": 700,
    }
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:11435/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=None) as resp:
            data = json.load(resp)
        content = data["choices"][0]["message"]["content"].strip()
        provider = data.get("provider", "?")
    except Exception as e:
        return {"ok": False, "error": f"hub injoignable: {str(e)[:160]}"}
    if not content:
        return {"ok": False, "error": "réponse vide du hub"}
    # voix Vivienne en arrière-plan (n'attend pas la fin de lecture)
    threading.Thread(target=_speak_texte, args=(content,), daemon=True).start()
    return {"ok": True, "texte": content, "provider": provider}


def _speak_texte(texte: str) -> None:
    """Lit un texte a voix haute (Vivienne) — thread arriere-plan.
    afplay tourne EN ARRIERE-PLAN : /stop (barge-in) peut couper la parole."""
    global _VOICE_PROC
    import tempfile as _tf
    try:
        with _tf.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            path = f.name
        if barge_in.activ():
            barge_in.preparer()  # calibration ambiant EN SILENCE, pendant la generation
        texte = oral_fr.oraliser(texte)  # 99,99 -> « quatre-vingt-dix-neuf virgule quatre-vingt-dix-neuf »
        cmd = [
            sys.executable, "-m", "edge_tts",
            "--voice", os.environ.get("EDGE_TTS_VOICE", "fr-FR-VivienneMultilingualNeural"),
            f"--rate={os.environ.get('EDGE_TTS_RATE', '-25%')}",
            "--text", texte, "--write-media", path,
        ]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if p.returncode == 0 and os.path.getsize(path) > 100:
            proc = subprocess.Popen(["afplay", path])
            with _VOICE_LOCK:
                _VOICE_PROC = proc
            if barge_in.activ():
                threading.Thread(target=barge_in.surveiller, args=(proc,), daemon=True).start()
            try:
                proc.wait(timeout=240)
            except subprocess.TimeoutExpired:
                proc.kill()
            finally:
                with _VOICE_LOCK:
                    if _VOICE_PROC is proc:
                        _VOICE_PROC = None
        if os.path.exists(path):
            try:
                os.unlink(path)
            except Exception:
                pass
    except Exception as e:
        print(f"[analyse-voix] ERR {e}", flush=True)


def stop_voice() -> str:
    """COUPE LA PAROLE (barge-in) : tue le afplay en cours, s'il y en a un."""
    global _VOICE_PROC
    with _VOICE_LOCK:
        proc = _VOICE_PROC
        _VOICE_PROC = None
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()
        return "Voix coupée."
    # La voix peut venir d'un SOUS-PROCESSUS (cortana_brief.py --speak) :
    # on la coupe quand même via pkill (filet global).
    p = subprocess.run(["pgrep", "-f", "afplay"], capture_output=True, text=True)
    if p.returncode == 0:
        subprocess.run(["pkill", "-f", "afplay"], capture_output=True, check=False)
        return "Voix coupée (sous-processus)."
    return "Aucune voix active."


def do_yeux(question: str = "", parler: bool = False) -> dict:
    """Les YEUX de Cortana : capture d'ecran -> hub Gemini vision -> analyse FR.
    Lance cortana_yeux.py en arriere-plan (capture + analyse + option lecture
    vocale), renvoie immediatement une confirmation (l'analyse arrive ensuite).
    """
    script = os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/scripts/cortana_yeux.py"
    )
    if not os.path.exists(script):
        return {"ok": False, "error": "cortana_yeux.py introuvable"}
    cmd = ["python3", script]
    if parler:
        cmd.append("--speak")
    if question and question.strip():
        cmd += ["--question", question.strip()[:500]]
    out_path = "/tmp/cortana_yeux_analyse.txt"
    cmd += ["--out", out_path]

    def _lancer():
        try:
            # vide l'analyse précédente : le polling ne renverra jamais un résultat
            # obsolète de la capture d'avant.
            try:
                if os.path.exists(out_path):
                    os.remove(out_path)
            except Exception:
                pass
            subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        except Exception as e:
            print(f"[yeux] ERR {e}", flush=True)

    threading.Thread(target=_lancer, daemon=True).start()
    return {"ok": True, "msg": "👁 Capture + analyse en cours…", "out": out_path}


def do_yeux_result() -> dict:
    """Lit le fichier d'analyse des yeux (écrit par cortana_yeux.py --out)."""
    p = "/tmp/cortana_yeux_analyse.txt"
    if not os.path.exists(p):
        return {"ok": True, "texte": None}
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            t = f.read().strip()
        return {"ok": True, "texte": t or None}
    except Exception:
        return {"ok": True, "texte": None}


def _http_cockpit() -> dict:
    import urllib.request
    import time

    url = "http://127.0.0.1:17800/cockpit/index.html"
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ace777-preflight/1"})
        with urllib.request.urlopen(req, timeout=1.5) as r:
            code = r.status
            r.read(64)
        ms = int((time.time() - t0) * 1000)
        ok = 200 <= int(code) < 400
        return {"ok": ok, "ms": ms, "code": code}
    except Exception as e:
        return {"ok": False, "ms": None, "err": str(e)[:80]}


def _hub_link() -> dict:
    """Hub Prise IA :11435 - health + nombre de providers actifs (pill COSMOS)."""
    import time
    import urllib.request

    url = "http://127.0.0.1:11435/health"
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ace777-preflight/1"})
        with urllib.request.urlopen(req, timeout=1.5) as r:
            data = json.loads(r.read().decode())
        ms = int((time.time() - t0) * 1000)
        ok = data.get("status") == "ok"
        prov = data.get("providers")
        detail = f"OK {prov} providers {ms}ms" if ok else f"status={data.get('status')} {ms}ms"
        return {"ok": ok, "ms": ms, "providers": prov, "detail": detail}
    except Exception as e:
        return {"ok": False, "ms": None, "detail": f"DOWN {str(e)[:50]}"}


def _genesis_ok() -> dict:
    import hashlib

    p = ROOT / "genesis_manifest.txt"
    if not p.exists():
        return {"ok": False, "md5": None, "detail": "genesis_manifest.txt manquant"}
    h = hashlib.md5(p.read_bytes()).hexdigest()
    ok = h.startswith("37fca367")
    return {"ok": ok, "md5": h[:12], "detail": f"md5 {h[:12]}…" + (" OK" if ok else " ≠ champion 37fca367")}


def _hulk_state() -> dict:
    import time

    if not HULK.is_dir():
        return {"ok": False, "state": "MISSING", "detail": "hulk-mexc absent"}
    # paper state / digest frais ?
    cands = list(HULK.glob("runs/**/*.json")) + list(HULK.glob("**/state*.json"))
    cands = [p for p in cands if p.is_file()]
    stop_paper = (HULK / "STOP_PAPER").exists()
    # mission.json often has hulk
    bags = None
    age = None
    if MISSION_JSON.exists():
        try:
            m = json.loads(MISSION_JSON.read_text(encoding="utf-8"))
            hk = m.get("hulk") or {}
            bags = hk.get("bags") or hk.get("n") or hk.get("positions")
            # prefer file mtime of mission for age of hulk block
            age = max(0, int(time.time() - MISSION_JSON.stat().st_mtime))
        except Exception:
            pass
    # Hulk OFF is normal often — warn not fail unless missing dir
    if stop_paper:
        return {"ok": True, "warn": True, "state": "STOP", "detail": "STOP_PAPER présent · paper arrêté", "bags": bags}
    if bags is not None:
        return {"ok": True, "warn": False, "state": "READ", "detail": f"bags={bags} · feed age {age}s", "bags": bags}
    return {"ok": True, "warn": True, "state": "IDLE", "detail": "pas de bags dans feed (paper idle OK)", "bags": bags}


def _stop_files() -> dict:
    import time

    names = []
    for n in ("STOP", "STOP_ALPHA", "STOP_BETA"):
        p = ROOT / n
        if p.exists():
            age = int(time.time() - p.stat().st_mtime)
            names.append(f"{n}({age}s)")
    ace = _ace_link()
    ace_on = ace.get("state") == "ON"
    if ace_on and names:
        return {"ok": False, "warn": False, "detail": "STOP pendant VOL: " + ", ".join(names), "files": names}
    if names:
        return {"ok": True, "warn": True, "detail": "STOP présents (froid OK): " + ", ".join(names), "files": names}
    return {"ok": True, "warn": False, "detail": "aucun STOP", "files": []}


def _thermo_core() -> dict:
    import time

    live = ROOT / "Index_Maison" / "thermo" / "live.json"
    if not live.exists():
        return {"ok": False, "detail": "live.json manquant", "ageSec": None}
    try:
        d = json.loads(live.read_text(encoding="utf-8"))
    except Exception as e:
        return {"ok": False, "detail": f"live.json illisible: {e}", "ageSec": None}
    age = max(0, int(time.time() - live.stat().st_mtime))
    fund = d.get("funding")
    oi = d.get("oi")
    fng = d.get("fearGreed")
    deg = bool(d.get("degraded") or d.get("staleFields"))
    ok = fund is not None and oi is not None and fng is not None
    detail = f"fund={fund} oi={oi} fng={fng} age={age}s"
    if deg:
        detail += " DEGRADED"
    if age > 900:
        return {"ok": ok, "warn": True, "detail": detail + " (thermo >15 min)", "ageSec": age}
    return {"ok": ok, "warn": deg or (age > 300), "detail": detail, "ageSec": age}


def _feed_core() -> dict:
    import time

    if not MISSION_JSON.exists():
        return {"ok": False, "detail": "mission.json manquant", "ageSec": None}
    try:
        d = json.loads(MISSION_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return {"ok": False, "detail": str(e)[:80], "ageSec": None}
    age = max(0, int(time.time() - MISSION_JSON.stat().st_mtime))
    run = d.get("run")
    combo = d.get("comboPnl")
    ok = bool(run) and combo is not None
    warn = age > 120
    return {
        "ok": ok,
        "warn": warn and ok,
        "detail": f"run={run} combo={combo} age={age}s",
        "ageSec": age,
        "run": run,
    }


def _daemons() -> dict:
    """LaunchAgents pont + http — best effort."""
    import subprocess

    uid = os.getuid()
    ok_p = ok_h = False
    try:
        r = subprocess.run(
            ["launchctl", "print", f"gui/{uid}/com.ace777.cockpit-pont"],
            capture_output=True, text=True, timeout=3,
        )
        out = (r.stdout or "") + (r.stderr or "")
        ok_p = r.returncode == 0 and ("state = running" in out or "active count = 1" in out)
    except Exception:
        ok_p = False
    try:
        r = subprocess.run(
            ["launchctl", "print", f"gui/{uid}/com.ace777.cockpit-http"],
            capture_output=True, text=True, timeout=3,
        )
        out = (r.stdout or "") + (r.stderr or "")
        ok_h = r.returncode == 0 and ("state = running" in out or "active count = 1" in out)
    except Exception:
        ok_h = False
    # fallback ports : si le service répond, c’est vert même si parse launchctl foire
    http = _http_cockpit()
    if http.get("ok"):
        ok_h = True
    # pont = ce process répond déjà → OK
    ok_p = True
    ok = ok_p and ok_h
    return {
        "ok": ok,
        "warn": not http.get("ok"),
        "detail": f"pont=ON http={'ON' if ok_h else 'OFF'}",
    }


def _item(iid: str, label: str, ok: bool, detail: str, go: str, warn: bool = False, level=None) -> dict:
    if level is None:
        if not ok:
            level = "fail"
        elif warn:
            level = "warn"
        else:
            level = "ok"
    return {
        "id": iid,
        "label": label,
        "ok": ok and level != "fail",
        "level": level,  # ok | warn | fail
        "detail": detail,
        "go": go,
    }


def do_preflight() -> dict:
    """Checklist allumage prototype — lecture seule, pas de GO trading."""
    ace = _ace_link()
    net = _net_link()
    http = _http_cockpit()
    hub = _hub_link()
    thermo = _thermo_core()
    feed = _feed_core()
    gen = _genesis_ok()
    hulk = _hulk_state()
    stops = _stop_files()
    daem = _daemons()
    mute = Path("/tmp/ace777_swarm_pids/.cortana_mute").exists()

    core = [
        _item(
            "pont", "PONT", True,
            "bridge :17777 répond",
            "bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh --daemons",
        ),
        _item(
            "http", "HTTP", bool(http.get("ok")),
            f":17800 {'OK' if http.get('ok') else http.get('err') or 'DOWN'} {http.get('ms') or ''}ms".strip(),
            "bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh --daemons",
            warn=False,
        ),
        _item(
            "hub", "HUB",
            bool(hub.get("ok")),
            hub.get("detail") or "—",
            "COSMOS complet dans l'onglet GRAPH · providers, budget cloud, file d'attente",
            warn=not bool(hub.get("ok")),
            level=("ok" if hub.get("ok") else "warn"),
        ),
        _item(
            "thermo", "THERMO", bool(thermo.get("ok")),
            thermo.get("detail") or "—",
            "python3 ~/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py",
            warn=bool(thermo.get("warn")),
        ),
        _item(
            "feed", "FEED", bool(feed.get("ok")),
            feed.get("detail") or "—",
            "python3 ~/ace777-test-day1/Index_Maison/scripts/cockpit_mission_feed.py",
            warn=bool(feed.get("warn")),
        ),
        _item(
            "ace", "ACE",
            ace.get("state") == "ON",
            f"{ace.get('label')} age={ace.get('ageSec')}s run={ace.get('run')}",
            "si OFF: hygiène + GO_USINE (Terminal) · si STALE: vérifier LIVE",
            warn=ace.get("state") == "STALE",
            level=("ok" if ace.get("state") == "ON" else ("warn" if ace.get("state") == "STALE" else "fail")),
        ),
        _item(
            "net", "NET",
            net.get("state") != "DOWN",
            f"{net.get('label')} {net.get('ms')}ms" if net.get("ms") is not None else str(net.get("label")),
            "réseau / VPN · ping fapi.binance.com",
            warn=net.get("state") == "SLOW",
            level=("fail" if net.get("state") == "DOWN" else ("warn" if net.get("state") == "SLOW" else "ok")),
        ),
        _item(
            "hulk", "HULK",
            bool(hulk.get("ok")),
            hulk.get("detail") or "—",
            "hulk-mexc paper · voir mission Hulk",
            warn=bool(hulk.get("warn")),
        ),
        _item(
            "genesis", "GENESIS",
            bool(gen.get("ok")),
            gen.get("detail") or "—",
            "NE PAS toucher genesis · restore champion 37fca367 si drift",
        ),
        _item(
            "stop", "STOP",
            bool(stops.get("ok")),
            stops.get("detail") or "—",
            "rm STOP* seulement si froid + GO hygiène · jamais pendant VOL sans ordre",
            warn=bool(stops.get("warn")),
        ),
        _item(
            "daemons", "DAEMONS",
            bool(daem.get("ok")),
            daem.get("detail") or "—",
            "bash ~/ace777-test-day1/Index_Maison/scripts/install_cockpit_daemons.sh && cockpit_up.sh --daemons",
            warn=bool(daem.get("warn")),
        ),
    ]

    # LIQ/ETF soft
    live_path = ROOT / "Index_Maison" / "thermo" / "live.json"
    liq = etf_btc = None
    if live_path.exists():
        try:
            ld = json.loads(live_path.read_text(encoding="utf-8"))
            liq = ld.get("liq24Usd")
            etf_btc = (ld.get("etf") or {}).get("btc")
        except Exception:
            pass

    extra = [
        _item(
            "voix", "VOIX",
            True,
            "MUTE" if mute else "LIVE (unmute)",
            "bouton MUET cockpit · ou cortana_mute.py",
            warn=mute,
            level="warn" if mute else "ok",
        ),
        _item(
            "liq", "LIQ/ETF",
            True,
            f"liq={liq} etf_btc={etf_btc} (free souvent n/d)",
            "WARN free flaky — pas bloquant",
            warn=(liq is None and etf_btc is None),
            level="warn" if (liq is None and etf_btc is None) else "ok",
        ),
        _item(
            "graph", "GRAPH",
            True,
            "onglet GRAPH machine · cerveau HTML = finition",
            "open Index_Maison/graph_cerveau/index.html (finition)",
            warn=False,
        ),
        _item(
            "session", "SESSION",
            True,
            "début/fin = scripts session_*.sh",
            "bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --open",
            warn=False,
        ),
    ]

    fails = [c for c in core if c["level"] == "fail"]
    warns = [c for c in core if c["level"] == "warn"]
    return {
        "ok": len(fails) == 0,
        "ready": len(fails) == 0,
        "failN": len(fails),
        "warnN": len(warns),
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "summary": (
            "PREFLIGHT GO" if not fails and not warns
            else ("PREFLIGHT GO · WARN" if not fails else f"PREFLIGHT NO-GO · {len(fails)} rouge(s)")
        ),
        "core": core,
        "extra": extra,
    }


# === AJOUT STRATÉGIE (onglet F2, GO 11/08) ===
def do_strategie() -> dict:
    """Lit STRATEGIE.md (analyste) + derniere_analyse.md → dashboard STRATÉGIE.
    Renvoie le texte brut des sections (court terme / tendance) et la date."""
    base = os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")
    strategie_path = os.path.join(base, "STRATEGIE.md")
    analyse_path = os.path.join(base, "derniere_analyse.md")

    out = {"ok": True, "strategie": None, "analyse": None, "date": None}
    try:
        if os.path.exists(strategie_path):
            with open(strategie_path, encoding="utf-8", errors="replace") as f:
                out["strategie"] = f.read()
            # date depuis la première ligne "# STRATEGIE — <ts>"
            m = __import__("re").match(r"# STRATEGIE[^—]*—\s*([^\n]+)", out["strategie"])
            if m:
                out["date"] = m.group(1).strip()
    except Exception:
        pass
    try:
        if os.path.exists(analyse_path):
            with open(analyse_path, encoding="utf-8", errors="replace") as f:
                out["analyse"] = f.read()
    except Exception:
        pass
    return out


def _last_decollage() -> dict:
    """Retourne le dernier DÉCOLLAGE (CHOIX_OFFRES.json) + trace d'évaluation.
    Détecte les erreurs 429/403 dans le log d'évaluation → écrit un cooldown 1h."""
    p = os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/strategie/CHOIX_OFFRES.json"
    )
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return None

    trace = None
    strategie_dir = os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")
    log_path = os.path.join(strategie_dir, f"EVAL_OFFRES_{d.get('date', '')}.log")
    cooldown_path = os.path.join(strategie_dir, "COOLDOWN_429.json")
    if os.path.exists(log_path):
        try:
            lignes = open(log_path, encoding="utf-8", errors="replace").read().splitlines()
            # dernières lignes récentes de l'évaluation en cours
            trace = lignes[-8:] if lignes else []
            # Détection STRICTE des erreurs de quota : uniquement des patterns
            # HTTP explicites (429/403/rate limit/insufficient). Jamais le mot
            # "quota" seul (présent dans la sortie normale d'eval_offres).
            quota_hit = any(
                (" 429 " in l or "429 " in l or l.strip().startswith("429")
                 or " 403 " in l or l.strip().startswith("403")
                 or "rate limit" in l.lower()
                 or "insufficient" in l.lower()
                 or "status 429" in l.lower() or "status 403" in l.lower())
                for l in lignes[-30:]
            )
            if quota_hit and not os.path.exists(cooldown_path):
                with open(cooldown_path, "w", encoding="utf-8") as f:
                    json.dump({"ts": datetime.now(timezone.utc).isoformat(),
                               "raison": "429/403 detecte"}, f)
        except Exception:
            trace = None
    return {"ts": d.get("ts", ""), "choix": d.get("choix", []), "trace": trace}


def _dernier_rapport_veille(date_du_jour: str) -> tuple:
    """Retourne (path, date) du dernier rapport VEILLE_HUB valide (cache J-1).
    Ne prend JAMAIS le rapport du jour (déjà traité), et ignore les fichiers
    vides/tronqués (< 60 octets ou sans section '### ')."""
    maison = os.path.expanduser("~/ace777-test-day1/Index_Maison")
    try:
        candidats = sorted(
            glob.glob(os.path.join(maison, "VEILLE_HUB_*.md")), reverse=True
        )
    except Exception:
        return None, None
    for p in candidats:
        base = os.path.basename(p)
        d = base.replace("VEILLE_HUB_", "").replace(".md", "")[:10]
        if d >= date_du_jour:
            continue
        try:
            taille = os.path.getsize(p)
            if taille < 60:
                continue
            with open(p, "r", encoding="utf-8", errors="replace") as f:
                tete = f.read(4000)
            if "### " not in tete or "Nouvelles offres" not in tete:
                continue
        except Exception:
            continue
        return p, d
    return None, None


FICHES_CACHE_PATH = Path.home() / "ace777-test-day1/Index_Maison/strategie/FICHES_OFFRES.json"
FICHES_GEN_SCRIPT = Path.home() / "ace777-test-day1/Index_Maison/scripts/fiches_offres.py"


def _sha12(section: str, item: str) -> str:
    """Clé stable d'une offre (section|item -> sha1 12 hex)."""
    return hashlib.sha1(f"{section}|{item}".encode("utf-8")).hexdigest()[:12]


def _charger_cache_fiches() -> dict:
    """Charge FICHES_OFFRES.json -> dict des fiches (jamais d'exception)."""
    if not FICHES_CACHE_PATH.exists():
        return {}
    try:
        with open(FICHES_CACHE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("fiches", {}) if isinstance(data, dict) else {}
    except Exception:
        return {}


def _quota_fiches_epuise() -> bool:
    """True si les 8 fiches du jour (UTC) sont déjà générées — évite de
    lancer le générateur pour rien à chaque poll du cockpit."""
    try:
        if not FICHES_CACHE_PATH.exists():
            return False
        with open(FICHES_CACHE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        jour = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return (data.get("jours") or {}).get(jour, 0) >= 8
    except Exception:
        return False


def _lancer_generateur_fiches_detache():
    """Lance fiches_offres.py en arrière-plan (jamais bloquant, anti-relance)."""
    if not FICHES_GEN_SCRIPT.exists():
        return
    if _quota_fiches_epuise():
        return  # quota du jour atteint — ne pas relancer pour rien
    try:
        res = subprocess.run(["pgrep", "-f", "fiches_offres.py"],
                             capture_output=True, text=True, timeout=5)
        if res.stdout.strip():
            return  # déjà en cours
    except Exception:
        pass
    try:
        with open("/tmp/fiches_offres.log", "a") as out, \
             open("/tmp/fiches_offres.err.log", "a") as err:
            subprocess.Popen([sys.executable, str(FICHES_GEN_SCRIPT)],
                             stdout=out, stderr=err, start_new_session=True)
    except Exception as e:
        print(f"[WARN] Impossible de lancer fiches_offres.py : {e}")


def do_offres() -> dict:
    """Lit VEILLE_HUB_<date>.md → dashboard STRATÉGIE (sections + offres).
    Si le rapport du jour est absent OU corrompu → fallback sur le dernier
    rapport valide (mode cache J-1), signalé par le champ "cache"."""
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    veille_path = os.path.expanduser(
        f"~/ace777-test-day1/Index_Maison/VEILLE_HUB_{date}.md"
    )
    cache = False
    cache_date = None
    if not os.path.exists(veille_path):
        veille_path, cache_date = _dernier_rapport_veille(date)
        if veille_path:
            cache = True
    elif os.path.getsize(veille_path) < 60:
        # rapport du jour corrompu (trop court) → cache J-1
        veille_path, cache_date = _dernier_rapport_veille(date)
        cache = True if veille_path else False
    if not veille_path:
        return {"ok": True, "date": date, "total": 0,
                "sections": [], "offres": [], "decollage": _last_decollage(),
                "cache": False}

    # Sections dont les offres sont évaluables automatiquement (A/B) par
    # eval_offres.py — les autres sont de la DÉCOUVERTE (pas encore testables).
    TESTABLE = ("openrouter", "nvidia", "inferx", "puter")

    sections = {}  # nom -> {count, err, testable}
    offres = []
    current_section = None
    try:
        with open(veille_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("### "):
                    current_section = line[4:].strip()
                    if current_section and current_section not in sections:
                        sections[current_section] = {
                            "count": 0, "err": False,
                            "testable": any(
                                k in current_section.lower() for k in TESTABLE
                            ),
                        }
                elif line.startswith("- ") and current_section:
                    item = line[2:].strip()
                    if "INTEGRATION" in current_section.upper():
                        continue
                    if item.startswith("ERR:"):
                        sections[current_section]["err"] = True
                        continue
                    if item and "aucune nouvelle" not in item.lower():
                        sections[current_section]["count"] += 1
                        if len(offres) < 25:
                            offres.append({
                                "section": current_section, "item": item,
                                "testable": sections[current_section]["testable"],
                            })
    except Exception:
        pass  # non fatal

    # === CHANTIER A v2 : fiches UNIQUES générées par l'IA du hub (cache, non bloquant) ===
    fiches_cache = _charger_cache_fiches()
    offres_en_attente = False
    for offre in offres:
        section = offre.get("section", "")
        item = offre.get("item", "")
        cle = _sha12(section, item)
        if cle in fiches_cache:
            offre["fiche"] = fiches_cache[cle]
        else:
            # Vue brute : coup d'œil immédiat même sans analyse IA
            fiche_attente = {
                "type": "⏳ Analyse en attente (max 8/jour)",
                "forts": ["Fiche générée par l'IA au prochain passage"],
                "faibles": ["Pas encore analysée"],
                "usage": "Recharge l'onglet dans quelques minutes",
                "avis_pour": "",
                "avis_attention": "",
                "brut": item,
                "section": section,
            }
            if "openrouter" in section.lower():
                fiche_attente["lien"] = (
                    "https://openrouter.ai/models?q=" + quote(item)
                )
            elif "nvidia" in section.lower():
                fiche_attente["lien"] = (
                    "https://build.nvidia.com/explore"
                )
            offre["fiche"] = fiche_attente
            offres_en_attente = True
    for n, s in sections.items():
        if not s.get("testable") and "fiche" not in s:
            s["fiche"] = {
                "type": "Nouveau lieu / source détecté par la veille",
                "forts": ["Peut cacher une offre ou un modèle intéressant"],
                "faibles": ["Inconnu — à vérifier avant de s'y fier"],
                "usage": "À explorer une fois par jour (7h) pour ne rien rater",
            }
    if offres_en_attente:
        _lancer_generateur_fiches_detache()

    total = sum(s["count"] for s in sections.values())
    return {
        "ok": True, "date": date, "total": total,
        "sections": [{"name": n, **s} for n, s in sections.items()],
        "offres": offres,
        "decollage": _last_decollage(),
        "cache": cache,
        "cache_date": cache_date,
    }


def do_signets() -> dict:
    """Signets X résumés par le lecteur IA (cache SIGNETS_RESUMES.json).
    Renvoie : résumés (triés date desc), quota du jour, nombre en attente,
    et lance le lecteur en détaché si des signets restent à analyser."""
    import pathlib
    from urllib.parse import quote as _quote

    cache_path = pathlib.Path(os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/strategie/SIGNETS_RESUMES.json"))
    cache = {"version": 1, "jours": {}, "signets": {}}
    if cache_path.exists():
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cache = json.load(f)
        except Exception:
            pass

    signets = []
    for _cle, _s in cache.get("signets", {}).items():
        _s = dict(_s)
        _s["_cle"] = _cle
        signets.append(_s)
    signets.sort(key=lambda s: (s.get("date", ""), s.get("generated", "")), reverse=True)

    # Compte les signets .md non résumés (attente) — scan léger
    signets_dir = pathlib.Path(os.path.expanduser(
        "~/Documents/Obsidian_ACE777/Signets_X"))
    en_attente = 0
    connus = set(cache.get("signets", {}).keys())
    try:
        for md in signets_dir.rglob("*.md"):
            try:
                txt = md.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            m = None
            for ligne in txt.splitlines():
                if ligne.strip().startswith("url:"):
                    m = ligne.split(":", 1)[1].strip().strip('"')
                    break
            if m:
                cle = hashlib.sha256(m.encode("utf-8")).hexdigest()[:12]
                if cle not in connus:
                    en_attente += 1
    except Exception as _e:
        print(f"[signets] scan en_attente : {_e}")

    # Si des signets attendent et quota pas épuisé → lance le lecteur en détaché
    aujourdhui = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    utilises = cache.get("jours", {}).get(aujourdhui, 0)
    if en_attente > 0 and utilises < 15:
        _lancer_lecteur_signets_detache()

    return {
        "ok": True,
        "total": len(signets),
        "en_attente": en_attente,
        "quota_jour": utilises,
        "quota_max": 15,
        "signets": signets[:50],  # les 50 plus récents
    }


def _lancer_lecteur_signets_detache():
    """Lance signets_lecture.py en détaché (sa propre session)."""
    import subprocess
    script = os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/scripts/signets_lecture.py")
    if not os.path.exists(script):
        return
    try:
        with open(os.devnull, "w") as nul:
            subprocess.Popen(
                [sys.executable, "-u", script],
                stdout=nul, stderr=subprocess.STDOUT,
                start_new_session=True,
            )
    except Exception as e:
        print(f"[signets] échec lancement lecteur : {e}")


def do_signets_valider(body: dict) -> dict:
    """POST /signets/valider : marque un signet à garder / poubelle / lu."""
    import pathlib
    cle = str(body.get("cle") or "")
    avis = str(body.get("avis") or "").strip().lower()
    if avis not in ("garder", "poubelle", "lu", ""):
        return {"ok": False, "error": "avis invalide"}
    cache_path = pathlib.Path(os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/strategie/SIGNETS_RESUMES.json"))
    if not cache_path.exists():
        return {"ok": False, "error": "cache introuvable"}
    try:
        with open(cache_path, "r", encoding="utf-8") as f:
            cache = json.load(f)
    except Exception:
        return {"ok": False, "error": "cache illisible"}
    if cle not in cache.get("signets", {}):
        return {"ok": False, "error": "signet inconnu"}
    cache["signets"][cle]["avis"] = avis
    # écriture atomique
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(cache_path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
        os.replace(tmp, cache_path)
    except Exception as e:
        try:
            os.unlink(tmp)
        except Exception:
            pass
        return {"ok": False, "error": str(e)}
    return {"ok": True, "avis": avis, "cle": cle}


def do_decoller(selection: list) -> dict:
    """Écrit CHOIX_OFFRES.json (atomique) et lance eval_offres.py en background."""
    if not selection:
        return {"ok": False, "error": "aucune offre cochée"}

    selection = selection[:5]  # protection quotas gratuits
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    strategie_dir = os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/strategie"
    )
    os.makedirs(strategie_dir, exist_ok=True)
    choix_path = os.path.join(strategie_dir, "CHOIX_OFFRES.json")

    # A9 : si un cooldown 429/403 est actif depuis < 1h, on refuse de relancer.
    # IMPORTANT : le check se fait AVANT toute écriture — jamais de faux
    # « DÉCOLLAGE lancé » dans l'UI si le lancement est refusé.
    cooldown_path = os.path.join(strategie_dir, "COOLDOWN_429.json")
    if os.path.exists(cooldown_path):
        try:
            with open(cooldown_path, encoding="utf-8") as f:
                cd = json.load(f)
            debut = cd.get("ts", "")
            if debut:
                try:
                    diff = (datetime.now(timezone.utc) - datetime.fromisoformat(debut)).total_seconds()
                except Exception:
                    diff = 99999
                if diff < 3600:
                    return {"ok": False, "error": (
                        "Quota épuisé (429/403) détecté il y a "
                        + str(int(diff // 60)) + " min — cooldown 1h. Réessayez plus tard.")}
        except Exception:
            pass

    data = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "date": date,
        "choix": selection,
    }

    tmp_path = choix_path + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp_path, choix_path)
    except Exception as e:
        return {"ok": False, "error": str(e)}

    script_path = os.path.expanduser(
        "~/ace777-test-day1/Index_Maison/scripts/eval_offres.py"
    )
    log_path = os.path.join(strategie_dir, f"EVAL_OFFRES_{date}.log")

    def _launch():
        try:
            with open(log_path, "a", encoding="utf-8") as logf:
                logf.write("\n=== DÉCOLLAGE %s ===\n" % datetime.now(timezone.utc).isoformat())
                subprocess.Popen(
                    ["python3", script_path, "--choix", choix_path],
                    stdout=logf,
                    stderr=logf,
                )
        except Exception:
            pass

    threading.Thread(target=_launch, daemon=True).start()
    return {"ok": True, "msg": f"Évaluation lancée sur {len(selection)} offre(s)"}


def do_status() -> dict:
    mute = Path("/tmp/ace777_swarm_pids/.cortana_mute").exists()
    return {
        "muted": mute,
        "ok": True,
        "port": PORT,
        "bridge": "cortana+mission",
        "pont": "ON",
        "ace": _ace_link(),
        "net": _net_link(),
    }


def do_mission() -> dict:
    """Régénère le feed puis renvoie mission.json (anti-cache)."""
    try:
        run_py(SCRIPTS / "cockpit_mission_feed.py", timeout=60)
    except Exception as e:
        return {"ok": False, "error": str(e)}
    if not MISSION_JSON.exists():
        return {"ok": False, "error": "mission.json manquant"}
    try:
        data = json.loads(MISSION_JSON.read_text(encoding="utf-8"))
        data["ok"] = True
        return data
    except Exception as e:
        return {"ok": False, "error": str(e)}


def do_alerts() -> dict:
    sys.path.insert(0, str(SCRIPTS))
    try:
        from cortana_thermo import load_day_alerts

        items = load_day_alerts()
    except Exception as e:
        return {"ok": False, "error": str(e), "alerts": []}
    return {"ok": True, "alerts": list(reversed(items[-80:])), "n": len(items)}


JUSTESSE_TTL = 1800  # 30 min : ne relance pas 27 analyses LLM à chaque appel

def do_justesse() -> dict:
    """Score de justesse de l'analyste (boucle d'apprentissage) — JSON pour le cockpit.
    Cache : régénère au plus toutes les 30 min (27 analyses LLM sinon)."""
    import time as _time
    tmp = SCRIPTS / "justesse_cockpit.json"
    if tmp.exists():
        age = _time.time() - tmp.stat().st_mtime
        if age < JUSTESSE_TTL:
            try:
                data = json.loads(tmp.read_text(encoding="utf-8"))
                data["ok"] = True
                data["cached"] = True
                return data
            except Exception:
                pass  # cache corrompu → régénère
    try:
        run_py(SCRIPTS / "score_justesse.py", "--json", str(tmp), timeout=60)
    except Exception as e:
        return {"ok": False, "error": str(e)}
    if not tmp.exists():
        return {"ok": False, "error": "justesse vide (aucune analyse notée pour l'instant)"}
    try:
        data = json.loads(tmp.read_text(encoding="utf-8"))
        data["ok"] = True
        return data
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _touch_stop(path: Path, note: str) -> None:
    try:
        path.write_text(note + "\n", encoding="utf-8")
    except Exception:
        pass


def _run_bash(script: Path, timeout: int = 90) -> str:
    if not script.exists():
        return f"missing:{script.name}"
    p = subprocess.run(
        ["bash", str(script)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
        timeout=timeout,
    )
    out = ((p.stdout or "") + (p.stderr or "")).strip()
    return (out[-500:] if out else f"rc={p.returncode}")


def _log_panic(mode: str, detail: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    line = f"{ts} PANIC mode={mode} {detail}\n"
    try:
        PANIC_LOG.parent.mkdir(parents=True, exist_ok=True)
        with PANIC_LOG.open("a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass


def do_panic(mode: str, confirm: str = "") -> dict:
    """Kill-switch lecture→sortie uniquement. A=propre · B=crash (confirm=CRASH)."""
    m = (mode or "").strip().upper()
    conf = (confirm or "").strip().upper()
    note = f"cockpit-panic-{m}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%MZ')}"

    if m not in ("A", "B"):
        return {"ok": False, "error": "mode A ou B requis", "mode": m}

    if m == "B" and conf != "CRASH":
        return {
            "ok": False,
            "error": "mode B : taper CRASH en confirm",
            "mode": "B",
            "needConfirm": "CRASH",
        }

    # Signaux stop ACE + Hulk paper (pas d'entrée)
    for name in ("STOP", "STOP_ALPHA", "STOP_BETA"):
        _touch_stop(ROOT / name, note)
    if HULK.is_dir():
        _touch_stop(HULK / "STOP_PAPER", note)
        _touch_stop(HULK / "STOP_DIGEST", note)

    steps = []
    if m == "A":
        steps.append("stop_ace777.sh:" + _run_bash(ROOT / "stop_ace777.sh", timeout=90))
        msg = "MODE A — arrêt propre (STOP + stop_ace777 + Hulk STOP_PAPER)"
    else:
        steps.append("stop_ace777_hard.sh:" + _run_bash(ROOT / "stop_ace777_hard.sh", timeout=120))
        # Filet NUAGE (hygiène partielle — pas WebKit/Cursor)
        for pat in (
            "ace777_launch_v85_nuage",
            "launch_vide_froid_4h_binance_NUAGE",
            "watchdog_ace777",
            "ace777_stream_genesis",
            "ruby -e sleep",
        ):
            subprocess.run(["pkill", "-9", "-f", pat], capture_output=True)
        steps.append("pkill_filet=done")
        msg = "MODE B — CRASH stop hard + filet"

    _log_panic(m, msg)
    return {"ok": True, "mode": m, "msg": msg, "steps": steps, "logged": str(PANIC_LOG)}


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store")

    def _json(self, code: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/status"):
            self._json(200, do_status())
            return
        if path == "/mission":
            self._json(200, do_mission())
            return
        if path == "/refresh":
            # GET aussi — certains WebView bloquent POST ou CORS préflight
            self._json(200, do_mission())
            return
        if path == "/alerts":
            self._json(200, do_alerts())
            return
        if path == "/preflight":
            self._json(200, do_preflight())
            return
        if path == "/justesse":
            self._json(200, do_justesse())
            return
        if path == "/offres":
            self._json(200, do_offres())
            return
        if path == "/signets":
            self._json(200, do_signets())
            return
        if path == "/strategie":
            self._json(200, do_strategie())
            return
        if path == "/yeux/result":
            self._json(200, do_yeux_result())
            return
        if path == "/ecoute":
            self._json(200, {"ok": True, "ecoute": barge_in.activ()})
            return
        self._json(404, {"ok": False, "error": "not found"})

    def _read_json(self) -> dict:
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except Exception:
            n = 0
        if n <= 0:
            return {}
        raw = self.rfile.read(n).decode("utf-8", errors="ignore")
        try:
            data = json.loads(raw or "{}")
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    def do_POST(self):
        path = urlparse(self.path).path

        def bg(fn, label):
            def wrap():
                try:
                    msg = fn()
                    print(f"[{label}] {str(msg)[:200]}")
                except Exception as e:
                    print(f"[{label}] ERR {e}")

            threading.Thread(target=wrap, daemon=True).start()

        if path == "/mute":
            msg = do_mute()
            self._json(200, {"ok": True, "action": "mute", "msg": msg, "muted": True})
            return
        if path == "/unmute":
            msg = do_unmute()
            self._json(200, {"ok": True, "action": "unmute", "msg": msg, "muted": False})
            return
        if path == "/speak":
            bg(do_speak, "speak")
            self._json(200, {"ok": True, "action": "speak", "msg": "brief en cours…", "muted": False})
            return
        if path == "/stop":
            msg = stop_voice()
            self._json(200, {"ok": True, "action": "stop", "msg": msg, "muted": False})
            return
        if path == "/ecoute":
            if barge_in.activ():
                etat = barge_in.ecoute_couper()
            else:
                etat = barge_in.ecoute_activer()
            self._json(200, {"ok": True, "action": "ecoute", "ecoute": etat})
            return
        if path == "/analyse":
            body = self._read_json()
            indice = str(body.get("indice") or "")
            if not indice:
                self._json(400, {"ok": False, "error": "indice manquant"})
                return
            data = do_analyse(indice)
            code = 200 if data.get("ok") else 502
            self._json(code, data)
            return
        if path == "/chat":
            body = self._read_json()
            message = str(body.get("message") or "")
            data = do_chat(message)
            code = 200 if data.get("ok") else 502
            self._json(code, data)
            return
        if path == "/yeux":
            body = self._read_json()
            question = str(body.get("question") or "")
            parler = bool(body.get("parler"))
            data = do_yeux(question, parler)
            code = 200 if data.get("ok") else 502
            self._json(code, data)
            return
        if path == "/refresh":
            data = do_mission()
            self._json(200, data)
            return
        if path == "/decoller":
            body = self._read_json()
            sel = body.get("selection") or []
            self._json(200, do_decoller(sel))
            return
        if path == "/signets/valider":
            body = self._read_json()
            self._json(200, do_signets_valider(body))
            return
        if path == "/panic":
            body = self._read_json()
            mode = str(body.get("mode") or "")
            confirm = str(body.get("confirm") or "")
            # Mode A synchrone (feedback UI) — peut prendre quelques secondes
            data = do_panic(mode, confirm)
            code = 200 if data.get("ok") else 400
            self._json(code, data)
            return
        self._json(404, {"ok": False, "error": "not found"})

    def log_message(self, fmt, *args):
        sys.stderr.write("[bridge] " + (fmt % args) + "\n")


def _maintenance_demarrage() -> None:
    """A6 : purge .tmp orphelins (> 10 min) et rotation des logs > 10 Mo.
    Exécutée à chaque démarrage du bridge — jamais bloquant."""
    try:
        import time as _t
        seuil = _t.time() - 600
        for base in ["~/ace777-test-day1/Index_Maison/strategie",
                     "~/ace777-test-day1/Index_Maison"]:
            d = os.path.expanduser(base)
            if not os.path.isdir(d):
                continue
            for nom in os.listdir(d):
                if not nom.endswith(".tmp"):
                    continue
                p = os.path.join(d, nom)
                try:
                    if os.path.getmtime(p) < seuil:
                        os.remove(p)
                except Exception:
                    pass
    except Exception:
        pass
    try:
        # rotation du log du bridge s'il dépasse 10 Mo
        for log in ["/tmp/cortana_cockpit_bridge.log",
                    "/tmp/brief_offres.err.log", "/tmp/brief_offres.out.log"]:
            if os.path.exists(log) and os.path.getsize(log) > 10 * 1024 * 1024:
                os.replace(log, log + ".old")
    except Exception:
        pass
    try:
        # purge d'un cooldown 429 expiré (> 1 h)
        cd = os.path.expanduser(
            "~/ace777-test-day1/Index_Maison/strategie/COOLDOWN_429.json")
        if os.path.exists(cd):
            try:
                with open(cd, encoding="utf-8") as f:
                    debut = json.load(f).get("ts", "")
                if debut and (datetime.now(timezone.utc)
                              - datetime.fromisoformat(debut)).total_seconds() > 3600:
                    os.remove(cd)
            except Exception:
                os.remove(cd)
    except Exception:
        pass


def main() -> int:
    import socket

    class ReuseThreadingHTTPServer(ThreadingHTTPServer):
        allow_reuse_address = True
        daemon_threads = True

        def server_bind(self):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            super().server_bind()

    _maintenance_demarrage()
    httpd = ReuseThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"CORTANA_BRIDGE http://127.0.0.1:{PORT}  (status|mission|alerts|preflight|refresh|panic|mute|speak)", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("stop")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
