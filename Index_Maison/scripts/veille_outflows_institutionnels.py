#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
veille_outflows_institutionnels.py — SONDE DES 3 SIGNAUX INSTITUTIONNELS (30/08/2026)
=====================================================================================
GO Christophe : « implémente trois signaux » — après consultation famille du 30/08
(consensus 6/6 : sanctuarisation des actifs AVANT rupture de système, piège de
rentrée en septembre, absorption institutionnelle en bas).

Les 3 signaux (seuils de la famille, issus de SYNTHESE_FAMILLE_PATTERN_INSTITUTIONS) :

  SIGNAL 1 — SORTIES CEX (validation de constitution de réserve opaque)
      Seuil : sorties cumulées > 10 000 BTC/jour × 5 jours consécutifs, prix stable.
      Lecture : le retail ne bouge pas 10k/j ; = réserve institutionnelle/souveraine.
      Action : renforcer la thèse d'absorption → préparer les échelles.

  SIGNAL 2 — BLOCS PRIVATISÉS (passage préparation → mouvement)
      Seuil : taux_fantome > 12% soutenus 48h (vs ~7% de base).
      Lecture : phase de préparation (août) → phase de mouvement (sept.).
      Action : activer DCA agressif sur la zone creux.

  SIGNAL 3 — DÉSÉQUILIBRE POUSSIÈRE (storage fini → choc imminent)
      Seuil : ratio poussière d'un côté > 80% + réouverture des carnets institutionnels.
      Lecture : la phase de storage est terminée → choc de prix dans les 48h.
      Action : s'engager UNIQUEMENT si le prix a validé la direction.

Ce script est une OBSERVATION CROISÉE : il LIT les fichiers déjà produits par les
sondes existantes (detecter_cpfp.py, detecter_bloc_privatise.py, surveiller_whales.py),
ne duplique AUCUNE API, et écrit :
  - Index_Maison/data/veille_institutionnelle_etat.json  (état courant, lu par cockpit/Cortana)
  - Index_Maison/data/veille_institutionnelle_hist.jsonl (historique append-only)
  - alertes dans data/alertes/AlERTE_INSTI_*.json + alerte vocale (si seuil soutenu)

Doctrine : stdlib uniquement, écriture atomique, kill-switch, idempotent, ne touche
à aucune autre sonde. NE DÉCIDE RIEN — signale seulement.
"""
import os
import json
import time
import tempfile
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ============================================================
# CHEMINS (convention ACE777 — chemins ABSOLUS, leçon famille n°4)
# ============================================================
REPO = Path.home() / "ace777-test-day1"
DATA_DIR = REPO / "Index_Maison" / "data"
ALERTES_DIR = DATA_DIR / "alertes"
STRATEGIE_DIR = REPO / "Index_Maison" / "strategie"
ETAT = DATA_DIR / "veille_institutionnelle_etat.json"
HIST = DATA_DIR / "veille_institutionnelle_hist.jsonl"
STOP_LOCAL = STRATEGIE_DIR / "STOP"
STOP_GLOBAL = REPO / "Index_Maison" / "STOP_ALL"
ALERTE_VOCALE = REPO / "Index_Maison" / "scripts" / "alerte_vocale.py"

# Fichiers sources (déjà produits par d'autres sondes)
CPFP_DETECT = DATA_DIR / "cpfp_detect.json"
CPFP_OBS = DATA_DIR / "cpfp_observations.jsonl"
BLOC_PRIV = DATA_DIR / "bloc_privatise.json"
BLOC_PRIV_HIST = DATA_DIR / "bloc_privatise_hist.jsonl"
WHALES_SCAN = DATA_DIR / "whales_scan_latest.json"
WHALES_MOUV = DATA_DIR / "whales_mouvements.jsonl"
WHALES_CFG = DATA_DIR / "whales.json"  # registre d'adresses → étiquettes (pour qualifier cibles)

# ============================================================
# SEUILS FAMILLE (SYNTHESE_FAMILLE_PATTERN_INSTITUTIONS_20260830)
# ============================================================
S1_BTC_JOUR = 10_000.0      # Signal 1 : > 10k BTC sortis/jour
S1_JOURS_CONSECUTIFS = 5    # ... pendant 5 jours consécutifs
S1_PRIX_STABLE_PCT = 2.0    # prix stable = variation < 2%/24h
S2_TAUX_SEUIL = 12.0        # Signal 2 : bloc privatisé > 12%
S2_HEURES_SOUTENU = 48      # ... soutenu 48h
S3_DESEQUILIBRE = 80.0      # Signal 3 : > 80% de poussière d'un côté

CONFIRMATION_S1_RUNS = 5    # runs consécutifs pour signal 1 (le plus lourd)
MAX_AGE_SOURCE_MIN = 90     # une source figée = on ne décide pas (éteint le signal)


def verifier_kill_switch():
    if STOP_LOCAL.exists() or STOP_GLOBAL.exists():
        print("[KILL] Kill switch activé. Arrêt propre.", file=os.sys.stderr)
        raise SystemExit(0)


def ecriture_atomique(chemin: Path, donnees):
    verifier_kill_switch()
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def append_jsonl(chemin: Path, donnees):
    verifier_kill_switch()
    chemin.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(donnees, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[AVERTISSEMENT] append {chemin}: {e}", file=os.sys.stderr)


def charger_json(chemin: Path, defaut):
    if not chemin.exists():
        return defaut
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defaut


def age_min(chemin: Path):
    if not chemin.exists():
        return None
    try:
        return (time.time() - chemin.stat().st_mtime) / 60.0
    except Exception:
        return None


def lire_jsonl(chemin: Path, heures=72):
    """Retourne les événements récents d'un jsonl (append-only)."""
    lignes = []
    if not chemin.exists():
        return lignes
    limite = datetime.now(timezone.utc) - timedelta(hours=heures)
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    evt = json.loads(line)
                    ts = evt.get("ts") or evt.get("utc") or ""
                    if ts:
                        dt = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
                        if dt >= limite:
                            lignes.append(evt)
                except Exception:
                    continue
    except Exception:
        pass
    return lignes


# ============================================================
# SIGNAL 1 — SORTIES CEX (outflows depuis whales_mouvements.jsonl)
# ============================================================
def charger_labels_exchange():
    """whales.json → {adresse: label} pour qualifier les cibles (comme le pont)."""
    d = charger_json(WHALES_CFG, {"portefeuilles": []})
    labels = {}
    for p in d.get("portefeuilles", []):
        addr = p.get("address")
        if addr:
            labels[addr] = p.get("label", "inconnu")
    return labels


def est_outflow(evt, labels):
    """Logique MAISON (pont_onchain.qualifier_direction) : outflow = mouvement
    qui PART d'un exchange étiqueté et NE VA PAS vers un exchange étiqueté.
    Cold→cold interne (ex: Bitbank cold→cold) = réorganisation interne, PAS une
    sortie CEX (ne compte pas). Inconnu→exchange = inflow, pas une sortie."""
    sources_label = evt.get("sources_label") or []
    cibles = evt.get("cibles") or []
    a_des_exchange = any("exchange" in str(s).lower() for s in sources_label)
    # cible étiquetée comme exchange ? (via le registre whales.json)
    vers_exchange = any(
        str(labels.get(c.get("adresse")) or "").lower().count("exchange") > 0
        for c in cibles
    )
    if a_des_exchange and not vers_exchange:
        return True
    return False  # inflow ou neutral — pas une sortie CEX nette


def signal_1_sorties_cex():
    """Somme les OUTFLOWS (>0) par jour UTC sur 7 jours, compte les jours
    consécutifs > S1_BTC_JOUR, exige _j CONSECUTIFS. Ne compte QUE les vraies
    sorties d'exchange (source label contient 'exchange', pas de cible exchange)."""
    mouvs = lire_jsonl(WHALES_MOUV, heures=168)  # 7 jours
    labels = charger_labels_exchange()
    par_jour = {}
    for m in mouvs:
        try:
            btc = float(m.get("btc", 0.0) or 0.0)
        except (TypeError, ValueError):
            continue
        if btc <= 0:
            continue
        jour = str(m.get("ts") or m.get("utc") or "")[:10]
        if not jour or jour.count("-") != 2:
            continue
        if est_outflow(m, labels):
            par_jour[jour] = par_jour.get(jour, 0.0) + btc

    # Jours consécutifs avec > seuil (outflow net cumulé par jour)
    jours_actifs = sorted(jour for jour, tot in par_jour.items() if tot > S1_BTC_JOUR)
    meilleur = 0
    n = 0
    for i, jour in enumerate(jours_actifs):
        if i == 0:
            n = 1
        else:
            d0 = datetime.fromisoformat(jours_actifs[i - 1])
            d1 = datetime.fromisoformat(jour)
            n = n + 1 if (d1 - d0).days == 1 else 1
        meilleur = max(meilleur, n)

    total_7j = sum(par_jour.values())
    declenche = meilleur >= S1_JOURS_CONSECUTIFS
    lignes = ", ".join(f"{j}={v:.0f}" for j, v in sorted(par_jour.items())) or "aucune sortie CEX nette"
    detail = (f"{meilleur}j consécutifs > {S1_BTC_JOUR:.0f} BTC/j (seuil {S1_JOURS_CONSECUTIFS}j) · "
              f"OUTFLOW CEX net 7j {total_7j:.0f} BTC · [{lignes}]")
    return {"declenche": declenche, "n_jours": meilleur,
            "total_7j": round(total_7j, 0), "detail": detail}


# ============================================================
# SIGNAL 2 — BLOCS PRIVATISÉS (taux fantôme)
# ============================================================
def signal_2_blocs_privatises():
    """taux_fantome soutenu > 12% pendant 48h.
    Source : bloc_privatise_hist.jsonl (produit par detecter_bloc_privatise.py)."""
    hist = lire_jsonl(BLOC_PRIV_HIST, heures=72)
    au_dessus = [h for h in hist
                 if isinstance(h.get("taux_fantome"), (int, float))
                 and h["taux_fantome"] >= S2_TAUX_SEUIL]
    n_total = len(hist)
    n_au_dessus = len(au_dessus)
    ratio = (n_au_dessus / n_total) if n_total else 0.0
    # Proxy 48h : proportion élevée de blocs au-dessus du seuil sur la fenêtre
    declenche = n_total >= 4 and ratio >= 0.6
    dernier_taux = None
    cur = charger_json(BLOC_PRIV, {})
    try:
        t = cur.get("taux_fantome")
        if isinstance(t, (int, float)):
            dernier_taux = round(t, 1)
    except Exception:
        pass
    detail = (f"dernier taux {dernier_taux}% (seuil {S2_TAUX_SEUIL}%) · "
              f"{n_au_dessus}/{n_total} blocs > seuil sur 72h (proxi 48h)")
    return {"declenche": declenche, "dernier_taux": dernier_taux,
            "n_au_dessus": n_au_dessus, "n_total": n_total, "detail": detail}


# ============================================================
# SIGNAL 3 — DÉSÉQUILIBRE POUSSIÈRE
# ============================================================
def signal_3_desequilibre_poussiere():
    """Ratio poussière d'un côté > 80%.
    Source : cpfp_detect.json / cpfp_observations.jsonl (produit par detecter_cpfp.py)."""
    cur = charger_json(CPFP_DETECT, {})
    cartes = cur.get("cartes", {}) or {}
    poussiere = cartes.get("carte3_poussiere", {}) or {}
    score_dust = float(poussiere.get("score", 0.0) or 0.0)  # échelle 0-50
    # Proxy du déséquilibre : score 40/50 (ratio 80% dans l'échantillon de la sonde)
    declenche = score_dust >= 40.0
    obs = lire_jsonl(CPFP_OBS, heures=48)
    moyenne_dust = sum(int(o.get("dust_vus", 0) or 0) for o in obs) / len(obs) if obs else 0.0
    detail = (f"score poussière {score_dust:.0f}/50 (proxy ≥40 = ratio côté ≥80%) · "
              f"moyenne dust_vus/run 48h {moyenne_dust:.1f}")
    return {"declenche": declenche, "score_poussiere": round(score_dust, 1),
            "moyenne_dust": round(moyenne_dust, 1), "detail": detail}


# ============================================================
# FRAÎCHEUR DES SOURCES — on ne décide pas sur une source figée
# ============================================================
def sources_fraiches():
    resultats = {}
    for nom, fichier, max_min in (
        ("cpfp", CPFP_DETECT, MAX_AGE_SOURCE_MIN),
        ("blocs_privatises", BLOC_PRIV, MAX_AGE_SOURCE_MIN),
        ("whales_mouvements", WHALES_MOUV, MAX_AGE_SOURCE_MIN),
    ):
        a = age_min(fichier)
        resultats[nom] = {
            "age_min": round(a, 1) if a is not None else None,
            "frais": a is not None and a <= max_min,
        }
    return resultats


# ============================================================
# ALERTE VOCALE (si un signal soutenu passe)
# ============================================================
def declarer_alerte(ts_int, signaux_declenches):
    """Écrit l'alerte + déclenche l'alerte vocale (anti-empilement)."""
    try:
        ALERTES_DIR.mkdir(parents=True, exist_ok=True)
        ecriture_atomique(
            ALERTES_DIR / f"ALERTE_INSTI_{ts_int}.json",
            {"ts": datetime.now(timezone.utc).isoformat(),
             "type": "INSTITUTIONS_3_SIGNAUX",
             "signaux": signaux_declenches})
    except Exception:
        pass
    # Anti-empilement : ne pas relancer une voix si une boucle tourne déjà
    try:
        out = subprocess.check_output(["pgrep", "-f", "alerte_vocale.py"],
                                      text=True, stderr=subprocess.DEVNULL)
        if out.strip():
            return
    except Exception:
        pass
    noms = {1: "Sorties de réserves", 2: "Blocs privatisés", 3: "Déséquilibre poussière"}
    libelles = [noms.get(int(s), str(s)) for s in signaux_declenches]
    msg = "Alerte ACE777. Signaux institutionnels. " + ", ".join(libelles)[:260]
    try:
        subprocess.Popen(["python3", str(ALERTE_VOCALE), "--message", msg,
                          "--id", str(ts_int)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
    except Exception:
        pass


# ============================================================
# MAIN
# ============================================================
def main():
    verifier_kill_switch()
    maintenant = datetime.now(timezone.utc)

    fraicheur = sources_fraiches()
    s1 = signal_1_sorties_cex()
    s2 = signal_2_blocs_privatises()
    s3 = signal_3_desequilibre_poussiere()

    # Un signal ne vaut que si SA source est fraîche
    actifs = []
    if s1["declenche"] and fraicheur["whales_mouvements"]["frais"]:
        actifs.append(1)
    if s2["declenche"] and fraicheur["blocs_privatises"]["frais"]:
        actifs.append(2)
    if s3["declenche"] and fraicheur["cpfp"]["frais"]:
        actifs.append(3)

    etat = {
        "ts": maintenant.isoformat(),
        "updated": maintenant.strftime("%Y-%m-%dT%H:%MZ"),
        "signaux_actifs": actifs,
        "verdict": (
            "ALERTE" if actifs else ("SURVEILLANCE" if (s1["n_jours"] or 0) >= 2
                                     or (s2["n_total"] or 0) > 0 else "CALME")),
        "signaux": {
            "1_sorties_cex": {**s1, "declenche_effectif": 1 in actifs},
            "2_blocs_privatises": {**s2, "declenche_effectif": 2 in actifs},
            "3_poussiere": {**s3, "declenche_effectif": 3 in actifs},
        },
        "fraicheur_sources": fraicheur,
    }
    ecriture_atomique(ETAT, etat)
    append_jsonl(HIST, {k: etat[k] for k in ("ts", "signaux_actifs", "verdict", "signaux")})

    # Alerte vocale UNIQUEMENT si un signal passe (pas en mode veille)
    if actifs:
        declarer_alerte(int(time.time()), actifs)

    # Écriture cockpit (pattern mission.js / live.js)
    js = "window.__VEILLE_INSTI__ = " + json.dumps(etat, ensure_ascii=False) + ";\n"
    try:
        ecriture_atomique(REPO / "Index_Maison" / "cockpit" / "veille_institutionnelle.js", js)
    except Exception:
        pass

    print(f"[SONDE 3 SIGNAUX] {etat['updated']} — actifs={actifs} verdict={etat['verdict']}")
    print(f"  S1 sorties: {s1['detail']}")
    print(f"  S2 blocs:   {s2['detail']}")
    print(f"  S3 poussière: {s3['detail']}")
    return 0


if __name__ == "__main__":
    main()