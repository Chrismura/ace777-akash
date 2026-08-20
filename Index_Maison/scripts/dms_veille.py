#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dms_veille.py — DEAD MAN'S SWITCH EXTERNE de la veille de dégradation (20/08).

Exigence famille (consultation canonique 20/08, GO-AVEC-RÉSERVES 82-88 %) :
« qui surveille la surveillante ? » La brique veille_degradation.py peut mourir
ou se figer SILENCIEUSEMENT (le pattern même qu'elle détecte). Ce script est un
TIERS INDÉPENDANT, lancé par sa propre plist launchd (com.ace777.dms-veille) :
il surveille la FRESHEUR de veille_degradation_etat.json (écrit ~60 s par la
brique) et l'état SAIN. Si le signal de vie s'arrête (fichier stale) ou si la
brique elle-même est déchargée → ALERTE VOCALE + journal, tant que ça ne va pas.

Anti-piège (famille) : le DMS n'utilise PAS la brique pour se vérifier — il lit
le fichier directement et vérifie launchctl lui-même. Canal externe : alerte
vocale (edge_tts) + data/alertes/DMS_VEILLE.json, lisible par le cockpit.

Stdlib uniquement, kill-switch, anti-empilement (une seule alerte à la fois).
"""
import json
import os
import subprocess
import sys
import time
import tempfile
from pathlib import Path

HOME = Path.home()
ROOT = HOME / "ace777-test-day1"
IM = ROOT / "Index_Maison"
ETAT_JSON = IM / "etat" / "veille_degradation_etat.json"
ALERTES_DIR = IM / "data" / "alertes"
ALERTE_VOCALE = IM / "scripts" / "alerte_vocale.py"
STOP_ALL = IM / "STOP_ALL"
STOP_STRAT = IM / "strategie" / "STOP"

# Tolérance : la brique écrit ~60 s. Stale si > 5 min (marge ×5 : ni faux
# positifs sur un Mac en veille, ni silence radio prolongé).
SEUIL_STALE_SEC = 300
# Plists dont le DMS vérifie lui-même la présence (le filet sous le filet).
PLISTS_CLEFS = [
    "com.ace777.veille-degradation",   # la brique elle-même
    "com.ace777.sante-index",          # le pré-vol des index
    "com.ace777.superviseur-core",     # les colonnes du cockpit
]
ID_ALERTE = "DMS_VEILLE"


def check_kill_switch():
    for s in (STOP_ALL, STOP_STRAT):
        if s.exists():
            print(f"[DMS] Kill-switch actif : {s} — sortie.", file=sys.stderr)
            sys.exit(0)


def ecrire_atomique(chemin: Path, data: dict):
    check_kill_switch()
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def lire_etat_brique():
    """Lit l'état de la brique : (fraiche, statut, age_sec, detail)."""
    if not ETAT_JSON.exists():
        return False, "ABSENT", None, "fichier veille_degradation_etat.json introuvable"
    try:
        data = json.loads(ETAT_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return False, "ILLISIBLE", None, f"json illisible : {e}"
    age = int(time.time()) - int(data.get("timestamp", 0))
    statut = data.get("statut_global", "?")
    fraiche = age <= SEUIL_STALE_SEC
    detail = (f"âge {age}s (seuil {SEUIL_STALE_SEC}s), statut {statut}"
              if fraiche else f"STALE : dernier battement il y a {age}s (seuil {SEUIL_STALE_SEC}s)")
    return fraiche and statut == "SAIN", statut, age, detail


def plists_manquantes():
    """Vérifie lui-même launchctl (ne fait pas confiance à la brique).
    Retourne (manquantes, etat_inconnu). En cas d'ERREUR d'exécution
    (timeout/ressources sous charge), on NE déclare PAS tout manquant :
    une fausse alerte désensibilise (cri de loup). On signale INCONNU
    (état indéterminé) — la brique veille_degradation fait foi alors.
    Corrigé 20/08 (charge load 7.0 : launchctl list timeoute → fausse
    alerte DMS permanente pendant le run 72h)."""
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True,
                             text=True, timeout=5)
        lignes = out.stdout or ""
    except Exception as e:
        return [], f"ETAT_INCONNU (launchctl indisponible: {e})"
    return [p for p in PLISTS_CLEFS if p not in lignes], "OK"


def alerte_vocale_en_cours() -> bool:
    try:
        out = subprocess.check_output(["pgrep", "-f", "alerte_vocale.py"],
                                      text=True, stderr=subprocess.DEVNULL)
        return bool(out.strip())
    except Exception:
        return False


def lancer_alerte(raison: str):
    """Double canal (exigence GROK/GEMINI, tour 2) :
    1. CANAL A — fichier d'alerte JSON (data/alertes/DMS_WEBHOOK.json) : canal
       externe asynchrone, lu par le cockpit — ne dépend ni de la voix ni du
       shell parent. Toujours écrit, même si la voix échoue.
    2. CANAL B — alerte vocale (si aucune n'est déjà en cours).
    """
    # CANAL A : webhook local (fichier ring-buffer) — indépendant de la voix
    try:
        webhook = ALERTES_DIR / "DMS_WEBHOOK.json"
        ecrire_atomique(webhook, {
            "timestamp": int(time.time()),
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "type": "DMS_ALERTE",
            "raison": raison,
            "canal": "webhook_local",
        })
        print(f"[DMS] canal webhook écrit : {webhook.name}")
    except Exception as e:
        print(f"[DMS] ERREUR canal webhook : {e}")
    # CANAL B : voix (anti-empilement)
    if alerte_vocale_en_cours():
        print(f"[DMS] alerte déjà en cours — skip voix (anti-empilement). raison={raison}")
        return
    msg = ("Alerte. Dead man switch. La surveillance de la dégradation est "
           "tombée ou s est figée. " + raison + ". Répétition en continu "
           "jusqu à extinction manuelle.")
    try:
        subprocess.Popen([sys.executable, str(ALERTE_VOCALE), "--message", msg,
                          "--id", ID_ALERTE],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[DMS] alerte vocale lancée : {raison}")
    except Exception as e:
        print(f"[DMS] ERREUR alerte vocale : {e}")


def main():
    # --test-panne : CHAOS TEST (exigence famille 20/08) — simule une brique
    # morte pour PROUVER que l'alerte sort réellement (une alerte non testée
    # par le feu n'est qu'un vœu pieux — ULTRA). Ne touche à rien de réel.
    test_panne = "--test-panne" in sys.argv
    check_kill_switch()
    if test_panne:
        fraiche, statut, age, detail = (False, "TEST_PANNE_SIMULEE", None,
                                        "test de chaos : brique simulée morte")
        manquantes, etat_inconnu = [], "OK"
    else:
        fraiche, statut, age, detail = lire_etat_brique()
        manquantes, etat_inconnu = plists_manquantes()

    anomalies = []
    if not fraiche:
        anomalies.append(f"veille_degradation {detail}")
    for p in manquantes:
        anomalies.append(f"plist {p} NON CHARGÉE (le filet sous le filet manque)")
    # État INCONNU (launchctl indisponible) : info, PAS une alerte — une
    # fausse alerte désensibilise (cri de loup). La brique SAIN fait foi.
    info_inconnu = etat_inconnu if (etat_inconnu != "OK" and fraiche) else None

    rapport = {
        "timestamp": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "dms_veille (Dead Man's Switch externe, exigence famille 20/08)",
        "brique": {"statut": statut, "age_sec": age, "detail": detail},
        "plists_manquantes": manquantes,
        "etat_inconnu": info_inconnu,
        "anomalies": anomalies,
        "statut": "ALERTE" if anomalies else "OK",
    }

    if anomalies:
        raison = " ; ".join(anomalies)[:200]
        lancer_alerte(raison)
        # Le DMS écrit lui-même son rapport ALERTE : même si la brique est
        # morte, le cockpit voit le trou (canal indépendant).
        ecrire_atomique(ALERTES_DIR / "DMS_VEILLE.json", rapport)
        print(f"[DMS] ALERTE — {raison}")
    else:
        # Tout va bien : on nettoie les reliquats d'alerte et on journalise OK.
        try:
            (IM / f"STOP_ALERTE_{ID_ALERTE}").unlink(missing_ok=True)
            (ALERTES_DIR / f"STOP_ALERTE_{ID_ALERTE}").unlink(missing_ok=True)
        except Exception:
            pass
        ecrire_atomique(ALERTES_DIR / "DMS_VEILLE.json", rapport)
        print(f"[DMS] OK — brique SAIN, plists {len(PLISTS_CLEFS) - len(manquantes)}/{len(PLISTS_CLEFS)}")


if __name__ == "__main__":
    main()
