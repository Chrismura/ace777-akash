#!/usr/bin/env python3
"""Local, read-only observation recorder for ACE shadow/replay work.

The recorder never contacts an exchange and never places orders. It is disabled
unless the caller explicitly passes ``enabled=True`` or sets
``ACE_OBSERVATION_RECORDING=TRUE``.
"""

from __future__ import annotations

import csv
import os
import tempfile
from pathlib import Path
from typing import Mapping, Optional

OBSERVATION_FIELDS = (
    "ts",
    "run_id",
    "unit",
    "cycle",
    "symbol",
    "bid",
    "ask",
    "mid",
    "spread_bps",
    "momentum_bps",
    "regime",
    "decision",
    "side",
    "confidence",
    "reason",
)


def recording_enabled() -> bool:
    return os.environ.get("ACE_OBSERVATION_RECORDING", "FALSE").upper() == "TRUE"


def _ensure_header(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        return
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as handle:
            csv.writer(handle).writerow(OBSERVATION_FIELDS)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def record_observation(
    path: os.PathLike[str] | str,
    observation: Mapping[str, object],
    *,
    enabled: Optional[bool] = None,
) -> bool:
    """Append one observation and return whether it was written.

    Missing fields are emitted as empty values. Unknown fields are ignored so
    callers can pass richer engine snapshots without changing the contract.
    """
    if enabled is None:
        enabled = recording_enabled()
    if not enabled:
        return False

    target = Path(path)
    _ensure_header(target)
    row = [observation.get(field, "") for field in OBSERVATION_FIELDS]
    with target.open("a", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerow(row)
        handle.flush()
        os.fsync(handle.fileno())
    return True


class ObservationRecorder:
    """Small convenience wrapper for a single run's observation CSV."""

    def __init__(self, path: os.PathLike[str] | str, *, enabled: Optional[bool] = None):
        self.path = Path(path)
        self.enabled = recording_enabled() if enabled is None else enabled

    def record(self, observation: Mapping[str, object]) -> bool:
        return record_observation(self.path, observation, enabled=self.enabled)
