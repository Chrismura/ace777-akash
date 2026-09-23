#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FLUX WEBSOCKET MEXC — lecture PUSH du carnet, avec décodeur protobuf minimal
============================================================================
GO 1/2 du 23/09/2026 (Christophe : « pourquoi ne pas faire les DEUX ??? »).

CE QUE ÇA REMPLACE : `ace_sense_mexc.aspiration_sense` fait **deux** appels REST `/depth`
séparés de 0,5 s (âge mesuré : 1 058 ms médian, 22,7 % sous la barre de 1 s du jury).
Ici on **écoute** le carnet : `spot@public.aggre.bookTicker.v3.api.pb@100ms@<paire>`.
Mesuré sur 4 paires : cadence 11 ms (pas de 10 ms) / 100 ms, **âge médian 14-15 ms, 100 % < 1 s**.

LES DEUX EN MÊME TEMPS : le dernier message donne un prix FRAIS, et la FRISE des messages
donne la CHUTE (variation du meilleur bid par seconde) **sans rien attendre**.

DÉCODEUR PROTOBUF : les trames MEXC v3 sont en protobuf (pas de JSON). On décode les champs
à longueur délimitée (type 2) et on retient ceux qui sont numériquement lisibles — le premier
sert de `bidPrice`, le suivant de `bidQuantity`, puis `askPrice`/`askQuantity`. GARDE-FOU
intégré : on n'accepte le décodage que si `0 < bid <= ask` (sinon on rend `ok: False`), donc
une mauvaise hypothèse de schéma se voit au lieu de produire un faux prix.

LECTURE SEULE · 0 ordre · 0 € · aucun ordre, aucune écriture moteur.
"""
from __future__ import annotations

import json
import threading
import time
from datetime import datetime, timezone

import websocket                                                    # websocket-client

WS = "wss://wbs-api.mexc.com/ws"
CANAL = "spot@public.aggre.bookTicker.v3.api.pb@%s@%s"


def _varint(b: bytes, i: int) -> tuple[int, int]:
    v = 0
    s = 0
    while i < len(b):
        c = b[i]
        i += 1
        v |= (c & 0x7F) << s
        if not (c & 0x80):
            break
        s += 7
    return v, i


def champs_protobuf(b: bytes) -> list[bytes]:
    """Champs à longueur délimitée (type 2) d'un message protobuf — sans le schéma."""
    out: list[bytes] = []
    i = 0
    while i < len(b):
        try:
            cle, i = _varint(b, i)
            typ = cle & 7
            if typ == 2:
                n, i = _varint(b, i)
                out.append(b[i:i + n])
                i += n
            elif typ == 0:
                _, i = _varint(b, i)
            elif typ == 1:
                i += 8
            elif typ == 5:
                i += 4
            else:
                break
        except Exception:
            break
    return out


def _nombre(x: bytes) -> float | None:
    try:
        s = x.decode("ascii").strip()
        if not s or len(s) > 24:
            return None
        return float(s)
    except Exception:
        return None


def decoder_bookticker(brut: bytes) -> dict:
    """Décode une trame `bookTicker` MEXC. Rend {} si le garde-fou échoue.

    STRUCTURE RÉELLE (lue sur une trame, pas supposée) : l'en-tête porte le canal (champ 1),
    le symbole (champ 2) et le corps est un **message imbriqué** (champ 3) dont les 4 champs
    sont `bidPrice`, `bidQuantity`, `askPrice`, `askQuantity` (types 0x0a/0x12/0x1a/0x22).
    Le premier essai décodeur cherchait les nombres au niveau RACINE : il ne trouvait rien et
    le garde-fou l'a dit (`aucune trame décodée`) au lieu de fabriquer un prix.
    """
    for f in champs_protobuf(brut):
        nums = [n for n in (_nombre(x) for x in champs_protobuf(f)) if n is not None]
        if len(nums) < 4:
            continue
        bid, bid_q, ask, ask_q = nums[0], nums[1], nums[2], nums[3]
        if not (0 < bid <= ask):
            continue
        return {"bid": bid, "bid_qty": bid_q, "ask": ask, "ask_qty": ask_q,
                "spread_bps": (ask - bid) / ((ask + bid) / 2) * 10000.0}
    return {}


def lire_flux(paires: list[str], secondes: float = 2.5, pas: str = "100ms",
              recu: dict | None = None) -> dict:
    """Écoute le flux `secondes` et rend, par paire :

      {ok, bid, ask, spread_bps, age_s, n, drop_bid_pct_per_s, wall_bid_usdt, wall_ask_usdt}

    `drop_bid_pct_per_s` = (dernier bid / premier bid − 1) × 100 / durée écoulée — c'est
    exactement la grandeur `drop_bid_pct_per_s` du satellite, mais mesurée sur la FRISE.
    `wall_bid_usdt` = plus gros bid × sa quantité observés (le « mur »), comme le carnet REST.
    """
    paires = [p.strip().upper() for p in paires if p.strip()]
    hist: dict[str, list[tuple[float, dict]]] = {p: [] for p in paires}

    def on_message(ws, msg):
        if not isinstance(msg, bytes):
            return
        # la trame contient d'abord l'en-tête (channel/symbol) puis le corps
        sym = None
        for p in paires:
            if p.encode() in msg:
                sym = p
                break
        if sym is None:
            return
        d = decoder_bookticker(msg)
        if d:
            hist[sym].append((time.time(), d))

    def on_open(ws):
        ws.send(json.dumps({"method": "SUBSCRIPTION",
                            "params": [CANAL % (pas, p) for p in paires]}))

    ws = websocket.WebSocketApp(WS, on_open=on_open, on_message=on_message)
    th = threading.Thread(target=ws.run_forever, kwargs={"ping_interval": 20}, daemon=True)
    th.start()
    t0 = time.time()
    while time.time() - t0 < secondes:
        time.sleep(0.05)
    try:
        ws.close()
    except Exception:
        pass

    now = time.time()
    out = {}
    for p in paires:
        h = hist.get(p) or []
        if not h:
            out[p] = {"ok": False, "reason": "aucune trame décodée"}
            continue
        t_p, d_p = h[0]
        t_d, d_d = h[-1]
        dur = max(t_d - t_p, 0.05)
        mur_b = max((x[1]["bid"] * x[1]["bid_qty"] for x in h), default=0.0)
        mur_a = max((x[1]["ask"] * x[1]["ask_qty"] for x in h), default=0.0)
        out[p] = {
            "ok": True, "bid": d_d["bid"], "ask": d_d["ask"], "spread_bps": round(d_d["spread_bps"], 2),
            "age_s": round(now - t_d, 3), "n": len(h),
            "drop_bid_pct_per_s": round((d_d["bid"] / d_p["bid"] - 1) * 100 / dur, 3) if d_p["bid"] else 0.0,
            "wall_bid_usdt": round(mur_b, 2), "wall_ask_usdt": round(mur_a, 2),
            "prix": d_d["ask"] if d_d["ask"] > 0 else d_d["bid"],
        }
    if recu is not None:
        recu.update(out)
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--paires", default="RIZEUSDT,TELUSDT,ZBCNUSDT,BTCUSDT,EDELUSDT")
    ap.add_argument("--secondes", type=float, default=3.0)
    ap.add_argument("--pas", default="100ms")
    a = ap.parse_args()
    print(f"FLUX MEXC (protobuf décodé) — {a.secondes:g} s · pas {a.pas} · "
          f"{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}")
    r = lire_flux(a.paires.split(","), a.secondes, a.pas)
    for p, d in r.items():
        if not d.get("ok"):
            print(f"  {p:<12} ÉCHEC — {d.get('reason')}")
            continue
        print(f"  {p:<12} bid {d['bid']:<12.8f} ask {d['ask']:<12.8f} · spread {d['spread_bps']:>7.2f} bps"
              f" · âge {d['age_s'] * 1000:>6.0f} ms · {d['n']:>4} trames · "
              f"chute {d['drop_bid_pct_per_s']:>+8.3f} %/s · mur {d['wall_bid_usdt']:>12.2f} $")
    print("  LECTURE SEULE · 0 ordre · 0 €")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
