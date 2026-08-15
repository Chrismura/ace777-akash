#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
famille_session.py — Consultation du trio (Gemini + DeepSeek + Juge)
sur certaines occasions (alerte récente, session dans le rouge, rafale revenge).

Pattern trio copié du bridge (cortana_cockpit_bridge.py) : 3 threads parallèles,
tasks audit.protocol / mission / signets.juge, synthèse écrite + voix optionnelle.

Usage :
  python3 famille_session.py --check            -> consulte si occasion détectée
  python3 famille_session.py --force            -> consulte toujours
  python3 famille_session.py --force --speak    -> + voix Vivienne (verdict du Juge)
  python3 famille_session.py --test             -> auto-test des conditions (sans réseau)
"""

import os
import sys
import json
import time
import threading
import urllib.request
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, Any

# === CONSTANTES ===
BASE = Path(os.path.expanduser("~")) / "ace777-test-day1" / "Index_Maison"
STRATEGIE = BASE / "strategie"
LIVE = STRATEGIE / "journal_intention_live.json"
MISSION = BASE / "cockpit" / "mission.json"
ALARME = STRATEGIE / "alarme.json"
OUT = STRATEGIE / "AVIS_FAMILLE_SESSION.md"
HISTO = STRATEGIE / "historique_famille"
ETAT = STRATEGIE / "famille_derniere.json"  # anti-spam
HUB = "http://127.0.0.1:11435/v1/chat/completions"
ALARME_FRAICHEUR_H = 6  # une alerte de plus de 6h n'est plus une "occasion"
ANTI_SPAM_MIN = 5       # anti-spam court (mode training : tout peut changer en 30 min) — une nouvelle occasion = consultation immédiate

ROLES = {
    "audit.protocol": (
        "Tu es Gemini, analyste senior de la maison ACE777. Donne un avis CONCIS "
        "(2-3 phrases max) : les risques, les angles morts, ce qu'on pourrait rater. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
    "mission": (
        "Tu es DeepSeek, expert technique de la maison ACE777. Donne un avis CONCIS "
        "(2-3 phrases max) : la cohérence du setup, ce qui peut casser, la faisabilité. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
    "signets.juge": (
        "Tu es le JUGE de la maison ACE777. Après avoir pesé les arguments, TRANCHE la "
        "décision de façon claire et concise (2-3 phrases max) : OUI / NON / SOUS CONDITION. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
}
TASKS = ["audit.protocol", "mission", "signets.juge"]
NOMS = ["GEMINI (analyste)", "DEEPSEEK (technique)", "LE JUGE tranche"]


def lire_json(path: Path, default: Any = None) -> Any:
    try:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        pass
    return default


def _appel_hub(task: str, messages: list, resultats: Dict[str, str], cle: str) -> None:
    """Appel hub pour un membre du trio (thread). timeout=None (règle maison)."""
    payload = {
        "task": task,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 500,
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=None) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            resultats[cle] = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print("famille: appel %s en echec (%s)" % (task, e), file=sys.stderr)
        resultats[cle] = None


def deja_consulte(raison: str) -> Tuple[bool, float]:
    """Anti-spam : même raison consultée il y a moins de ANTI_SPAM_MIN minutes ?"""
    try:
        if ETAT.exists():
            d = json.loads(ETAT.read_text(encoding="utf-8"))
            if d.get("raison") == raison:
                age = time.time() - d.get("ts", 0)
                if 0 < age < ANTI_SPAM_MIN * 60:
                    return True, age
    except Exception:
        pass
    return False, 0.0


def marquer_consulte(raison: str) -> None:
    try:
        STRATEGIE.mkdir(parents=True, exist_ok=True)
        ETAT.write_text(json.dumps({"raison": raison, "ts": time.time()}), encoding="utf-8")
    except Exception:
        pass


def est_une_occasion(live: dict, force: bool = False) -> Tuple[bool, str]:
    """Détermine si une occasion de consultation existe (déterministe)."""
    if force:
        return True, "demande explicite"

    # 1. Alerte RÉCENTE (la vigie écrit alarme.json seulement quand elle tire)
    if ALARME.exists():
        try:
            frais = (time.time() - ALARME.stat().st_mtime) < ALARME_FRAICHEUR_H * 3600
            alarme = lire_json(ALARME, {})
            if frais and alarme and isinstance(alarme, dict) and alarme.get("type"):
                return True, "alerte en cours"
        except Exception:
            pass

    # 2. Session dans le rouge
    bots = (live or {}).get("bots", {})
    alpha = bots.get("alpha", {})
    if alpha.get("fills", 0) > 0 and alpha.get("pnl", 0.0) < 0:
        return True, "session dans le rouge"

    # 3. Rafale revenge
    if alpha.get("revenge", 0) >= 3:
        return True, "rafale de mode revenge"

    return False, ""


def build_sujet(live: dict) -> str:
    """Construit le brief compact en français pour le trio."""
    bots = (live or {}).get("bots", {})
    alpha = bots.get("alpha", {})
    beta = bots.get("beta", {})
    story = (live or {}).get("story", [])

    alerte_txt = "aucune"
    try:
        a = lire_json(ALARME, None)
        if a:
            alerte_txt = json.dumps(a, ensure_ascii=False)[:300]
    except Exception:
        pass

    return (
        "SESSION (depuis %s) :\n"
        "• ALPHA (Le Sniper) : %s tirs, %s skips (discipline), pnl %+.2f $, "
        "dont %s revenge 1.5x\n"
        "• BETA (L'Éclaireur) : %s sondes, conf moyenne %s, %s long / %s court\n"
        "• STORY : %s\n"
        "• ALERTE : %s\n"
        "QUESTION : cette session appelle-t-elle une action ? (ajuster le setup, "
        "réduire l'exposition, laisser courir...) Réponds en français, macOS, concis."
        % (
            live.get("since", "N/A"),
            alpha.get("fills", 0), alpha.get("skips", 0), alpha.get("pnl", 0.0),
            alpha.get("revenge", 0),
            beta.get("fills", 0), beta.get("conf_moy", 0),
            beta.get("direction", {}).get("long", 0),
            beta.get("direction", {}).get("short", 0),
            " | ".join(story[-3:]) if story else "aucune",
            alerte_txt,
        )
    )


def consulter(force: bool = False, speak: bool = False) -> None:
    """Consultation principale du trio."""
    live = lire_json(LIVE, {}) or {}

    occasion, raison = est_une_occasion(live, force)
    if not occasion:
        print("pas d'occasion — le trio reste en veille")
        return
    if not force:
        deja, age = deja_consulte(raison)
        if deja:
            print("deja consulte (%s) il y a %d min — anti-spam, trio en veille"
                  % (raison, int(age // 60)))
            return

    sujet = build_sujet(live)
    ts = datetime.now().isoformat()

    resultats: Dict[str, Any] = {}
    threads = []
    for task in TASKS:
        t = threading.Thread(
            target=_appel_hub,
            args=(task, [{"role": "system", "content": ROLES[task]},
                         {"role": "user", "content": sujet}], resultats, task),
            daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join(timeout=240)

    parties = []
    for i, task in enumerate(TASKS):
        r = resultats.get(task)
        if r:
            parties.append("• %s : %s" % (NOMS[i], r.strip()))
        else:
            parties.append("• %s : (injoignable)" % NOMS[i])

    contenu = (
        "# AVIS FAMILLE SESSION — %s\n"
        "OCCASION : %s\n\n"
        "🟡 CONSULTATION FAMILLE\n\n"
        "%s\n\n"
        "— Famille consultée, %s\n"
        % (ts, raison, "\n\n".join(parties), datetime.now().strftime("%d/%m/%Y %H:%M"))
    )
    contenu = contenu.replace("**", "")

    try:
        STRATEGIE.mkdir(parents=True, exist_ok=True)
        OUT.write_text(contenu, encoding="utf-8")
        HISTO.mkdir(parents=True, exist_ok=True)
        (HISTO / ("AVIS_%s.md" % ts.replace(":", "-"))).write_text(contenu, encoding="utf-8")
        # anti-spam marqué APRÈS l'écriture réussie uniquement
        if not force:
            marquer_consulte(raison)
        print("Avis écrit : %s (occasion : %s)" % (OUT, raison))
    except Exception as e:
        print("Erreur écriture avis: %s" % e, file=sys.stderr)

    if speak:
        juge = resultats.get("signets.juge")
        if juge:
            speak_verdict(juge)


def speak_verdict(texte: str) -> None:
    """Voix Vivienne via python -m edge_tts (pattern analyste.py)."""
    try:
        subprocess.run(
            [sys.executable, "-m", "edge_tts",
             "--voice", "fr-FR-VivienneMultilingualNeural",
             "--rate=-15%",
             "--text", texte[:800],
             "--write-media", "/tmp/famille_verdict.mp3"],
            check=True, timeout=60, capture_output=True)
        subprocess.run(["afplay", "/tmp/famille_verdict.mp3"], check=True, timeout=120)
    except Exception:
        pass


def run_test() -> int:
    """Auto-test des conditions (sans réseau, hermétique : on isole ALARME)."""
    import tempfile
    tmpd = Path(tempfile.mkdtemp())
    global ALARME
    ALARME = tmpd / "alarme_absent.json"  # isole du fichier réel

    errors = 0

    def check(name, cond):
        nonlocal errors
        print("OK  %s" % name if cond else "FAIL %s" % name)
        if not cond:
            errors += 1

    # 1. session dans le rouge
    o, r = est_une_occasion({"bots": {"alpha": {"fills": 3, "pnl": -5.0, "revenge": 0}}})
    check("session rouge -> occasion", o and r == "session dans le rouge")

    # 2. rafale revenge
    o, r = est_une_occasion({"bots": {"alpha": {"fills": 3, "pnl": 10.0, "revenge": 4}}})
    check("rafale revenge -> occasion", o and r == "rafale de mode revenge")

    # 3. pas d'occasion
    o, r = est_une_occasion({"bots": {"alpha": {"fills": 1, "pnl": 2.0, "revenge": 0}}})
    check("session verte -> pas d'occasion", not o)

    # 4. force
    o, r = est_une_occasion({}, force=True)
    check("force -> occasion", o)

    # 5. alerte RÉCENTE -> occasion
    al = tmpd / "alarme_recente.json"
    al.write_text('{"type": "prix", "raison": "volume x3"}', encoding="utf-8")
    ALARME = al
    o, r = est_une_occasion({})
    check("alerte recente -> occasion", o and r == "alerte en cours")

    # 6. alerte STALE (vieille) -> pas d'occasion
    stale = tmpd / "alarme_stale.json"
    stale.write_text('{"type": "prix"}', encoding="utf-8")
    vieux = time.time() - (ALARME_FRAICHEUR_H * 3600 + 3600)
    import os
    os.utime(str(stale), (vieux, vieux))
    ALARME = stale
    o, r = est_une_occasion({})
    check("alerte stale -> pas d'occasion", not o)

    # 7. build_sujet
    sujet = build_sujet({"bots": {"alpha": {"fills": 2, "pnl": -3.0},
                                  "beta": {"fills": 10, "conf_moy": 0.9}},
                         "story": ["BETA a sonde."], "since": "2026-08-12T00:00:00Z"})
    check("sujet contient les roles", "ALPHA" in sujet and "BETA" in sujet and "Le Sniper" in sujet)

    return 0 if errors == 0 else 1


def main():
    args = sys.argv[1:]
    if "--test" in args:
        sys.exit(run_test())

    force = "--force" in args
    speak = "--speak" in args
    if "--check" in args or force:
        consulter(force=force, speak=speak)
    else:
        print("Usage: famille_session.py --check [--force] [--speak] | --test")


if __name__ == "__main__":
    main()
