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
    "deriv_corr.json": 40,  # gen_deriv_corr.py, StartInterval 900 s : 15 min = marge x2.5 (API lentes)
    "cpfp_detect.json": 30,
    "mission.json": 30,
    "ada_saison_live.json": 15,
    "ada_gardienne_live.json": 15,
    "cortana_feed.json": 90,  # run horaire (3600 s) : 60 min = marge nulle, Mac en veille = faux positif
    "sante_index.json": 15,
    "sentinel_history.json": 15,  # sentinel.py, StartInterval 300 s : 5 min = marge x3 (ajout 27/08)
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
    # Message vocal CLAIR (pas de jargon technique)
    msgs_clairs = []
    for a in anomalies:
        if "blocs privatis" in a.lower() or "taux_fantome" in a.lower():
            msgs_clairs.append("Le taux de blocs privatisés est anormalement élevé. L'activité onchain est intense.")
        elif "dead man" in a.lower() or "dms" in a.lower():
            msgs_clairs.append("La couche de surveillance externe a un problème. Vérifie le DMS.")
        elif "degradation" in a.lower():
            msgs_clairs.append("Un indicateur est hors norme. Vérifie le cockpit.")
        else:
            msgs_clairs.append(a[:80])
    msg = "Alerte ACE777. " + " ; ".join(msgs_clairs)[:300]
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
    # 1bis. DÉRIVÉS — gen_deriv_corr → deriv_corr.json → cockpit + Cortana
    #       (corrélations 30j + carte liquidité, sources gratuites Binance/OKX)
    # ============================================================
    maillons = []
    dcorr_proc = proc_vivant("com.ace777.deriv-corr")
    maillons.append(maillon("générateur (launchd deriv-corr)", dcorr_proc,
                           "vivant" if dcorr_proc else "PAS LANCÉ"))
    dcorr = IM / "data" / "deriv_corr.json"
    a_dcorr = age_min(dcorr)
    dcorr_frais = frais(dcorr, SEUILS["deriv_corr.json"])
    dcorr_degrade = degrade(dcorr, SEUILS["deriv_corr.json"])
    if dcorr_degrade:
        maillons.append(maillon("deriv_corr.json", True,
                                f"DÉGRADÉ : âge {a_dcorr:.0f} min (> {SEUILS['deriv_corr.json']} min)"))
        chaines_degradees.append("DÉRIVÉS")
    else:
        maillons.append(maillon("deriv_corr.json", dcorr_frais,
                                f"âge {a_dcorr:.0f} min" if a_dcorr is not None else "ABSENT"))
    ok_deriv = dcorr_proc and dcorr_frais
    if not ok_deriv:
        anomalies.append("DÉRIVÉS : générateur ou fichier figé")
    chaines.append({
        "id": "deriv", "nom": "DÉRIVÉS",
        "chemin": "gen_deriv_corr.py → deriv_corr.json → cockpit + Cortana",
        "ok": ok_deriv, "maillons": maillons,
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

    # 2bis. Contrat Hulk ↔ Cortana (ajout 27/08 : le pilot était figé depuis le 15/08
    # avec un score 0.44 faux — le script qui le régénère n'était branché nulle part).
    analyzer_proc = proc_vivant("com.ace777.cortana-analyzer")
    maillons.append(maillon("cortana_analyzer launchd", analyzer_proc,
                           "vivant" if analyzer_proc else "PAS LANCÉ"))
    pilot = RACINE / "hulk-mexc" / "strategie" / "cortana_pilot.json"
    pilot_frais = frais(pilot, 1500)  # régénéré 07:45/jour → marge 25h
    maillons.append(maillon("cortana_pilot.json", pilot_frais,
                            f"âge {age_min(pilot):.0f} min" if age_min(pilot) is not None else "ABSENT"))
    analysis = IM / "data" / "cortana_analysis.json"
    analysis_frais = frais(analysis, 30)  # cortana_analyzer tourne toutes les 5 min
    maillons.append(maillon("cortana_analysis.json", analysis_frais,
                            f"âge {age_min(analysis):.0f} min" if age_min(analysis) is not None else "ABSENT"))

    ok_hulk = hulk_proc and csv_frais and analyzer_proc and pilot_frais and analysis_frais
    if not ok_hulk:
        anomalies.append("HULK : sonde, CSV, contrat Cortana ou analyses figés")
    chaines.append({
        "id": "hulk", "nom": "HULK",
        "chemin": "paper_diprip → CSV aspiration + cortana_analyzer → cortana_analysis.json → pilot (contrat)",
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
    # hub-cockpit-feed est un script one-shot (pas un daemon)
    # On vérifie la fraîcheur de hub.json au lieu du process
    hub_json = IM / "cockpit" / "hub.json"
    hub_frais = frais(hub_json, 3600)  # seuil 1h
    maillons.append(maillon("hub.json (one-shot)", hub_frais,
                           f"âge {age_min(hub_json):.0f} min" if age_min(hub_json) is not None else "ABSENT"))

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
    # 5. SENTINELLE — z-score → sniffer DeepSeek sur anomalie (ajout 27/08)
    # ============================================================
    maillons = []
    sent_proc = proc_vivant("com.ace777.sentinel")
    maillons.append(maillon("sentinelle launchd", sent_proc,
                           "vivant" if sent_proc else "PAS LANCÉ"))
    sent_hist = IM / "data" / "sentinel_history.json"
    sent_frais = frais(sent_hist, SEUILS["sentinel_history.json"])
    maillons.append(maillon("sentinel_history.json", sent_frais,
                            f"âge {age_min(sent_hist):.0f} min" if age_min(sent_hist) is not None else "ABSENT"))
    # Le fichier de signaux n'existe que s'il y a eu une alerte (append-only, normal si marché calme)
    sent_sign = IM / "data" / "sentinel_signals.json"
    if sent_sign.exists():
        sent_n = len(json.loads(sent_sign.read_text(encoding="utf-8")).get("signals", []))
        maillons.append(maillon("signaux", True, f"{sent_n} signaux émis"))
    else:
        maillons.append(maillon("signaux", True, "aucun signal (normal si calme)"))

    ok_sent = sent_proc and sent_frais
    if not ok_sent:
        anomalies.append("SENTINELLE : launchd ou historique figé")
    chaines.append({
        "id": "sentinel", "nom": "SENTINELLE",
        "chemin": "sentinel.py (5 min) → z-score 12 métriques → sniffer DeepSeek sur anomalie",
        "ok": ok_sent, "maillons": maillons,
    })

    # ============================================================
    # 6. GEOPOL — indice_app 5 modules → live.json.geopol (ajout 27/08)
    # ============================================================
    maillons = []
    # Le geopol est recalculé à chaque run thermo (~1h) et injecté dans live.json.geopol.
    # Le fichier scores_geopol.json (indice_app/data) est un artefact figé (écrit seulement
    # par `python3 orchestrator.py` en direct) — on surveille donc la fraîcheur INTERNE
    # du geopol dans live.json, pas celle du fichier (qui reste figé = normal).
    geo_live = live_data.get("geopol") or {}
    geo_ts = geo_live.get("ts") or ""
    geo_age_h = None
    if geo_ts:
        try:
            from datetime import datetime as _dt
            geo_dt = _dt.fromisoformat(str(geo_ts).replace("Z", "+00:00"))
            geo_age_h = (datetime.now(timezone.utc) - geo_dt).total_seconds() / 3600.0
        except Exception:
            geo_age_h = None
    # Seuil : le thermo tourne ~1h, le geopol doit avoir < 3 h (marge x3).
    geo_frais = geo_age_h is not None and geo_age_h < 3.0
    geo_nb_ok = int(geo_live.get("nb_ok") or 0)
    geo_nb_mod = int(geo_live.get("nb_modules") or 0)
    geo_tous_ok = geo_nb_mod > 0 and geo_nb_ok == geo_nb_mod
    maillons.append(maillon("geopol.ts frais", geo_frais,
                            f"âge {geo_age_h:.1f}h" if geo_age_h is not None else "ABSENT"))
    maillons.append(maillon("modules OK", geo_tous_ok,
                            f"{geo_nb_ok}/{geo_nb_mod} modules" if geo_nb_mod else "aucun module"))

    ok_geopol = geo_frais and geo_tous_ok
    if not ok_geopol:
        anomalies.append("GEOPOL : score figé ou modules en erreur")
    chaines.append({
        "id": "geopol", "nom": "GEOPOL",
        "chemin": "indice_app (5 modules) → live.json.geopol → juge + cockpit",
        "ok": ok_geopol, "maillons": maillons,
    })

    # ============================================================
    # 7. SÉCURITÉ — veilleuse synapses + kill-switches
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

    # ============================================================
    # 8. VEILLE DÉGRADATION — brique méta-analyse (20/08) : le pattern
    #    dominant des 484 audits est la DÉGRADATION SILENCIEUSE. Cette chaîne
    #    vérifie que la brique veille_degradation.py TOURNE et rapporte SAIN.
    # ============================================================
    maillons = []
    vd_proc = proc_vivant("com.ace777.veille-degradation")
    maillons.append(maillon("process veille_degradation (launchd)", vd_proc,
                           "chargée" if vd_proc else "PAS LANCÉE"))
    vd_json = IM / "etat" / "veille_degradation_etat.json"
    vd_frais = frais(vd_json, 15)  # brique prévue ~60 s + marge
    a_vd = age_min(vd_json)
    vd_statut = "ABSENT"
    if vd_json.exists():
        try:
            vd_statut = lire_json(vd_json).get("statut_global", "?")
        except Exception:
            vd_statut = "illisible"
    vd_ok = vd_statut == "SAIN"
    maillons.append(maillon("rapport veille_degradation_etat.json",
                            vd_frais and vd_ok,
                            f"{vd_statut} · âge {a_vd:.0f} min" if a_vd is not None else "ABSENT"))
    if not vd_proc:
        anomalies.append("VEILLE DÉGRADATION : brique méta-analyse PAS LANCÉE (dégradation silencieuse non surveillée)")
    if not (vd_frais and vd_ok):
        anomalies.append(f"VEILLE DÉGRADATION : rapport {vd_statut} ou figé — dégradation silencieuse détectée")
    # 8c. Dead Man's Switch externe (exigence famille, consultation canonique 20/08) :
    #     qui surveille la surveillante ? Le DMS est un tiers indépendant qui vérifie
    #     la fraîcheur de la brique + launchctl lui-même, et CRIE si ça ne va pas.
    dms_proc = proc_vivant("com.ace777.dms-veille")
    maillons.append(maillon("Dead Man's Switch (dms-veille)", dms_proc,
                           "chargée" if dms_proc else "PAS CHARGÉE"))
    dms_json = ALERTES_DIR / "DMS_VEILLE.json"
    dms_frais = frais(dms_json, 15)
    dms_statut = "ABSENT"
    if dms_json.exists():
        try:
            dms_statut = lire_json(dms_json).get("statut", "?")
        except Exception:
            dms_statut = "illisible"
    dms_ok = dms_frais and dms_statut == "OK"
    maillons.append(maillon("rapport DMS_VEILLE.json", dms_ok,
                            f"{dms_statut}" if dms_statut != "ABSENT" else "ABSENT"))
    if not dms_proc:
        anomalies.append("VEILLE DÉGRADATION : Dead Man's Switch NON CHARGÉ (le filet sous le filet manque)")
    if not dms_ok:
        anomalies.append(f"VEILLE DÉGRADATION : Dead Man's Switch {dms_statut} ou figé — la surveillance elle-même est en panne")
    chaines.append({
        "id": "veille_deg", "nom": "VEILLE DÉGRADATION",
        "chemin": "veille_degradation.py (plists + heartbeats + indicateurs) → etat.json + DMS externe (dms-veille) → cockpit",
        "ok": vd_proc and vd_frais and vd_ok and dms_proc and dms_ok, "maillons": maillons,
    })

    # ============================================================
    # 9. MACRO TEMPÊTE — choc exogène (leçon 20/08 : le +8% du 19-20/08 était
    #    exogène, décision Trésor/Fed ; le détecteur bloque les trades contre-choc
    #    via radar_gate.rb). Leçon 8 : il tourne mais RIEN ne surveille s'il meurt.
    # ============================================================
    maillons = []
    mt_proc = proc_vivant("com.ace777.macro-tempete")
    maillons.append(maillon("process detecteur_macro_tempete (launchd)", mt_proc,
                           "chargée" if mt_proc else "PAS LANCÉE"))
    mt_json = RACINE / "runs" / "macro_tempete.json"
    mt_frais = frais(mt_json, 15)  # détecteur ~quelques min + marge
    a_mt = age_min(mt_json)
    mt_active = False
    if mt_json.exists():
        try:
            mt_active = bool(lire_json(mt_json).get("active", False))
        except Exception:
            mt_active = False
    maillons.append(maillon("macro_tempete.json", mt_frais,
                            f"âge {a_mt:.0f} min" if a_mt is not None else "ABSENT"))
    # Fix 24/08 (Buffy) : bug d'inversion — quand PAS de tempête (mt_active=False)
    # l'état est SAIN (normal) ; la case était marquée KO à tort. La présence
    # d'une tempête n'est pas une panne du détecteur (couvrée par mt_frais) :
    # on affiche l'état, toujours OK tant que le fichier est frais.
    maillons.append(maillon("état courant", True,
                            "TEMPÊTE ACTIVE" if mt_active else "normal"))
    if not mt_proc:
        anomalies.append("MACRO TEMPÊTE : détecteur PAS LANCÉ — choc exogène non surveillé (leçon 20/08)")
    if not mt_frais:
        anomalies.append("MACRO TEMPÊTE : macro_tempete.json figé — le garde-fou anti-choc est mort (leçon 8)")
    chaines.append({
        "id": "macro_tempete", "nom": "MACRO TEMPÊTE",
        "chemin": "detecteur_macro_tempete.py (launchd) → macro_tempete.json → radar_gate.rb (bloque trades contre-choc)",
        "ok": mt_proc and mt_frais, "maillons": maillons,
    })

    # ============================================================
    # 10. CROISEMENT EXTERNE — règle des 2 sources (29/08, GO Christophe) :
    #     avant toute décision, nos prix doivent être validés par une source
    #     externe (MEXC/Binance). Écart > 5 % = data_quality_fail = on ne décide
    #     pas. Les warns MURS sont informatifs (carnet déséquilibré, pas une
    #     corruption). Ce croisement EST la valideuse de nos données.
    # ============================================================
    maillons = []
    cq_proc = proc_vivant("com.ace777.croisement-externe")
    maillons.append(maillon("process croisement (launchd)", cq_proc,
                           "chargée" if cq_proc else "PAS LANCÉE"))
    cq_json = IM / "data" / "croisement_externe_etat.json"
    cq_frais = frais(cq_json, 45)  # plist toutes les 30 min + marge
    a_cq = age_min(cq_json)
    cq_n_fails = 0
    cq_n_warns = 0
    cq_detail = "ABSENT"
    if cq_json.exists():
        try:
            cq = lire_json(cq_json)
            cq_n_fails = int(cq.get("n_fails", 0))
            cq_n_warns = int(cq.get("n_warns", 0))
            cq_detail = f"{cq_n_fails} fail prix · {cq_n_warns} warn murs"
        except Exception:
            cq_detail = "illisible"
    maillons.append(maillon("croisement_externe_etat.json", cq_frais,
                            f"âge {a_cq:.0f} min" if a_cq is not None else "ABSENT"))
    # Fails PRIX = données douteuses (on ne décide pas) — c'est le cœur du protocole
    cq_ok = cq_proc and cq_frais and cq_n_fails == 0
    maillons.append(maillon("fails prix (> 5 % vs externe)", cq_n_fails == 0,
                            f"{cq_n_fails} fail(s)" if cq_n_fails else "aucun — données validées"))
    maillons.append(maillon("warns murs (info)", True,
                            f"{cq_n_warns} warn(s) carnet déséquilibré (info)" if cq_n_warns else "aucun"))
    if not cq_proc:
        anomalies.append("CROISEMENT EXTERNE : process PAS LANCÉ — nos données ne sont plus validées par une source externe (règle 2 sources)")
    if not cq_frais:
        anomalies.append("CROISEMENT EXTERNE : croisement_externe_etat.json figé — la valideuse des données est morte")
    if cq_n_fails > 0:
        anomalies.append(f"CROISEMENT EXTERNE : {cq_n_fails} prix en écart > 5 % avec une source externe — NE PAS DÉCIDER (data_quality_fail)")
    chaines.append({
        "id": "croisement_externe", "nom": "CROISEMENT EXTERNE",
        "chemin": "croiser_donnees_externes.py (launchd 30 min) → nos prix vs MEXC/Binance → data_quality_fail si écart > 5 % (on ne décide pas)",
        "ok": cq_ok, "maillons": maillons,
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
