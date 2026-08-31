#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ada_gardienne.py — ADA GARDIENNE + COUP D'ŒIL (fondation 3)

Rôle : GUETTE + ALERTE + CONSEIL. ADA ne touche JAMAIS au moteur :
aucun ordre, aucun gel, aucun retrait forcé. ACE est construit pour
marcher dans la tempête — c'est là que sont les plus-values.

Principes (gravés par Christophe) :
  - La voilure est CONTINUE (règles lissées, jamais de saut IF/THEN brutal).
  - Le seuil X est RELATIF et auto-appris (ADA observe et s'enrichit sur
    sa propre donnée), jamais une valeur fixe.
  - ROUGE = « réduis la voilure » (ACE le fait déjà lui-même — ADA reflète).
  - Sous le seuil X = « prends la perte » (perte encaissée = chasse continue).
  - JAMAIS de blocage : ACE reste libre de re-rentrer 1, 3 ou 10 s après une
    claque — aucune fenêtre d'attente imposée.
  - Les ALERTES ne sont PAS lissées : au premier signal (funding hors norme,
    liquidations, bascule, chute brutale), ADA hurle immédiatement.
  - La famille (trio) est consultée aux besoins, jamais en spam.

Python 3.9 stdlib uniquement. Écritures atomiques. Crash-safe.
"""

import json
import os
import sys
import time
import argparse
import tempfile
import shutil
import datetime
from typing import Dict, Any, List, Tuple, Optional

# ============================================================
# CHEMINS (même convention que ada_saison.py)
# ============================================================
BASE_DIR = os.path.join(os.path.expanduser("~"), "ace777-test-day1", "Index_Maison")
STRATEGIE_DIR = os.path.join(BASE_DIR, "strategie")
HISTORIQUE_DIR = os.path.join(STRATEGIE_DIR, "historique_gardienne")
HISTORIQUE_JSONL = os.path.join(STRATEGIE_DIR, "ada_gardienne_historique.jsonl")
COCKPIT_DIR = os.path.join(BASE_DIR, "cockpit")
THERMO_LIVE = os.path.join(BASE_DIR, "thermo", "live.json")
MISSION = os.path.join(COCKPIT_DIR, "mission.json")
SAISON_LIVE = os.path.join(STRATEGIE_DIR, "ada_saison_live.json")
JOURNAL_LIVE = os.path.join(STRATEGIE_DIR, "journal_intention_live.json")
GARDIENNE_LIVE = os.path.join(STRATEGIE_DIR, "ada_gardienne_live.json")
AVIS_FAMILLE = os.path.join(STRATEGIE_DIR, "AVIS_FAMILLE_SESSION.md")
ETAT_FAMILLE = os.path.join(STRATEGIE_DIR, "famille_derniere.json")

# ============================================================
# CONSTANTES DOCUMENTÉES (pondérations + zones + ancrages)
# ============================================================

# Pondérations du mélange (doivent sommer à 1.0)
W_BLEED = 0.40      # le saignement (perte vs ancrage + vitesse de chute)
W_STORM = 0.40      # la tempête (saison + intensité marché)
W_REVERSAL = 0.20   # le retournement (alignement qui se retourne)

# Bornes de zones — en POURCENT de voilure (bandes LISSÉES, pas des seuils qui claquent)
ZONE_VERT = 70.0    # voilure >= 70 % -> tout va bien
ZONE_JAUNE = 45.0   # 45 % <= voilure < 70 % -> le ciel se charge
                    # voilure < 45 % -> ROUGE

# Ancrages RELATIFS du seuil X (PRENDS LA PERTE)
A1 = 1.5            # perte_session >= A1 * perte_moyenne_rolling (historique ADA)
A2 = 0.8            # perte_session >= A2 * gains_peak_session
FENETRE_HIST = 60   # scans gardés dans l'historique roulant ADA

LIVE_STALE_H = 2.0  # thermo/live.json plus vieux que 2h -> fallback mission.json
ANTI_SPAM_MIN = 5   # famille : pas de double consultation avant 5 min

# Fallbacks UNIQUEMENT au premier démarrage (avant que ADA n'ait appris)
FALLBACK_PERTE_MOY = 50.0
FALLBACK_GAINS = 50.0

# FIX 31/08 (GO Christophe, audit ADA) : les « liquidations massives » utilisaient
# un seuil STATIQUE 50 M$ — mais la médiane 7j de liq24Usd est 44,7 M$ et le max
# historique 141 M$ : 50 M$ sonnait sur un jour NORMAL (28/08 : 54,7 M$) → sirène
# pour du « au-dessus de la moyenne ». Désormais : massives = liq24h > 1,5× médiane
# 7j, avec un plancher absolu de 80 M$ (un vrai pic). Même référence pour la
# pression storm (fini la saturation à 100% dès 50 M$).
HISTORY_JSONL = os.path.join(BASE_DIR, "thermo", "history.jsonl")
LIQ_MULT_MEDIANE = 1.5       # x la médiane 7j = niveau « massif »
LIQ_PLANCHER_USD = 80_000_000.0  # jamais en dessous de 80 M$ (plancher absolu)
LIQ_FALLBACK_USD = 50_000_000.0  # historique (si aucune donnée 7j disponible)


def mediane_liq_7j() -> Optional[float]:
    """Médiane de liq24Usd sur les 7 derniers jours (thermo/history.jsonl).
    Référence RELATIVE de la normale — un jour normal ne doit jamais sonner
    « massif ». Retourne None si pas assez de données (fallback historique)."""
    try:
        vals: List[float] = []
        now = time.time()
        if os.path.exists(HISTORY_JSONL):
            with open(HISTORY_JSONL, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        j = json.loads(line)
                    except Exception:
                        continue
                    ts = j.get("tsUnix")
                    v = j.get("liq24Usd")
                    if ts is None or v is None:
                        continue
                    if now - float(ts) > 7 * 86400:
                        continue
                    try:
                        vals.append(float(v))
                    except (TypeError, ValueError):
                        continue
        if not vals:
            return None
        vals.sort()
        return vals[len(vals) // 2]
    except Exception:
        return None

EN_TEST = False     # mode tests : jamais de consultation famille, tout en /tmp
DEMO_MAX_MIN = 20   # drapeau démo périmé au-delà -> auto-retour au réel


# ============================================================
# HELPERS MAISON
# ============================================================

def safe_load_json(path: str, default: Any = None) -> Any:
    if default is None:
        default = {}
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return default


def atomic_write_json(path: str, data: Any) -> bool:
    try:
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=d or ".", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, path)
        return True
    except Exception:
        return False


def safe_get(d: Any, keys: List[str], default: Any = None) -> Any:
    cur = d
    for k in keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return default
    return cur


def now_iso() -> str:
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


def lissage_monotone(p: float) -> float:
    """Smoothstep : lissage continu, jamais de saut brutal."""
    p = max(0.0, min(1.0, p))
    return 3.0 * p * p - 2.0 * p * p * p


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


# ============================================================
# CHARGEMENT DES DONNÉES (stale guard + fallback)
# ============================================================

def est_vieux(thermo: Dict, stale_h: float = LIVE_STALE_H) -> bool:
    """Vrai si live.json est plus vieux que stale_h (tsUnix epoch, fallback ts ISO)."""
    if not thermo:
        return True
    ts_unix = thermo.get("tsUnix", 0) or 0
    if ts_unix:
        return (time.time() - float(ts_unix)) > stale_h * 3600
    ts = str(thermo.get("ts", ""))
    try:
        dt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        return (datetime.datetime.now(datetime.timezone.utc) - dt).total_seconds() > stale_h * 3600
    except Exception:
        return False


def en_mode_demo() -> bool:
    """Vrai si le drapeau démo cockpit est présent (données synthétiques)."""
    return os.path.exists(os.path.join(STRATEGIE_DIR, "ada_demo.flag"))


def charger_donnees_demo() -> Optional[Dict[str, Any]]:
    """Mode démo cockpit : si le drapeau est présent et frais, ADA joue des
    données SYNTHÉTIQUES (pour montrer la tempête à l'écran, sans risque).
    Si le drapeau est périmé, on le retire et on revient au réel (auto-réparation)."""
    try:
        flag_path = os.path.join(STRATEGIE_DIR, "ada_demo.flag")
        if not os.path.exists(flag_path):
            return None
        flag = safe_load_json(flag_path, {})
        ts = float(flag.get("ts", 0) or 0)
        if ts and (time.time() - ts) > DEMO_MAX_MIN * 60:
            try:
                os.remove(flag_path)
            except Exception:
                pass
            return None
        d = safe_load_json(os.path.join(STRATEGIE_DIR, "ada_demo_data.json"), {})
        return d if d else None
    except Exception:
        return None


def charger_donnees() -> Dict[str, Any]:
    """Charge thermo (stale guard -> fallback mission), saison, journal, avis famille."""
    data: Dict[str, Any] = {
        "saison": safe_load_json(SAISON_LIVE, {"saison": "CALME", "direction": "flat", "alignement": 0.5}),
        "journal": safe_load_json(JOURNAL_LIVE, {"bots": {}}),
        "mission": safe_load_json(MISSION, {}),
        "thermo": {},
        "sources": ["aucune source fraîche"],
        "degraded": False,
        "avis_famille": "",
        # 18/08 (Christophe : « Ada ne voit pas les bots ») — état ACE + HULK
        # extrait de mission.json (écrit par cockpit_mission_feed) en lecture seule.
        "bots": {},
    }

    # --- VISION DES BOTS (ACE + HULK) depuis mission.json ---
    try:
        mission_bots = data.get("mission") or {}
        ace_a = mission_bots.get("alpha") or {}
        ace_b = mission_bots.get("beta") or {}
        hulk = mission_bots.get("hulk") or {}
        data["bots"] = {
            "ace_alpha_fills": ace_a.get("fills"),
            "ace_alpha_pnl": ace_a.get("pnl"),
            "ace_beta_fills": ace_b.get("fills"),
            "ace_beta_pnl": ace_b.get("pnl"),
            "ace_combo": mission_bots.get("comboPnl"),
            "hulk_pnl": hulk.get("pnl"),
            "hulk_trades": hulk.get("trades"),
            "hulk_positions": len(hulk.get("positions") or []),
            "hulk_cash": hulk.get("cash"),
            "hulk_equity": hulk.get("equity"),
        }
        if data["bots"]:
            data["sources"].insert(0, "mission.json (bots ACE+HULK)")
    except Exception:
        pass

    thermo = safe_load_json(THERMO_LIVE, {})
    if thermo and not est_vieux(thermo):
        data["thermo"] = thermo
        data["sources"] = ["live.json"]
    else:
        fallback = safe_get(data["mission"], ["thermo"], {}) or {}
        if fallback:
            data["thermo"] = fallback
            data["sources"] = ["mission.json (live.json absent ou vieux)"]
            data["degraded"] = True
        else:
            data["degraded"] = True

    try:
        if os.path.exists(AVIS_FAMILLE):
            with open(AVIS_FAMILLE, "r", encoding="utf-8") as f:
                data["avis_famille"] = f.read(4000)
    except Exception:
        pass

    # Mode démo cockpit : les données synthétiques remplacent les vraies
    demo = charger_donnees_demo()
    if demo:
        for k in ("saison", "journal", "thermo"):
            if demo.get(k):
                data[k] = demo[k]
        data["sources"] = ["démo cockpit (synthétique)"]
        data["degraded"] = False

    return data


# ============================================================
# L'HISTORIQUE ROULANT D'ADA (elle s'enrichit sur sa propre donnée)
# ============================================================

def lire_historique() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    try:
        if os.path.exists(HISTORIQUE_JSONL):
            with open(HISTORIQUE_JSONL, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rows.append(json.loads(line))
                    except Exception:
                        continue
    except Exception:
        pass
    return rows[-FENETRE_HIST:]


def ajouter_historique(ts: str, pnl: float, voilure: float, zone: str) -> None:
    """Écriture ATOMIQUE (tmp + replace) — jamais de jsonl à moitié écrit."""
    try:
        rows = lire_historique()
        rows.append({"ts": ts, "pnl": pnl, "voilure": voilure, "zone": zone})
        rows = rows[-FENETRE_HIST:]
        d = os.path.dirname(HISTORIQUE_JSONL)
        if d:
            os.makedirs(d, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=d, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp_path, HISTORIQUE_JSONL)
    except Exception:
        pass


# ============================================================
# LES ANCRAGES RELATIFS (seuil X)
# ============================================================

def calculer_ancres(rows: List[Dict[str, Any]], pnl_cur: float) -> Dict[str, float]:
    """perte_moy = moyenne des chutes de pnl observées · gains_peak = pic de pnl.
    Tout est RELATIF : ADA apprend sa propre normalité."""
    pertes: List[float] = []
    pnls = [float(r.get("pnl", 0.0)) for r in rows]
    pnls.append(pnl_cur)
    for i in range(1, len(pnls)):
        d = pnls[i] - pnls[i - 1]
        if d < 0:
            pertes.append(abs(d))

    perte_moy = (sum(pertes) / len(pertes)) if pertes else FALLBACK_PERTE_MOY
    gains_peak = max(0.0, max(pnls)) if pnls else 0.0
    if gains_peak <= 0:
        gains_peak = FALLBACK_GAINS

    seuil_x = max(A1 * perte_moy, A2 * gains_peak)
    return {
        "perte_moy": round(perte_moy, 2),
        "gains_peak": round(gains_peak, 2),
        "seuil_x": round(seuil_x, 2),
    }


# ============================================================
# LES PRESSIONS (0..1)
# ============================================================

def calculer_p_bleed(perte_session: float, seuil_x: float,
                     pnl_prev: Optional[float], pnl_cur: float) -> float:
    """Saignement : rapport perte/ancrage (relatif) + vitesse de chute (relative)."""
    ratio = (perte_session / seuil_x) if seuil_x > 0 else 0.0
    p_base = lissage_monotone(clamp(ratio * 0.8))

    vitesse = 0.0
    if pnl_prev is not None:
        denom = max(1.0, abs(pnl_cur), abs(pnl_prev))
        vitesse = clamp(abs(pnl_cur - pnl_prev) / denom)

    return round(clamp(0.7 * p_base + 0.35 * vitesse), 3)


def calculer_p_storm(saison: Dict, thermo: Dict) -> float:
    saison_map = {
        "CALME": 0.10, "ACCUMULATION": 0.30, "CHAUFFE": 0.50,
        "MOUVEMENT": 0.70, "CHAOS": 0.95,
    }
    base = saison_map.get(str(saison.get("saison", "CALME")).upper(), 0.3)
    try:
        funding = abs(float(thermo.get("funding", 0.0)))
        chg24 = abs(float(thermo.get("chg24", 0.0)))
        # FIX 31/08 : référence = médiane 7j × 1,5 (au lieu du 50 M$ fixe qui
        # sature à 100% dès 50 M$ et ne distingue pas 53 M$ de 141 M$).
        med = mediane_liq_7j()
        ref = (med * LIQ_MULT_MEDIANE) if med else LIQ_FALLBACK_USD
        liq = clamp(float(thermo.get("liq24Usd", 0.0)) / ref)
        fear = abs(float(thermo.get("fearGreed", 50)) - 50) / 50
        intensite = clamp(funding * 4.0 + chg24 * 1.2 + liq * 0.8 + fear * 0.6)
    except Exception:
        intensite = 0.0
    return round(clamp(base * 0.6 + intensite * 0.4), 3)


def calculer_p_reversal(saison: Dict, thermo: Dict) -> float:
    """Retournement : le camp opposé gagne du terrain (alignement de la saison)."""
    align = saison.get("alignement") or {}
    if isinstance(align, dict):
        score = float(align.get("score", 0.5) or 0.5)
        nb_long = float(align.get("nb_long", 0.0) or 0.0)
        nb_short = float(align.get("nb_short", 0.0) or 0.0)
        direction = str(align.get("direction") or saison.get("direction", "flat"))
    else:
        score = float(align or 0.5)
        nb_long = nb_short = 0.0
        direction = str(saison.get("direction", "flat"))

    if nb_long + nb_short > 0:
        total = nb_long + nb_short
        if direction == "long":
            part_contraire = nb_short / total
        elif direction == "short":
            part_contraire = nb_long / total
        else:
            part_contraire = 0.0
        if part_contraire > 0.5:
            return round(clamp(part_contraire * 1.5), 3)

    # Sinon : l'alignement qui faiblit = signe de retournement
    return round(clamp((0.5 - score) * 0.6), 3)


def pressions(data: Dict, perte_session: float, seuil_x: float,
              pnl_prev: Optional[float], pnl_cur: float) -> Dict[str, float]:
    return {
        "bleed": calculer_p_bleed(perte_session, seuil_x, pnl_prev, pnl_cur),
        "storm": calculer_p_storm(data["saison"], data["thermo"]),
        "reversal": calculer_p_reversal(data["saison"], data["thermo"]),
    }


# ============================================================
# LES SIRÈNES (alertes INSTANTANÉES — pas de lissage, on hurle tout de suite)
# ============================================================

def signaux_instantanes(data: Dict, pnl_cur: float,
                        pnl_prev: Optional[float]) -> Tuple[bool, List[str]]:
    """Signaux bruts, relatifs à la normale du marché — AUCUN lissage.
    Dès qu'un signal claque, ADA allume les feux immédiatement (même si
    la voilure, elle, est encore en train de descendre en douceur)."""
    declencheurs: List[str] = []
    saison = data.get("saison", {})
    thermo = data.get("thermo", {})

    # 1. La bascule de saison : le ciel change -> on hurle avant le mouvement
    if saison.get("bascule"):
        declencheurs.append("bascule de saison")

    # 2. Tempête déclarée par la saison (CHAOS)
    if str(saison.get("saison", "")).upper() == "CHAOS":
        declencheurs.append("tempête déclarée")

    # 3. Funding hors norme RELATIVE (vs sa propre moyenne 30j) + plancher
    try:
        funding = abs(float(thermo.get("funding", 0.0) or 0.0))
        moy30 = abs(float(thermo.get("fundingAvg30", 0.0) or 0.0))
        if moy30 > 0 and funding >= 3.0 * moy30 and funding >= 0.0003:
            declencheurs.append("funding à %.1fx sa moyenne" % (funding / moy30))
    except Exception:
        pass

    # 4. Liquidations massives (FIX 31/08 : seuil RELATIF médiane 7j × 1,5,
    # plancher 80 M$ — un jour normal ne sonne plus « massif »)
    try:
        liq_now = float(thermo.get("liq24Usd", 0.0) or 0.0)
        med = mediane_liq_7j()
        seuil = max((med * LIQ_MULT_MEDIANE) if med else LIQ_FALLBACK_USD,
                    LIQ_PLANCHER_USD)
        if liq_now >= seuil:
            declencheurs.append("liquidations massives (%.0f M$ ≥ seuil %.0f M$)"
                                % (liq_now / 1e6, seuil / 1e6))
    except Exception:
        pass

    # 5. Le vortex tourne fort (indice force 2 de la saison)
    try:
        vortex = safe_get(saison, ["indices", "vortex"], {})
        if int(vortex.get("force", 0) or 0) >= 2:
            declencheurs.append("le vortex tourne fort")
    except Exception:
        pass

    # 6. Chute brutale de la session d'un scan à l'autre (relative)
    if pnl_prev is not None and pnl_cur < pnl_prev:
        denom = max(1.0, abs(pnl_prev))
        chute = (pnl_prev - pnl_cur) / denom
        if chute >= 0.30 and abs(pnl_prev) >= 5.0:
            declencheurs.append("chute brutale de la session")

    return bool(declencheurs), declencheurs


# ============================================================
# VOILURE (mélange pondéré + lissage continu)
# ============================================================

def calculer_voilure(p: Dict[str, float], thermo: Optional[Dict] = None) -> float:
    melange = W_BLEED * p["bleed"] + W_STORM * p["storm"] + W_REVERSAL * p["reversal"]
    voilure = round(clamp(1.0 - lissage_monotone(melange), 0.0, 1.0) * 100.0, 1)
    # Modulateur ONCHAIN (famille : ±10% max, jamais de blocage, seuil relatif auto-appris)
    if thermo:
        oc = thermo.get("onchain") or {}
        cumul_24h = float(oc.get("whaleCumul24hBtc", 0.0) or 0.0)
        moy7j = float(oc.get("whaleMoy7jBtc", 0.0) or 0.0)
        direction = str(oc.get("whaleDir", "neutral"))
        if moy7j > 0 and cumul_24h > 2.0 * moy7j and direction == "outflow":
            facteur = 0.93  # sortie massive d'exchange → pression vendeuse → voilure réduite
        elif direction == "inflow" and cumul_24h > moy7j:
            facteur = 1.05  # accumulation → voilure légèrement élargie
        else:
            facteur = 1.0
        voilure = round(clamp(voilure * facteur, 0.0, 100.0), 1)
        # Modulateur CPFP v2 (confirmation ≥2, mode actif — géré par le pont) :
        # EXÉCUTION CPFP confirmée → prudence (expulsion imminente) ; sinon neutre.
        cpfp_signal = oc.get("cpfpSignal")
        if cpfp_signal and "EXÉCUTION CPFP" in str(cpfp_signal):
            facteur_cpfp = 0.93  # prudence face à une expulsion massive imminente
            voilure = round(clamp(voilure * facteur_cpfp, 0.0, 100.0), 1)
    return voilure


def determiner_zone(voilure_pct: float) -> Tuple[str, str]:
    """Bandes LISSÉES en pourcent — le seuil ne claque jamais."""
    if voilure_pct >= ZONE_VERT:
        return "VERT", "🟢"
    if voilure_pct >= ZONE_JAUNE:
        return "JAUNE", "🟡"
    return "ROUGE", "🔴"


# ============================================================
# STORY (français, métaphores nature — la tempête = fenêtre aussi)
# ============================================================

def generer_story(zone: str, voilure: float, p: Dict[str, float],
                  seuil_x: float, degraded: bool) -> List[str]:
    v = int(voilure)
    vent = p["storm"] > 0.55
    if zone == "VERT":
        story = [
            f"La voilure tient à {v} % — le bassin est calme, ACE garde sa toile déployée.",
            "Rien ne presse : le Sniper reste en embuscade, l'Éclaireur sonde.",
        ]
    elif zone == "JAUNE":
        story = [
            f"La voilure descend à {v} % — le vent se lève, la pression monte.",
            "Fenêtre encore ouverte, mais l'œil reste sur le ciel : ACE réduit sa toile tout seul.",
        ]
    elif zone == "PRENDS_LA_PERTE":
        story = [
            f"La voilure est au plus bas ({v} %) — le saignement dépasse l'ancrage ({seuil_x:.0f} $) : la perte est prise.",
            "Aucun blocage : ACE reste libre de re-rentrer à la seconde où le mur du carnet parle. La chasse continue.",
        ]
    else:  # ROUGE
        story = [
            f"Tempête en vue — la voilure tombe à {v} %. C'est aussi une fenêtre de plus-value pour ACE en embuscade.",
            "Moins de voilure, même cap : ACE reste libre de tirer dès que l'occasion claque. Aucune attente imposée.",
        ]

    if vent and zone in ("JAUNE", "ROUGE") and len(story) < 3:
        story.append("Le vent forcit — ACE est construit pour ça : marcher dans la tempête.")
    if degraded and len(story) < 3:
        story.append("⚠️ Données de repli (live.json absent ou vieux) — prudence.")
    return story[:3]


# ============================================================
# COUP D'ŒIL (le bloc compact)
# ============================================================

def extraire_verdict_famille(avis: str) -> str:
    if not avis:
        return "pas de verdict récent"
    for line in avis.splitlines():
        line = line.strip()
        if line.startswith("• ") and len(line) > 3:
            return line[:140]
    return "pas de verdict récent"


def construire_coup_doeil(data: Dict, saison: str, voilure: float, zone: str,
                          story: Optional[List[str]] = None) -> Dict[str, str]:
    journal = data.get("journal", {})
    alpha = safe_get(journal, ["bots", "alpha"], {})
    beta = safe_get(journal, ["bots", "beta"], {})
    pnl = float(alpha.get("pnl", 0.0) or 0.0)
    fills = int(alpha.get("fills", 0) or 0)
    revenge = int(alpha.get("revenge", 0) or 0)
    sondes = int(beta.get("fills", 0) or 0)

    intention = "Alpha en observation"
    if fills > 0:
        intention = "Alpha : %d tir%s (%d revenge), pnl %+.2f $" % (
            fills, "s" if fills > 1 else "", revenge, pnl)
    if sondes > 0:
        intention += " · Beta : %d sondes" % sondes

    # 18/08 — Ada voit aussi HULK (lecture seule, depuis mission.json)
    bots = data.get("bots") or {}
    hulk_pnl = bots.get("hulk_pnl")
    hulk_pos = bots.get("hulk_positions")
    if hulk_pnl is not None:
        intention += " · Hulk : pnl %+.2f $ (%d positions)" % (
            float(hulk_pnl), int(hulk_pos or 0))

    saison_emoji = {"CHAUFFE": "🌡️", "MOUVEMENT": "🌀", "CHAOS": "⛈️"}.get(saison, "🌿")
    zone_emoji = {"JAUNE": "🟡", "ROUGE": "🔴", "PRENDS_LA_PERTE": "⛔"}.get(zone, "🟢")

    accroche = ""
    if story:
        accroche = story[0][:110]
    ligne = "%s %s · voilure %d %% · %s %s — %s" % (
        saison, saison_emoji, int(voilure), zone, zone_emoji, accroche)

    return {
        "ts": now_iso(),
        "saison": saison,
        "saison_emoji": saison_emoji,
        "voilure": "%d %%" % int(voilure),
        "zone": zone,
        "zone_emoji": zone_emoji,
        "verdict_famille": extraire_verdict_famille(data.get("avis_famille", "")),
        "intention": intention,
        "ligne": ligne,
    }


# ============================================================
# ÉCRITURE DES SORTIES (atomique, jamais mission.json ici)
# ============================================================

def ecrire_sorties(resultat: Dict, zone_precedente: str) -> None:
    atomic_write_json(GARDIENNE_LIVE, resultat)
    if en_mode_demo():
        # Démo : on ne pollue PAS l'historique d'apprentissage d'ADA
        return
    g = resultat.get("gardienne", {})
    ajouter_historique(g.get("ts", now_iso()),
                       float(g.get("pnl_alpha", 0.0) or 0.0),
                       float(g.get("voilure_pct", 0.0) or 0.0),
                       str(g.get("zone", "VERT")))
    # Archive uniquement au changement de zone (pas de flood)
    if zone_precedente and zone_precedente != g.get("zone"):
        try:
            os.makedirs(HISTORIQUE_DIR, exist_ok=True)
            nom = "gardienne_%s_%s.json" % (
                g.get("zone", "?"), datetime.datetime.utcnow().strftime("%Y%m%d_%H%M"))
            atomic_write_json(os.path.join(HISTORIQUE_DIR, nom), resultat)
        except Exception:
            pass


# ============================================================
# CONSULTATION FAMILLE (aux besoins — jamais en spam, jamais en test)
# ============================================================

def consulter_famille() -> None:
    """Consultation famille NON BLOQUANTE (thread détaché) : le feed ne stalle
    jamais, même si le trio met 4 min. Garde-fou : si la famille a déjà répondu
    il y a moins de 5 min (fichier état), on laisse passer — pas de double."""
    if EN_TEST or en_mode_demo():
        return  # jamais de consultation famille pendant les tests ou la démo
    try:
        if os.path.exists(ETAT_FAMILLE):
            if time.time() - os.path.getmtime(ETAT_FAMILLE) < ANTI_SPAM_MIN * 60:
                return
    except Exception:
        pass
    try:
        import threading

        def _lancer() -> None:
            try:
                import famille_session
                famille_session.consulter()
            except Exception:
                pass

        threading.Thread(target=_lancer, daemon=True).start()
    except Exception:
        pass


# ============================================================
# SCAN PRINCIPAL
# ============================================================

def scan() -> Dict[str, Any]:
    """Orchestration complète. Ne lève jamais d'exception."""
    try:
        data = charger_donnees()
        journal = data.get("journal", {})
        pnl_cur = float(safe_get(journal, ["bots", "alpha", "pnl"], 0.0) or 0.0)
        perte_session = max(0.0, -pnl_cur)

        rows = lire_historique()
        ancres = calculer_ancres(rows, pnl_cur)
        seuil_x = ancres["seuil_x"]

        # état précédent (vitesse du saignement) — logé dans le live précédent
        prev = safe_load_json(GARDIENNE_LIVE, {})
        etat_prev = prev.get("etat", {}) if isinstance(prev, dict) else {}
        pnl_prev = etat_prev.get("pnl")

        p = pressions(data, perte_session, seuil_x, pnl_prev, pnl_cur)
        voilure = calculer_voilure(p, data.get("thermo"))
        zone_name, emoji = determiner_zone(voilure)

        if perte_session >= seuil_x:
            zone_finale = "PRENDS_LA_PERTE"
            emoji_finale = "⛔"
        else:
            zone_finale, emoji_finale = zone_name, emoji

        # LES SIRÈNES d'abord : voie rapide, brute, sans lissage
        sirene, declencheurs = signaux_instantanes(data, pnl_cur, pnl_prev)
        alerte = sirene or zone_finale in ("ROUGE", "PRENDS_LA_PERTE")
        story = generer_story(zone_finale, voilure, p, seuil_x, data["degraded"])
        if sirene:
            story.insert(0, "🚨 FEUX DE L'ORAGE : %s — ADA hurle maintenant, pas après."
                          % ", ".join(declencheurs))

        gardienne = {
            "ts": now_iso(),
            "voilure_pct": int(voilure),
            "zone": zone_finale,
            "zone_emoji": emoji_finale,
            "pressions": p,
            "sirene": sirene,
            "declencheurs": declencheurs,
            "seuil_x": seuil_x,
            "ancres": ancres,
            "alerte": alerte,
            "raison": ("; ".join(declencheurs) + " ; zone " + zone_finale) if alerte else "",
            "pnl_alpha": round(pnl_cur, 2),
            "sources": data["sources"],
            "story": story,
        }
        coup_doeil = construire_coup_doeil(
            data, str(data["saison"].get("saison", "CALME")), voilure, zone_finale, story)

        resultat = {
            "ts": now_iso(),
            "gardienne": gardienne,
            "coup_doeil": coup_doeil,
            "etat": {"pnl": pnl_cur, "ts": now_iso()},
            "zone": zone_finale,
            "voilure": voilure,
            "alerte": alerte,
            "story": story,
        }

        ecrire_sorties(resultat, str(prev.get("gardienne", {}).get("zone", "")))

        if alerte:
            consulter_famille()

        return resultat
    except Exception as e:
        return {"zone": "VERT", "voilure": 75.0, "alerte": False,
                "story": ["ADA en mode observation."],
                "erreur": str(e)}


# ============================================================
# TESTS HERMÉTIQUES (tout en /tmp, jamais la famille)
# ============================================================

def run_tests() -> bool:
    global STRATEGIE_DIR, GARDIENNE_LIVE, HISTORIQUE_DIR, HISTORIQUE_JSONL
    global SAISON_LIVE, JOURNAL_LIVE, THERMO_LIVE, MISSION, AVIS_FAMILLE, EN_TEST

    print("=== Tests hermétiques ada_gardienne ===")
    _sauve = (STRATEGIE_DIR, GARDIENNE_LIVE, HISTORIQUE_DIR, HISTORIQUE_JSONL,
              SAISON_LIVE, JOURNAL_LIVE, THERMO_LIVE, MISSION, AVIS_FAMILLE)
    EN_TEST = True
    tmp = tempfile.mkdtemp(prefix="ada_gardienne_test_")
    STRATEGIE_DIR = tmp
    GARDIENNE_LIVE = os.path.join(tmp, "ada_gardienne_live.json")
    HISTORIQUE_DIR = os.path.join(tmp, "histo")
    HISTORIQUE_JSONL = os.path.join(tmp, "ada_gardienne_historique.jsonl")
    SAISON_LIVE = os.path.join(tmp, "saison.json")
    JOURNAL_LIVE = os.path.join(tmp, "journal.json")
    THERMO_LIVE = os.path.join(tmp, "live.json")
    MISSION = os.path.join(tmp, "mission.json")
    AVIS_FAMILLE = os.path.join(tmp, "avis.md")

    erreurs = 0

    def _restore() -> None:
        global STRATEGIE_DIR, GARDIENNE_LIVE, HISTORIQUE_DIR, HISTORIQUE_JSONL
        global SAISON_LIVE, JOURNAL_LIVE, THERMO_LIVE, MISSION, AVIS_FAMILLE
        (STRATEGIE_DIR, GARDIENNE_LIVE, HISTORIQUE_DIR, HISTORIQUE_JSONL,
         SAISON_LIVE, JOURNAL_LIVE, THERMO_LIVE, MISSION, AVIS_FAMILLE) = _sauve

    def check(nom: str, ok: bool) -> None:
        nonlocal erreurs
        print("  %s %s" % ("✓" if ok else "✗", nom))
        if not ok:
            erreurs += 1

    # -- Test 1 : marché calme, session verte -> VERT, pas d'alerte
    atomic_write_json(SAISON_LIVE, {"saison": "CALME", "direction": "flat", "alignement": 0.5})
    atomic_write_json(JOURNAL_LIVE, {"bots": {"alpha": {"pnl": 12.0, "fills": 3, "revenge": 0},
                                              "beta": {"fills": 5, "conf_moy": 0.9}}})
    atomic_write_json(THERMO_LIVE, {"tsUnix": time.time(), "funding": 0.0001, "chg24": 0.1})
    res = scan()
    check("calme + verte -> VERT", res["zone"] == "VERT" and not res["alerte"])

    # -- Test 2 : régression du bug de zones (voilure 55 % doit être JAUNE, pas VERT)
    z, _ = determiner_zone(55.0)
    check("55% -> JAUNE (bug bornes corrigé)", z == "JAUNE")
    z2, _ = determiner_zone(80.0)
    z3, _ = determiner_zone(30.0)
    check("bornes cohérentes (VERT/JAUNE/ROUGE)", z2 == "VERT" and z3 == "ROUGE")

    # -- Test 3 : lissage monotone (pas de saut brutal)
    v1 = calculer_voilure({"bleed": 0.2, "storm": 0.2, "reversal": 0.1})
    v2 = calculer_voilure({"bleed": 0.9, "storm": 0.9, "reversal": 0.9})
    check("lissage monotone (pression croissante -> voilure décroissante)", v2 < v1)
    check("voilure reste dans 0..100", 0 <= v2 < v1 <= 100)

    # -- Test 4 : seuil X relatif + PRENDS LA PERTE (ADA apprend sa propre normalité)
    for pnl in [10, 5, 0, -10, -12, -8, -14]:
        ajouter_historique(now_iso(), pnl, 60.0, "JAUNE")
    rows = lire_historique()
    ancres = calculer_ancres(rows, -40.0)
    check("ancres relatives calculées", ancres["seuil_x"] > 0 and ancres["perte_moy"] > 0)
    check("perte 40 > seuil relatif (%.1f)" % ancres["seuil_x"], ancres["seuil_x"] < 40.0)

    # -- Test 5 : zone ROUGE -> alerte + raison, famille JAMAIS appelée en test
    atomic_write_json(JOURNAL_LIVE, {"bots": {"alpha": {"pnl": -60.0, "fills": 8, "revenge": 3},
                                              "beta": {"fills": 2}}})
    res5 = scan()
    check("grosse perte -> ROUGE ou PRENDS_LA_PERTE",
          res5["zone"] in ("ROUGE", "PRENDS_LA_PERTE") and res5["alerte"])

    # -- Test 6 : story en français, métaphores nature
    story = res5.get("gardienne", {}).get("story", [])
    txt = " ".join(story).lower()
    check("story française + voilure/tempête", "voilure" in txt and ("tempête" in txt or "saignement" in txt))

    # -- Test 7 : stale guard
    check("live vieux -> est_vieux True", est_vieux({"tsUnix": time.time() - 3 * 3600}))
    check("live frais -> est_vieux False", not est_vieux({"tsUnix": time.time()}))

    # -- Test 8 : coup d'œil porte saison + intention + verdict
    cd = res5.get("coup_doeil", {})
    check("coup d'œil complet", cd.get("saison") and cd.get("intention") and "%" in str(cd.get("voilure")))

    # -- Test 9 : les SIRÈNES sont INSTANTANÉES (pas d'attente de lissage) —
    #    funding 12x sa moyenne doit hurler même si la voilure est encore haute
    atomic_write_json(SAISON_LIVE, {"saison": "CALME", "direction": "flat",
                                    "alignement": {"nb_long": 2, "nb_short": 1,
                                                    "score": 0.33, "direction": "long"},
                                    "bascule": False})
    atomic_write_json(JOURNAL_LIVE, {"bots": {"alpha": {"pnl": 5.0, "fills": 2, "revenge": 0},
                                              "beta": {"fills": 1}}})
    atomic_write_json(THERMO_LIVE, {"tsUnix": time.time(), "funding": 0.0012, "fundingAvg30": 0.0001,
                                    "chg24": 0.1, "liq24Usd": 0.0})
    res9 = scan()
    g9 = res9.get("gardienne", {})
    check("funding 12x sa moyenne -> sirène immédiate (pas de lissage)",
          res9["alerte"] and any("funding" in d for d in g9.get("declencheurs", [])))
    check("sirène dans la story", "FEUX DE L'ORAGE" in " ".join(res9.get("story", [])))

    # -- Test 10 : jamais de langage de blocage dans les stories
    txt10 = " ".join(res5.get("gardienne", {}).get("story", [])).lower()
    check("pas de 'gèle'/'fige' dans les stories", "gèle" not in txt10 and "fige" not in txt10)

    # -- Test 10bis (31/08, GO Christophe) : liquidations SEUIL RELATIF —
    #    un jour normal (53 M$ sans historique 7j -> fallback 50 M$ + plancher
    #    80 M$) ne doit PAS sonner ; un vrai pic (141 M$) doit sonner.
    atomic_write_json(SAISON_LIVE, {"saison": "CALME", "direction": "flat", "bascule": False})
    atomic_write_json(JOURNAL_LIVE, {"bots": {"alpha": {"pnl": 5.0, "fills": 1}, "beta": {}}})
    atomic_write_json(THERMO_LIVE, {"tsUnix": time.time(), "funding": 0.0001, "fundingAvg30": 0.0001,
                                    "chg24": 0.1, "liq24Usd": 53_000_000.0, "fearGreed": 50})
    res10 = scan()
    g10 = res10.get("gardienne", {})
    check("liq 53 M$ (jour normal) -> PAS de sirène liquidations",
          not any("liquidations" in d for d in g10.get("declencheurs", [])))
    atomic_write_json(THERMO_LIVE, {"tsUnix": time.time(), "funding": 0.0001, "fundingAvg30": 0.0001,
                                    "chg24": 0.1, "liq24Usd": 141_000_000.0, "fearGreed": 50})
    res10b = scan()
    g10b = res10b.get("gardienne", {})
    check("liq 141 M$ (vrai pic) -> sirène liquidations massives",
          any("liquidations" in d for d in g10b.get("declencheurs", [])))

    # -- Test 11 : mode démo cockpit (drapeau + données synthétiques)
    import json as _json
    with open(os.path.join(tmp, "ada_demo.flag"), "w", encoding="utf-8") as f:
        _json.dump({"ts": time.time()}, f)
    with open(os.path.join(tmp, "ada_demo_data.json"), "w", encoding="utf-8") as f:
        _json.dump({
            "saison": {"saison": "CHAOS", "direction": "short", "bascule": True,
                       "alignement": {"nb_long": 0, "nb_short": 4, "score": 0.1, "direction": "short"}},
            "journal": {"bots": {"alpha": {"pnl": -120.0, "fills": 12, "revenge": 4},
                                   "beta": {"fills": 3}}},
            "thermo": {"tsUnix": time.time(), "funding": 0.0010, "fundingAvg30": 0.0001,
                        "chg24": 4.0, "liq24Usd": 150000000.0},
        }, f, ensure_ascii=False)
    res11 = scan()
    check("mode démo : données synthétiques prises en compte",
          res11["alerte"] and str(res11.get("gardienne", {}).get("sources", [""])[0]).startswith("démo"))
    os.remove(os.path.join(tmp, "ada_demo.flag"))
    os.remove(os.path.join(tmp, "ada_demo_data.json"))
    res11b = scan()
    check("mode démo retiré -> retour au réel",
          "démo" not in str(res11b.get("gardienne", {}).get("sources", [""])))

    shutil.rmtree(tmp, ignore_errors=True)
    _restore()
    print("=== %s (%d erreur%s) ===" % (
        "TOUS LES TESTS SONT VERTS" if erreurs == 0 else "ÉCHEC",
        erreurs, "s" if erreurs > 1 else ""))
    return erreurs == 0


# ============================================================
# MAIN
# ============================================================

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--story", action="store_true")
    args = parser.parse_args()

    if args.test:
        return 0 if run_tests() else 1
    if args.story:
        res = scan()
        for ligne in res.get("story", []):
            print(ligne)
        return 0
    res = scan()
    print("ADA Gardienne → Zone: %s | Voilure: %s%% | Alerte: %s"
          % (res["zone"], int(res["voilure"]), res["alerte"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
