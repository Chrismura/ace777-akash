# RÉPONSE HUB (task code.ia · via Puter Grok (gratuit)) — 2026-08-13T16:00:33

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
famille_session.py — Module consultation Famille ACE777 (v6)
Verrou famille + mode tempête + trio réel (Gemini/DeepSeek/Juge)
Fusion v3 (trio réel) + corrections v4 (os.close, mode tempête) + v5 (TTL conservé)
+ Ajustements v6 : vortex >= 2, TTL seulement si occasion, join aligné sur 245s
Python 3.9 stdlib uniquement — macOS compatible — non fatal
"""

import os
import json
import time
import fcntl
import threading
import urllib.request
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, Any

# ============================================================
# CHEMINS ABSOLUS (v3)
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
STRATEGIE_DIR = (SCRIPT_DIR.parent / "strategie").resolve()
STRATEGIE_DIR.mkdir(parents=True, exist_ok=True)

FICHIER_LIVE = str(STRATEGIE_DIR / "journal_intention_live.json")
FICHIER_ALARME = str(STRATEGIE_DIR / "alarme.json")
FICHIER_ETAT = str(STRATEGIE_DIR / ".famille_etat")
FICHIER_AVIS = str(STRATEGIE_DIR / "AVIS_FAMILLE_SESSION.md")
FICHIER_LOCK = str(STRATEGIE_DIR / ".famille.lock")
HISTORIQUE_DIR = STRATEGIE_DIR / "historique_famille"
HISTORIQUE_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# CONSTANTES RÉELLES
# ============================================================
HUB = "http://127.0.0.1:11435/v1/chat/completions"
ALARME_FRAICHEUR_H = 6
ANTI_SPAM_MIN = 5

ROLES = {
    "audit.protocol": (
        "Tu es Gemini, analyste senior de la maison ACE777. Donne un avis CONCIS "
        "(2-3 phrases max) : les risques, les angles morts, ce qu'on pourrait rater. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
    "mission": (
        "Tu es DeepSeek, expert technique de la maison ACE777. Donne un avis CONCIS "
        "(2-3 phrases max) : la cohérence du setup, ce qui peut casser, la faisabilité. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
    "signets.juge": (
        "Tu es le JUGE de la maison ACE777. Après avoir pesé les arguments, TRANCHE la "
        "décision de façon claire et concise (2-3 phrases max) : OUI / NON / SOUS CONDITION. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
}

TASKS = ["audit.protocol", "mission", "signets.juge"]
NOMS = ["GEMINI (analyste)", "DEEPSEEK (technique)", "LE JUGE tranche"]


# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================
def lire_json(path: str, default: Any = None) -> Any:
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return default


def _ecrire_avis_famille(contenu: str) -> None:
    try:
        with open(FICHIER_AVIS, "w", encoding="utf-8") as f:
            f.write(contenu)
    except Exception:
        pass

    try:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        hist_path = HISTORIQUE_DIR / f"AVIS_{ts}.md"
        with open(hist_path, "w", encoding="utf-8") as f:
            f.write(contenu)
    except Exception:
        pass


def _duree_anti_spam() -> float:
    """Retourne la durée anti-spam selon le mode (tempête ou calme)."""
    try:
        if mode_tempete_actif():
            return 60.0
        return ANTI_SPAM_MIN * 60.0
    except Exception:
        return ANTI_SPAM_MIN * 60.0


def _verifier_etat_ttl() -> bool:
    """Vérifie si le TTL anti-spam est encore valide (timestamp initial conservé)."""
    try:
        etat = lire_json(FICHIER_ETAT, {})
        if not etat or "timestamp" not in etat:
            return False
        duree = _duree_anti_spam()
        return (time.time() - etat["timestamp"]) < duree
    except Exception:
        return False


def _creer_etat_ttl() -> None:
    """Crée l'état TTL avec timestamp initial (appelé seulement si occasion réelle)."""
    try:
        etat = {
            "timestamp": time.time(),
            "source": "famille_session_v6"
        }
        with open(FICHIER_ETAT, "w", encoding="utf-8") as f:
            json.dump(etat, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _noter_fin_consultation() -> None:
    """Ajoute une note de fin sans modifier le timestamp initial."""
    try:
        etat = lire_json(FICHIER_ETAT, {})
        if etat and "timestamp" in etat:
            etat["derniere_fin"] = time.time()
            with open(FICHIER_ETAT, "w", encoding="utf-8") as f:
                json.dump(etat, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# ============================================================
# FONCTIONS RÉELLES DU TRIO
# ============================================================
def _appel_hub(task: str, messages: list, resultats: dict, cle: str) -> None:
    """Appel hub pour un membre du trio (thread). timeout=None (règle maison)."""
    payload = {
        "task": task,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 500,
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=None) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            resultats[cle] = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print("famille: appel %s en echec (%s)" % (task, e), file=sys.stderr)
        resultats[cle] = None


def est_une_occasion(live: dict, force: bool = False) -> Tuple[bool, str]:
    """Détermine si une occasion de consultation existe (déterministe)."""
    if force:
        return True, "demande explicite"

    try:
        if os.path.exists(FICHIER_ALARME):
            frais = (time.time() - os.path.getmtime(FICHIER_ALARME)) < ALARME_FRAICHEUR_H * 3600
            alarme = lire_json(FICHIER_ALARME, {})
            if frais and alarme and isinstance(alarme, dict) and alarme.get("type"):
                return True, "alerte en cours"
    except Exception:
        pass

    bots = (live or {}).get("bots", {})
    alpha = bots.get("alpha", {})
    if alpha.get("fills", 0) > 0 and alpha.get("pnl", 0.0) < 0:
        return True, "session dans le rouge"

    if alpha.get("revenge", 0) >= 3:
        return True, "rafale de mode revenge"

    return False, ""


def build_sujet(live: dict) -> str:
    """Construit le brief compact en français pour le trio."""
    bots = (live or {}).get("bots", {})
    alpha = bots.get("alpha", {})
    beta = bots.get("beta", {})
    story = (live or {}).get("story", [])

    alerte_txt = "aucune"
    try:
        a = lire_json(FICHIER_ALARME, None)
        if a:
            alerte_txt = json.dumps(a, ensure_ascii=False)[:300]
    except Exception:
        pass

    return (
        "SESSION (depuis %s) :\n"
        "• ALPHA (Le Sniper) : %s tirs, %s skips (discipline), pnl %+.2f $, "
        "dont %s revenge 1.5x\n"
        "• BETA (L'Éclaireur) : %s sondes, conf moyenne %s, %s long / %s court\n"
        "• STORY : %s\n"
        "• ALERTE : %s\n"
        "QUESTION : cette session appelle-t-elle une action ? (ajuster le setup, "
        "réduire l'exposition, laisser courir...) Réponds en français, macOS, concis."
        % (
            live.get("since", "N/A"),
            alpha.get("fills", 0), alpha.get("skips", 0), alpha.get("pnl", 0.0),
            alpha.get("revenge", 0),
            beta.get("fills", 0), beta.get("conf_moy", 0),
            beta.get("direction", {}).get("long", 0),
            beta.get("direction", {}).get("short", 0),
            " | ".join(story[-3:]) if story else "aucune",
            alerte_txt,
        )
    )


# ============================================================
# THREAD RÉEL DU TRIO (v6)
# ============================================================
def _thread_trio(lock_fd: int) -> None:
    """Thread qui détient le verrou flock jusqu'à la fin réelle des 3 appels."""
    resultats = {}
    try:
        live = lire_json(FICHIER_LIVE, {}) or {}
        occasion, raison = est_une_occasion(live)
        if not occasion:
            return

        # TTL créé ici seulement si occasion réelle (ajustement v6)
        _creer_etat_ttl()

        sujet = build_sujet(live)

        threads = []
        for task in TASKS:
            t = threading.Thread(
                target=_appel_hub,
                args=(task, [{"role": "system", "content": ROLES[task]},
                             {"role": "user", "content": sujet}], resultats, task),
                daemon=True)
            threads.append(t)
            t.start()
        for t in threads:
            t.join(timeout=240)

        parties = []
        for i, task in enumerate(TASKS):
            r = resultats.get(task)
            if r:
                parties.append("• %s : %s" % (NOMS[i], r.strip()))
            else:
                parties.append("• %s : (injoignable)" % NOMS[i])

        ts = datetime.now().isoformat()
        contenu = (
            "# AVIS FAMILLE SESSION — %s\n"
            "OCCASION : %s\n\n"
            "🟡 CONSULTATION FAMILLE\n\n"
            "%s\n\n"
            "— Famille consultée, %s\n"
            % (ts, raison, "\n\n".join(parties),
               datetime.now().strftime("%d/%m/%Y %H:%M"))
        )
        contenu = contenu.replace("**", "")
        _ecrire_avis_famille(contenu)

    except Exception:
        pass
    finally:
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_UN)
        except Exception:
            pass
        try:
            os.close(lock_fd)
        except Exception:
            pass
        try:
            _noter_fin_consultation()
        except Exception:
            pass


# ============================================================
# MODE TEMPÊTE (v6 avec vortex)
# ============================================================
def mode_tempete_actif() -> bool:
    """Détecte le mode tempête selon ADA ROUGE / vortex / alarme / etat_tempete."""
    try:
        # 1) Zone ADA ROUGE / PRENDS_LA_PERTE
        g = lire_json(str(STRATEGIE_DIR / "ada_gardienne_live.json"), {})
        zone = str(g.get("zone", "")).upper()
        if zone in ("ROUGE", "PRENDS_LA_PERTE"):
            return True

        # 1.5) Vortex saison force >= 2 (tempête qui monte)
        try:
            saison = lire_json(str(STRATEGIE_DIR / "ada_saison_live.json"), {})
            if int(saison.get("vortex", {}).get("force", 0) or 0) >= 2:
                return True
        except Exception:
            pass

        # 2) Alarme récente (dernière heure)
        try:
            if os.path.exists(FICHIER_ALARME):
                if (time.time() - os.path.getmtime(FICHIER_ALARME)) < 3600:
                    a = lire_json(FICHIER_ALARME, {})
                    if isinstance(a, dict) and a.get("type"):
                        return True
        except Exception:
            pass

        # 3) Fichier d'état tempête explicite
        etat = lire_json(str(STRATEGIE_DIR / "etat_tempete.json"), {})
        return bool(etat.get("actif", False))
    except Exception:
        return False


# ============================================================
# FONCTION PRINCIPALE (v6)
# ============================================================
def consulter_famille(force: bool = False) -> None:
    """
    Point d'entrée principal (v6).
    Vérifie TTL (sauf force ou tempête), acquiert le verrou,
    puis lance le thread trio. Le TTL n'est créé que dans le thread
    si une occasion réelle existe.
    """
    try:
        if not force and not mode_tempete_actif() and _verifier_etat_ttl():
            return

        lock_fd = os.open(FICHIER_LOCK, os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(lock_fd)
            return

        # Plus de création TTL ici (ajustement v6) : le flock suffit pendant le thread
        t = threading.Thread(target=_thread_trio, args=(lock_fd,), daemon=True)
        t.start()
        t.join(timeout=245)

    except Exception:
        pass


# ============================================================
# POINT D'ENTRÉE
# ============================================================
if __name__ == "__main__":
    consulter_famille()
```
