#!/usr/bin/env python3
"""Tests hermétiques du contrat ACE Duo Alpha/Beta.

Aucun réseau, aucun ordre, aucun lancement du champion : uniquement le bus simulé.
"""
from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path


def write_bus(path: Path, run_id: str, role: str, status: str, ts: float):
    path.write_text(json.dumps({
        "run_id": run_id,
        "role": role,
        "status": status,
        "ts": ts,
    }) + "\n")


def read_bus(path: Path, expected_run_id: str, now: float, ttl: float = 60.0):
    if not path.exists():
        return {"ok": False, "reason": "missing"}
    data = json.loads(path.read_text())
    if data.get("run_id") != expected_run_id:
        return {"ok": False, "reason": "run_id_mismatch"}
    age = now - float(data.get("ts", 0))
    if age > ttl:
        return {"ok": False, "reason": "stale"}
    return {"ok": True, "role": data.get("role"), "status": data.get("status")}


def decide(alpha, beta, double_death=False):
    """Politique attendue : sortie maintenue, pas de nouvelle entrée si bus invalide."""
    if double_death:
        return "STOP_NO_RELAUNCH"
    if not beta["ok"] or not alpha["ok"]:
        return "NO_NEW_ENTRIES"
    return "NORMAL"


def main():
    now = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        beta_path = root / "duo_beta.json"
        alpha_path = root / "duo_alpha.json"
        run_id = "test-run-001"

        # Beta arrêté : Alpha ne doit pas poursuivre une entrée sur un état absent.
        write_bus(alpha_path, run_id, "HUNTER", "OPEN", now)
        beta = read_bus(beta_path, run_id, now)
        alpha = read_bus(alpha_path, run_id, now)
        assert decide(alpha, beta) == "NO_NEW_ENTRIES"

        # Alpha arrêté : même règle symétrique.
        write_bus(beta_path, run_id, "SCOUT", "OPEN", now)
        alpha_path.unlink()
        beta = read_bus(beta_path, run_id, now)
        alpha = read_bus(alpha_path, run_id, now)
        assert decide(alpha, beta) == "NO_NEW_ENTRIES"

        # Bus périmé : aucune entrée nouvelle.
        write_bus(beta_path, run_id, "SCOUT", "OPEN", now - 61)
        write_bus(alpha_path, run_id, "HUNTER", "OPEN", now)
        beta = read_bus(beta_path, run_id, now)
        alpha = read_bus(alpha_path, run_id, now)
        assert beta["reason"] == "stale"
        assert decide(alpha, beta) == "NO_NEW_ENTRIES"

        # Ancienne session : ne jamais consommer son bus.
        write_bus(beta_path, "old-run", "SCOUT", "OPEN", now)
        write_bus(alpha_path, run_id, "HUNTER", "OPEN", now)
        beta = read_bus(beta_path, run_id, now)
        assert beta["reason"] == "run_id_mismatch"
        assert decide(alpha, beta) == "NO_NEW_ENTRIES"

        # Double mort : arrêt propre, pas de boucle de relance.
        assert decide(alpha, beta, double_death=True) == "STOP_NO_RELAUNCH"

        # Les deux jambes fraîches et même session : fonctionnement normal.
        write_bus(beta_path, run_id, "SCOUT", "OPEN", now)
        beta = read_bus(beta_path, run_id, now)
        assert decide(alpha, beta) == "NORMAL"

    print("ACE_DUO_SCENARIO_TESTS_OK")


if __name__ == "__main__":
    main()
