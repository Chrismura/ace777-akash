# Réponse codeur (provider Google Gemini, 6.7s)

Voici le code exact du fichier `Index_Maison/scripts/kelly_ombre.py` et le diff pour `discipline_quotidienne.py`, conformément à la spécification.

### 1. Fichier à créer : `Index_Maison/scripts/kelly_ombre.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kelly fractionnaire 1/4 en mode OMBRE (sizing Hulk)
Calcule et affiche le Kelly sans rien modifier (mode observation pur).
Conforme spec ACE777 - 15/08/2026.
"""

from pathlib import Path
import json
import csv
import glob
from datetime import datetime
import sys

# Chemins absolus / relatifs robustes
ROOT = Path(__file__).resolve().parent.parent.parent  # Racine globale (Index_Maison est un sous-dossier ou racine)
# Ajustement selon l'arborescence : si Index_Maison/scripts/kelly_ombre.py, ROOT est deux niveaux au-dessus.
# Verifions l'emplacement réel de hulk-mexc par rapport à ce script :
# Index_Maison/scripts/kelly_ombre.py -> parent.parent est la racine globale contenant Index_Maison et hulk-mexc.
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

def get_latest_hulk_trades():
    """
    Parcourt le dernier CSV PAPER_V1_*.csv dans hulk-mexc/runs/.
    Compte les événements de sortie (pnl_usdt != 0) et extrait les PnL.
    Ignore BUY, SEED, SKIP, BAG_ARM, BAG_DCA, etc.
    """
    try:
        csv_files = sorted(glob.glob(str(HULK_RUNS_DIR / "PAPER_V1_*.csv")), key=lambda p: Path(p).stat().st_mtime, reverse=True)
        if not csv_files:
            return []

        latest_csv = csv_files[0]
        trades_pnl = []

        with open(latest_csv, mode="r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            for row in reader:
                action = str(row.get("action", "")).upper()
                # Exclure explicitement les actions de type entrée/seed/bag
                if any(x in action for x in ["BUY", "SEED", "SKIP", "BAG_ARM", "BAG_DCA"]):
                    continue
                
                # Vérifier si c'est une sortie avec un PnL mesurable
                pnl_str = row.get("pnl_usdt", "")
                if pnl_str != "":
                    try:
                        pnl = float(pnl_str)
                        # On ne garde que les trades clos ayant un pnl renseigné
                        if pnl != 0.0 or "SELL" in action or "STOP" in action or "CRASH" in action:
                            trades_pnl.append(pnl)
                    except ValueError:
                        continue
        return trades_pnl
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
        "applique": False
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
Le Kelly calculé est de {kelly_1_4:.4f} (soit {mise_recommandee}$ par trade). En mode actif, cela ajusterait dynamiquement l'exposition au risque. Cependant, le moteur reste en mode OMBRE pur par prudence supervision.

## Règle
« mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20 trades ET justesse Cortana ≥ 50% (validation humaine). »
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
```

---

### 2. Diff pour `discipline_quotidienne.py` (3 lignes minimales)

Recherchez l'endroit correspondant à la dérive mémoire dans `Index_Maison/scripts/discipline_quotidienne.py` et appliquez ce diff exact :

```python
<<<<
    # (Fin de la dérive mémoire existante)
====
    # [CHANTIER 3] Kelly fractionnaire 1/4 en mode OMBRE (fail-open, non bloquant)
    try:
        subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "kelly_ombre.py")], check=False, capture_output=True, timeout=30)
    except Exception:
        pass
>>>>
```
