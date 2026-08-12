#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fiches_offres.py — Générateur de fiches IA pour les offres (ACE777)
Rôle : analyse une seule fois chaque offre via le hub, cache atomique, quota 8/jour.
"""

import os
import sys
import json
import hashlib
import datetime
import urllib.request
import tempfile
from pathlib import Path

# === Chemins (convention ACE777) ===
BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
VEILLE_DIR = BASE
CACHE_DIR = BASE / "strategie"
CACHE_FILE = CACHE_DIR / "FICHES_OFFRES.json"
LOCK_FILE = CACHE_DIR / ".FICHES_OFFRES.lock"
STOP_FILE = CACHE_DIR / "STOP"
STOP_ALL = BASE / "STOP_ALL"

# === Constantes ===
MAX_PAR_JOUR = 8
TESTABLE_KEYWORDS = ["openrouter", "nvidia", "inferx", "puter"]
HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"


def maintenant_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha12(section: str, item: str) -> str:
    h = hashlib.sha1(f"{section}|{item}".encode("utf-8")).hexdigest()
    return h[:12]


def charger_cache():
    if not CACHE_FILE.exists():
        return {"version": 2, "jours": {}, "fiches": {}}
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # Cache corrompu : on le PRÉSERVE (rename) avant de repartir de zéro
        try:
            import time as _t
            os.rename(CACHE_FILE, str(CACHE_FILE) + f".corrupt-{int(_t.time())}")
            print(f"[WARN] Cache corrompu préservé en .corrupt", file=sys.stderr)
        except Exception:
            pass
        return {"version": 2, "jours": {}, "fiches": {}}


def prendre_verrou():
    """Verrou atomique O_EXCL : empêche 2 générateurs de tourner en même
    temps (course au quota — max 8 fiches/jour). Retourne True si pris."""
    try:
        fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return True
    except FileExistsError:
        # Verrou existant : mort si le PID n'existe plus (auto-réparation)
        try:
            pid = int(open(LOCK_FILE).read().strip() or "0")
        except Exception:
            pid = 0
        if pid and not os.path.exists(f"/proc/{pid}") and not _pid_vivant(pid):
            try:
                os.unlink(LOCK_FILE)
                return prendre_verrou()
            except Exception:
                return False
        return False
    except Exception:
        return False


def _pid_vivant(pid: int) -> bool:
    """macOS : kill 0 pour tester la présence d'un PID (pas de /proc)."""
    try:
        os.kill(pid, 0)
        return True
    except Exception:
        return False


def liberer_verrou():
    try:
        os.unlink(LOCK_FILE)
    except Exception:
        pass


def save_atomic(data: dict):
    """Écriture atomique (tmp + rename) comme eval_offres.py"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=CACHE_DIR, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, CACHE_FILE)
    except Exception as e:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
        print(f"[ERREUR] Écriture cache échouée : {e}", file=sys.stderr)


def kill_switch_actif() -> bool:
    return STOP_FILE.exists() or STOP_ALL.exists()


def trouver_rapport_veille():
    """Retourne le chemin du rapport du jour ou du dernier disponible"""
    aujourdhui = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    rapport_jour = VEILLE_DIR / f"VEILLE_HUB_{aujourdhui}.md"
    if rapport_jour.exists():
        return rapport_jour, aujourdhui

    # Sinon dernier rapport disponible
    rapports = sorted(VEILLE_DIR.glob("VEILLE_HUB_*.md"), reverse=True)
    if rapports:
        date = rapports[0].stem.replace("VEILLE_HUB_", "")
        return rapports[0], date
    return None, None


def parser_offres(chemin_md: Path):
    """Parse les sections ### et les items commençant par - """
    offres = []
    section_courante = None
    try:
        with open(chemin_md, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne.startswith("### "):
                    section_courante = ligne[4:].strip()
                elif ligne.startswith("- ") and section_courante:
                    item = ligne[2:].strip()
                    if item:
                        offres.append((section_courante, item))
    except Exception as e:
        print(f"[ERREUR] Lecture veille : {e}", file=sys.stderr)
    return offres


def est_testable(section: str, item: str) -> bool:
    txt = (section + " " + item).lower()
    return any(kw in txt for kw in TESTABLE_KEYWORDS)


def appeler_hub(prompt: str):
    """Appel non bloquant vers le hub local (timeout=None)"""
    payload = {
        "task": "analyste.strategie",  # gemini rapide (analyse.profonde -> nvidia bloque)
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 350,
        "temperature": 0.3
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(HUB_URL, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            reponse = resp.read().decode("utf-8")
        # La réponse du hub est l'enveloppe OpenAI complète : extraire le contenu
        env = json.loads(reponse)
        contenu = env["choices"][0]["message"]["content"] or ""
        # Nettoyage fences éventuels
        if "```json" in contenu:
            contenu = contenu.split("```json")[1].split("```")[0].strip()
        elif "```" in contenu:
            contenu = contenu.split("```")[1].split("```")[0].strip()
        return json.loads(contenu)
    except Exception as e:
        print(f"[ERREUR] Appel hub : {e}", file=sys.stderr)
        return None


def generer_fiche(section: str, item: str):
    prompt = f"""Tu rédiges la fiche de présentation d'une offre IA gratuite pour un débutant.
OFFRE : {section} — {item}
Réponds UNIQUEMENT avec un JSON valide, sans commentaire, de la forme :
{{"type": "...", "forts": ["..."], "faibles": ["..."], "usage": "...",
 "avis_pour": "...", "avis_attention": "..."}}
- type : 1 phrase claire (ex. « Modèle de codage gratuit », « Fournisseur de modèles d'entreprise »)
- forts/faibles : puces courtes, concrètes, pour nos besoins (scripts Python, analyse, jugement)
- usage : où l'utiliser chez ACE777 (codeur, analyste, juge, chat…)
- avis_pour : pourquoi l'essayer, en 1 phrase motivée
- avis_attention : le piège/limite à connaître, en 1 phrase
Si tu ne sais pas ce qu'est l'offre, reste honnête et prudent dans les avis."""

    for tentative in range(2):
        resultat = appeler_hub(prompt)
        if resultat and all(k in resultat for k in ["type", "forts", "faibles", "usage", "avis_pour", "avis_attention"]):
            return resultat
        print(f"[INFO] Réponse invalide, tentative {tentative+1}/2", file=sys.stderr)
    return None


def main():
    if kill_switch_actif():
        print("[INFO] Kill switch actif — sortie immédiate")
        return

    # Verrou anti-course : un seul générateur à la fois (sinon quota dépassé)
    if not prendre_verrou():
        print("[INFO] Un autre générateur tourne déjà — sortie")
        return
    try:
        _main_interne()
    finally:
        liberer_verrou()


def _main_interne():
    cache = charger_cache()
    aujourdhui = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    jours = cache.setdefault("jours", {})
    deja_genere = jours.get(aujourdhui, 0)
    quota_restant = MAX_PAR_JOUR - deja_genere

    if quota_restant <= 0:
        print(f"[INFO] Quota journalier atteint ({MAX_PAR_JOUR}/jour)")
        return

    rapport, date_utilisee = trouver_rapport_veille()
    if not rapport:
        print("[ERREUR] Aucun rapport VEILLE_HUB trouvé")
        return

    offres = parser_offres(rapport)
    print(f"[INFO] Rapport utilisé : {rapport.name} ({len(offres)} offres)")

    # Sélection des offres à analyser (priorité testable)
    a_analyser = []
    for section, item in offres:
        cle = sha12(section, item)
        if cle not in cache["fiches"]:
            a_analyser.append((section, item, cle))

    # Tri : testable d'abord, puis ordre du rapport
    index_offres = {o: i for i, o in enumerate(offres)}
    a_analyser.sort(key=lambda x: (0 if est_testable(x[0], x[1]) else 1,
                                   index_offres.get((x[0], x[1]), 999)))

    a_analyser = a_analyser[:quota_restant]

    generees = 0
    for section, item, cle in a_analyser:
        fiche = generer_fiche(section, item)
        if fiche:
            cache["fiches"][cle] = {
                "section": section,
                "item": item,
                "generated": maintenant_iso(),
                **fiche
            }
            jours[aujourdhui] = jours.get(aujourdhui, 0) + 1
            generees += 1
            save_atomic(cache)  # écriture après chaque fiche
            print(f"[OK] Fiche générée : {section} — {item[:40]}...")
        else:
            print(f"[SKIP] Échec analyse : {section} — {item[:40]}...")

    save_atomic(cache)
    print(f"[BILAN] Offres lues: {len(offres)} | Fiches générées: {generees} | Quota restant: {MAX_PAR_JOUR - jours.get(aujourdhui, 0)}")


if __name__ == "__main__":
    main()
