# RÉPONSE HUB (task code.ia · via Google Gemini) — 2026-08-29T16:06:58

```python
# hulk-mexc/scripts/trades_last_run.py
"""
Rôle : Helper et CLI pour analyser uniquement le dernier run PAPER_V1 actif.
Évite le piège de l'agrégation de multiples CSV (dus aux --resume successifs).
Stdlib uniquement, compatible Python 3.9+, robuste et non fatal.
"""

from __future__ import annotations

import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


def recent_paper_csv(root: Path) -> Path | None:
    """
    Renvoie le chemin du fichier CSV PAPER_V1 le plus récent dans le dossier runs/
    en se basant sur le timestamp extrait du nom du fichier (et non le mtime).
    Ex: PAPER_V1_20260829_120000.csv -> tri chronologique fiable.
    """
    runs_dir = root / "runs"
    if not runs_dir.exists() or not runs_dir.is_dir():
        return None

    csv_files = list(runs_dir.glob("PAPER_V1_*.csv"))
    if not csv_files:
        return None

    # Fonction de tri par timestamp dans le nom du fichier
    def extract_ts(path: Path) -> str:
        # Format attendu: PAPER_V1_YYYYMMDD_HHMMSS.csv ou similaire
        name = path.stem
        parts = name.split("_")
        # On cherche les segments numériques pour composer une clé de tri
        numeric_parts = [p for p in parts if p.isdigit()]
        return "".join(numeric_parts) if numeric_parts else name

    # Trie par ordre croissant du timestamp extrait, le plus récent en dernier
    csv_files_sorted = sorted(csv_files, key=extract_ts)
    return csv_files_sorted[-1]


def trades(df_path: Path) -> List[Dict[str, str]]:
    """
    Parse le CSV spécifié, dédoublonne les lignes par (ts, pair, action)
    en conservant la première occurrence, et renvoie la liste des dictionnaires.
    """
    if not df_path.exists():
        return []

    lignes_brutes = []
    try:
        with open(df_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lignes_brutes.append(row)
    except Exception as e:
        print(f"[ERREUR] Lecture impossible de {df_path} : {e}", file=sys.stderr)
        return []

    # Dédoublonnage par clé unique (ts, pair, action)
    # Note : conservation de la première occurrence (ordre chronologique d'apparition)
    vus = set()
    lignes_uniques = []

    for row in lignes_brutes:
        # Normalisation des clés de recherche (gestion des variations de nommage)
        ts = row.get("ts") or row.get("timestamp") or row.get("time") or ""
        pair = row.get("pair") or row.get("symbol") or ""
        action = row.get("action") or row.get("side") or ""

        cle = (ts, pair, action)
        if cle not in vus:
            vus.add(cle)
            lignes_uniques.append(row)

    return lignes_uniques


def pnl_par_pair(lignes: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    """
    Calcule le PnL réel par paire à partir des lignes dédoublonnées.
    Sépare les SELL full (commission déduite) et les SELL_PARTIAL.
    """
    resultats: Dict[str, Dict[str, float]] = {}

    for row in lignes:
        pair = row.get("pair") or row.get("symbol")
        action = row.get("action") or row.get("side")
        if not pair or not action:
            continue

        if pair not in resultats:
            resultats[pair] = {
                "pnl_sell_full": 0.0,
                "pnl_sell_partial": 0.0,
                "pnl_total": 0.0,
            }

        # Extraction sécurisée des valeurs financières
        try:
            pnl = float(row.get("pnl", 0.0) or 0.0)
        except ValueError:
            pnl = 0.0

        if action.upper() == "SELL":
            resultats[pair]["pnl_sell_full"] += pnl
            resultats[pair]["pnl_total"] += pnl
        elif action.upper() == "SELL_PARTIAL":
            resultats[pair]["pnl_sell_partial"] += pnl
            resultats[pair]["pnl_total"] += pnl

    return resultats


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    target_pair = None

    # Analyse très basique des arguments CLI sans argparse pour rester en stdlib légère
    args = sys.argv[1:]
    if "--pair" in args:
        try:
            idx = args.index("--pair")
            target_pair = args[idx + 1].upper()
        except (IndexError, ValueError):
            pass

    csv_path = recent_paper_csv(root)
    if not csv_path:
        print("[INFO] Aucun fichier PAPER_V1_*.csv trouvé dans runs/.")
        sys.exit(0)

    print(f"--- ANALYSE DU DERNIER RUN PAPER ---")
    print(f"Fichier cible : {csv_path.name}")

    # Lecture brute vs dédoublonnée pour comparaison
    with open(csv_path, mode="r", encoding="utf-8") as f:
        total_brut = sum(1 for _ in f) - 1  # Moins l'en-tête

    lignes = trades(csv_path)
    print(f"Lignes brutes : {max(0, total_brut)} | Lignes dédoublonnées : {len(lignes)}")

    stats = pnl_par_pair(lignes)

    print("\n--- PNL PAR PAIRE ---")
    grand_total = 0.0
    for pair, data in sorted(stats.items()):
        if target_pair and pair != target_pair:
            continue
        tot = data["pnl_total"]
        grand_total += tot
        print(
            f"  {pair:<12} | Full: {data['pnl_sell_full']:>8.2f}$ | "
            f"Partial: {data['pnl_sell_partial']:>8.2f}$ | Total: {tot:>8.2f}$"
        )

    print("-" * 42)
    print(f"  {'GRAND TOTAL':<12} | {grand_total:>31.2f}$")


if __name__ == "__main__":
    main()
```

```python
# hulk-mexc/scripts/audit_pnl_reel.py
"""
Rôle : Génère un rapport d'audit PnL réel (36j) basé exclusivement sur le dernier run,
évitant ainsi les artefacts de double-comptage dus aux cumuls de --resume.
Écriture atomique du rapport Markdown dans runs/AUDIT_PNL_REEL_<ts>.md.
"""

from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path

# Import du module de référence du même répertoire
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

try:
    import trades_last_run
except ImportError:
    print("[ERREUR] Impossible d'importer trades_last_run.py", file=sys.stderr)
    sys.exit(1)


def ecrire_atomique(chemin_cible: Path, contenu: str) -> None:
    """Écriture atomique sécurisée via fichier temporaire et os.replace."""
    chemin_cible.parent.mkdir(parents=True, exist_ok=True)
    fd, chemin_temp = tempfile.mkstemp(dir=chemin_cible.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(chemin_temp, chemin_cible)
    except Exception as e:
        if os.path.exists(chemin_temp):
            os.remove(chemin_temp)
        raise e


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    runs_dir = root / "runs"

    csv_path = trades_last_run.recent_paper_csv(root)
    if not csv_path:
        print("[ERREUR] Aucun run PAPER_V1 disponible pour l'audit.")
        sys.exit(1)

    lignes = trades_last_run.trades(csv_path)
    stats = trades_last_run.pnl_par_pair(lignes)

    ts_rapport = datetime.now().strftime("%Y%m%d_%H%M%S")
    rapport_path = runs_dir / f"AUDIT_PNL_REEL_{ts_rapport}.md"

    # Construction du contenu Markdown
    lignes_md = [
        f"# Rapport d'Audit PnL Réel (Dernier Run)",
        f"",
        f"- **Date de generation** : `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`",
        f"- **Source analysee** : `{csv_path.name}`",
        f"- **Nombre de trades uniques** : `{len(lignes)}`",
        f"",
        f"## Synthèse par Paire",
        f"",
        f"| Paire | PnL SELL (Full) | PnL SELL (Partial) | PnL Total ($) |",
        f"| :--- | ---: | ---: | ---: |",
    ]

    grand_total = 0.0
    for pair, data in sorted(stats.items()):
        tot = data["pnl_total"]
        grand_total += tot
        lignes_md.append(
            f"| `{pair}` | {data['pnl_sell_full']:.2f} | {data['pnl_sell_partial']:.2f} | **{tot:.2f}** |"
        )

    lignes_md.extend([
        f"| **TOTAL GENERAL** | - | - | **{grand_total:.2f} $** |",
        f"",
        f"---",
        f"*Note ACE777 : Rapport généré via lecture exclusive du dernier run pour neutraliser le trompe-l'œil des copies --resume.*"
    ])

    contenu_final = "\n".join(lignes_md)

    try:
        ecrire_atomique(rapport_path, contenu_final)
        print(f"[SUCCES] Rapport d'audit généré : {rapport_path}")
    except Exception as e:
        print(f"[ERREUR] Écriture du rapport impossible : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

### NOTES

1. **Choix de la clé de déduplication `(ts, pair, action)` vs `(ts, pair)`** :
   - *Pourquoi `(ts, pair, action)` ?* Dans le moteur de trading, un même timestamp (seconde) peut théoriquement enregistrer une séquence d'actions distinctes (ex: `BUY` suivi d'un `SELL_PARTIAL` ou d'un `SELL` suite à une mise à jour d'état rapide). 
   - Restreindre la clé uniquement à `(ts, pair)` risquerait de supprimer par erreur des événements légitimes survenus à la même seconde mais de natures différentes. L'association avec `action` garantit l'unicité stricte de l'événement commercial tout en éliminant proprement les duplications de lignes entières induites par les empilements successifs des `--resume` (`shutil.copy2`).

2. **Respect des contraintes** :
   - Utilisation exclusive de la stdlib Python (`csv`, `pathlib`, `sys`, `os`, `tempfile`, `datetime`).
   - Aucune modification du moteur `paper_diprip.py` ou des scripts de divergence (isolation totale).
   - Écriture sécurisée et atomique (`mkstemp` + `os.replace`).
   - Gestion robuste des cas limites (absence de dossier `runs/` ou de fichiers CSV sans interruption brutale).
