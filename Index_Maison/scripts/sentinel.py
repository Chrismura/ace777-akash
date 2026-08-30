#!/usr/bin/env python3
"""
sentinel.py — SENTINELLE DU VRAI
Surveille live.json en continu. Ne déclenche le sniffer (DeepSeek V4) QUE
quand un z-score dépasse le seuil = anomalie structurelle détectée.

Architecture (F2 — Gemini) :
  live.json → sentinel.py → [z-score > 2.0] → sniffer_vrai.py → Hulk

En marché calme : 0 appel Hub/heure.
En volatile : 12 appels/heure max (rate-limite 30 min/paire).

Auteur : Ace (Index Maison)
Version : 1.0
Date : 2026-08-25
"""

import json
import math
import time
import urllib.request
from pathlib import Path
from datetime import datetime, timezone
from collections import deque

# ─── Config ────────────────────────────────────────────────────

INDEX = Path(__file__).parent.parent
LIVE = INDEX / "thermo" / "live.json"
HISTORY = INDEX / "data" / "sentinel_history.json"
SIGNALS = INDEX / "data" / "sentinel_signals.json"
HUB = "http://127.0.0.1:11435/v1/chat/completions"

# Seuils de z-score (au-delà = anomalie)
ZSCORE_THRESHOLDS = {
    "price_1h": 2.5,        # Prix bouge trop vite en 1h
    "volume": 2.0,          # Volume anormal
    "funding": 2.0,         # Funding rate anormal
    "whale_usd": 2.5,       # Baleine géante
    "liquidations": 2.0,    # Liquidations massives
    "sdi": 2.0,             # Silent Drain Index anormal
    "ipt": 2.0,             # Indice Pression Topologique anormal
    "cpfp": 2.0,            # CPFP anormal
    "dust": 2.0,            # Dust anormal
    "long_short": 2.0,      # Ratio long/short anormal
    "taker_ratio": 2.0,     # Taker ratio anormal
    "fear_greed": 2.0,      # Fear/Greed change brutalement
}

# Rate limiting : 1 appel Hub toutes les 30 min par paire
RATE_LIMIT_SECONDS = 1800

# Historique : garder les 288 dernières mesures (24h à 5 min d'intervalle)
HISTORY_SIZE = 288

# ─── History management ────────────────────────────────────────

def load_history():
    """Charge l'historique des mesures sentinel"""
    try:
        return json.loads(HISTORY.read_text(encoding="utf-8"))
    except Exception:
        return {"measures": [], "last_trigger": {}}

def save_history(history):
    """Sauvegarde l'historique"""
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    # Garder seulement les 288 dernières mesures
    history["measures"] = history["measures"][-HISTORY_SIZE:]
    HISTORY.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")

# ─── Z-Score calculation ──────────────────────────────────────

def compute_zscore(current, history_values):
    """Calcule le z-score d'une valeur par rapport à l'historique"""
    if len(history_values) < 10:
        return 0.0  # Pas assez de données
    
    mean = sum(history_values) / len(history_values)
    variance = sum((v - mean) ** 2 for v in history_values) / len(history_values)
    std = math.sqrt(variance) if variance > 0 else 0.0
    # Fix 27/08 (v2) : un historique quasi-constant n'a PAS de volatilité mesurable
    # → aucune anomalie détectable → z = 0 (pas de signal). Avant : variance ~1e-17
    # de micro-variations flottantes → z astronomique (z=-1.5e15) → 12 fausses alertes
    # → 12 appels hub d'un coup. La sentinelle ne doit déclencher QUE sur une
    # variation RÉELLE par rapport à une distribution stable (comportement doc 25/08).
    if std < 1e-4 * max(1.0, abs(mean)):
        return 0.0
    
    return (current - mean) / std

def extract_metrics(live):
    """Extrait les métriques de live.json pour le z-score.

    FIX 27/08 (leçon « 5 min en trading = la fin du monde », Christophe) :
    price_1h et volume étaient lus depuis live.json, figé par le thermo (1×/h) —
    la sentinelle restait aveugle jusqu'à 55 min sur 60 quand le marché bougeait
    (z-score ≈ 0 sur des valeurs figées → aucun sniffer → silence total).
    Désormais price_1h + volume viennent du MEXC LIVE (1 appel 5 min, gratuit,
    fail-open) ; les indices onchain (sdi/ipt/cpfp/dust) restent du thermo (ils
    n'existent pas ailleurs).
    """
    onchain = live.get("onchain", {})
    sdi_data = live.get("sdi", {})
    ipt_data = live.get("ipt", {})

    # MEXC live : chg1h réel (1 appel, fail-open → repli live.json).
    # Le VOLUME reste sur live.json (volQuote = volume crypto TOTAL ~13B$) —
    # le quoteVolume MEXC BTCUSDT (~0.65B$) n'est PAS la même échelle : le
    # comparer à l'historique casserait le z-score (fausse alerte systématique).
    chg1h_live = fetch_price_volume_live()

    return {
        "price_1h": abs(chg1h_live) if chg1h_live is not None else abs(live.get("chg1h") or 0),
        "volume": live.get("volQuote") or 0,
        "funding": live.get("funding") or 0,
        "whale_usd": live.get("whaleUsd") or 0,
        "liquidations": live.get("liq24Usd") or 0,
        "sdi": sdi_data.get("sdi", 0) if sdi_data else 0,
        "ipt": ipt_data.get("ipt", 0) if ipt_data else 0,
        "cpfp": onchain.get("cpfpDustScore", 0) or 0,
        "dust": onchain.get("cpfpDustScore", 0) or 0,
        "long_short": live.get("longShort") or 1,
        "taker_ratio": live.get("takerRatio") or 0.5,
        "fear_greed": live.get("fearGreed") or 50,
    }

def fetch_price_volume_live():
    """Mouvement 1h BTC réel (MEXC live, 1 appel).

    Fail-open : toute erreur réseau → None → extract_metrics replie sur
    live.json (comportement d'avant). Zéro coût : API publique MEXC, 1 appel
    toutes les 5 min (288/jour, gratuit).
    """
    try:
        import urllib.parse as _up
        q = _up.urlencode({"symbol": "BTCUSDT", "interval": "60m", "limit": 2})
        url = f"https://api.mexc.com/api/v3/klines?{q}"
        req = urllib.request.Request(url, headers={"User-Agent": "ACE777-sentinel/1.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            kl = json.loads(r.read().decode())
        if not kl or len(kl) < 2:
            return None
        # chg1h réel = close courant vs close de la bougie d'il y a 1h
        c_now, c_prev = float(kl[-1][4]), float(kl[-2][4])
        return (c_now / c_prev - 1.0) * 100.0 if c_prev > 0 else 0.0
    except Exception:
        return None


# ─── Rate limiting ────────────────────────────────────────────

def is_rate_limited(history, metric_name):
    """Vérifie si une métrique est rate-limitée"""
    last = history.get("last_trigger", {}).get(metric_name, 0)
    return (time.time() - last) < RATE_LIMIT_SECONDS

def set_rate_limit(history, metric_name):
    """Marque une métrique comme déclenchée"""
    if "last_trigger" not in history:
        history["last_trigger"] = {}
    history["last_trigger"][metric_name] = time.time()

# ─── Sniffer trigger ──────────────────────────────────────────

def fetch_news_headlines(query, n=5):
    """Récupère les titres Google News pour une paire"""
    import urllib.parse
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl=fr&gl=FR&ceid=FR:fr"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ACE777-sentinel/1.0"})
        raw = urllib.request.urlopen(req, timeout=12).read().decode("utf-8", "ignore")
        import re
        titres = re.findall(r"<title>(.*?)</title>", raw, re.DOTALL)
        titres = [re.sub(r"<[^>]+>", "", t).strip() for t in titres[1:]]
        return [t for t in titres if t][:n]
    except Exception:
        return []

def trigger_sniffer(metric_name, zscore, current_value, headlines):
    """Déclenche l'analyse DeepSeek V4 via le Hub"""
    print(f"  🚨 SNIFER DECLANCHÉ : {metric_name} z={zscore:.2f} val={current_value}")
    
    system = """Tu es un expert en détection de mouvements silencieux de baleines crypto.
Analyse la DIVERGENCE entre les données brutes et le narratif médiatique.
Sois concis. Retourne un JSON avec : {"signal": "bullish/bearish/neutral", "confidence": 0-100, "reason": "..."}"""
    
    user = f"""ALERTE SENTINELLE : {metric_name} = {current_value} (z-score {zscore:.2f})

TITRES MÉDIATIQUES :
{chr(10).join(f'- {h}' for h in headlines)}

Analyse la divergence entre cette anomalie onchain et le narratif médiatique.
Les baleines bougent-elles silencieusement ? Le narratif est-il déconnecté de la réalité ?"""
    
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": "nvidia",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": 800,
        "temperature": 0.3,
    }).encode()
    
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.loads(r.read().decode())
            txt = d["choices"][0]["message"]["content"].strip()
            print(f"  ✅ Sniffer response: {txt[:200]}...")
            return {"metric": metric_name, "zscore": zscore, "value": current_value, "analysis": txt, "ts": datetime.now(timezone.utc).isoformat()}
    except Exception as e:
        print(f"  ❌ Hub error: {e}")
        return None

# ─── Main loop ────────────────────────────────────────────────

def sentinel_cycle():
    """Un cycle de la sentinel : lit live.json, calcule les z-scores, déclenche si anomalie"""
    print(f"\n[SENTINEL] Cycle {datetime.now(timezone.utc).strftime('%H:%M:%S')}")
    
    # 1. Charger live.json
    try:
        live = json.loads(LIVE.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  ❌ Impossible de lire live.json: {e}")
        return []
    
    # 2. Charger historique
    history = load_history()
    
    # 3. Extraire métriques
    metrics = extract_metrics(live)
    # FIX 27/08 : timestamp sur chaque mesure — sans lui, impossible d'aligner les
    # mesures aux trades/prix (le test « les indices auraient-ils fait la différence »
    # exige un alignement temporel). Ignoré par le z-score (absent de ZSCORE_THRESHOLDS).
    metrics["ts"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # 4. Ajouter à l'historique
    history["measures"].append(metrics)
    
    # 5. Calculer les z-scores et détecter les anomalies
    alerts = []
    for metric_name, current in metrics.items():
        if metric_name not in ZSCORE_THRESHOLDS:
            continue
        
        # Extraire les valeurs historiques pour cette métrique
        historical = [m.get(metric_name, 0) for m in history["measures"][:-1]]
        
        if len(historical) < 10:
            continue  # Pas assez de données
        
        zscore = compute_zscore(current, historical)
        threshold = ZSCORE_THRESHOLDS[metric_name]
        
        if abs(zscore) > threshold:
            print(f"  ⚠️ {metric_name}: z={zscore:.2f} (seuil {threshold}) val={current}")
            
            # Rate limit check
            if is_rate_limited(history, metric_name):
                print(f"    ⏳ Rate-limité (30 min)")
                continue
            
            # Fetch headlines
            headlines = fetch_news_headlines(metric_name, n=5)
            
            # Trigger sniffer
            result = trigger_sniffer(metric_name, zscore, current, headlines)
            if result:
                alerts.append(result)
                set_rate_limit(history, metric_name)
    
    # 6. Sauvegarder historique
    save_history(history)
    
    # 7. Sauvegarder signaux
    if alerts:
        try:
            existing = json.loads(SIGNALS.read_text(encoding="utf-8"))
        except Exception:
            existing = {"signals": []}
        
        existing["signals"].extend(alerts)
        existing["signals"] = existing["signals"][-50:]  # Garder les 50 derniers
        SIGNALS.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # 8. Résumé
    n_measures = len(history["measures"])
    print(f"  📊 {n_measures} mesures en historique | {len(alerts)} alertes ce cycle")
    
    return alerts

def main():
    """Point d'entrée : un seul cycle (pour launchd/cron)"""
    alerts = sentinel_cycle()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
