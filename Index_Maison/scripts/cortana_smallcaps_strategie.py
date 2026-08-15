#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cortana — stratégie small caps ACE777 (thèse Christophe + Canton + verdict famille) + voix."""
import json, os, subprocess, sys, tempfile, time, urllib.request
from datetime import datetime, timezone

WS = os.path.expanduser("~/ace777-test-day1/Index_Maison")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(WS, "CORTANA_AVIS_SMALLCAPS_2026-08-15.md")
IDENT = os.path.join(WS, "identity", "prompts", "cortana.md")


def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception as e:
        return f"(indisponible: {e})"


def speak(text):
    if os.path.exists("/tmp/ace777_swarm_pids/.cortana_mute"):
        print("  [voix:MUETTE] mute actif — saut", file=sys.stderr)
        return
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        mp3 = f.name
    cmd = ["python3", "-m", "edge_tts", "--voice", "fr-FR-VivienneMultilingualNeural",
           "--rate=-15%", "--text", text, "--write-media", mp3]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if p.returncode != 0 or not os.path.exists(mp3) or os.path.getsize(mp3) < 100:
        print("  ✘ voix échouée", file=sys.stderr)
        return
    subprocess.run(["killall", "say"], check=False, capture_output=True)
    subprocess.run(["killall", "afplay"], check=False, capture_output=True)
    time.sleep(0.05)
    subprocess.run(["afplay", mp3], check=False, timeout=240)
    os.unlink(mp3)


def main():
    ident = read(IDENT)
    user = (
        "Christophe (via Buffy) te demande ton avis sur SA stratégie small caps pour Hulk.\n\n"
        "THÈSE DE CHRISTOPHE (règle d'exception) : ses 15 small caps ne sont pas « du fun » mais des "
        "projets à gros potentiel d'adoption, suivis depuis longtemps, adossés à de l'institutionnel, "
        "délibérément tenus sous le radar du mainstream. Donc manque de liquidité et dumps = occasions "
        "d'accumuler des BAGS, pas des fuites. XRP et HBAR sortent de cette logique.\n\n"
        "VÉRIFICATION (web, cas Canton Network / CC, tiré au hasard) : participants institutionnels "
        "vérifiés (Goldman Sachs, BNY Mellon, CBOE, Microsoft, Moody's, Deutsche Börse, BNP Paribas…), "
        "token d'utilité, tokenomics « no pre-mine, no VC unlock » + burn-and-mint, « not chasing "
        "headlines ». Ça confirme la thèse structurelle.\n\n"
        "VERDICT FAMILLE (gemini 70% / nvidia 72%, GO-AVEC-RÉSERVE) : thèse fondée pour les projets à "
        "adoption institutionnelle vérifiable, NON généralisable à tous les small caps. Recommandation : "
        "2 classes de paires (A core liquides = règles actuelles ; B small caps bag = filtres assouplis, "
        "mais taille max 5-10%, horizon bag ≥12 mois, PAS de stop technique → stop fondamental, max 20% "
        "du portefeuille, rééval trimestrielle).\n\n"
        "Donne TON avis structuré (FAITS, LECTURE PHYSIQUE, PATTERN, OPINION) : la thèse est-elle juste ? "
        "Quels pièges vois-tu ? Comment toi, en tant que cerveau de Hulk, piloterais-tu ces 2 classes ? "
        "Termine par ton AVIS STRICT obligatoire (LONG|SHORT|NEUTRE / HORIZON / CONFIANCE). "
        "8-12 phrases, honnête, chiffres exacts. Tu n'agis sur rien."
    )
    payload = {
        "task": "cortana.analyse",
        "messages": [{"role": "system", "content": ident},
                     {"role": "user", "content": user}],
        "temperature": 0.4, "max_tokens": 900,
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
        f.write(f"# Cortana — stratégie small caps ({ts}, provider {provider}, {secs}s)\n\n{content}\n")
    print(content)
    print(f"\n[provider={provider} · {secs}s · {OUT}]", file=sys.stderr)
    print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
    speak("Cortana. " + content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
