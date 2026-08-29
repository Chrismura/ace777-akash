#!/usr/bin/env python3
"""
silent_drain_index.py — SDI (Silent Drain Index) + IPT (Indice de Pression Topologique)
Détecte les mouvements silencieux de baleines via :
  1. SDI : divergence BTC dormant (>1 an) vs frais payés par adresses <30 jours
  2. IPT : ratio micro-tx × z-score frais × entropie scripts

Auteur : Ace (Index Maison)
Version : 2.0 (fix API 404)
Date : 2026-08-25
"""

import json
import os
import statistics
import tempfile
import time
import urllib.request
from pathlib import Path
import math
from datetime import datetime, timezone

DATA_DIR = Path(__file__).parent.parent / "data"
LIVE_FILE = DATA_DIR / "live.json"
SDI_OUTPUT = DATA_DIR / "sdi_latest.json"

# PathRegistry (FIX famille n°4) : valide les chemins au démarrage avant tout
# calcul. Le sapi_etat.json est recréé au 1er run (donc non bloquant), mais
# les chemins obligatoires (script, murs_observations) doivent exister.
try:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    import path_registry as _pr
    _pr.verifier("sapi")
except ImportError:
    pass

# ─── Corrections famille (29/08 soir, GO Christophe) ────────────
# État SAPI : historique du spread BTC (normalisation σ1h) + scores
# (persistance 3 ticks avant alerte). Fichier d'état atomique.
SAPI_ETAT = DATA_DIR / "sapi_etat.json"
SAPI_HISTO_SPREAD_MAX = 12   # 12 × 5 min ≈ 1h de fenêtre σ
SAPI_PERSISTANCE_TICKS = 3   # 3 runs consécutifs ≥ seuil avant alerte
SAPI_SEUIL_ALERTE = 0.75
SAPI_VOLAT_K = 3.0           # normalisation : |Δspread| / (σ1h × K)

# FIX famille n°4 (29/08 suite GO) — proxy carnet / poussière affinés :
# - Heures creuses UTC (02-06) : le spread s'élargit naturellement (peu de MM).
#   Le proxy ne doit pas confondre un manque de liquidité légitime avec de la
#   poussière institutionnelle → poids du proxy réduit en heures creuses.
HEURE_CREUSE_DEBUT: int = 2
HEURE_CREUSE_FIN: int = 5          # inclusif
COEFF_PROXY_CREUSE: float = 0.35   # en heures creuses le proxy ne compte que ×0.35

# - Entropie temporelle : régularité quasi-robotique du CARNET. Une poussière
#   institutionnelle (script) laisse le carnet à un spread/cadence suspectement
#   stable (CV très bas), vs le chaos retail (CV élevé). On stocke l'historique
#   du taux_fantome et on ajoute un bonus SAPI si le rythme est régulier.
SAPI_ENTROPIE_MAX = 12
SAPI_CV_REGULIER: float = 0.15     # CV ≤ 15 % = rythme quasi-robotique


def _ecriture_atomique(path, donnees):
    """Écrit un JSON de façon atomique (.tmp + os.replace). FIX famille —
    fin des fichiers tronqués en cas de crash en pleine écriture."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(donnees, fh, ensure_ascii=False, indent=2)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def _charger_sapi_etat():
    """Charge l'état SAPI (historique spread + scores). Fail-open."""
    try:
        if SAPI_ETAT.exists():
            return json.loads(SAPI_ETAT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
    return {"spreads": [], "scores": []}


def _sauver_sapi_etat(etat):
    """Sauvegarde l'état SAPI en écriture atomique. Fail-open silencieux."""
    try:
        _ecriture_atomique(SAPI_ETAT, etat)
    except OSError:
        pass


def _normaliser_par_volatilite(spread_abs, historique):
    """Normalisation σ1h (FIX famille) : z = |Δspread| / (σ1h × K), borné [0,1].
    Si le spread bouge parce que le carnet est VIDE (σ1h élevé), le diviseur
    neutralise le faux positif. Historique insuffisant (< 3) → pas de
    normalisation (retourne le brut borné, comportement d'avant).
    """
    brut = min(1.0, spread_abs / 100.0)
    if len(historique) < 3:
        return brut
    sigma = statistics.stdev(historique)
    if sigma <= 0.0:
        return brut
    return min(1.0, spread_abs / (sigma * SAPI_VOLAT_K))


def _en_heure_creuse(dt_utc=None) -> bool:
    """Vrai si l'heure UTC est dans [HEURE_CREUSE_DEBUT, HEURE_CREUSE_FIN].
    Fenêtre simple (début ≤ fin), cf. 02-06."""
    heure = (dt_utc or datetime.now(timezone.utc)).hour
    return HEURE_CREUSE_DEBUT <= heure <= HEURE_CREUSE_FIN


def _taux_entropie_temporelle(serie) -> float:
    """Entropie temporelle du rythme de poussière : retourne 1.0 si la série
    est quasi-constante (un script robotique), 0.0 si c'est du chaos.
    CV = stdev / mean ; CV ≤ SAPI_CV_REGULIER → rythme régulier (bonus poussière).
    Fail-open : < 3 points ou mean ~ 0 → 0.0 (pas de base pour juger)."""
    serie = [float(v) for v in (serie or [])]
    if len(serie) < 3:
        return 0.0
    m = sum(serie) / len(serie)
    if m <= 0.0:
        return 0.0
    sigma = statistics.stdev(serie) if len(serie) >= 2 else 0.0
    cv = sigma / m
    if cv <= SAPI_CV_REGULIER:
        return 1.0
    # Dégradé : plus le CV est faible, plus le rythme est suspect de robotique.
    return max(0.0, min(1.0, (1.0 - cv) * 1.4))


def _coef_proxy_heure_creuse() -> float:
    """Poids du proxy carnet : 1.0 en session, COEFF_PROXY_CREUSE en heures
    creuses UTC (le spread s'élargit naturellement sans MM)."""
    return COEFF_PROXY_CREUSE if _en_heure_creuse() else 1.0

# ─── Fetch helpers ──────────────────────────────────────────────

def fetch_json(url, timeout=8):
    """Fetch JSON depuis une URL"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Ace-SDI/2.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  [SDI] fetch error {url}: {e}")
        return None

# ─── SDI Calculation ───────────────────────────────────────────

def get_btc_dormant():
    """
    Récupère le pourcentage de BTC dormant >1 an via Blockchain.com
    Alternative: utiliser l'API supply-still-never-been-spent
    """
    # Source 1: utxo-pool-value (peut être indisponible)
    url = "https://api.blockchain.info/charts/utxo-pool-value?timespan=30days&format=json"
    data = fetch_json(url)
    
    if data and "values" in data:
        values = [v["y"] for v in data["values"]]
        if len(values) >= 2:
            current = values[-1]
            avg_30d = sum(values) / len(values)
            return {
                "current_pct": round(current, 2),
                "avg_30d_pct": round(avg_30d, 2),
                "divergence_pct": round(((current - avg_30d) / avg_30d) * 100, 2) if avg_30d > 0 else 0,
                "source": "blockchain.com"
            }
    
    # Source 2: alternative.me (fear & greed comme proxy)
    # FIX 28/08 : renommé dormant_pct → fg_sentiment_pct pour dire la vérité.
    # blockchain.info/utxo-pool-value renvoie 404. Le FG est un PROXY raisonnable :
    # FG bas = peur = holders pressés = activité dormant accrue. Pas parfait mais
    # honnête (le label « dormant_pct » sur un indice FG était trompeur).
    url2 = "https://api.alternative.me/fng/?limit=30&format=json"
    data2 = fetch_json(url2)
    if data2 and "data" in data2:
        fg_values = [int(d["value"]) for d in data2["data"]]
        current_fg = fg_values[0] if fg_values else 50
        avg_fg = sum(fg_values) / len(fg_values) if fg_values else 50

        # FG bas vs moyenne = peur accrue = holders pressés = potentiel drain
        divergence = ((current_fg - avg_fg) / avg_fg) * 100 if avg_fg > 0 else 0

        return {
            "fg_sentiment_pct": current_fg,
            "fg_avg_30d_pct": round(avg_fg, 2),
            "divergence_pct": round(-divergence, 2),
            "source": "alternative.me (FG proxy — les données dormant sont indisponibles)"
        }
    
    return None

def get_fee_pressure():
    """Récupère la pression des frais — RÈGLE DES 2 SOURCES (29/08, protocole
    croisement externe Christophe) : mempool.space en PRIORITÉ, fallback
    blockstream.info si mempool est down (prouvé 29/08 : mempool down 6h+
    → SDI/IPT/RBF (la pépite Cortana) restaient figés). Fail-open : les deux
    down = None (le pipeline complet s'arrête proprement)."""
    # Source 1 : mempool.space (format fastestFee/halfHourFee/hourFee/economyFee)
    data = fetch_json("https://mempool.space/api/v1/fees/recommended")
    if data:
        return {
            "fastest": data.get("fastestFee", 0),
            "halfHour": data.get("halfHourFee", 0),
            "hour": data.get("hourFee", 0),
            "economy": data.get("economyFee", 0),
            "source": "mempool.space",
        }
    # Source 2 : blockstream.info (format {blocs: sat/vB} — 1, 2, 3, 6, 10 blocs)
    data2 = fetch_json("https://blockstream.info/api/fee-estimates")
    if data2:
        def _v(k):
            try:
                return max(1, round(float(data2.get(str(k), 0))))
            except Exception:
                return 1
        return {
            "fastest": _v(2),      # ~10 min
            "halfHour": _v(6),     # ~30 min
            "hour": _v(12),        # ~60 min
            "economy": _v(24),      # ~2h
            "source": "blockstream.info (fallback)",
        }
    return None

def get_dormant_surge(fee_pressure):
    """
    SDI = divergence des BTC dormant × pression des frais
    Si les vieux BTC bougent + frais montent = drainage silencieux
    """
    dormant = get_btc_dormant()
    if not dormant or not fee_pressure:
        return None
    
    # Score de divergence (>2% = suspect, >5% = alarme)
    div = dormant["divergence_pct"]
    if div > 5:
        div_score = 1.0
    elif div > 2:
        div_score = 0.5 + (div - 2) * 0.17
    else:
        div_score = max(0, div * 0.1)
    
    # Score de frais (fastest > 50 sat/vB = pression élevée)
    fee = fee_pressure["fastest"]
    if fee > 50:
        fee_score = 1.0
    elif fee > 20:
        fee_score = 0.5 + (fee - 20) * 0.017
    else:
        fee_score = max(0, fee * 0.01)
    
    # SDI composite (0-1)
    sdi = round((div_score * 0.6 + fee_score * 0.4), 3)
    
    return {
        "sdi": sdi,
        "divergence_score": round(div_score, 3),
        "fee_score": round(fee_score, 3),
        "dormant_pct": dormant.get("current_pct") or dormant.get("fg_sentiment_pct"),
        "dormant_avg_30d": dormant.get("avg_30d_pct") or dormant.get("fg_avg_30d_pct"),
        "dormant_source": dormant.get("source", "unknown"),
        "fee_fastest_sat": fee
    }

# ─── IPT Calculation (INFERX) ──────────────────────────────────

def get_mempool_entropy():
    """
    Entropie de la mempool : diversité des scripts × variance des frais
    Plus l'entropie est basse = un seul acteur automatisé
    """
    # Récupérer les dernières transactions
    url = "https://mempool.space/api/mempool/recent"
    txs = fetch_json(url)
    if not txs or len(txs) < 10:
        return None
    
    # Variance des fees
    fees = [tx.get("fee", 0) / tx.get("vsize", 1) for tx in txs if tx.get("vsize", 0) > 0]
    if not fees:
        return None
    
    mean_fee = sum(fees) / len(fees)
    variance = sum((f - mean_fee) ** 2 for f in fees) / len(fees)
    std_fee = math.sqrt(variance) if variance > 0 else 0
    
    # Coefficient de variation (inverse de l'entropie)
    cv = std_fee / mean_fee if mean_fee > 0 else 0
    
    # Entropie (1 - cv normalisé)
    entropy = max(0, min(1, 1 - cv))
    
    return {
        "entropy": round(entropy, 3),
        "cv": round(cv, 3),
        "n_txs": len(txs)
    }

def get_ipt(mempool_entropy, fee_pressure):
    """
    IPT = (micro-tx volume / total) × z-score frais × entropie
    Si entropie chute + micro-tx montent = un seul acteur automatisé
    """
    if not mempool_entropy or not fee_pressure:
        return None
    
    # Micro-tx ratio (txs < 1000 sat)
    url = "https://mempool.space/api/mempool/recent"
    txs = fetch_json(url)
    if not txs:
        return None
    
    micro_count = sum(1 for tx in txs if tx.get("value", 0) < 100000)  # < 0.001 BTC
    micro_ratio = micro_count / len(txs) if txs else 0
    
    # Z-score frais (fastest vs médiane)
    fee = fee_pressure["fastest"]
    median_fee = fee_pressure.get("hour", 1)
    z_fee = (fee - median_fee) / median_fee if median_fee > 0 else 0
    
    # IPT composite
    ipt = round((micro_ratio * 0.4 + max(0, z_fee) * 0.3 + mempool_entropy["entropy"] * 0.3), 3)
    
    return {
        "ipt": ipt,
        "micro_tx_ratio": round(micro_ratio, 3),
        "z_fee": round(z_fee, 3),
        "entropy": mempool_entropy["entropy"]
    }

# ─── RBF Analytics (Replace-By-Fee) ───────────────────

def get_rbf_analytics():
    """
    Détecte le RBF (Replace-By-Fee) RÉEL : les DOUBLES DÉPENSES.
    FIX 28/08 v2 (GO Christophe « approfondis, tu fais erreur » — il avait raison) :
    l'ancienne méthode (flag nSequence < 0xfffffffe, BIP 125) mesurait la CAPACITÉ
    RBF — la plupart des wallets modernes l'activent par défaut → score bloqué à
    1.0 en permanence (faux positif structurel, vérifié en direct : 80% des tx
    récentes ont le flag alors que 0/3 ont une vraie double dépense).
    La VRAIE détection : un UTXO d'entrée dépensé par DEUX tx différentes dans la
    mempool = une tx a remplacé l'autre (même input, frais plus hauts). Via
    /api/tx/{parent}/outspends : si l'output est spent par un txid ≠ la tx courante
    → double dépense = RBF réel.
    Coût : ~6 appels tx/{txid} + outspends cachés (~8-12 appels/cycle, ~10s),
    rate-limit mempool.space respecté (sleep 0.5s). Fail-open : injoignable = non RBF.
    """
    url_recent = "https://mempool.space/api/mempool/recent"
    txs = fetch_json(url_recent)
    if not txs or len(txs) < 5:
        return None

    rbf_count = 0
    checked = 0
    outspends_cache = {}  # parent_txid -> liste outspends (évite les appels en double)
    rbf_detail = []
    for tx in txs[:6]:  # borné à 6 (rate-limit + budget API)
        txid = tx.get("txid")
        if not txid:
            continue
        try:
            detail_url = "https://mempool.space/api/tx/%s" % txid
            detail = fetch_json(detail_url, timeout=4)
            if not detail:
                continue
            checked += 1
            vin = detail.get("vin", []) or []
            is_rbf = False
            for v in vin[:3]:  # 3 premiers inputs suffisent (souvent 1 seul)
                parent_txid = v.get("txid")
                parent_vout = v.get("vout")
                if not parent_txid or parent_vout is None:
                    continue
                if parent_txid not in outspends_cache:
                    outs_url = "https://mempool.space/api/tx/%s/outspends" % parent_txid
                    outspends_cache[parent_txid] = fetch_json(outs_url, timeout=4)
                    time.sleep(0.5)
                outs = outspends_cache.get(parent_txid) or []
                if parent_vout < len(outs) and outs[parent_vout]:
                    spent_by = outs[parent_vout].get("txid")
                    # L'UTXO est dépensé par UNE AUTRE tx = remplacement réel
                    if spent_by and spent_by != txid:
                        is_rbf = True
                        rbf_detail.append({
                            "tx": txid[:16],
                            "remplacee_par": spent_by[:16],
                            "input": "%s:%d" % (parent_txid[:16], parent_vout),
                        })
                        break
            if is_rbf:
                rbf_count += 1
            time.sleep(0.5)  # rate-limit respectueux
        except Exception:
            continue  # fail-open : tx injoignable = non RBF

    rbf_ratio = rbf_count / max(checked, 1)
    rbf_score = round(rbf_ratio, 3)  # échelle honnête : ratio direct, plus de ×5 saturant

    return {
        "rbf_score": rbf_score,
        "rbf_ratio": round(rbf_ratio, 3),
        "rbf_pairs": rbf_count,
        "n_txs": checked,
        "rbf_method": "outspends-double-depense",
        "rbf_detail": rbf_detail,
    }

# ─── Main ──────────────────────────────────────────────────────

def compute_sdi():
    """Calcule le SDI, IPT et RBF, sauvegarde dans sdi_latest.json"""
    print("[SDI] Calcul en cours...")
    
    # 1. Fee pressure
    fee_pressure = get_fee_pressure()
    if not fee_pressure:
        print("[SDI] Erreur: impossible de récupérer les frais")
        return None
    
    # 2. SDI
    sdi_result = get_dormant_surge(fee_pressure)
    
    # 3. Mempool entropy
    mempool_entropy = get_mempool_entropy()
    
    # 4. IPT
    ipt_result = get_ipt(mempool_entropy, fee_pressure)
    
    # 5. RBF Analytics
    rbf_result = get_rbf_analytics()
    
    # 5bis. SAPI — Score d'Alerte Poussière Institutionnelle (29/08, GO Christophe)
    # Formule Cortana (session poussiere-20260829-152854, tour 1), validée par nos
    # données (corr micro_tx/RBF = −0.275 sur 13 933 points). Intégration par le
    # codeur (minimax-m3/Gemini), CORRIGÉE par supervision Buffy (FIX 1 : chemin
    # murs_observations, FIX 2 : clé top_murs[pair] et non top_murs[paire]).
    def _integrer_sapi(result: dict, data_dir: Path) -> None:
        """Calcule et injecte le SAPI, avec fail-open total."""
        try:
            ipt_result = result.get("ipt", {}) or {}
            z_fee = float(ipt_result.get("z_fee", 0.0) or 0.0)
            micro_tx_ratio = float(ipt_result.get("micro_tx_ratio", 0.0) or 0.0)

            # 2. bloc_privatise.json (taux_fantome + volume_btc)
            taux_fantome = 0.0
            volume_btc = 0.0
            bloc_path = data_dir / "bloc_privatise.json"
            if bloc_path.exists():
                try:
                    bloc_data = json.loads(bloc_path.read_text(encoding="utf-8"))
                    taux_fantome = float(bloc_data.get("taux_fantome", 0.0) or 0.0)
                    volume_btc = float(bloc_data.get("volume_btc", 0.0) or 0.0)
                except Exception:
                    pass

            # 3. Proxy carnet spot : spread_avg_bps BTCUSDT depuis murs_observations.json
            # FIX 1 (supervision) : data_dir = Index_Maison/data → il faut remonter
            # DEUX niveaux (data_dir.parent.parent = ace777-test-day1) pour atteindre
            # hulk-mexc. Le chemin du codeur (data_dir.parent/hulk-mexc) était FAUX.
            # FIX famille : normalisation σ1h — si le spread bouge parce que le
            # carnet est vide, le diviseur σ1h neutralise le faux positif.
            spot_proxy = 0.0
            spread_abs = 0.0
            murs_path = data_dir.parent.parent / "hulk-mexc" / "runs" / "murs_observations.json"
            if murs_path.exists():
                try:
                    murs_data = json.loads(murs_path.read_text(encoding="utf-8"))
                    top_murs = murs_data.get("top_murs") or []
                    # FIX 2 (supervision) : top_murs est une LISTE de dicts avec la
                    # clé "pair" (le codeur cherchait "paire" → jamais trouvé).
                    spread_avg_bps = 0.0
                    for item in top_murs:
                        if isinstance(item, dict) and item.get("pair") == "BTCUSDT":
                            spread_avg_bps = float(item.get("spread_avg_bps", 0.0) or 0.0)
                            break
                    spread_abs = abs(spread_avg_bps)
                except Exception:
                    pass

            # 3bis. État SAPI : historique spread (σ1h) + taux_fantome
            # (entropie temporelle) + scores (persistance 3 ticks)
            etat = _charger_sapi_etat()
            spreads = list(etat.get("spreads", []))
            spreads.append(spread_abs)
            spreads = spreads[-SAPI_HISTO_SPREAD_MAX:]
            spot_proxy = _normaliser_par_volatilite(spread_abs, spreads)

            # FIX famille n°4 : heures creuses UTC — le spread s'élargit
            # naturellement sans MM, on réduit le poids du proxy pour ne pas
            # confondre manque de liquidité légitime avec de la poussière.
            coef_creuse = _coef_proxy_heure_creuse()
            spot_proxy = spot_proxy * coef_creuse

            # FIX famille n°4 : entropie temporelle — une poussière
            # institutionnelle = un script qui laisse le carnet à un rythme
            # suspectement régulier (CV très bas). Historique taux_fantome.
            fantomes = list(etat.get("fantomes", []))
            fantomes.append(taux_fantome)
            fantomes = fantomes[-SAPI_ENTROPIE_MAX:]
            temp_entropie = _taux_entropie_temporelle(fantomes)

            # 4. Formule SAPI (avec les 2 nouveaux termes famille n°4)
            term_z_fee = 0.35 if z_fee > 2.0 else 0.0
            term_fantome = min(1.0, taux_fantome / 0.15) * 0.30
            term_micro = 0.20 if micro_tx_ratio > 0.5 else 0.0
            term_spot = min(1.0, spot_proxy * 10.0) * 0.15
            # Bonus entropie temporelle : +0.10 max si rythme robotique ET déjà
            # une base fantôme détectée (évite un bonus seul déclencheur).
            bonus_entropie = 0.10 * temp_entropie if term_fantome > 0.05 else 0.0
            sapi = max(0.0, min(1.0, term_z_fee + term_fantome + term_micro
                                + bonus_entropie - term_spot))

            # 4bis. Persistance 3 ticks (FIX famille) : l'alerte ne s'allume que si
            # les SAPI_PERSISTANCE_TICKS derniers runs sont ≥ seuil. Tue les faux
            # positifs isolés (pic de cotation, micro-lag réseau).
            scores = list(etat.get("scores", []))
            scores.append(round(sapi, 3))
            scores = scores[-SAPI_PERSISTANCE_TICKS:]
            persistance = all(s >= SAPI_SEUIL_ALERTE for s in scores)
            _sauver_sapi_etat({"spreads": spreads, "scores": scores,
                               "fantomes": fantomes})

            alerte_sapi = bool(persistance and sapi >= SAPI_SEUIL_ALERTE and volume_btc >= 500)
            result["sapi"] = {
                "score": round(sapi, 3),
                "alerte": alerte_sapi,
                "persistance": persistance,
                "scores_recents": scores,
                "composantes": {
                    "z_fee": round(z_fee, 3),
                    "taux_fantome": round(taux_fantome, 3),
                    "micro_tx_ratio": round(micro_tx_ratio, 3),
                    "spot_proxy": round(spot_proxy, 3),
                    "coef_heure_creuse": coef_creuse,
                    "entropie_tempo": round(temp_entropie, 3),
                },
                "note": "Score d'Alerte Poussière Institutionnelle (Cortana tour 1, validé 29/08 — corr RBF plat −0.275). Proxy carnet spot = spread_avg_bps normalisé σ1h (FIX famille). FIX 4 : proxy réduit ×0.35 en heures creuses UTC (02-06) + bonus entropie temporelle (rythme robotique du carnet) si base fantôme. Alerte = persistance 3 ticks ≥ 0.75 + volume ≥ 500 BTC.",
            }
            if alerte_sapi:
                msg = "SAPI ÉLEVÉ: poussière institutionnelle probable (score ≥ 0.75 sur 3 ticks + volume)"
                if msg not in result.get("alerts", []):
                    result.setdefault("alerts", []).append(msg)
        except Exception as e:
            result["sapi"] = {
                "score": 0.0, "alerte": False,
                "composantes": {"z_fee": 0.0, "taux_fantome": 0.0,
                                 "micro_tx_ratio": 0.0, "spot_proxy": 0.0},
                "note": f"Erreur calcul SAPI (fail-open): {str(e)}",
            }

    # 6. Assemblage
    result = {
        "timestamp": int(time.time()),
        "sdi": sdi_result,
        "ipt": ipt_result,
        "rbf": rbf_result,
        "fee_pressure": fee_pressure,
        "alerts": []
    }
    _integrer_sapi(result, DATA_DIR)
    
    # 7. Alertes
    if sdi_result and sdi_result["sdi"] > 0.7:
        result["alerts"].append("SDI ÉLEVÉ: drainage silencieux probable")
    if ipt_result and ipt_result["ipt"] > 0.8:
        result["alerts"].append("IPT ÉLEVÉ: un seul acteur automatisé détecté")
    if mempool_entropy and mempool_entropy["entropy"] < 0.3:
        result["alerts"].append("ENTROPIE BASSE: mempool anormalement homogène")
    if rbf_result and rbf_result["rbf_score"] > 0.6:
        result["alerts"].append("RBF ÉLEVÉ: remplacements de frais détectés = urgence")
    
    # 8. Sauvegarde (atomique — FIX famille)
    try:
        _ecriture_atomique(SDI_OUTPUT, result)
    except OSError as exc:
        print(f"[SDI] ERREUR ecriture {SDI_OUTPUT}: {exc}")
        return None
    
    sdi_val = sdi_result['sdi'] if sdi_result else 'N/A'
    ipt_val = ipt_result['ipt'] if ipt_result else 'N/A'
    rbf_val = rbf_result['rbf_score'] if rbf_result else 'N/A'
    print(f"[SDI] SDI={sdi_val} | IPT={ipt_val} | RBF={rbf_val} | Alertes={len(result['alerts'])}")
    
    return result

if __name__ == "__main__":
    compute_sdi()
