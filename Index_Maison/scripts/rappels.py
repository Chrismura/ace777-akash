#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAPPELS.py — rappels de tâches pour Cortana (étape 5, 18/08/2026).

Usage :
  python3 rappels.py ajouter "acheter du pain" 18:30
  python3 rappels.py ajouter "réunion" "2026-08-19 09:00"
  python3 rappels.py lister
  python3 rappels.py supprimer <id|texte>
  python3 rappels.py verifier        # lit les rappels échus -> alerte vocale + cockpit

Garde-fous : pas de rappel sans heure · plafond MAX_ACTIFS · TTL (expire après
48h échu) · jamais d'ordre de trading. Stdlib uniquement.
"""
import json
import os
import sys
import time
import tempfile
import subprocess
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

IM = Path(__file__).resolve().parent.parent
RAPPELS_PATH = IM / "strategie" / "rappels.json"
ALERTE_VOCALE = IM / "scripts" / "alerte_vocale.py"
COCKPIT_JS = IM / "cockpit" / "rappels_live.js"

MAX_ACTIFS = 20
TTL_SEC = 48 * 3600  # un rappel échu expire après 48h


def _lire():
    try:
        return json.loads(RAPPELS_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []


def _ecrire(rappels):
    RAPPELS_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(RAPPELS_PATH.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(rappels, f, ensure_ascii=False, indent=2)
        os.replace(tmp, str(RAPPELS_PATH))
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def _ecrire_cockpit(rappels):
    try:
        COCKPIT_JS.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(COCKPIT_JS.parent), suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("window.__RAPPELS__ = " + json.dumps(rappels, ensure_ascii=False) + ";\n")
        os.replace(tmp, str(COCKPIT_JS))
    except Exception:
        pass


def _parse_heure(texte: str):
    """Retourne un timestamp (epoch) à partir de 'HH:MM' (aujourd'hui/demain)
    ou 'YYYY-MM-DD HH:MM'. Lève ValueError si invalide."""
    texte = texte.strip()
    now = datetime.now()
    m = re.match(r"^(\d{1,2}):(\d{2})$", texte)
    if m:
        h, mi = int(m.group(1)), int(m.group(2))
        if not (0 <= h <= 23 and 0 <= mi <= 59):
            raise ValueError("heure invalide")
        due = now.replace(hour=h, minute=mi, second=0, microsecond=0)
        if due <= now:
            due += timedelta(days=1)
        return due.timestamp()
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[ T](\d{1,2}):(\d{2})$", texte)
    if m:
        d, h, mi = m.group(1), int(m.group(2)), int(m.group(3))
        if not (0 <= h <= 23 and 0 <= mi <= 59):
            raise ValueError("heure invalide")
        return datetime.strptime(f"{d} {h:02d}:{mi:02d}", "%Y-%m-%d %H:%M").timestamp()
    raise ValueError("format attendu : HH:MM ou YYYY-MM-DD HH:MM")


def _alerter(message: str):
    try:
        subprocess.Popen([sys.executable, str(ALERTE_VOCALE), "--message", message,
                          "--id", str(int(time.time()))],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
    except Exception:
        pass


def ajouter(tache, heure):
    tache = (tache or "").strip()
    if not tache:
        return False, "tâche vide"
    try:
        due = _parse_heure(heure)
    except ValueError as e:
        return False, str(e)
    rappels = _lire()
    actifs = [r for r in rappels if not r.get("fait")]
    if len(actifs) >= MAX_ACTIFS:
        return False, f"plafond de {MAX_ACTIFS} rappels actifs atteint"
    rappel = {
        "id": int(time.time() * 1000),
        "tache": tache,
        "due": due,
        "due_iso": datetime.fromtimestamp(due, timezone.utc).isoformat(),
        "created_iso": datetime.now(timezone.utc).isoformat(),
        "fait": False,
    }
    rappels.append(rappel)
    _ecrire(rappels)
    _ecrire_cockpit(rappels)
    return True, rappel


def lister():
    rappels = _lire()
    now = time.time()
    lignes = []
    for r in rappels:
        if r.get("fait"):
            continue
        d = datetime.fromtimestamp(r.get("due") or 0)
        reste = int((r.get("due") or 0) - now) // 60
        etat = "ÉCHU" if reste <= 0 else f"dans {reste} min"
        lignes.append({"id": r.get("id"), "tache": r.get("tache"),
                       "quand": d.strftime("%Y-%m-%d %H:%M"), "etat": etat})
    return lignes


def supprimer(cible):
    rappels = _lire()
    avant = len(rappels)
    cible = str(cible or "")
    reste = [r for r in rappels if not (str(r.get("id")) == cible or r.get("tache", "").strip().lower() == cible.lower())]
    _ecrire(reste)
    _ecrire_cockpit(reste)
    return (avant - len(reste)) > 0


def verifier():
    """Rappels échus -> alerte vocale + marquage fait + nettoyage TTL."""
    rappels = _lire()
    now = time.time()
    change = False
    for r in rappels:
        if r.get("fait"):
            continue
        due = r.get("due") or 0
        if due <= now:
            _alerter(f"Rappel ACE777. {r.get('tache')}")
            r["fait"] = True
            change = True
    # TTL : purge les rappels échus depuis > 48h
    nettoyes = [r for r in rappels if not r.get("fait") or (now - (r.get("due") or 0)) < TTL_SEC]
    if len(nettoyes) != len(rappels):
        change = True
        rappels = nettoyes
    if change:
        _ecrire(rappels)
        _ecrire_cockpit(rappels)
    return [r for r in rappels if not r.get("fait")]


def main():
    if len(sys.argv) < 2:
        print("Usage : rappels.py ajouter|lister|supprimer|verifier")
        return 2
    cmd = sys.argv[1]
    if cmd == "ajouter":
        if len(sys.argv) < 4:
            print("Usage : rappels.py ajouter \"tâche\" \"HH:MM\"")
            return 2
        ok, res = ajouter(sys.argv[2], sys.argv[3])
        if not ok:
            print(f"[RAPPELS] erreur : {res}")
            return 1
        print(f"[RAPPELS] ajouté (#{res['id']}) : {res['tache']} -> {res['due_iso']}")
    elif cmd == "lister":
        for l in lister():
            print(f"  #{l['id']} · {l['tache']} · {l['quand']} ({l['etat']})")
    elif cmd == "supprimer":
        if len(sys.argv) < 3:
            print("Usage : rappels.py supprimer <id|texte>")
            return 2
        ok = supprimer(sys.argv[2])
        print(f"[RAPPELS] {'supprimé' if ok else 'introuvable'}")
        return 0 if ok else 1
    elif cmd == "verifier":
        restants = verifier()
        print(f"[RAPPELS] {len(restants)} rappels encore actifs")
    else:
        print("Commande inconnue.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
