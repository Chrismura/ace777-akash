#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P1b SCORER SYSTÉMATIQUE — bac à sable (29/10/2026, GO Christophe).

Problème P1 : 839 suivis, 20 scorés (2,4 %), aucun ts→issue → M1 non actionnable.
Ce scorer : (1) snapshotte chaque run d'analyse en journal append-only /tmp,
(2) résout les appels directionnels vieux de 24 h+ contre le prix BTC,
(3) sort la table régime→accuracy.

Règles de résolution PRÉ-DÉCLARÉES (pas inventées au moment du verdict) :
- direction : niveau critique/dangereux → baissier ; haussier → haussier ;
  neutre/inconnu → non scorable (compté à part, exclu de H1).
- hit : |move24| ≥ 0,3 % dans le bon sens (seuil_move_pct de justesse_v2, relu).
- horizon : 24 h (même que fade_ombre, comparabilité).
LECTURE SEULE maison. Écritures : /tmp uniquement. 0 ordre, 0 réseau.
"""
import json
import glob as _glob
from pathlib import Path

HULK = Path(__file__).resolve().parents[1]
MAISON = HULK.parent / "Index_Maison"
RUNS = HULK / "runs"
ANALYSIS = MAISON / "data" / "cortana_analysis.json"
JOURNAL = RUNS / "sandbox_cortana_scores.jsonl"  # DURCI 29/10 : /tmp est vidé au reboot
# → une semaine d'accumulation ne doit pas mourir avec un redémarrage.
# Fichier NEUF namespacé sandbox_ : le moteur ne le lit jamais (0 effet live).
OUT = Path("/tmp/SELF_MODEL_P1B.json")

H_H = 24.0
SEUIL_MOVE = 0.3  # relu dans justesse_v2.seuil_move_pct — jamais recopié en dur ailleurs
BEARISH = {"critique", "dangereux"}
BULLISH = {"haussier"}


def direction_de(niveau):
    if niveau in BEARISH:
        return "bearish"
    if niveau in BULLISH:
        return "bullish"
    return None


def charger_journal():
    rows = []
    if JOURNAL.exists():
        for l in JOURNAL.read_text(encoding="utf-8").splitlines():
            l = l.strip()
            if l:
                try:
                    rows.append(json.loads(l))
                except Exception:
                    pass
    return rows


def snapshot():
    """Ajoute le run courant au journal (dedupe ts+fiche). Retourne (ajoutés, lus)."""
    try:
        d = json.loads(ANALYSIS.read_text(encoding="utf-8"))
    except Exception as e:
        return 0, f"lecture analysis impossible : {e}"
    run_ts = d.get("timestamp") or d.get("date")
    existentes = set()
    for r in charger_journal():
        existentes.add((str(r.get("ts_run")), str(r.get("fiche"))))
    ajoutes = 0
    with open(JOURNAL, "a", encoding="utf-8") as f:
        for a in d.get("analyses", []):
            fiche = a.get("fiche")
            inter = a.get("interpretation") or {}
            niveau = inter.get("niveau")
            cle = (str(run_ts), str(fiche))
            if cle in existentes:
                continue
            sig = a.get("signal") or {}
            f.write(json.dumps({
                "ts_run": run_ts,
                "fiche": fiche,
                "niveau": niveau,
                "direction": direction_de(niveau),
                "action": a.get("action"),
                "signal_metric": (sig.get("metric") if isinstance(sig, dict) else None),
                "signal_ts": (sig.get("ts") if isinstance(sig, dict) else None),
                "issue": None,
            }, ensure_ascii=False) + "\n")
            ajoutes += 1
    return ajoutes, f"{len(d.get('analyses', []))} analyses lues"


def _to_epoch(ts):
    """Normalise float epoch ou ISO (miroir analyzer.load_signals — un signal
    en ISO ne doit jamais être silencieusement ignoré)."""
    if ts is None:
        return 0
    if isinstance(ts, (int, float)):
        return float(ts)
    try:
        from datetime import datetime as _dt
        return _dt.fromisoformat(str(ts)).timestamp()
    except Exception:
        return 0


def prix_btc():
    """Série (ts, prix) BTC du flux, live + archives (borné, même méthode que short_btc)."""
    import gzip as _gzip
    pts = []
    arch = sorted(_glob.glob(str(RUNS / "croisement_contexte.jsonl.*.gz")))
    for path in arch + [str(RUNS / "croisement_contexte.jsonl")]:
        try:
            op = _gzip.open if path.endswith(".gz") else open
            with op(path, "rt", encoding="utf-8", errors="ignore") as f:
                for l in f:
                    l = l.strip()
                    if not l:
                        continue
                    try:
                        r = json.loads(l)
                    except Exception:
                        continue
                    if r.get("pair") == "BTCUSDT" and r.get("ts") and r.get("price"):
                        try:
                            pts.append((float(r["ts"]), float(r["price"])))
                        except (TypeError, ValueError):
                            pass
        except FileNotFoundError:
            pass
    pts.sort()
    return pts


def prix_a(pts, ts):
    """Dernier prix connu à ts (pas de futur)."""
    best = None
    for t, p in pts:
        if t <= ts:
            best = p
        else:
            break
    return best


def resoudre():
    """Résout les entrées directionnelles vieilles de 24 h+ sans issue."""
    import time
    rows = charger_journal()
    if not rows:
        return {"resolus": 0, "note": "journal vide"}
    pts = prix_btc()
    if not pts:
        return {"resolus": 0, "note": "pas de prix"}
    now = time.time()
    resolus = 0
    for r in rows:
        if r.get("issue") is not None or not r.get("direction"):
            continue
        ts = _to_epoch(r.get("signal_ts"))
        if not ts:
            r["issue"] = "ts_illisible"  # jamais d'accumulation silencieuse
            continue
        if now - ts < H_H * 3600:
            continue
        p0 = prix_a(pts, ts)
        p1 = prix_a(pts, ts + H_H * 3600)
        if not p0 or not p1:
            r["issue"] = "prix_indisponible"
            continue
        move = 100.0 * (p1 / p0 - 1)
        r["move24_pct"] = round(move, 3)
        if r["direction"] == "bearish":
            r["hit"] = bool(move <= -SEUIL_MOVE)
        else:
            r["hit"] = bool(move >= SEUIL_MOVE)
        r["issue"] = "hit" if r["hit"] else "miss"
        resolus += 1
    JOURNAL.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                       encoding="utf-8")
    return {"resolus": resolus}


def regime_simple(pts, ts):
    try:
        p0 = prix_a(pts, float(ts))
        p1 = prix_a(pts, float(ts) - 24 * 3600)
    except (TypeError, ValueError):
        return "inconnu"
    if not p0 or not p1:
        return "inconnu"
    chg = 100.0 * (p0 / p1 - 1)
    if chg > 1.5:
        return "bull"
    if chg < -1.5:
        return "bear"
    return "range"


def main():
    ajoutes, note = snapshot()
    reso = resoudre()
    rows = charger_journal()
    pts = prix_btc()
    table = {r: {"n": 0, "hit": 0} for r in ("bull", "bear", "range", "inconnu")}
    n_dir = n_nondir = n_attente = 0
    for r in rows:
        if not r.get("direction"):
            n_nondir += 1
            continue
        if r.get("issue") in ("hit", "miss"):
            reg = regime_simple(pts, r.get("signal_ts") or 0)
            table[reg]["n"] += 1
            table[reg]["hit"] += 1 if r["issue"] == "hit" else 0
            n_dir += 1
        else:
            n_attente += 1
    for v in table.values():
        v["acc_pct"] = round(100.0 * v["hit"] / v["n"], 1) if v["n"] else None
        v["actionnable"] = v["n"] >= 10
    out = {
        "snapshot_ajoutes": ajoutes, "snapshot_note": note,
        "resolution": reso,
        "journal_total": len(rows),
        "directionnels_resolus": n_dir,
        "non_directionnels": n_nondir,
        "en_attente_24h": n_attente,
        "table_regime": table,
        "journal": str(JOURNAL),
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    lignes = ["# P1b SCORER — résultat",
              f"- snapshot : +{ajoutes} ({note})",
              f"- résolus ce run : {reso}",
              f"- journal : {len(rows)} entrées ({n_dir} directionnelles résolues, "
              f"{n_nondir} non directionnelles, {n_attente} en attente des 24 h)",
              "", "| régime | n | hit | acc | actionnable |",
              "|---|---|---|---|---|"]
    for reg, v in table.items():
        lignes.append(f"| {reg} | {v['n']} | {v['hit']} | {v['acc_pct']} | "
                      f"{'OUI' if v['actionnable'] else 'NON'} |")
    if n_attente or ajoutes:
        lignes += ["", "Prochain run dans 24 h+ : les entrées en attente seront résolues, "
                   "n grandira à chaque run (5 min si branché)."]
    print("\n".join(lignes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
