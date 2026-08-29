"""
Rôle : Helper et CLI pour analyser le PnL réel du moteur Hulk (PAPER), sans le
double-comptage induit par les copies --resume. Codé par le CODEUR (task code.ia,
29/08), intégré et testé par Buffy — la correction d'intégration porte sur le
mapping des colonnes réelles (ts, pair, event, pnl_usdt) et l'ajout du mode
HISTORIQUE (--all), indispensable quand la chaîne --resume se casse.

DEUX MODES :
  - défaut           : lit le DERNIER run seul (contrôle rapide du run actif).
  - --all            : concatène TOUS les runs et déduplique par (ts, pair, event)
                       → le PnL HISTORIQUE fiable sur 36 jours. C'est le mode de
                       référence pour un audit (la chaîne --resume peut se casser :
                       un run relancé à vide ne remonte pas dans le passé).

Stdlib uniquement, compatible Python 3.9+, robuste et non fatal.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Dict, List

# Colonnes RÉELLES du moteur (PAPER_V1_*.csv) — vérifiées sur un vrai run.
COL_TS = "ts"
COL_PAIR = "pair"
COL_EVENT = "event"
COL_PNL = "pnl_usdt"


def all_paper_csvs(root: Path) -> List[Path]:
    """Tous les CSV PAPER_V1_*.csv de runs/, triés par timestamp du nom
    (les copies --resume gardent le mtime, donc on ne trie PAS par mtime)."""
    runs_dir = root / "runs"
    if not runs_dir.exists() or not runs_dir.is_dir():
        return []
    csvs = list(runs_dir.glob("PAPER_V1_*.csv"))

    def extract_ts(path: Path) -> str:
        name = path.stem
        numeric = [p for p in name.split("_") if p.isdigit()]
        return "".join(numeric) if numeric else name

    return sorted(csvs, key=extract_ts)


def recent_paper_csv(root: Path) -> Path | None:
    """Le CSV PAPER_V1 le plus récent par timestamp du nom."""
    csvs = all_paper_csvs(root)
    return csvs[-1] if csvs else None


def trades(df_path: Path) -> List[Dict[str, str]]:
    """Parse UN CSV, dédoublonne par (ts, pair, event), garde la première occ."""
    if not df_path.exists():
        return []
    lignes: List[Dict[str, str]] = []
    try:
        with open(df_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lignes.append(row)
    except Exception as e:
        print(f"[ERREUR] Lecture impossible de {df_path} : {e}", file=sys.stderr)
        return []
    return _dedup(lignes)


def trades_all(root: Path) -> List[Dict[str, str]]:
    """Concatène TOUS les runs puis déduplique par (ts, pair, event)."""
    tous: List[Dict[str, str]] = []
    for p in all_paper_csvs(root):
        try:
            with open(p, mode="r", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    tous.append(row)
        except Exception as e:
            print(f"[ERREUR] Lecture impossible de {p} : {e}", file=sys.stderr)
            continue
    return _dedup(tous)


def _dedup(lignes: List[Dict[str, str]]) -> List[Dict[str, str]]:
    vus = set()
    out = []
    for row in lignes:
        ts = row.get(COL_TS) or ""
        pair = row.get(COL_PAIR) or ""
        event = row.get(COL_EVENT) or ""
        cle = (ts, pair, event)
        if cle not in vus:
            vus.add(cle)
            out.append(row)
    return out


def pnl_par_pair(lignes: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    """PnL par paire : pnl_usdt moteur déjà net de commission. Sépare SELL
    (full) et SELL_PARTIAL."""
    resultats: Dict[str, Dict[str, float]] = {}
    for row in lignes:
        pair = row.get(COL_PAIR)
        event = (row.get(COL_EVENT) or "").upper()
        if not pair or not event:
            continue
        if pair not in resultats:
            resultats[pair] = {
                "pnl_sell_full": 0.0,
                "pnl_sell_partial": 0.0,
                "pnl_total": 0.0,
            }
        try:
            pnl = float(row.get(COL_PNL, 0.0) or 0.0)
        except ValueError:
            pnl = 0.0
        if event == "SELL":
            resultats[pair]["pnl_sell_full"] += pnl
            resultats[pair]["pnl_total"] += pnl
        elif event == "SELL_PARTIAL":
            resultats[pair]["pnl_sell_partial"] += pnl
            resultats[pair]["pnl_total"] += pnl
    return resultats


def _affiche(stats: Dict[str, Dict[str, float]], target_pair) -> None:
    grand_total = 0.0
    for pair, data in sorted(stats.items()):
        if target_pair and pair != target_pair:
            continue
        tot = data["pnl_total"]
        grand_total += tot
        print(f"  {pair:<12} | Full: {data['pnl_sell_full']:>8.2f}$ | "
              f"Partial: {data['pnl_sell_partial']:>8.2f}$ | Total: {tot:>8.2f}$")
    print("-" * 42)
    print(f"  {'GRAND TOTAL':<12} | {grand_total:>31.2f}$")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    target_pair = None
    all_mode = "--all" in sys.argv
    if "--pair" in sys.argv:
        try:
            target_pair = sys.argv[sys.argv.index("--pair") + 1].upper()
        except (IndexError, ValueError):
            pass

    if all_mode:
        tous = all_paper_csvs(root)
        if not tous:
            print("[INFO] Aucun fichier PAPER_V1_*.csv trouvé dans runs/.")
            sys.exit(0)
        lignes = trades_all(root)
        print("--- ANALYSE HISTORIQUE (tous les runs, dédupliqués) ---")
        print(f"Runs lus : {len(tous)} | lignes dédoublonnées : {len(lignes)}")
        _affiche(pnl_par_pair(lignes), target_pair)
        return

    csv_path = recent_paper_csv(root)
    if not csv_path:
        print("[INFO] Aucun fichier PAPER_V1_*.csv trouvé dans runs/.")
        sys.exit(0)
    print("--- ANALYSE DU DERNIER RUN PAPER ---")
    print(f"Fichier cible : {csv_path.name}")
    lignes = trades(csv_path)
    print(f"Lignes dédoublonnées : {len(lignes)}")
    _affiche(pnl_par_pair(lignes), target_pair)


if __name__ == "__main__":
    main()