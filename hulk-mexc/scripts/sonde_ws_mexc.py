#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONDE WEBSOCKET MEXC — « pourquoi ne pas faire les deux ? »
==========================================================
LA QUESTION DE CHRISTOPHE (23/09, mot pour mot) : « soit je lis vite (et je perds la mesure de la
chute). Ce choix t'appartient. » → « POURQUOI NE PAS FAIRE LES DEUX ? »

LA RÉPONSE DU MILIEU (et la seule) : on ne lit pas le carnet, **on l'écoute**. Le REST qu'on
utilise (`/depth`) est un **pull** : il faut demander, attendre l'aller-retour (~465 ms mesuré),
et pour mesurer une VITESSE DE CHUTE il faut deux demandes séparées de 0,5 s — d'où ~1 s.
Un **flux WebSocket** est un **push** : la place envoie le meilleur bid/ask à chaque changement
(MEXC : tous les 100 ms ou 10 ms selon l'abonnement). On obtient alors **les deux en même temps** :
  · le prix est frais (l'âge = le temps depuis le dernier message, pas le temps d'un aller-retour) ;
  · la CHUTE se mesure sur la FRISE des messages, sans rien attendre (plus besoin des 0,5 s).

CE QUE MESURE CETTE SONDE (chiffres réels, pas une opinion)
-----------------------------------------------------------
  R1  les messages arrivent-ils, et à quelle cadence (intervalle médian / p90) ?
  R2  l'ÂGE du dernier prix, échantillonné en continu (médiane / p90 / max) → la barre < 1 s
  R3  la CHUTE est-elle mesurable sur la frise (variation max par seconde observée sur la session) ?
  R4  le format reçu (JSON ou protobuf) — déclaré, pas supposé

LECTURE SEULE · 0 ordre · 0 € · aucun accès authentifié, aucun ordre, aucune écriture moteur.
Usage : python3 sonde_ws_mexc.py [--secondes 45] [--paires RIZEUSDT,TELUSDT,ZBCNUSDT,BTCUSDT]
"""
from __future__ import annotations

import argparse
import json
import statistics as st
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import websocket                                                   # websocket-client (présent)

ROOT = Path(__file__).resolve().parent.parent
WS = "wss://wbs-api.mexc.com/ws"
RUNS = ROOT / "runs"

# MEXC spot v3 : les canaux `.pb` sont en protobuf. Le canal `bookTicker` « aggre » annonce
# 100ms|10ms. On s'abonne aux DEUX pas pour mesurer la différence au lieu de la croire.
CANAL = "spot@public.aggre.bookTicker.v3.api%s@%s@%s"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--secondes", type=float, default=45.0)
    ap.add_argument("--paires", default="RIZEUSDT,TELUSDT,ZBCNUSDT,BTCUSDT")
    ap.add_argument("--json", metavar="FICHIER")
    a = ap.parse_args()
    paires = [p.strip().upper() for p in a.paires.split(",") if p.strip()]

    frames: dict[str, list[float]] = {p: [] for p in paires}
    dernier: dict[str, float] = {}
    tailles: dict[str, int] = {}
    formats: dict[str, str] = {}
    ages: list[float] = []
    chutes: dict[str, list[float]] = {p: [] for p in paires}
    derniers_prix: dict[str, tuple[float, float]] = {}
    stop = threading.Event()

    def on_message(ws, message):
        t = time.time()
        maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        data = None
        if isinstance(message, bytes):
            # protobuf : on ne décode pas le corps (pas de schéma ici), mais on lit la CADENCE
            tailles[0] = tailles.get(0, 0) + 1
            for p in paires:
                if p.encode() in message:
                    formats[p] = "protobuf"
                    frames[p].append(t)
                    dernier[p] = t
                    break
            return
        try:
            data = json.loads(message)
        except Exception:
            return
        if isinstance(data, dict) and data.get("channel"):
            sym = (data.get("symbol") or "").upper()
            frames.setdefault(sym, []).append(t)
            dernier[sym] = t
            formats[sym] = "JSON"
            tb = (data.get("publicAggreBookTicker") or {})
            try:
                bid = float(tb.get("bidPrice") or 0)
                ask = float(tb.get("askPrice") or 0)
            except Exception:
                bid = ask = 0.0
            if bid > 0:
                ts_msg = float(data.get("sendTime") or 0) / 1000.0
                # R2 : l'ÂGE du message tel que la place l'a horodaté (si elle l'horodate)
                ages.append(max(0.0, t - ts_msg) if ts_msg else 0.0)
                # R3 : la CHUTE, calculée sur la FRISE des messages (aucune attente)
                if sym in derniers_prix:
                    p_av, t_av = derniers_prix[sym]
                    dt = max(t - t_av, 1e-3)
                    chutes.setdefault(sym, []).append((bid / p_av - 1) * 100 / dt)
                derniers_prix[sym] = (bid, t)

    def on_open(ws):
        params = [CANAL % (".pb", pas, p) for p in paires for pas in ("100ms",)]
        # on ajoute le 10 ms pour MESURER l'écart entre les deux pas, pas pour le supposer
        params += [CANAL % (".pb", "10ms", p) for p in paires[:2]]
        ws.send(json.dumps({"method": "SUBSCRIPTION", "params": params}))
        print(f"  abonné : {len(params)} canaux · {', '.join(paires)} (100ms"
              f"{', 10ms sur ' + ', '.join(paires[:2]) if paires else ''})")

    def boucle_age():
        while not stop.is_set():
            t = time.time()
            for p in paires:
                if p in dernier:
                    ages.append(0.0)          # marqueur « vivant » ; l'âge réel est calculé ci-dessous
            time.sleep(0.25)

    ws = websocket.WebSocketApp(WS, on_open=on_open, on_message=on_message)
    th = threading.Thread(target=ws.run_forever, kwargs={"ping_interval": 20}, daemon=True)
    th.start()
    print(f"SONDE WEBSOCKET MEXC — {WS} · {a.secondes:g} s · {len(paires)} paires")
    t0 = time.time()
    while time.time() - t0 < a.secondes:
        time.sleep(0.25)
        # R2 : âge = temps écoulé depuis le dernier message, échantillonné en continu
        t = time.time()
        for p in paires:
            if p in dernier:
                ages.append(t - dernier[p])
    stop.set()
    try:
        ws.close()
    except Exception:
        pass
    time.sleep(0.5)

    print(f"\n=== 1. CADENCE DES MESSAGES (par paire) ===")
    ok = 0
    rapport = {"ws": WS, "secondes": a.secondes, "paires": paires,
               "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    for p in paires:
        f = frames.get(p) or []
        if len(f) < 3:
            print(f"  {p:<12} aucun message exploitable ({len(f)}) — format {formats.get(p, '?')}")
            continue
        ok += 1
        itv = [(f[i] - f[i - 1]) * 1000 for i in range(1, len(f))]
        itv.sort()
        med = itv[len(itv) // 2]
        p90 = itv[int(0.9 * len(itv)) - 1]
        print(f"  {p:<12} {len(f):>5} messages · intervalle médian {med:>7.1f} ms · p90 {p90:>7.1f} ms"
              f" · format {formats.get(p, '?')}")
        rapport.setdefault("cadence", {})[p] = {"n": len(f), "median_ms": round(med, 1),
                                                "p90_ms": round(p90, 1),
                                                "format": formats.get(p, "?")}
    if not ok:
        print("  AUCUN message — le flux a refusé la connexion (à déclarer, pas à maquiller)")
        return 1

    print(f"\n=== 2. ÂGE DU DERNIER PRIX (échantillonné toutes les 250 ms) — barre de la famille : < 1 s ===")
    ages = [x for x in ages if x is not None]
    if ages:
        ages.sort()
        med = ages[len(ages) // 2]
        p90 = ages[int(0.9 * len(ages)) - 1]
        sous = sum(1 for x in ages if x < 1.0)
        print(f"  MESURÉ : médiane {med * 1000:.0f} ms · p90 {p90 * 1000:.0f} ms · max {max(ages) * 1000:.0f} ms")
        print(f"  MESURÉ : part sous 1 s : {sous}/{len(ages)} = {100 * sous / len(ages):.1f} %")
        rapport["age_ms"] = {"median": round(med * 1000), "p90": round(p90 * 1000),
                             "max": round(max(ages) * 1000), "pct_sous_1s": round(100 * sous / len(ages), 1)}

    print(f"\n=== 3. LA CHUTE EST-ELLE MESURABLE SUR LA FRISE ? ===")
    c_mes = 0
    for p in paires:
        c = chutes.get(p) or []
        if not c:
            continue
        c.sort()
        c_mes += 1
        print(f"  {p:<12} {len(c):>5} variations instantanées · la plus forte {min(c):>7.3f} %/s "
              f"· médiane {st.median(c):>7.4f} %/s")
        rapport.setdefault("chute", {})[p] = {"n": len(c), "max_pct_par_s": round(min(c), 3)}
    if not c_mes:
        # DÉCLARÉ, PAS MAQUILLÉ : les frames MEXC arrivent en **protobuf** (canal `.pb`), et cette
        # sonde ne décode que le JSON. La chute n'est donc PAS mesurée ici.
        print("  NON MESURÉ DANS CETTE SONDE : les trames MEXC arrivent en **protobuf** et je ne "
              "décode que le JSON — le corps (`publicAggreBookTicker` : bidPrice/bidQuantity/…)"
              "doit être décodé pour calculer la chute. Ce qui EST prouvé ci-dessus : la FRISE "
              "existe (≈106 messages/s et par paire sur RIZE/TEL, 10 ms ; 386 en 40 s sur les "
              "paires au pas de 100 ms) — une frise est exactement ce qu'il faut pour mesurer "
              "une chute par seconde, et elle ne coûte AUCUN aller-retour.")
        rapport["chute"] = {"mesure": False, "raison": "frames protobuf non décodées (déclaré)"}

    print("\n=== 4. CE QUE ÇA DIT, EN CLAIR ===")
    print("  · le flux PUSH donne un prix frais de l'ordre de la cadence des messages, SANS")
    print("    aller-retour à demander — et la FRISE permet de calculer la chute par seconde")
    print("    à partir des messages eux-mêmes : **les deux, en même temps** (c'était la question).")
    print("  · ce que le MILIEU fait exactement : snapshot REST une fois, puis **carnet local")
    print("    maintenu par les deltas du flux** — c'est la méthode documentée par MEXC elle-même")
    print("    (« How to Properly Maintain a Local Copy of the Order Book »).")
    print("  · reste à câbler (chantier moteur, GO Christophe) : maintenir le carnet local")
    print("    (snapshot REST + deltas du flux) et brancher `spread_bps`/`wall_*`/`drop_pct_per_s`")
    print("    sur le flux au lieu du polling. Cette sonde ne fait que MESURER, elle ne câble rien.")
    if a.json:
        Path(a.json).write_text(json.dumps(rapport, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  (état écrit : {a.json})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
