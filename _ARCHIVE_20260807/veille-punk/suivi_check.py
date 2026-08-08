#!/usr/bin/env python3
"""
Suivi Info — filtre un post d'un compte suivi vs tableau vivant Index.
Écrit A_Mon_Attention si pertinent, met à jour Attention vocale, log mémoire collab.

Usage:
  suivi "@RaoulGMI liquidité 87% ..."
  suivi "https://x.com/..."
  suivi --speak "texte…"     # + say macOS (proxy Cortana)
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT.parent / "Index_Maison"
COMPTES = INDEX / "Suivi_Info" / "COMPTES.md"
TABLEAU = INDEX / "01_TABLEAU_VIVANT.md"
ATTENTION_DIR = INDEX / "A_Mon_Attention"
ATTENTION_IDX = ATTENTION_DIR / "INDEX.md"
VOCALE_WS = ATTENTION_DIR / "ATTENTION_VOCALE.md"
OUTBOX = INDEX / "OUTBOX_OBSIDIAN"

sys.path.insert(0, str(ROOT))
from memoire_collab import log_touch  # noqa: E402
from veille_check import (  # noqa: E402
    OBSIDIAN_ROOT,
    analyze,
    extract_verdict_line,
    ollama_chat,
    OPENROUTER_KEY,
    openrouter_chat,
)

# Compte suivi → lien Index par défaut (filtre offline / secours OOM)
COMPTE_LIENS = {
    "raoulgmi": ("M1", "PERTINENT"),
    "macro_synergy": ("C16", "SOFT"),
    "ruujss": ("C17", "SOFT"),
    "undefinedki": ("M3", "SOFT"),
    "0xsomni": ("P-Graph", "SOFT"),
    "slash1sol": ("M4", "SOFT"),
        "ridark_eth": ("M2", "PERTINENT"),
        "kropanchik": ("P-Poly", "SOFT"),
        "rebelliomarket": ("D", "SOFT"),
        "milkroadai": ("M1", "SOFT"),
        "0x_punisher": ("S11", "PERTINENT"),
        "av1dlive": ("P-Graph", "SOFT"),
    }

SYSTEM_SUIVI = """Tu es le filtre « Suivi Info » du swarm ACE777 / Index Maison.
Réponds EN FRANÇAIS, concis. Sceptique du packaging Twitter.

Tu compares le post aux AMÉLIORATIONS du tableau (mindsets M1–M5, indicateurs, pistes sniper/judge/Poly, process S*).
Tu as aussi le BRIEF_IA_SNIFF : priorise Walk-Forward/OOS, Monte Carlo, Profit Factor réaliste,
frais/slippage Binance·MEXC, kill-switches, liquidité/qui paie le +1$.
REFUS bots clés-en-main, boutiques « gratuites » derrière referral exchange, PnL miracle sans fills.
Pas un signal BUY/SELL ACE. Champion jamais modifié.

Format obligatoire:
## Pertinence
Une ligne: PERTINENT / SOFT / IGNORER — puis 1 phrase.

## Lien Index
IDs touchés (ex. M1, C17, P-Sniper, S6, S9, S10) ou « aucun ».

## Résumé vocal
2–3 phrases vulgarisées, oralement naturelles (Cortana dira ça).

## Pourquoi
1–2 phrases (garder / bruit).

## Action
noter attention / ignorer / demander Cursor
"""


def load_text(path: Path, limit: int = 8000) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")[:limit]


def parse_pertinence(answer: str) -> str:
    m = re.search(
        r"##\s*Pertinence\s*\n+([^\n]+)", answer, re.I
    )
    line = (m.group(1) if m else extract_verdict_line(answer)).upper()
    for k in ("PERTINENT", "SOFT", "IGNORER"):
        if k in line:
            return k
    if "BULLSHIT" in line or "IGNOR" in line:
        return "IGNORER"
    if "SEMI" in line or "VRAI" in line:
        return "SOFT"
    return "SOFT"


def parse_section(answer: str, title: str) -> str:
    m = re.search(
        rf"##\s*{re.escape(title)}\s*\n+(.*?)(?=\n##\s|\Z)",
        answer,
        re.I | re.S,
    )
    return (m.group(1).strip() if m else "").strip()


def write_attention(ts: str, user_input: str, answer: str, pert: str) -> Path:
    ATTENTION_DIR.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^\w]+", "_", user_input[:40]).strip("_")[:40] or "post"
    note = ATTENTION_DIR / f"{ts}_{slug}.md"
    body = (
        f"# Suivi — {ts}\n\n"
        f"- **Pertinence :** {pert}\n"
        f"- **Input :** `{user_input[:300]}`\n\n"
        f"{answer}\n"
    )
    note.write_text(body, encoding="utf-8")
    line = f"- [ ] [[{note.stem}]] — {pert} · `{user_input[:80]}`\n"
    if ATTENTION_IDX.exists():
        t = ATTENTION_IDX.read_text(encoding="utf-8")
        if note.stem not in t:
            ATTENTION_IDX.write_text(t.rstrip() + "\n" + line, encoding="utf-8")
    else:
        ATTENTION_IDX.write_text("# Index — À mon attention\n\n" + line, encoding="utf-8")
    return note


def _write_mirror(rel: str, text: str) -> None:
    """Workspace toujours ; coffre si TCC OK ; sinon OUTBOX."""
    try:
        dest = OBSIDIAN_ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        return
    except OSError as e:
        print(f"[coffre] {rel}: {e}", file=sys.stderr)
    try:
        dest = OUTBOX / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print(f"[outbox] {dest}", file=sys.stderr)
    except OSError as e:
        print(f"[outbox] {rel}: {e}", file=sys.stderr)


def write_vocale(ts: str, pert: str, resume: str, lien: str, compte_hint: str) -> None:
    text = (
        f"# Attention vocale — Cortana\n\n"
        f"## Dernier résumé\n"
        f"> {resume.strip() or 'Résumé indisponible.'}\n\n"
        f"## Meta\n"
        f"- statut: READY\n"
        f"- ts: {ts}\n"
        f"- pertinence: {pert}\n"
        f"- compte: {compte_hint}\n"
        f"- lien Index: {lien or '—'}\n\n"
        f"## Règle\n"
        f"Cortana / `speak_attention` peut lire le résumé, puis repasser IDLE.\n"
    )
    VOCALE_WS.write_text(text, encoding="utf-8")
    _write_mirror("Swarm_Bus/10_ATTENTION_VOCALE.md", text)
    _write_mirror("Index_Maison/A_Mon_Attention/ATTENTION_VOCALE.md", text)


def speak(resume: str) -> None:
    msg = "Veille Index. " + re.sub(r"\s+", " ", resume)[:500]
    try:
        subprocess.run(["say", "-v", "Thomas", msg], check=False)
    except FileNotFoundError:
        print("[speak] commande say indisponible", file=sys.stderr)


def sync_note_coffre(note: Path) -> None:
    body = note.read_text(encoding="utf-8")
    _write_mirror(f"A_Mon_Attention/{note.name}", body)
    _write_mirror(f"Index_Maison/A_Mon_Attention/{note.name}", body)
    for name in ("MEMOIRE_COLLAB.md", "01_TABLEAU_VIVANT.md"):
        src = INDEX / name
        if src.exists():
            _write_mirror(f"Index_Maison/{name}", src.read_text(encoding="utf-8"))
    comptes = INDEX / "Suivi_Info" / "COMPTES.md"
    if comptes.exists():
        _write_mirror(
            "Index_Maison/Suivi_Info/COMPTES.md",
            comptes.read_text(encoding="utf-8"),
        )


def offline_filter(user_input: str, material: str) -> str:
    """Filtre secours sans LLM (Mac 8 Go / Ollama OOM)."""
    low = (user_input + " " + material).lower()
    compte = "—"
    lien, pert = "aucun", "IGNORER"
    m = re.search(r"@([A-Za-z0-9_]+)", user_input)
    if m:
        compte = "@" + m.group(1)
        key = m.group(1).lower()
        if key in COMPTE_LIENS:
            lien, pert = COMPTE_LIENS[key]
    # mots-clés Index → boost
    boosts = [
        ("liquidit", "M1", "PERTINENT"),
        ("rrp", "M1", "PERTINENT"),
        ("beta.?binomial|brier|sniper|bucket", "M2", "PERTINENT"),
        ("hmm|régime|regime", "C17", "SOFT"),
        ("judge|daemon|graphe|graph", "M3", "SOFT"),
        ("prove me wrong|context", "M4", "SOFT"),
        ("polymarket|poly ", "P-Poly", "SOFT"),
        ("walk.?forward|out.?of.?sample|monte.?carlo|profit.?factor|overfit", "S9", "PERTINENT"),
        ("funding|slippage|spread|maker|taker|post.?only", "S10", "PERTINENT"),
        ("kill.?switch|hard.?stop|heartbeat|rate.?limit", "S2", "SOFT"),
    ]
    for pat, lid, p in boosts:
        if re.search(pat, low):
            lien, pert = lid, p
            break
    snippet = re.sub(r"\s+", " ", material.strip())[:280]
    resume = (
        f"Compte {compte}. Lien probable {lien}, verdict {pert}. "
        f"Idée: {snippet}"
    )
    return (
        f"## Pertinence\n{pert} — filtre offline (pas de LLM).\n\n"
        f"## Lien Index\n{lien}\n\n"
        f"## Résumé vocal\n{resume}\n\n"
        f"## Pourquoi\nSecours Ollama/mémoire : mapping compte + mots-clés vs tableau.\n\n"
        f"## Action\nnoter attention\n"
    )


def ensure_coffre_bus_index() -> None:
    """Ajoute 09/10 au LIRE_MOI Swarm_Bus si possible."""
    p = OBSIDIAN_ROOT / "Swarm_Bus" / "00_LIRE_MOI.md"
    try:
        if not p.exists():
            return
        t = p.read_text(encoding="utf-8")
        if "09_MEMOIRE_COLLAB" in t:
            return
        extra = (
            "\n| [[09_MEMOIRE_COLLAB]] | **Mémoire collab** — journal de ce qu’on touche |\n"
            "| [[10_ATTENTION_VOCALE]] | Résumé oral Cortana (Suivi Info) |\n"
        )
        if "| [[08_LECONS]]" in t:
            t = t.replace("| [[08_LECONS]] | Leçons |", "| [[08_LECONS]] | Leçons |" + extra)
        else:
            t = t.rstrip() + "\n" + extra
        p.write_text(t, encoding="utf-8")
    except OSError:
        pass


def main() -> int:
    ap = argparse.ArgumentParser(description="Suivi Info → Attention + Cortana")
    ap.add_argument("text", nargs="+", help="URL ou texte du post")
    ap.add_argument("--speak", action="store_true", help="Dire le résumé (say)")
    ap.add_argument("--force-note", action="store_true", help="Noter même si IGNORER")
    ap.add_argument(
        "--offline",
        action="store_true",
        help="Filtre sans LLM (secours Mac 8 Go / Ollama OOM)",
    )
    args = ap.parse_args()
    user_input = " ".join(args.text).strip()
    if not user_input:
        print("usage: suivi \"@compte post…\"", file=sys.stderr)
        return 2

    comptes = load_text(COMPTES)
    tableau = load_text(TABLEAU)
    brief = load_text(INDEX / "BRIEF_IA_SNIFF.md", limit=4000)
    from veille_check import fetch_url_text

    material = user_input
    if re.match(r"https?://", user_input):
        material = fetch_url_text(user_input)

    prompt = (
        f"## Brief IA sniff (intérêts Christophe)\n{brief}\n\n"
        f"## Comptes suivis\n{comptes}\n\n"
        f"## Tableau vivant (améliorations)\n{tableau}\n\n"
        f"## Post à évaluer\n{material[:10000]}\n\n"
        f"## Input brut\n{user_input[:1500]}"
    )
    import veille_check as vc

    if args.offline or os.environ.get("VEILLE_OFFLINE", "").lower() in ("1", "true", "yes"):
        answer = offline_filter(user_input, material)
        backend = "offline"
    else:
        old = vc.SYSTEM
        vc.SYSTEM = SYSTEM_SUIVI
        try:
            if OPENROUTER_KEY and os.environ.get("VEILLE_BACKEND", "").lower() == "openrouter":
                answer = openrouter_chat(prompt)
                backend = "openrouter"
            else:
                answer = ollama_chat(prompt)
                backend = "ollama"
                if answer.startswith("ERREUR") and OPENROUTER_KEY:
                    answer = openrouter_chat(prompt)
                    backend = "openrouter-fallback"
                elif answer.startswith("ERREUR"):
                    print("[suivi] Ollama KO → filtre offline", file=sys.stderr)
                    answer = offline_filter(user_input, material)
                    backend = "offline-fallback"
        finally:
            vc.SYSTEM = old

    if answer.startswith("ERREUR"):
        print(answer, file=sys.stderr)
        print("Abandon: pas de note (LLM en erreur).", file=sys.stderr)
        return 1

    pert = parse_pertinence(answer)
    resume = parse_section(answer, "Résumé vocal") or parse_section(answer, "Resume vocal")
    lien = parse_section(answer, "Lien Index")
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    compte_hint = user_input.split()[0][:40] if user_input.startswith("@") else "—"

    print(answer)
    print("\n——")
    print(f"Pertinence parsée: {pert} · backend={backend}")

    ensure_coffre_bus_index()

    if pert in ("PERTINENT", "SOFT") or args.force_note:
        note = write_attention(ts, user_input, answer, pert)
        write_vocale(ts, pert, resume, lien, compte_hint)
        sync_note_coffre(note)
        log_touch(
            "Punk",
            "+",
            f"A_Mon_Attention/{note.name}",
            f"Suivi {pert} · {backend} · {user_input[:50]}",
        )
        print(f"Note: {note}")
        if args.speak or pert == "PERTINENT":
            speak(resume or answer[:300])
    else:
        log_touch(
            "Punk",
            "★",
            "Suivi_Info",
            f"IGNORER · {user_input[:60]}",
        )
        print("Ignoré (pas de note attention).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
