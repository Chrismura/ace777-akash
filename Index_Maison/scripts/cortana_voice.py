#!/usr/bin/env python3
"""
CORTANA VOICE — humanize chiffres + TTS.
Priorité : edge-tts neuronal (Vivienne = voix validée « suave »)
Repli : macOS say UNIQUEMENT si CORTANA_TTS=auto et edge échoue à générer.

Env:
  EDGE_TTS_VOICE   défaut fr-FR-VivienneMultilingualNeural
  EDGE_TTS_RATE    défaut -18%  (posé / pédagogique)
  CORTANA_TTS      edge|say|auto  (défaut edge — évite mélange Vivienne+Amélie)
  CORTANA_VOICE    repli say (Amelie…)
"""
from __future__ import annotations

import fcntl
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path

# Voix « Cortana film » — Vivienne (validée Christophe 2026-07-30)
EDGE_VOICE = os.getenv("EDGE_TTS_VOICE", "fr-FR-VivienneMultilingualNeural")
EDGE_RATE = os.getenv("EDGE_TTS_RATE", "-18%")
TTS_MODE = os.getenv("CORTANA_TTS", "edge").lower()  # edge|say|auto

VOIX = os.getenv("CORTANA_VOICE", "Amelie")
FALLBACKS = ["Amelie", "Amélie", "Thomas", "Samantha"]
SPEAK_LOCK = Path("/tmp/ace777_swarm_pids/.cortana_speak.lock")

UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
TEENS = [
    "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize",
    "dix-sept", "dix-huit", "dix-neuf",
]
TENS = [
    "", "", "vingt", "trente", "quarante", "cinquante", "soixante",
    "soixante", "quatre-vingt", "quatre-vingt",
]


def num2words_fr(n: int) -> str:
    if n < 0:
        return "moins " + num2words_fr(-n)
    if n < 10:
        return UNITS[n]
    if n < 20:
        return TEENS[n - 10]
    if n < 60:
        d, u = divmod(n, 10)
        if u == 0:
            return TENS[d]
        if u == 1 and d in (2, 3, 4, 5, 6):
            return TENS[d] + " et un"
        return TENS[d] + "-" + UNITS[u]
    if n < 70:
        u = n - 60
        if u == 0:
            return "soixante"
        if u == 1:
            return "soixante et un"
        return "soixante-" + UNITS[u]
    if n < 80:
        return "soixante-" + TEENS[n - 70]
    if n < 100:
        if n == 80:
            return "quatre-vingts"
        if n == 81:
            return "quatre-vingt-un"
        return "quatre-vingt-" + num2words_fr(n - 80)
    if n < 1000:
        c, r = divmod(n, 100)
        head = "cent" if c == 1 else num2words_fr(c) + " cent"
        if r == 0:
            return head + ("s" if c > 1 else "")
        return head + " " + num2words_fr(r)
    if n < 10000:
        m, r = divmod(n, 1000)
        head = "mille" if m == 1 else num2words_fr(m) + " mille"
        if r == 0:
            return head
        return head + " " + num2words_fr(r)
    return " ".join(UNITS[int(d)] for d in str(n))


def float2words_fr(f: float, *, digit_decimals: bool = True) -> str:
    if f < 0:
        return "moins " + float2words_fr(-f, digit_decimals=digit_decimals)
    if abs(f) >= 10000:
        return " ".join(UNITS[int(d)] for d in str(int(abs(f))))
    s = f"{f:.6f}".rstrip("0").rstrip(".")
    if "." not in s:
        return num2words_fr(int(s))
    int_part, dec_part = s.split(".", 1)
    int_word = num2words_fr(int(int_part))
    if digit_decimals:
        dec_digits = " ".join(UNITS[int(d)] for d in dec_part[:4])
        return f"{int_word} virgule {dec_digits}"
    return f"{int_word} virgule {num2words_fr(int(dec_part[:2] or '0'))}"


def _sign_word(sign: str) -> str:
    if sign == "+":
        return "plus "
    if sign == "-":
        return "moins "
    return ""


def _pct_to_words(sign: str, val: float) -> str:
    return _sign_word(sign) + float2words_fr(val) + " pour cent"


def _money_to_words(sign: str, val: float) -> str:
    return _sign_word(sign) + float2words_fr(val) + " dollars"


def _unit_to_words(val_str: str, unit: str) -> str:
    num = float2words_fr(float(val_str)) if "." in val_str else num2words_fr(int(float(val_str)))
    unit_map = {
        "ms": "millisecondes",
        "s": "secondes",
        "min": "minutes",
        "h": "heures",
        "USDT": "U S D T",
        "BTC": "bitcoin",
        "ETH": "éthereum",
    }
    return f"{num} {unit_map.get(unit, unit)}"


def humanize(text: str) -> str:
    """Chiffres → français parlé. Ne remplace JAMAIS '-' en global.
    Purge aussi l'anglais pour éviter que Vivienne (multilingual) bascule de langue.
    """
    # --- FR d'abord (jargon) pour éviter superposition FR/EN ---
    fr_map = [
        (r"\bCortana urgent\.?", "Cortana. Alerte."),
        (r"\bfunding\b", "taux de financement"),
        (r"\bFunding\b", "taux de financement"),
        (r"\bfund\b", "taux de financement"),
        (r"\bFUD\b", "taux de financement"),
        (r"\bfud\b", "taux de financement"),
        (r"\bURGENT\b", "alerte"),
        (r"\bALERTE\b", "alerte"),
        (r"\bSource\b", "provenance"),
        (r"\bmanual\b", "manuel"),
        (r"\bdrawdown\b", "recul"),
        (r"\bDrawdown\b", "recul"),
        (r"\bprofit\b", "bénéfice"),
        (r"\bProfit\b", "bénéfice"),
        (r"\bPnL\b", "bénéfice"),
        (r"\bPnl\b", "bénéfice"),
        (r"\bsess\b", "session"),
        (r"\bSKIP\b", "passé"),
        (r"\bBUY\b", "achat"),
        (r"\bSELL\b", "vente"),
        (r"\bSTOP\b", "arrêt"),
        (r"\bFLAT\b", "à plat"),
        (r"\bLONG\b", "position longue"),
        (r"\bSHORT\b", "position courte"),
        (r"\bLIVE\b", "en direct"),
        (r"\bheat\b", "chaleur"),
        (r"\bmark\b", "cours"),
        (r"\bWhales?\b", "baleines"),
        (r"\bwhales?\b", "baleines"),
        (r"\bprints?\b", "transactions"),
        (r"\bproxy\b", "estimation"),
        (r"\btaker\b", "ratio acheteur"),
        (r"\bOI\b", "intérêt ouvert"),
        (r"\bmoy\b", "moyenne"),
        (r"\bnow\b", "actuel"),
        (r"\bUSDT\b", "dollars"),
        (r"\bBTC\b", "bitcoin"),
        (r"\bETH\b", "éthereum"),
        (r"\bACE\b", "Ace"),
        (r"\bHULK\b", "Hulk"),
        (r"\bBETA\b", "bêta"),
        (r"\bALPHA\b", "alfa"),
        (r"\bcommander\b", "commandant"),
        (r"\bHello\b", "Bonjour"),
        (r"\bsystems?\b", "systèmes"),
        (r"\bnominal\b", "nominaux"),
        (r"\bsoft\b", "souple"),
        (r"\bskip\b", "passé"),
        (r"\bscore\b", "score"),
    ]
    for pat, rep in fr_map:
        text = re.sub(pat, rep, text, flags=re.IGNORECASE)

    # Dates ISO / scientific → neutre (évite lecture chiffre-par-chiffre bizarre)
    text = re.sub(r"\d{4}-\d{2}-\d{2}T[\d:]+Z?", "à l'instant", text)
    text = re.sub(
        r"(\d+(?:\.\d+)?)e\+?(-?\d+)",
        lambda m: float2words_fr(float(m.group(0))),
        text,
        flags=re.IGNORECASE,
    )
    # fichiers log / chemins : ne pas épeler
    text = re.sub(r"\b[\w.-]+\.(log|csv|json|html)\b", "fichier journal", text, flags=re.IGNORECASE)
    text = re.sub(r"\bNUAGE_[\w]+\b", "run nuage", text)
    text = re.sub(r"≥", "plus de ", text)
    text = re.sub(r"≈", "environ ", text)
    text = re.sub(r"·", ",", text)

    text = re.sub(
        r"([+-]?)(\d+\.\d+)%",
        lambda m: _pct_to_words(m.group(1), float(m.group(2))),
        text,
    )
    text = re.sub(
        r"([+-]?)(\d+\.\d+)\s*\$",
        lambda m: _money_to_words(m.group(1), float(m.group(2))),
        text,
    )
    text = re.sub(
        r"([+-]?)(\d+)\s*\$",
        lambda m: _money_to_words(m.group(1), float(m.group(2))),
        text,
    )
    text = re.sub(
        r"(\d+\.?\d*)\s*(ms|s|min|h|USDT|BTC|ETH)\b",
        lambda m: _unit_to_words(m.group(1), m.group(2)),
        text,
    )
    text = re.sub(
        r"\b([A-Za-z_][A-Za-z0-9_]*)=([+-]?\d+\.\d+)\b",
        lambda m: f"{m.group(1)} {float2words_fr(float(m.group(2)))}",
        text,
    )
    text = re.sub(
        r"\b([A-Za-z_][A-Za-z0-9_]*)=([+-]?\d+)\b",
        lambda m: f"{m.group(1)} {num2words_fr(int(m.group(2)))}",
        text,
    )
    text = re.sub(
        r"(?<![\w.])([+-]?\d+\.\d+)(?![\w%$/])",
        lambda m: float2words_fr(float(m.group(1))),
        text,
    )
    text = re.sub(
        r"(?<![\w.])(\d{1,4})(?![\w.%$/])",
        lambda m: num2words_fr(int(m.group(1))),
        text,
    )
    text = re.sub(r"(?<!\w)\+(?!\w)", " plus ", text)
    text = re.sub(r"(?<!\w)=(?!\w)", " égal ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def resolve_voice() -> str:
    pref = os.getenv("CORTANA_VOICE", VOIX)
    try:
        out = subprocess.run(["say", "-v", "?"], capture_output=True, text=True, check=False)
        names = [ln.split()[0] for ln in (out.stdout or "").splitlines() if ln.strip()]
    except Exception:
        names = []
    for c in [pref, pref.replace("é", "e"), *FALLBACKS]:
        if c in names:
            return c
    for n in names:
        if n.lower().startswith("amel"):
            return n
    return "Thomas"


def _edge_available() -> bool:
    try:
        r = subprocess.run(
            ["python3", "-m", "edge_tts", "--help"],
            capture_output=True,
            check=False,
            timeout=8,
        )
        return r.returncode == 0
    except Exception:
        return False


def _silence_players() -> None:
    """Coupe say + afplay pour une seule piste."""
    subprocess.run(["killall", "say"], check=False, capture_output=True)
    subprocess.run(["killall", "afplay"], check=False, capture_output=True)
    time.sleep(0.05)


def _prechime_wav_path() -> Path:
    """WAV doux généré une fois — pad 2 tons ~0.45 s (anti crise cardiaque)."""
    path = Path("/tmp/ace777_cortana_prechime.wav")
    if path.exists() and path.stat().st_size > 200:
        return path
    import math
    import struct
    import wave

    sr = 22050
    dur = 0.48
    n = int(sr * dur)
    frames = bytearray()
    for i in range(n):
        t = i / sr
        # enveloppe douce attack/release
        env = min(1.0, t / 0.06) * max(0.0, 1.0 - (t - 0.22) / 0.26)
        env = max(0.0, min(1.0, env))
        # deux sinus bas (pas de bip aigu)
        s = 0.55 * math.sin(2 * math.pi * 392.0 * t)  # G4
        s += 0.35 * math.sin(2 * math.pi * 493.88 * t)  # B4
        s *= env * 0.22
        frames += struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767))
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(bytes(frames))
    return path


def play_prechime(*, urgent: bool = False) -> None:
    """Son suave juste avant la voix. Désactiver : CORTANA_PRECHIME=0."""
    if os.getenv("CORTANA_PRECHIME", "1") == "0":
        return
    # news / briefs : toujours · urgent : aussi (sinon surprise pire)
    vol = os.getenv("CORTANA_PRECHIME_VOL", "0.22" if not urgent else "0.28")
    try:
        wav = _prechime_wav_path()
        subprocess.run(
            ["afplay", "-v", str(vol), str(wav)],
            check=False,
            timeout=5,
            capture_output=True,
        )
        time.sleep(0.12)  # micro silence avant Vivienne
    except Exception:
        pass


def edge_speak(text: str, voice: str | None = None, rate: str | None = None) -> str:
    """Synthèse neuronale Microsoft → afplay.
    Retourne: 'ok' | 'gen_fail' | 'play_interrupted' | 'error'
    Ne jamais traiter play_interrupted comme échec → sinon double voix (say par-dessus).
    """
    v = voice or EDGE_VOICE
    r = rate or EDGE_RATE
    t = text.strip()
    if len(t) > 2200:
        t = t[:2200] + "…"
    path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            path = f.name
        cmd = [
            "python3", "-m", "edge_tts",
            "--voice", v,
            f"--rate={r}",  # une seule arg : sinon -10% est mangé par argparse
            "--text", t,
            "--write-media", path,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=90, check=False)
        if proc.returncode != 0 or not Path(path).exists() or Path(path).stat().st_size < 100:
            if path:
                Path(path).unlink(missing_ok=True)
            return "gen_fail"
        play = subprocess.run(["afplay", path], check=False, timeout=180)
        Path(path).unlink(missing_ok=True)
        # afplay tué par un autre brief / mute → pas un échec de synthèse
        if play.returncode != 0:
            return "play_interrupted"
        return "ok"
    except Exception:
        if path:
            try:
                Path(path).unlink(missing_ok=True)
            except Exception:
                pass
        return "error"


def say_speak(text: str, voice: str | None = None) -> None:
    v = voice or resolve_voice()
    try:
        subprocess.run(["say", "-v", v, text], check=False, timeout=90)
    except Exception:
        subprocess.run(["say", text], check=False)


def _with_speak_lock(fn):
    """Un seul brief à la fois — évite Vivienne + Amélie en parallèle."""
    SPEAK_LOCK.parent.mkdir(parents=True, exist_ok=True)
    with SPEAK_LOCK.open("a+") as lf:
        fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
        try:
            return fn()
        finally:
            fcntl.flock(lf.fileno(), fcntl.LOCK_UN)


def speak(text: str, urgent: bool = False, voice: str | None = None) -> str:
    """Humanize + TTS (edge Vivienne). Respecte mute. Pas de mélange say/edge."""
    mute_path = Path("/tmp/ace777_swarm_pids/.cortana_mute")
    if mute_path.exists() and not urgent:
        human = humanize(text)
        print(f"[voix:MUETTE] {human[:120]}…")
        return human
    if mute_path.exists() and urgent:
        if os.getenv("CORTANA_MUTE_ALLOW_URGENT", "1") != "1":
            print("[voix:MUETTE] alerte silencieuse (mute strict)")
            return humanize(text)

    human = humanize(text)
    prefix = "Alerte. " if urgent else ""
    full = prefix + human

    def _do() -> str:
        mode = TTS_MODE
        use_edge = mode == "edge" or (mode == "auto" and _edge_available())
        if mode == "say":
            use_edge = False

        engine = "none"
        _silence_players()
        # Avertisseur doux avant la voix (évite le « d’un coup »)
        play_prechime(urgent=urgent)

        if use_edge:
            ev = os.getenv("EDGE_TTS_VOICE", EDGE_VOICE)
            status = edge_speak(full, voice=ev)
            if status == "ok":
                engine = f"edge:{ev}"
            elif status == "play_interrupted":
                # Un autre brief a pris la main — ne PAS lancer say
                engine = f"edge:{ev}:interrompu"
            elif mode == "auto":
                # Repli Mac uniquement en mode auto explicite
                say_speak(full, voice=voice)
                engine = "say:" + resolve_voice() + ":fallback"
            else:
                # mode edge strict : silence plutôt que voix Mac mélangée
                engine = f"edge:{ev}:echec_gen"
                print(f"[voix:WARN] edge KO ({status}) — pas de repli say (CORTANA_TTS=edge)")
        else:
            say_speak(full, voice=voice)
            engine = "say:" + resolve_voice()

        print(f"[voix:{engine}] {full[:160]}{'…' if len(full) > 160 else ''}")
        return full

    return _with_speak_lock(_do)


if __name__ == "__main__":
    import sys

    demo = " ".join(sys.argv[1:]) or "PnL +32.44$ drawdown -8.36%. Systèmes nominaux, commandant."
    print("HUMAN:", humanize(demo))
    speak(demo)
