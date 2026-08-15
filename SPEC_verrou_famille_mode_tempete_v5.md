# SPEC v5 — FUSION FINALE (trio réel v3 + corrections v4, SANS suppression du TTL)

## Statut et problème

La v4 a corrigé les 3 points (os.close, mode tempête branché, TTL après flock) MAIS a
introduit **2 régressions bloquantes** signalées par DEEPSEEK (audit V4) :

1. **Le vrai trio a disparu.** La v3 contenait le trio réel (3 appels hub via
   `_appel_hub` avec ROLES/TASKS/NOMS, `est_une_occasion`, `build_sujet`, écriture de
   `AVIS_FAMILLE_SESSION.md`). La v4 a remplacé tout ça par un stub qui ne fait que
   lire/écrire le JSON d'état — AUCUN appel au hub. C'est interdit par la spec
   (« zéro placeholder »).
2. **Suppression intempestive de FICHIER_ETAT.** Dans le `finally` de `_thread_trio`,
   la v4 fait `os.remove(FICHIER_ETAT)`. Résultat : l'état TTL (anti-spam) est effacé
   à la fin de chaque consultation → l'anti-spam 5 min (calme) / 60 s (tempête) ne
   tient PAS → l'appel suivant (10 s plus tard) repart → **le bug du 13/08 revient**.

**Consigne : la v5 est une FUSION.** Le codeur doit produire un module complet =
structure et trio réel de la v3 (le bon code) + les 3 corrections de la v4 (os.close,
mode tempête, TTL juste après flock) + le TTL CONSERVÉ (jamais supprimé à la fin).

## RÈGLES ABSOLUES

1. Python 3.9 stdlib, pas de dépendance externe.
2. `typing.Optional`, jamais `str | None`.
3. Non fatal, UTF-8, ne pas toucher au moteur ACE ni aux formats produits.
4. Fichiers : `Index_Maison/scripts/` + `Index_Maison/strategie/`.

## CE QU'IL FAUT FAIRE (exactement)

### 1. BASE = la v3 (`CODE_verrou_famille_mode_tempete_v3.md`)
Prendre la v3 ENTIÈRE comme base : elle contient le BON code —
- Chemins absolus : `SCRIPT_DIR`/`STRATEGIE_DIR`, FICHIER_LIVE, FICHIER_ALARME,
  FICHIER_ETAT, FICHIER_AVIS, FICHIER_LOCK, HISTORIQUE_DIR ✅
- Constantes réelles : HUB, ALARME_FRAICHEUR_H, ANTI_SPAM_MIN, ROLES, TASKS, NOMS ✅
- `lire_json`, `_ecrire_avis_famille` ✅
- **`_appel_hub` RÉEL** (payload, urlopen timeout=None, écrit dans resultats) ✅
- **`est_une_occasion` RÉEL** (alarme / session rouge / revenge) ✅
- **`build_sujet` RÉEL** (brief complet) ✅
- **`_thread_trio` RÉEL** (lit live, est_une_occasion, build_sujet, lance les 3
  threads du trio, joint 240, écrit AVIS_FAMILLE_SESSION.md + historique) ✅

### 2. APPLIQUER les corrections v4 par-dessus la v3

- **C1 (v4) — os.close(lock_fd)** : dans le `finally` de `_thread_trio`, après
  `fcntl.flock(lock_fd, fcntl.LOCK_UN)`, ajouter `os.close(lock_fd)`.
- **C2 (v4) — mode tempête branché** :
  - `consulter_famille(force=False)` : `if not force and not mode_tempete_actif() and _verifier_etat_ttl(): return`
  - `_duree_anti_spam()` retourne 60.0 si `mode_tempete_actif()` sinon
    `ANTI_SPAM_MIN * 60.0`
  - `mode_tempete_actif()` : zone ADA ROUGE/PRENDS_LA_PERTE, puis alarme < 1 h,
    puis `etat_tempete.json` (version v4, robuste).
- **C3 (v4) — TTL juste après le flock** : dans `consulter_famille()`, `_creer_etat_ttl()`
  immédiatement après le `flock` réussi (avant le lancement du thread).

### 3. NE PAS supprimer FICHIER_ETAT (correctif v5)

- **Supprimer le `os.remove(FICHIER_ETAT)` du `finally` de `_thread_trio`.**
- Le fichier TTL reste en place après la consultation : c'est lui qui fait tenir
  l'anti-spam (5 min calme / 60 s tempête) entre deux consultations.
- À la place, dans le `finally`, on peut écrire une note de fin dans le fichier
  (ex. `derniere_fin = time.time()`), MAIS le `timestamp` initial (début de
  consultation) ne doit pas être modifié — `_verifier_etat_ttl()` compare
  `time.time() - etat["timestamp"]` à la durée. Ne pas rajeunir ce timestamp.
- `FICHIER_ETAT` n'est jamais supprimé par le module (sauf éventuellement par un
  nettoyage manuel externe).

## CONTRAT DE SORTIE v5

Le module `famille_session.py` v5 COMPLET, prêt à copier dans
`Index_Maison/scripts/famille_session.py` : v3 (trio réel) + C1/C2/C3 (v4) + TTL
conservé (v5). Zéro placeholder, zéro stub, zéro `pass` dans les fonctions métier,
syntaxe valide Python 3.9, commentaires en français, non fatal.

## FICHIER CONCERNÉ

- `Index_Maison/scripts/famille_session.py` (v5 complète)


---

## ANNEXE — CODE v3 (BASE, à fusionner)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
famille_session.py — Module consultation Famille ACE777 (v3)
Verrou famille + mode tempête + trio réel (Gemini/DeepSeek/Juge)
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
# CHEMINS ABSOLUS (v2 corrigé)
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
# CONSTANTES RÉELLES (copiées)
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
# FONCTIONS UTILITAIRES (v2 + v3)
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
    """Retourne le temps minimum entre deux consultations (secondes)."""
    return ANTI_SPAM_MIN * 60


def _verifier_etat_ttl() -> bool:
    """Vérifie si un état TTL est encore valide."""
    try:
        if not os.path.exists(FICHIER_ETAT):
            return False
        mtime = os.path.getmtime(FICHIER_ETAT)
        return (time.time() - mtime) < _duree_anti_spam()
    except Exception:
        return False


def _creer_etat_ttl() -> None:
    try:
        Path(FICHIER_ETAT).touch(exist_ok=True)
    except Exception:
        pass


# ============================================================
# FONCTIONS RÉELLES DU TRIO (copiées mot pour mot)
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
# THREAD RÉEL DU TRIO (v3)
# ============================================================
def _thread_trio(lock_fd: int) -> None:
    """Thread qui détient le verrou flock jusqu'à la fin réelle des 3 appels."""
    resultats = {}
    try:
        live = lire_json(FICHIER_LIVE, {}) or {}
        occasion, raison = est_une_occasion(live)
        if not occasion:
            return

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
            if os.path.exists(FICHIER_ETAT):
                os.remove(FICHIER_ETAT)
        except Exception:
            pass


# ============================================================
# FONCTION PRINCIPALE (v2 + v3 intégrée)
# ============================================================
def consulter_famille(force: bool = False) -> None:
    """
    Point d'entrée principal.
    - Vérifie l'état TTL au début
    - Acquiert le verrou flock
    - Lance le thread trio (qui détient le verrou jusqu'à la fin)
    - Ne relâche JAMAIS le lock dans cette fonction
    """
    if _verifier_etat_ttl():
        return

    try:
        lock_fd = os.open(FICHIER_LOCK, os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(lock_fd)
            return

        _creer_etat_ttl()

        t = threading.Thread(target=_thread_trio, args=(lock_fd,), daemon=True)
        t.start()
        t.join(timeout=90)

    except Exception:
        pass


# ============================================================
# MODE TEMPÊTE (stub minimal non fatal)
# ============================================================
def mode_tempete_actif() -> bool:
    """Retourne True si le mode tempête est actif (à connecter au moteur ACE)."""
    try:
        etat = lire_json(str(STRATEGIE_DIR / "etat_tempete.json"), {})
        return bool(etat.get("actif", False))
    except Exception:
        return False


if __name__ == "__main__":
    consulter_famille()

```


---

## ANNEXE — CODE v4 (corrections C1-C3, à extraire)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
famille_session.py — v4
Module de verrouillage famille avec mode tempête (machine de tempête)
Python 3.9 stdlib uniquement — non fatal — commentaires en français
"""

import os
import fcntl
import time
import threading
import json
from pathlib import Path
from typing import Optional, Dict, Any

# === CONSTANTES ===
BASE_DIR = Path("Index_Maison")
SCRIPTS_DIR = BASE_DIR / "scripts"
STRATEGIE_DIR = BASE_DIR / "strategie"

FICHIER_LOCK = str(SCRIPTS_DIR / "famille.lock")
FICHIER_ETAT = str(SCRIPTS_DIR / "famille_etat.json")
FICHIER_ALARME = str(SCRIPTS_DIR / "alarme.json")
ANTI_SPAM_MIN = 5.0


def lire_json(chemin: str, defaut: Any = None) -> Any:
    """Lecture JSON non fatale."""
    if defaut is None:
        defaut = {}
    try:
        if os.path.exists(chemin):
            with open(chemin, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return defaut


def ecrire_json(chemin: str, donnees: Dict[str, Any]) -> None:
    """Écriture JSON non fatale."""
    try:
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _creer_etat_ttl() -> None:
    """Crée l'état TTL immédiatement après le verrou."""
    try:
        etat = {
            "timestamp": time.time(),
            "source": "famille_session_v4"
        }
        ecrire_json(FICHIER_ETAT, etat)
    except Exception:
        pass


def _verifier_etat_ttl() -> bool:
    """Vérifie si le TTL anti-spam est encore valide."""
    try:
        etat = lire_json(FICHIER_ETAT, {})
        if not etat or "timestamp" not in etat:
            return False
        duree = _duree_anti_spam()
        return (time.time() - etat["timestamp"]) < duree
    except Exception:
        return False


def mode_tempete_actif() -> bool:
    """Détecte le mode tempête selon la machine de tempête (ADA ROUGE / alarme / etat_tempete)."""
    try:
        # 1) Zone ADA ROUGE / PRENDS_LA_PERTE
        g = lire_json(str(STRATEGIE_DIR / "ada_gardienne_live.json"), {})
        zone = str(g.get("zone", "")).upper()
        if zone in ("ROUGE", "PRENDS_LA_PERTE"):
            return True

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


def _duree_anti_spam() -> float:
    """Retourne la durée anti-spam selon le mode (tempête ou calme)."""
    try:
        if mode_tempete_actif():
            return 60.0  # tempête : réactivité immédiate
        return ANTI_SPAM_MIN * 60.0  # calme : 5 minutes
    except Exception:
        return ANTI_SPAM_MIN * 60.0


def _thread_trio(lock_fd: int) -> None:
    """Thread qui exécute le trio réel (consultation famille + actions)."""
    try:
        # === TRIO RÉEL INTÉGRÉ ===
        # 1. Lecture de l'état famille
        etat_famille = lire_json(FICHIER_ETAT, {})

        # 2. Vérification et mise à jour des membres actifs
        membres = etat_famille.get("membres", [])
        if not isinstance(membres, list):
            membres = []

        # 3. Actions stratégiques (exemple : mise à jour timestamp)
        etat_famille["derniere_consultation"] = time.time()
        etat_famille["mode_tempete"] = mode_tempete_actif()
        ecrire_json(FICHIER_ETAT, etat_famille)

        # Ici pourrait être ajouté le vrai traitement métier
        # (sans placeholder — logique minimale fonctionnelle)

    except Exception:
        pass
    finally:
        # Libération propre du verrou + fermeture descripteur (correction 1)
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_UN)
        except Exception:
            pass
        try:
            os.close(lock_fd)
        except Exception:
            pass
        try:
            if os.path.exists(FICHIER_ETAT):
                os.remove(FICHIER_ETAT)
        except Exception:
            pass


def consulter_famille(force: bool = False) -> None:
    """
    Point d'entrée principal.
    Applique le verrou flock + TTL + mode tempête (corrections 2 et 3).
    """
    try:
        # Bypass TTL en mode tempête ou sur force explicite (correction 2a)
        if not force and not mode_tempete_actif() and _verifier_etat_ttl():
            return

        # Ouverture et verrouillage exclusif non bloquant
        lock_fd = os.open(FICHIER_LOCK, os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(lock_fd)
            return

        # Création immédiate de l'état TTL après le flock réussi (correction 3)
        _creer_etat_ttl()

        # Lancement du thread trio
        t = threading.Thread(target=_thread_trio, args=(lock_fd,), daemon=True)
        t.start()
        t.join(timeout=90)

    except Exception:
        pass


# === POINT D'ENTRÉE OPTIONNEL ===
if __name__ == "__main__":
    consulter_famille(force=True)

```
