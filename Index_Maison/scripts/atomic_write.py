#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atomic_write.py — Écriture et lecture atomique et verrouillée pour live.json
Famille ACE777 — Standard POSIX (macOS compatible)

Utilisation :
    writer = SafeLiveWriter("/path/to/live.json")
    writer.write(data_dict)   # atomique, verrouillé
    data = writer.read()      # sécurisé, fallback {}
"""
import os
import json
import fcntl
from pathlib import Path
from typing import Dict, Any


class SafeLiveWriter:
    """Écriture atomique de JSON via fcntl + tmp + os.replace.
    Compatible macOS, zéro dépendance externe."""

    def __init__(self, target_path: str = "live.json"):
        self.target = Path(target_path).resolve()
        self.directory = self.target.parent
        self.tmp = self.directory / f".{self.target.name}.tmp"
        self.lock_file = self.directory / f".{self.target.name}.lock"
        self.directory.mkdir(parents=True, exist_ok=True)
        if not self.lock_file.exists():
            self.lock_file.touch()

    def write(self, data: Dict[str, Any]) -> None:
        """Écriture atomique :
        1. json.dumps en mémoire (fail-fast)
        2. fcntl.flock(LOCK_EX)
        3. Écriture .tmp + fsync
        4. os.replace(.tmp, target) — atomique POSIX
        5. fcntl.flock(LOCK_UN)
        """
        serialized = json.dumps(data, ensure_ascii=False, indent=2)

        with open(self.lock_file, "w") as lock_fd:
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_EX)

                with open(self.tmp, "w", encoding="utf-8") as tmp_fd:
                    tmp_fd.write(serialized)
                    tmp_fd.flush()
                    os.fsync(tmp_fd.fileno())

                os.replace(str(self.tmp), str(self.target))

            finally:
                if self.tmp.exists():
                    try:
                        self.tmp.unlink()
                    except OSError:
                        pass
                fcntl.flock(lock_fd, fcntl.LOCK_UN)

    def read(self) -> Dict[str, Any]:
        """Lecture sécurisée avec verrou partagé. Fallback {} en cas d'erreur."""
        if not self.target.exists():
            return {}

        with open(self.lock_file, "w") as lock_fd:
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_SH)
                if not self.target.exists():
                    return {}
                with open(self.target, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError, ValueError):
                return {}
            finally:
                fcntl.flock(lock_fd, fcntl.LOCK_UN)


if __name__ == "__main__":
    import tempfile, multiprocessing, time

    def writer_task(path, n):
        w = SafeLiveWriter(path)
        for i in range(50):
            w.write({"writer": n, "i": i, "ts": time.time()})

    def reader_task(path, results):
        w = SafeLiveWriter(path)
        errors = 0
        for _ in range(200):
            try:
                d = w.read()
                if d and "writer" not in d:
                    errors += 1
            except Exception:
                errors += 1
        results.append(errors)

    print("=== TEST CONCURRENCE ===")
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "live.json")
        results = multiprocessing.Manager().list()

        readers = [multiprocessing.Process(target=reader_task, args=(p, results)) for _ in range(20)]
        writers = [multiprocessing.Process(target=writer_task, args=(p, i)) for i in range(10)]

        for proc in readers + writers:
            proc.start()
        for proc in readers + writers:
            proc.join(timeout=30)

        total_errors = sum(results)
        print(f"Readers: 20 | Writers: 10 | Erreurs: {total_errors}")
        print("✅ PASS" if total_errors == 0 else f"❌ FAIL ({total_errors} erreurs)")
