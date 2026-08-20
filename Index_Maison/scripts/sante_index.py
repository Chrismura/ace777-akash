#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SANTE_INDEX.py — PRÉ-VOL DES INDEX (conception Christophe, 17/08/2026).
Vérifie que chaque chaîne d'index est branchée DE BOUT EN BOUT et écrit le
rapport thermo/sante_index.json affiché sur le cockpit (carte SANTÉ).

Ce que la veilleuse ne vérifie pas : la veilleuse vérifie l'intégrité (md5)
et la fraîcheur des fichiers UN PAR UN — pas que la donnée TRAVERSE la chaîne.
Exemple vécu : le scan baleines tournait (fichier frais) mais le pont n'était
lancé par aucune plist → Ada/Cortana ne recevaient rien, et rien ne le montrait.
Ici : chaque chaîne est vérifiée maillon par maillon (process → fichier → clé
présente chez le consommateur), avec l'âge réel de chaque fichier.

Stdlib uniquement. Ne touche à rien : lecture seule + écriture atomique du rapport.
"""

import os
import sys
import json
import time
import tempfile
import subprocess
from pathlib import Path
from datetime import datetime, timezone

RACINE = Path(__file__).resolve().parent.parent.parent
IM = RACINE / "Index_Maison"
# Hook étape 5 : auto_reparer.py vit dans ce même dossier scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent))
RAPPORT = IM / "thermo" / "sante_index.json"
ALERTES_DIR = IM / "data" / "alertes"
HISTORIQUE_LOG = ALERTES_DIR / "sante_index.log"
MAINTENANCE_PATH = IM / "strategie" / "MAINTENANCE_PREVUE"
ALERTE_VOCALE = IM / "scripts" / "alerte_vocale.py"

# Âges maximum (minutes) par fichier — au-delà = chaîne figée
SEUILS = {
    "live.json": 120,
    "whales_scan_latest.json": 15,
    "whales_mouvements.jsonl": 30,
    "cpfp_detect.json": 30,
    "mission.json": 30,
    "ada_saison_live.json": 15,
    "ada_gardienne_live.json": 15,
    "cortana_feed.json": 90,  # run horaire (3600 s) : 60 min = marge nulle, Mac en veille = faux positif
    "sante_index.json": 15,
}
# DÉGRADÉ (orange) : fichier entre seuil rouge et 2× le seuil — ralentissement,
# pas encore une panne franche. Évite de crier trop tôt (famille : escalade douce).
DEGRADE_MULT = 2.0

KILL_SWITCHES = [
    IM / "strategie" / "STOP",
    RACINE / "Index_Maison" / "STOP_ALL",
]


def age_min(chemin: Path):
    """Âge du fichier en minutes, ou None s'il n'existe pas."""
    try:
        return (time.time() - chemin.stat().st_mtime) / 60.0
    except Exception:
        return None


def frais(chemin: Path, max_min: int):
    """True si le fichier existe et est plus jeune que max_min."""
    a = age_min(chemin)
    return a is not None and a <= max_min


def degrade(chemin: Path, max_min: int):
    """True si le fichier est entre le seuil et 2× le seuil (DÉGRADÉ, orange)."""
    a = age_min(chemin)
    return a is not None and max_min < a <= max_min * DEGRADE_MULT


def verifier_maintenance() -> bool:
    """True si MAINTENANCE_PREVUE existe avec une date de fin future."""
    if not MAINTENANCE_PATH.exists():
        return False
    try:
        fin = datetime.fromisoformat(MAINTENANCE_PATH.read_text(encoding="utf-8").strip())
        return datetime.now(timezone.utc) < fin
    except Exception:
        return False


def kill_switch_actif() -> bool:
    return any(ks.exists() for ks in KILL_SWITCHES)


def alerte_vocale_active() -> bool:
    """Anti-empilement : vrai si une boucle d'alerte vocale tourne déjà."""
    try:
        out = subprocess.check_output(["pgrep", "-f", "alerte_vocale.py"], text=True,
                                      stderr=subprocess.DEVNULL)
        return bool(out.strip())
    except Exception:
        return False


def arreter_alerte_vocale():
    """Éteint toute alerte vocale SANTÉ en cours (touch STOP_ALERTE + kill).
    Appelé quand l'état redevient OK/DÉGRADÉ : la boucle infinie ne doit PAS
    continuer de crier une fois le problème réparé (leçon 17/08 : l'alerte
    BALEINES de 23:17Z a crié 8h26 après le fix)."""
    try:
        (IM / "STOP_ALERTE").touch()
        (ALERTES_DIR / "STOP_ALERTE").touch()
    except Exception:
        pass
    try:
        subprocess.run(["pkill", "-9", "-f", "alerte_vocale.py"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass


def declencher_alerte(anomalies):
    """Écrit ALERTE_SANTE_[ts].json + lance alerte_vocale.py détaché (anti-empilement)."""
    ts = int(time.time())
    try:
        ALERTES_DIR.mkdir(parents=True, exist_ok=True)
        ecriture_atomique(ALERTES_DIR / f"ALERTE_SANTE_{ts}.json",
                          json.dumps({"ts": datetime.now(timezone.utc).isoformat(),
                                      "type": "SANTE_INDEX", "anomalies": anomalies},
                                     ensure_ascii=False, indent=2))
    except Exception:
        pass
    if alerte_vocale_active():
        return False
    # Nettoyer les STOP_ALERTE laissés par l'extinction précédente (sinon la
    # nouvelle alerte s'éteindrait immédiatement au premier cycle).
    try:
        for f in (IM / "STOP_ALERTE", ALERTES_DIR / "STOP_ALERTE"):
            if f.exists():
                f.unlink()
    except Exception:
        pass
    msg = "Alerte ACE777. Santé des index. " + " ; ".join(anomalies)[:300]
    try:
        subprocess.Popen(["python3", str(ALERTE_VOCALE), "--message", msg, "--id", str(ts)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
        return True
    except Exception:
        return False


def journaliser(rapport):
    """Historique append-only des transitions (OK / DÉGRADÉ / ALERTE)."""
    try:
        ALERTES_DIR.mkdir(parents=True, exist_ok=True)
        ligne = {"ts": datetime.now(timezone.utc).isoformat(),
                 "etat": rapport["etat"],
                 "chaines_ok": rapport["chaines_ok"],
                 "anomalies": rapport["anomalies"],
                 "degradees": rapport.get("degradees", [])}
        with open(HISTORIQUE_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:
        pass


def proc_vivant(attendu: str) -> bool:
    """True si le label launchd/process est vivant (launchctl puis pgrep)."""
    try:
        out = subprocess.check_output(["launchctl", "list"], text=True,
                                      stderr=subprocess.DEVNULL)
        if attendu in out:
            return True
    except Exception:
        pass
    try:
        out = subprocess.check_output(["pgrep", "-fl", attendu], text=True,
                                      stderr=subprocess.DEVNULL)
        return attendu in out
    except Exception:
        return False


def lire_json(chemin: Path):
    try:
        return json.loads(chemin.read_text(encoding="utf-8"))
    except Exception:
        return {}


def maillon(nom: str, ok: bool, detail: str) -> dict:
    return {"nom": nom, "ok": ok, "detail": detail}


def verifier_chaines():
    """Vérifie chaque chaîne et renvoie (liste_chaines, anomalies, degradees)."""
    now = datetime.now(timezone.utc).isoformat(timespec="minutes")
    chaines = []
    anomalies = []
    chaines_degradees = []

    # ============================================================
    # 1. BALEINES — scan → pont → live.json.onchain → Ada + Cortana
    #    (la chaîne qui était coupée : le pont n'avait aucune plist)
    # ============================================================
    maillons = []
    scan = IM / "data" / "whales_scan_latest.json"
    mouv = IM / "data" / "whales_mouvements.jsonl"
    live = IM / "thermo" / "live.json"

    # 1a. Process attendus
    scan_ok = proc_vivant("com.ace777.whales")
    pont_ok = proc_vivant("com.ace777.pont-onchain")
    maillons.append(maillon("scan (launchd whales)", scan_ok,
                           "vivant" if scan_ok else "PAS LANCÉ"))
    maillons.append(maillon("pont (launchd pont-onchain)", pont_ok,
                           "vivant" if pont_ok else "PAS LANCÉ"))

    # 1b. Fichiers frais
    scan_frais = frais(scan, SEUILS["whales_scan_latest.json"])
    scan_degrade = degrade(scan, SEUILS["whales_scan_latest.json"])
    a_scan = age_min(scan)
    if scan_degrade:
        maillons.append(maillon("scan file", True,
                                f"DÉGRADÉ : âge {a_scan:.0f} min (> {SEUILS['whales_scan_latest.json']} min)"))
        chaines_degradees.append("BALEINES")
    else:
        maillons.append(maillon("scan file", scan_frais,
                                f"âge {a_scan:.0f} min" if a_scan is not None else "ABSENT"))
    # whales_mouvements.jsonl est APPEND-ONLY : n'existe que s'il y a eu un événement.
    # Marché calme = fichier absent/ancien = normal (pas une panne).
    a_mouv = age_min(mouv)
    if mouv.exists():
        mouv_frais = frais(mouv, SEUILS["whales_mouvements.jsonl"])
        maillons.append(maillon("mouvements (events)", True,
                                f"dernier événement il y a {a_mouv:.0f} min" if a_mouv is not None else "vide"))
    else:
        maillons.append(maillon("mouvements (events)", True,
                                "aucun événement depuis le début (append-only, normal si marché calme)"))

    # 1c. La donnée est-elle ARRIVÉE chez le consommateur ?
    #     live.json.onchain non vide + frais = le pont a injecté récemment
    live_data = lire_json(live)
    oc = live_data.get("onchain") or {}
    onchain_ok = bool(oc) and frais(live, SEUILS["live.json"])
    maillons.append(maillon("→ live.json.onchain", onchain_ok,
                            "section onchain présente" if oc else "ABSENTE (pont n'injecte pas)"))

    # 1d. Ada l'utilise-t-elle ? (modulateur voilure : facteur présent dans la logique)
    ada = lire_json(IM / "strategie" / "ada_gardienne_live.json")
    ada_frais = frais(IM / "strategie" / "ada_gardienne_live.json", SEUILS["ada_gardienne_live.json"])
    maillons.append(maillon("→ Ada gardienne", ada_frais,
                            f"voilure {ada.get('voilure')} · zone {ada.get('zone')}"
                            if ada_frais else f"âge {age_min(IM / 'strategie' / 'ada_gardienne_live.json'):.0f} min"))

    # 1e. Cortana la lit-elle ? (feed frais)
    feed = IM / "thermo" / "cortana_feed.json"
    feed_frais = frais(feed, SEUILS["cortana_feed.json"])
    maillons.append(maillon("→ Cortana feed", feed_frais,
                            f"âge {age_min(feed):.0f} min" if age_min(feed) is not None else "ABSENT"))

    ok_baleines = all(m["ok"] for m in maillons)
    if not ok_baleines:
        casses = [m["nom"] for m in maillons if not m["ok"]]
        anomalies.append(f"BALEINES coupée : {', '.join(casses)}")
    chaines.append({
        "id": "baleines", "nom": "BALEINES",
        "chemin": "scan → pont → live.json.onchain → Ada + Cortana",
        "ok": ok_baleines, "maillons": maillons,
    })

    # ============================================================
    # 2. HULK — sonde aspiration (paper MEXC) → CSV calibration
    # ============================================================
    maillons = []
    hulk_proc = proc_vivant("paper_diprip.py")
    maillons.append(maillon("process paper_diprip", hulk_proc,
                           "vivant" if hulk_proc else "PAS LANCÉ"))

    csvs = sorted(RACINE.glob("hulk-mexc/runs/ASPIRATION_CALIB_*.csv"))
    csv_recent = csvs[-1] if csvs else None
    if csv_recent is not None:
        a_csv = age_min(csv_recent)
        csv_frais = a_csv is not None and a_csv <= 15
        maillons.append(maillon("CSV aspiration", csv_frais,
                                f"{csv_recent.name} · âge {a_csv:.0f} min" if a_csv is not None else "ABSENT"))
    else:
        csv_frais = False
        maillons.append(maillon("CSV aspiration", False, "aucun CSV trouvé"))
    maillons.append(maillon("corrélation BTC", True, "colonne btc_price (si run actif)"))

    ok_hulk = hulk_proc and csv_frais
    if not ok_hulk:
        anomalies.append("HULK : sonde ou CSV figé (process absent ou CSV > 15 min)")
    chaines.append({
        "id": "hulk", "nom": "HULK",
        "chemin": "sonde paper_diprip → CSV aspiration (murs + prix + BTC)",
        "ok": ok_hulk, "maillons": maillons,
    })

    # ============================================================
    # 3. LIVE — thermo → mission.json → cockpit
    # ============================================================
    maillons = []
    live_frais = frais(live, SEUILS["live.json"])
    maillons.append(maillon("live.json", live_frais,
                            f"âge {age_min(live):.0f} min" if age_min(live) is not None else "ABSENT"))
    mission = IM / "cockpit" / "mission.json"
    mission_frais = frais(mission, SEUILS["mission.json"])
    maillons.append(maillon("mission.json → cockpit", mission_frais,
                            f"âge {age_min(mission):.0f} min" if age_min(mission) is not None else "ABSENT"))
    feed_proc = proc_vivant("com.ace777.hub-cockpit-feed")
    maillons.append(maillon("feed launchd", feed_proc,
                           "vivant" if feed_proc else "PAS LANCÉ"))

    ok_live = live_frais and mission_frais
    if not ok_live:
        anomalies.append("LIVE : thermo ou mission.json figé")
    chaines.append({
        "id": "live", "nom": "LIVE",
        "chemin": "thermo → mission.json → cockpit",
        "ok": ok_live, "maillons": maillons,
    })

    # ============================================================
    # 4. CPFP — détecteur (observation 7j) → pont → Ada
    # ============================================================
    maillons = []
    cpfp_proc = proc_vivant("com.ace777.cpfp")
    maillons.append(maillon("détecteur launchd", cpfp_proc,
                           "vivant" if cpfp_proc else "PAS LANCÉ"))
    cpfp = IM / "data" / "cpfp_detect.json"
    cpfp_frais = frais(cpfp, SEUILS["cpfp_detect.json"])
    maillons.append(maillon("cpfp_detect.json", cpfp_frais,
                            f"âge {age_min(cpfp):.0f} min" if age_min(cpfp) is not None else "ABSENT"))
    # mode observation = normal tant que validation 7j pas finie
    oc_cpfp = oc.get("cpfpSignal") or ""
    cpfp_mode = "observation" if not (oc_cpfp and "EXÉCUTION" in str(oc_cpfp)) else "ACTIF"
    maillons.append(maillon("mode", True, f"{cpfp_mode} (validation 7j en cours)"))

    ok_cpfp = cpfp_proc and cpfp_frais
    if not ok_cpfp:
        anomalies.append("CPFP : détecteur ou fichier figé")
    chaines.append({
        "id": "cpfp", "nom": "CPFP",
        "chemin": "détecteur → pont → Ada (voilure ±10%)",
        "ok": ok_cpfp, "maillons": maillons,
    })

    # ============================================================
    # 5. SÉCURITÉ — veilleuse synapses + kill-switches
    # ============================================================
    maillons = []
    veilleuse_proc = proc_vivant("com.ace777.veilleuse")
    maillons.append(maillon("veilleuse launchd", veilleuse_proc,
                           "vivant" if veilleuse_proc else "PAS LANCÉ"))
    vmd = IM / "thermo" / "VEILLEUSE.md"
    vmd_frais = frais(vmd, 30)
    vmd_ok = "STABLE" in (vmd.read_text(encoding="utf-8") if vmd.exists() else "")
    maillons.append(maillon("rapport VEILLEUSE.md", vmd_frais and vmd_ok,
                            "STABLE" if vmd_ok else "anomalies signalées"))
    stop = IM / "strategie" / "STOP"
    maillons.append(maillon("kill-switches", True,
                           "présents" if (stop.exists() or (RACINE / "Index_Maison" / "STOP_ALL").exists())
                           else "aucun (normal en prod)"))

    ok_secu = veilleuse_proc and vmd_frais
    if not ok_secu:
        anomalies.append("SÉCURITÉ : veilleuse ou rapport figé")
    chaines.append({
        "id": "securite", "nom": "SÉCURITÉ",
        "chemin": "veilleuse synapses (md5 + pannes) + kill-switches",
        "ok": ok_secu, "maillons": maillons,
    })

    # ============================================================
    # 6. SAISON — ada_saison (6 indices) → saison → gardienne
    # ============================================================
    maillons = []
    saison = IM / "strategie" / "ada_saison_live.json"
    saison_frais = frais(saison, SEUILS["ada_saison_live.json"])
    saison_data = lire_json(saison)
    saison_nom = saison_data.get("saison") or saison_data.get("etat") or "?"
    maillons.append(maillon("ada_saison_live.json", saison_frais,
                            f"saison {saison_nom}" if saison_frais else f"âge {age_min(saison):.0f} min"))
    n_indices = len(saison_data.get("indices", {})) if isinstance(saison_data.get("indices"), dict) else 0
    maillons.append(maillon("6 indices calculés", n_indices >= 6,
                            f"{n_indices}/6 présents"))

    ok_saison = saison_frais and n_indices >= 6
    if not ok_saison:
        anomalies.append("SAISON : ada_saison figé ou indices incomplets")
    chaines.append({
        "id": "saison", "nom": "SAISON",
        "chemin": "ada_saison (6 indices) → saison → gardienne",
        "ok": ok_saison, "maillons": maillons,
    })

    # ============================================================
    # 7. VIGIE MARCHÉ — radar temps réel (leçon 3 du 20/08 :
    #    le trou du filet — aucun check ne couvrait la vigie marché)
    # ============================================================
    maillons = []
    # 7a. Process vivant : vigie_live.py (via launchd KeepAlive ou superviseur)
    vigie_proc = proc_vivant("vigie_live.py")
    maillons.append(maillon("process vigie_live", vigie_proc,
                           "vivant" if vigie_proc else "PAS LANCÉ"))
    # 7b. Heartbeat : journal_radar.log frais (la vigie écrit à chaque tick)
    radar = IM / "strategie" / "journal_radar.log"
    radar_frais = frais(radar, 5)  # ≤ 5 min = la vigie écrit en continu
    a_radar = age_min(radar)
    maillons.append(maillon("journal_radar.log", radar_frais,
                            f"âge {a_radar:.0f} min" if a_radar is not None else "ABSENT"))
    # 7c. Relance automatique en place (les plists doivent être chargées — leçon 8 :
    #     un garde-fou écrit ≠ un garde-fou actif)
    sup_proc = proc_vivant("com.ace777.superviseur-process")
    maillons.append(maillon("relance (superviseur-process)", sup_proc,
                           "chargée" if sup_proc else "PAS CHARGÉE"))
    sup_core = proc_vivant("com.ace777.superviseur-core")
    maillons.append(maillon("colonnes (superviseur-core)", sup_core,
                           "chargée" if sup_core else "PAS CHARGÉE"))
    vigie_plist = proc_vivant("com.ace777.vigie-live")
    maillons.append(maillon("vigie-live (launchd)", vigie_plist,
                           "chargée" if vigie_plist else "PAS CHARGÉE"))

    ok_vigie = vigie_proc and radar_frais
    if not ok_vigie:
        anomalies.append("VIGIE MARCHÉ : radar mort ou journal figé (le trou du 19/08)")
    if not (sup_proc and sup_core and vigie_plist):
        anomalies.append("VIGIE MARCHÉ : plist(s) de relance NON CHARGÉE(S) — garde-fou écrit mais inactif (leçon 8)")
    chaines.append({
        "id": "vigie", "nom": "VIGIE MARCHÉ",
        "chemin": "vigie_live.py → journal_radar.log → alertes (relance superviseur-process + superviseur-core + vigie-live)",
        "ok": ok_vigie, "maillons": maillons,
    })

    return chaines, anomalies, now, chaines_degradees


def ecriture_atomique(chemin: Path, contenu: str):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def main():
    # Kill-switch : sortie propre sans rien écrire
    if kill_switch_actif():
        print("[SANTE_INDEX] Kill-switch actif — sortie sans écriture.")
        return 0

    chaines, anomalies, now, chaines_degradees = verifier_chaines()
    n_ok = sum(1 for c in chaines if c["ok"])
    etat = "ALERTE" if anomalies else ("DÉGRADÉ" if chaines_degradees else "OK")
    rapport = {
        "ts": now,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "etat": etat,
        "chaines_ok": f"{n_ok}/{len(chaines)}",
        "anomalies": anomalies,
        "degradees": chaines_degradees,
        "chaines": chaines,
    }
    ecriture_atomique(RAPPORT, json.dumps(rapport, ensure_ascii=False, indent=2))
    # Version JS pour le cockpit (même pattern que live.js / mission.js)
    js = "window.__SANTE__ = " + json.dumps(rapport, ensure_ascii=False) + ";\n"
    ecriture_atomique(IM / "cockpit" / "sante_live.js", js)

    # Historique append-only (chaque run, même OK — pour voir les coupures passées)
    journaliser(rapport)

    # Alerte vocale UNIQUEMENT sur chaîne rouge (pas sur DÉGRADÉ — escalade douce)
    if anomalies and not verifier_maintenance():
        declencher_alerte(anomalies)
    else:
        # Retour au calme : éteindre toute alerte vocale en cours (sinon elle crie
        # en boucle toutes les 30s jusqu'à extinction MANUELLE — leçon 17/08).
        arreter_alerte_vocale()

    # Étape 5 (18/08) : auto-réparation BORNÉE des chaînes de monitoring.
    # DÉFAUT = OBSERVATION (dry-run) : trace ce qui serait réparé, ne relance rien.
    # Bascule actif = marqueur Index_Maison/strategie/AUTO_REPARER_ACTIF (GO humain).
    if anomalies and not verifier_maintenance():
        try:
            import auto_reparer
            res = auto_reparer.reparer(actif=auto_reparer.est_actif())
            if res.get("actions"):
                print(f"[SANTE_INDEX] auto-réparation ({res['mode']}) : "
                      + "; ".join(f"{a['service']}={a['decision']}" for a in res["actions"]))
            elif res.get("gel"):
                print(f"[SANTE_INDEX] auto-réparation gelée : {res['gel']}")
        except Exception as e:
            print(f"[SANTE_INDEX] auto_reparer indisponible : {e}")

    print(f"[SANTE_INDEX] {rapport['updated']} — {rapport['chaines_ok']} chaînes OK · état {etat}"
          + (f" — ALERTE : {', '.join(anomalies)}" if anomalies else ""))
    return 1 if anomalies else 0


if __name__ == "__main__":
    sys.exit(main())
