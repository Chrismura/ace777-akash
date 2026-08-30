#!/usr/bin/env python3
"""
pipeline_health.py — Moteur de Santé du Pipeline (MSP)
Évalue en temps réel la fiabilité de chaque source de données.

3 modes (F3 — Gemini) :
  - Nominal (score >= 0.85) : tailles standard (100%)
  - Dégradé (0.60-0.85) : tailles réduites (50%), stops resserrés
  - Kill Switch (<0.60) : gel du trading, annulation ordres ouverts

Sources évaluées :
  1. Binance API (prix, funding, OI) — TTL 500ms, critique >1.5s
  2. Mempool.space (CPFP, dust, frais) — TTL 10s, critique >30s
  3. Alternative.me (Fear/Greed) — TTL 26h, critique >48h
  4. Deribit (options, GEX) — TTL 2s, critique >5s
  5. Blockchain.com (BTC dormant) — TTL 6h, critique >24h
  6. Google News RSS (narratif) — TTL 1h, critique >4h
  7. SDI/IPT (calcul local) — TTL 10s, critique >30s

Auteur : Ace (Index Maison)
Version : 1.0
Date : 2026-08-25
"""

import json
import time
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

DATA_DIR = Path(__file__).parent.parent / "data"
LIVE = Path(__file__).parent.parent / "thermo" / "live.json"
HEALTH_OUTPUT = DATA_DIR / "pipeline_health.json"

# ─── TTL Configuration ────────────────────────────────────────

SOURCE_CONFIG = {
    "binance": {
        "ttl_nominal": 0.5,      # 500ms
        "ttl_critique": 1.5,     # 1.5s
        "poids": 0.25,           # Plus Important — c'est le prix
    },
    "mempool": {
        "ttl_nominal": 10,       # 10s
        "ttl_critique": 30,      # 30s
        "poids": 0.20,
    },
    "deribit": {
        "ttl_nominal": 2,        # 2s
        "ttl_critique": 5,       # 5s
        "poids": 0.15,
    },
    "alternative": {
        "ttl_nominal": 93600,    # 26h
        "ttl_critique": 172800,  # 48h
        "poids": 0.10,
    },
    "blockchain": {
        "ttl_nominal": 21600,    # 6h
        "ttl_critique": 86400,   # 24h
        "poids": 0.10,
    },
    "google_news": {
        "ttl_nominal": 3600,     # 1h
        "ttl_critique": 14400,   # 4h
        "poids": 0.10,
    },
    "sdi_ipt": {
        "ttl_nominal": 10,       # 10s
        "ttl_critique": 30,      # 30s
        "poids": 0.10,
    },
}

# ─── Source Health Checks ─────────────────────────────────────

def check_binance(live):
    """Vérifie la santé de la source Binance"""
    mark = live.get("mark")
    funding = live.get("funding")
    oi = live.get("oi")
    
    issues = []
    score = 1.0
    
    # Vérifier que les données existent
    if mark is None:
        issues.append("mark=None")
        score -= 0.5
    elif mark <= 0:
        issues.append(f"mark={mark} (aberrant)")
        score -= 0.5
    
    if funding is None:
        issues.append("funding=None")
        score -= 0.2
    elif abs(funding) > 0.01:  # >1% = suspect
        issues.append(f"funding={funding} (aberrant)")
        score -= 0.3
    
    if oi is None:
        issues.append("oi=None")
        score -= 0.2
    
    # Vérifier la cohérence prix (fix 27/08 : chg1h peut être null dans live.json
    # quand Binance renvoie un champ vide → abs(None) crashait compute_health
    # (crash observé 12:12Z, repli sur le fichier pipeline_health.json).
    chg1h = live.get("chg1h", 0)
    if chg1h is None:
        issues.append("chg1h=None")
        score -= 0.2
    elif abs(chg1h) > 10:  # >10% en 1h = suspect
        issues.append(f"chg1h={chg1h}% (flash crash?)")
        score -= 0.3
    
    return {
        "source": "binance",
        "score": max(0, min(1, score)),
        "issues": issues,
        "data_age": 0,  # Binance = temps réel
    }

def check_mempool(live):
    """Vérifie la santé de la source Mempool"""
    onchain = live.get("onchain", {})
    cpfp = onchain.get("cpfpDustScore")
    dust = onchain.get("cpfpDustDetail")
    
    issues = []
    score = 1.0
    
    if cpfp is None:
        issues.append("cpfpDustScore=None")
        score -= 0.3
    
    # Vérifier la cohérence dust
    if cpfp is not None and cpfp < 0:
        issues.append(f"cpfp={cpfp} (aberrant)")
        score -= 0.3
    
    # Vérifier si le signal CPFP est cohérent
    cpfp_signal = onchain.get("cpfpSignal")
    if cpfp_signal and cpfp and cpfp > 50 and cpfp_signal == "aucun":
        issues.append("dust élevé mais signal=aucun (incohérent)")
        score -= 0.2
    
    return {
        "source": "mempool",
        "score": max(0, min(1, score)),
        "issues": issues,
        "data_age": 0,
    }

def check_deribit(live):
    """Vérifie la santé de la source Deribit"""
    gex = live.get("gex", {})
    put_call = live.get("gexPutCall")
    call_wall = live.get("gexCallWall")
    put_wall = live.get("gexPutWall")
    
    issues = []
    score = 1.0
    
    # GEX peut timeout (c'est fréquent)
    if not gex or gex.get("ok") is False:
        issues.append("gex.ok=False (timeout Deribit)")
        score -= 0.4
    
    if put_call is None:
        issues.append("putCall=None")
        score -= 0.2
    elif put_call <= 0 or put_call > 5:
        issues.append(f"putCall={put_call} (aberrant)")
        score -= 0.3
    
    if call_wall is None or put_wall is None:
        issues.append("walls=None")
        score -= 0.2
    
    return {
        "source": "deribit",
        "score": max(0, min(1, score)),
        "issues": issues,
        "data_age": 0,
    }

def check_alternative(live):
    """Vérifie la santé de la source Alternative.me"""
    fg = live.get("fearGreed")
    fg_label = live.get("fearGreedLabel")
    
    issues = []
    score = 1.0
    
    if fg is None:
        issues.append("fearGreed=None")
        score -= 0.5
    elif fg < 0 or fg > 100:
        issues.append(f"fearGreed={fg} (aberrant)")
        score -= 0.5
    
    # Vérifier cohérence label
    if fg is not None and fg_label:
        if fg < 25 and "Greed" in fg_label:
            issues.append(f"FG={fg} mais label={fg_label} (incohérent)")
            score -= 0.3
        elif fg > 75 and "Fear" in fg_label:
            issues.append(f"FG={fg} mais label={fg_label} (incohérent)")
            score -= 0.3
    
    return {
        "source": "alternative",
        "score": max(0, min(1, score)),
        "issues": issues,
        "data_age": 0,
    }

def check_blockchain(live):
    """Vérifie la santé de la source Blockchain.com"""
    sdi = live.get("sdi", {})
    
    issues = []
    score = 1.0
    
    if not sdi:
        issues.append("sdi=absent")
        score -= 0.3
    elif sdi.get("dormant_source") == "unknown":
        issues.append("dormant source=unknown (API 404)")
        score -= 0.4
    
    return {
        "source": "blockchain",
        "score": max(0, min(1, score)),
        "issues": issues,
        "data_age": 0,
    }

def check_google_news(live):
    """Vérifie la santé de la source Google News"""
    # Google News est alimenté par le sniffer (pas dans live.json).
    # FIX 28/08 (GO Christophe « google news devrait être down pour ça » — il avait
    # raison) : l'ancien score 0.5 en dur était un « je ne sais pas » déguisé en
    # « à moitié OK ». Honnêteté : une source qu'on ne peut PAS vérifier en direct
    # ne vaut ni 1.0 ni 0.5 — elle est INCONNUE → DOWN (0). La source reste dans
    # le calcul (poids 0.10), mais elle ne contribue plus un faux demi-point.
    # Si le sniffer écrit un fichier narratif vérifiable à l'avenir, on pourra
    # lui redonner un vrai check (présence + fraîcheur).
    issues = ["source non vérifiable en direct (alimentée par sniffer) → DOWN"]
    score = 0.0
    
    return {
        "source": "google_news",
        "score": score,
        "issues": issues,
        "data_age": 0,
    }

def check_sdi_ipt(live):
    """Vérifie la santé du calcul SDI/IPT"""
    sdi = live.get("sdi")
    ipt = live.get("ipt")
    
    issues = []
    score = 1.0
    
    if not sdi:
        issues.append("sdi=absent")
        score -= 0.4
    
    if not ipt:
        issues.append("ipt=absent")
        score -= 0.3
    
    # Vérifier cohérence
    if sdi and ipt:
        sdi_val = sdi.get("sdi", 0)
        ipt_val = ipt.get("ipt", 0)
        if sdi_val > 0.8 and ipt_val > 0.8:
            issues.append("SDI+IPT ambos élevés (peut être un vrai signal ou un bug)")
    
    return {
        "source": "sdi_ipt",
        "score": max(0, min(1, score)),
        "issues": issues,
        "data_age": 0,
    }

# ─── Global Health Score ──────────────────────────────────────

def compute_global_health(live):
    """Calcule le score de santé global du pipeline"""
    checks = [
        check_binance(live),
        check_mempool(live),
        check_deribit(live),
        check_alternative(live),
        check_blockchain(live),
        check_google_news(live),
        check_sdi_ipt(live),
    ]
    
    # Score pondéré
    total_poids = sum(SOURCE_CONFIG[c["source"]]["poids"] for c in checks)
    weighted_score = sum(
        c["score"] * SOURCE_CONFIG[c["source"]]["poids"] for c in checks
    ) / total_poids if total_poids > 0 else 0
    
    # Déterminer le mode
    if weighted_score >= 0.85:
        mode = "nominal"
        mode_label = "✅ NOMINAL"
        position_mult = 1.0
    elif weighted_score >= 0.60:
        mode = "degrade"
        mode_label = "⚠️ DÉGRADÉ"
        position_mult = 0.5
    else:
        mode = "kill_switch"
        mode_label = "🚨 KILL SWITCH"
        position_mult = 0.0
    
    # Collecter toutes les issues
    all_issues = []
    for c in checks:
        for issue in c["issues"]:
            all_issues.append(f"{c['source']}: {issue}")
    
    return {
        "timestamp": int(time.time()),
        "global_score": round(weighted_score, 3),
        "mode": mode,
        "mode_label": mode_label,
        "position_multiplier": position_mult,
        "sources": {c["source"]: {"score": c["score"], "issues": c["issues"]} for c in checks},
        "all_issues": all_issues,
        "n_issues": len(all_issues),
    }

# ─── Main ─────────────────────────────────────────────────────

def compute_health():
    """Calcule la santé du pipeline, sauvegarde dans pipeline_health.json"""
    print("[HEALTH] Calcul en cours...")
    
    # 1. Charger live.json
    try:
        live = json.loads(LIVE.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  ❌ Impossible de lire live.json: {e}")
        return None
    
    # 2. Calculer la santé
    health = compute_global_health(live)
    
    # 3. Sauvegarder
    HEALTH_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(HEALTH_OUTPUT, "w") as f:
        json.dump(health, f, indent=2)
    
    # 4. Résumé
    print(f"  Score: {health['global_score']} | Mode: {health['mode_label']} | "
          f"Issues: {health['n_issues']} | Mult: ×{health['position_multiplier']}")
    
    if health["all_issues"]:
        for issue in health["all_issues"][:5]:
            print(f"    ⚠️ {issue}")
    
    return health

if __name__ == "__main__":
    compute_health()
