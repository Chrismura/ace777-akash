#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle (ACE777) : DÉTECTEUR CPFP v2 — la « pépite » UTXO/CPFP de Christophe.
Détecte les mouvements camouflés de baleines que les seuils publics (≥1000 BTC)
ne voient pas : arbre de poussière à frais quasi nuls + transaction enfant CPFP
à frais astronomiques qui force le mineur à valider tout l'arbre.

3 cartes :
  1. Z-SCORE ADAPTATIF — la ligne bouge chaque jour (les baleines ne peuvent pas
     s'adapter à un seuil qu'elles ne connaissent pas) : déclenche à ≥3σ de la
     moyenne mobile 7j, avec plancher absolu ≥500 BTC.
  2. SIGNATURE CPFP PAR FRAIS — inaltérable (le frais astronomique EST le
     mécanisme) : enfant ≥20× médiane + parent ≤1 sat/vB + total arbre ≥100 BTC.
     Pré-filtre API IMPÉRATIF : on ne creuse QUE si frais > 20× médiane
     (protection du free tier mempool.space) + backoff + cache.
  3. ACCUMULATION POUSSIÈRE — anticipation : les baleines préparent leur coup
     pendant des heures/jours. Transactions à frais quasi nuls (<2 sat/vB).

MODE = "observation" PAR DÉFAUT (SILENCIEUX) : on loggue et on calibre les seuils
sur le réel, AUCUNE alerte tant que Christophe n'a pas validé le bilan 7 jours.
Bascule en mode actif : python3 detecter_cpfp.py --actif

Doctrine : stdlib uniquement, écriture atomique, kill-switch, idempotent,
100% gratuit (mempool.space sans clé). NE TOUCHE PAS à surveiller_whales.py.
"""

import os
import sys
import json
import math
import time
import argparse
import tempfile
import urllib.request
from datetime import datetime, timezone, timedelta

# ============================================================
# CHEMINS (convention ACE777 — repo racine ~/ace777-test-day1)
# ============================================================
HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, "ace777-test-day1")
INDEX_MAISON = os.path.join(REPO, "Index_Maison")
DATA_DIR = os.path.join(INDEX_MAISON, "data")

STOP_LOCAL = os.path.join(INDEX_MAISON, "strategie", "STOP")
STOP_GLOBAL = os.path.join(INDEX_MAISON, "STOP_ALL")

CPFP_OUT = os.path.join(DATA_DIR, "cpfp_detect.json")
CPFP_MODE_FILE = os.path.join(DATA_DIR, "cpfp_mode.json")
CPFP_OBS = os.path.join(DATA_DIR, "cpfp_observations.jsonl")
CPFP_BILAN = os.path.join(DATA_DIR, "CPFP_BILAN_7JOURS.md")
CPFP_FRAIS_HIST = os.path.join(DATA_DIR, "cpfp_frais_hist.jsonl")

WHALES_SCAN = os.path.join(DATA_DIR, "whales_scan_latest.json")
WHALES_MOUVEMENTS = os.path.join(DATA_DIR, "whales_mouvements.jsonl")

MEMPOOL_API = "https://mempool.space/api"
USER_AGENT = "ACE777-CPFP/1.0"

# ============================================================
# SEUILS v1 (arbitrés famille + supervision — calibrés sur le réel en observation)
# ============================================================
Z_SEUIL = 3.0            # carte 1 : z-score ≥ 3σ
PLANCHER_BTC = 500.0     # carte 1 : plancher absolu (filet si moyenne trop basse)
FRAIS_RATIO = 20.0       # carte 2 : enfant ≥ 20× la médiane
PARENT_MAX_SAT_VB = 1.0  # carte 2 : parent ≤ 1 sat/vB
ARBRE_MIN_BTC = 100.0    # carte 2 : total de l'arbre ≥ 100 BTC
DUST_MAX_SAT_VB = 2.0    # carte 3 : poussière < 2 sat/vB
BACKOFF_API_MIN = 10.0   # backoff : pas plus d'1 creusage par 10 min (free tier)
CONFIRMATION_MIN = 2     # 2 runs successifs avant de considérer le signal (D6)


def verifier_kill_switch():
    if os.path.exists(STOP_LOCAL) or os.path.exists(STOP_GLOBAL):
        print("[KILL] Kill switch activé. Arrêt propre.", file=sys.stderr)
        sys.exit(0)


def ecriture_atomique(chemin, donnees):
    verifier_kill_switch()
    d = os.path.dirname(chemin)
    if d:
        os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d or ".", suffix=".tmp")
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


def append_jsonl(chemin, donnees):
    verifier_kill_switch()
    d = os.path.dirname(chemin)
    if d:
        os.makedirs(d, exist_ok=True)
    try:
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(donnees, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[AVERTISSEMENT] append {chemin}: {e}", file=sys.stderr)


def charger_json(chemin, defaut):
    if not os.path.exists(chemin):
        return defaut
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defaut


def charger_jsonl(chemin, jours=7):
    lignes = []
    if not os.path.exists(chemin):
        return lignes
    limite = datetime.now(timezone.utc) - timedelta(days=jours)
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    evt = json.loads(line)
                    ts = str(evt.get("ts", ""))
                    if ts:
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                        if dt >= limite:
                            lignes.append(evt)
                except Exception:
                    continue
    except Exception:
        pass
    return lignes


def requete_mempool(endpoint):
    """Un appel API, avec timeout court. Retourne dict/list ou None (jamais de crash)."""
    url = MEMPOOL_API + endpoint
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
    except Exception:
        pass
    return None


def parse_ts(ts_str):
    try:
        return datetime.fromisoformat(str(ts_str).replace("Z", "+00:00"))
    except Exception:
        return None


# ============================================================
# CARTE 1 — Z-SCORE ADAPTATIF (100% local, zéro appel API)
# ============================================================
def analyser_zscore():
    """Re-analyse les gros blocs/fragmentations EXISTANTS (scan + mouvements 7j)
    avec un seuil statistique : ≥3σ de la moyenne mobile 7j, plancher ≥500 BTC.

    Correction supervision (trouvée en test) : la moyenne mobile 7j NE DOIT PAS
    inclure l'observation courante, sinon le z-score compare le signal à une
    distribution qui le contient déjà (signal dilué, jamais détecté). On calcule
    la normale sur les jours PRÉCÉDENTS, puis on mesure l'anomalie d'aujourd'hui
    contre cette normale."""
    maintenant = datetime.now(timezone.utc)
    debut_aujourdhui = maintenant.replace(hour=0, minute=0, second=0, microsecond=0)

    montants_avant = []   # normale : jours précédents
    montants_auj = []     # anomalie : mouvement du jour courant

    scan = charger_json(WHALES_SCAN, {"gros_blocs": [], "fragmentations": []})
    ts_scan = parse_ts(scan.get("ts", "")) or maintenant
    for g in scan.get("gros_blocs", []) or []:
        (montants_auj if ts_scan >= debut_aujourdhui else montants_avant).append(
            float(g.get("btc", 0.0) or 0.0))
    for f in scan.get("fragmentations", []) or []:
        (montants_auj if ts_scan >= debut_aujourdhui else montants_avant).append(
            float(f.get("btc", 0.0) or 0.0))

    for evt in charger_jsonl(WHALES_MOUVEMENTS, jours=7):
        ts = parse_ts(evt.get("ts", ""))
        if not ts:
            continue
        cible = montants_auj if ts >= debut_aujourdhui else montants_avant
        cible.append(float(evt.get("btc", 0.0) or 0.0))

    declenche, score, detail = False, 0.0, "pas assez de données"
    moyenne, sigma = 0.0, 0.0
    # Normale = jours précédents (au moins 3 points) ; anomalie = mouvement du jour
    if len(montants_avant) >= 3 and montants_auj:
        n = len(montants_avant)
        moyenne = sum(montants_avant) / n
        variance = sum((v - moyenne) ** 2 for v in montants_avant) / n
        sigma = math.sqrt(variance)
        max_auj = max(montants_auj)
        z = (max_auj - moyenne) / sigma if sigma > 0 else 0.0
        declenche = z >= Z_SEUIL and max_auj >= PLANCHER_BTC
        score = round(min(100.0, (z / 5.0) * 100.0), 2)
        detail = (f"z={z:.2f} (seuil {Z_SEUIL}) | max aujourd'hui {max_auj:.0f} BTC "
                  f"(plancher {PLANCHER_BTC:.0f}) | normale 7j {moyenne:.1f} ± {sigma:.1f}")
    return {"declenche": declenche, "score": score, "detail": detail}, moyenne, sigma


# ============================================================
# CARTE 2 — SIGNATURE CPFP PAR FRAIS (inaltérable, pré-filtre + backoff)
# ============================================================
def mediane_frais_7j():
    """Médiane historique des frais recommandés (7j) — pour le ratio 20×."""
    valeurs = []
    for evt in charger_jsonl(CPFP_FRAIS_HIST, jours=7):
        try:
            valeurs.append(float(evt.get("mediane", 0.0)))
        except Exception:
            continue
    if not valeurs:
        return None
    valeurs.sort()
    n = len(valeurs)
    if n % 2 == 1:
        return valeurs[n // 2]
    return (valeurs[n // 2 - 1] + valeurs[n // 2]) / 2.0


def analyser_cpfp():
    """Pré-filtre : on creuse si les frais actuels > 1.5× la médiane 7j.

    CORRECTION 21/08 (Buffy, GO Christophe — pépite mise de côté famille) :
    l'ancien seuil (>20× médiane) ne passait JAMAIS en marché calme (frais
    réels 1-8 sat/vB vs seuil 20 sat/vB) → le détecteur tournait à l'aveugle
    (817 runs, zéro détection, 6 jours).
    Nouveau comportement : le pré-filtre ne sert plus à décider la détection
    (ça, c'est le ratio enfant ≥20× dans la boucle) mais juste à éviter de
    spammer l'API free tier — le backoff 10 min + cache font déjà ce travail.
    On creuse dès qu'il y a la MOINDRE anomalie (1.5×) pour voir les tx ;
    la signature CPFP (enfant ≥20× médiane + parent ≤1 sat/vB + arbre ≥100 BTC)
    reste strict et inaltérable."""
    # 1 appel léger systématique : frais recommandés
    fees = requete_mempool("/v1/fees/recommended")
    if not fees:
        return {"declenche": False, "score": 0.0,
                "detail": "API mempool injoignable (repli propre)"}, None

    mediane_actuelle = float(fees.get("halfHourFee", 0.0) or 0.0)
    minimum_fee = float(fees.get("minimumFee", 0.0) or 0.0)
    append_jsonl(CPFP_FRAIS_HIST, {"ts": datetime.now(timezone.utc).isoformat(),
                                   "mediane": mediane_actuelle})

    hist = mediane_frais_7j()
    # Seuil de creusage : 1.5× la médiane (CORRECTION 21/08 — voir docstring)
    CREUSAGE_RATIO = 1.5
    if hist and hist > 0 and mediane_actuelle <= CREUSAGE_RATIO * hist:
        return {"declenche": False, "score": 0.0,
                "detail": (f"pré-filtre : frais {mediane_actuelle:.0f} sat/vB ≤ "
                           f"{CREUSAGE_RATIO:.1f}× médiane 7j ({hist:.0f}) — pas de creusage")}, mediane_actuelle

    # Backoff : pas plus d'un creusage par BACKOFF_API_MIN (free tier)
    if os.path.exists(CPFP_OUT):
        old = charger_json(CPFP_OUT, {})
        try:
            last = parse_ts(old.get("ts", ""))
            if last and (datetime.now(timezone.utc) - last).total_seconds() < BACKOFF_API_MIN * 60:
                return {"declenche": False, "score": 0.0,
                        "detail": f"backoff API ({BACKOFF_API_MIN:.0f} min) — réessaie plus tard"}, mediane_actuelle
        except Exception:
            pass

    # Pré-filtre passé : on creuse. Tx récentes de la mempool (léger)
    # CORRECTION 21/08 : endpoint /mempool/recent (le /v1/ renvoyait 404)
    recents = requete_mempool("/mempool/recent")
    if not isinstance(recents, list) or not recents:
        return {"declenche": False, "score": 0.0,
                "detail": "mempool récente injoignable"}, mediane_actuelle

    detail = f"frais {mediane_actuelle:.0f} sat/vB > {CREUSAGE_RATIO:.1f}× médiane 7j — creusage (signature CPFP enfant ≥{FRAIS_RATIO:.0f}×)"
    for tx in recents:
        fee = float(tx.get("fee", 0.0) or 0.0)
        if fee <= 0 or not FRAIS_RATIO * (hist or 10.0) or fee < FRAIS_RATIO * (hist or 10.0):
            continue
        # Tx enfant suspecte : on regarde ses entrées (1 appel ciblé)
        txid = tx.get("txid", "")
        if not txid:
            continue
        txc = requete_mempool(f"/tx/{txid}")
        if not isinstance(txc, dict):
            continue
        parents = [vin.get("txid") for vin in txc.get("vin", []) if isinstance(vin, dict)]
        total_in = sum(float(i.get("value", 0.0) or 0.0) for i in txc.get("vin", [])
                       if isinstance(i, dict))
        total_btc = total_in / 1e8
        if total_btc < ARBRE_MIN_BTC:
            continue
        # Le premier parent (≤3 appels max par run, ciblés)
        parent_bas = False
        for pid in parents[:3]:
            ptx = requete_mempool(f"/tx/{pid}")
            if not isinstance(ptx, dict):
                continue
            vsize = float(ptx.get("vsize", 1.0) or 1.0)
            pfee = float(ptx.get("fee", 0.0) or 0.0)
            if vsize > 0 and (pfee / vsize) <= PARENT_MAX_SAT_VB:
                parent_bas = True
                break
        if parent_bas:
            return {"declenche": True,
                    "score": round(min(100.0, (fee / (FRAIS_RATIO * (hist or 10.0))) * 100.0), 2),
                    "detail": (f"CPFP : enfant {fee:.0f} sat/vB + parent ≤{PARENT_MAX_SAT_VB:.0f} "
                               f"sat/vB, arbre ≥{total_btc:.0f} BTC")}, mediane_actuelle
    return {"declenche": False, "score": 0.0, "detail": detail + " — aucun enfant suspect"}, mediane_actuelle


# ============================================================
# CARTE 3 — ACCUMULATION POUSSIÈRE (anticipation)
# ============================================================
def analyser_poussiere():
    """Poussière visible dans la mempool (frais < 2 sat/vB) + minimumFee.
    En observation on accumule les comptages dans cpfp_observations.jsonl
    → le seuil (≥1000/48h, référence Cortana) sera calibré sur le réel."""
    dust_vus = 0
    max_dust_btc = 0.0
    # CORRECTION 21/08 (Buffy, GO Christophe) : l'endpoint /v1/mempool/recent
    # renvoyait 404 → la carte 3 comptait 0 poussière depuis le 15/08 (bug réel).
    # Endpoint correct : /mempool/recent (10 tx) — l'échantillon reste petit mais
    # le comptage marche enfin ; on garde l'agrégation 48h pour le seuil 1000.
    recents = requete_mempool("/mempool/recent")
    if isinstance(recents, list):
        for tx in recents:
            fee = float(tx.get("fee", 0.0) or 0.0)
            vsize = float(tx.get("vsize", 0.0) or 0.0)
            if vsize > 0 and (fee / vsize) < DUST_MAX_SAT_VB:
                dust_vus += 1
                val = float(tx.get("value", 0.0) or 0.0)
                if val > max_dust_btc:
                    max_dust_btc = val / 1e8

    # Seuil de déclenchement conservateur : au moins 1000 tx poussière / 48h.
    # En observation on ne peut pas compter 48h en un appel → on agrège les
    # observations récentes (proxy honnête, calibré sur le réel).
    obs = charger_jsonl(CPFP_OBS, jours=2)
    total_dust = sum(int(o.get("dust_vus", 0) or 0) for o in obs) + dust_vus
    declenche = total_dust >= 1000

    return {"declenche": declenche,
            "score": round(min(100.0, (total_dust / 1000.0) * 50.0), 2),
            "detail": (f"poussière <{DUST_MAX_SAT_VB} sat/vB : {dust_vus} vues ce run, "
                       f"{total_dust} cumulées 48h (seuil 1000) — max {max_dust_btc:.4f} BTC")}, dust_vus


# ============================================================
# BILAN 7 JOURS (décision Christophe : basculer en actif ou ajuster)
# ============================================================
def generer_bilan():
    data = charger_json(CPFP_OUT, {})
    obs = charger_jsonl(CPFP_OBS, jours=7)
    n_declenche = sum(1 for o in obs if o.get("declenche_global"))
    n_z = sum(1 for o in obs if o.get("carte1"))
    n_cpfp = sum(1 for o in obs if o.get("carte2"))
    n_dust = sum(1 for o in obs if o.get("carte3"))

    contenu = f"""# Bilan 7 jours — Détection CPFP / Poussière (ACE777)
*Généré le : {datetime.now(timezone.utc).isoformat()}*

## État
- **Mode** : {data.get('mode', 'observation')} (SILENCIEUX tant que non validé)
- **Alerte émise** : JAMAIS (observation stricte)
- **Confirmation courante** : {data.get('confirmation', 0)} / {CONFIRMATION_MIN}
- **Runs observés (7j)** : {len(obs)}
- **Runs avec déclenchement global** (z-score ET CPFP) : {n_declenche}

## Déclenchements par carte
- Carte 1 (z-score adaptatif ≥{Z_SEUIL}σ + plancher {PLANCHER_BTC:.0f} BTC) : {n_z}
- Carte 2 (signature CPFP par frais ≥{FRAIS_RATIO:.0f}× médiane) : {n_cpfp}
- Carte 3 (poussière <{DUST_MAX_SAT_VB} sat/vB, seuil 1000/48h) : {n_dust}

## Calibration observée
- Médiane frais 7j : {data.get('calibration', {}).get('mediane_frais', '?')} sat/vB
- Moyenne mobile 7j : {data.get('calibration', {}).get('moyenne_7j', '?')} BTC
- Sigma : {data.get('calibration', {}).get('sigma', '?')}
- Max dust vu : {data.get('calibration', {}).get('max_dust', 0)} BTC

## Détail de la dernière passe
```json
{json.dumps(data.get('cartes', {}), ensure_ascii=False, indent=2)}
```

---
**DÉCISION REQUISE (Christophe)** : après lecture de ce bilan, soit
`python3 detecter_cpfp.py --actif` (brancher les alertes), soit ajuster les seuils
dans la spec et recalibrer.
"""
    verifier_kill_switch()
    try:
        with open(CPFP_BILAN, "w", encoding="utf-8") as f:
            f.write(contenu)
        print(f"[BILAN] Rapport écrit : {CPFP_BILAN}")
    except Exception as e:
        print(f"[BILAN ERREUR] {e}", file=sys.stderr)


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="Détecteur CPFP ACE777 (mode observation par défaut)")
    parser.add_argument("--once", action="store_true", help="Exécuter une passe puis quitter")
    parser.add_argument("--bilan", action="store_true", help="Générer le bilan 7 jours")
    parser.add_argument("--actif", action="store_true",
                        help="Basculer en mode ACTIF (alertes branchées) — APRÈS validation 7 jours")
    args = parser.parse_args()

    verifier_kill_switch()

    # Mode : observation par défaut, actif seulement après validation explicite
    mode = "observation"
    mode_file = charger_json(CPFP_MODE_FILE, {})
    if mode_file.get("mode") == "actif":
        mode = "actif"
    if args.actif:
        mode = "actif"
        ecriture_atomique(CPFP_MODE_FILE, {"mode": "actif", "ts": datetime.now(timezone.utc).isoformat()})
        print("[MODE] Bascule en mode ACTIF — alertes désormais autorisées (si confirmation ≥2).")

    if args.bilan:
        generer_bilan()
        return

    # --- Cartes ---
    carte1, moyenne_7j, sigma = analyser_zscore()
    carte2, mediane_frais = analyser_cpfp()
    carte3, dust_vus = analyser_poussiere()

    # D5 : double condition — z-score ET signature CPFP ensemble (un seul signal = rien)
    declenche_global = carte1["declenche"] and carte2["declenche"]

    # D6 : confirmation = runs successifs où le signal global est présent
    ancien = charger_json(CPFP_OUT, {})
    ancienne_conf = int(ancien.get("confirmation", 0) or 0)
    if declenche_global:
        confirmation = ancienne_conf + 1
    else:
        confirmation = max(0, ancienne_conf - 1)

    max_dust = max(float(o.get("max_dust_btc", 0.0) or 0.0) for o in charger_jsonl(CPFP_OBS, jours=7)) if charger_jsonl(CPFP_OBS, jours=7) else 0.0

    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "tip": "mempool.space + scan local",
        "zscores": carte1.get("score", 0.0),
        "cartes": {
            "carte1_zscore": carte1,
            "carte2_cpfp": carte2,
            "carte3_poussiere": carte3,
        },
        "declenche_global": declenche_global,
        "alerte_potentielle": {
            "emise": False,
            "raison": "MODE = observation (silencieux) — validation 7 jours requise" if mode == "observation"
                      else "confirmation < " + str(CONFIRMATION_MIN) if confirmation < CONFIRMATION_MIN
                      else "confirmation ≥ " + str(CONFIRMATION_MIN) + " — ALERTE AUTORISÉE",
        },
        "confirmation": confirmation,
        "calibration": {
            "mediane_frais": mediane_frais,
            "moyenne_7j": round(moyenne_7j, 2),
            "sigma": round(sigma, 2),
            "max_dust": round(max_dust, 6),
        },
    }
    ecriture_atomique(CPFP_OUT, payload)

    # Journal des observations (append-only, pour le bilan)
    append_jsonl(CPFP_OBS, {
        "ts": payload["ts"],
        "carte1": int(carte1["declenche"]),
        "carte2": int(carte2["declenche"]),
        "carte3": int(carte3["declenche"]),
        "declenche_global": int(declenche_global),
        "dust_vus": dust_vus,
        "max_dust_btc": round(max_dust, 6),
        "mediane_frais": mediane_frais,
    })

    # MODE ACTIF : si confirmation ≥ 2, le pont/Cortana/Ada verront le signal via
    # live.json (le pont onchain enrichit la section). Jamais d'alerte vocale ici :
    # c'est la veilleuse qui alerte, et le pont qui nourrit les analystes.
    print(f"[OK] cpfp mode={mode} | z={carte1['score']} cpfp={'OUI' if carte2['declenche'] else 'non'} "
          f"dust={dust_vus} | global={'OUI' if declenche_global else 'non'} "
          f"| confirmation={confirmation}/{CONFIRMATION_MIN} | {carte2['detail'][:60]}")


if __name__ == "__main__":
    main()
