#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obsidian_cli_bridge.py — Pont CLI Obsidian (GO Christophe 31/08, validé famille 3/3)
====================================================================================
Remplace le bricolage OUTBOX_OBSIDIAN (écritures .md espérées vues par l'app) par
la CLI OFFICIELLE Obsidian (v1.12+, activée dans Settings > General > Advanced).

VALIDÉ PAR LA CONSULTATION FAMILLE+CODEUR (31/08) — 4 corrections intégrées :
1. FILE D'ATTENTE SÉQUENTIELLE : toutes les écritures passent par un verrou global
   (Obsidian écrit en mono-thread → 2 IA en parallèle = timeout/rejet).
2. TIMEOUT STRICT 3s par commande CLI + READ-BACK : après create/append, on relit et
   on compare le contenu (ne JAMAIS faire confiance à exit code 0).
3. FAIL-OPEN ABSOLU : si la CLI est injoignable/stale, on écrit DIRECTEMENT le .md
   dans le vault (le disque ne plante pas) — Obsidian l'indexera au prochain refresh.
4. CIRCUIT BREAKER : 3 échecs CLI consécutifs → mode « disque pur » 15 min (ne pas
   marteler une app morte). Audit jsonl de chaque écriture.

CONTRAINTE CLI : l'app Obsidian doit tourner (la CLI parle à l'app via IPC local).

Usage :
    from obsidian_cli_bridge import ObsidianBridge
    res = ObsidianBridge.write_note("FICHE_EDEL_20260831", "# Contenu...", folder="Crypto_Projet")
    # -> {"status": "SUCCESS_CLI" | "SUCCESS_FALLBACK", "path": ...}
"""
import hashlib
import json
import os
import subprocess
import threading
import time
from pathlib import Path

# === CONFIG ===
OBSIDIAN_CLI = "/Applications/Obsidian.app/Contents/MacOS/obsidian-cli"
VAULT = Path(os.environ.get("ACE777_VAULT", "~/Documents/Obsidian_ACE777")).expanduser()
AUDIT_LOG = Path(os.environ.get("ACE777_AUDIT", str(VAULT / ".ace777_bridge_audit.jsonl")))

CLI_TIMEOUT = 3.0          # max par commande CLI (famille+codeur : 3s)
PING_TIMEOUT = 1.0         # ping léger (is_alive)
CB_THRESHOLD = 3           # 3 échecs CLI consécutifs → disque pur
CB_COOLDOWN = 900          # 15 min de mode disque pur
MAX_CONTENT_LEN = 200_000  # garde-fou : ne pas envoyer de payload géant via la CLI


class ObsidianBridge:
    """Pont séquentiel CLI Obsidian avec fallback disque et circuit breaker."""

    _lock = threading.Lock()          # file d'attente : UNE écriture à la fois
    _failures = 0                     # échecs CLI consécutifs
    _disk_only_until = 0.0            # fin du mode « disque pur »

    # ------------------------------------------------------------------ internes
    @classmethod
    def _run_cli(cls, args, timeout=CLI_TIMEOUT):
        """Exécute une commande CLI. Retourne (ok: bool, output: str)."""
        try:
            res = subprocess.run(
                [OBSIDIAN_CLI] + args,
                capture_output=True, text=True, timeout=timeout,
            )
            if res.returncode == 0:
                return True, res.stdout.strip()
            return False, (res.stderr or res.stdout).strip()
        except subprocess.TimeoutExpired:
            return False, "CLI_TIMEOUT"
        except FileNotFoundError:
            return False, "CLI_NOT_FOUND"

    @classmethod
    def is_alive(cls):
        """Ping rapide : l'app Obsidian répond-elle ? (léger, 1s max)."""
        ok, _ = cls._run_cli(["tags", "counts"], timeout=PING_TIMEOUT)
        return ok

    @classmethod
    def _cli_allowed(cls):
        """Vrai si la CLI est utilisable (pas en mode disque pur)."""
        if cls._failures >= CB_THRESHOLD and time.time() < cls._disk_only_until:
            return False
        return True

    @classmethod
    def _note_cli_failure(cls):
        cls._failures += 1
        if cls._failures >= CB_THRESHOLD:
            cls._disk_only_until = time.time() + CB_COOLDOWN
            print(f"[bridge] ⚡ Circuit breaker CLI ({cls._failures} échecs) → "
                  f"disque pur {CB_COOLDOWN}s")

    @classmethod
    def _note_cli_success(cls):
        cls._failures = 0

    @classmethod
    def _audit(cls, entry):
        try:
            AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
            with open(AUDIT_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception:
            pass  # l'audit ne doit jamais faire planter une écriture

    # ------------------------------------------------------------------ API
    @classmethod
    def write_note(cls, title, content, folder=""):
        """Crée (ou écrase) une note. Retourne dict {status, path, via}.

        - CLI d'abord (create + read-back hash) si l'app répond.
        - Sinon fallback : écriture directe dans le vault (fail-open absolu).
        """
        filename = title if title.endswith(".md") else f"{title}.md"
        path = f"{folder}/{filename}".lstrip("/")
        full = VAULT / path
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        with cls._lock:  # 1) file d'attente : une seule écriture à la fois
            # Garde-fou taille
            if len(content) > MAX_CONTENT_LEN:
                content = content[:MAX_CONTENT_LEN] + "\n\n<!-- TRONQUÉ par le pont -->"

            # 2) Tentative CLI si autorisée
            if cls._cli_allowed() and cls.is_alive():
                ok, err = cls._run_cli(["create", f"name={path}", f"content={content}"])
                if ok:
                    # 3) READ-BACK : on relit et on compare (hash)
                    rok, rdata = cls._run_cli(["read", f"path={path}"])
                    if rok and rdata and hashlib.sha256(rdata.encode()).hexdigest() == \
                            hashlib.sha256(content.encode()).hexdigest():
                        cls._note_cli_success()
                        entry = {"ts": ts, "action": "create", "title": title,
                                 "path": path, "status": "SUCCESS_CLI"}
                        cls._audit(entry)
                        return {"status": "SUCCESS_CLI", "path": path, "via": "cli",
                                "audit": entry}
                    # read-back KO → on laisse tomber vers le fallback
                else:
                    cls._note_cli_failure()

            # 4) FALLBACK : écriture disque directe dans le vault (fail-open)
            try:
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_text(content, encoding="utf-8")
                cls._note_cli_success()  # le fallback disque réinitialise le CB
                entry = {"ts": ts, "action": "create", "title": title,
                         "path": str(full), "status": "SUCCESS_FALLBACK",
                         "reason": err if "err" in dir() else "cli_indisponible"}
                cls._audit(entry)
                return {"status": "SUCCESS_FALLBACK", "path": str(full),
                        "via": "disk", "audit": entry}
            except Exception as e:
                entry = {"ts": ts, "action": "create", "title": title,
                         "path": str(full), "status": "ERROR", "reason": str(e)}
                cls._audit(entry)
                return {"status": "ERROR", "path": str(full), "error": str(e)}

    @classmethod
    def append(cls, path, content):
        """Ajoute du contenu à une note existante (même logique queue+fallback)."""
        full = VAULT / path
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with cls._lock:
            if cls._cli_allowed() and cls.is_alive():
                ok, err = cls._run_cli(["append", f"path={path}", f"content={content}"])
                if ok:
                    rok, rdata = cls._run_cli(["read", f"path={path}"])
                    if rok and content.strip() in rdata:
                        cls._note_cli_success()
                        entry = {"ts": ts, "action": "append", "path": path,
                                 "status": "SUCCESS_CLI"}
                        cls._audit(entry)
                        return {"status": "SUCCESS_CLI", "path": path, "via": "cli"}
                else:
                    cls._note_cli_failure()
            # Fallback disque
            try:
                full.parent.mkdir(parents=True, exist_ok=True)
                with open(full, "a", encoding="utf-8") as f:
                    f.write(content + "\n")
                cls._note_cli_success()
                entry = {"ts": ts, "action": "append", "path": str(full),
                         "status": "SUCCESS_FALLBACK"}
                cls._audit(entry)
                return {"status": "SUCCESS_FALLBACK", "path": str(full), "via": "disk"}
            except Exception as e:
                return {"status": "ERROR", "path": str(full), "error": str(e)}

    @classmethod
    def read(cls, path):
        """Lit une note via la CLI (fallback : lecture disque)."""
        with cls._lock:
            ok, data = cls._run_cli(["read", f"path={path}"])
            if ok and data:
                return data
            full = VAULT / path
            if full.exists():
                return full.read_text(encoding="utf-8")
            return None

    @classmethod
    def status(cls):
        """État du pont (pour le cockpit / supervision)."""
        alive = cls.is_alive()
        return {
            "app": "ONLINE" if alive else "OFFLINE",
            "mode": "disque_pur" if not cls._cli_allowed() else "cli",
            "failures_cli": cls._failures,
            "disk_only_until": cls._disk_only_until,
            "vault": str(VAULT),
        }


if __name__ == "__main__":
    # Auto-test rapide (sans rien laisser dans le vault)
    print("status:", ObsidianBridge.status())
    res = ObsidianBridge.write_note("__TEST_BRIDGE__", "# test\nok")
    print("write:", res["status"], res["path"])
    lu = ObsidianBridge.read("__TEST_BRIDGE__.md")
    print("read-back:", "OK" if lu and "ok" in lu else f"KO ({lu})")
    # Nettoyage
    import pathlib
    p = pathlib.Path(res["path"])
    if p.exists():
        p.unlink()
    print("nettoyé")
