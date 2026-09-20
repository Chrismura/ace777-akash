#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kronos_ombre.py — CAPTEUR OMBRE Kronos (P4, GO Christophe 13/09 « go p4 »).

═════════════════════════════════════════════════════════════════════════
SPÉCIFICATION FIGÉE AVANT LE PREMIER CYCLE (anti data-snooping — un seul
démarrage, critère pré-enregistré, AUCUNE retouche pendant l'essai).
═════════════════════════════════════════════════════════════════════════
RÔLE : Kronos (fondation model bougies, open source shiyu-coder/Kronos,
poids NeoQuasar/Kronos-base 409 Mo, local, 0 €) prédit en SILENCE la
prochaine bougie horaire de BTC. Un registre note ses prédictions de
manière MÉCANIQUE. AUCUN branchement : il ne parle à aucun autre organe,
il n'émet aucune alerte, il ne passe aucun ordre. OMBRE = il écrit, on lit.

PRÉDICTION (figée) :
  - Données : bougies 1 h BTC/USDT Binance (klines publiques, gratuit),
    lookback 400 bougies FERMÉES (Kronos max_context=512).
  - Question : la bougie suivante FERMERA au-dessus ou en dessous de son
    OUVERTURE ? (avis HAUSSE / BAISSE — la direction de la bougie prédite)
  - Paramètres d'échantillonnage figés : T=1.0, top_p=0.9, sample_count=1,
    pred_len=1. (Valeurs par défaut du modèle — pas d'optimisation.)

NOTATION MÉCANIQUE (figée) :
  - Une prédiction émise à T pour la bougie qui ferme à T+1h est jugée
    dès que cette bougie est fermée : HIT si la direction réelle
    (close>=open → HAUSSE, sinon BAISSE) = la direction prédite, MISS sinon.
  - Les bougies plat (|close-open| < 0,01 % du prix) sont notées HIT pour
    les deux directions ? NON : elles sont comptées, direction réelle par
    la convention close>=open. HONNÊTETÉ : aucun filtre a posteriori.
  - Le verrou de fraîcheur : une échéance ne peut être jugée qu'une fois.

CRITÈRE PRÉ-ENREGISTRÉ (écrit AVANT le premier cycle — verdict J+14,
soit le 27/09) :
  - SUCCÈS : HIT / (HIT+MISS) >= 55 % sur n >= 100 prédictions jugées,
    ET t-stat >= +2.0 (t = (p-0.5)/sqrt(0.25/n)).
  - ÉCHEC : tout résultat en dessous → Kronos n'est JAMAIS branché, le
    dossier est fermé (pas de « deuxième essai », pas de variante).
  - Entre les deux (n < 100 au 27/09) : on prolonge la collecte jusqu'à
    n=100, verdict mécanique à ce moment-là, aucun critère ne bouge.

CADENCE : 1 h (plist), à :05 pour laisser la bougie se fermer à :00.
COÛT : 0 € (modèle local, données publiques).
ZÉRO ORDRE, ZÉRO ALARME, LECTURE SEULE sur la maison.

Sorties :
  - data/kronos_ombre.jsonl     : prédictions émises (append-only)
  - data/kronos_ombre.jsonl     : mises à jour de statut (pending→HIT/MISS)
  - thermo/kronos_ombre_etat.json : état courant pour le chien de garde
Usage : python3 kronos_ombre.py            # cycle complet (émission + jugement)
        python3 kronos_ombre.py --status   # affiche le tableau de bord
"""
import argparse
import json
import math
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

MAISON = Path.home() / "ace777-test-day1" / "Index_Maison"
DATA = MAISON / "data"
THERMO = MAISON / "thermo"
PRED_JSONL = DATA / "kronos_ombre.jsonl"
ETAT = THERMO / "kronos_ombre_etat.json"

KR = Path.home() / "ace777-test-day1" / "kronos" / "Kronos"
VENV_PY = Path.home() / "ace777-test-day1" / ".venv-kronos" / "bin" / "python"

MODELE = "NeoQuasar/Kronos-base"
TOKENIZER = "NeoQuasar/Kronos-Tokenizer-base"
LOOKBACK = 400          # figé (max_context 512, marge)
PRED_LEN = 1            # figé : UNE bougie
T_TEMP, TOP_P, SAMPLES = 1.0, 0.9, 1   # figés : défauts du modèle

# ---- paramètres d'inférence qui doivent être modifiables par l'utilisateur ----
INF_PARAMS = {"T": 1.0, "top_p": 0.9, "sample_count": 1}  # noqa: par défaut

def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {msg}", flush=True)

def fetch_klines(interval: str = "1h", limit: int = 420) -> list:
    """Bougies 1h BTCUSDT Binance (publique, gratuit). Retourne du plus ancien au plus récent."""
    url = (f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval={interval}&limit={limit}")
    with urllib.request.urlopen(url, timeout=30) as r:
        raw = json.loads(r.read())
    # colonnes Binance : 0 open_time, 1 open, 2 high, 3 low, 4 close, 5 volume, 6 close_time ...
    out = []
    for k in raw:
        out.append({
            "open_time": int(k[0]), "close_time": int(k[6]),
            "open": float(k[1]), "high": float(k[2]),
            "low": float(k[3]), "close": float(k[4]),
            "volume": float(k[5]),
        })
    return out

def infere_kronos(x_df_rows: list) -> dict:
    """Appelle Kronos dans le venv isolé. Retourne {close_pred, open_pred, ...}."""
    code = r'''
import sys, json
sys.path.insert(0, "/Users/christophe/ace777-test-day1/kronos/Kronos")
import pandas as pd
from model import Kronos, KronosTokenizer, KronosPredictor

payload = json.loads(sys.stdin.read())
rows = payload["rows"]
df = pd.DataFrame(rows)
df["ts"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
x_df = df[["open", "high", "low", "close", "volume"]].copy()
x_ts = df["ts"]
# y_timestamp : l'heure suivante (1 bougie)
y_ts = pd.Series([x_ts.iloc[-1] + pd.Timedelta(hours=1)])

tok = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-base")
pred = KronosPredictor(model, tok, device="cpu", max_context=512)
res = pred.predict(df=x_df, x_timestamp=x_ts, y_timestamp=y_ts,
                   pred_len=1, T=1.0, top_p=0.9, sample_count=1)
out = {
    "open_pred": float(res["open"].iloc[0]),
    "close_pred": float(res["close"].iloc[0]),
    "high_pred": float(res["high"].iloc[0]),
    "low_pred": float(res["low"].iloc[0]),
}
print("@@KRONOS@@" + json.dumps(out))
'''
    proc = subprocess.run(
        [str(VENV_PY), "-c", code],
        input=json.dumps({"rows": x_df_rows}).encode(),
        capture_output=True, timeout=600,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"kronos venv a échoué : {proc.stderr.decode()[-500:]}")
    for line in proc.stdout.decode().splitlines():
        if line.startswith("@@KRONOS@@"):
            return json.loads(line[len("@@KRONOS@@"):])
    raise RuntimeError("pas de sortie Kronos exploitable")

def charger_predictions() -> list:
    if not PRED_JSONL.exists():
        return []
    return [json.loads(l) for l in PRED_JSONL.read_text().splitlines() if l.strip()]

def ecrire_etat(extra: dict) -> None:
    etat = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "organe": "kronos-ombre", "role": "capteur ombre (aucun branchement)",
        **extra,
    }
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1))

def cycle() -> None:
    DATA.mkdir(exist_ok=True)
    THERMO.mkdir(exist_ok=True)
    preds = charger_predictions()
    bougies = fetch_klines(limit=420)
    maintenant_ms = int(time.time() * 1000)
    # les bougies FERMÉES (close_time passé)
    fermees = [b for b in bougies if b["close_time"] < maintenant_ms]
    if len(fermees) < LOOKBACK + 2:
        raise RuntimeError(f"pas assez de bougies fermées ({len(fermees)})")

    # ── 1. JUGEMENT des prédictions en attente (dès que leur bougie existe fermée) ──
    par_open = {b["open_time"]: b for b in fermees}
    n_juge = 0
    for p in preds:
        if p.get("statut") != "pending":
            continue
        b = par_open.get(p["bougie_open_time"])
        if not b:
            continue  # pas encore fermée
        reel = "HAUSSE" if b["close"] >= b["open"] else "BAISSE"
        p["statut"] = "HIT" if reel == p["direction"] else "MISS"
        p["reel"] = reel
        p["open_reel"] = b["open"]; p["close_reel"] = b["close"]
        p["juge_ts"] = datetime.now(timezone.utc).isoformat()
        n_juge += 1
    if n_juge:
        PRED_JSONL.write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in preds) + "\n")

    # ── 2. ÉMISSION d'une nouvelle prédiction (si pas déjà faite pour la prochaine bougie) ──
    derniere_fermee = fermees[-1]
    # FIX acquisition (13/09, pré-verdict) : close_time Binance = open_time + 3599999 ms,
    # donc la bougie suivante ouvre à close_time + 1 ms EXACTEMENT (10:00:00.000).
    # Sans le +1, le pointeur ne matche jamais un open_time réel → pending éternel.
    cible_open = derniere_fermee["close_time"] + 1
    deja = any(p["bougie_open_time"] == cible_open for p in preds)
    nouvelle = None
    if not deja:
        log("inférence Kronos (CPU, peut prendre 1-3 min)…")
        t0 = time.time()
        x_rows = fermees[-LOOKBACK:]
        res = infere_kronos(x_rows)
        duree = round(time.time() - t0, 1)
        direction = "HAUSSE" if res["close_pred"] >= res["open_pred"] else "BAISSE"
        nouvelle = {
            "ts_emission": datetime.now(timezone.utc).isoformat(),
            "bougie_open_time": cible_open,
            "bougie_close_prevue": datetime.fromtimestamp(
                (cible_open + 3600_000) / 1000, tz=timezone.utc).isoformat(),
            "fix_pointer": "close_time+1ms (open_time exact Binance) — corrigé pré-verdict 13/09",
            "direction": direction,
            "open_pred": res["open_pred"], "close_pred": res["close_pred"],
            "prix_ref_derniere_fermee": derniere_fermee["close"],
            "modele": MODELE, "lookback": LOOKBACK,
            "statut": "pending",
            "duree_inference_s": duree,
        }
        preds.append(nouvelle)
        PRED_JSONL.write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in preds) + "\n")
        log(f"prédiction émise pour la bougie {datetime.fromtimestamp(cible_open/1000, tz=timezone.utc).strftime('%H:%M')} : {direction} (close prédite {res['close_pred']:.0f} $) · {duree}s")
    else:
        log("prédiction déjà émise pour la bougie en cours — rien à émettre")

    # ── 3. ÉTAT (pour le chien + le tableau de bord) ──
    juges = [p for p in preds if p.get("statut") in ("HIT", "MISS")]
    hits = sum(1 for p in juges if p["statut"] == "HIT")
    n = len(juges)
    p_pct = (hits / n * 100) if n else None
    t_stat = (round((hits / n - 0.5) / math.sqrt(0.25 / n), 2) if n else None)
    etat = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "organe": "kronos-ombre",
        "role": "capteur ombre — AUCUN branchement (P4, GO 13/09)",
        "emises": len(preds),
        "pending": sum(1 for p in preds if p.get("statut") == "pending"),
        "juges": n, "hits": hits,
        "pct": round(p_pct, 1) if p_pct is not None else None,
        "t_stat": t_stat,
        "critere_succes": "pct>=55 et t>=2.0 sur n>=100 (verdict 27/09)",
        "derniere": {k: nouvelle[k] for k in ("ts_emission", "direction", "close_pred") if nouvelle and k in nouvelle},
    }
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1))
    log(f"état : {n} jugées · {hits} HIT · {p_pct if p_pct is not None else '—'} % · t={t_stat}")

def status() -> None:
    if not ETAT.exists():
        print("aucun état — l'organe n'a jamais tourné")
        return
    etat = json.loads(ETAT.read_text())
    print(json.dumps(etat, ensure_ascii=False, indent=1))
    preds = charger_predictions()
    if preds:
        print("\n— 8 dernières prédictions —")
        for p in preds[-8:]:
            print(f"  {p['ts_emission'][:16]} · bougie {datetime.fromtimestamp(p['bougie_open_time']/1000, tz=timezone.utc).strftime('%d/%m %H:00')} · {p['direction']:7s} · {p.get('statut','?')}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    if a.status:
        status()
    else:
        cycle()
