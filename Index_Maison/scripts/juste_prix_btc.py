#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
juste_prix_btc.py — PHASE A du plan boucle Dan1ro0 (GO Christophe 13/09/2026).

SPÉCIFICATION FIGÉE AVANT LE PREMIER CYCLE — anti data-snooping, UN SEUL ESSAI.
Verdict pré-enregistré (écrit avant toute donnée) : la note doit prédire le sens
de la bougie 5m à ≥ 52 % sur 200+ bougies jugées, verdict lu le 11/10/2026.
Si ÉCHEC → la couche « juste prix » est abandonnée, pas de variante déguisée.

QU'IL FAIT (la boucle du post Dan1ro0, couche 1 — le juste prix) :
  1. Chaque cycle (5 min) : calcule une note composite dans [-1, +1] en croisant
     UNIQUEMENT les capteurs déjà existants de la maison (aucun nouveau flux) :
       - momentum 5m Binance (12 dernières bougies fermées)      poids 0.30
       - takerRatio (fiche Cortana, agressivité acheteurs)        poids 0.20
       - climate Cortana (bullish +1 / bearish -1 / autre 0)      poids 0.20
       - funding (contrarien au-delà de ±0.03 %)                  poids 0.15
       - fear&greed (contrarien aux extrêmes <25 / >75)           poids 0.15
     Les poids sont FIXES ci-dessus, premier jugement, JAMAIS retouchés pendant
     l'essai (les retoucher après coup = tricher avec le verdict).
  2. Émet la prédiction pour la bougie qui S'OUVRE à l'instant du cycle
     (up si note > 0, down si note < 0, égalité → momentum tranche).
     Il s'engage TOUJOURS (pas de « flat ») : la note est une promesse vérifiable.
  3. Juge mécaniquement les prédictions passées dont la bougie est fermée :
     HIT si la direction réalisée (close vs open) = prédiction, MISS sinon.
  4. Écrit tout en append-only : data/juste_prix_hist.jsonl (on ne réécrit JAMAIS
     l'histoire). Rotation via rotation_jsonl.py si présent (convention maison).

LECTURE SEULE sur la maison : il ne touche ni moteur, ni profils, ni config.
Zéro alerte, zéro sonnerie. Phase B (edge exécutable) et C (paliers) attendent
leur GO et le verdict A du 11/10.
"""
import json
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path.home() / "ace777-test-day1"
MAISON = BASE / "Index_Maison"
HIST = MAISON / "data" / "juste_prix_hist.jsonl"
FEED = MAISON / "thermo" / "cortana_feed.json"
SENTINEL = MAISON / "data" / "sentinel_signals.json"

POIDS = {"momentum": 0.30, "taker": 0.20, "climate": 0.20, "funding": 0.15, "feargreed": 0.15}


def maintenant():
    return datetime.now(timezone.utc)


def bougie_courante_ms(ts):
    """Début (openTime) de la bougie 5m contenant ts, en ms."""
    epoch = ts.timestamp()
    return int((epoch // 300) * 300 * 1000)


def binance(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ace777-juste-prix/1"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode())


def composantes(ts):
    """Rassemble les 5 composantes dans [-1, +1] (0 = neutre). Best-effort."""
    out = {"momentum": 0.0, "taker": 0.0, "climate": 0.0, "funding": 0.0, "feargreed": 0.0}
    detail = {}
    # 1) momentum 5m — 12 dernières bougies FERMÉES
    try:
        open_cur = bougie_courante_ms(ts)
        ks = binance("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&endTime=%d&limit=13" % (open_cur - 1))
        fermees = [k for k in ks if k[6] < open_cur][-12:]
        if len(fermees) >= 6:
            first_o = float(fermees[0][1]); last_c = float(fermees[-1][4])
            bps = (last_c - first_o) / first_o * 10000.0
            out["momentum"] = max(-1.0, min(1.0, bps / 30.0))  # ±30 bps = saturation
            detail["momentum_bps"] = round(bps, 1)
    except Exception as e:
        detail["momentum_err"] = str(e)[:60]
    # 2) fiche Cortana : takerRatio + climate + funding
    try:
        f = json.loads(FEED.read_text())
        tr = f.get("takerRatio")
        if isinstance(tr, (int, float)) and tr > 0:
            # 1.0 = équilibre ; ±0.15 d'écart = saturation
            out["taker"] = max(-1.0, min(1.0, (tr - 1.0) / 0.15))
            detail["takerRatio"] = tr
        clim = str(f.get("climate", "")).lower()
        if any(w in clim for w in ("bull", "hauss", "risk-on")):
            out["climate"] = 1.0
        elif any(w in clim for w in ("bear", "baiss", "risk-off", "crise")):
            out["climate"] = -1.0
        detail["climate"] = clim[:24]
        fu = f.get("funding")
        if isinstance(fu, (int, float)):
            # contrarien : funding très positif = foule longue → pression baissière
            out["funding"] = max(-1.0, min(1.0, -(fu / 0.03)))
            detail["funding"] = fu
    except Exception as e:
        detail["cortana_err"] = str(e)[:60]
    # 3) fear&greed (sentinel) — contrarien aux extrêmes
    try:
        s = json.loads(SENTINEL.read_text())
        for sig in s.get("signals", []):
            if sig.get("metric") == "fear_greed":
                v = sig.get("value")
                if isinstance(v, (int, float)):
                    if v >= 75:
                        out["feargreed"] = -min(1.0, (v - 75) / 15.0)
                    elif v <= 25:
                        out["feargreed"] = min(1.0, (25 - v) / 15.0)
                    detail["fear_greed"] = v
                break
    except Exception as e:
        detail["sentinel_err"] = str(e)[:60]
    return out, detail


def juger_en_attente():
    """Juge les prédictions dont la bougie 5m est fermée. Retourne les lignes jugement."""
    lignes = []
    if not HIST.exists():
        return lignes
    preds = []
    for ln in HIST.read_text().splitlines():
        try:
            o = json.loads(ln)
        except Exception:
            continue
        if o.get("type") == "prediction" and o.get("ts") not in (
            p.get("ts") for p in preds):
            preds.append(o)
    deja = set()
    for ln in HIST.read_text().splitlines():
        try:
            o = json.loads(ln)
        except Exception:
            continue
        if o.get("type") == "jugement":
            deja.add(o.get("ts_prediction"))
    maintenant_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    for p in preds:
        ts = p.get("ts")
        if ts in deja or not ts:
            continue
        if maintenant_ms < ts + 300_000:  # bougie pas encore fermée
            continue
        try:
            ks = binance("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&startTime=%d&limit=1" % ts)
            k = next((x for x in ks if x[0] == ts), None)
            if not k:
                continue
            o_, c_ = float(k[1]), float(k[4])
            reel = "up" if c_ >= o_ else "down"
            lignes.append({
                "type": "jugement", "ts_prediction": ts,
                "juge_at": maintenant(now_iso=True),
                "pred": p.get("direction"), "reel": reel,
                "hit": p.get("direction") == reel,
                "conf": p.get("confidence"),
                "note": p.get("note"),
            })
        except Exception:
            continue
    return lignes


def maintenant(now_iso=False):
    t = datetime.now(timezone.utc)
    return t.isoformat() if now_iso else t


def emettre_prediction():
    ts_ = maintenant()
    open_ms = bougie_courante_ms(ts_)
    comp, detail = composantes(ts_)
    note = sum(POIDS[k] * comp[k] for k in POIDS)
    if note == 0.0:
        direction = "up" if comp["momentum"] >= 0 else "down"
    else:
        direction = "up" if note > 0 else "down"
    conf = round(50 + abs(note) * 30, 1)
    ligne = {
        "type": "prediction", "ts": open_ms,
        "ts_iso": ts_.isoformat(),
        "direction": direction, "note": round(note, 4),
        "confidence": conf,
        "composantes": {k: round(v, 3) for k, v in comp.items()},
        "detail": detail,
        "poids": POIDS,
        "spec": "Phase A — figée 13/09/2026, verdict 11/10 : ≥52 % sur 200+ bougies",
    }
    HIST.parent.mkdir(parents=True, exist_ok=True)
    with HIST.open("a") as fh:
        fh.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    return ligne


def rotation():
    rj = MAISON / "scripts" / "rotation_jsonl.py"
    if rj.exists():
        try:
            subprocess.run([sys.executable, str(rj), str(HIST), "--max-mo", "100"],
                           capture_output=True, timeout=30)
        except Exception:
            pass


def status():
    if not HIST.exists():
        print("aucune donnée — premier cycle à venir")
        return
    preds, hits, misses, pending = 0, 0, 0, 0
    conf_h = conf_t = 0.0
    for ln in HIST.read_text().splitlines():
        try:
            o = json.loads(ln)
        except Exception:
            continue
        if o.get("type") == "prediction":
            preds += 1
        elif o.get("type") == "jugement":
            if o.get("hit"):
                hits += 1; conf_h += o.get("conf") or 0
            else:
                misses += 1; conf_t += o.get("conf") or 0
    n_j = hits + misses
    pending = max(0, preds - n_j)
    print("═══ JUSTE PRIX — Phase A (verdict 11/10 : ≥52 % sur 200+) ═══")
    print("prédictions émises : %d · jugées : %d · en attente : %d" % (preds, n_j, pending))
    if n_j:
        rate = hits / n_j * 100
        print("réussite : %d/%d = %.1f %%  (objectif ≥ 52 %%)" % (hits, n_j, rate))
        print("  · prédiction moyenne quand HIT : %.1f / quand MISS : %.1f" % (
            conf_h / max(1, hits), conf_t / max(1, misses)))
        print("  · bougies restantes avant verdict : %d" % max(0, 200 - n_j))
    print("historique : %s" % HIST)


if __name__ == "__main__":
    if "--status" in sys.argv:
        status()
        sys.exit(0)
    jugements = juger_en_attente()
    with HIST.open("a") as fh:
        for j in jugements:
            fh.write(json.dumps(j, ensure_ascii=False) + "\n")
    pred = emettre_prediction()
    rotation()
    print("prediction %s (note %+.3f, conf %.1f) pour la bougie %s — %d jugement(s) passé(s)" % (
        pred["direction"], pred["note"], pred["confidence"],
        datetime.fromtimestamp(pred["ts"] / 1000, timezone.utc).strftime("%H:%M"),
        len(jugements)))
