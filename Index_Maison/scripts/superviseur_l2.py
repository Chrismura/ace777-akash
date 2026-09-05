#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUPERVISEUR L2 PASSIF — lecture seule, zéro ordre, zéro clé (protocole R32, feu vert famille).
Rôle :
  1. Corpus pour le bras D (relais OFI + trigger dérivée seconde) — jamais rejouable si non capté.
  2. Calibration « mur institutionnel BTC » en notionnel (inexistante à ce jour — décision famille).
  3. Détection évaporation / annulation-sans-exécution (Ruse 2, prouvée chez Hulk).

Ce qu'il fait :
  - REST /fapi/v1/depth?symbol=BTCUSDT&limit=50 sondé 1×/s (poids ~5, limite 2400/min → très large)
  - Écrit 2 CSV dédiés (jamais touchés par le shadow/champion) :
      runs/L2_YYYYMMDD_SNAPS.csv  : 1 ligne/s (ts, mid, spread, bid1_px/sz, ask1_px/sz, md5 carnet)
      runs/L2_YYYYMMDD_MURS.csv   : 1 ligne par événement mur (APPARU / EVAPORE / FRANCHI)
  - Mur = niveau dont le notionnel dépasse le seuil courant (médiane glissante des top-50 × facteur,
    borné [50k ; 2M] USDT) — calibration RELATIVE, leçon Hulk, pas de seuil absolu figé.
  - Flag SPOOF (méthode validée de Hulk, observer_murs.py) : mur qui FOND puis SE RECONSTRUIT
    au même niveau dans la fenêtre SPOOF_WINDOW → événement "SPOOF" dans le CSV murs.
    Le mur de façade n'est jamais un bouclier : cette information nourrira le FPC (V3).
  - Arrêt propre : touch runs/STOP_L2
Usage :
  python3 superviseur_l2.py            # tourne jusqu'à STOP_L2
  RUN_SEC=900 python3 superviseur_l2.py  # auto-stop après 900 s (test)
"""
import csv, hashlib, json, os, statistics, time, urllib.request
from collections import deque
from datetime import datetime, timezone

RUNS = os.path.expanduser("~/ace777-test-day1/runs")
URL = "https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=50"
MUR_FACTOR = 8.0            # un mur = 8× la médiane notionnelle des niveaux visibles
MUR_BORNES = (50_000.0, 2_000_000.0)
MED_WINDOW = 600            # fenêtre glissante de la médiane (10 min de snapshots)
SNAP_EVERY = 1.0            # 1 snapshot/s
RUN_SEC = int(os.environ.get("RUN_SEC", "0"))  # 0 = jusqu'à STOP_L2
# --- Méthode SPOOF validée de Hulk (observer_murs.py) : mur qui fond puis se reconstruit ---
SPOOF_WINDOW = 120          # fenêtre (s) : réapparition au même niveau ≤ 120s → mur de façade
                            # (Hulk : fond ≥15%/s puis reconstruit ; ici cadence 1s, même logique)

day = datetime.now(timezone.utc).strftime("%Y%m%d")
snaps_path = os.path.join(RUNS, f"L2_{day}_SNAPS.csv")
murs_path = os.path.join(RUNS, f"L2_{day}_MURS.csv")
stop_path = os.path.join(RUNS, "STOP_L2")
pid_path = os.path.join(RUNS, "l2.pid")

SNAP_COLS = ["ts", "mid", "spread", "bid1_px", "bid1_sz", "ask1_px", "ask1_sz",
             "med_notional", "mur_seuil", "n_bids", "n_asks"]
MUR_COLS = ["ts", "side", "px", "notional", "event"]


def get_depth():
    with urllib.request.urlopen(URL, timeout=10) as r:
        return json.loads(r.read().decode())


def wall_lines(levels):
    """[(px, notional)] des niveaux ; notional = px × qty."""
    out = []
    for px_s, qty_s in levels:
        px, qty = float(px_s), float(qty_s)
        out.append((px, px * qty))
    return out


def main():
    # hygiène : pas de double instance — pidfile géré par le LAUNCHER bash seul
    # (v2 : le python n'écrit plus le pidfile — évite la course bash/python qui
    #  laissait des pidfiles fantômes et bloquait le lancement du propriétaire)
    if os.path.exists(pid_path):
        try:
            old = int(open(pid_path).read().strip())
            os.kill(old, 0)
            print(f"L2 déjà actif (pid {old}) — sortie.")
            return
        except (ValueError, ProcessLookupError, PermissionError):
            os.remove(pid_path)   # pidfile fantôme (process mort) → nettoyer et continuer

    new_snaps = not os.path.exists(snaps_path)
    new_murs = not os.path.exists(murs_path)
    fs = open(snaps_path, "a", newline="")
    fm = open(murs_path, "a", newline="")
    ws = csv.DictWriter(fs, SNAP_COLS)
    wm = csv.DictWriter(fm, MUR_COLS)
    if new_snaps:
        ws.writeheader()
    if new_murs:
        wm.writeheader()

    med_notional = 10_000.0     # départ prudent, converge en ~10 min
    med_hist = deque(maxlen=MED_WINDOW)
    prev_walls = {}             # {(side, px_arrondi): notional} du snapshot précédent
    evap_hist = {}              # {(side, px): ts} — murs évaporés récemment (détection SPOOF)
    t_start = time.time()
    n_snap = n_mur = n_err = n_spoof = 0

    print(f"L2_ON pid={os.getpid()} day={day}")
    print(f"  snaps : {snaps_path}")
    print(f"  murs  : {murs_path}")
    print(f"  seuil mur : {MUR_FACTOR}× médiane notionnelle, bornes {MUR_BORNES}")
    print(f"  stop  : touch {stop_path}" + (f"  | auto-stop après {RUN_SEC}s" if RUN_SEC else ""))

    try:
        while True:
            if os.path.exists(stop_path):
                print("STOP_L2 détecté — arrêt propre.")
                break
            if RUN_SEC and (time.time() - t_start) >= RUN_SEC:
                print(f"RUN_SEC={RUN_SEC}s atteint — auto-stop.")
                break
            t0 = time.time()
            try:
                d = get_depth()
                bids = wall_lines(d["bids"])
                asks = wall_lines(d["asks"])
                now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

                # snapshot
                if bids and asks:
                    mid = (bids[0][0] + asks[0][0]) / 2
                    spread = asks[0][0] - bids[0][0]
                    for _, notional in bids + asks:
                        med_hist.append(notional)
                    if len(med_hist) >= 100:
                        med_notional = statistics.median(med_hist)
                    mur_seuil = max(MUR_BORNES[0], min(MUR_BORNES[1], MUR_FACTOR * med_notional))
                    ws.writerow({
                        "ts": now, "mid": f"{mid:.1f}", "spread": f"{spread:.2f}",
                        "bid1_px": f"{bids[0][0]:.1f}", "bid1_sz": f"{bids[0][1]/bids[0][0]:.4f}",
                        "ask1_px": f"{asks[0][0]:.1f}", "ask1_sz": f"{asks[0][1]/asks[0][0]:.4f}",
                        "med_notional": f"{med_notional:.0f}", "mur_seuil": f"{mur_seuil:.0f}",
                        "n_bids": len(bids), "n_asks": len(asks),
                    })
                    fs.flush()
                    n_snap += 1

                    # événements murs (comparaison au snapshot précédent)
                    cur = {}
                    for side, levels in (("BID", bids), ("ASK", asks)):
                        for px, notional in levels:
                            if notional >= mur_seuil:
                                key = (side, round(px, 1))
                                cur[key] = notional
                                if key not in prev_walls:
                                    wm.writerow({"ts": now, "side": side, "px": f"{px:.1f}",
                                                 "notional": f"{notional:.0f}", "event": "APPARU"})
                                    n_mur += 1
                    for key, notional in prev_walls.items():
                        if key not in cur:
                            wm.writerow({"ts": now, "side": key[0], "px": f"{key[1]:.1f}",
                                         "notional": f"{notional:.0f}", "event": "EVAPORE"})
                            n_mur += 1
                            evap_hist[key] = t0   # mémoriser pour la détection SPOOF (méthode Hulk)
                    # SPOOF (leçon Hulk) : réapparition d'un mur évaporé au MÊME niveau
                    # dans la fenêtre SPOOF_WINDOW → le mur est de façade, pas un bouclier.
                    for key in list(cur.keys()):
                        if key in evap_hist and (t0 - evap_hist[key]) <= SPOOF_WINDOW:
                            wm.writerow({"ts": now, "side": key[0], "px": f"{key[1]:.1f}",
                                         "notional": f"{cur[key]:.0f}", "event": "SPOOF"})
                            n_mur += 1; n_spoof += 1
                            del evap_hist[key]   # consommer l'évaporation (1 spoof = 1 event)
                    # purger les vieilles évaporations hors fenêtre
                    for k in [k for k, ts_e in evap_hist.items() if (t0 - ts_e) > SPOOF_WINDOW]:
                        del evap_hist[k]
                    prev_walls = cur
                    if n_mur:
                        fm.flush()
            except Exception:
                n_err += 1

            # cadence 1 Hz
            dt = time.time() - t0
            if dt < SNAP_EVERY:
                time.sleep(SNAP_EVERY - dt)
            if n_snap % 60 == 0 and n_snap:
                print(f"  {n_snap} snapshots | {n_mur} événements | {n_spoof} spoof | {n_err} erreurs", flush=True)
    finally:
        fs.close()
        fm.close()
        print(f"L2_OFF | {n_snap} snapshots, {n_mur} événements ({n_spoof} spoof), {n_err} erreurs")


if __name__ == "__main__":
    main()
