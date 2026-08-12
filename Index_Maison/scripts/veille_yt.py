#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
veille_yt.py — La veille YouTube automatique (11/08, v4)
=========================================================
1 lien YouTube -> 1 dossier de preuve, sans rien configurer.

Usage :
  python3 veille_yt.py "https://youtube.com/watch?v=..."   # lien donne
  python3 veille_yt.py                                     # lien lu dans le presse-papiers
  python3 veille_yt.py --fichier transcription.txt         # analyser un texte deja transcrit

Ce que ca fait, tout seul :
  1. Recupere les sous-titres de la video (yt-dlp, pas de telechargement video),
     en conservant les MINUTES dans la transcription (preuve sourcee)
  2. Envoie la transcription au hub (task veille.youtube -> Gemini)
  3. Ecrit le DOSSIER DE PREUVE dans Evaluations/VEILLE_YT_*.md
     (source + citations minute par minute + impact strategie)
  4. Affiche le verdict a l'ecran

Zéro usine a gaz : un seul script, un seul appel, fichier range tout seul.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/v1/chat/completions"
HEALTH = HUB.replace("/v1/chat/completions", "/health")
TASK = "veille.youtube"
# yt-dlp via venv Python 3.12 : la version systeme (py3.9) est plafonnee a 2025.10.14,
# trop vieille pour les protections YouTube 2026 (PO token). Le venv a la derniere
# version (2026.07.04, testee 11/08).
YTDLP = [os.path.expanduser("~/.venv-yt/bin/yt-dlp")]
if not os.path.isfile(YTDLP[0]):
    YTDLP = ["python3", "-m", "yt_dlp"]  # repli systeme
EVAL_DIR = os.path.expanduser("~/Documents/Obsidian_ACE777/Evaluations")
MAX_CAR = 24000  # garde : ne pas noyer le modele
CLIENTS_YT = ["android", "web_embedded", "ios", "tv"]  # android passe sans PO token (08/2026)


def extraire_lien_yt(texte):
    """Extrait la 1re URL YouTube d'un texte (presse-papiers souvent 'titre + lien')."""
    m = re.search(r"https?://(?:www\.)?(?:youtube\.com|youtu\.be)/\S+", texte or "")
    return m.group(0).rstrip(".,);") if m else ""


def lire_presse_papiers():
    """Lit le presse-papiers macOS (pbpaste)."""
    try:
        out = subprocess.run(["pbpaste"], capture_output=True, timeout=5)
        return out.stdout.decode("utf-8", errors="replace").strip()
    except Exception:
        return ""


def titre_video(url):
    """Recupere le titre (appel leger --get-title). Echec = id de la video."""
    try:
        r = subprocess.run(
            YTDLP + ["--get-title", "--no-playlist", "--no-warnings", "--quiet", url],
            capture_output=True, timeout=60, text=True)
        t = r.stdout.strip().splitlines()
        if t and t[0].strip():
            return t[0].strip()
    except Exception:
        pass
    m = re.search(r"[?&]v=([A-Za-z0-9_-]{6,})", url)
    return m.group(1) if m else "video"


def recuperer_sous_titres(url):
    """Telecharge les sous-titres (auto, fr puis en) sans telecharger la video.
    Dossier temp UNIQUE par execution (pas de sous-titres peimes d'une autre video).
    Patience : YouTube renvoie parfois HTTP 429 (trop de requetes) — on reessaie.
    NB : --print title fait sortir yt-dlp SANS ecrire les sous-titres -> appels separes."""
    outdir = tempfile.mkdtemp(prefix="veille_yt_")
    base = os.path.join(outdir, "%(id)s")
    derniere_erreur = ""
    for client in CLIENTS_YT:
        for tentative in range(8):
            cmd = YTDLP + [
                "--skip-download", "--write-auto-subs", "--write-subs",
                "--sub-langs", "fr.*,en.*", "--sub-format", "vtt/best",
                "--extractor-args", f"youtube:player_client={client}",
                "-o", base, "--no-playlist", "--no-warnings", "--quiet", url,
            ]
            r = subprocess.run(cmd, capture_output=True, timeout=180, text=True)
            vtts = [f for f in os.listdir(outdir) if f.endswith(".vtt")]
            if vtts:
                vtts.sort(key=lambda f: (0 if ".fr" in f else 1, f))
                path = os.path.join(outdir, vtts[0])
                return path, vtts[0]
            derniere_erreur = r.stderr[-200:]
            if "429" in (r.stderr or "") and tentative < 7:
                print("   (YouTube limite les requetes — nouvelle tentative dans 10 s)", file=sys.stderr)
                time.sleep(10)
                continue
            break  # erreur non-429 : ce client ne marche pas, on passe au suivant
    raise RuntimeError(
        "Pas de sous-titres trouves pour cette video (fr/en absents). "
        f"[derniere tentative : {derniere_erreur}]"
    )


def vtt_en_texte(path):
    """Transforme un .vtt en texte propre, en GARDANT les minutes [mm:ss] par segment
    (preuve sourcee : Gemini pourra citer 'a 3:42 il dit...')."""
    segments = []
    current = []
    for raw in open(path, encoding="utf-8", errors="replace"):
        line = raw.strip()
        if "-->" in line:
            # debut d'un nouveau segment : on flushe le precedent, horodatage -> [mm:ss]
            if current:
                segments.append(" ".join(current))
            m = re.match(r"(\d{2}):(\d{2}):(\d{2})", line)
            if m:
                mi, s = int(m.group(2)), int(m.group(3))
                current = [f"[{mi:02d}:{s:02d}]"]
            continue
        if not line or line.startswith("WEBVTT") or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        line = re.sub(r"<[^>]+>", "", line)        # balises <c>, <00:00:19.039>
        line = re.sub(r"\{\\.*?\}", "", line)      # balises de style vtt
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            current.append(line)
    if current:
        segments.append(" ".join(current))
    return " ".join(segments)


def call_hub(texte, meta):
    """Envoie la transcription au hub -> Gemini -> dossier de preuve."""
    consigne = (
        "Tu es l'analyste de veille de la maison ACE777. "
        "Tu viens de lire la transcription d'une video d'analyse, avec des "
        "horodatages [mm:ss] en debut de chaque passage. "
        "Produis un DOSSIER DE PREUVE en francais, strictement au format :\n"
        "\n"
        "📌 Source : <chaine/date>\n"
        "🗣️ En 3 phrases, ce que dit le youtuber\n"
        "🔑 Points cles (liste courte, CHACUN avec sa minute [mm:ss] si presente)\n"
        "🔄 Impact sur notre strategie :\n"
        "   - ➕ NOUVEAU : <infos nouvelles>\n"
        "   - ⚠️ CONTREDIT : <ce qui contredit nos analyses, a verifier>\n"
        "   - ✅ CONFIRME : <ce qui confirme ce qu'on sait deja>\n"
        "🧠 MON AVIS (ton avis a TOI, pas une paraphrase) :\n"
        "   - Verdict : <d'accord / pas d'accord / mitigé> avec le youtuber, en 1 ligne\n"
        "   - Pourquoi : <ton raisonnement propre, 2-3 lignes max>\n"
        "🎯 PREDICTIONS VERIFIABLES (extrait de la video ET de ton avis) :\n"
        "   Chaque prediction sur UNE ligne, format :\n"
        "   - [date_limite YYYY-MM-DD] <critere mesurable et precis> (source : youtuber / moi)\n"
        "   Exemples : [2026-08-31] BTC depasse 66 000 USD au moins une fois (source : youtuber)\n"
        "   [2026-08-18] ETH surperforme BTC sur 7 jours (source : moi)\n"
        "   IMPORTANT : uniquement des affirmations VERIFIABLES avec date limite. "
        "   Si la video n'en contient aucune, ecris '- aucune prediction verifiable'.\n"
        "📎 Decision : <rien a faire / a surveiller / a integrer> — une seule phrase.\n"
        "\n"
        "Sois factuel : ne cite QUE ce qui est reellement dans la transcription, "
        "avec la minute exacte quand elle existe. "
        "Si rien ne contredit rien, ecris '- ⚠️ CONTREDIT : rien'. "
        "Si la transcription est une chanson ou un contenu sans analyse, dis-le "
        "honnetement au lieu d'inventer."
    )
    payload = {
        "task": TASK,
        "messages": [
            {"role": "system", "content": consigne},
            {"role": "user", "content": (
                f"Transcription (video : {meta['titre']} — {meta['url']}):\n\n"
                + texte[:MAX_CAR]
            )},
        ],
        "max_tokens": 1500,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?")


def main():
    ap = argparse.ArgumentParser(description="Veille YouTube automatique -> dossier de preuve")
    ap.add_argument("url", nargs="?", default=None, help="lien YouTube (sinon lu dans le presse-papiers)")
    ap.add_argument("--fichier", default=None, help="analyser un texte deja transcrit (sans yt-dlp)")
    args = ap.parse_args()

    # 1) trouver le lien : argument, presse-papiers, ou fichier
    url = args.url or ""
    if not url and not args.fichier:
        clip = lire_presse_papiers()
        url = extraire_lien_yt(clip)
        if url:
            print(f"[i] lien lu dans le presse-papiers : {url[:60]}...")
        else:
            print("[X] Donne un lien YouTube en argument (ou copie le lien puis relance).",
                  file=sys.stderr)
            sys.exit(1)
    if url and not re.search(r"(youtube\.com|youtu\.be)/", url):
        print("[X] Ce n'est pas un lien YouTube.", file=sys.stderr)
        sys.exit(1)

    # 2) hub vivant ?
    try:
        with urllib.request.urlopen(HEALTH, timeout=5) as r:
            json.loads(r.read().decode())
    except Exception:
        print("[X] Hub :11435 injoignable. Lance le hub, puis relance.", file=sys.stderr)
        sys.exit(1)

    # 3) recuperer le texte
    try:
        if args.fichier:
            texte = open(args.fichier, encoding="utf-8", errors="replace").read()
            meta = {"titre": os.path.basename(args.fichier), "url": args.fichier}
            print("[i] analyse du fichier transcrit ...", flush=True)
        else:
            print("[i] recuperation des sous-titres (yt-dlp, pas de telechargement video) ...", flush=True)
            sub_path, sub_name = recuperer_sous_titres(url)
            texte = vtt_en_texte(sub_path)
            meta = {"titre": titre_video(url), "url": url}
            print(f"[i] transcription : {sub_name} — {len(texte)} caracteres", flush=True)
            if len(texte) > MAX_CAR:
                print(f"   (transcription longue : {len(texte)} caracteres — tronquee a {MAX_CAR} pour l'analyse)", flush=True)
        if len(texte) < 50:
            print("[X] Transcription trop courte/vide — sous-titres inutilisables.", file=sys.stderr)
            sys.exit(1)
    except RuntimeError as e:
        print(f"[X] {e}", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("[X] Telechargement des sous-titres trop long (internet ? youtube bloque ?).",
              file=sys.stderr)
        sys.exit(1)

    # 4) analyse par le hub
    try:
        print("[i] la Reine analyse (hub -> Gemini) ...", flush=True)
        analyse, provider = call_hub(texte, meta)
    except urllib.error.HTTPError as e:
        print(f"[X] le hub a repondu HTTP {e.code} : {e.read().decode()[:300]}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[X] analyse impossible : {e}", file=sys.stderr)
        sys.exit(1)

    # 5) dossier de preuve range dans Evaluations/
    os.makedirs(EVAL_DIR, exist_ok=True)
    jour = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = re.sub(r"[^\w]+", "_", meta["titre"])[:40].strip("_")
    out_path = os.path.join(EVAL_DIR, f"VEILLE_YT_{jour}_{slug}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"date: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H%MZ')}\n")
        f.write(f"source: {meta['url']}\n")
        f.write(f"agent: hub ({TASK} : gemini)\n")
        f.write("type: veille_youtube\n")
        f.write("---\n\n")
        f.write(f"# Veille YouTube — {meta['titre']}\n\n")
        f.write(f"Lien : {meta['url']}\n\n")
        f.write(analyse + "\n")

    print("")
    print("━━━ 📋 VEILLE TERMINÉE ━━━")
    print(analyse)
    print(f"━━━━ (provider : {provider}) ━━━━")
    print("")
    print(f"[OK] Dossier de preuve : {out_path}")


if __name__ == "__main__":
    main()
