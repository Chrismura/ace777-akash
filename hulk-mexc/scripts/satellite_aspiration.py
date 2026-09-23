#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""satellite_aspiration.py — SATELLITE carnet/aspiration (Phase 3, 31/08, GO Christophe).

POURQUOI
--------
Phase 3 « moteur léger et costaud » : sortir la LECTURE du carnet de profondeur
(aspiration_sense) du cœur de trading pour alléger la boucle de décision et
isoler les pannes réseau. Ce satellite est un démon autonome qui fait le travail
d'OBSERVATION (radar aspiration par paire active) et écrit un fichier JSON unique,
écrit ATOMIQUEMENT (fichier .tmp + os.replace) : runs/aspiration_live.json.

ZÉRO RISQUE :
- Le moteur Hulk continue de tourner INLINE tant que la bascule config
  (ASPIRATION_SRC=fichier) n'est PAS activée. Ce satellite observe et écrit.
- Une fois validé sur plusieurs jours, on bascule le cœur sur ce fichier via
  ESP/ASPIRATION_SRC → la lecture carnet sort du cœur. Rien n'est forcé.

CONTENU DE aspiration_live.json (écrit en continu, ~1×/LOOP_SEC) :
  { ts, frais, btc_price, gex:{callWall,putWall,ok},
    paires: { SYM: {régime, side, drop_bid_pct_per_s, drop_ask_pct_per_s,
                    max_drop_pct_per_s, spread_bps, spread_delta_bps,
                    wall_bid_usdt, wall_ask_usdt, notional_drop_ok,
                    spoof, price_delta_pct, price, delay_s} } }

USAGE : python3 scripts/satellite_aspiration.py   (boucle continue)
Planifié par launchd com.ace777.satellite-aspiration (StartInterval ~20s via --once
ou boucle interne ; on utilise --once + StartInterval pour la résilience launchd).

Lecture des paires actives : depuis le DERNIER state du moteur (PAPER_V1_*_state.json)
pour connaître le régime de chaque paire (COOLING/IMPULSE = actives). Fail-open :
si pas de state, on ne fait rien.
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
LIVE = RUNS / "aspiration_live.json"
LOOP_SEC = 20.0          # cadence d'écriture (le moteur a une boucle 20s aussi)
# GO 3 du 23/09/2026 (GO Christophe après l'audit MEXC × HULK) — POURQUOI CE CHIFFRE EST PASSÉ
# DE 5 À 20 :
#   L'audit a mesuré que **13 paires sur 20 n'avaient AUCUNE vue live** à l'instant du contrôle :
#   le satellite ne sondait que 5 « actives » (+ les forcées). Pour ces 13 paires, le moteur
#   calcule le cap de mise sur le `mur_bid_med` du PROFIL — un chiffre figé, faux de 8 à 82 %
#   (RIZE : cap 4,88 $ pour un carnet mesuré à 364,74 $).
#   COÛT RÉSEAU, calculé et non supposé : chaque paire = 2 lectures /depth (delay_s=0.5).
#   20 paires ≈ 40 appels par passe ; launchd StartInterval=20 s ⇒ une passe dure ~22 s et la
#   suivante est décalée ⇒ **≈ 80-100 appels/min**, sous le plafond observé de ~200/min
#   (le moteur, lui, fait 1 appel batch de prix par cycle). L'âge d'une vue devient ≤ ~40 s,
#   donc SOUS le seuil « frais » de 45 s du moteur et TRÈS en dessous du `wall_stale_sec` (120 s).
#   RÉVERSIBLE en une ligne (ou par ASPIRATION_MAX_PAIRS=5 dans l'environnement).
MAX_PAIRS = int(os.environ.get("ASPIRATION_MAX_PAIRS", "20"))   # paires sondées par passe
# ── MESURE QUI A CORRIGÉ LE GO 3 LE JOUR MÊME (23/09) ─────────────────────────────────────
# Première version : 20 paires × 2 lectures /depth ⇒ passe de 35,8 s ⇒ avec StartInterval=20 s,
# l'âge de la vue oscillait **4 → 55 s**, donc AU-DESSUS du seuil « frais » de 45 s du moteur →
# **ASPIRATION_STALE — NO_NEW_ENTRIES** (531 lignes dans le log). Le remède n'est pas de
# relâcher le seuil du moteur (ce serait régler le contrôle sur le défaut) mais de redevenir
# rapide : les paires PRIORITAIRES (forcées + actives COOLING/IMPULSE) gardent les 2 lectures
# (elles ont besoin du signal de CHUTE du mur), les autres passent en **1 lecture** — spread
# et mur live, ce dont le CAP a besoin. Coût : ≈ 8×2 + 12×1 = 28 lectures/passe (≈ 80/min).
MAX_PAIRS_PRIO = int(os.environ.get("ASPIRATION_MAX_PAIRS_PRIO", "8"))
MAX_PAIRS_LIGHT = int(os.environ.get("ASPIRATION_MAX_PAIRS_LIGHT", "12"))
# GO Christophe 05/09 : calibration des derniers actifs — ces paires n'ont AUCUN
# corpus (n_mesures=0, profil pré-calibré à la main) → elles sont sondées À CHAQUE
# passe, priorité sur les actives, jusqu'à constitution du corpus (méthodologie
# d'origine : mesurer PUIS calibrer). Retirées de cette liste une fois calibrées.
FORCE_PROBE = ("BTCUSDT", "ETHUSDT", "QNTUSDT", "FLUIDUSDT", "RWAUSDT", "MNSRYUSDT")
STALE_STATE_MAX = 120.0  # un state moteur + vieux que ça = on abandonne la passe
HTTP_TIMEOUT = 12.0

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ace_sense_mexc import aspiration_sense, book_sense  # noqa: E402


def http_json(url, timeout=HTTP_TIMEOUT, retries=1):
    import signal
    import urllib.request

    last_err = None
    for attempt in range(max(1, retries)):
        try:
            prev = signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError("alarm")))
            signal.alarm(int(timeout) + 2)
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "hulk-satellite/1.0"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return json.loads(r.read().decode())
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, prev)
        except Exception as e:
            last_err = e
            time.sleep(0.3 * (attempt + 1))
    raise last_err


def derniere_paires():
    """Lit le dernier state du moteur → {pair: regime}. Fail-open."""

    def to_state(st):
        return st.get("ts"), st.get("scores") or {}

    best = None
    for f in RUNS.glob("PAPER_V1_*_state.json"):
        try:
            ts = f.stat().st_mtime
            if best is None or ts > best[0]:
                best = (ts, f)
        except Exception:
            continue
    if not best:
        return {}
    if time.time() - best[0] > STALE_STATE_MAX:
        return {}
    try:
        st = json.loads(best[1].read_text(encoding="utf-8"))
    except Exception:
        return {}
    scores = st.get("scores") or {}
    pairs_cfg = set(p.strip().upper() for p in (st.get("pairs") or []))
    return {p: ((scores.get(p) or {}).get("regime") or "?") for p in pairs_cfg}


def gex_local():
    """Lit la GEX wall depuis thermo/live.json (fichier local, pas réseau)."""
    try:
        # 2026-09-08 fix GEX path : ROOT pointe hulk-mexc/ mais Index_Maison vit à la racine ace777-test-day1/ (parents[2]) — le gex était ok:false depuis toujours
        _thermo_live = ROOT.parent / "Index_Maison" / "thermo" / "live.json"
        live = json.loads(_thermo_live.read_text())
        gex = live.get("gex") or {}
        return {"ok": bool(gex.get("ok")),
                "callWall": float(gex.get("callWall") or 0),
                "putWall": float(gex.get("putWall") or 0)}
    except Exception:
        return {"ok": False, "callWall": 0, "putWall": 0}


def corpus_write(radar: dict, btc: float):
    """Accumule chaque mesure ok dans un CSV quotidien (GO Christophe 05/09).
    Sans ça, aspiration_live.json est écrasé à chaque passe et RIEN ne s'accumule :
    impossible de calibrer les profils selon la méthodologie (mesurer puis calibrer).
    Même schéma que les ASPIRATION_CALIB du moteur → pipeline d'analyse compatible."""
    try:
        day = time.strftime("%Y%m%d", time.gmtime())
        path = RUNS / f"CORPUS_ASP_{day}.csv"
        new = not path.exists()
        with path.open("a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(
                    ["ts", "pair", "regime", "asp_side", "drop_bid_pct_per_s",
                     "drop_ask_pct_per_s", "max_drop_pct_per_s", "spread_bps",
                     "spread_delta_bps", "wall_bid_usdt", "wall_ask_usdt",
                     "notional_ok", "spoof", "price_delta_pct", "btc_price",
                     "btc_delta_pct", "delay_s", "price"]
                )
            ts_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            for pair, v in radar.items():
                if not v.get("ok"):
                    continue
                w.writerow(
                    [ts_utc, pair, v.get("regime", "?"), v.get("aspiration_side"),
                     v.get("drop_bid_pct_per_s"), v.get("drop_ask_pct_per_s"),
                     v.get("max_drop_pct_per_s"), v.get("spread_bps"),
                     v.get("spread_delta_bps"), v.get("wall_bid_usdt"),
                     v.get("wall_ask_usdt"), v.get("notional_drop_ok"),
                     "", v.get("price_delta_pct"),
                     round(btc, 2), "", v.get("delay_s"), v.get("prix") or 0.0]
                )
            f.flush()
    except Exception as e:
        print(f"[sat-asp] CORPUS_ERR {e}")


def atomic_write(path: Path, data: dict):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def saisir_prix(pairs):
    """1 appel batch → {pair: prix} (même technique que le cœur Phase 1)."""
    out = {}
    try:
        data = http_json("https://api.mexc.com/api/v3/ticker/price")
    except Exception:
        return out
    if isinstance(data, list):
        want = set(pairs)
        for it in data:
            if isinstance(it, dict) and it.get("symbol") in want:
                try:
                    out[it["symbol"]] = float(it["price"])
                except Exception:
                    continue
    return out


def run_once() -> int:
    paires = derniere_paires()
    if not paires:
        # pas de state frais → ne rien écrire (on ne cache pas l'absente)
        return 0
    # ── SÉLECTION (corrigée le 23/09/2026 — GO 3) ───────────────────────────────────────────
    # AVANT : `actives = [paires COOLING/IMPULSE][:5]` puis + FORCE_PROBE. À l'instant de
    # l'audit, cela ne produisait que **7-8 paires** couvertes : les 12-13 autres n'avaient
    # donc AUCUNE vue live, et le moteur calculait leur cap de mise sur le profil figé.
    # MAINTENANT : quand MAX_PAIRS couvre l'univers, on sonde **TOUTES les paires du moteur**,
    # en gardant l'ordre de priorité (forcées → actives → les autres). L'information de régime
    # reste prise dans le state, jamais inventée.
    actives_reg = [p for p, r in paires.items() if r in ("COOLING", "IMPULSE")]
    force = [p for p in FORCE_PROBE if p in paires and p not in actives_reg]
    prio = (force + actives_reg)[: MAX_PAIRS_PRIO]
    # Les « light » prennent TOUT ce qui reste, dans la limite du budget total : sinon une
    # paire hors régime actif pouvait être laissée de côté (mesuré : RIZE manquait la 1re fois).
    autres = [p for p in paires if p not in prio][: max(0, MAX_PAIRS - len(prio))]
    if not autres:
        autres = [p for p in paires if p not in prio][: MAX_PAIRS_LIGHT]
    actives = (prio + autres)[: MAX_PAIRS]
    prix = saisir_prix(list(paires.keys()))
    btc = prix.get("BTCUSDT", 0.0)
    radar = {}

    for pair in actives:
        radar[pair] = {"regime": paires.get(pair, "?"), "prix": prix.get(pair, 0.0)}
        if pair in prio:
            # MODE COMPLET (2 lectures) : le signal de chute du mur est mesuré.
            try:
                a = aspiration_sense(pair, http_json, delay_s=0.5, min_notional_usdt=500)
            except Exception as e:
                radar[pair]["ok"] = False
                radar[pair]["reason"] = f"probe_err:{e}"
                continue
            radar[pair]["ok"] = bool(a.get("ok"))
            radar[pair]["mode"] = "full"
            for k in ("aspiration_side", "drop_bid_pct_per_s", "drop_ask_pct_per_s",
                      "max_drop_pct_per_s", "spread_bps", "spread_delta_bps",
                      "wall_bid_usdt", "wall_ask_usdt", "notional_drop_ok",
                      "price_delta_pct", "delay_s"):
                radar[pair][k] = a.get(k)
        else:
            # MODE LÉGER (1 lecture) : spread + mur LIVE, sans signal de chute.
            # C'est exactement ce dont le CAP DE MISE et le gate de murs ont besoin ; le
            # champ `mode` dit à quiconque lit le fichier ce qui manque ici.
            try:
                b = book_sense(pair, http_json, limit=20)
            except Exception as e:
                radar[pair]["ok"] = False
                radar[pair]["reason"] = f"book_err:{e}"
                continue
            radar[pair]["ok"] = bool(b.get("ok"))
            radar[pair]["mode"] = "light"
            for k in ("spread_bps", "wall_bid_usdt", "wall_ask_usdt"):
                radar[pair][k] = b.get(k)

    LIVE_DATA = {
        "ts": int(time.time()),
        "ts_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        # GO 1 (23/09) : on déclare AUSSI la couverture et l'âge, pour que le moteur et les
        # instruments puissent juger la fraîcheur de la vue au lieu de la supposer.
        "n_paires_univers": len(paires),
        "couverture_pct": round(100.0 * len(actives) / max(1, len(paires)), 1),
        "max_pairs": MAX_PAIRS,
        "frais": True,
        "btc_price": btc,
        "gex": gex_local(),
        "n_actives": len(actives),
        "paires": radar,
        "source": "satellite_aspiration",
        "sat_ok": True,
    }
    try:
        atomic_write(LIVE, LIVE_DATA)
        # ── FLUX WEBSOCKET EN OMBRE (GO 1 du 23/09, ordre Christophe « pourquoi pas les deux ? »)
        # CE QUE ÇA FAIT : on ÉCOUTE le carnet (push, `spot@…bookTicker…@100ms`) au lieu de le
        # DEMANDER deux fois à 0,5 s d'écart. Mesuré : âge médian 14-15 ms et 100 % sous la barre
        # de 1 s du jury, contre 1 058 ms / 22,7 % en REST.
        # POURQUOI EN OMBRE ET PAS EN REMPLACEMENT : le moteur lit `aspiration_live.json`. Tant que
        # les deux sources n'ont pas été comparées sur des données réelles, on AJOUTE (`ws`) sans
        # RIEN retirer — le moteur continue sur les valeurs d'aujourd'hui. Rien de silencieux : le
        # bloc dit lui-même ce qu'il est. Lecture seule, aucun ordre, aucun seuil touché.
        try:
            import ws_book                                            # noqa: PLC0415
            _ws = ws_book.lire_flux(actives, secondes=1.5, pas="100ms")
            _n_ok = 0
            for _p, _d in _ws.items():
                if not _d.get("ok"):
                    radar.setdefault(_p, {})["ws_ok"] = False
                    continue
                _n_ok += 1
                radar[_p].update({
                    "ws_ok": True, "ws_prix": _d["prix"], "ws_spread_bps": _d["spread_bps"],
                    "ws_age_s": _d["age_s"], "ws_n_trames": _d["n"],
                    "ws_drop_bid_pct_per_s": _d["drop_bid_pct_per_s"],
                    "ws_wall_bid_usdt": _d["wall_bid_usdt"], "ws_wall_ask_usdt": _d["wall_ask_usdt"],
                })
            _ws_ecart = []
            for _p, _d in _ws.items():
                _r = radar.get(_p) or {}
                if _d.get("ok") and _r.get("prix") and _d.get("prix"):
                    _ws_ecart.append((_d["prix"] / _r["prix"] - 1) * 100)
            _ws_ecart.sort()

            def _ws_med(v):
                return round(v[len(v) // 2], 4) if v else None

            LIVE_DATA["ws_ombre"] = {
                "ok": True, "n_paires": _n_ok, "source": "flux bookTicker 100ms (protobuf décodé)",
                "ecart_prix_median_pct": _ws_med(_ws_ecart),
                "ecart_prix_max_abs_pct": (round(max(abs(x) for x in _ws_ecart), 4) if _ws_ecart else None),
                "note": "AJOUT, pas remplacement : le moteur lit toujours les valeurs REST ci-dessus. "
                        "Le passage au flux attend la comparaison (et un GO).",
            }
        except Exception as _e:                                     # noqa: BLE001
            LIVE_DATA["ws_ombre"] = {"ok": False, "reason": str(_e)[:120]}
        # RÉÉCRITURE NÉCESSAIRE (faute trouvée en vérifiant, 23/09) : `aspiration_live.json` est
        # écrit AVANT ce bloc, donc mes champs `ws_*` n'apparaissaient JAMAIS dans le fichier lu
        # par le moteur — la mesure était faite puis jetée. On réécrit avec le MÊME écrivain
        # atomique, dans un try : une réécriture qui échoue ne casse pas la passe.
        try:
            atomic_write(RUNS / "aspiration_live.json", LIVE_DATA)
        except Exception:
            pass
        corpus_write(radar, btc)
        print(f"[sat-asp] ts={LIVE_DATA['ts']} actives={len(actives)} "
              f"écrites->{LIVE.name} btc={btc:.0f}")
    except Exception as e:
        print(f"[sat-asp] WRITE_ERR {e}")
        return 1
    return 0


def main() -> int:
    if "--once" in sys.argv:
        return run_once()
    while True:
        try:
            run_once()
        except Exception as e:
            print(f"[sat-asp] ERR {e}")
        time.sleep(LOOP_SEC)
    return 0


if __name__ == "__main__":
    sys.exit(main())