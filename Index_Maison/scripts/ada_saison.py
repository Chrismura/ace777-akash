#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ada_saison.py — ADA Fondation 2 : détection de SAISON (indices bruts + alignement).

Lit thermo/live.json (indices bruts) + mission.json (fallback), calcule 6 signaux
déterministes (température, pouls/funding, bassin/OI, vortex/volume, essaim/foule,
baleines), l'alignement, et tranche une saison : CALME / ACCUMULATION / CHAUFFE /
MOUVEMENT / CHAOS. Détecte la bascule de saison.

Usage :
  python3 ada_saison.py          -> détecte, écrit live + état + archive
  python3 ada_saison.py --story  -> affiche la story courante
  python3 ada_saison.py --test   -> auto-test hermétique (sans fichiers réels, sans réseau)

Python 3.9 - stdlib uniquement. Lecture seule (jamais de modification du moteur).
"""

import json
import os
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple

# === CONSTANTES (modifiables pour runtests — les seuils s'ajustent avec les données) ===
SEUIL_LIQ_CHAOS = 50_000_000.0      # liq24Usd >= 50 M$ -> potentiel chaos
SEUIL_FUNDING_CHAUD = 0.0005         # |funding| >= 0.05 % -> chaud
SEUIL_VOL_FORT = 1.0                 # |chg24| >= 1 % -> mouvement fort
SEUIL_VOL_MODERE = 0.3               # |chg24| >= 0.3 % -> mouvement modéré
SEUIL_ALIGNEMENT = 0.6               # alignement >= 60 % -> MOUVEMENT
SEUIL_WHALE_N = 3                    # whaleN >= 3 -> activité
SEUIL_WHALE_USD = 5_000_000.0
SEUIL_FEAR_EXTREME = 25
SEUIL_GREED_EXTREME = 75
LIVE_STALE_H = 2                     # live.json plus vieux que 2h -> fallback mission.json

# === CHEMINS ===
BASE_DIR = os.path.join(os.path.expanduser("~"), "ace777-test-day1", "Index_Maison")
THERMO_LIVE = os.path.join(BASE_DIR, "thermo", "live.json")
MISSION = os.path.join(BASE_DIR, "cockpit", "mission.json")
STRATEGIE_DIR = os.path.join(BASE_DIR, "strategie")
ETAT_PATH = os.path.join(STRATEGIE_DIR, "ada_saison_etat.json")
LIVE_OUT = os.path.join(STRATEGIE_DIR, "ada_saison_live.json")
HISTO_DIR = os.path.join(STRATEGIE_DIR, "historique_saisons")

EMOJI = {"CHAOS": "⛈️", "MOUVEMENT": "🌀", "CHAUFFE": "🌡️",
         "ACCUMULATION": "💧", "CALME": "🧊"}


def safe_load_json(path: str) -> Dict[str, Any]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def safe_get(d: Dict[str, Any], key: str, default: Any = None) -> Any:
    val = d.get(key, default)
    return val if val is not None else default


def signaux(live: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Calcule les 6 signaux déterministes."""
    result: Dict[str, Dict[str, Any]] = {}

    # Température
    climate = safe_get(live, "climate", "ok")
    score = safe_get(live, "score", 0)
    force = 0
    if climate == "hot":
        force = 2
    elif climate == "warn":
        force = 1
    if score >= 70 and climate != "ok":
        force = min(2, force + 1)
    result["temperature"] = {"direction": "neutre", "force": force, "brut": climate}

    # Pouls (funding)
    funding = safe_get(live, "funding", 0.0) or 0.0
    seuil = SEUIL_FUNDING_CHAUD
    if funding >= seuil:
        direction = "long"
        force = 2 if abs(funding) >= 2 * seuil else 1
    elif funding <= -seuil:
        direction = "short"
        force = 2 if abs(funding) >= 2 * seuil else 1
    else:
        direction = "neutre"
        force = 0
    result["pouls"] = {"direction": direction, "force": force, "brut": funding}

    # Bassin (OI)
    deltas = safe_get(live, "deltas", {})
    oi_info = safe_get(deltas, "oi", {}) if isinstance(deltas, dict) else {}
    oi_dir = safe_get(oi_info, "dir", "flat") if isinstance(oi_info, dict) else "flat"
    direction = "long" if oi_dir == "up" else ("short" if oi_dir == "down" else "neutre")
    result["bassin"] = {"direction": direction, "force": 1 if direction != "neutre" else 0,
                        "brut": oi_dir}

    # Vortex (volume)
    chg24 = safe_get(live, "chg24", 0.0) or 0.0
    abs_chg = abs(chg24)
    force = 2 if abs_chg >= SEUIL_VOL_FORT else (1 if abs_chg >= SEUIL_VOL_MODERE else 0)
    direction = "long" if chg24 > 0 else ("short" if chg24 < 0 else "neutre")
    result["vortex"] = {"direction": direction, "force": force, "brut": chg24}

    # Essaim (foule)
    long_short = safe_get(live, "longShort", 1.0) or 1.0
    taker_ratio = safe_get(live, "takerRatio", 0.5) or 0.5
    fear_greed = safe_get(live, "fearGreed", 50)
    direction = "neutre"
    force = 0
    if long_short > 1.5:
        direction = "long"
        force = 1
    elif long_short < 0.8:
        direction = "short"
        force = 1
    if taker_ratio > 0.55:
        force += 1
    if fear_greed <= SEUIL_FEAR_EXTREME or fear_greed >= SEUIL_GREED_EXTREME:
        force = min(2, force + 1)
    result["essaim"] = {"direction": direction, "force": min(2, force), "brut": long_short}

    # Baleines
    whale_n = safe_get(live, "whaleN", 0) or 0
    whale_usd = safe_get(live, "whaleUsd", 0.0) or 0.0
    force = 1 if (whale_n >= SEUIL_WHALE_N or whale_usd >= SEUIL_WHALE_USD) else 0
    result["baleines"] = {"direction": "neutre", "force": force, "brut": whale_n}

    return result


def alignement(signaux_dict: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    nb_long = 0
    nb_short = 0
    for v in signaux_dict.values():
        if v["direction"] == "long":
            nb_long += 1
        elif v["direction"] == "short":
            nb_short += 1
    total = nb_long + nb_short
    score = abs(nb_long - nb_short) / max(1, total)
    direction = "long" if nb_long > nb_short else ("short" if nb_short > nb_long else "neutre")
    return {"nb_long": nb_long, "nb_short": nb_short,
            "score": round(score, 2), "direction": direction}


def decider(signaux_dict: Dict[str, Dict[str, Any]],
            align_dict: Dict[str, Any],
            live: Dict[str, Any]) -> Tuple[str, str]:
    """Détermine la saison selon les règles de priorité."""
    liq = safe_get(live, "liq24Usd", 0.0) or 0.0
    vol_force = signaux_dict.get("vortex", {}).get("force", 0)
    funding = safe_get(live, "funding", 0.0) or 0.0
    funding_chaud = abs(funding) >= SEUIL_FUNDING_CHAUD
    temp_force = signaux_dict.get("temperature", {}).get("force", 0)
    oi_dir = signaux_dict.get("bassin", {}).get("direction", "neutre")
    funding_neutre = signaux_dict.get("pouls", {}).get("direction", "neutre") == "neutre"
    vol_force0 = vol_force == 0

    if liq >= SEUIL_LIQ_CHAOS and (vol_force == 2 or funding_chaud):
        return "CHAOS", "orage — liquidations massives"
    # MOUVEMENT exige un VRAI alignement : >= 3 indices directionnels (évite le
    # score saturé à 1.0 avec un seul indice aligné) ET vol en marche
    nb_alignes = align_dict["nb_long"] + align_dict["nb_short"]
    if align_dict["score"] >= SEUIL_ALIGNEMENT and nb_alignes >= 3 and vol_force >= 1:
        return "MOUVEMENT", "vortex en marche (direction %s)" % align_dict["direction"]
    if temp_force >= 1 and (funding_chaud or oi_dir == "long"):
        return "CHAUFFE", "la température monte, le ciel se prépare"
    if oi_dir == "long" and vol_force0 and funding_neutre:
        return "ACCUMULATION", "le bassin se remplit en silence"
    return "CALME", "hiver — rien ne bouge, ADA dort"


def detecter_bascule(etat: Dict[str, Any], saison: str) -> Tuple[bool, str]:
    """Bascule de saison : False si état absent (premier run) ou saison inchangée."""
    if not etat:
        return False, ""
    previous = etat.get("saison", "")
    if not previous or previous == saison:
        return False, ""
    return True, "%s → %s" % (previous, saison)


def story(saison: str, align_dict: Dict[str, Any],
          signaux_dict: Dict[str, Dict[str, Any]],
          bascule: bool, bascule_raison: str, degraded: bool = False) -> List[str]:
    """Génère 2-4 phrases françaises déterministes."""
    lines: List[str] = []
    temp = signaux_dict.get("temperature", {})
    oi = signaux_dict.get("bassin", {})
    vol = signaux_dict.get("vortex", {})

    if saison == "CHAOS":
        lines.append("SAISON : CHAOS ⛈️ — liquidations massives détectées, le marché tremble.")
    elif saison == "MOUVEMENT":
        lines.append("SAISON : MOUVEMENT 🌀 — vortex %s, alignement %d%%."
                     % (align_dict["direction"], int(align_dict["score"] * 100)))
    elif saison == "CHAUFFE":
        lines.append("SAISON : CHAUFFE 🌡️ — température %s, bassin %s."
                     % (temp.get("brut", "ok"), oi.get("direction", "neutre")))
    elif saison == "ACCUMULATION":
        lines.append("SAISON : ACCUMULATION 💧 — le bassin se remplit en silence.")
    else:
        lines.append("SAISON : CALME 🧊 — hiver, ADA dort.")

    lines.append("Alignement : %d haussiers / %d baissiers."
                 % (align_dict["nb_long"], align_dict["nb_short"]))
    vf = vol.get("force", 0)
    if vf >= 2:
        lines.append("Le vortex tourne fort (%+.2f %% sur 24h) — le mouvement est là." % (vol.get("brut") or 0))
    elif vf == 1:
        lines.append("Le vent se lève (%+.2f %% sur 24h) — pas encore un vortex." % (vol.get("brut") or 0))
    if bascule:
        lines.append("⚡ BASCULE : %s — le ciel change, prépare-toi." % bascule_raison)
    if degraded:
        lines.append("⚠️ Sources dégradées — saison à confirmer avec des données fraîches.")
    return lines


def ecrire_sorties(saison: str, align_dict: Dict[str, Any],
                   signaux_dict: Dict[str, Dict[str, Any]],
                   bascule: bool, bascule_raison: str,
                   sources: List[str], degraded: bool = False) -> List[str]:
    """Écrit live.json (atomique), état et archive. Retourne la story."""
    ts = datetime.now(timezone.utc).isoformat()
    out = {
        "ts": ts,
        "saison": saison,
        "emoji": EMOJI.get(saison, ""),
        "direction": align_dict["direction"],
        "bascule": bascule,
        "bascule_raison": bascule_raison,
        "alignement": align_dict,
        "indices": signaux_dict,
        "story": story(saison, align_dict, signaux_dict, bascule, bascule_raison, degraded),
        "sources": sources,
        "degraded": degraded,
    }
    os.makedirs(STRATEGIE_DIR, exist_ok=True)
    os.makedirs(HISTO_DIR, exist_ok=True)

    # live (écriture atomique : tmp + replace)
    tmp = LIVE_OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    os.replace(tmp, LIVE_OUT)

    # état
    with open(ETAT_PATH, "w", encoding="utf-8") as f:
        json.dump({"saison": saison, "ts": ts}, f, ensure_ascii=False, indent=2)

    # archive (JSONL append — un seul fichier, rotation à ~5000 lignes)
    # Avant : un fichier SAISON_<ts>.json par scan (~toutes les 10s avec la page
    # cockpit ouverte) → 28k fichiers. Désormais : append compact, rotation bornée.
    hist = os.path.join(HISTO_DIR, "historique_saisons.jsonl")
    try:
        os.makedirs(HISTO_DIR, exist_ok=True)
        with open(hist, "a", encoding="utf-8") as f:
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
        # rotation : au-delà de ~2 Mo (≈5000 lignes), on archive le courant en .old
        if os.path.exists(hist) and os.path.getsize(hist) > 2_000_000:
            old = hist + ".old"
            try:
                if os.path.exists(old):
                    os.remove(old)
                os.replace(hist, old)
            except Exception:
                pass
    except Exception:
        pass

    return out["story"]


def charger_donnees() -> Tuple[Dict[str, Any], List[str], bool]:
    """Live.json d'abord ; fallback mission.json (thermo) si absent/vieux.
    Retourne (données, sources, degraded)."""
    live = safe_load_json(THERMO_LIVE)
    if live:
        ts_unix = safe_get(live, "tsUnix", 0) or 0
        if ts_unix and (time.time() - ts_unix) > LIVE_STALE_H * 3600:
            live = {}  # stale -> fallback
        else:
            return live, ["live.json"], False
    mission = safe_load_json(MISSION)
    thermo = mission.get("thermo") or {}
    if thermo:
        return thermo, ["mission.json (live.json absent/vieux)"], True
    return live or {}, ["aucune source fraîche"], True


def scan() -> None:
    """Exécution principale."""
    live, sources, degraded = charger_donnees()
    sig = signaux(live)
    al = alignement(sig)
    saison, raison = decider(sig, al, live)

    # Bascule : pas de fausse bascule au premier run (état absent)
    etat = safe_load_json(ETAT_PATH)
    bascule, bascule_raison = detecter_bascule(etat, saison)

    story_lines = ecrire_sorties(saison, al, sig, bascule, bascule_raison, sources, degraded)
    for line in story_lines:
        print(line)


def run_tests() -> int:
    """Auto-tests hermétiques (aucun fichier réel)."""
    errors = 0

    def check(name, cond):
        nonlocal errors
        print("OK  %s" % name if cond else "FAIL %s" % name)
        if not cond:
            errors += 1

    # CHAOS
    mock = {"liq24Usd": 80_000_000, "chg24": -1.5, "funding": 0.0006}
    sig = signaux(mock); al = alignement(sig)
    s, _ = decider(sig, al, mock)
    check("CHAOS (liq 80M + vol fort)", s == "CHAOS")

    # MOUVEMENT long
    mock = {"funding": 0.0006, "deltas": {"oi": {"dir": "up"}}, "chg24": 0.8,
            "longShort": 1.9, "fearGreed": 30, "takerRatio": 0.6}
    sig = signaux(mock); al = alignement(sig)
    s, _ = decider(sig, al, mock)
    check("MOUVEMENT long (alignement + vol)", s == "MOUVEMENT" and al["direction"] == "long")

    # ACCUMULATION
    mock = {"funding": 0.0001, "deltas": {"oi": {"dir": "up"}}, "chg24": 0.1,
            "longShort": 1.2, "climate": "ok"}
    sig = signaux(mock); al = alignement(sig)
    s, _ = decider(sig, al, mock)
    check("ACCUMULATION (OI up, vol basse)", s == "ACCUMULATION")

    # CALME
    mock = {"funding": 0.0, "chg24": 0.0, "longShort": 1.0, "climate": "ok"}
    sig = signaux(mock); al = alignement(sig)
    s, _ = decider(sig, al, mock)
    check("CALME (tout plat)", s == "CALME")

    # CHAUFFE
    mock = {"climate": "warn", "funding": 0.0006, "deltas": {"oi": {"dir": "up"}}, "chg24": 0.2}
    sig = signaux(mock); al = alignement(sig)
    s, _ = decider(sig, al, mock)
    check("CHAUFFE (température + funding chaud)", s == "CHAUFFE")

    # Bascule : logique extraite et testée réellement
    b, r = detecter_bascule({}, "CHAUFFE")
    check("bascule premier run (etat absent) = False", not b and r == "")
    b, r = detecter_bascule({"saison": "CALME"}, "CHAUFFE")
    check("bascule CALME->CHAUFFE = True", b and r == "CALME → CHAUFFE")
    b, r = detecter_bascule({"saison": "CALME"}, "CALME")
    check("bascule meme saison = False", not b)

    # story contient la saison
    st = story("CHAUFFE", {"nb_long": 3, "nb_short": 1, "score": 0.5, "direction": "long"},
               {"temperature": {"brut": "warn", "force": 1, "direction": "neutre"},
                "bassin": {"direction": "long", "force": 1, "brut": "up"},
                "vortex": {"direction": "neutre", "force": 0, "brut": 0.2}}, False, "")
    check("story CHAUFFE en français", any("CHAUFFE" in s for s in st) and any("haussiers" in s for s in st))

    return 0 if errors == 0 else 1


def main() -> None:
    args = sys.argv[1:]
    if "--test" in args:
        sys.exit(run_tests())
    if "--story" in args:
        data = safe_load_json(LIVE_OUT)
        for line in data.get("story", ["Aucune story disponible."]):
            print(line)
        sys.exit(0)
    scan()


if __name__ == "__main__":
    main()
