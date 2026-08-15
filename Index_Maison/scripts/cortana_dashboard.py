#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cortana_dashboard.py — Cortana = dashboard (F3, 15/08/2026)

Cortana lit TOUTE la maison (ACE fills + Hulk paper + marché) et en fait une
synthèse unique, écrite ET vocale. C'est le cerveau/dashboard d'ACE777.

- Source de vérité : mission.json (agrégat cockpit) + CSV fills (récent) +
  Hulk state/veille + thermo live.json + ADA gardienne (voilure/saison).
- Normalisation : un schéma unique (snapshot) pour ACE + Hulk + marché.
- Sortie : `cortana_snapshot_{ts}.json` (rotation 50 max) + synthèse via le hub
  (task cortana.analyse, prompt identité Cortana canon).

Lecture seule (C2/C3) : aucun ordre, aucune écriture hors snapshots/rotation.

Usage :
  python3 cortana_dashboard.py            # synthèse écrite
  python3 cortana_dashboard.py --speak    # + lecture vocale (Vivienne)
  python3 cortana_dashboard.py --json     # snapshot seul (sans LLM)
  python3 cortana_dashboard.py --test     # auto-test hermétique (sans fichiers réels)
"""
import argparse
import json
import os
import sys
import subprocess
import tempfile
import time
import urllib.request
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
INDEX = os.path.join(BASE, "Index_Maison")
SCRIPTS = os.path.join(INDEX, "scripts")
MISSION = os.path.join(INDEX, "cockpit", "mission.json")
THERMO_LIVE = os.path.join(INDEX, "thermo", "live.json")
ADA_LIVE = os.path.join(INDEX, "strategie", "ada_gardienne_live.json")
SAISON_LIVE = os.path.join(INDEX, "strategie", "ada_saison_live.json")
HULK_RUNS = os.path.join(BASE, "hulk-mexc", "runs")
HULK_VEILLE = os.path.join(HULK_RUNS, ".veille_status.json")
IDENTITY = os.path.join(INDEX, "identity", "prompts", "cortana.md")
SNAP_DIR = os.path.join(INDEX, "strategie", "cortana_snapshots")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "cortana.analyse"
MAX_SNAPS = 50


def safe_json(path, default=None):
    if default is None:
        default = {}
    try:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return default


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def tail_lines(path, nbytes=120000, max_lines=600):
    """Dernières lignes du fichier (sans charger le fichier entier en RAM)."""
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - nbytes))
            data = f.read().decode("utf-8", errors="replace")
        lines = data.splitlines()
        if lines and not lines[0].lstrip().startswith("20"):
            lines = lines[1:]
        return lines[-max_lines:]
    except Exception:
        return []


# ── ACE (fills) ──────────────────────────────────────────────
def ace_recent(csv_path):
    """Stats récentes d'un CSV de fills ACE (dernières lignes, post-fix 12 colonnes)."""
    out = {"win": 0, "loss": 0, "flat": 0, "revenge": 0, "hold_sum": 0.0, "hold_n": 0,
           "pnl_by_reason": {}}
    for line in tail_lines(csv_path):
        parts = line.split(",")
        if len(parts) < 11 or parts[3] != "FILLED":
            continue
        try:
            pnl = float(parts[8])
        except ValueError:
            continue
        if pnl > 0.0001:
            out["win"] += 1
        elif pnl < -0.0001:
            out["loss"] += 1
        else:
            out["flat"] += 1
        reason = parts[9]
        out["pnl_by_reason"][reason] = round(out["pnl_by_reason"].get(reason, 0.0) + pnl, 4)
        # revenge : présent dans msg (col 12) ou dans le slot holdSec des vieilles lignes
        blob = " ".join(parts[10:]).lower()
        if "revenge" in blob:
            out["revenge"] += 1
        try:
            hold = float(parts[10])
            out["hold_sum"] += hold
            out["hold_n"] += 1
        except (ValueError, IndexError):
            pass
    out["avg_hold_sec"] = round(out["hold_sum"] / out["hold_n"], 1) if out["hold_n"] else None
    return out


def load_ace(mission):
    alpha = mission.get("alpha") or {}
    beta = mission.get("beta") or {}
    a_file = os.path.join(BASE, "runs", alpha.get("file", ""))
    b_file = os.path.join(BASE, "runs", beta.get("file", ""))
    return {
        "run": mission.get("run"),
        "combo_pnl": mission.get("comboPnl"),
        "alpha": {
            "pnl_session": alpha.get("pnl"),
            "fills": alpha.get("fills"),
            "skips": alpha.get("skips"),
            "pnl_lifetime": alpha.get("pnlLifetime"),
            "fills_lifetime": alpha.get("fillsLifetime"),
            "recent": ace_recent(a_file) if a_file else {},
        },
        "beta": {
            "pnl_session": beta.get("pnl"),
            "fills": beta.get("fills"),
            "skips": beta.get("skips"),
            "pnl_lifetime": beta.get("pnlLifetime"),
            "fills_lifetime": beta.get("fillsLifetime"),
            "recent": ace_recent(b_file) if b_file else {},
        },
    }


# ── Hulk ─────────────────────────────────────────────────────
def load_hulk(mission):
    hulk = mission.get("hulk") or {}
    state = safe_json(os.path.join(HULK_RUNS, hulk.get("stateFile", "")), {})
    veille = safe_json(HULK_VEILLE, {})
    vcount = {"RED": 0, "AMBER": 0, "GREEN": 0}
    for k, v in veille.items():
        if k.startswith("_") or not isinstance(v, dict):
            continue
        st = str(v.get("status", "")).upper()
        if st in vcount:
            vcount[st] += 1
    return {
        "pnl_total": hulk.get("pnl"),
        "trades": hulk.get("trades"),
        "notional": hulk.get("notional"),
        "base": hulk.get("base"),
        "positions": [{"pair": p.get("pair")} for p in hulk.get("positions", [])],
        "positions_n": len(hulk.get("positions", [])),
        "bags_n": len(state.get("bags", {})),
        "bag_dca_n": len(state.get("bag_dca", {})),
        "veille": vcount,
    }


# ── Marché ───────────────────────────────────────────────────
def load_marche():
    live = safe_json(THERMO_LIVE, {})
    ada = safe_json(ADA_LIVE, {})
    saison = safe_json(SAISON_LIVE, {})
    return {
        "mark": live.get("mark"),
        "chg24": live.get("chg24"),
        "funding": live.get("funding"),
        "fear_greed": live.get("fearGreed"),
        "climate": live.get("climate"),
        "score": live.get("score"),
        "saison": saison.get("saison") or ada.get("coup_doeil", {}).get("saison"),
        "voilure": ada.get("voilure"),
        "zone": ada.get("zone"),
    }


def build_snapshot():
    mission = safe_json(MISSION, {})
    return {
        "version": "v1",
        "ts": utc_now(),
        "ace": load_ace(mission),
        "hulk": load_hulk(mission),
        "marche": load_marche(),
        "sources": ["mission.json", "runs/*.csv (tail)", "hulk state+veille",
                    "thermo/live.json", "ada_gardienne_live.json"],
    }


# ── Identité + hub ───────────────────────────────────────────
def load_identity():
    try:
        return open(IDENTITY, encoding="utf-8").read()
    except Exception:
        return ("Tu es Cortana, le cerveau/dashboard d'ACE777. Analyste court terme, "
                "lecture seule, aucun ordre. Réponds écrit + voix, chiffres exacts, vulgarise.")


def ask_hub(snapshot, identity):
    payload = {
        "task": TASK,
        "messages": [
            {"role": "system", "content": identity},
            {"role": "user", "content": (
                "Voici l'état complet de la maison ACE777 (snapshot normalisé) :\n\n"
                f"{json.dumps(snapshot, ensure_ascii=False, indent=1)}\n\n"
                "Fais la synthèse de dashboard : (1) l'état du moteur ACE (duo ALPHA/BETA, "
                "PnL, revenge, flat, hold), (2) l'état de Hulk (paper, positions, bags, veille), "
                "(3) le marché (saison, voilure, climat), (4) 1-3 points d'attention ou "
                "anomalies, (5) un verdict court. 8-12 phrases max, chiffres exacts, "
                "vulgarisé, sans ordre ni recommandation d'achat/vente."
            )},
        ],
        "temperature": 0.4,
        "max_tokens": 900,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"], data.get("provider", "?")


def save_snapshot(snapshot):
    os.makedirs(SNAP_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = os.path.join(SNAP_DIR, f"cortana_snapshot_{ts}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)
    # rotation : garder les MAX_SNAPS plus récents
    snaps = sorted(os.listdir(SNAP_DIR))
    for old in snaps[:-MAX_SNAPS]:
        try:
            os.remove(os.path.join(SNAP_DIR, old))
        except OSError:
            pass
    return path


def speak_text(text, voice="fr-FR-VivienneMultilingualNeural", rate="-15%"):
    if os.path.exists("/tmp/ace777_swarm_pids/.cortana_mute"):
        print("  [voix:MUETTE] mute actif — saut", file=sys.stderr)
        return 1
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        path = f.name
    cmd = ["python3", "-m", "edge_tts", "--voice", voice, f"--rate={rate}",
           "--text", text, "--write-media", path]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    if proc.returncode != 0 or not os.path.exists(path) or os.path.getsize(path) < 100:
        print("  ✘ génération voix échouée", file=sys.stderr)
        return 1
    subprocess.run(["killall", "say"], check=False, capture_output=True)
    subprocess.run(["killall", "afplay"], check=False, capture_output=True)
    time.sleep(0.05)
    subprocess.run(["afplay", path], check=False, timeout=240)
    os.unlink(path)
    return 0


# ── Tests hermétiques ────────────────────────────────────────
def run_tests():
    global BASE, MISSION, THERMO_LIVE, ADA_LIVE, SAISON_LIVE, HULK_RUNS, SNAP_DIR
    _sauve = (BASE, MISSION, THERMO_LIVE, ADA_LIVE, SAISON_LIVE, HULK_RUNS, SNAP_DIR)
    tmp = tempfile.mkdtemp(prefix="cortana_dashboard_test_")
    BASE = tmp
    MISSION = os.path.join(tmp, "mission.json")
    THERMO_LIVE = os.path.join(tmp, "live.json")
    ADA_LIVE = os.path.join(tmp, "ada.json")
    SAISON_LIVE = os.path.join(tmp, "saison.json")
    SNAP_DIR = os.path.join(tmp, "snaps")
    errors = 0

    def check(name, cond):
        nonlocal errors
        print("  %s %s" % ("✓" if cond else "✗", name))
        if not cond:
            errors += 1

    def restore():
        global BASE, MISSION, THERMO_LIVE, ADA_LIVE, SAISON_LIVE, HULK_RUNS, SNAP_DIR
        (BASE, MISSION, THERMO_LIVE, ADA_LIVE, SAISON_LIVE, HULK_RUNS, SNAP_DIR) = _sauve

    json.dump({
        "run": "TEST", "comboPnl": 1.23,
        "alpha": {"file": "a.csv", "pnl": 1.0, "fills": 5, "skips": 10,
                  "pnlLifetime": 100.0, "fillsLifetime": 50},
        "beta": {"file": "b.csv", "pnl": 0.23, "fills": 8, "skips": 12,
                 "pnlLifetime": 10.0, "fillsLifetime": 80},
        "hulk": {"file": "p.csv", "stateFile": "p.json", "pnl": -2.0, "trades": 3,
                 "notional": 18.0, "base": 20.0, "positions": [{"pair": "XUSDT"}]},
    }, open(MISSION, "w"))
    json.dump({"mark": 63000.0, "chg24": 0.5, "funding": 0.0001, "fearGreed": 30,
               "climate": "ok", "score": 70}, open(THERMO_LIVE, "w"))
    json.dump({"voilure": 87.9, "zone": "VERT"}, open(ADA_LIVE, "w"))
    json.dump({"saison": "CALME"}, open(SAISON_LIVE, "w"))
    os.makedirs(HULK_RUNS, exist_ok=True)
    json.dump({"_meta": {}, "XUSDT": {"status": "RED"}, "YUSDT": {"status": "GREEN"}},
              open(os.path.join(HULK_RUNS, ".veille_status.json"), "w"))
    # CSV synthétique (12 colonnes, 1 win + 1 revenge)
    os.makedirs(os.path.join(tmp, "runs"), exist_ok=True)
    with open(os.path.join(tmp, "runs", "a.csv"), "w") as f:
        f.write("ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg\n")
        f.write("2026-08-15T00:00:00Z,1,BUY,FILLED,100,101,0.01,1.0,0.01,win_reason,6,radar=long\n")
        f.write("2026-08-15T00:01:00Z,2,BUY,FILLED,100,99,0.01,-1.0,-0.01,stop_reason,7,size_note=hunter_revenge_1.5x\n")

    snap = build_snapshot()
    check("snapshot ace.alpha.pnl_session == 1.0", snap["ace"]["alpha"]["pnl_session"] == 1.0)
    check("snapshot ace.alpha.recent win=1", snap["ace"]["alpha"]["recent"]["win"] == 1)
    check("snapshot ace.alpha.recent revenge=1", snap["ace"]["alpha"]["recent"]["revenge"] == 1)
    check("snapshot hulk veille RED=1", snap["hulk"]["veille"]["RED"] == 1)
    check("snapshot marche voilure 87.9", snap["marche"]["voilure"] == 87.9)
    check("snapshot saison CALME", snap["marche"]["saison"] == "CALME")
    path = save_snapshot(snap)
    check("snapshot écrit", os.path.exists(path))

    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    restore()
    print("=== %s (%d erreur%s) ===" % (
        "TOUS LES TESTS SONT VERTS" if errors == 0 else "ÉCHEC",
        errors, "s" if errors > 1 else ""))
    return 0 if errors == 0 else 1


def main():
    ap = argparse.ArgumentParser(description="Cortana dashboard (ACE+Hulk+marché)")
    ap.add_argument("--speak", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()

    if a.test:
        sys.exit(run_tests())

    snapshot = build_snapshot()
    path = save_snapshot(snapshot)
    print(f"[snapshot] {path}", file=sys.stderr)

    if a.json:
        print(json.dumps(snapshot, ensure_ascii=False, indent=2))
        return 0

    try:
        content, provider = ask_hub(snapshot, load_identity())
    except Exception as e:
        print(f"✘ hub injoignable : {e} — snapshot seul disponible", file=sys.stderr)
        print(json.dumps(snapshot, ensure_ascii=False, indent=2))
        return 1

    print(f"[provider: {provider}]", file=sys.stderr)
    print(content)
    if a.speak:
        speak_text(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
