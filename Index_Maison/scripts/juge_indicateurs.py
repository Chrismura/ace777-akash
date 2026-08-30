#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
juge_indicateurs.py
Pave d'indicateurs FRAIS pour le juge LLM des trades (SPEC_JUGE_ECLAIRE_20260824).
Lit des fichiers JSON produits par la chaine Index_Maison, verifie leur age (TTL),
extrait les valeurs essentielles, et assemble un texte compact (<= MAX_PAVE_CAR).

Regles:
- Python 3.9, stdlib uniquement, non fatal (un fichier en erreur -> une ligne [err]).
- Fraicheur: tout fichier plus vieux que son TTL est marque [STALE xx m] et son
  contenu n'est PAS injecte (le modele sait qu'il ne doit pas en tenir compte).
- Use en import par llm_gate_hub_bridge.py ET en test: python3 juge_indicateurs.py --test
"""

import json
import os
import shutil
import sys
import tempfile
import time

# --- Table des indicateurs (chemin relatif a la racine Indexes, TTL en s) ---
# Chaque entree: (nom court, chemin, ttl_s, nom_extracteur)
INDICATEURS = [
    ("taux_fantome", "data/bloc_privatise.json", 15 * 60, "extrait_bloc"),
    ("zone", "strategie/ada_gardienne_live.json", 10 * 60, "extrait_gardienne"),
    ("marche", "thermo/live.json", 10 * 60, "extrait_live"),
    ("sante", "thermo/sante_index.json", 30 * 60, "extrait_sante"),
    ("alarme", "strategie/alarme.json", 5 * 60, "extrait_alarme"),
    ("regime", "thermo/regime_couleur.json", 5 * 60, "extrait_regime"),
    ("deriv", "data/deriv_corr.json", 40 * 60, "extrait_deriv"),
    ("geopol", "thermo/live.json", 10 * 60, "extrait_geopol"),
]

MAX_PAVE_CAR = 1500  # coupure (le pont peut l'ajuster via env)


def _charger_json(chemin):
    """Retourne (ok: bool, contenu-dict ou message-erreur). Jamais fatal."""
    try:
        with open(chemin, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            return False, "json non-objet"
        return True, data
    except FileNotFoundError:
        return False, "absent"
    except json.JSONDecodeError:
        return False, "json corrompu"
    except Exception:
        return False, "erreur-lecture"


def _get(data, *keys, default="?"):
    cur = data
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur if cur is not None else default


# --- Extracteurs (tolerants : champ manquant -> '?') ---

def extrait_bloc(data):
    taux = _get(data, "taux_fantome")
    nb = _get(data, "n_snapshots")
    cachees = _get(data, "nb_tx_cachees")
    total = _get(data, "total_tx_bloc")
    non_fiable = _get(data, "taux_non_fiable", default=True)
    label = "non-fiable" if non_fiable else "fiable"
    texte = "taux_fantome=%s%% (%s snapshots, %s)" % (taux, nb, label)
    if cachees != "?" and total != "?":
        texte += " — privatise %s/%s tx" % (cachees, total)
    return texte


def extrait_gardienne(data):
    zone = _get(data, "zone")
    voilure = _get(data, "gardienne", "voilure_pct")
    alerte = _get(data, "gardienne", "alerte")
    sirene = _get(data, "gardienne", "sirene")
    pnl = _get(data, "etat", "pnl")
    return "zone=%s voilure=%s%% gardienne_alerte=%s sirene=%s pnl_alpha=%s" % (
        zone, voilure, alerte, sirene, pnl)


def extrait_live(data):
    """Marché + ONCHAIN COMPLET (fix 27/08 : avant, la clé lue était 'indice'
    alors que la vraie clé est 'indiceOnchain' → l'onchain entier (poussière,
    CPFP, baleines, indiceOnchain) n'atteignait JAMAIS le juge des trades)."""
    parts = []
    for cle in ("mark", "oi", "funding"):
        v = _get(data, cle)
        if v != "?":
            parts.append("%s=%s" % (cle, v))
    if isinstance(data.get("onchain"), dict):
        oc = data["onchain"]
        # Indice onchain unifié 0-100 (clé RÉELLE : indiceOnchain, pas 'indice')
        i = _get(oc, "indiceOnchain")
        lab = _get(oc, "indiceOnchainLabel")
        if i != "?":
            parts.append("onchain=%s/100" % i)
            if lab != "?":
                parts.append("(%s)" % lab)
        # Poussière + CPFP (score et z-score)
        dust = _get(oc, "cpfpDustScore")
        if dust != "?":
            parts.append("poussiere=%s" % dust)
        z = _get(oc, "cpfpZscore")
        if z != "?" and z != 0:
            parts.append("cpfp_z=%s" % z)
        sig = _get(oc, "cpfpSignal")
        if sig not in ("?", "None", "none", ""):
            parts.append("cpfp_signal=%s" % sig)
        # Baleines : blocs + direction
        b = _get(oc, "whaleBlocsN")
        btc = _get(oc, "whaleBlocsBtc")
        wd = _get(oc, "whaleDirLabel")
        if b != "?" and int(b) > 0:
            parts.append("baleines=%s blocs (%s BTC)" % (b, btc))
        if wd != "?" and wd != "neutral":
            parts.append("baleines_dir=%s" % wd)
    # SDI / IPT / RBF (mouvements silencieux, ajoutés 25/08)
    if isinstance(data.get("sdi"), dict):
        s = _get(data["sdi"], "sdi")
        if s != "?":
            parts.append("sdi=%s" % s)
    if isinstance(data.get("ipt"), dict):
        ip = _get(data["ipt"], "ipt")
        if ip != "?":
            parts.append("ipt=%s" % ip)
    if isinstance(data.get("rbf"), dict):
        r = _get(data["rbf"], "rbf_score")
        if r != "?":
            parts.append("rbf=%s" % r)
    if isinstance(data.get("couleur"), dict):
        c = _get(data["couleur"], "couleur")
        if c == "?":
            c = _get(data["couleur"], "regime")
        if c != "?":
            parts.append("couleur=%s" % c)
    elif isinstance(data.get("regime"), dict):
        c = _get(data["regime"], "couleur")
        if c != "?":
            parts.append("couleur=%s" % c)
    return " ".join(parts) if parts else "vide"


def extrait_sante(data):
    # Structure reelle : {"etat": "OK", "chaines_ok": "9/9", "degrades": [], ...}
    statut = _get(data, "etat")
    if statut == "?":
        statut = _get(data, "statut_global")
    if statut == "?":
        statut = _get(data, "statut")
    chaines = _get(data, "chaines_ok")
    deg = data.get("degradees") or data.get("anomalies") or []
    texte = "sante=%s" % statut
    if chaines != "?":
        texte += " (%s chaines)" % chaines
    if isinstance(deg, list) and deg:
        ids = [d.get("id", "?") if isinstance(d, dict) else d for d in deg]
        texte += " DEGRADE:%s" % ",".join(str(i) for i in ids)
    return texte


def extrait_alarme(data):
    # structure reelle : {"type": "prix", "variation_pct": 0.07, "raison": "volume x3", ...}
    if not data:
        return "aucune"
    typo = _get(data, "type")
    vari = _get(data, "variation_pct")
    raison = _get(data, "raison")
    texte = "alarme"
    if typo != "?":
        texte += " type=%s" % typo
    if vari != "?":
        texte += " var=%s%%" % vari
    if raison != "?":
        texte += " raison=%s" % raison
    return texte


def extrait_regime(data):
    coul = _get(data, "couleur")
    if coul == "?":
        coul = _get(data, "regime")
    if coul == "?":
        coul = _get(data, "statut")
    score = _get(data, "score")
    return "regime=%s score=%s" % (coul, score)


def extrait_geopol(data):
    """Géopolitique : score GEOPOL + niveau + modules + ML (live.json.geopol, 25/08).
    Compact : score unifié / niveau / nb modules OK / alertes éventuelles.
    Fraîcheur interne : le geopol est recalculé au run thermo (~1h) — si geopol.ts
    a plus de 2 h, on marque [STALE] et on n'injecte pas la valeur."""
    import datetime as _dt
    geo = data.get("geopol") or {}
    if not geo:
        return "geopol=[absent]"
    # Fraîcheur interne (le fichier live.json est réécrit par le pont toutes les 5 min
    # mais le geopol à l'intérieur date du dernier run thermo) : honnêteté.
    ts = geo.get("ts") or ""
    try:
        ts_dt = _dt.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        age_h = (time.time() - ts_dt.timestamp()) / 3600.0
    except Exception:
        age_h = None
    if age_h is not None and age_h > 2.0:
        return "geopol=[STALE %.1fh]" % age_h
    score = geo.get("score")
    niveau = geo.get("niveau") or "?"
    emoji = geo.get("emoji") or ""
    nb_ok = geo.get("nb_ok")
    nb_mod = geo.get("nb_modules")
    alerte = (geo.get("alerte") or "")[:90]
    ml = (geo.get("ml") or {}).get("label_nom") or ""
    s = "geopol=%s %s n=%s/%s ml=%s" % (score, emoji, nb_ok, nb_mod, ml)
    if alerte:
        s += " ALERTE:%s" % alerte
    return s


def extrait_deriv(data):
    """Dérivés : corrélations 30j + carte liquidité (data/deriv_corr.json, 24/08).
    Compact : corr OI/funding/LS/taker + longs dessous/shorts dessus + lecture courte."""
    corr = data.get("correlations") or {}
    r_oi = _get(corr.get("prix_oi") or {}, "r", default="?")
    r_fund = _get(corr.get("prix_funding") or {}, "r", default="?")
    r_ls = _get(corr.get("prix_longshort") or {}, "r", default="?")
    r_tak = _get(corr.get("prix_taker") or {}, "r", default="?")
    liq = data.get("liquidations") or {}
    lb = liq.get("longs_below_usd") or 0
    sa = liq.get("shorts_above_usd") or 0
    lecture = (liq.get("lecture") or "")[:120]
    return "corr_oi=%s corr_fund=%s corr_ls=%s corr_taker=%s liq_longs_dessous=%.0f$ liq_shorts_dessus=%.0f$ | %s" % (
        r_oi, r_fund, r_ls, r_tak, lb, sa, lecture)


_EXTRACTEURS = {
    "extrait_bloc": extrait_bloc,
    "extrait_gardienne": extrait_gardienne,
    "extrait_live": extrait_live,
    "extrait_sante": extrait_sante,
    "extrait_alarme": extrait_alarme,
    "extrait_regime": extrait_regime,
    "extrait_deriv": extrait_deriv,
    "extrait_geopol": extrait_geopol,
}


def _age_min(chemin, now):
    try:
        return max(0, int((now - os.stat(chemin).st_mtime) / 60))
    except Exception:
        return None


def pave(racine, now=None):
    """Assemble le pave d'indicateurs frais. Retourne une string (<= MAX_PAVE_CAR)."""
    if now is None:
        now = time.time()
    lignes = []
    for nom, rel, ttl, extrac in INDICATEURS:
        chemin = os.path.join(racine, rel)
        if not os.path.isfile(chemin):
            lignes.append("[%s] [absent]" % nom)
            continue
        age_min = _age_min(chemin, now)
        if age_min is None:
            lignes.append("[%s] [age-inconnu]" % nom)
            continue
        if age_min * 60 > ttl:  # STALE : contenu NON injecte
            lignes.append("[%s] [STALE %d m]" % (nom, age_min))
            continue
        ok, data = _charger_json(chemin)
        if not ok:
            lignes.append("[%s] [%s]" % (nom, data))
            continue
        try:
            texte = _EXTRACTEURS[extrac](data)
        except Exception:
            texte = "extraction impossible"
        lignes.append("[%s] %s (age %dm)" % (nom, texte, age_min))
    pave_str = "\n".join(lignes)
    if len(pave_str) > MAX_PAVE_CAR:
        pave_str = pave_str[:MAX_PAVE_CAR]
    return pave_str


# --- Mode CLI ---

def _racine_defaut():
    """Racine Index_Maisons = parent du dossier scripts/."""
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def _tests():
    """Tests hermétiques : tout dans /tmp, aucun fichier réel touché."""
    base = tempfile.mkdtemp(prefix="juge_test_")
    now = 1_700_000_000.0

    def ecrire(rel, obj, age_s):
        chemin = os.path.join(base, rel)
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, "w", encoding="utf-8") as fh:
            json.dump(obj, fh)
        os.utime(chemin, (now - age_s, now - age_s))

    # T1 : tout frais
    ecrire("thermo/live.json", {"mark": 77525.9, "oi": 107000.0, "funding": 0.0001}, 120)
    ecrire("data/bloc_privatise.json", {"taux_fantome": 2.15, "n_snapshots": 16,
                                        "nb_tx_cachees": 140, "total_tx_bloc": 6508,
                                        "taux_non_fiable": False}, 300)
    ecrire("strategie/ada_gardienne_live.json", {"zone": "VERT",
                                                 "gardienne": {"voilure_pct": 91, "alerte": False, "sirene": False},
                                                 "etat": {"pnl": 2.01}}, 200)
    ecrire("thermo/sante_index.json", {"etat": "OK", "chaines_ok": "9/9", "anomalies": [], "degradees": []}, 600)
    ecrire("strategie/alarme.json", {"type": "prix", "variation_pct": 0.07, "raison": "volume x3"}, 60)
    p = pave(base, now)
    assert "taux_fantome=2.15%" in p, p
    assert "zone=VERT" in p, p
    assert "sante=OK" in p, p
    assert "alarme type=prix" in p, p
    assert "STALE" not in p, p
    assert "[taux_fantome] [absent]" not in p, p
    print("T1 OK (frais, 5 indicateurs, aucun STALE)")

    # T2 : fichier vieilli -> STALE + contenu non injecte
    ecrire("data/bloc_privatise.json", {"taux_fantome": 99.9}, 20 * 60)
    p2 = pave(base, now)
    assert "[taux_fantome] [STALE" in p2, p2
    assert "99.9" not in p2, "contenu STALE ne doit pas etre injecte"
    print("T2 OK (STALE -> [STALE xx m], contenu non injecte)")

    # T3 : fichier absent
    os.remove(os.path.join(base, "strategie", "alarme.json"))
    p3 = pave(base, now)
    assert "[alarme] [absent]" in p3, p3
    print("T3 OK (fichier absent -> [absent], pas de crash)")

    # T4 : JSON corrompu
    with open(os.path.join(base, "thermo", "sante_index.json"), "w") as fh:
        fh.write("{pas du json!!")
    p4 = pave(base, now)
    assert "[sante] [json corrompu]" in p4, p4
    print("T4 OK (JSON corrompu -> [json corrompu], pas de crash)")

    # T5 : déterminisme a now fige
    assert pave(base, now=now) == pave(base, now=now)
    print("T5 OK (determinisme)")

    # T6 : longueur <= MAX sur donnees reelles (si racine existe)
    p6 = pave(_racine_defaut())
    assert len(p6) <= MAX_PAVE_CAR, "pave trop long"
    print("T6 OK (longueur <= %d car. sur donnees reelles : %d car.)" % (MAX_PAVE_CAR, len(p6)))

    print("TESTS JUGE OK (6/6)")
    shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        _tests()
    else:
        print(pave(_racine_defaut()))