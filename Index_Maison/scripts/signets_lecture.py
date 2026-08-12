#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
signets_lecture.py — Lecteur de signets X avec résumé IA (ACE777)
Rôle : résume chaque nouveau bookmark de Signets_X via le hub (task
analyste.strategie, Gemini rapide), cache atomique, quota 15/jour.
Corrigé par le superviseur (2026-08-12) : URL hub 11435, timeout=None,
écriture atomique mkstemp, cache corrompu préservé.
"""

import os
import sys
import re
import json
import hashlib
import datetime
import tempfile
import urllib.request
from pathlib import Path

# === Configuration (convention ACE777) ===
HOME = Path.home()
SIGNETS_DIR = HOME / "Documents/Obsidian_ACE777/Signets_X"
CACHE_DIR = HOME / "ace777-test-day1/Index_Maison/strategie"
CACHE_FILE = CACHE_DIR / "SIGNETS_RESUMES.json"
LOCK_FILE = CACHE_DIR / "SIGNETS_RESUMES.lock"
STOP_STRATEGIE = CACHE_DIR / "STOP"
STOP_ALL = HOME / "ace777-test-day1/Index_Maison/STOP_ALL"

MAX_PAR_JOUR = 50
TASK_NAME = "analyste.strategie"
HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"


# === Utilitaires ===
def verifier_kill_switch():
    if STOP_STRATEGIE.exists() or STOP_ALL.exists():
        print("[KILL] Kill switch activé. Arrêt propre.")
        sys.exit(0)


def _pid_vivant(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except Exception:
        return False


def acquerir_verrou():
    """Verrou exclusif O_EXCL avec détection de PID mort (macOS)."""
    try:
        fd = os.open(str(LOCK_FILE), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return True
    except FileExistsError:
        try:
            pid = int(open(LOCK_FILE).read().strip() or "0")
        except Exception:
            pid = 0
        if pid and not _pid_vivant(pid):
            try:
                os.unlink(str(LOCK_FILE))
                return acquerir_verrou()
            except Exception:
                return False
        print("[LOCK] Un autre processus est en cours. Sortie.")
        return False
    except Exception:
        return False


def liberer_verrou():
    try:
        os.unlink(str(LOCK_FILE))
    except Exception:
        pass


def sha12(chaine: str) -> str:
    return hashlib.sha256(chaine.encode("utf-8")).hexdigest()[:12]


def charger_cache():
    if not CACHE_FILE.exists():
        return {"version": 1, "jours": {}, "signets": {}}
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # Cache corrompu : on le PRÉSERVE avant de repartir de zéro
        try:
            os.rename(CACHE_FILE, str(CACHE_FILE) + f".corrupt-{int(datetime.datetime.utcnow().timestamp())}")
            print("[WARN] Cache corrompu préservé en .corrupt", file=sys.stderr)
        except Exception:
            pass
        return {"version": 1, "jours": {}, "signets": {}}


def ecrire_cache_atomique(cache_data):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(CACHE_DIR), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, CACHE_FILE)
    except Exception as e:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
        print(f"[ERREUR] Écriture cache échouée : {e}", file=sys.stderr)


def date_aujourdhui():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def quota_restant(cache_data):
    aujourdhui = date_aujourdhui()
    utilises = cache_data.get("jours", {}).get(aujourdhui, 0)
    return max(0, MAX_PAR_JOUR - utilises)


def incrementer_quota(cache_data):
    aujourdhui = date_aujourdhui()
    if "jours" not in cache_data:
        cache_data["jours"] = {}
    cache_data["jours"][aujourdhui] = cache_data["jours"].get(aujourdhui, 0) + 1


# === Parsing des signets ===
def extraire_texte_tweet(contenu):
    lignes = contenu.splitlines()
    in_frontmatter = False
    texte_lignes = []
    for ligne in lignes:
        if ligne.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue
        if not in_frontmatter:
            texte_lignes.append(ligne)
    texte = "\n".join(texte_lignes).strip()
    texte = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", texte)
    texte = re.sub(r"<[^>]+>", "", texte)
    return texte.strip()


def parser_signet(chemin: Path):
    try:
        contenu = chemin.read_text(encoding="utf-8")
    except Exception:
        return None

    meta = {}
    if contenu.startswith("---"):
        try:
            fin_front = contenu.find("\n---", 3)
            if fin_front < 0:
                fin_front = contenu.find("---", 3)
            front = contenu[3:fin_front].strip()
            for ligne in front.splitlines():
                if ":" in ligne:
                    k, v = ligne.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
        except Exception:
            pass

    texte = extraire_texte_tweet(contenu)
    if len(texte) > 800:
        texte = texte[:800] + "..."

    return {
        "id": meta.get("id", ""),
        "author": meta.get("author", ""),
        "url": meta.get("url", ""),
        "date": meta.get("tweet_date", ""),
        "texte": texte,
        "chemin": str(chemin),
    }


# === Appel hub (task Gemini rapide, timeout=None — non bloquant) ===
def appeler_hub(prompt):
    payload = {
        "task": TASK_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 300,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        HUB_URL, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=None) as response:
            result = json.loads(response.read().decode("utf-8"))
        content = result["choices"][0]["message"]["content"]
        content = content.strip()
        if content.startswith("```"):
            content = content.split("\n", 1)[1]
        if content.endswith("```"):
            content = content.rsplit("\n", 1)[0]
        return content.strip()
    except Exception as e:
        print(f"[ERREUR HUB] {e}", file=sys.stderr)
        return None


# === Traitement principal ===
def traiter_signets():
    verifier_kill_switch()

    cache = charger_cache()
    restants = quota_restant(cache)
    if restants <= 0:
        print("[BILAN] Quota journalier atteint.")
        return

    # macOS TCC : le dossier Documents est protégé — sortie propre si interdit
    try:
        _premier = next(SIGNETS_DIR.iterdir(), None)
        if _premier is None:
            print(f"[INFO] Dossier signets vide : {SIGNETS_DIR}")
            return
    except PermissionError:
        print("[TCC] Accès au dossier Documents refusé par macOS (PermissionError).", file=sys.stderr)
        print("[TCC] Autorise l'accès complet au disque pour python3 : Réglages → Confidentialité → Accès complet au disque.", file=sys.stderr)
        return
    except FileNotFoundError:
        print(f"[ERREUR] Dossier signets introuvable : {SIGNETS_DIR}", file=sys.stderr)
        return
    except Exception as _e:
        print(f"[ERREUR] Dossier signets inaccessible : {_e}", file=sys.stderr)
        return

    tous_signets = []
    for md_file in SIGNETS_DIR.rglob("*.md"):
        data = parser_signet(md_file)
        if data and data["url"]:
            key = sha12(data["url"])
            if key not in cache.get("signets", {}):
                tous_signets.append((data, key))

    if not tous_signets:
        print("[OK] Aucun nouveau signet à traiter.")
        return

    tous_signets.sort(key=lambda x: (x[0]["date"], x[0]["chemin"]), reverse=True)
    a_traiter = tous_signets[:restants]

    print(f"[INFO] {len(a_traiter)} signets à traiter (quota restant: {restants})")

    resumes_generes = 0
    for data, key in a_traiter:
        verifier_kill_switch()

        prompt = f"""Tu résumes un bookmark X (tweet) pour Christophe, non-expert.
AUTEUR : {data['author']}
DATE : {data['date']}
TEXTE :
{data['texte']}

Réponds UNIQUEMENT avec un JSON valide : {{"resume": "..."}}
- resume : 2-3 lignes en français, concret. Ce que dit le post + en quoi c'est utile pour ACE777 (IA gratuite, agents, trading crypto, dev, veille…). Si c'est un post sans intérêt pour nous, dis-le honnêtement (« Sans intérêt direct pour ACE777 »)."""

        reponse = appeler_hub(prompt)
        if not reponse:
            print(f"[SKIP] Échec appel hub pour {data['author']}")
            continue

        try:
            resume_json = json.loads(reponse)
            resume = resume_json.get("resume", "Résumé non disponible")
        except Exception:
            resume = reponse[:200]

        if "signets" not in cache:
            cache["signets"] = {}
        cache["signets"][key] = {
            "id": data["id"],
            "author": data["author"],
            "url": data["url"],
            "date": data["date"],
            "resume": resume,
            "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }

        incrementer_quota(cache)
        ecrire_cache_atomique(cache)
        resumes_generes += 1

        texte_court = data["texte"][:60].replace("\n", " ")
        print(f"[OK] Résumé : {data['author']} — {texte_court}...")

    print(f"\n[BILAN] Signets lus: {len(a_traiter)} | Résumés générés: {resumes_generes} | Quota restant: {quota_restant(cache)}")


if __name__ == "__main__":
    if acquerir_verrou():
        try:
            traiter_signets()
        finally:
            liberer_verrou()
    else:
        print("[LOCK] Verrou non acquis — sortie")
