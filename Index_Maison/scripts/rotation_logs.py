#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rotation_logs.py — ecrit par GEMINI (delegation Ada, loi 1quinquies)
# Etape 4 Phase 0 : rotation COPYTRUNCATE des logs (ne touche jamais le hub).
import os
import shutil
from datetime import datetime, timezone

SEUIL_OCTETS = 500000
BACKUP_COUNT = 3
BASE_DIR = "/Users/christophe/prise-ia"
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
ROTATION_LOG = os.path.join(REPORTS_DIR, "ROTATION.log")

def get_files():
    files = [
        os.path.join(REPORTS_DIR, "SYNC_LOG.md"),
        os.path.join(BASE_DIR, "usage.jsonl"),
        os.path.join(BASE_DIR, "hub_events.jsonl"),
        os.path.join(REPORTS_DIR, "SUPERVISEUR.log"),
    ]
    try:
        for entry in os.listdir(REPORTS_DIR):
            full = os.path.join(REPORTS_DIR, entry)
            if os.path.isfile(full) and (entry.endswith(".log") or entry.endswith(".out.log") or entry.endswith(".err.log")):
                files.append(full)
    except OSError:
        pass
    return files

def rotate_file(filepath):
    try:
        size = os.path.getsize(filepath)
    except OSError:
        return None
    if size <= SEUIL_OCTETS:
        return None

    try:
        for i in range(BACKUP_COUNT, 0, -1):
            src = f"{filepath}.{i-1}" if i > 1 else filepath
            dst = f"{filepath}.{i}"
            if i == 1:
                # copy current to .1
                shutil.copy2(filepath, dst)
            else:
                if os.path.exists(src):
                    if os.path.exists(dst):
                        os.remove(dst)
                    os.rename(src, dst)
        # truncate current
        with open(filepath, "w", encoding="utf-8") as f:
            f.truncate(0)
        # remove backups beyond count
        extra = f"{filepath}.{BACKUP_COUNT+1}"
        if os.path.exists(extra):
            os.remove(extra)
        return size
    except Exception:
        return None

def main():
    now = datetime.now(timezone.utc).isoformat()
    rotated = []
    for f in get_files():
        size = rotate_file(f)
        if size is not None:
            rotated.append((f, size))
            try:
                with open(ROTATION_LOG, "a", encoding="utf-8") as log:
                    log.write(f"[{now}] rotation: {f} ({size} octets -> archive .1, backups: {BACKUP_COUNT})\n")
            except OSError:
                pass

    print(f"ROTATION LOGS - {now}")
    if rotated:
        for f, size in rotated:
            print(f"roté: {os.path.basename(f)} ({size} octets)")
    else:
        print("aucun fichier a roter")

if __name__ == "__main__":
    main()
