#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cortana — « comment améliorer Hulk ? » (identité + état réel Hulk injecté + voix)."""
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timezone

WS = os.path.expanduser("~/ace777-test-day1/Index_Maison")
HULK = os.path.expanduser("~/ace777-test-day1/hulk-mexc")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(WS, "CORTANA_AVIS_AMELIORER_HULK_2026-08-15.md")

IDENT = os.path.join(WS, "identity", "prompts", "cortana.md")
STATE = os.path.join(HULK, "runs", "PAPER_V1_20260813_071858_state.json")
DIGEST = os.path.join(HULK, "runs", "DIGEST_LATEST.md")


def read(p, n=0):
    try:
        s = open(p, encoding="utf-8").read()
        return s if not n else s[:n]
    except Exception as e:
        return f"(indisponible: {e})"


def hulk_state_compact() -> str:
    try:
        st = json.load(open(STATE, encoding="utf-8"))
    except Exception as e:
        return f"(state indisponible: {e})"
    pos = st.get("positions") or {}
    lines = [
        f"- PnL total : {st.get('pnl_total')} USDT (base {st.get('base_notional')}$)",
        f"- Notionnel vivant : {st.get('notional_live')} USDT · trades : {st.get('trades')}",
        f"- Bags réalisés : {len(st.get('bags') or {})} (vide) · bag_dca : {len(st.get('bag_dca') or {})}",
        f"- Positions ouvertes : {len(pos)}",
    ]
    for p, d in pos.items():
        lines.append(
            f"  • {p}: regime={d.get('regime')} tension={d.get('tension')} "
            f"spread={d.get('sense_spread')}bps stake={d.get('stake')}$ "
            f"rip={d.get('rip')}% stop={d.get('stop')}%"
        )
    # vol_flag agrégé (marché mort ?)
    flags = {}
    for p, s in (st.get("scores") or {}).items():
        f = s.get("vol_flag")
        flags[f] = flags.get(f, 0) + 1
    lines.append("- Vol flags (par paire) : " + ", ".join(f"{k}={v}" for k, v in sorted(flags.items())))
    return "\n".join(lines)


def speak(text):
    if os.path.exists("/tmp/ace777_swarm_pids/.cortana_mute"):
        print("  [voix:MUETTE] mute actif — saut", file=sys.stderr)
        return 1
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        mp3 = f.name
    cmd = ["python3", "-m", "edge_tts", "--voice", "fr-FR-VivienneMultilingualNeural",
           "--rate=-15%", "--text", text, "--write-media", mp3]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if p.returncode != 0 or not os.path.exists(mp3) or os.path.getsize(mp3) < 100:
        print("  ✘ voix échouée", file=sys.stderr)
        return 1
    subprocess.run(["killall", "say"], check=False, capture_output=True)
    subprocess.run(["killall", "afplay"], check=False, capture_output=True)
    time.sleep(0.05)
    subprocess.run(["afplay", mp3], check=False, timeout=240)
    os.unlink(mp3)
    return 0


def main():
    ident = read(IDENT)
    state = hulk_state_compact()
    digest_head = read(DIGEST, 900)
    user = (
        "Question de Christophe (via le superviseur Buffy) : COMMENT AMÉLIORER HULK ?\n\n"
        "Hulk = portefeuille intelligent autonome (paper MEXC spot, 15 small-caps), stratégie "
        "dip&rip : achat dip, vente rip, mise→2×→bag (vente 50%), DCA, compound, reentry. "
        "Doctrine : moteur déterministe (paper_diprip.py) exécute SEUL, toi (Cortana) = cerveau "
        "des paramètres hors boucle d'ordre.\n\n"
        "=== ÉTAT RÉEL HULK (injecté, ne rien inventer) ===\n"
        f"{state}\n\n"
        "=== DERNIER DIGEST (début) ===\n"
        f"{digest_head}\n\n"
        "=== CE QUI VIENT D'ÊTRE FAIT (15/08) ===\n"
        "1. La veille (digest_watch.py) se pendait sur le réseau WiFi/alpage → corrigé : timeout 12s "
        "+ back-off exponentiel + circuit-breaker + deadline 90s. Digest de nouveau frais.\n"
        "2. Famille consultée (gemini 90%, nvidia 78%) : architecture 2 étages validée, transposition "
        "du moteur ACE (scalper futures BTC) ÉCARTÉE à l'unanimité → Hulk reste dédié spot.\n"
        "3. Reste à faire (validé famille) : kill-switch déterministe global + brancher Cortana en "
        "pilote de paramètres (contrat JSON).\n\n"
        "Donne ton analyse structurée (FAITS, LECTURE PHYSIQUE, PATTERN, OPINION) puis "
        "TROIS améliorations concrètes PRIORISÉES pour Hulk, en finissant par ton AVIS STRICT "
        "obligatoire (LONG|SHORT|NEUTRE / HORIZON / CONFIANCE). 8-12 phrases, concis, honnête. "
        "Si une donnée manque, dis-le. Tu n'agis sur rien : lecture et recommandation uniquement."
    )
    payload = {
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": ident},
            {"role": "user", "content": user},
        ],
        "temperature": 0.4,
        "max_tokens": 900,
    }
    req = urllib.request.Request(HUB, data=json.dumps(payload).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as r:
        d = json.loads(r.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    secs = round(time.time() - t0, 1)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# Cortana — « comment améliorer Hulk ? » ({ts}, provider {provider}, {secs}s)\n\n{content}\n")
    print(content)
    print(f"\n[provider={provider} · {secs}s · sauvegardé {OUT}]", file=sys.stderr)
    # Lecture vocale (Vivienne)
    print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
    speak("Cortana. " + content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
