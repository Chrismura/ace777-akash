"""
Rôle : Génère un rapport d'audit PnL réel (36j) basé sur la concaténation de TOUS
les runs dédupliqués (mode --all de trades_last_run), évitant les artefacts de
double-comptage des copies --resume. Codé par le CODEUR (29/08), intégré et testé
par Buffy. Écriture atomique du rapport dans runs/AUDIT_PNL_REEL_<ts>.md.
"""
from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# Import du module frère (même répertoire)
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

try:
    import trades_last_run
except ImportError:
    print("[ERREUR] Impossible d'importer trades_last_run.py", file=sys.stderr)
    sys.exit(1)


def ecrire_atomique(chemin_cible: Path, contenu: str) -> None:
    chemin_cible.parent.mkdir(parents=True, exist_ok=True)
    fd, chemin_temp = tempfile.mkstemp(dir=chemin_cible.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(chemin_temp, chemin_cible)
    except Exception:
        if os.path.exists(chemin_temp):
            os.remove(chemin_temp)
        raise


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    runs_dir = root / "runs"

    tous = trades_last_run.all_paper_csvs(root)
    if not tous:
        print("[ERREUR] Aucun run PAPER_V1 disponible pour l'audit.")
        sys.exit(1)

    lignes = trades_last_run.trades_all(root)
    stats = trades_last_run.pnl_par_pair(lignes)

    ts_rapport = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    rapport_path = runs_dir / f"AUDIT_PNL_REEL_{ts_rapport}.md"

    md = [
        "# Rapport d'Audit PnL Réel (36j, tous les runs dédupliqués)",
        "",
        f"- **Généré** : `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ')}`",
        f"- **Runs concaténés** : `{len(tous)}`",
        f"- **Trades uniques (dédupliqués ts, pair, action)** : `{len(lignes)}`",
        "",
        "## Synthèse par Paire",
        "",
        "| Paire | PnL SELL (full) | PnL SELL (partial) | Total ($) |",
        "| :--- | ---: | ---: | ---: |",
    ]
    grand = 0.0
    for pair, data in sorted(stats.items()):
        tot = data["pnl_total"]
        grand += tot
        md.append(
            f"| `{pair}` | {data['pnl_sell_full']:.2f} | "
            f"{data['pnl_sell_partial']:.2f} | **{tot:.2f}** |"
        )
    md.extend([
        f"| **TOTAL GENERAL** | | | **{grand:.2f} $** |",
        "",
        "---",
        "*Note ACE777 : rapport via concaténation de tous les runs + déduplication "
        "par (ts, pair, action) pour neutraliser le trompe-l'œil des copies --resume.*",
    ])

    ecrire_atomique(rapport_path, "\n".join(md))
    print(f"[SUCCES] Rapport d'audit généré : {rapport_path}")


if __name__ == "__main__":
    main()