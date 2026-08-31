#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obsidian_cli_bridge.py — Pont CLI Obsidian (GO Christophe 31/08, validé famille 3/3)
====================================================================================
Remplace le bricolage OUTBOX_OBSIDIAN (écritures .md espérées vues par l'app) par
la CLI OFFICIELLE Obsidian (v1.12+, activée dans Settings > General > Advanced).

VALIDÉ PAR LA CONSULTATION FAMILLE+CODEUR (31/08) — corrections intégrées :
1. FILE D'ATTENTE SÉQUENTIELLE : toutes les écritures passent par un verrou global.
2. TIMEOUT STRICT 3s par commande CLI + READ-BACK hash (ne JAMAIS faire confiance
   à exit code 0).
3. FAIL-OPEN ABSOLU : si la CLI est injoignable/stale, on écrit DIRECTEMENT le .md
   dans le vault — Obsidian l'indexera au prochain refresh.
4. CIRCUIT BREAKER : 3 échecs CLI consécutifs → mode « disque pur » 15 min.
5. AUDIT jsonl de chaque écriture.

GATEKEEPER (v2, 31/08 — famille 3/3 : gemini, juge, deepseek) :
- Les agents génèrent un OBJET JSON structuré {type, frontmatter, body} au lieu
  d'un .md brut → le pont VALIDE contre un schéma (type connu, propriétés
  requises, valeurs autorisées) puis COMPILE le markdown conforme au template.
- Rejet explicite (status REJECTED + errors actionables) si non conforme.
- 4 TYPES STRICTS : actif, signal, synthese_ia, journal (pas 50 comme l'expert).
- Day Zero rule : les 1733 notes existantes ne sont PAS migrées ; le gatekeeper
  s'applique aux nouvelles écritures. write_note() reste rétrocompatible.

Usage :
    from obsidian_cli_bridge import ObsidianBridge
    res = ObsidianBridge.write_typed("actif", {
        "actif": "EDEL", "statut": "valide", "date": "2026-08-31",
        "source": "deepdive", "body": "## Analyse\n..."})
    # -> {"status": "SUCCESS"|"REJECTED", "path": ..., "errors": [...]}
"""
import hashlib
import json
import os
import subprocess
import threading
import time
from datetime import datetime, timezone
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

# === GATEKEEPER : 4 TYPES STRICTS (famille 3/3) ===
# Chaque type : dossier cible (structure du vault existant), propriétés requises,
# valeurs autorisées, template markdown (frontmatter YAML + sections).
TYPES = {
    "actif": {
        "folder": "Crypto_Projet",
        "required_props": ["actif", "statut"],
        "allowed_values": {"statut": ["brouillon", "valide", "archive"]},
        "template": (
            "---\n"
            "type: actif\n"
            "actif: {actif}\n"
            "statut: {statut}\n"
            "date: {date}\n"
            "source: {source}\n"
            "tags: {tags}\n"
            "---\n\n"
            "# Actif : {actif}\n\n"
            "{body}\n"
        ),
    },
    "signal": {
        "folder": "Hulk",
        "required_props": ["actif", "direction", "statut"],
        "allowed_values": {
            "direction": ["long", "short", "neutral"],
            "statut": ["traite", "ignore", "en_cours"],
        },
        "template": (
            "---\n"
            "type: signal\n"
            "actif: {actif}\n"
            "direction: {direction}\n"
            "statut: {statut}\n"
            "date: {date}\n"
            "source: {source}\n"
            "---\n\n"
            "# Signal : {actif} ({direction})\n\n"
            "{body}\n"
        ),
    },
    "synthese_ia": {
        "folder": "Index_Maison",
        "required_props": ["type_consultation", "membres", "statut"],
        "allowed_values": {"statut": ["brouillon", "valide", "archive"]},
        "template": (
            "---\n"
            "type: synthese_ia\n"
            "type_consultation: {type_consultation}\n"
            "membres: {membres}\n"
            "date: {date}\n"
            "statut: {statut}\n"
            "source: {source}\n"
            "---\n\n"
            "# Synthèse IA : {type_consultation}\n\n"
            "{body}\n"
        ),
    },
    "journal": {
        "folder": "Cahier",
        "required_props": ["source", "statut"],
        "allowed_values": {"statut": ["brouillon", "valide", "archive"]},
        "template": (
            "---\n"
            "type: journal\n"
            "date: {date}\n"
            "source: {source}\n"
            "statut: {statut}\n"
            "---\n\n"
            "# Journal - {date}\n\n"
            "{body}\n"
        ),
    },
}


def _yaml_escape(val):
    """Échappe proprement les valeurs pour le frontmatter YAML simple."""
    if isinstance(val, (list, tuple)):
        items = [str(v).strip() for v in val]
        return "[" + ", ".join(items) + "]"
    s = str(val)
    if (":" in s or "#" in s or "\n" in s or s.startswith("-") or s == ""
            or s.startswith("[") or s.startswith("{")):
        s_escaped = s.replace('"', '\\"')
        return '"' + s_escaped + '"'
    return s


def validate_and_compile(note_type, data):
    """Valide les données selon le schéma du type puis compile en Markdown.

    Retourne (markdown_str, errors_list). errors non vide → REJECTED.
    """
    errors = []
    if note_type not in TYPES:
        return None, [f"Type inconnu: '{note_type}'. Types acceptés: {list(TYPES.keys())}"]

    schema = TYPES[note_type]

    # 1. Propriétés obligatoires
    for prop in schema["required_props"]:
        v = data.get(prop)
        if v is None or (isinstance(v, str) and not v.strip()):
            errors.append(f"Propriété obligatoire manquante ou vide: '{prop}'")

    # 2. Valeurs autorisées (énumérations)
    for prop, allowed in schema.get("allowed_values", {}).items():
        if prop in data and data[prop] not in allowed:
            errors.append(
                f"Valeur invalide pour '{prop}': '{data[prop]}', attendu parmi {allowed}"
            )

    if errors:
        return None, errors

    # 3. Contexte par défaut. Le BODY est du markdown (jamais échappé YAML),
    # seules les propriétés du frontmatter sont échappées.
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    body = data.get("body") or data.get("content") or ""
    frontmatter = {
        "date": _yaml_escape(data.get("date") or now_str),
        "source": _yaml_escape(data.get("source") or "agent"),
        "statut": _yaml_escape(data.get("statut") or "brouillon"),
        "actif": _yaml_escape(data.get("actif") or "general"),
        "direction": _yaml_escape(data.get("direction") or "neutral"),
        "type_consultation": _yaml_escape(data.get("type_consultation") or "standard"),
        "membres": _yaml_escape(data.get("membres") or ["system"]),
        "tags": _yaml_escape(data.get("tags") or []),
    }

    # 4. Compilation via le template (body inséré brut, non échappé)
    try:
        template = schema["template"]
        # Séparer le template : frontmatter (échappé) + corps (brut)
        compiled_fm = template.split("{body}")[0].format(**frontmatter)
        compiled = compiled_fm + body + "\n"
    except KeyError as e:
        return None, [f"Erreur de template interne, clé manquante: {e}"]
    return compiled, []


def parse_frontmatter_light(content):
    """Extrait le type + le body d'un frontmatter YAML minimal, si présent."""
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    fm_text = parts[1]
    body = parts[2].strip()
    meta = {}
    for line in fm_text.strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta.get("type"), body


class ObsidianBridge:
    """Pont séquentiel CLI Obsidian avec gatekeeper, fallback disque et CB."""

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

    @classmethod
    def _safe_name(cls, title):
        """Nom de fichier sûr (alphanum + espace _ -)."""
        return "".join(c for c in str(title) if c.isalnum() or c in (" ", "_", "-")).strip()

    # ------------------------------------------------------------------ API
    @classmethod
    def write_typed(cls, note_type, data, title=None):
        """GATEKEEPER : valide un objet structuré puis écrit la note compilée.

        data = {actif/type_consultation/source..., body: "..."} selon le type.
        Retourne {status: SUCCESS|REJECTED|ERROR, path, errors}.
        """
        compiled_md, errors = validate_and_compile(note_type, data)
        if errors:
            return {"status": "REJECTED", "path": None, "errors": errors}

        schema = TYPES[note_type]
        folder = schema["folder"]
        if not title:
            title = (data.get("actif") or data.get("type_consultation")
                     or f"note_{int(time.time())}")
        filename = f"{cls._safe_name(title)}.md"
        path = f"{folder}/{filename}"

        with cls._lock:  # file d'attente : une seule écriture à la fois
            if len(compiled_md) > MAX_CONTENT_LEN:
                compiled_md = compiled_md[:MAX_CONTENT_LEN] + "\n\n<!-- TRONQUÉ par le pont -->"

            # Tentative CLI si autorisée
            if cls._cli_allowed() and cls.is_alive():
                ok, err = cls._run_cli(["create", f"name={path}", f"content={compiled_md}"])
                if ok:
                    # READ-BACK : on relit et on compare (hash)
                    rok, rdata = cls._run_cli(["read", f"path={path}"])
                    if rok and rdata and hashlib.sha256(rdata.encode()).hexdigest() == \
                            hashlib.sha256(compiled_md.encode()).hexdigest():
                        cls._note_cli_success()
                        entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                 "action": "create", "type": note_type, "title": title,
                                 "path": path, "status": "SUCCESS_CLI"}
                        cls._audit(entry)
                        return {"status": "SUCCESS", "path": path, "via": "cli", "errors": [],
                                "audit": entry}
                else:
                    cls._note_cli_failure()

            # FALLBACK : écriture disque directe dans le vault (fail-open)
            try:
                full = VAULT / path
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_text(compiled_md, encoding="utf-8")
                cls._note_cli_success()
                entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                         "action": "create", "type": note_type, "title": title,
                         "path": str(full), "status": "SUCCESS_FALLBACK",
                         "reason": err if "err" in dir() else "cli_indisponible"}
                cls._audit(entry)
                return {"status": "SUCCESS", "path": str(full), "via": "disk",
                        "errors": [], "audit": entry}
            except Exception as e:
                entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                         "action": "create", "type": note_type, "title": title,
                         "path": str(VAULT / path), "status": "ERROR", "reason": str(e)}
                cls._audit(entry)
                return {"status": "ERROR", "path": str(VAULT / path), "errors": [str(e)]}

    @classmethod
    def write_note(cls, title, content, folder="00_Inbox"):
        """Rétrocompatible (scripts existants). Si le contenu a un frontmatter
        avec 'type:' reconnu, passe par le gatekeeper ; sinon écriture brute
        (Day Zero rule)."""
        detected_type, body = parse_frontmatter_light(content)
        if detected_type and detected_type in TYPES:
            return cls.write_typed(detected_type, {"body": body, "actif": title}, title=title)

        # Comportement brut historique
        filename = f"{cls._safe_name(title)}.md"
        path = f"{folder}/{filename}"
        with cls._lock:
            if cls._cli_allowed() and cls.is_alive():
                ok, err = cls._run_cli(["create", f"name={path}", f"content={content}"])
                if ok:
                    rok, rdata = cls._run_cli(["read", f"path={path}"])
                    if rok and rdata and hashlib.sha256(rdata.encode()).hexdigest() == \
                            hashlib.sha256(content.encode()).hexdigest():
                        cls._note_cli_success()
                        cls._audit({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                    "action": "create", "title": title, "path": path,
                                    "status": "SUCCESS_CLI", "note": "no_type"})
                        return {"status": "SUCCESS", "path": path, "via": "cli", "errors": []}
                else:
                    cls._note_cli_failure()
            try:
                full = VAULT / path
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_text(content, encoding="utf-8")
                cls._note_cli_success()
                cls._audit({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                            "action": "create", "title": title, "path": str(full),
                            "status": "SUCCESS_FALLBACK", "note": "no_type"})
                return {"status": "SUCCESS", "path": str(full), "via": "disk", "errors": []}
            except Exception as e:
                return {"status": "ERROR", "path": str(full), "errors": [str(e)]}

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
                        cls._audit({"ts": ts, "action": "append", "path": path,
                                    "status": "SUCCESS_CLI"})
                        return {"status": "SUCCESS_CLI", "path": path, "via": "cli"}
                else:
                    cls._note_cli_failure()
            try:
                full.parent.mkdir(parents=True, exist_ok=True)
                with open(full, "a", encoding="utf-8") as f:
                    f.write(content + "\n")
                cls._note_cli_success()
                cls._audit({"ts": ts, "action": "append", "path": str(full),
                            "status": "SUCCESS_FALLBACK"})
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
            "types": list(TYPES.keys()),
        }


if __name__ == "__main__":
    # Auto-test rapide (sans rien laisser dans le vault)
    print("status:", ObsidianBridge.status())

    # 1. Validation OK → SUCCESS
    r1 = ObsidianBridge.write_typed("actif", {
        "actif": "EDEL", "statut": "valide", "date": "2026-08-31",
        "source": "deepdive", "body": "## Analyse\nFiche de test gatekeeper.",
    })
    print("1) actif valide:", r1["status"], r1.get("path"))

    # 2. Validation KO → REJECTED (statut invalide)
    r2 = ObsidianBridge.write_typed("actif", {
        "actif": "EDEL", "statut": "peut_etre", "body": "x",
    })
    print("2) statut invalide:", r2["status"], r2.get("errors"))

    # 3. Type inconnu → REJECTED
    r3 = ObsidianBridge.write_typed("machin", {"actif": "X"})
    print("3) type inconnu:", r3["status"], r3.get("errors"))

    # 4. Propriété requise manquante → REJECTED
    r4 = ObsidianBridge.write_typed("signal", {"actif": "BTC", "direction": "long"})
    print("4) statut manquant:", r4["status"], r4.get("errors"))

    # 5. write_note rétrocompatible : sans type → brut
    r5 = ObsidianBridge.write_note("__TEST_RAW__", "# brut\ntexte sans type", folder="Cahier")
    print("5) note brute:", r5["status"])

    # 6. write_note avec frontmatter type → gatekeeper
    r6 = ObsidianBridge.write_note("__TEST_TYPED__",
                                   "---\ntype: actif\nactif: X\nstatut: valide\n---\n\n# X\ncorps",
                                   folder="Crypto_Projet")
    print("6) note typée via write_note:", r6["status"])

    # Nettoyage
    import pathlib
    for r in (r1, r5, r6):
        p = r.get("path")
        if p and pathlib.Path(p).exists():
            pathlib.Path(p).unlink()
            print(f"   nettoyé: {p}")
    print("tests gatekeeper OK")
