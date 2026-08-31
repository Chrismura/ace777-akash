# CODEUR (provider Google Gemini)

Voici le code complet et mis à jour de `obsidian_cli_bridge.py`. Ce script intègre le **Gatekeeper** tel que défini par la famille, tout en restant compatible avec Python 3.9 et en utilisant exclusivement la bibliothèque standard (sans `PyYAML`).

```python
#!/usr/bin/env python3
"""
obsidian_cli_bridge.py
Pont Python vers la CLI Obsidian avec Gatekeeper intégré (v2.0 - Gatekeeper).
Implémentation standard lib (Python 3.9+), supporte l'écriture typée et validée.
"""

import datetime
import json
import os
import re
import subprocess
import threading
import time

# =====================================================================
# CONFIGURATION & CONSTANTES
# =====================================================================
OBSIDIAN_VAULT_PATH = os.environ.get(
    "OBSIDIAN_VAULT_PATH", "/path/to/your/Index_Maison"
)
AUDIT_LOG_PATH = os.path.join(
    OBSIDIAN_VAULT_PATH, "scripts", ".ace777_bridge_audit.jsonl"
)

# =====================================================================
# A) SCHÉMAS ET TEMPLATES DU GATEKEEPER
# =====================================================================

TYPES = {
    "actif": {
        "folder": "02_Actifs",
        "required_props": ["actif", "statut"],
        "allowed_values": {
            "statut": ["brouillon", "valide", "archive"],
        },
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
        "folder": "03_Signaux",
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
            "---\n\n"
            "# Signal : {actif} ({direction})\n\n"
            "{body}\n"
        ),
    },
    "synthese_ia": {
        "folder": "04_Syntheses",
        "required_props": ["type_consultation", "membres", "statut"],
        "allowed_values": {
            "statut": ["brouillon", "valide", "archive"],
        },
        "template": (
            "---\n"
            "type: synthese_ia\n"
            "type_consultation: {type_consultation}\n"
            "membres: {membres}\n"
            "date: {date}\n"
            "statut: {statut}\n"
            "---\n\n"
            "# Synthèse IA : {type_consultation}\n\n"
            "{body}\n"
        ),
    },
    "journal": {
        "folder": "05_Journaux",
        "required_props": ["source", "statut"],
        "allowed_values": {
            "statut": ["brouillon", "valide", "archive"],
        },
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

# =====================================================================
# GESTIONNAIRE DE CIRCUIT BREAKER ET THREADING (ÉTAT INTERNE)
# =====================================================================
_bridge_lock = threading.Lock()
_cli_failures = 0
_circuit_open_until = 0.0
CIRCUIT_THRESHOLD = 3
CIRCUIT_TIMEOUT = 900  # 15 minutes


# =====================================================================
# UTILITAIRES YAML & COMPILATION MARKDOWN
# =====================================================================
def _yaml_escape(val):
    """Échappe proprement les valeurs pour le YAML simple."""
    if isinstance(val, list):
        # Format liste YAML inline ex: [gemini, juge]
        items = [str(v).strip() for v in val]
        return "[" + ", ".join(items) + "]"
    s = str(val)
    if ":" in s or "#" in s or "\n" in s or s.startswith("-") or s == "":
        s_escaped = s.replace('"', '\\"')
        return f'"{s_escaped}"'
    return s


def parse_frontmatter_light(content):
    """Extrait un frontmatter minimal si présent pour détecter le type."""
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
    return meta.get("type"), content


# =====================================================================
# MOTEUR DE VALIDATION GATEKEEPER
# =====================================================================
def validate_and_compile(note_type, data):
    """Valide les données selon le type strict et compile en Markdown.

    Retourne (markdown_str, errors_list)
    """
    errors = []

    if note_type not in TYPES:
        return None, [
            f"Type inconnu: '{note_type}'. Types acceptés: {list(TYPES.keys())}"
        ]

    schema = TYPES[note_type]

    # 1. Vérification des propriétés obligatoires
    for prop in schema["required_props"]:
        if prop not in data or data[prop] is None or data[prop] == "":
            errors.append(f"Propriété obligatoire manquante: '{prop}'")

    # 2. Vérification des valeurs autorisées (énumérations)
    if "allowed_values" in schema:
        for prop, allowed in schema["allowed_values"].items():
            if prop in data and data[prop] not in allowed:
                errors.append(
                    f"Valeur invalide pour '{prop}': '{data[prop]}', attendu parmi {allowed}"
                )

    if errors:
        return None, errors

    # 3. Préparation des valeurs par défaut pour le template
    now_str = datetime.datetime.now().isoformat()
    context = {
        "date": data.get("date", now_str),
        "source": data.get("source", "agent"),
        "statut": data.get("statut", "brouillon"),
        "actif": data.get("actif", "general"),
        "direction": data.get("direction", "neutral"),
        "type_consultation": data.get("type_consultation", "standard"),
        "membres": data.get("membres", ["system"]),
        "body": data.get("body", data.get("content", "")),
    }

    # Échappement YAML de toutes les variables du contexte
    escaped_context = {k: _yaml_escape(v) for k, v in context.items()}

    # 4. Compilation via le template
    try:
        compiled_md = schema["template"].format(**escaped_context)
    except KeyError as e:
        return None, [f"Erreur de template interne, clé manquante: {e}"]

    return compiled_md, []


# =====================================================================
# COEUR DU PONT OBSIDIAN (CLI & DISQUE)
# =====================================================================
def is_alive():
    """Vérifie si la CLI Obsidian répond."""
    try:
        res = subprocess.run(
            ["obsidian", "status"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        return res.returncode == 0
    except Exception:
        return False


def _audit_log(entry):
    """Enregistre l'écriture dans le fichier d'audit jsonl."""
    try:
        os.makedirs(os.path.dirname(AUDIT_LOG_PATH), exist_ok=True)
        with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _write_via_cli(path, content):
    """Tente d'écrire via la CLI Obsidian avec timeout."""
    cmd = ["obsidian", "write", "--path", path, "--content", content]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
    if res.returncode != 0:
        raise RuntimeError(f"CLI error: {res.stderr.strip()}")
    return True


def _read_vault_file(path):
    """Lit directement depuis le disque pour le read-back hash."""
    full_path = os.path.join(OBSIDIAN_VAULT_PATH, path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    return None


def _write_disk_fallback(path, content):
    """Écriture directe sur disque (fail-open absolu)."""
    full_path = os.path.join(OBSIDIAN_VAULT_PATH, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def _core_write_pipeline(path, content, source_mode):
    """Pipeline sécurisé : Lock -> CLI -> Readback Hash -> Fallback Disque + Circuit Breaker."""
    global _cli_failures, _circuit_open_until

    with _bridge_lock:
        now = time.time()
        use_cli = True

        # Vérification Circuit Breaker
        if _cli_failures >= CIRCUIT_THRESHOLD:
            if now < _circuit_open_until:
                use_cli = False
            else:
                # Reset après expiration du timeout
                _cli_failures = 0

        success = False
        method_used = "cli"

        if use_cli:
            try:
                _write_via_cli(path, content)
                # Read-back de contrôle
                read_back = _read_vault_file(path)
                if read_back and content.strip() in read_back:
                    success = True
                    _cli_failures = 0  # Succès, reset des échecs
                else:
                    raise RuntimeError("Read-back verification failed.")
            except Exception as e:
                _cli_failures += 1
                if _cli_failures >= CIRCUIT_THRESHOLD:
                    _circuit_open_until = now + CIRCUIT_TIMEOUT
                use_cli = False

        if not use_cli or not success:
            # Fallback disque direct
            try:
                _write_disk_fallback(path, content)
                method_used = (
                    "disk_fallback" if _cli_failures > 0 else "disk_direct"
                )
                success = True
            except Exception as ex:
                _audit_log(
                    {
                        "timestamp": datetime.datetime.now().isoformat(),
                        "path": path,
                        "status": "FAILED",
                        "error": str(ex),
                    }
                )
                raise RuntimeError(
                    f"Échec critique écriture disque: {str(ex)}"
                )

        # Audit de l'opération
        _audit_log(
            {
                "timestamp": datetime.datetime.now().isoformat(),
                "path": path,
                "method": method_used,
                "mode": source_mode,
                "status": "SUCCESS",
            }
        )
        return True


# =====================================================================
# FONCTIONS PUBLIQUES (API DU PONT)
# =====================================================================


def write_typed(note_type, data, title=None):
    """B) GATEKEEPER : Valide et écrit une note structurée.

    Retourne un dict: {status: "SUCCESS"|"REJECTED", path: str, errors: list}
    """
    compiled_md, errors = validate_and_compile(note_type, data)
    if errors:
        return {"status": "REJECTED", "path": None, "errors": errors}

    # Détermination du titre et du chemin cible
    schema = TYPES[note_type]
    folder = schema["folder"]

    # Si pas de titre fourni, on prend 'actif' ou 'type_consultation' ou timestamp
    if not title:
        title = (
            data.get("actif")
            or data.get("type_consultation")
            or f"note_{int(time.time())}"
        )

    # Nettoyage sécurisé du nom de fichier
    safe_title = "".join(
        c for c in str(title) if c.isalnum() or c in (" ", "_", "-")
    ).strip()
    filename = f"{safe_title}.md"
    rel_path = f"{folder}/{filename}"

    try:
        _core_write_pipeline(rel_path, compiled_md, source_mode="typed")
        return {"status": "SUCCESS", "path": rel_path, "errors": []}
    except Exception as e:
        return {"status": "ERROR", "path": rel_path, "errors": [str(e)]}


def write_note(title, content, folder="00_Inbox"):
    """C) Rétrocompatibilité + Gatekeeper automatique.

    Si le contenu contient un frontmatter valide avec 'type:', passe par le gatekeeper.
    Sinon, écriture brute (Day Zero Rule préservée pour les scripts existants).
    """
    detected_type, _ = parse_frontmatter_light(content)

    if detected_type and detected_type in TYPES:
        # Extraction basique du body après le frontmatter pour le passer au gatekeeper
        parts = content.split("---", 2)
        body_content = parts[2].strip() if len(parts) >= 3 else content
        data = {"body": body_content, "actif": title}
        return write_typed(detected_type, data, title=title)

    # Comportement brut historique (Day Zero)
    safe_title = "".join(
        c for c in str(title) if c.isalnum() or c in (" ", "_", "-")
    ).strip()
    filename = f"{safe_title}.md"
    rel_path = f"{folder}/{filename}"

    try:
        _core_write_pipeline(rel_path, content, source_mode="raw_legacy")
        _audit_log(
            {
                "timestamp": datetime.datetime.now().isoformat(),
                "path": rel_path,
                "note": "no_type",
            }
        )
        return {"status": "SUCCESS", "path": rel_path, "errors": []}
    except Exception as e:
        return {"status": "ERROR", "path": rel_path, "errors": [str(e)]}


def append(path, content):
    """Ajoute du contenu à la fin d'un fichier existant (sans validation stricte)."""
    with _bridge_lock:
        full_path = os.path.join(OBSIDIAN_VAULT_PATH, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "a", encoding="utf-8") as f:
            f.write("\n" + content)
        _audit_log(
            {
                "timestamp": datetime.datetime.now().isoformat(),
                "path": path,
                "mode": "append",
                "status": "SUCCESS",
            }
        )
        return
