#!/usr/bin/env python3
"""
RAFRAÎCHISSEUR FUSIBLES (10/09/2026, GO Christophe) — le thermomètre des fusibles.

Fonction : relancer mesurer_volatilite_paires.py toutes les 5 min (launchd
com.ace777.fusibles-mesure) pour que les conditions de DÉGEL restent des
données vivantes. Le garde-fusible (fusibles_paires.py, dans HULK) est
fail-CLOSED : mesures périmées > 15 min → dégel impossible (jamais de dégel
sur des données périmées). Ce capteur est fail-OPEN : s'il meurt, aucun
dégel ne peut se produire ( posture inverse, la bonne : un capteur qui rate
ne doit jamais PROVOQUER un dégel).

Échec d'une mesure : on ne touche PAS au fichier existant (le garde-fusible
continue de lire la dernière mesure valide ; son contrôle de fraîcheur 15 min
sévérité-la si nécessaire). Trace dans fusibles_erreurs.jsonl.
"""
from __future__ import annotations

import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # racine projet
OUT = ROOT / "Index_Maison" / "data" / "volatilite_paires.json"
ERR = ROOT / "Index_Maison" / "data" / "fusibles_erreurs.jsonl"
OUTIL = ROOT / "Index_Maison" / "scripts" / "mesurer_volatilite_paires.py"


def _note(msg: str) -> None:
    try:
        with ERR.open("a", encoding="utf-8") as f:
            f.write(json_dumps({"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "src": "rafraichir_fusibles", "msg": msg}) + "\n")
    except Exception:
        pass


def json_dumps(d: dict) -> str:
    import json
    return json.dumps(d, ensure_ascii=False)


def main() -> int:
    ts_avant = OUT.stat().st_mtime if OUT.exists() else 0.0
    t0 = time.time()
    try:
        r = subprocess.run(
            [sys.executable, str(OUTIL)],
            capture_output=True, text=True, timeout=90,
        )
    except subprocess.TimeoutExpired:
        _note("mesure timeout 90s — fichier existant intact")
        return 1
    duree = time.time() - t0
    if r.returncode != 0:
        _note(f"mesure échouée rc={r.returncode} — fichier existant intact · {r.stderr.strip()[-200:]}")
        return 1
    try:
        ts_apres = OUT.stat().st_mtime
    except OSError:
        _note("fichier de mesures disparu après run ?!")
        return 1
    if ts_apres <= ts_avant and ts_avant > 0:
        _note("fichier non réécrit ? (mtime inchangé)")
        return 1
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] mesures "
          f"rafraîchies en {duree:.1f}s → {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
