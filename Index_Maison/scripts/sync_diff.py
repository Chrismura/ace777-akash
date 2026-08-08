#!/usr/bin/env python3
"""sync_diff.py — rapport de synchronisation OUTBOX vs VAULT (conception Gemini, intégré Ada).

Liste les fichiers canoniques, compare les deux mondes, signale divergences
et indique qui est le plus récent. Lecture seule — ne copie JAMAIS tout seul.

Usage : python3 sync_diff.py
"""
import os
import filecmp
from pathlib import Path

HOME = Path.home()
OUTBOX = HOME / "ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN"
VAULT = HOME / "Documents/Obsidian_ACE777"

# Fichiers canoniques : la liste de vérité du sync (à étendre si besoin)
CANONICAL = [
    "MEMOIRE_COLLAB.md",
    "CONSOLE_GENERALE.md",
    "THERMO_DERNIER.md",
    "SOUS_L_OEIL.md",
    "PLAN_DE_VOL.md",
    "AUTO_PROCESSUS.md",
    "AUTO_EVOL/IDEES.md",
    "AUTO_EVOL/MEMOIRE_PRIORITES.md",
    "Cahier/",
    "Evaluations/",
]


def human_size(n):
    if n >= 1024 * 1024:
        return f"{n / 1024 / 1024:.1f} Mo"
    return f"{n / 1024:.1f} Ko"


def main():
    print("=" * 62)
    print("  RAPPORT DE SYNCHRONISATION : OUTBOX vs VAULT")
    print("=" * 62)
    if not OUTBOX.exists():
        print(f"[ERREUR] OUTBOX introuvable : {OUTBOX}")
        return 1
    vault_ok = VAULT.exists()
    if not vault_ok:
        print(f"[AVERTISSEMENT] Vault illisible (TCC ?) : {VAULT}")
        print("  -> mode dégradé : analyse OUTBOX seule.")

    diverge = 0
    identiques = 0
    absents = 0
    for rel in CANONICAL:
        out = OUTBOX / rel
        print(f"\n[{rel}]")
        if not out.exists():
            print("  ❌ Absent de l'OUTBOX")
            absents += 1
            continue
        out_size = out.stat().st_size
        out_mtime = out.stat().st_mtime
        if not vault_ok or not (VAULT / rel).exists():
            print(f"  ⚠️  Présent OUTBOX ({human_size(out_size)}) mais ABSENT du vault")
            absents += 1
            continue
        v = VAULT / rel
        if out.is_dir() and v.is_dir():
            print("  ℹ️  (dossier) à comparer fichier par fichier — vu comme OK ici")
            identiques += 1
            continue
        same = filecmp.cmp(out, v, shallow=False)
        if same:
            print(f"  ✅ IDENTIQUE ({human_size(out_size)})")
            identiques += 1
        else:
            diverge += 1
            v_size = v.stat().st_size
            v_mtime = v.stat().st_mtime
            print(f"  ⚡ DIVERGENT !")
            print(f"     OUTBOX : {human_size(out_size)} (modifié {out_mtime:.0f})")
            print(f"     VAULT  : {human_size(v_size)} (modifié {v_mtime:.0f})")
            print(f"     [Tendance] {'OUTBOX plus récent' if out_mtime > v_mtime else 'VAULT plus récent'}")

    print("\n" + "=" * 62)
    print(f"  BILAN : {identiques} identiques · {diverge} divergents · {absents} absents")
    if diverge:
        print("  ⚠️  Divergences présentes — résolution = manuelle (jamais d'écrasement auto)")
    print("=" * 62)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
