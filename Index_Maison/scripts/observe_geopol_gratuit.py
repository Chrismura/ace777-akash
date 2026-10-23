#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""observe_geopol_gratuit.py — OBSERVATEUR Phase 2 (GO Christophe 23/10 « go »).

Lit 2 rails GRATUITS, SANS clé (World Monitor API parquée : Pro payant) :
  1. GDELT 2.1 (events mondiaux : pétrole, sanctions, conflits) ;
  2. Polymarket gamma (cotes publiques : la foule a-t-elle pricé ?).
Compare avec notre geopol maison (thermo/live.json, 5 modules + ML).
Écrit Index_Maison/thermo/geopol_gratuit_live.json — LECTURE SEULE :
aucun effet trading, aucun ordre, aucune clé, aucun lock.
INCASSABLE : chaque source est best-effort (timeout, try/except) ; le fichier
est TOUJOURS écrit (avec erreurs notées) ; exit 0 sauf crash imprévu.
Run manuel pour l'instant (pas de plist) : observation quelques semaines AVANT
tout câblage (règle : mesurer d'abord).
"""
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
THERMO = ROOT + "/Index_Maison/thermo"
OUT = THERMO + "/geopol_gratuit_live.json"


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def get_json(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "ACE777-veille/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "ignore"))


def gdelt(query, n=3, attente=8.0):
    """Top headlines GDELT artlist (gratuit, sans clé).
    Poli : n petit + pause entre appels (GDELT rate-limite vite : 429).
    Un 429 -> une seule reprise après pause, sinon on note HS (fail-open)."""
    import urllib.error as _ue
    q = urllib.parse.quote(query)
    url = (f"https://api.gdeltproject.org/api/v2/doc/doc?query={q}"
           f"&mode=artlist&maxrecords={n}&format=json&sort=dateasc")
    try:
        d = get_json(url)
    except _ue.HTTPError as e:
        if getattr(e, "code", 0) == 429:
            time.sleep(45.0)
            d = get_json(url)
        else:
            raise
    finally:
        time.sleep(attente)  # politesse inter-appels, même en échec
    arts = d.get("articles") or []
    return [{"titre": a.get("title"), "source": a.get("domain"),
             "pays": a.get("sourcecountry"), "vu": a.get("seendate")}
            for a in arts[:n]]


def polymarket_crypto(limit=50):
    """Marchés actifs, filtrés crypto/macro/géo (gamma API publique)."""
    url = ("https://gamma-api.polymarket.com/events"
           f"?active=true&closed=false&limit={limit}")
    evs = get_json(url)
    mots = ("bitcoin", "btc", "crypto", "ethereum", "eth", "fed", "rate",
            "recession", "war", "oil", "tariff", "election", "xrp")
    out = []
    for e in (evs if isinstance(evs, list) else []):
        t = ((e.get("title") or "") + " " + (e.get("slug") or "")).lower()
        if not any(m in t for m in mots):
            continue
        mkts = e.get("markets") or []
        probs = []
        for m in mkts[:4]:
            try:
                px = json.loads(m.get("outcomePrices") or "[]")
                outs = json.loads(m.get("outcomes") or "[]")
                probs.append({"q": m.get("question") or m.get("groupItemTitle"),
                              "prix": [float(x) for x in px],
                              "issues": outs})
            except Exception:
                continue
        if probs:
            out.append({"event": e.get("title"), "slug": e.get("slug"),
                        "volume": e.get("volume"), "marches": probs})
        if len(out) >= 12:
            break
    return out


def main():
    res = {"ts": utc(), "sources": {}, "gdelt": {}, "polymarket": [],
           "notre_geopol": {}, "lecture": "", "ok": True}
    # UN SEUL appel GDELT (requête combinée OR) : 3 appels = 429 assuré.
    # GDELT rate-limite par IP/fenêtre ; 1 appel poli + 1 reprise longue.
    try:
        res["gdelt"]["monde"] = gdelt("(petroleum OR oil OR sanctions OR war OR conflict)", n=8)
        res["sources"]["gdelt_monde"] = f"ok ({len(res['gdelt']['monde'])} articles)"
    except Exception as e:
        res["gdelt"]["monde"] = []
        res["sources"]["gdelt_monde"] = f"HS: {e} (fenetre rate-limit, reessayer plus tard)"
        res["ok"] = False
    try:
        res["polymarket"] = polymarket_crypto()
        res["sources"]["polymarket"] = f"ok ({len(res['polymarket'])} events crypto/macro)"
    except Exception as e:
        res["sources"]["polymarket"] = f"HS: {e}"
        res["ok"] = False
    try:
        g = json.load(open(THERMO + "/live.json", encoding="utf-8")).get("geopol") or {}
        res["notre_geopol"] = {"score": g.get("score"), "niveau": g.get("niveau"),
                               "emoji": g.get("emoji")}
    except Exception as e:
        res["notre_geopol"] = {"erreur": str(e)}
    n_g = sum(len(v) for v in res["gdelt"].values())
    n_p = len(res["polymarket"])
    ng = res["notre_geopol"]
    res["lecture"] = (f"GDELT {n_g} gros titres · Polymarket {n_p} events "
                      f"crypto/macro suivis · maison géopol {ng.get('score')} "
                      f"{ng.get('niveau')} — croisement à suivre sur la durée.")
    try:
        json.dump(res, open(OUT, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        # Historique (1 ligne/run) : le croisement se juge sur la DURÉE, pas
        # sur un instant. Append-only, jamais écrasé (incassable par construction).
        with open(THERMO + "/geopol_gratuit_hist.jsonl", "a", encoding="utf-8") as h:
            h.write(json.dumps({"ts": res["ts"], "ok": res["ok"],
                                "sources": res["sources"],
                                "n_gdelt": sum(len(v) for v in res["gdelt"].values()),
                                "n_poly": len(res["polymarket"]),
                                "maison": res["notre_geopol"],
                                "poly_top": [(e.get("event") or "")[:60] for e in res["polymarket"][:6]]},
                               ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"écriture impossible : {e}")
        return 2
    print(res["lecture"])
    print(f"-> {OUT} (ok={res['ok']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
