#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
journal_intention.py
Couche de lecture qui transforme les CSV des bots (Alpha/Beta) en journal d'intention.
Sorties :
  - journal_intention.jsonl         (append-only, un événement JSON par ligne)
  - journal_intention_live.json     (résumé vivant + story française)
  - journal_intention.cursor.json   (curseur incrémental)

Python 3.9 - stdlib uniquement. NE TOUCHE PAS au moteur (.rb/.sh).
Usage :
  python3 journal_intention.py            -> scan incrémental
  python3 journal_intention.py --runs DIR -> scan sur un dossier précis (tests archives)
  python3 journal_intention.py --story    -> affiche la story courante
  python3 journal_intention.py --test     -> auto-test sur échantillons réels
"""

import csv
import json
import re
import os
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any, List, Tuple

# === CONSTANTES (modifiables facilement) ===
RUNS = Path(os.path.expanduser("~")) / "ace777-test-day1" / "runs"
STRATEGIE = Path(os.path.expanduser("~")) / "ace777-test-day1" / "Index_Maison" / "strategie"
OUT_JSONL = STRATEGIE / "journal_intention.jsonl"
OUT_LIVE = STRATEGIE / "journal_intention_live.json"
CURSOR = STRATEGIE / "journal_intention.cursor.json"
MISSION = Path(os.path.expanduser("~")) / "ace777-test-day1" / "Index_Maison" / "cockpit" / "mission.json"

ROLES = {
    "alpha": {
        "surnom": "Le Sniper",
        "role": "Tire juste, seul ou sur signal de Beta",
        "mesure": "precision des fills, pas le volume",
    },
    "beta": {
        "surnom": "L'Eclaireur",
        "role": "Sonde le marche et renseigne Alpha",
        "mesure": "qualite des infos transmises, PAS son PnL",
    },
}

MSG_REGEX = re.compile(r"(\w+)=([^\s]+)")

EXIT_MAP = {
    "shock_inversion_stop": "sortie — retournement choc",
    "fluid_exit_inversion": "sortie — inversion fluide",
    "trailing_stop": "sortie — trailing (laisser courir)",
    "fluid_exit_brake": "sortie — frein",
    "stop_loss": "sortie — stop loss",
    "shock_exit_10bps": "sortie — 10 bps",
}


def atomic_write_json(path: Path, data: Dict[str, Any]) -> None:
    """Écriture atomique : tmp puis os.replace."""
    tmp = path.with_suffix(".tmp")
    try:
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(str(tmp), str(path))
    except Exception:
        if tmp.exists():
            try:
                tmp.unlink()
            except Exception:
                pass


def read_cursor() -> Dict[str, int]:
    if not CURSOR.exists():
        return {}
    try:
        return json.loads(CURSOR.read_text(encoding="utf-8"))
    except Exception:
        return {}


def write_cursor(cursor: Dict[str, int]) -> None:
    try:
        CURSOR.parent.mkdir(parents=True, exist_ok=True)
        CURSOR.write_text(json.dumps(cursor, indent=2), encoding="utf-8")
    except Exception:
        pass


def freshest() -> Tuple[Optional[Path], Optional[Path]]:
    """Retourne la paire (alpha_csv, beta_csv) la plus récente.
    Critère : le min(mtime_alpha, mtime_beta) le plus grand (paire cohérente)."""
    try:
        candidates = list(RUNS.glob("*.csv"))
    except Exception:
        return None, None
    alpha_files = [f for f in candidates if "ALPHA" in f.name.upper()]
    beta_files = [f for f in candidates if "BETA" in f.name.upper()]
    if not alpha_files or not beta_files:
        return None, None
    best_pair = None
    best_min_m = 0.0
    for a in alpha_files:
        for b in beta_files:
            try:
                min_m = min(a.stat().st_mtime, b.stat().st_mtime)
                if min_m > best_min_m:
                    best_min_m = min_m
                    best_pair = (a, b)
            except Exception:
                continue
    return best_pair if best_pair else (None, None)


def parse_msg(msg: str) -> Dict[str, Any]:
    """Extrait les clés du champ msg."""
    result: Dict[str, Any] = {
        "radar": None, "conf": None, "size_note": None,
        "tension": None, "bid_drop": None, "ask_drop": None,
        "swarm": None, "mode_revenge": False, "aspiration": False,
        "reason": None,
    }
    if not msg:
        return result
    try:
        for m in MSG_REGEX.finditer(msg):
            key = m.group(1).lower()
            val = m.group(2)
            if key == "radar":
                result["radar"] = val.lower() if val else None
            elif key == "conf":
                try:
                    result["conf"] = float(val)
                except Exception:
                    pass
            elif key == "size_note":
                result["size_note"] = val
                if val:
                    result["mode_revenge"] = "revenge" in val.lower()
                    result["aspiration"] = "aspiration" in val.lower()
            elif key in ("tension", "bid_drop", "ask_drop", "swarm"):
                try:
                    result[key] = float(val)
                except Exception:
                    pass
            elif key == "reason":
                result["reason"] = val
    except Exception:
        pass
    return result


def parse_row(line: str) -> Optional[Dict[str, Any]]:
    """Parse UNE ligne CSV de façon robuste (11 ou 12 champs, sans quotes)."""
    try:
        parts = next(csv.reader([line]))
    except Exception:
        return None
    if len(parts) < 10:
        return None
    msg = " ".join(parts[10:]) if len(parts) > 10 else ""
    row = {
        "ts": parts[0],
        "cycle": parts[1],
        "side": parts[2],
        "status": parts[3].upper(),
        "pnl": 0.0,
        "exitReason": parts[9] if len(parts) > 9 else "",
    }
    try:
        row["pnl"] = float(parts[8]) if parts[8] not in ("", "None") else 0.0
    except Exception:
        pass
    row.update(parse_msg(msg))
    return row


def classify(row: Dict[str, Any], bot: str) -> Tuple[str, str, str]:
    """Retourne (action, intention, exit_label)."""
    status = (row.get("status") or "").upper()
    exit_reason = (row.get("exitReason") or "").lower()
    parsed = row  # row contient déjà les clés parse_msg

    if status == "SKIPPED":
        if "impulse_resonance_wait" in exit_reason:
            return "wait", "attente — mur du carnet intact", EXIT_MAP.get(exit_reason, exit_reason)
        if "radar_block" in exit_reason:
            return "skip", "pas d'opportunite — discipline (radar bloque)", EXIT_MAP.get(exit_reason, exit_reason)
        if "duo_wait" in exit_reason:
            return "wait", "attente de l'etat du duo (Beta)", EXIT_MAP.get(exit_reason, exit_reason)
        return "skip", "skip — %s" % exit_reason, EXIT_MAP.get(exit_reason, exit_reason)

    if status == "FILLED":
        if bot == "alpha":
            if parsed.get("mode_revenge"):
                return "fire", "a tire en mode revenge 1.5x", EXIT_MAP.get(exit_reason, exit_reason)
            return "fire", "a frappe en embuscade (13x)", EXIT_MAP.get(exit_reason, exit_reason)
        return "probe", "a sonde le marche", EXIT_MAP.get(exit_reason, exit_reason)

    return "skip", "statut inconnu", EXIT_MAP.get(exit_reason, exit_reason)


def session_since(force: Optional[str] = None) -> str:
    """Retourne un ts ISO-UTC (format 'YYYY-MM-DDTHH:MM:SSZ') : force si fourni,
    sinon sessionSince de mission.json, sinon -24h."""
    if force:
        force = force.replace("+00:00", "Z")
        if not force.endswith("Z"):
            force += "Z"
        m = re.match(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})(:\d{2})?Z$", force)
        if m:
            return m.group(1) + (m.group(2) or ":00") + "Z"
        return force
    try:
        if MISSION.exists():
            d = json.loads(MISSION.read_text(encoding="utf-8"))
            s = d.get("sessionSince")
            if s:
                s = str(s).replace("+00:00", "Z")
                if not s.endswith("Z"):
                    s += "Z"
                # normalise les secondes (mission.json peut donner 2026-08-02T00:00Z)
                m = re.match(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})(:\d{2})?Z$", s)
                if m:
                    return m.group(1) + (m.group(2) or ":00") + "Z"
    except Exception:
        pass
    past = datetime.now(timezone.utc) - timedelta(hours=24)
    return past.strftime("%Y-%m-%dT%H:%M:%SZ")


def aggregate(csv_path: Path, bot: str, since: str) -> Dict[str, Any]:
    """Lit le CSV et agrège la session (ts >= since). Renvoie compteurs + stats."""
    agg = {
        "role": "sniper" if bot == "alpha" else "eclaireur",
        "surnom": ROLES[bot]["surnom"],
        "fills": 0, "skips": 0, "pnl": 0.0, "best": 0.0, "conf_moy": 0.0,
        "events": [], "counts": {"wait": 0, "fire": 0, "probe": 0, "skip": 0},
        "direction": {"long": 0, "short": 0}, "revenge": 0,
        "_confs": [],
    }
    try:
        with csv_path.open("r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception:
        return agg
    if not lines:
        return agg
    # sauter la ligne d'en-tête
    body = lines[1:] if lines[0].lower().startswith("ts,") else lines
    for line in body:
        line = line.strip()
        if not line:
            continue
        row = parse_row(line)
        if not row:
            continue
        if since and row["ts"] < since:
            continue
        action, intention, exit_label = classify(row, bot)
        if action in ("fire", "probe"):
            agg["fills"] += 1
            agg["pnl"] += row.get("pnl") or 0.0
            if row.get("pnl") and row["pnl"] > agg["best"]:
                agg["best"] = row["pnl"]
            if row.get("mode_revenge"):
                agg["revenge"] += 1
            if row.get("conf") is not None:
                agg["_confs"].append(row["conf"])
        elif action == "wait":
            pass  # compté une seule fois via counts[action] ci-dessous
        else:
            agg["skips"] += 1
        # UN SEUL point de comptage (pas de double incrément)
        agg["counts"][action] = agg["counts"].get(action, 0) + 1
        d = row.get("radar")
        if d in ("long", "short"):
            agg["direction"][d] += 1
        # conserver les 20 derniers événements de la session
        ev = {
            "ts": row["ts"], "bot": bot, "cycle": 0, "action": action,
            "intention": intention, "direction": d,
            "conf": row.get("conf"), "exit": exit_label,
            "meta": {"size_note": row.get("size_note"), "tension": row.get("tension")},
            "file": csv_path.name,
        }
        try:
            ev["cycle"] = int(row["cycle"]) if str(row["cycle"]).isdigit() else 0
        except Exception:
            pass
        agg["events"].append(ev)
        if len(agg["events"]) > 20:
            agg["events"] = agg["events"][-20:]
    if agg["_confs"]:
        agg["conf_moy"] = sum(agg["_confs"]) / len(agg["_confs"])
    agg.pop("_confs", None)
    return agg


def build_story(live: Dict[str, Any]) -> List[str]:
    """Construit 3-5 phrases françaises déterministes (jamais de jugement sur le PnL de Beta)."""
    story: List[str] = []
    alpha = live.get("bots", {}).get("alpha", {})
    beta = live.get("bots", {}).get("beta", {})

    # --- Beta : les sondes, pas le PnL ---
    beta_sondes = beta.get("fills", 0)
    beta_long = beta.get("direction", {}).get("long", 0)
    beta_short = beta.get("direction", {}).get("short", 0)
    beta_conf = beta.get("conf_moy", 0.0)
    if beta_sondes > 0:
        story.append(
            "BETA a sonde le marche (%d sondes, %d long / %d court, conf moyenne %.2f) — il renseigne Alpha."
            % (beta_sondes, beta_long, beta_short, beta_conf)
        )
    else:
        story.append("BETA veille — pas encore de sonde sur la session en cours.")

    # --- Alpha : patience, puis frappe ---
    alpha_skips = alpha.get("skips", 0)
    alpha_fills = alpha.get("fills", 0)
    alpha_revenge = alpha.get("revenge", 0)
    alpha_pnl = alpha.get("pnl", 0.0)
    alpha_best = alpha.get("best", 0.0)
    if alpha_skips > 50:
        story.append(
            "ALPHA attend son moment : %d skips (discipline), le mur du carnet ne s'effondre pas."
            % alpha_skips
        )
    if alpha_fills > 0:
        rev = " (dont %d en mode revenge 1.5x)" % alpha_revenge if alpha_revenge > 0 else ""
        if alpha_best > 0:
            story.append(
                "ALPHA a frappe %d fois en embuscade (13x)%s : %+.2f $, meilleur trade %+.2f $."
                % (alpha_fills, rev, alpha_pnl, alpha_best)
            )
        else:
            story.append(
                "ALPHA a frappe %d fois en embuscade (13x)%s : %+.2f $ — session difficile, tous les tirs dans le rouge."
                % (alpha_fills, rev, alpha_pnl)
            )
    else:
        story.append("ALPHA attend son signal — aucun tir sur la session en cours.")
    return story[:5]


def scan(runs_dir: Optional[Path] = None, since_override: Optional[str] = None) -> None:
    global RUNS, OUT_JSONL, OUT_LIVE, CURSOR
    if runs_dir:
        # Mode test/archive : ne JAMAIS toucher aux sorties de production
        RUNS = runs_dir
        test_dir = Path("/tmp") / "journal_intention_test"
        test_dir.mkdir(parents=True, exist_ok=True)
        OUT_JSONL = test_dir / "journal_intention.jsonl"
        OUT_LIVE = test_dir / "journal_intention_live.json"
        CURSOR = test_dir / "journal_intention.cursor.json"
    STRATEGIE.mkdir(parents=True, exist_ok=True)

    since = session_since(since_override)
    alpha_csv, beta_csv = freshest()
    if not alpha_csv or not beta_csv:
        print("Aucun CSV Alpha/Beta trouve dans %s" % RUNS)
        return

    cursor = read_cursor()
    new_events = []
    for csv_path in (alpha_csv, beta_csv):
        bot = "alpha" if "ALPHA" in csv_path.name.upper() else "beta"
        last_pos = cursor.get(str(csv_path), 0)
        try:
            with csv_path.open("r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception:
            continue
        total = len(lines)
        start = (total - 500) if (last_pos == 0 and total > 500) else last_pos
        for i in range(start, total):
            line = lines[i].strip()
            if not line or i == 0 and line.lower().startswith("ts,"):
                continue
            row = parse_row(line)
            if not row:
                continue
            action, intention, exit_label = classify(row, bot)
            event = {
                "ts": row["ts"], "bot": bot,
                "cycle": int(row["cycle"]) if str(row["cycle"]).isdigit() else 0,
                "action": action, "intention": intention,
                "direction": row.get("radar"), "conf": row.get("conf"),
                "exit": exit_label,
                "meta": {"size_note": row.get("size_note"), "tension": row.get("tension")},
                "file": csv_path.name,
            }
            try:
                with OUT_JSONL.open("a", encoding="utf-8") as jf:
                    jf.write(json.dumps(event, ensure_ascii=False) + "\n")
            except Exception:
                pass
            new_events.append(event)
        cursor[str(csv_path)] = total
    write_cursor(cursor)

    # --- Live : agrégation complète de la session (pas seulement les nouveaux events) ---
    live = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "since": since,
        "bots": {
            "alpha": aggregate(alpha_csv, "alpha", since),
            "beta": aggregate(beta_csv, "beta", since),
        },
        "story": [],
    }
    live["story"] = build_story(live)
    atomic_write_json(OUT_LIVE, live)
    print("Scan termine : %d nouveaux evenements (session depuis %s)" % (len(new_events), since))


def run_test() -> int:
    """Tests intégrés sur échantillons réels de la session du 27/07."""
    samples = [
        # ALPHA FILLED normal (attendu: fire, long, conf 0.8881, pas revenge)
        "2026-07-27T12:03:29Z,165,BUY,FILLED,65107.30000000,65130.00000000,0.15970000,3.48655220,3.62519000,shock_inversion_stop,radar=long conf=0.8881 size_note=strong_conf_full+entry_25_75_full soft=0 pct=0.03486552 tension=7.56251398 bid_drop=0.00000000 ask_drop=49.15634089",
        # ALPHA revenge (attendu: fire + revenge)
        "2026-07-27T12:40:11Z,381,BUY,FILLED,64950.60000000,64969.00000000,0.12000000,2.83292225,2.20800000,shock_inversion_stop,radar=long conf=0.9819 size_note=hunter_revenge_1.5x+entry_25_75_full soft=1 pct=0.02832922 tension=4.23002247 bid_drop=0.00026084 ask_drop=27.49514607",
        # ALPHA wait (attendu: wait + 'mur' dans l'intention)
        "2026-07-27T11:37:15Z,1,SKIP,SKIPPED,,,,,0,impulse_resonance_wait,reason=wall_not_collapsed tension=0.83114663 bid_drop=0.00339558 ask_drop=5.40245308",
        # ALPHA skip radar_block (attendu: skip, pas de radar dans le msg)
        "2026-07-27T11:37:28Z,2,SKIP,SKIPPED,,,,,0,radar_block,reason=momentum_too_small conf=0.2869 mom_sig=0.00000000 raw_mom_bps=0.00000000 spread_bps=2.88520000 tension=0.00000000 bid_drop=0.00000000 ask_drop=0.00000000 swarm=0",
        # BETA probe short (attendu: probe + short)
        "2026-07-27T12:32:51Z,344,SELL,FILLED,64964.90000000,64918.30000000,0.00760000,7.17310425,0.35416000,shock_inversion_stop,radar=short conf=0.976 size_note=strong_conf_full+entry_25_75_full soft=1 pct=0.07173104 tension=5.73367133 bid_drop=37.26886367 ask_drop=0.04415790",
    ]
    errors = 0

    def check(name, cond):
        nonlocal errors
        if cond:
            print("OK  %s" % name)
        else:
            print("FAIL %s" % name)
            errors += 1

    r = parse_row(samples[0])
    a, i, e = classify(r, "alpha")
    check("alpha fire normal (long, conf 0.8881, pas revenge)",
          a == "fire" and r["radar"] == "long" and r["conf"] == 0.8881 and not r["mode_revenge"]
          and "embuscade" in i)

    r = parse_row(samples[1])
    a, i, e = classify(r, "alpha")
    check("alpha fire revenge 1.5x detecte", a == "fire" and r["mode_revenge"] and "revenge" in i and "1.5x" in i)

    r = parse_row(samples[2])
    a, i, e = classify(r, "alpha")
    check("alpha wait mur du carnet", a == "wait" and "mur" in i)

    r = parse_row(samples[3])
    a, i, e = classify(r, "alpha")
    check("alpha skip discipline (radar absent du msg)",
          a == "skip" and r["conf"] == 0.2869)

    r = parse_row(samples[4])
    a, i, e = classify(r, "beta")
    check("beta probe short", a == "probe" and r["radar"] == "short")

    # Test 6 : pas de double comptage des wait/skip dans aggregate
    import tempfile
    tmpd = Path(tempfile.mkdtemp())
    small = tmpd / "T_ALPHA_X13_BURST13.csv"
    small.write_text(
        "ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg\n"
        "2026-07-27T11:00:00Z,1,SKIP,SKIPPED,,,,,0,radar_block,reason=momentum_too_small\n"
        "2026-07-27T11:00:01Z,2,SKIP,SKIPPED,,,,,0,impulse_resonance_wait,reason=wall_not_collapsed\n"
        "2026-07-27T11:00:02Z,3,BUY,FILLED,100,101,1,10,1.0,shock_inversion_stop,radar=long conf=0.9\n",
        encoding="utf-8",
    )
    agg = aggregate(small, "alpha", "2026-07-27T00:00:00Z")
    check("aggregate sans double comptage",
          agg["counts"] == {"wait": 1, "fire": 1, "probe": 0, "skip": 1}
          and agg["fills"] == 1 and agg["skips"] == 1 and agg["pnl"] == 1.0)

    # Test story : une beta remplie -> pas de jugement PnL
    live = {"bots": {
        "alpha": {"fills": 2, "skips": 310, "pnl": 26.77, "best": 51.56, "revenge": 1, "events": [], "direction": {"long": 1, "short": 1}},
        "beta": {"fills": 191, "skips": 2463, "pnl": 5.66, "best": 1.58, "revenge": 0, "conf_moy": 0.9,
                 "events": [{"conf": 0.88}, {"conf": 0.92}], "direction": {"long": 97, "short": 94}},
    }}
    story = build_story(live)
    check("story Beta = sondes (191), pas son PnL",
          any("191 sondes" in s for s in story) and not any("5.66" in s for s in story))
    check("story Alpha = frappe + pnl + revenge",
          any("2 fois" in s and "+26.77" in s and "revenge" in s for s in story))

    return 0 if errors == 0 else 1


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Journal d'intention des bots")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--story", action="store_true")
    parser.add_argument("--runs", type=str, default=None)
    parser.add_argument("--since", type=str, default=None,
                        help="Force le debut de session (ISO UTC), ex: 2026-07-27T00:00:00Z")
    args = parser.parse_args()

    if args.test:
        sys.exit(run_test())
    if args.story:
        if OUT_LIVE.exists():
            try:
                data = json.loads(OUT_LIVE.read_text(encoding="utf-8"))
                for line in data.get("story", []):
                    print(line)
            except Exception:
                print("Impossible de lire le live.json")
        else:
            print("Aucun live.json disponible.")
        return
    scan(Path(args.runs) if args.runs else None, args.since)


if __name__ == "__main__":
    main()
