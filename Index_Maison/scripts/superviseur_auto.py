#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
superviseur_auto.py — Superviseur autonome ACE777 (C1+C2, 08/08/2026).
Spec : Evaluations/SPEC_SUPERVISEUR_2026-08-08.md
Production : hub (base Qwen, intégrée + complétée par Ada : chemins réels,
AGIR/JOURNALISER/POUSSER/main). Stdlib uniquement, zéro dépendance.

Cycle de 6 étapes : LIRE → ÉTAT → DÉCISION (hub) → AGIR → JOURNALISER → POUSSER.
Règles absolues : ne touche JAMAIS au moteur de trading, jamais d'écriture dans
~/Documents (TCC) — tout passe par l'OUTBOX, non fatal, timeouts, écritures atomiques,
anti-boucle (max 1 relance/passage, max 3/jour/job).

Usage :
    python3 superviseur_auto.py            # cycle complet
    python3 superviseur_auto.py --dry-run  # lit l'état, propose, N'ÉCRIT RIEN
"""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request

# ============================================================================
# CHEMINS RÉELS (vérifiés le 08/08 — ne pas deviner, c'est la leçon du jour)
# ============================================================================
HOME = Path.home()
SYSTEME = HOME / "ace777-test-day1"
OUTBOX = SYSTEME / "Index_Maison" / "OUTBOX_OBSIDIAN"
VAULT = HOME / "Documents" / "Obsidian_ACE777"
SCRIPTS = SYSTEME / "Index_Maison" / "scripts"

ATTENTION_DIR = OUTBOX / "A_Mon_Attention"
ATTENTION_VOCALE_PATH = ATTENTION_DIR / "ATTENTION_VOCALE.md"
LOG_PATH = OUTBOX / "SUPERVISEUR_LOG.md"
STATE_CACHE_PATH = OUTBOX / ".superviseur_state.json"

GIT_PUSH_SCRIPT = SCRIPTS / "git_push_auto.sh"
SYNC_NOW_SCRIPT = OUTBOX / "_sync_now.sh"
SESSION_DEBUT_SCRIPT = SCRIPTS / "session_debut.sh"

# Rappel de lecture complète (règle 1septies, 08/08) : la preuve de lecture du
# coffre (entrée MEMOIRE_COLLAB « lecture complète » / « LECTURE MECANIQUE »)
# doit avoir moins de 24 h. Sinon le superviseur (Qwen local) écrit un rappel.
RAPPEL_LECTURE_PATH = ATTENTION_DIR / "RAPPEL_LECTURE_COMPLETE.md"
MAX_AGE_PREUVE_H = 24

HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"
HUB_HEALTH_URL = "http://127.0.0.1:11435/health"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"

# Les 10 jobs launchd attendus (labels complets, vérifiés 10/08)
# MAJ fusion : qwen-btc/qwen-elabore (pause Qwen) + pulse/vigie (absorbés par
# superviseur-core) retirés ; superviseur-core ajouté (absorbe heartbeat,
# pulse, vigie, quotas, rotation).
JOBS_ATTENDUS = [
    "com.ace777.cockpit-http", "com.ace777.cortana.horaire",
    "com.ace777.prise-ia", "com.ace777.analyste-cadence",
    "com.ace777.cockpit-pont", "com.ace777.journal-soir", "com.ace777.gitpush",
    "com.ace777.cortana.urgent", "com.ace777.brief-matin",
    "com.ace777.superviseur-core",
]

TIMEOUT_RESEAU = 5
TIMEOUT_HUB = 600
MAX_LOG_LINES = 200
MAX_RELANCES_JOUR_PAR_JOB = 3

# ============================================================================
# UTILITAIRES
# ============================================================================


def log_message(msg: str):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")


def ecriture_atomique(chemin: Path, contenu: str):
    """Écrit de manière atomique (.tmp + os.replace) — piège n°1 de la veille."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = chemin.with_suffix(chemin.suffix + ".tmp")
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(tmp_path, chemin)
    except Exception as e:
        log_message(f"ERREUR écriture atomique {chemin}: {e}")
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except Exception:
                pass


def append_log_borne(ligne: str, dry_run: bool = False):
    """Append au log + tronque à MAX_LOG_LINES dernières lignes."""
    if dry_run:
        log_message(f"[DRY-RUN LOG] {ligne}")
        return
    OUTBOX.mkdir(parents=True, exist_ok=True)
    lignes = []
    if LOG_PATH.exists():
        try:
            with open(LOG_PATH, "r", encoding="utf-8") as f:
                lignes = f.read().splitlines()
        except Exception:
            pass
    lignes.append(ligne)
    if len(lignes) > MAX_LOG_LINES:
        lignes = lignes[-MAX_LOG_LINES:]
    ecriture_atomique(LOG_PATH, "\n".join(lignes) + "\n")


def charger_tracker() -> dict:
    """Anti-boucle : compteur de relances par job, réinitialisé chaque jour."""
    if STATE_CACHE_PATH.exists():
        try:
            data = json.loads(STATE_CACHE_PATH.read_text(encoding="utf-8"))
            if data.get("date") == datetime.now().strftime("%Y-%m-%d"):
                return data
        except Exception:
            pass
    return {"date": datetime.now().strftime("%Y-%m-%d"), "relances": {}}


def sauvegarder_tracker(tracker: dict, dry_run: bool = False):
    if dry_run:
        return
    ecriture_atomique(STATE_CACHE_PATH, json.dumps(tracker, indent=2))


def lire_fichier(chemin: Path, max_chars: int) -> str:
    """Lit un fichier, tolérant (retourne "" si absent/illisible)."""
    try:
        return chemin.read_text(encoding="utf-8")[:max_chars]
    except Exception:
        return ""


def _dernier_ts_preuve(mem: str):
    """Extrait le timestamp le plus récent d'une preuve de lecture dans un texte.

    Tag machine exigé par l'audit juge : [LECTURE_COMPLETE_OK]. Repli
    rétrocompatible : « lecture complète » / « LECTURE MECANIQUE »."""
    from datetime import datetime, timezone
    import re as _re
    if not mem:
        return None
    TAG = "[LECTURE_COMPLETE_OK]"
    dernier_ts = None
    for ligne in mem.splitlines():
        valide = TAG in ligne or "lecture complète" in ligne.lower() \
            or "lecture complete" in ligne.lower() or "LECTURE MECANIQUE" in ligne
        if not valide:
            continue
        m = _re.search(r'\| (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z) \|', ligne)
        if not m:
            continue
        try:
            ts = datetime.strptime(m.group(1), "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc)
            if dernier_ts is None or ts > dernier_ts:
                dernier_ts = ts
        except ValueError:
            continue
    return dernier_ts


def age_preuve_lecture():  # -> float ou None (Python 3.9 : pas de | dans les annotations)
    """Retourne l'âge (heures) de la dernière entrée « lecture complète » dans
    MEMOIRE_COLLAB. None = aucune preuve.

    Règle 1septies (08/08) : la preuve de lecture du coffre doit être < 24 h.
    Format des entrées : | 2026-08-08T18:04Z | ... (append-only, récent EN BAS).

    CORRECTION 08/08 19:05Z (constat : « Obsidian ne bouge pas ») : l'ancienne
    logique choisissait UNE seule source par mtime — le miroir OUTBOX (12 Ko,
    07/08) était souvent plus récent en mtime que le vault (67 Ko) et écrasait la
    preuve → rappel fantôme écrit à tort. Désormais on lit LES DEUX sources et on
    prend la preuve la PLUS RÉCENTE trouvée dans l'une ou l'autre."""
    from datetime import datetime, timezone
    ts_vault = _dernier_ts_preuve(lire_fichier(VAULT / "MEMOIRE_COLLAB.md", 2_000_000))
    ts_outbox = _dernier_ts_preuve(lire_fichier(OUTBOX / "MEMOIRE_COLLAB.md", 2_000_000))
    if ts_vault is None and ts_outbox is None:
        return None
    dernier_ts = ts_outbox if (ts_outbox is not None and (ts_vault is None or ts_outbox > ts_vault)) else ts_vault
    age_h = (datetime.now(timezone.utc) - dernier_ts).total_seconds() / 3600.0
    return age_h


# ============================================================================
# ÉTAPE 1 : LIRE
# ============================================================================


def etape_lire() -> dict:
    """1/6 LIRE — TOP_DEMAIN, REVEIL_BUFFY, MEMOIRE depuis OUTBOX (repli vault)."""
    log_message("Étape 1/6 : LIRE les contextes...")
    outbox_top = OUTBOX / "TOP_DEMAIN.md"
    outbox_reveil = OUTBOX / "REVEIL_BUFFY.md"
    outbox_mem = OUTBOX / "MEMOIRE_COLLAB.md"
    # ADDITIF (A2b, 09/08) : ETAT_CONSOLIDE = memoire compacte du jour (archive = MEMOIRE_COLLAB)
    etat_file = SYSTEME / "Index_Maison" / "ETAT_CONSOLIDE.md"
    contexte = {
        "etat_consolide": lire_fichier(etat_file, 1500),
        "top_demain": lire_fichier(outbox_top if outbox_top.exists() else VAULT / "AUTO_EVOL" / "TOP_DEMAIN.md", 1500),
        "reveil_buffy": lire_fichier(outbox_reveil if outbox_reveil.exists() else VAULT / "REVEIL_BUFFY.md", 800),
        "memoire_collab": lire_fichier(outbox_mem if outbox_mem.exists() else VAULT / "MEMOIRE_COLLAB.md", 800),
    }
    return contexte


# ============================================================================
# ÉTAPE 2 : ÉTAT
# ============================================================================


def etape_etat() -> dict:
    """2/6 ÉTAT — hub, ollama, jobs launchd, git (système + vault)."""
    log_message("Étape 2/6 : ÉTAT du système...")
    etat = {
        "timestamp": datetime.now().isoformat(),
        "hub_ok": False,
        "ollama_ok": False,
        "jobs_invalides": [],
        "git_systeme_propre": True,
        "git_vault_propre": True,
        "preuve_lecture_age_h": age_preuve_lecture(),  # None = jamais faite (règle 1septies)
    }

    try:
        req = urllib.request.Request(HUB_HEALTH_URL, method="GET")
        with urllib.request.urlopen(req, timeout=TIMEOUT_RESEAU) as resp:
            if resp.status == 200:
                etat["hub_ok"] = True
    except Exception:
        pass

    try:
        req = urllib.request.Request(OLLAMA_TAGS_URL, method="GET")
        with urllib.request.urlopen(req, timeout=TIMEOUT_RESEAU) as resp:
            if resp.status == 200:
                etat["ollama_ok"] = True
    except Exception:
        pass

    try:
        res = subprocess.run(["launchctl", "list"], capture_output=True,
                             text=True, timeout=TIMEOUT_RESEAU)
        if res.returncode == 0:
            output = res.stdout
            for job in JOBS_ATTENDUS:
                if job not in output:
                    etat["jobs_invalides"].append(job)
    except Exception as e:
        log_message(f"Erreur launchctl: {e}")

    # Git système + vault : 3 états — propre / sale / inaccessible (TCC en launchd)
    for cle, repo in (("git_systeme_propre", SYSTEME), ("git_vault_propre", VAULT)):
        try:
            res = subprocess.run(["git", "-C", str(repo), "status", "--short"],
                                 capture_output=True, text=True, timeout=TIMEOUT_RESEAU)
            if res.returncode == 0:
                etat[cle] = not bool(res.stdout.strip())
            else:
                # Le vault (~/Documents) est hors accès launchd/TCC (SPEC_SYNC) :
                # état illisible = INFORMATION, pas une anomalie.
                etat[cle] = None
                etat[cle.replace("propre", "") + "lisible"] = False
        except Exception:
            etat[cle] = None
            etat[cle.replace("propre", "") + "lisible"] = False

    return etat


# ============================================================================
# ÉTAPE 3 : DÉCISION (via le hub)
# ============================================================================


def etape_decision(contexte: dict, etat: dict) -> dict:
    """3/6 DÉCISION — hub (qwen.elabore) → JSON strict {action, detail, pourquoi}."""
    log_message("Étape 3/6 : DÉCISION via le hub...")

    if not etat["hub_ok"]:
        log_message("Hub injoignable → décision prudente : none")
        return {"action": "none", "detail": "Hub injoignable, aucune action risquée.",
                "pourquoi": "Sécurité réseau."}

    prompt_system = (
        "Tu es le module de décision d'un superviseur autonome macOS strict. "
        "Analyse l'état du système fourni. Réponds EXCLUSIVEMENT avec un objet JSON "
        "valide, sans markdown autour, au format exact : "
        '{"action": "none"|"fix"|"ask", "detail": "...", "pourquoi": "..."} '
        "- none : tout va bien ou anomalie mineure sans action. "
        "- fix : action mécanique simple (relancer un job mort, pousser git, sync). "
        "- ask : décision humaine nécessaire, ambiguïté, ou blocage persistant. "
        "RÈGLE ABSOLUE : ne JAMAIS toucher au trading (ACE/Hulk). "
        "Si un job est mort, propose 'fix' avec le nom exact du job dans detail.\n"
        "Un dépôt git 'sale' (fichiers modifiés ou non commités) est un état NORMAL "
        "de travail en cours — ce n'est JAMAIS une raison de 'ask'. Un état vault "
        "illisible/null (limitation TCC launchd sur ~/Documents) est connu et bénin. "
        "'ask' UNIQUEMENT pour : job mort répété, hub ou ollama injoignables, "
        "problème de sécurité, ou une décision humaine réelle (argent, trade, GO). "
        "Dans le doute : 'none'.\n"
    )
    prompt_user = (
        "État actuel du système :\n"
        f"{json.dumps(etat, indent=2, ensure_ascii=False)}\n\n"
        "Contexte fichiers (résumé) :\n"
        f"- ETAT_CONSOLIDE: {contexte.get('etat_consolide', '')[:500]}\n"
        f"- TOP_DEMAIN: {contexte.get('top_demain', '')[:300]}\n"
        f"- REVEIL_BUFFY: {contexte.get('reveil_buffy', '')[:300]}\n"
    )

    payload = {
        "task": "supervise.decision",
        "messages": [
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        "temperature": 0.2,
        "max_tokens": 300,
    }

    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(HUB_URL, data=data,
                                     headers={"Content-Type": "application/json"},
                                     method="POST")
        with urllib.request.urlopen(req, timeout=TIMEOUT_HUB) as resp:
            reponse = json.loads(resp.read().decode("utf-8"))
        content = reponse.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        # Nettoyage éventuel des balises markdown
        content = content.strip("`").strip()
        if content.startswith("json"):
            content = content[4:].strip()
        decision = json.loads(content)
        if decision.get("action") not in ("none", "fix", "ask"):
            raise ValueError("action inconnue")
        return decision
    except Exception as e:
        log_message(f"Erreur décision hub ({e}) → défaut : none")
        return {"action": "none", "detail": "Erreur parse décision hub.",
                "pourquoi": "Sécurité par défaut."}


# ============================================================================
# ÉTAPE 4 : AGIR
# ============================================================================


def escalade_attention(detail: str, pourquoi: str, dry_run: bool):
    """Écrit un bloc d'escalade humaine dans ATTENTION_VOCALE.md."""
    if dry_run:
        return
    bloc = (
        "\n\n## ⚠️ SUPERVISEUR — besoin de Christophe\n"
        f"- ts: {datetime.now().strftime('%Y%m%dT%H%MZ')}\n"
        f"- demande: {detail}\n"
        f"- pourquoi: {pourquoi}\n"
    )
    ATTENTION_DIR.mkdir(parents=True, exist_ok=True)
    ancien = lire_fichier(ATTENTION_VOCALE_PATH, 100000)
    ecriture_atomique(ATTENTION_VOCALE_PATH, ancien + bloc)


def rappel_lecture(dry_run: bool, tracker: dict) -> str:
    """Règle 1septies : si la preuve de lecture complète du coffre est absente ou
    plus vieille que 24 h, écrit un rappel dans A_Mon_Attention (le pont le copie
    vers le vault). Dédup : 1 rappel max par jour (clé date).

    C'est le rappel de Qwen (le superviseur tourne en Qwen local) — Ada le voit
    au réveil, c'est plus léger que de m'en remettre à ma mémoire."""
    age_h = tracker.get("preuve_lecture_age_h")
    if age_h is None or age_h > MAX_AGE_PREUVE_H:
        jour = datetime.now().strftime("%Y-%m-%d")
        if tracker.get("dernier_rappel_lecture") == jour:
            return f"rappel lecture déjà écrit aujourd'hui ({jour})"
        tracker["dernier_rappel_lecture"] = jour
        if dry_run:
            return "RAPPEL LECTURE (dry-run) : preuve absente/périmée → écrirait un rappel"
        bloc = (
            "\n\n## 📖 RAPPEL — LECTURE COMPLÈTE DU COFFRE (règle 1septies)\n"
            f"- ts: {datetime.now().strftime('%Y%m%dT%H%MZ')}\n"
            "- message: la preuve de lecture complète du coffre est absente ou "
            f"vielle de {('jamais' if age_h is None else f'{age_h:.0f} h')} (> {MAX_AGE_PREUVE_H} h).\n"
            "- action: lire INVENTAIRE_COMPLET.md en entier + graver la preuve "
            "« lecture complète » dans MEMOIRE_COLLAB (vault_inventory.py + buffy_reveil.py).\n"
        )
        ATTENTION_DIR.mkdir(parents=True, exist_ok=True)
        ancien = lire_fichier(RAPPEL_LECTURE_PATH, 100000)
        ecriture_atomique(RAPPEL_LECTURE_PATH, ancien + bloc)
        return f"rappel lecture écrit (âge preuve : {age_h if age_h is not None else 'aucune'})"
    return f"preuve lecture OK ({age_h:.1f} h < {MAX_AGE_PREUVE_H} h)"


def _besoin_humain_reel(etat: dict, detail: str) -> bool:
    """Garde mécanique déterministe (loi 5 : vérifier en code, pas dans le prompt).
    Correctif audit tiers 09/08 : logique INVERSÉE — on rétrograde UNIQUEMENT les
    motifs connus BÉNINS (git sale = WIP normal, vault illisible = TCC launchd,
    job fantôme « génère_auto », incohérence de répertoires, lecture 1septies).
    TOUT LE RESTE passe (défaut-refus sur le bénin, jamais de perte silencieuse
    d'une vraie demande : disque plein, quota, clé, backup, rapport...)."""
    if etat.get("jobs_invalides"):
        return True
    if not etat.get("hub_ok"):
        return True
    d = detail.lower()
    motifs_benins = ("git", "propre", "inaccessible", "incohérent", "incoherent",
                     "répertoire", "repertoire", "génère_auto", "genere_auto",
                     "lecture complète", "lecture complete", "état de git",
                     "dirty", "wip", "travail en cours")
    return not any(m in d for m in motifs_benins)


def etape_agir(decision: dict, etat: dict, tracker: dict, dry_run: bool) -> str:
    """4/6 AGIR — exécute l'action décidée (fix mécanique ou escalade ask)."""
    action = decision.get("action", "none")
    detail = str(decision.get("detail", ""))  # coerce : le modèle peut renvoyer un nombre
    pourquoi = str(decision.get("pourquoi", ""))
    log_message(f"Étape 4/6 : AGIR → {action}")

    if action == "none":
        return "rien à faire"

    if action == "ask" and not _besoin_humain_reel(etat, detail):
        # Trace des escalades ignorées (audit : ne rien avaler sans laisser de trace)
        ignorees = tracker.setdefault("escalades_ignorees", [])
        ignorees.append({"ts": datetime.now().strftime("%Y-%m-%dT%H:%MZ"),
                         "detail": detail[:200], "pourquoi": pourquoi[:200]})
        tracker["escalades_ignorees"] = ignorees[-20:]
        # Seuil : même demande non pertinente 3x/jour → on escalade quand même
        if sum(1 for e in tracker["escalades_ignorees"]
               if e.get("detail") == detail[:200]) >= 3:
            escalade_attention(f"(seuil 3x répété) {detail}", pourquoi, dry_run)
            return f"escalade (seuil 3x répété) : {detail[:120]}"
        log_message("Escalade ignorée (motif bénin) : " + detail[:120])
        return f"none (escalade ignorée, motif bénin) : {detail[:120]}"

    if action == "ask":
        # Dédup : ne ré-écrire que si la demande change (évite un bloc par heure)
        derniere = tracker.get("derniere_escalade", "")
        if detail == derniere:
            return f"escalade déjà notifiée (inchangée) : {detail}"
        tracker["derniere_escalade"] = detail
        escalade_attention(detail, pourquoi, dry_run)
        return f"escalade humaine : {detail}"

    # action == "fix" — PRIORITÉ 1 : relance d'un job launchd mort (avant les
    # branches push/sync/session : « git » est dans « gitpush », matching trop large)
    for job in JOBS_ATTENDUS:
        if job in detail and job in etat.get("jobs_invalides", []):
            compteur = tracker.get("relances", {}).get(job, 0)
            if compteur >= MAX_RELANCES_JOUR_PAR_JOB:
                escalade_attention(f"Limite de relances atteinte pour {job}",
                                   "3 relances/jour dépassées, intervention humaine requise.",
                                   dry_run)
                return f"job {job} : limite de relances atteinte → escalade écrite"
            tracker.setdefault("relances", {})[job] = compteur + 1
            if not dry_run:
                subprocess.run(["launchctl", "kickstart", f"gui/{os.getuid()}/{job}"],
                               capture_output=True, text=True, timeout=10)
            return f"relance job {job} (n°{compteur + 1}/jour)"

    # PRIORITÉ 2 : actions mécaniques par mots-clés
    if "git" in detail.lower() or "push" in detail.lower():
        if not dry_run and GIT_PUSH_SCRIPT.exists():
            subprocess.run(["bash", str(GIT_PUSH_SCRIPT)], capture_output=True,
                           text=True, timeout=60)
        return "push git lancé"

    if "sync" in detail.lower():
        if not dry_run and SYNC_NOW_SCRIPT.exists():
            subprocess.run(["bash", str(SYNC_NOW_SCRIPT)], capture_output=True,
                           text=True, timeout=30)
        return "pont OUTBOX→vault lancé"

    if "session" in detail.lower() or "reveil" in detail.lower():
        if not dry_run and SESSION_DEBUT_SCRIPT.exists():
            subprocess.run(["bash", str(SESSION_DEBUT_SCRIPT)], capture_output=True,
                           text=True, timeout=120)
        return "session_debut lancé"

    return f"action fix non reconnue (détaillée) : {detail[:120]}"


# ============================================================================
# ÉTAPE 5 : JOURNALISER
# ============================================================================


def etape_journaliser(etat: dict, decision: dict, resultat: str, dry_run: bool):
    def etat_git(v):
        return 'P' if v is True else ('?' if v is None else 'D')
    ligne = (f"| {datetime.now().strftime('%Y-%m-%dT%H:%MZ')} | SUPERVISEUR | "
             f"hub={'OK' if etat.get('hub_ok') else 'DOWN'} ollama={'OK' if etat.get('ollama_ok') else 'DOWN'} "
             f"jobs_manquants={etat.get('jobs_invalides', [])} "
             f"git_sys={etat_git(etat.get('git_systeme_propre'))} "
             f"git_vault={etat_git(etat.get('git_vault_propre'))} "
             f"action={decision.get('action')} résultat={resultat} |")
    append_log_borne(ligne, dry_run)


# ============================================================================
# ÉTAPE 6 : POUSSER
# ============================================================================


def etape_pousser(dry_run: bool, action: str):
    """6/6 POUSSER — push git si des changements ont été faits."""
    if dry_run or action == "rien à faire":
        return
    if GIT_PUSH_SCRIPT.exists():
        try:
            subprocess.run(["bash", str(GIT_PUSH_SCRIPT)], capture_output=True,
                           text=True, timeout=120)
            log_message("Push automatique exécuté")
        except Exception as e:
            log_message(f"Erreur push: {e}")


# ============================================================================
# MAIN
# ============================================================================


def main():
    ap = argparse.ArgumentParser(description="Superviseur autonome ACE777")
    ap.add_argument("--dry-run", action="store_true",
                    help="lit l'état et propose une action sans rien écrire")
    args = ap.parse_args()

    dry_run = args.dry_run
    log_message(f"=== CYCLE SUPERVISEUR {'(DRY-RUN)' if dry_run else ''} ===")

    try:
        contexte = etape_lire()
        etat = etape_etat()
        tracker = charger_tracker()
        # Garde mécanique (règle 1septies) : le rappel de lecture passe dans l'état
        # pour que Qwen le voie, et se déclenche indépendamment de la décision du hub.
        tracker["preuve_lecture_age_h"] = etat.get("preuve_lecture_age_h")
        resultat_rappel = rappel_lecture(dry_run, tracker)
        decision = etape_decision(contexte, etat)
        resultat = etape_agir(decision, etat, tracker, dry_run)
        if resultat_rappel and "preuve lecture OK" not in resultat_rappel:
            resultat = f"{resultat} | {resultat_rappel}"
        etape_journaliser(etat, decision, resultat, dry_run)
        sauvegarder_tracker(tracker, dry_run)
        etape_pousser(dry_run, resultat)

        log_message(f"Résultat : {resultat}")
        print(json.dumps({"action": decision.get("action"),
                          "detail": decision.get("detail"),
                          "resultat": resultat,
                          "jobs_manquants": etat.get("jobs_invalides", []),
                          "hub_ok": etat.get("hub_ok")}, ensure_ascii=False))
        return 0
    except Exception as e:
        log_message(f"ERREUR FATALE (non fatale par design) : {e}")
        append_log_borne(f"| {datetime.now().strftime('%Y-%m-%dT%H:%MZ')} | SUPERVISEUR | ERREUR: {e} |", dry_run)
        return 1


if __name__ == "__main__":
    sys.exit(main())
