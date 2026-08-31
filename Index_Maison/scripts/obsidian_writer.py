#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obsidian_writer.py — Wrapper global OUTBOX → pont Obsidian (chantier A' + B, 31/08)
==================================================================================
Recommandation famille (3/3) : NE PAS réécrire les ~60 scripts qui écrivent dans
OUTBOX_OBSIDIAN. On pose un CONSOMMATEUR global : ce script scanne la boîte,
fait passer chaque .md par le pont (gatekeeper write_typed si type détectable,
sinon write_note brut), archive les fichiers traités et trace les rejets au DLO.

- Mapping dossier OUTBOX → type gatekeeper :
    Crypto_Projet → actif        (fiches setup / deepdive)
    Cahier       → journal       (journaux)
    Index_Maison → synthese_ia   (synthèses famille/cortana)
    Hulk         → signal        (signaux hulk)
    A_Mon_Attention / AUTO_EVOL / autres → brut (write_note, fail-open)
- SÉCURITÉ : on ne touche JAMAIS aux fichiers déjà traités (archive _traites/).
- Day Zero : si un .md a déjà un frontmatter `type:` reconnu, write_note le
  route automatiquement vers le gatekeeper (rétrocompat pont v2).

Usage :
    python3 obsidian_writer.py --scan            # une passe
    python3 obsidian_writer.py --watch           # boucle (pour cron/launchd)
    python3 obsidian_writer.py --scan --dry-run  # ne rien écrire, juste lister
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from obsidian_cli_bridge import VAULT, ObsidianBridge, parse_frontmatter_light

# === CONFIG ===
ROOT = Path(__file__).resolve().parent.parent          # Index_Maison/
OUTBOX = ROOT / "OUTBOX_OBSIDIAN"
ARCHIVE = OUTBOX / "_traites"                          # fichiers déjà consommés
WATCH_INTERVAL = 60                                    # secondes (mode --watch)

# Mapping dossier OUTBOX → type gatekeeper (4 types stricts famille)
FOLDER_TO_TYPE = {
    "Crypto_Projet": "actif",
    "Cahier": "journal",
    "Index_Maison": "synthese_ia",
    "Hulk": "signal",
}

# Types qui exigent des propriétés que le fichier brut n'a pas → on ajoute des
# valeurs par défaut raisonnables pour ne pas tout rejeter en masse.
DEFAULTS = {
    "actif": {"statut": "brouillon", "actif": "non_renseigne"},
    "journal": {"statut": "brouillon", "source": "agent"},
    "synthese_ia": {"type_consultation": "non_renseigne", "membres": ["system"], "statut": "brouillon"},
    "signal": {"direction": "neutral", "statut": "en_cours", "actif": "non_renseigne"},
}


def _extract_title(path: Path, content: str) -> str:
    """Titre : 1er H1 du contenu, sinon nom du fichier sans extension."""
    for line in content.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return path.stem


def _type_for(path: Path):
    """Détermine le type gatekeeper depuis le chemin relatif OUTBOX."""
    rel = path.relative_to(OUTBOX)
    parts = rel.parts
    if len(parts) >= 2:
        return FOLDER_TO_TYPE.get(parts[0])
    return None


def process_one(path: Path, dry_run: bool = False):
    """Consomme un .md de la boîte → pont. Retourne un dict de résultat."""
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": str(path), "status": "ERROR_LECTURE", "error": str(e)}

    # 1. Frontmatter type présent ? → gatekeeper direct (Day Zero rétrocompat)
    detected, body = parse_frontmatter_light(content)
    note_type = detected if detected in ("actif", "signal", "synthese_ia", "journal") \
        else _type_for(path)

    # 2. Préparer les données pour write_typed
    title = _extract_title(path, content)
    if note_type:
        data = dict(DEFAULTS.get(note_type, {}))
        data["body"] = body if detected else content
        data["date"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        # wikilink automatique : la fiche se relie à sa propre famille (Day Zero F)
        data["wikilink_to"] = [f"FICHE_SETUP_{title.upper()}"[:60]] if note_type == "actif" else []
        if dry_run:
            return {"file": str(path), "status": "DRYRUN_TYPED", "type": note_type, "title": title}
        res = ObsidianBridge.write_typed(note_type, data, title=title)
        if res["status"] == "REJECTED":
            return {"file": str(path), "status": "REJECTED", "type": note_type,
                    "title": title, "errors": res["errors"]}
        return {"file": str(path), "status": res["status"], "type": note_type,
                "title": title, "path": res.get("path"), "via": res.get("via")}

    # 3. Pas de type → brut (fail-open, jamais de perte)
    if dry_run:
        return {"file": str(path), "status": "DRYRUN_BRUT", "title": title}
    res = ObsidianBridge.write_note(title, content, folder="00_Inbox")
    return {"file": str(path), "status": res["status"], "title": title,
            "path": res.get("path"), "via": res.get("via")}


def archive(path: Path, result: dict):
    """Déplace le fichier traité vers _traites/ (jamais retraité)."""
    try:
        ARCHIVE.mkdir(parents=True, exist_ok=True)
        dest = ARCHIVE / path.name
        # suffixe si collision
        if dest.exists():
            dest = ARCHIVE / f"{path.stem}_{int(time.time())}{path.suffix}"
        path.rename(dest)
        result["archive"] = str(dest)
    except Exception as e:
        result["archive_error"] = str(e)


# Fichiers de travail réécrits en continu par des scripts : on ne les consomme
# JAMAIS (ils doivent rester dans la boîte, le pont lit le vault à la demande).
PROTECTED_STEMS = {
    "THERMO_DERNIER", "SUPERVISEUR_LOG", "CHECKUP_DERNIER", "ETAT_SYSTEME",
    "CHECKUP_20260730T1511Z", "HEARTBEAT", "JOURNAL_COCKPIT", "POINT_REPRISE_DERNIER",
}


def _protected(path: Path) -> bool:
    return path.stem in PROTECTED_STEMS or path.name.startswith(".")


def _already_in_vault(path: Path) -> bool:
    """Idempotence (Day Zero) : si le fichier existe déjà dans le vault au même
    chemin relatif (la synchro manuelle cp l'a déjà copié), on NE le réécrit
    PAS — éviter les doublons et ne pas toucher aux notes existantes."""
    try:
        rel = path.relative_to(OUTBOX)
        return (VAULT / rel).exists()
    except Exception:
        return False


def scan(dry_run: bool = False, age_heures: float = 0):
    """Une passe complète de la boîte. Retourne le bilan.

    age_heures > 0 : ne traiter que les fichiers modifiés depuis moins de N
    heures (séquencement famille — ne pas tout archiver d'un coup, ne pas
    toucher aux fichiers de travail en cours).
    """
    if not OUTBOX.exists():
        print(f"[writer] OUTBOX introuvable : {OUTBOX}")
        return
    now = time.time()
    md_files = sorted(p for p in OUTBOX.rglob("*.md") if "_traites" not in p.parts)
    results = []
    for p in md_files:
        if _protected(p):
            continue
        if age_heures > 0 and (now - p.stat().st_mtime) > age_heures * 3600:
            continue
        if _already_in_vault(p):
            results.append({"file": str(p), "status": "DEJA_DANS_VAULT"})
            if not dry_run:
                archive(p, results[-1])  # la copie existe déjà : on archive la source
            continue
        r = process_one(p, dry_run=dry_run)
        results.append(r)
        print(f"  {r.get('status', '?'):<18} {p.relative_to(OUTBOX)}"
              + (f"  [{r.get('type')}]" if r.get('type') else ""))
        if not dry_run and r.get("status") not in ("ERROR_LECTURE", "REJECTED"):
            archive(p, r)

    n_ok = sum(1 for r in results if r.get("status") in ("SUCCESS", "SUCCESS_CLI", "SUCCESS_FALLBACK"))
    n_rej = sum(1 for r in results if r.get("status") == "REJECTED")
    n_err = sum(1 for r in results if r.get("status") == "ERROR_LECTURE")
    n_deja = sum(1 for r in results if r.get("status") == "DEJA_DANS_VAULT")
    print(f"\n[writer] {len(results)} fichiers | OK {n_ok} | DÉJÀ VAULT {n_deja} | "
          f"REJETÉS {n_rej} | ERREURS {n_err}" + (" | DRY-RUN" if dry_run else ""))
    return {"total": len(results), "ok": n_ok, "deja_vault": n_deja,
            "rejetes": n_rej, "erreurs": n_err}


def watch():
    """Boucle de consommation (cron/launchd ou usage manuel)."""
    print(f"[writer] mode WATCH toutes les {WATCH_INTERVAL}s — Ctrl+C pour arrêter")
    while True:
        try:
            scan(dry_run=False)
        except KeyboardInterrupt:
            print("\n[writer] arrêt.")
            break
        except Exception as e:
            print(f"[writer] erreur passe : {e}")
        time.sleep(WATCH_INTERVAL)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Wrapper global OUTBOX → pont Obsidian")
    ap.add_argument("--scan", action="store_true", help="une passe")
    ap.add_argument("--watch", action="store_true", help="boucle continue")
    ap.add_argument("--dry-run", action="store_true", help="ne rien écrire")
    ap.add_argument("--age-heures", type=float, default=0,
                    help="ne traiter que les fichiers de moins de N heures")
    args = ap.parse_args()
    if args.watch:
        watch()
    else:
        scan(dry_run=args.dry_run, age_heures=args.age_heures)
