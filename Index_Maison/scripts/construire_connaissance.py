#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Collecteur de la base de connaissance ACE777.
- Ingère les verdicts famille (dossiers CONSULTATION_FAMILLE_*/VERDICT_FAMILLE.md)
  → met à jour statut_verification + ajoute le fait d'audit (idempotent).
- Consolide les signets X « garder » (SIGNETS_RESUMES.json) → signets_cles par projet
  (matching par alias de projet dans le résumé/url).
- Applique les règles anti-engraissement (péremption, quota, scoring, archive).
- Génère le dashboard de santé (thermo/SANTE_CONNAISSANCE.md).
Chantier connaissance : ZÉRO touche au moteur Hulk.
"""

import os
import sys
import re
import json
import glob
import hashlib
import tempfile
from datetime import datetime, timezone, timedelta

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INDEX_MAISON = os.path.join(BASE_DIR, "Index_Maison")
STRATEGIE_DIR = os.path.join(INDEX_MAISON, "strategie")
SCRIPTS_DIR = os.path.join(INDEX_MAISON, "scripts")
THERMO_DIR = os.path.join(INDEX_MAISON, "thermo")

CONNAISSANCE_PATH = os.path.join(STRATEGIE_DIR, "CONNAISSANCE_PROJETS.json")
SIGNETS_PATH = os.path.join(STRATEGIE_DIR, "SIGNETS_RESUMES.json")
SANTE_PATH = os.path.join(THERMO_DIR, "SANTE_CONNAISSANCE.md")

STOP_FILE = os.path.join(STRATEGIE_DIR, "STOP")
STOP_ALL_FILE = os.path.expanduser("~/ace777-test-day1/Index_Maison/STOP_ALL")

# Fiabilité par source (verdict famille)
FIABILITE_AUDIT = 0.7
PEREMPTION_FONDAMENTAUX_J = 90
PEREMPTION_MARCHE_J = 30
QUOTA_MAX_FAITS = 50
QUOTA_MAX_LECONS = 50
SEUIL_INJECTION = 0.6
ARCHIVE_FROIDE_J = 180

# Alias projet → symbole clé (le matching signets s'appuie dessus)
PROJET_ALIASES = {
    "CCUSDT": ["ccusdt", "canton", "canton network", "canton coin"],
    "XRPUSDT": ["xrp"],
    "HBARUSDT": ["hbar", "hedera"],
}


def check_kill_switch():
    if os.path.exists(STOP_FILE) or os.path.exists(STOP_ALL_FILE):
        print("[KILL] Kill switch activé. Arrêt propre.", file=sys.stderr)
        sys.exit(0)


def atomic_write_json(filepath, data):
    check_kill_switch()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(filepath), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, filepath)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
        raise


def load_connaissance():
    if not os.path.exists(CONNAISSANCE_PATH):
        return {"version": "1.0", "updated": datetime.now(timezone.utc).isoformat(),
                "projets": {}, "archives": []}
    try:
        with open(CONNAISSANCE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("[AVERTISSEMENT] CONNAISSANCE_PROJETS.json illisible — base vide.", file=sys.stderr)
        return {"version": "1.0", "updated": datetime.now(timezone.utc).isoformat(),
                "projets": {}, "archives": []}


def normaliser_projet(nom_dossier):
    """Du nom de dossier CONSULTATION_FAMILLE_SMALLCAPS_CANTON_20260815 → symbole clé."""
    partie = re.sub(r"^CONSULTATION_FAMILLE_", "", nom_dossier)
    partie = re.sub(r"_\d{8}$", "", partie)
    partie = re.sub(r"^(SMALLCAPS|CONTRAT|SPEC|SIGNETS|DERIVE|KELLY|QUANT|DISCIPLINE)_", "", partie)
    partie = partie.upper().replace("_", "")
    for sym in PROJET_ALIASES:
        aliases = [a.replace(" ", "").upper() for a in PROJET_ALIASES[sym]]
        if partie in aliases or any(a in partie for a in aliases if len(a) >= 4):
            return sym
    return None


def extraire_score_verdict(content):
    """Extrait le score de confiance du verdict (ex. 'gemini (70%), nvidia (72%)').
    Ciblé pour éviter de capter les % du contenu (spreads, tailles...)."""
    scores = []
    # Ligne « Avis reçus » : gemini (70%), nvidia (72%) — les % DE CETTE LIGNE
    for ligne in content.split("\n"):
        if re.search(r"[Aa]vis reçus?", ligne):
            scores += [int(s) for s in re.findall(r"(\d{1,3})\s*%", ligne) if 0 <= int(s) <= 100]
            break
    # Lignes « CONFIANCE : N % » (par modèle ou globale)
    for ligne in content.split("\n"):
        m = re.search(r"CONFIANCE[^\n]*?[：:]\s*(\d{1,3})\s*%", ligne, re.IGNORECASE)
        if m:
            v = int(m.group(1))
            if 0 <= v <= 100:
                scores.append(v)
    # Repli : « (70%), (72%) » proches (verdict consolidé)
    if not scores:
        m2 = re.search(r"\(?(\d{1,3})\s*%\)?[^\n]{0,40}(\d{1,3})\s*%", content)
        if m2:
            scores += [int(s) for s in m2.groups() if 0 <= int(s) <= 100]
    if not scores:
        return None
    return round(sum(scores) / len(scores))


def extraire_verdict(content):
    """Extrait GO/NO-GO/GO-AVEC-RÉSERVE (insensible à la casse, tolère accents majuscules)."""
    m = re.search(r"(GO-AVEC-RÉSERVE|GO-AVEC-RESERVE|NO-GO|GO)\b", content, re.IGNORECASE)
    if not m:
        return None
    v = m.group(1).upper().replace("RESERVE", "RÉSERVE")
    return v


def parse_verdicts_famille(data):
    now_iso = datetime.now(timezone.utc).isoformat()
    dossiers = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "CONSULTATION_FAMILLE_*")))
    for cdir in dossiers:
        verdict_path = os.path.join(cdir, "VERDICT_FAMILLE.md")
        if not os.path.exists(verdict_path):
            continue
        try:
            with open(verdict_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"[AVERTISSEMENT] Lecture impossible {verdict_path}: {e}", file=sys.stderr)
            continue

        sym = normaliser_projet(os.path.basename(cdir))
        if not sym:
            print(f"[INFO] Dossier {os.path.basename(cdir)} : projet non mappé, ignoré.")
            continue

        verdict = extraire_verdict(content)
        score = extraire_score_verdict(content)
        if not verdict:
            print(f"[INFO] {os.path.basename(cdir)} : verdict non trouvé, ignoré.")
            continue

        projet = data["projets"].setdefault(sym, {
            "nom": sym, "these": "", "classe_hulk": "A_core", "horizon_bag": "moyen",
            "capital_alloue_max": "", "statut_verification": {}, "faits": [],
            "lecons": [], "signets_cles": [], "updated": now_iso,
        })

        ancien_statut = projet.get("statut_verification") or {}
        projet["statut_verification"] = {
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "verdict": verdict,
            "score": score if score is not None else 0,
            "reserve": ancien_statut.get("reserve", ""),
        }
        projet["updated"] = now_iso

        # Fait d'audit idempotent (clé = hash texte + source)
        texte_audit = f"Audit famille {projet['statut_verification']['date']} : {verdict}"
        h = hashlib.md5((texte_audit + "|audit_famille").encode()).hexdigest()[:12]
        fait_id = f"fait_{sym.lower()}_audit_{h}"
        existants = {f.get("id") for f in projet.get("faits", [])}
        if fait_id not in existants:
            projet.setdefault("faits", []).append({
                "id": fait_id,
                "texte": texte_audit,
                "source": "audit_famille",
                "fiabilite": FIABILITE_AUDIT,
                "score": FIABILITE_AUDIT,
                "etat": "verifie",
                "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "expires_at": (datetime.now(timezone.utc) + timedelta(days=PEREMPTION_FONDAMENTAUX_J)).strftime("%Y-%m-%d"),
            })
        print(f"[OK] Verdict famille → {sym} ({verdict}, {score}%)")


def consolider_signets(data):
    if not os.path.exists(SIGNETS_PATH):
        print("[INFO] SIGNETS_RESUMES.json absent — consolidation signets ignorée.")
        return
    try:
        with open(SIGNETS_PATH, "r", encoding="utf-8") as f:
            cache = json.load(f)
    except Exception as e:
        print(f"[AVERTISSEMENT] SIGNETS_RESUMES.json illisible : {e}", file=sys.stderr)
        return

    signets = cache.get("signets", {})
    if not isinstance(signets, dict):
        return

    for cle, s in signets.items():
        if not isinstance(s, dict):
            continue
        if s.get("avis") != "garder":
            continue
        texte = " ".join([
            str(s.get("author", "")), str(s.get("resume", "")),
            str(s.get("url", "")), str(s.get("id", "")),
        ]).lower()
        for sym, aliases in PROJET_ALIASES.items():
            if sym not in data["projets"]:
                continue
            if any(a in texte for a in aliases):
                projet = data["projets"][sym]
                signets_cles = projet.setdefault("signets_cles", [])
                if cle not in [sc.get("id") for sc in signets_cles]:
                    signets_cles.append({
                        "id": cle,
                        "author": s.get("author", ""),
                        "url": s.get("url", ""),
                        "date": s.get("date", ""),
                        "resume": (s.get("resume", "") or "")[:200],
                    })
                break


def appliquer_regles_anti_engraissement(data):
    now = datetime.now(timezone.utc)
    aujourd_hui = now.strftime("%Y-%m-%d")

    for p_nom, p_data in list(data.get("projets", {}).items()):
        # 1. Péremption par expires_at (ou date d'entrée à défaut)
        for liste, type_el in [("faits", "fait"), ("lecons", "lecon")]:
            valides = []
            for el in p_data.get(liste, []):
                if type_el == "lecon":
                    el["etat"] = "verifie"  # une leçon reste valide tant qu'elle est dans la base
                else:
                    ref = el.get("expires_at") or el.get("date", aujourd_hui)
                    try:
                        ref_date = datetime.strptime(str(ref)[:10], "%Y-%m-%d").date()
                    except Exception:
                        ref_date = now.date()
                    if ref_date < now.date() and el.get("etat") == "verifie":
                        el["etat"] = "obsolete"
                        data.setdefault("archives", []).append({**el, "type": type_el, "projet": p_nom})
                        continue
                    # non vérifié 7 jours après entrée → en_attente (hors injection)
                    if type_el == "fait" and el.get("etat") == "verifie":
                        try:
                            entree = datetime.strptime(str(el.get("date", aujourd_hui))[:10], "%Y-%m-%d").date()
                        except Exception:
                            entree = now.date()
                        if (now.date() - entree) > timedelta(days=7) and el.get("source") == "signet_x":
                            el["etat"] = "en_attente"
                valides.append(el)
            p_data[liste] = valides

            # 2. Quota max
            if len(valides) > QUOTA_MAX_FAITS and type_el == "fait":
                p_data[liste] = sorted(valides, key=lambda x: (x.get("score", 0), x.get("date", "")), reverse=True)[:QUOTA_MAX_FAITS]
            if len(valides) > QUOTA_MAX_LECONS and type_el == "lecon":
                p_data[liste] = valides[-QUOTA_MAX_LECONS:]

    # 3. Archive froide : purge au-delà de 180 j
    archives = []
    for arc in data.get("archives", []):
        try:
            a_dt = datetime.strptime(str(arc.get("date", aujourd_hui))[:10], "%Y-%m-%d")
        except Exception:
            a_dt = now
        if (now - a_dt) <= timedelta(days=ARCHIVE_FROIDE_J):
            archives.append(arc)
    data["archives"] = archives


def generer_sante(data):
    check_kill_switch()
    compteur = {"verifie": 0, "obsolete": 0, "en_attente": 0, "a_confirmer": 0}
    for p in data.get("projets", {}).values():
        for f in p.get("faits", []):
            compteur[f.get("etat", "verifie")] = compteur.get(f.get("etat", "verifie"), 0) + 1

    md = f"""# Dashboard Santé — Connaissance ACE777

- **Dernière mise à jour** : {datetime.now(timezone.utc).isoformat()}
- **Projets suivis** : {len(data.get("projets", {}))}
- **Faits vérifiés** : {compteur["verifie"]}
- **Faits en attente** : {compteur["en_attente"]}
- **Faits à confirmer** : {compteur["a_confirmer"]}
- **Faits obsolètes (archivés)** : {compteur["obsolete"]} · archive froide : {len(data.get("archives", []))} éléments
- **Seuil d'injection** : score ≥ {SEUIL_INJECTION} · états autorisés : verifie
"""
    os.makedirs(os.path.dirname(SANTE_PATH), exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(SANTE_PATH), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(md)
        os.replace(tmp_path, SANTE_PATH)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
        raise


def main():
    check_kill_switch()
    data = load_connaissance()
    parse_verdicts_famille(data)
    consolider_signets(data)
    appliquer_regles_anti_engraissement(data)
    data["updated"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(CONNAISSANCE_PATH, data)
    generer_sante(data)
    print("[SUCCÈS] Base de connaissance construite et consolidée.")


if __name__ == "__main__":
    main()
