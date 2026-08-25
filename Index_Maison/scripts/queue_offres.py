#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""queue_offres.py v6 — file d'attente des offres IA gratuites (ACE777).

Assemblé par le superviseur : base = v4 du codeur (structure correcte) +
corrections P1-P5 de la spec v5 (code exact validé). Flux maison :
- mode_scan : pistes (signets GARDER) + offres (veille) → file
- run_pretest : test RÉEL d'accès (call_chat) sur les 'nouveau'
- evaluate_top_entries : top 6 teste_ok → A/B réel → VRAI juge (hub)
  → si MIEUX → intégration ACTIVE (providers.json, free:True, enabled:True)
DÉCISION CHRISTOPHE 14/08 : les offres IA (nouveaux providers gratuits) n'ont
PAS besoin de sa validation — le test réel + juge + routeur conservateur
(≥5 échantillons, +15 pts, rollback auto) sont les vrais garde-fous. La
validation humaine reste pour les offres qui impactent le SETUP (architecture,
scripts, config, stratégie) : famille → juge → Christophe → GO.
Non fatal · verrou PID · écriture atomique · quota 4/jour.
"""
import os
import sys
import json
import datetime
import shutil
import hashlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from collections import Counter

# === CHEMINS RÉELS (vérifiés superviseur) ===
BASE_DIR = Path("/Users/christophe/ace777-test-day1/Index_Maison")
SCRIPTS_DIR = BASE_DIR / "scripts"
SIGNETS_FILE = BASE_DIR / "strategie" / "SIGNETS_RESUMES.json"
QUEUE_FILE = BASE_DIR / "strategie" / "QUEUE_OFFRES.json"
PROVIDERS_FILE = Path.home() / "prise-ia" / "providers.json"
PID_FILE = SCRIPTS_DIR / "queue_offres.pid"

# === CONSTANTES ===
MAX_ESSAIS = 3
MAX_INTEGRATIONS_JOUR = 4
MAX_TESTS_PAR_PASSAGE = 6
MOTS_CLES_PISTE = [".free", "openrouter", "nvidia", "inferx", "puter",
                   "huggingface", "gratuit", "free"]

# === IMPORTS RÉELS (règle absolue : pas de réimplémentation) ===
try:
    from eval_offres import (call_chat, hub_juge, closest_reference,
                             active_providers, candidates_from_veille)
except ImportError as e:
    print(f"ERREUR: Impossible d'importer eval_offres.py : {e}", file=sys.stderr)
    sys.exit(1)


# === ENV (.env de prise-ia, comme eval_offres.env_key) ===

def charger_env() -> None:
    """Charge les clés depuis ~/prise-ia/.env dans os.environ (sans écraser)."""
    env_path = Path.home() / "prise-ia" / ".env"
    try:
        if not env_path.exists():
            return
        for ligne in env_path.read_text(encoding="utf-8").splitlines():
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or "=" not in ligne:
                continue
            k, v = ligne.split("=", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v
    except Exception:
        pass


# === UTILITAIRES ===

def maintenant_iso() -> str:
    return datetime.datetime.now().isoformat()


def sha12(chaine: str) -> str:
    return hashlib.sha256(chaine.encode("utf-8")).hexdigest()[:12]


def charger_json(chemin: Path, defaut: Any) -> Any:
    if not chemin.exists():
        return defaut
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defaut


def sauvegarder_atomique(chemin: Path, donnees: Any) -> bool:
    """Écriture atomique via tmp + replace. Retourne True si OK."""
    try:
        chemin.parent.mkdir(parents=True, exist_ok=True)
        tmp = chemin.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=2, ensure_ascii=False)
        tmp.replace(chemin)
        return True
    except Exception as e:
        print(f"[ERREUR] Écriture {chemin.name} : {e}")
        return False


# === VERROU ANTI-COURSE (PID mort détecté) ===

def verrou_pid() -> bool:
    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text().strip())
            os.kill(pid, 0)  # vivant ?
            print("[VERROU] Un autre queue_offres.py tourne. Sortie.")
            return False
        except (ProcessLookupError, ValueError, PermissionError):
            PID_FILE.unlink(missing_ok=True)
    try:
        PID_FILE.write_text(str(os.getpid()))
    except Exception:
        pass
    return True


def liberer_verrou() -> None:
    try:
        PID_FILE.unlink(missing_ok=True)
    except Exception:
        pass


# === P4 — FILE (quota journalier reset, file conservée) ===

def charger_queue() -> Dict[str, Any]:
    data = charger_json(QUEUE_FILE, {})
    if not isinstance(data, dict):
        data = {"entrees": data if isinstance(data, list) else []}
    if "entrees" not in data:
        data["entrees"] = []
    if "traites_jour" not in data:
        data["traites_jour"] = 0
    aujourdhui = datetime.date.today().isoformat()
    if data.get("date") != aujourdhui:
        data["date"] = aujourdhui
        data["traites_jour"] = 0     # quota quotidien remis à zéro, file conservée
    return data


def sauvegarder_queue(queue: Dict[str, Any]) -> None:
    sauvegarder_atomique(QUEUE_FILE, queue)


# === V1 — PISTES depuis les signets GARDER (mots-clés IA gratuite) ===

def load_signets_garder() -> List[Dict[str, Any]]:
    cache = charger_json(SIGNETS_FILE, {})
    pistes = []
    for cle, signet in cache.get("signets", {}).items():
        if signet.get("avis") != "garder":
            continue
        resume = (signet.get("resume") or "").lower()
        if not any(mot in resume for mot in MOTS_CLES_PISTE):
            continue
        pistes.append({
            "id": cle,
            "type": "piste",
            "source": "signets_garder",
            "source_detail": signet.get("url", ""),
            "resume": signet.get("resume", ""),
            "arrivee": signet.get("date", maintenant_iso()),
            "statut": "piste",
            "essais": 0,
        })
    return pistes


# === V2 — SCAN : pistes signets + offres veille ===

def mode_scan() -> None:
    queue = charger_queue()

    # Pistes signets GARDER
    pistes = load_signets_garder()
    for p in pistes:
        if not any(e.get("id") == p["id"] for e in queue["entrees"]):
            queue["entrees"].append(p)

    # Offres testables de la veille (import réel eval_offres)
    try:
        for v in candidates_from_veille():
            entree = {
                "id": sha12(v["model"] + v.get("base_url", "")),
                "type": "offre",
                "source": "veille_hub",
                "source_detail": v.get("model", ""),
                "model": v.get("model"),
                "base_url": v.get("base_url"),
                "api_key_env": v.get("api_key_env"),
                "role": "gros cerveau",
                "arrivee": maintenant_iso(),
                "statut": "nouveau",
                "essais": 0,
            }
            if not any(e.get("id") == entree["id"] for e in queue["entrees"]):
                queue["entrees"].append(entree)
    except Exception as e:
        print(f"[SCAN] veille indisponible : {e}")

    sauvegarder_queue(queue)
    print(f"[SCAN] {len(queue['entrees'])} entrées dans la file.")


# === P3 — CLÉ API (False si pas de clé → attente_cle) ===

def cle_api_disponible(entree: dict) -> bool:
    env_var = entree.get("api_key_env")
    if not env_var:
        return False          # pas de clé déclarée → attente_cle
    return bool(os.environ.get(env_var))


# === P1 — PRÉ-FILTRE : test RÉEL d'accès (pas le juge) ===

def run_pretest() -> None:
    queue = charger_queue()
    tests = 0
    for entree in queue["entrees"]:
        if tests >= MAX_TESTS_PAR_PASSAGE:
            break
        if entree.get("type") == "piste":
            # PISTE SIGNET (fix 23/08) : une piste est un lien X + résumé, PAS un
            # endpoint testable — elle ne peut pas passer le pre-test. Au lieu de
            # la sauter en silence (elle restait « piste » à jamais, jamais vue),
            # on la marque attente_cle avec une note lisible dans l'état :
            # nécessite une INSCRIPTION + clé API (action humaine) pour devenir
            # une offre testable.
            if entree.get("statut") == "piste":
                entree["statut"] = "attente_cle"
                entree["note"] = ("Piste signet : nécessite inscription + clé API "
                                  "(action humaine) pour devenir une offre testable.")
            continue
        # On retraite 'nouveau' ET 'attente_cle' (une clé peut devenir dispo)
        if entree.get("statut") not in ("nouveau", "attente_cle"):
            continue

        if not cle_api_disponible(entree):
            entree["statut"] = "attente_cle"
            continue

        try:
            ok, texte, erreur = call_chat(
                entree.get("base_url"),
                entree.get("model"),
                os.environ.get(entree.get("api_key_env", ""), ""),
                timeout=35,
            )
            entree["test_reel"] = {"ok": ok, "erreur": erreur}
            if ok:
                entree["statut"] = "teste_ok"
            else:
                entree["essais"] = entree.get("essais", 0) + 1
                if entree["essais"] >= MAX_ESSAIS:
                    entree["statut"] = "poubelle"
                else:
                    entree["statut"] = "nouveau"   # retenté au prochain passage
        except Exception as e:
            entree["essais"] = entree.get("essais", 0) + 1
            if entree["essais"] >= MAX_ESSAIS:
                entree["statut"] = "poubelle"
            else:
                entree["statut"] = "nouveau"
            entree["test_reel"] = {"ok": False, "erreur": str(e)}
        tests += 1

    sauvegarder_queue(queue)
    print("[PRETEST] terminé.")


# === V5/V6 — INTÉGRATION observation (backup COPIE, structure hub exacte) ===

def ajouter_provider_observation(entree: dict) -> bool:
    cfg = charger_json(PROVIDERS_FILE, {"providers": []})
    if "providers" not in cfg or not isinstance(cfg.get("providers"), list):
        cfg["providers"] = []
    providers_list = cfg["providers"]

    # Doublon ?
    for p in providers_list:
        if p.get("base_url") == entree.get("base_url") and p.get("model") == entree.get("model"):
            return False

    nouveau_provider = {
        "id": f"obs-{int(__import__('time').time())}",
        "name": entree.get("model", "observation"),
        "kind": "llm",
        "base_url": entree.get("base_url"),
        "model": entree.get("model"),
        "api_key_env": entree.get("api_key_env"),
        "order": len(providers_list),
        "timeout": 30,
        "free": True,
        # VERDICT FAMILLE 18/08 (unanime 3/3) : toute intégration passe par le sas
        # d'observation 48h (enabled:false) avant activation — même les obs-*.
        # L'observatoire (étendu) les sonde 48h puis les active (rollback = désactivation).
        "enabled": False,
        "status": "observation",
        "note": "auto queue_offres | VERDICT FAMILLE 18/08 : observation 48h avant activation",
    }
    providers_list.append(nouveau_provider)
    cfg["providers"] = providers_list

    # Backup par COPIE (jamais rename — on ne risque pas de perdre providers.json)
    try:
        backup = PROVIDERS_FILE.with_name(
            f"providers.json.bak-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        )
        shutil.copy2(PROVIDERS_FILE, backup)
    except Exception:
        pass
    return sauvegarder_atomique(PROVIDERS_FILE, cfg)


# === P2 — ÉVALUATION : top 6 teste_ok → A/B réel → VRAI juge → intégration ===

def evaluate_top_entries() -> None:
    queue = charger_queue()
    entrees = [e for e in queue.get("entrees", []) if e.get("statut") == "teste_ok"]
    entrees = sorted(entrees, key=lambda x: x.get("arrivee", ""), reverse=True)[:6]

    cfg = charger_json(PROVIDERS_FILE, {"providers": []})
    providers = active_providers(cfg)

    for entree in entrees:
        if queue.get("traites_jour", 0) >= MAX_INTEGRATIONS_JOUR:
            print("[QUOTA] 4 intégrations/jour atteint.")
            break
        try:
            # 1) Candidat
            ok_c, texte_c, _ = call_chat(
                entree.get("base_url"),
                entree.get("model"),
                os.environ.get(entree.get("api_key_env", ""), ""),
                timeout=35,
            )
            if not ok_c:
                continue
            # 2) Actuel de référence
            ref = closest_reference(providers, entree.get("role", "gros cerveau"))
            if not ref:
                continue
            ok_r, texte_r, _ = call_chat(
                ref.get("base_url"), ref.get("model"),
                os.environ.get(ref.get("api_key_env", ""), ""),
                timeout=35,
            )
            if not ok_r:
                continue
            # 3) VRAI juge — 4 arguments : textes puis noms de modèles
            verdict, preuve = hub_juge(texte_c, texte_r,
                                       entree.get("model"), ref.get("model"))
            entree["evaluation"] = verdict
            entree["preuve_eval"] = preuve
            # 4) Intégration observation
            if verdict == "MIEUX":
                if ajouter_provider_observation(entree):
                    entree["statut"] = "integre"
                    queue["traites_jour"] = queue.get("traites_jour", 0) + 1
                    print(f"[INTÉGRÉ] {entree.get('model')} → observation")
        except Exception as e:
            entree["evaluation"] = "erreur"
            entree["erreur_eval"] = str(e)

    sauvegarder_queue(queue)
    print("[EVAL] Top 6 évalués.")


# === P5 — ÉTAT (compteurs + pistes récentes) ===

def mode_etat() -> None:
    queue = charger_queue()
    entrees = queue.get("entrees", [])
    stats = Counter(e.get("statut", "?") for e in entrees)
    print(f"=== ÉTAT QUEUE ({len(entrees)} entrées) ===")
    print(f"Statuts : {dict(stats)}")
    print(f"Intégrées aujourd'hui : {queue.get('traites_jour', 0)}/{MAX_INTEGRATIONS_JOUR}")
    print("Pistes récentes (5) :")
    for p in [e for e in entrees if e.get("type") == "piste"][:5]:
        print(f"  - {p.get('source_detail', '')[:60]} | {p.get('resume', '')[:50]}")


# === CLI ===

def main() -> None:
    if not verrou_pid():
        return
    try:
        args = [a for a in sys.argv[1:] if a.startswith("--")]
        mode = args[0][2:] if args else "full"
        if mode == "scan":
            mode_scan()
        elif mode == "pretest":
            run_pretest()
        elif mode == "eval":
            evaluate_top_entries()
        elif mode == "etat":
            mode_etat()
        else:
            # Mode full : scan → pretest → eval → etat
            mode_scan()
            run_pretest()
            evaluate_top_entries()
            mode_etat()
    finally:
        liberer_verrou()


if __name__ == "__main__":
    charger_env()   # clés du hub dispo même hors terminal (launchd)
    try:
        main()
    except Exception as e:
        print(f"[FATAL] Exception non interceptée (non bloquante) : {e}")
