#!/usr/bin/env python3
"""
VEILLE PUNK — bullshit check liens / tweets (cold path).
Backend défaut : Ollama local (gratuit). Option : OpenRouter si clé présente.

Usage:
  check "https://x.com/..."
  check "texte collé du tweet"
  veille "..."
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "out"
INBOX_DIR = ROOT / "inbox"
CONTEXT_FILE = ROOT / "CONTEXTE_PUNK.md"


def _load_obsidian_env() -> None:
    """Charge obsidian.env si OBSIDIAN_DIR pas déjà exporté."""
    if os.environ.get("OBSIDIAN_DIR"):
        return
    env_path = ROOT / "obsidian.env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export ") :]
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


_load_obsidian_env()
OBSIDIAN_ROOT = Path(
    os.environ.get(
        "OBSIDIAN_DIR",
        "/Users/christophe/Documents/Obsidian_ACE777",
    )
)
OBSIDIAN_PUNK = OBSIDIAN_ROOT / "Swarm_Bus" / "Punk"
OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_MODEL = os.environ.get("VEILLE_MODEL", "qwen2.5:3b")
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "").strip()
OPENROUTER_MODEL = os.environ.get(
    "VEILLE_OPENROUTER_MODEL", "openrouter/free"
)
MAX_LOG_ENTRIES = 12

SYSTEM = """Tu es un filtre veille crypto/AI pour un trader prudent (ACE777/Hulk).
Réponds EN FRANÇAIS, concis, structuré. Sois SCEPTIQUE envers les posts Twitter viraux (WTF, BREAKING, 245x, forever free).

Format obligatoire:
## Verdict
Une ligne: VRAI / SEMI-VRAI / BULLSHIT / INCERTAIN — puis 1 phrase.
SEMI-VRAI = technique réelle mais marketing exagéré (ex: boot 245x ≠ modèle plus fort).

## Claim
Ce que le post affirme (3 puces max).

## Preuves / trous
Vérifiable vs hype. Distingue: vitesse du harness vs qualité du LLM vs gratuité réelle.

## Utile pour ACE/Hulk/Cortana?
Oui / Non / Cold path only — 1 phrase.
ACE/Hulk = trading. Un outil coding rapide ≠ edge trading. Par défaut Cold path only ou Non.

## Action
1 ligne: ignorer / noter Obsidian / demander à Cursor (si décision code/trading).

Ne pas inventer de chiffres. Si texte pauvre → INCERTAIN."""


def http_get(url: str, timeout: int = 25) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "VeillePunk/1.0 (local research; +https://localhost)",
            "Accept": "text/html,application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        charset = "utf-8"
        ctype = resp.headers.get_content_charset()
        if ctype:
            charset = ctype
        return raw.decode(charset, errors="replace")


def fetch_url_text(url: str) -> str:
    """Essaie plusieurs miroirs pour X/Twitter et pages web."""
    url = url.strip()
    chunks: list[str] = []
    candidates = [url]
    if re.search(r"(x\.com|twitter\.com)/", url, re.I):
        # miroirs lecture (souvent plus stables que x.com nu)
        candidates = [
            f"https://r.jina.ai/{url}",
            url.replace("https://x.com/", "https://tweetlook.com/").replace(
                "https://twitter.com/", "https://tweetlook.com/"
            ),
            url,
        ]
    else:
        candidates = [f"https://r.jina.ai/{url}", url]

    errors = []
    for u in candidates:
        try:
            text = http_get(u)
            # strip grossier HTML
            text = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
            text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) > 200:
                chunks.append(f"[source:{u}]\n{text[:12000]}")
                break
            errors.append(f"{u}: trop court ({len(text)})")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{u}: {e}")
    if not chunks:
        return (
            "ECHEC_FETCH. Impossible de lire le lien automatiquement.\n"
            "Erreurs: "
            + " | ".join(errors[:4])
            + "\n→ Colle le texte du tweet après la commande, ou sauvegarde dans inbox/."
        )
    return chunks[0]


def ollama_chat(prompt: str) -> str:
    body = {
        "model": OLLAMA_MODEL,
        "stream": False,
        "options": {"temperature": 0.2},
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    }
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.load(resp)
        return (data.get("message") or {}).get("content") or data.get("response") or ""
    except urllib.error.URLError as e:
        return (
            f"ERREUR Ollama ({OLLAMA_URL}): {e}\n"
            "→ Lance: ollama serve\n"
            f"→ Vérifie le modèle: ollama pull {OLLAMA_MODEL}"
        )


def openrouter_chat(prompt: str) -> str:
    body = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "HTTP-Referer": "https://localhost/veille-punk",
            "X-Title": "VeillePunk",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"]


def load_project_context(limit_chars: int = 4500) -> str:
    if not CONTEXT_FILE.exists():
        return ""
    try:
        return CONTEXT_FILE.read_text(encoding="utf-8")[:limit_chars]
    except OSError:
        return ""


def extract_verdict_line(answer: str) -> str:
    lines = [ln.strip() for ln in answer.splitlines() if ln.strip()]
    for i, line in enumerate(lines):
        low = line.lower()
        if low.startswith("## verdict") or low == "verdict":
            # ligne suivante souvent le vrai verdict
            if i + 1 < len(lines):
                return lines[i + 1][:200]
            continue
        if re.match(r"^(VRAI|SEMI-VRAI|SEMI_VRAI|BULLSHIT|INCERTAIN)\b", line, re.I):
            return line[:200]
    return lines[0][:200] if lines else "(pas de verdict)"


def update_context_log(ts: str, user_input: str, answer: str) -> None:
    """Enrichit CONTEXTE_PUNK.md pour les prochains checks."""
    if not CONTEXT_FILE.exists():
        return
    text = CONTEXT_FILE.read_text(encoding="utf-8")
    start = "<!-- PUNK_LOG_START -->"
    end = "<!-- PUNK_LOG_END -->"
    if start not in text or end not in text:
        return
    before, rest = text.split(start, 1)
    _old, after = rest.split(end, 1)
    old_block = _old.strip()
    entries = []
    if old_block and "vide — se remplit" not in old_block:
        # split on --- entries
        for part in re.split(r"\n---\n", old_block):
            part = part.strip()
            if part:
                entries.append(part)
    verdict = extract_verdict_line(answer)
    new_entry = (
        f"### {ts}\n"
        f"- input: `{user_input[:180]}`\n"
        f"- {verdict}"
    )
    entries = [new_entry] + entries
    entries = entries[:MAX_LOG_ENTRIES]
    new_block = "\n\n---\n\n".join(entries)
    CONTEXT_FILE.write_text(
        before + start + "\n" + new_block + "\n" + end + after,
        encoding="utf-8",
    )


def save_to_obsidian(ts: str, user_input: str, backend: str, answer: str) -> Optional[Path]:
    """Dépose le digest dans le vault Obsidian (enrichit le cahier swarm)."""
    try:
        OBSIDIAN_PUNK.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"[obsidian] dossier inaccessible: {e}", file=sys.stderr)
        return None
    model = OLLAMA_MODEL if "ollama" in backend else OPENROUTER_MODEL
    body = (
        f"# Punk check — {ts}\n\n"
        f"tags: #punk #veille #cold-path\n\n"
        f"- agent: **Punk** (terminal veille)\n"
        f"- backend: `{backend}` · model: `{model}`\n"
        f"- input: `{user_input[:400]}`\n\n"
        f"{answer}\n\n"
        f"---\n"
        f"Liens: [[05_VEILLE_SECTEUR]] · contexte local `veille-punk/CONTEXTE_PUNK.md`\n"
    )
    note = OBSIDIAN_PUNK / f"CHECK_{ts}.md"
    try:
        note.write_text(body, encoding="utf-8")
        latest = OBSIDIAN_PUNK / "CHECK_LATEST.md"
        latest.write_text(body, encoding="utf-8")
        # index rolling dans Swarm_Bus
        index = OBSIDIAN_ROOT / "Swarm_Bus" / "07_PUNK_VEILLE.md"
        prev = ""
        if index.exists():
            prev = index.read_text(encoding="utf-8")
        header = (
            "# Punk — bus veille\n\n"
            f"Dernière MAJ : `{ts}`\n\n"
            f"→ note : `Swarm_Bus/Punk/CHECK_{ts}.md`\n\n"
            f"## Dernier verdict\n\n{extract_verdict_line(answer)}\n\n"
            f"## Input\n`{user_input[:300]}`\n\n"
            "---\n\n"
        )
        # keep short history
        tail = prev.split("---\n\n", 1)[-1] if "---\n\n" in prev else ""
        index.write_text(header + (tail[:6000] if tail else ""), encoding="utf-8")
        return note
    except OSError as e:
        print(f"[obsidian] écriture échouée: {e}", file=sys.stderr)
        return None


def analyze(user_input: str, force_text: bool = False) -> tuple[str, str, str]:
    raw = user_input.strip()
    source_kind = "text"
    material = raw
    if not force_text and re.match(r"https?://", raw):
        source_kind = "url"
        material = fetch_url_text(raw)
    ctx = load_project_context()
    prompt = (
        (f"## Contexte projet Punk\n{ctx}\n\n" if ctx else "")
        + f"## Matériel à évaluer ({source_kind})\n\n{material[:12000]}\n\n"
        + f"## Input utilisateur\n{raw[:2000]}"
    )
    backend = "ollama"
    if OPENROUTER_KEY and os.environ.get("VEILLE_BACKEND", "").lower() == "openrouter":
        backend = "openrouter"
        answer = openrouter_chat(prompt)
    else:
        answer = ollama_chat(prompt)
        if answer.startswith("ERREUR Ollama") and OPENROUTER_KEY:
            backend = "openrouter-fallback"
            answer = openrouter_chat(prompt)
    return backend, material[:500], answer


def save_report(user_input: str, backend: str, answer: str) -> Tuple[Path, Optional[Path]]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    path = OUT_DIR / f"CHECK_{ts}.md"
    body = (
        f"# Veille check — {ts}\n\n"
        f"- backend: `{backend}`\n"
        f"- model: `{OLLAMA_MODEL if 'ollama' in backend else OPENROUTER_MODEL}`\n"
        f"- input: `{user_input[:300]}`\n\n"
        f"{answer}\n"
    )
    path.write_text(body, encoding="utf-8")
    (OUT_DIR / "CHECK_LATEST.md").write_text(body, encoding="utf-8")
    update_context_log(ts, user_input, answer)
    obsidian_path = save_to_obsidian(ts, user_input, backend, answer)
    return path, obsidian_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Veille Punk — bullshit check")
    ap.add_argument("input", nargs="+", help="URL ou texte du tweet/post")
    ap.add_argument(
        "--text",
        action="store_true",
        help="Ne pas fetch URL, traiter comme texte brut",
    )
    ap.add_argument("--no-save", action="store_true")
    args = ap.parse_args()
    user_input = " ".join(args.input).strip()
    if not user_input:
        print("Usage: check <url|texte>", file=sys.stderr)
        return 2

    print("◆ PUNK — analyse + Obsidian…", file=sys.stderr)
    backend, _preview, answer = analyze(user_input, force_text=args.text)
    print()
    print(answer)
    print()
    if not args.no_save:
        path, obsidian_path = save_report(user_input, backend, answer)
        print(f"[sauvé] {path}", file=sys.stderr)
        if obsidian_path:
            print(f"[obsidian] {obsidian_path}", file=sys.stderr)
        else:
            print("[obsidian] non écrit (droits / chemin)", file=sys.stderr)
        print(f"[backend] {backend}", file=sys.stderr)
        print(f"[contexte] {CONTEXT_FILE} enrichi", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
