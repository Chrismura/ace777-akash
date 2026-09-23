#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_prix_mexc_fraicheur.py — LE TEST QUE LA FAMILLE EXIGE (23/09/2026)
=======================================================================

Pourquoi ce fichier existe : dans l'audit MEXC×HULK j'ai écrit « le prix de remplissage a
1 à 5 minutes de retard », et j'en ai tiré une explication (cache de cycle / photo
d'aspiration). Les trois modèles de la famille ont répondu la même chose en substance :
« la mesure est là, l'EXPLICATION est extrapolée — mesure l'écart d'horloge avant de
conclure ». Et Nemotron a ajouté le point qui fait mal : *mes propres conclusions ne
passent pas le filtre que j'applique au moteur*.

CE TEST TRANCHE ENTRE DEUX MONDES OPPOSÉS :

  H1 (notre bug) : MEXC a un prix frais (dernier TRADE récent) et le moteur utilise quand
     même un prix vieux de 1 à 5 min → c'est bien notre chaîne qui retarde.
  H2 (pas notre bug, pire) : sur une paire peu liquide, il n'y a PAS eu de trade depuis
     plusieurs minutes — le « dernier prix » de MEXC est vieux PAR NATURE. Alors le moteur
     a bien lu le prix de l'exchange, mais **ce prix n'était pas négociable** : on a
     paper-tradé à un prix qu'aucune contrepartie n'offrait. C'est un défaut du PAPER,
     pas de la lecture — et ça change complètement la conclusion.

MESURES (par paire, lecture seule) :
  · âge du dernier TRADE (dernière kline 1 min avec volume > 0) ;
  · écart entre `/ticker/price` (le « dernier prix » utilisé par le moteur) et la clôture
    de cette dernière kline négociée ;
  · spread live du carnet (`bookTicker`) — la seule grandeur réellement instantanée ;
  · pour une paire sans trade depuis N minutes : le prix exécutable est-il le bid/ask ?

Sortie : runs/PROBE_PRIX_FRAICHEUR_*.json/.txt · 0 ordre, 0 €.
"""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
RUNS = RACINE / "hulk-mexc" / "runs" if (RACINE / "hulk-mexc").exists() else RACINE / "runs"
TAG = datetime.now(timezone.utc).strftime("%Y%m%d")
UA = {"User-Agent": "hulk-audit/1.0"}


def http_json(url, timeout=15.0, retries=3):
    last = None
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return json.loads(r.read().decode()), r.headers.get("Date")
        except Exception as e:                       # noqa: BLE001
            last = e
            time.sleep(0.5 * (i + 1))
    raise RuntimeError(f"HTTP KO {url} : {last}")


def main() -> int:
    state = sorted(RUNS.glob("PAPER_V1_*_state.json"))[-1]
    st = json.loads(state.read_text(encoding="utf-8"))
    paires = list(st.get("pairs") or [])
    print("=== PROBE FRAÎCHEUR DU PRIX MEXC — le test exigé par la famille ===")
    print(f"paires moteur : {len(paires)} · {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print()

    # horloge : l'en-tête HTTP `Date` de MEXC vs notre horloge locale (1er test)
    _, date_hdr = http_json("https://api.mexc.com/api/v3/ticker/price?symbol=BTCUSDT")
    local_now = datetime.now(timezone.utc)
    skew = None
    if date_hdr:
        try:
            srv = datetime.strptime(date_hdr, "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=timezone.utc)
            skew = round((local_now - srv).total_seconds(), 1)
        except Exception:
            pass
    print(f"HORLOGE : en-tête HTTP MEXC « Date » = {date_hdr} · notre horloge = "
          f"{local_now.strftime('%H:%M:%SZ')} · ÉCART = {skew} s")
    print()

    lignes = []
    for pair in paires:
        try:
            t, _ = http_json("https://api.mexc.com/api/v3/ticker/price?" +
                             urllib.parse.urlencode({"symbol": pair}))
            last_px = float(t["price"])
            k, _ = http_json("https://api.mexc.com/api/v3/klines?" +
                             urllib.parse.urlencode({"symbol": pair, "interval": "1m", "limit": 15}))
            bt, _ = http_json("https://api.mexc.com/api/v3/ticker/bookTicker?" +
                              urllib.parse.urlencode({"symbol": pair}))
            time.sleep(0.1)
        except Exception as e:                       # noqa: BLE001
            lignes.append({"pair": pair, "erreur": str(e)[:100]})
            continue
        # dernière kline 1 min AVEC volume > 0 = dernier échange réel
        dernier = None
        for c in reversed(k):
            if float(c[5]) > 0:
                dernier = c
                break
        age_trade_min = None
        ecart_px_vs_dernier_pct = None
        if dernier:
            age_ms = time.time() * 1000 - int(dernier[0])
            age_trade_min = round(age_ms / 60_000, 1)
            close = float(dernier[4])
            if close > 0:
                ecart_px_vs_dernier_pct = round((last_px - close) / close * 100, 4)
        bid = float(bt.get("bidPrice") or 0)
        ask = float(bt.get("askPrice") or 0)
        mid = (bid + ask) / 2 if bid and ask else 0
        bps_px_vs_mid = round((last_px - mid) / mid * 10000, 1) if mid else None
        spread_bps = round((ask - bid) / mid * 10000, 2) if mid else None
        lignes.append({
            "pair": pair, "ticker_price": last_px, "bid": bid, "ask": ask, "mid": mid,
            "spread_bps": spread_bps, "prix_vs_mid_bps": bps_px_vs_mid,
            "age_dernier_trade_min": age_trade_min,
            "ticker_vs_derniere_kline_pct": ecart_px_vs_dernier_pct,
        })

    ok = [x for x in lignes if "erreur" not in x]
    print(f"{'paire':<12}{'ticker':>14}{'bid':>14}{'ask':>14}{'spread bps':>11}"
          f"{'prix vs mid bps':>17}{'âge dernier trade (min)':>24}")
    for x in sorted(ok, key=lambda y: -(y.get("age_dernier_trade_min") or 0)):
        print(f"{x['pair']:<12}{x['ticker_price']:>14.8f}{x['bid']:>14.8f}{x['ask']:>14.8f}"
              f"{(x['spread_bps'] or 0):>11.2f}{(x['prix_vs_mid_bps'] or 0):>17.1f}"
              f"{(x['age_dernier_trade_min'] if x['age_dernier_trade_min'] is not None else -1):>24.1f}")
    for x in lignes:
        if "erreur" in x:
            print(f"{x['pair']:<12}   (erreur : {x['erreur'][:60]})")

    vieux = [x for x in ok if (x.get("age_dernier_trade_min") or 0) >= 1.0]
    tres_vieux = [x for x in ok if (x.get("age_dernier_trade_min") or 0) >= 5.0]
    print()
    print(f"paires dont le DERNIER TRADE a ≥ 1 min : {len(vieux)}/{len(ok)}")
    print(f"paires dont le DERNIER TRADE a ≥ 5 min : {len(tres_vieux)}/{len(ok)} "
          f"{[x['pair'] for x in tres_vieux]}")
    print()
    # ⚠ Verdict CORRIGÉ le jour même : ma première version disait « H2 DOMINANTE » dès qu'UNE
    # paire avait un dernier trade vieux de ≥ 5 min — c'était une conclusion plus large que la
    # mesure (le défaut que la famille m'a reproché). Le verdict est maintenant RELATIF :
    # H2 est CONFIRMÉE pour les paires listées, et H1 reste le cas général sur les autres.
    n_frais = len(ok) - len(vieux)
    nom_vieux = [x["pair"] for x in sorted(vieux, key=lambda y: -(y.get("age_dernier_trade_min") or 0))]
    verdict = (
        f"MIXTE, et il faut le dire par paire : ({n_frais}/{len(ok)}) paires ont échangé dans la "
        f"dernière minute → pour elles, un prix de remplissage vieux de 2-5 min N'EST PAS expliqué "
        f"par l'exchange (H1 = notre chaîne) ; ({len(vieux)}/{len(ok)}) paires ont un dernier trade "
        f"≥ 1 min et {len(tres_vieux)} ≥ 5 min {nom_vieux} → pour celles-là, le prix « dernier "
        f"échangé » est vieux PAR NATURE et le paper a rempli à un prix qu'aucune contrepartie "
        f"n'offrait (H2). Test DÉCISIF restant : rejouer la sonde AU MOMENT d'un remplissage "
        f"(alignée sur le journal), pas à un instant arbitraire.")
    print("VERDICT :", verdict)

    rapport = {
        "instrument": "probe_prix_mexc_fraicheur.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ecart_horloge_vs_mexc_s": skew, "entete_date_mexc": date_hdr,
        "n_paires": len(ok), "age_trade_ge1min": len(vieux), "age_trade_ge5min": len(tres_vieux),
        "verdict": verdict, "paires": lignes, "lecture_seule": True, "ordres": 0,
    }
    (RUNS / f"PROBE_PRIX_FRAICHEUR_{TAG}.json").write_text(
        json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    (RUNS / f"PROBE_PRIX_FRAICHEUR_{TAG}.txt").write_text("\n".join([
        f"PROBE FRAÎCHEUR PRIX MEXC — {rapport['ts_utc']}",
        f"écart horloge vs en-tête MEXC : {skew} s",
        f"dernier trade ≥ 1 min : {len(vieux)}/{len(ok)} · ≥ 5 min : {len(tres_vieux)}/{len(ok)}",
        f"écart ticker vs mid : max {max((abs(x.get('prix_vs_mid_bps') or 0) for x in ok), default=0):.1f} bps",
        f"VERDICT : {verdict}",
    ] + [f"  {x['pair']} âge {x.get('age_dernier_trade_min')} min · spread {x.get('spread_bps')} bps"
         for x in lignes if 'erreur' not in x]), encoding="utf-8")
    print(f"écrit : PROBE_PRIX_FRAICHEUR_{TAG}.json/.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
