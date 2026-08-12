#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
watch_chaines.py — Veille automatique des chaînes YouTube (11/08)
================================================================
Surveille la LISTE_YOUTUBERS.md, detecte les nouvelles videos (hors shorts),
les analyse via le hub (veille_yt.py -> Gemini), et met a jour le
REGISTRE_PREDICTIONS.md (le carnet qui permettra de verifier si l'IA avait raison).

Usage :
  python3 watch_chaines.py              # scan + analyse des nouvelles videos
  python3 watch_chaines.py --force      # re-analyse tout (ignore l'etat)
  python3 watch_chaines.py --max 3      # limite de videos par scan (defaut : 3)

La liste des chaines (LISTE_YOUTUBERS.md) :
  ## nom de la chaine
  handle: https://www.youtube.com/@Nom
  # ou directement :
  channel_id: UCxxxxxxxxxxxxxxxxxxxxxx
  # (la premiere fois, le script resout le handle -> channel_id automatiquement)

Fichiers :
  LISTE_YOUTUBERS.md        -> la liste (VOUS la gardez a jour)
  ~/.watch_chaines/etat.json -> les videos deja vues (le script s'en souvient)
  REGISTRE_PREDICTIONS.md   -> le carnet des predictions (a verifier plus tard)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

# NOTE (11/08) : macOS TCC bloque l'ecriture dans ~/Documents pour les jobs launchd.
# Le travail de veille vit donc dans un dossier NON protege (Index_Maison/veille_yt/),
# et une copie vers Obsidian/Evaluations est faite EN PLUS quand les droits le permettent
# (lancement manuel dans le terminal).
BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison/veille_yt")
ETAT_PATH = os.path.join(BASE, "etat.json")
LISTE_PATH = os.path.join(BASE, "LISTE_YOUTUBERS.md")
REGISTRE_PATH = os.path.join(BASE, "REGISTRE_PREDICTIONS.md")
OBSIDIAN_EVAL = os.path.expanduser("~/Documents/Obsidian_ACE777/Evaluations")
VEILLE_SCRIPT = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts/veille_yt.py")
RSS = "https://www.youtube.com/feeds/videos.xml?channel_id={}"
DUREE_MAX_SHORT_S = 75  # les shorts YouTube font moins d'1 min 15


def copier_vers_obsidian():
    """Copie liste + registre vers Obsidian SI les droits le permettent (manuel oui, launchd non)."""
    try:
        os.makedirs(OBSIDIAN_EVAL, exist_ok=True)
        import shutil
        for src, dst in ((LISTE_PATH, os.path.join(OBSIDIAN_EVAL, "LISTE_YOUTUBERS.md")),
                         (REGISTRE_PATH, os.path.join(OBSIDIAN_EVAL, "REGISTRE_PREDICTIONS.md"))):
            if os.path.isfile(src):
                shutil.copy(src, dst)
        return True
    except Exception:
        return False


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")


def lire_liste():
    """Parse LISTE_YOUTUBERS.md -> [{nom, channel_id}]."""
    if not os.path.isfile(LISTE_PATH):
        print(f"[X] Liste introuvable : {LISTE_PATH}", file=sys.stderr)
        sys.exit(1)
    chaines = []
    nom = ""
    channel_id = ""
    dans_commentaire = False
    for raw in open(LISTE_PATH, encoding="utf-8"):
        line = raw.strip()
        if line.startswith("<!--"):
            dans_commentaire = True
            continue
        if dans_commentaire:
            if "-->" in line:
                dans_commentaire = False
            continue
        if line.startswith("## "):
            if nom and channel_id:
                chaines.append({"nom": nom, "channel_id": channel_id})
            nom = line[3:].strip()
            channel_id = ""
        elif line.startswith("channel_id:"):
            channel_id = line.split(":", 1)[1].strip()
        elif line.startswith("handle:"):
            handle = line.split(":", 1)[1].strip()
            cid = resoudre_handle(handle)
            if cid:
                channel_id = cid
    if nom and channel_id:
        chaines.append({"nom": nom, "channel_id": channel_id})
    if not chaines:
        print("[X] Aucune chaine trouvee dans la liste (format : ## nom + channel_id: ou handle:).",
              file=sys.stderr)
        sys.exit(1)
    return chaines


def resoudre_handle(handle):
    """Handle -> channel_id via yt-dlp (repli si le RSS direct ne marche pas)."""
    try:
        r = subprocess.run(
            ["/Users/christophe/.venv-yt/bin/yt-dlp", "--print", "channel_id",
             "--no-warnings", "--quiet", handle],
            capture_output=True, text=True, timeout=90)
        cid = r.stdout.strip()
        if cid.startswith("UC"):
            return cid
    except Exception:
        pass
    return ""


def duree_video(url):
    """Duree de la video en secondes (via yt-dlp --get-duration). 0 si inconnu."""
    try:
        r = subprocess.run(
            ["/Users/christophe/.venv-yt/bin/yt-dlp", "--get-duration",
             "--no-warnings", "--quiet", url],
            capture_output=True, text=True, timeout=90)
        return float(r.stdout.strip() or 0)
    except Exception:
        return 0


def videos_du_rss(channel_id):
    """Videos recentes d'une chaine : [(video_id, titre, publie_iso)]."""
    url = RSS.format(channel_id)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"   [i] RSS impossible pour {channel_id} : {e}", file=sys.stderr)
        return []
    root = ET.fromstring(data)
    ns = {"yt": "http://www.youtube.com/xml/schemas/2015",
          "media": "http://search.yahoo.com/mrss/",
          "atom": "http://www.w3.org/2005/Atom"}
    out = []
    for entry in root.findall("atom:entry", ns):
        vid = entry.findtext("yt:videoId", "", ns)
        titre = entry.findtext("atom:title", "", ns)
        publie = entry.findtext("atom:published", "", ns)
        if vid:
            out.append((vid, titre, publie))
    return out


def charger_etat():
    if os.path.isfile(ETAT_PATH):
        try:
            return json.load(open(ETAT_PATH))
        except Exception:
            return {}
    return {}


def sauver_etat(etat):
    os.makedirs(BASE, exist_ok=True)
    json.dump(etat, open(ETAT_PATH, "w"), indent=1, ensure_ascii=False)


def ligne_registre(vid, titre, analyse):
    """Extrait les lignes 🎯 PREDICTIONS de l'analyse pour le registre."""
    lignes = []
    en_pred = False
    for line in analyse.splitlines():
        s = line.strip()
        if s.startswith("🎯 PREDICTIONS") or s.startswith("PREDICTIONS"):
            en_pred = True
            continue
        if en_pred:
            if s.startswith(("📎", "🧠", "🔄", "📌", "🗣", "🔑", "##")):
                en_pred = False
                continue
            if s.startswith("-") and "[" in s and "]" in s:
                lignes.append(s.lstrip("- ").strip())
    return lignes


def mettre_a_jour_registre(entries):
    """Entries : [{date, video_id, titre, url, chaine, predictions:[...]}].
    Ajoute en TETE, PRESERVE toutes les entrées existantes (les anciennes
    restent en dessous — le banc d'essai doit accumuler dans le temps)."""
    os.makedirs(os.path.dirname(REGISTRE_PATH), exist_ok=True)
    ancien = ""
    if os.path.isfile(REGISTRE_PATH):
        ancien = open(REGISTRE_PATH, encoding="utf-8").read()
    # corps existant = tout ce qui suit la 1re entrée (### ), i.e. toutes les entrées passées
    m = re.search(r"^### .*", ancien, re.S | re.M)
    corps = ancien[m.start():] if m else ""
    # en-tête fixe
    entete = (
        "---\n"
        f"date: {now_iso()}\n"
        "type: registre_predictions\n"
        "---\n\n"
        "# 📓 Registre des prédictions — la vérification du banc d'essai\n\n"
        "Chaque prédiction est notée avec sa date limite. Le script "
        "`verifier_predictions.py` re-vérifie les échues (statut VRAIE/FAUSSE/NON VÉRIFIABLE).\n\n"
    )
    # nouvelles entrées (en tête)
    nouvelles = ""
    for e in entries:
        nouvelles += f"### {e['date']} — {e['chaine']} : {e['titre']}\n"
        nouvelles += f"Lien : {e['url']}\n\n"
        if e["predictions"]:
            for p in e["predictions"]:
                nouvelles += f"- ⏳ EN ATTENTE | {p}\n"
        else:
            nouvelles += "- _(aucune prédiction vérifiable extraite)_\n"
        nouvelles += "\n"
    with open(REGISTRE_PATH, "w", encoding="utf-8") as f:
        f.write(entete + nouvelles + corps)


def analyser_video(vid, titre, chaine):
    url = f"https://www.youtube.com/watch?v={vid}"
    print(f"   ▶ analyse de : {titre[:60]}...", flush=True)
    r = subprocess.run(
        ["python3", VEILLE_SCRIPT, url],
        capture_output=True, text=True, timeout=600)
    return r.stdout, r.returncode


def main():
    ap = argparse.ArgumentParser(description="Veille auto des chaînes YouTube")
    ap.add_argument("--force", action="store_true", help="re-analyser tout (ignore l'état)")
    ap.add_argument("--max", type=int, default=3, help="max de videos par scan (defaut 3)")
    args = ap.parse_args()

    if not os.path.isfile(VEILLE_SCRIPT):
        print(f"[X] veille_yt.py introuvable : {VEILLE_SCRIPT}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(BASE, exist_ok=True)
    etat = charger_etat()
    chaines = lire_liste()
    print(f"[i] {len(chaines)} chaine(s) surveillee(s) — scan RSS ...", flush=True)

    nouvelles = []  # [(chaine, vid, titre, publie)]
    for c in chaines:
        vids = videos_du_rss(c["channel_id"])
        vues = etat.get(c["channel_id"], {}).get("vues", [])
        for vid, titre, publie in vids:
            if vid in vues and not args.force:
                continue
            nouvelles.append((c, vid, titre, publie))

    if not nouvelles:
        print("[i] Aucune nouvelle video. Rien a faire.")
        return

    print(f"[i] {len(nouvelles)} nouvelle(s) video(s) — limite : {args.max}/scan")
    nouvelles = nouvelles[:args.max]

    entries = []
    marquees = {c["channel_id"]: [] for c in chaines}
    for c, vid, titre, publie in nouvelles:
        url = f"https://www.youtube.com/watch?v={vid}"
        # filtre les shorts : duree < 75s = pas d'analyse (mais marquee vue : pas de re-scan)
        duree = duree_video(url)
        if 0 < duree < DUREE_MAX_SHORT_S:
            print(f"   ⏭ short ignore : {titre[:50]} ({int(duree)}s)", flush=True)
            marquees[c["channel_id"]].append(vid)
            continue
        print(f"[i] {c['nom']} : {titre} ({int(duree)}s)" if duree else f"[i] {c['nom']} : {titre}", flush=True)
        stdout, rc = analyser_video(vid, titre, c["nom"])
        if rc != 0 or "VEILLE TERMINÉE" not in stdout:
            print(f"   [X] echec analyse {titre[:50]} (YouTube rate-limit ?) — sera retente au prochain scan", file=sys.stderr)
            continue  # PAS marquee vue : on reessaiera
        # decoupe la sortie : garde le bloc analyse (entre les ━━━)
        m = re.search(r"━━━ 📋 VEILLE TERMINÉE ━━━\n(.*?)\n━━━━", stdout, re.S)
        analyse = m.group(1) if m else stdout
        preds = ligne_registre(vid, titre, analyse)
        entries.append({
            "date": now_iso(), "video_id": vid, "titre": titre,
            "url": url, "chaine": c["nom"], "predictions": preds,
        })
        marquees[c["channel_id"]].append(vid)
        print(analyse, flush=True)
        print("", flush=True)

    # marquer VUES uniquement ce qui a ete reellement traite (analyse OK ou short filtre)
    if not args.force:
        for cid, vids in marquees.items():
            if not vids:
                continue
            vues = etat.setdefault(cid, {}).setdefault("vues", [])
            etat[cid]["vues"] = vues + [v for v in vids if v not in vues]
        sauver_etat(etat)

    if entries:
        mettre_a_jour_registre(entries)
        print(f"[OK] {len(entries)} video(s) analysee(s) — registre mis a jour : {REGISTRE_PATH}")
    # copie vers Obsidian si les droits le permettent (silencieux si non)
    if copier_vers_obsidian():
        print(f"[OK] copie vers Obsidian : {OBSIDIAN_EVAL}")
    else:
        print("[i] (obsidian non accessible ici — lancement manuel requis pour la copie)")


if __name__ == "__main__":
    main()
