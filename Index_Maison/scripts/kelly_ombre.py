#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kelly fractionnaire 1/4 en mode OMBRE (sizing Hulk)
Calcule et affiche le Kelly sans rien modifier (mode observation pur).
Conforme spec ACE777 - 15/08/2026. Chantier 3 (Burry N°43 + Saint-Pétersbourg N°105).
"""

from pathlib import Path
import json
import csv
import glob
from datetime import datetime
import sys

# Racine globale : Index_Maison/scripts/kelly_ombre.py -> parent.parent.parent = ace777-test-day1
ROOT_GLOBAL = Path(__file__).resolve().parent.parent.parent

JUSTESSE_JSON = ROOT_GLOBAL / "Index_Maison" / "scripts" / "justesse_v2.json"
HULK_RUNS_DIR = ROOT_GLOBAL / "hulk-mexc" / "runs"
KELLY_JSON = ROOT_GLOBAL / "hulk-mexc" / "strategie" / "kelly_ombre.json"
KELLY_MD = ROOT_GLOBAL / "hulk-mexc" / "runs" / "KELLY_OMBRE.md"


def get_justesse_cortana():
    """Lit la justesse Cortana (pct) depuis justesse_v2.json (fail-open -> 0.0)."""
    try:
        if JUSTESSE_JSON.exists():
            with open(JUSTESSE_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
                return float(data.get("pct", 0.0))
    except Exception:
        pass
    return 0.0


def _trades_du_csv(csv_path):
    """Extrait les PnL des sorties d'un CSV donné (liste vide si aucune sortie)."""
    trades_pnl = []
    try:
        with open(csv_path, mode="r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            for row in reader:
                event = str(row.get("event", "")).upper()
                # Exclure explicitement les événements d'entrée/seed/bag-arm
                if any(x in event for x in ["BUY", "SEED", "SKIP", "BAG_ARM", "BAG_DCA"]):
                    continue
                pnl_str = row.get("pnl_usdt", "")
                if pnl_str != "":
                    try:
                        pnl = float(pnl_str)
                        if pnl != 0.0 or any(x in event for x in ["SELL", "STOP", "CRASH"]):
                            trades_pnl.append(pnl)
                    except ValueError:
                        continue
    except Exception:
        return []
    return trades_pnl


def get_latest_hulk_trades():
    """
    Parcourt les CSVs PAPER_V1_*.csv dans hulk-mexc/runs/ du plus récent au plus
    ancien, et renvoie les PnL du premier CSV ayant des trades clos (sinon []).
    """
    try:
        csv_files = sorted(
            glob.glob(str(HULK_RUNS_DIR / "PAPER_V1_*.csv")),
            key=lambda p: Path(p).stat().st_mtime, reverse=True,
        )
        if not csv_files:
            return []
        for csv_path in csv_files:
            trades_pnl = _trades_du_csv(csv_path)
            if trades_pnl:
                return trades_pnl
        return []
    except Exception:
        return []


def main():
    now_iso = datetime.now().isoformat()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Collecte des données
    justesse_pct = get_justesse_cortana()
    pnl_list = get_latest_hulk_trades()

    n = len(pnl_list)
    if n == 0:
        # Données insuffisantes (aucun trade clos) -> exit 1 (fail-open respecté)
        sys.exit(1)

    wins = [p for p in pnl_list if p > 0]
    losses = [p for p in pnl_list if p < 0]

    nb_wins = len(wins)
    win_rate = (nb_wins / n) if n > 0 else 0.0

    avg_win = (sum(wins) / len(wins)) if wins else 0.0
    avg_loss = (abs(sum(losses) / len(losses))) if losses else 0.0

    b = (avg_win / avg_loss) if avg_loss > 0 else 0.0

    # Kelly plein : k = W - (1 - W) / b
    if b > 0:
        kelly_plein = win_rate - ((1.0 - win_rate) / b)
    else:
        kelly_plein = 0.0

    # Kelly 1/4
    kelly_1_4 = kelly_plein * 0.25

    # Plancher honnête (règle d'or anti-paralysie)
    motif_parts = []
    if win_rate < 0.50 or kelly_1_4 <= 0:
        kelly_1_4 = 0.0
        motif_parts.append("win_rate < 50% ou Kelly ≤ 0 — pas de sizing adaptatif tant que la preuve n'est pas là")
    else:
        motif_parts.append("Kelly valide en mode ombre")

    if n < 20:
        kelly_1_4 = kelly_1_4 * 0.5
        motif_parts.append(f"pénalité petit échantillon (n={n} < 20)")

    # Plafond dur : k4 <= 0.02 (2% max)
    if kelly_1_4 > 0.02:
        kelly_1_4 = 0.02
        motif_parts.append("plafonné à 2% max")

    motif = " — ".join(motif_parts)

    # Capital de base par défaut : 20$
    capital = 20.0
    mise_recommandee = round(kelly_1_4 * capital, 2)

    # 2. Sortie JSON
    output_json = {
        "ts": now_iso,
        "capital": capital,
        "win_rate": round(win_rate, 4),
        "n": n,
        "b": round(b, 4),
        "kelly_plein": round(kelly_plein, 4),
        "kelly_1_4": round(kelly_1_4, 4),
        "mise_recommandee": mise_recommandee,
        "motif": motif,
        "applique": False,
    }

    try:
        KELLY_JSON.parent.mkdir(parents=True, exist_ok=True)
        with open(KELLY_JSON, "w", encoding="utf-8") as f:
            json.dump(output_json, f, indent=2, ensure_ascii=False)
    except Exception:
        pass

    # 3. Sortie Rapport Markdown
    md_content = f"""# Kelly ombre — {date_str}

- **win_rate** : {win_rate:.2%} ({nb_wins}/{n} wins)
- **n** : {n} trades clos
- **avg_win** : {avg_win:.4f}$
- **avg_loss** : {avg_loss:.4f}$
- **b** : {b:.4f}
- **kelly_plein** : {kelly_plein:.4f}
- **kelly_1_4** : {kelly_1_4:.4f}
- **mise_recommandee** : {mise_recommandee}$ (sur capital de {capital}$)
- **justesse_cortana** : {justesse_pct}%
- **motif** : {motif}

## AVIS
Le Kelly calculé est de {kelly_1_4:.4f} (soit {mise_recommandee}$ par trade). En mode actif,
cela ajusterait dynamiquement l'exposition au risque. Cependant, le moteur reste en mode
OMBRE pur par prudence de supervision.

## Règle
« mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20
trades ET justesse Cortana ≥ 50% (validation humaine). »
"""

    try:
        KELLY_MD.parent.mkdir(parents=True, exist_ok=True)
        with open(KELLY_MD, "w", encoding="utf-8") as f:
            f.write(md_content)
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
