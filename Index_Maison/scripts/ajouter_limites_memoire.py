#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ajouter_limites_memoire.py — LIMITES MÉMOIRE DANS LES PLISTS (PAA-ACE777, 20/08).

Exigence ULTRA (tour 2) : le 19/08, superviseur.sh est mort sans trace —
cause probable : OOM killer silencieux (pas de limite mémoire dans launchd).
Ce script ajoute à une plist les clés SoftResourceLimits/HardResourceLimits
(RSS et nombre de processus) pour que macOS coupe AVANT l'asphyxie totale,
et qu'une mort mémoire laisse une trace (le trap_mort journalise).

Usage :
  python3 ajouter_limites_memoire.py <plist> [rss_mb] [proc_count]
  Ex. : python3 ajouter_limites_memoire.py com.ace777.superviseur-process.plist 400 20

La plist est modifiée en place avec backup .bak-AAAAMMJJ.
"""
import os
import shutil
import sys
import time
from pathlib import Path

PLISTS_DIR = Path("/Users/christophe/ace777-test-day1/Index_Maison/plists")
LAUNCH_AGENTS = Path.home() / "Library" / "LaunchAgents"

# Plists de surveillance critiques à durcir (surveillance = doit TOUJOURS vivre ;
# le moteur de trading lui n'est JAMAIS lancé par launchd — C1).
CRITIQUES = [
    "com.ace777.superviseur-process.plist",   # relanceur vigie marché
    "com.ace777.superviseur-core.plist",      # colonnes cockpit
    "com.ace777.veille-degradation.plist",    # brique méta-analyse
    "com.ace777.dms-veille.plist",            # Dead Man's Switch
    "com.ace777.heartbeats.plist",            # battements par service
    "com.ace777.sante-index.plist",           # pré-vol des index
    "com.ace777.vigie-live.plist",            # vigie marché
]

DEFAULT_RSS_MB = 400   # mémoire max par process de surveillance
DEFAULT_PROC = 20      # nb max de sous-process


def patcher(plist_path: Path, rss_mb: int, proc: int):
    txt = plist_path.read_text(encoding="utf-8")
    if "SoftResourceLimits" in txt:
        print(f"  {plist_path.name}: déjà durcie — skip")
        return False
    # Backup
    bak = plist_path.with_name(plist_path.name + f".bak-{time.strftime('%Y%m%d')}")
    if not bak.exists():
        shutil.copy2(plist_path, bak)
    # Insérer les limites avant </dict></plist>
    limits = f"""    <key>SoftResourceLimits</key>
    <dict>
        <key>MemoryLimit</key>
        <integer>{rss_mb * 1024 * 1024}</integer>
        <key>NumberOfProcesses</key>
        <integer>{proc}</integer>
    </dict>
    <key>HardResourceLimits</key>
    <dict>
        <key>MemoryLimit</key>
        <integer>{rss_mb * 1024 * 1024}</integer>
        <key>NumberOfProcesses</key>
        <integer>{proc}</integer>
    </dict>
"""
    txt = txt.replace("</dict>\n</plist>", limits + "</dict>\n</plist>")
    plist_path.write_text(txt, encoding="utf-8")
    print(f"  {plist_path.name}: limites ajoutées (RSS {rss_mb} Mo, proc {proc})")
    return True


def main():
    rss_mb = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_RSS_MB
    proc = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PROC
    for nom in CRITIQUES:
        src = PLISTS_DIR / nom
        if not src.exists():
            print(f"  {nom}: introuvable dans {PLISTS_DIR} — skip")
            continue
        patcher(src, rss_mb, proc)
        # Copier dans Library/LaunchAgents (si le fichier y existe déjà)
        dst = LAUNCH_AGENTS / nom
        if dst.exists():
            shutil.copy2(src, dst)
            print(f"  -> copié vers {dst.name}")


if __name__ == "__main__":
    main()
