#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2_duo_live.py — MOTEUR LIVE PAPIER DUO (BETA Scout 200$ SL 16 bps + ALPHA Hunter
Revenge 800$), révisé CONFORME à la spec scellée E32 avant lancement.

PROVENANCE (noir sur blanc) : script initial apparu le 17/09 à 22:42 (auteur :
« Supervision Antigravity », agent externe — pas Buffy). Il contenait alors
SL 25 bps et la mention « +133.02$ NET PROUVÉ » SANS AUCUNE SOURCE (aucun fichier
de résultat de la maison ne contient ce chiffre ; notre replay scellé E32 donne
Duo net −64,19 $ = ÉCHEC). Il a été re-modifié PENDANT l'audit de Buffy (22:4x →
0.0016). Buffy le réécrit ici en conformité avec LA SEULE spec scellée (E32,
règles originelles du champion certifié 37FCA367, SHA 7d1ed5f6) — lancements
et consignations dans engle/JOURNAL_ERREURS.md E33.

SPÉCIFICATION FIGÉE AVANT LANCEMENT (directive LIVE COCKPIT 17/09 + spec E32) :
  SIGNAL D'ENTRÉE SCOUT (LONG uniquement) :
    - Régime macro 1D STRICT : HAUSSIER (SMA 50/200 causales sur clôtures 1D) ;
    - au moins 2 confirmations/3 (directive Duo-live du propriétaire) :
        C1 funding actuel > moyenne 30 j      (indisponible si avg30 absent)
        C2 flux baleines 48 h ≥ +5 BTC        (indisponible si ledger absent —
                                               calculé sur whales_mouvements.jsonl,
                                               dédup txid, direction vs registre)
        C3 chute 4H ≤ −0,5 %                  (clôture 4H vs clôture 4H précédente)
    - veto négatif seul : funding actuel ≤ 0 → aucune entrée (GO 4H du 17/09).
  BETA SCOUT : 200 $ · SL 16 bps (STOP_LOSS_BPS l.55 champion) · trailing σ4h
    arm 1,0σ / giveback 0,4σ (convention maison scellée — l'initial « 1,2/0,3 »
    non scellé est rétabli à la convention E32) · σ4h = écart-type des rendements
    des 30 dernières bougies 4H closes.
  ALPHA HUNTER REVENGE : si et seulement si le Scout ferme PAR STOP-LOSS →
    entrée au prix du stop, 800 $, sens OPPOSÉ (DUO_FORCE_OPPOSITE=TRUE l.321 —
    l'initial prenait toujours LONG, non conforme) · hard stop 32 bps
    (DUO_HUNTER_HARD_STOP_MULT=2.0 l.323) · trail agressif arm +2 bps /
    giveback +1 bp (l.334-335) · durée max 240 s (DUO_HUNTER_MAX_HOLD_SEC l.322,
    l'initial n'avait AUCUNE sortie en perte : position 800 $ pouvait rester
    ouverte toute la nuit — corrigé) · résolution d'exécution : cycle 10 s.
  ÉCONOMIE : frais 16 bps AR → Scout 0,32 $ · Hunter 1,28 $.
  ARRÊT : programmé à 07h00 HEURE LOCALE (= 05:00 UTC — le code initial faisait
    déjà ça, seul son libellé « 07h00 UTC » était faux).
  PAPIER : zéro clé API, zéro ordre, lecture seule des endpoints publics Binance.
  ÉCRITURES : thermo/v2conf_etat.json (affiché par v2conf_live.sh),
    thermo/v2conf_log.jsonl, thermo/v2conf_trades.jsonl, stdout log visible.
"""
import json
import math
import statistics
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ------------------------- constantes figées (spec E32) --------------
NOTIONNEL_SCOUT = 200.0
NOTIONNEL_HUNTER = 800.0
FRAIS_SCOUT_AR = 0.32
FRAIS_HUNTER_AR = 1.28
SL_SCOUT_BPS = 0.0016            # 16 bps — champion l.55
HARD_STOP_HUNTER = 0.0032        # 32 bps = 2 × 16 — l.323
TRAIL_ARM_HUNTER = 0.0002        # 2 bps — l.334
TRAIL_GIVE_HUNTER = 0.0001       # 1 bp — l.335
SIGMA_ARM_SCOUT, SIGMA_GIVE_SCOUT = 1.0, 0.4   # convention scellée E32
SEUIL_FLUX_BTC = 5.0
CHG4H_PANIQUE_PCT = 0.5          # % — directive Duo-live
VETO_FUNDING_NEG = 0.0
HUNTER_MAX_HOLD_S = 240          # l.322
FLUX_FIABLE_DES = "2026-08-14"   # masque R2 (aujourd'hui 17/09 : fiable)

SPOT_URL = "https://api.binance.com/api/v3/klines"
FUT_URL = "https://fapi.binance.com/fapi/v1/klines"
FUND_URL = "https://fapi.binance.com/fapi/v1/fundingRate"

BASE = Path.home() / "ace777-test-day1"
TH = BASE / "Index_Maison/thermo"
ETAT_FILE = TH / "v2conf_etat.json"
LOG_FILE = TH / "v2conf_log.jsonl"
TRADES_FILE = TH / "v2conf_trades.jsonl"

def z(): return datetime.now(timezone.utc)

def log(msg, **kw):
    ligne = {"ts": z().strftime("%Y-%m-%dT%H:%M:%SZ"), "msg": msg, **kw}
    try:
        TH.mkdir(parents=True, exist_ok=True)
        with LOG_FILE.open("a") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:
        pass

def http_json(url):
    try:
        r = subprocess.run(["curl", "-s", "-m", "20", url], capture_output=True, text=True, timeout=25)
        return json.loads(r.stdout)
    except Exception:
        return []

def get_klines_4h():
    kl = http_json(SPOT_URL + "?symbol=BTCUSDT&interval=4h&limit=200") or \
         http_json(FUT_URL + "?symbol=BTCUSDT&interval=4h&limit=200")
    out = []
    for k in (kl or []):
        out.append({"t": int(k[0]), "o": float(k[1]), "h": float(k[2]),
                    "l": float(k[3]), "c": float(k[4])})
    return out

def get_closes_1d():
    kl = http_json(SPOT_URL + "?symbol=BTCUSDT&interval=1d&limit=400") or \
         http_json(FUT_URL + "?symbol=BTCUSDT&interval=1d&limit=400")
    return [float(k[4]) for k in (kl or [])]

def get_funding():
    data = http_json(FUND_URL + "?symbol=BTCUSDT&limit=100")
    pts = [float(x["fundingRate"]) for x in (data or [])]
    dernier = pts[-1] if pts else None
    avg30 = statistics.mean(pts[-90:]) if len(pts) >= 10 else None
    return dernier, avg30

def flux_net_48h():
    """Ledger dédup txid, direction vs registre — copie fidèle du replay scellé.
    None-safe : retourne None si données absentes (porte indisponible)."""
    ledger = BASE / "Index_Maison/data/whales_mouvements.jsonl"
    registre = BASE / "Index_Maison/data/whales.json"
    try:
        ex = {p["address"] for p in json.loads(registre.read_text()).get("portefeuilles", [])
              if p.get("type") in {"exchange_hot", "exchange_cold", "exchange_reserve"}}
        par_txid = {}
        for line in ledger.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            txid = o.get("txid") or ""
            if not txid:
                continue
            e = par_txid.get(txid)
            if e is None:
                par_txid[txid] = {"ts": o.get("ts", ""), "ligne": o}
            elif o.get("ts", "") < e["ts"]:
                par_txid[txid]["ts"] = o.get("ts", "")
        d1 = z()
        d0 = d1 - timedelta(hours=48)
        net = 0.0
        for e in par_txid.values():
            try:
                t = datetime.strptime(e["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if d0 <= t < d1:
                m = e["ligne"]
                try:
                    btc = max(float(m.get("btc") or 0.0), 0.0)
                except (TypeError, ValueError):
                    continue
                src = set(m.get("sources") or [])
                dst = {c.get("adresse") for c in (m.get("cibles") or []) if c.get("adresse")}
                if src & ex and not dst & ex:
                    net -= btc          # SORTANT
                elif dst & ex and not src & ex:
                    net += btc          # ENTRANT
        return net
    except Exception:
        return None

def main():
    log("=== DEMARRAGE DUO LIVE PAPIER — spec scellee E32 (Scout 200$ SL16bps, "
        "Hunter 800$ oppose hard-stop 32bps, duree max 240s) — FIN 07h00 locale ===")

    # arrêt à 07h00 heure locale = 05:00 UTC demain (si lancé avant 05:00 UTC)
    target_end = z().replace(hour=5, minute=0, second=0, microsecond=0)
    if target_end <= z():
        target_end += timedelta(days=1)

    trades = []
    pos_scout = None
    pos_hunter = None
    pending_revenge = None          # (prix_stop, ts_stop) — tire une seule fois

    while z() < target_end:
        try:
            kl4h = get_klines_4h()
            closes1d = get_closes_1d()
            last_f, avg30_f = get_funding()

            if len(closes1d) >= 200:
                s50 = sum(closes1d[-50:]) / 50
                s200 = sum(closes1d[-200:]) / 200
                regime = "HAUSSIER" if s50 > s200 else ("BAISSIER" if s50 < s200 else "NEUTRE")
            else:
                regime = "NEUTRE"

            current_px = kl4h[-1]["c"] if kl4h else 0.0
            chg4h = ((kl4h[-1]["c"] / kl4h[-2]["c"]) - 1) * 100.0 if len(kl4h) >= 2 and kl4h[-2]["c"] else 0.0
            s4h = (statistics.pstdev([math.log(kl4h[k]["c"] / kl4h[k-1]["c"])
                                      for k in range(len(kl4h)-30, len(kl4h))])
                   if len(kl4h) >= 31 else None) or 0.0
            net48 = None                      # fuite mémoire évitée : réinit chaque cycle

            # ---------- Scout : sorties (SL d'abord — pessimiste) ----------
            if pos_scout:
                stop_px = pos_scout["entree"] * (1.0 - SL_SCOUT_BPS)
                if current_px <= stop_px:
                    brut = (stop_px - pos_scout["entree"]) / pos_scout["entree"] * NOTIONNEL_SCOUT
                    net = brut - FRAIS_SCOUT_AR
                    t = {"entree_j": pos_scout["ts"], "side": "BETA (Scout)",
                         "net": round(net, 2), "raison": "stop_loss_16bps",
                         "entree": pos_scout["entree"], "sortie": round(stop_px, 2)}
                    trades.append(t)
                    log(f"SCOUT STOPPE -> Perte {net:.2f} $", trade=t)
                    pos_scout = None
                    pending_revenge = {"prix": stop_px, "ts": z()}   # Revenge armée
                else:
                    pos_scout["mfp"] = max(pos_scout["mfp"], current_px)
                    arm_px = pos_scout["entree"] * (1.0 + SIGMA_ARM_SCOUT * s4h)
                    if pos_scout["mfp"] >= arm_px:
                        gb = pos_scout["mfp"] - SIGMA_GIVE_SCOUT * s4h * pos_scout["entree"]
                        if current_px <= gb:
                            brut = (gb - pos_scout["entree"]) / pos_scout["entree"] * NOTIONNEL_SCOUT
                            net = brut - FRAIS_SCOUT_AR
                            t = {"entree_j": pos_scout["ts"], "side": "BETA (Scout)",
                                 "net": round(net, 2), "raison": "trailing_profit",
                                 "entree": pos_scout["entree"], "sortie": round(gb, 2)}
                            trades.append(t)
                            log(f"SCOUT SORTI GAIN -> Net {net:.2f} $", trade=t)
                            pos_scout = None

            # ---------- Hunter : gestion (hard stop d'abord, puis trail, puis durée) ----------
            if pos_hunter:
                held = (z() - pos_hunter["t_entree"]).total_seconds()
                e0 = pos_hunter["entree"]
                exit_px, raison = None, None
                if current_px >= e0 * (1.0 + HARD_STOP_HUNTER):      # hard stop 32 bps
                    exit_px, raison = e0 * (1.0 + HARD_STOP_HUNTER), "hard_stop_32bps"
                elif held >= HUNTER_MAX_HOLD_S:                       # durée max 240 s
                    exit_px, raison = current_px, "duree_max_240s"
                else:
                    pos_hunter["mfp"] = min(pos_hunter["mfp"], current_px)   # SHORT
                    if pos_hunter["mfp"] <= e0 * (1.0 - TRAIL_ARM_HUNTER):
                        gb = pos_hunter["mfp"] * (1.0 + TRAIL_GIVE_HUNTER)   # giveback DERRIÈRE
                        if current_px >= gb:
                            exit_px, raison = gb, "trail_agressif"
                if exit_px is not None:
                    brut = (e0 - exit_px) / e0 * NOTIONNEL_HUNTER
                    net = brut - FRAIS_HUNTER_AR
                    t = {"entree_j": pos_hunter["ts"], "side": "ALPHA (Hunter)",
                         "net": round(net, 2), "raison": raison,
                         "entree": e0, "sortie": round(exit_px, 2)}
                    trades.append(t)
                    log(f"HUNTER FERME ({raison}) -> Net {net:.2f} $", trade=t)
                    pos_hunter = None

            # ---------- Hunter Revenge : entrée (sens OPPOSÉ au Scout = SHORT) ----------
            if pending_revenge and pos_hunter is None and pos_scout is None:
                p0 = pending_revenge["prix"]
                pos_hunter = {"side": "ALPHA SHORT (opposé)", "entree": p0,
                              "mfp": p0, "ts": z().strftime("%H:%M:%S"),
                              "t_entree": z()}
                log(f"HUNTER REVENGE ENTRE -> SHORT 800 $ au stop du Scout {p0:.2f} $ (opposé, l.321)")
                pending_revenge = None

            # ---------- Scout : entrée (régime HAUSSIER strict + 2/3 confirmations) ----------
            if pos_scout is None and pos_hunter is None and pending_revenge is None:
                confirmations, indispo_msgs, portes_dispo = [], [], 0
                # C1 funding > avg30 (None-safe : indisponible ≠ confirmation)
                if last_f is not None and avg30_f is not None:
                    portes_dispo += 1
                    if last_f > avg30_f:
                        confirmations.append(f"funding {last_f:.2e} > avg30 {avg30_f:.2e}")
                else:
                    indispo_msgs.append("funding INDISPONIBLE")
                # C2 flux baleines 48 h ≥ +5 BTC (None-safe)
                net48 = flux_net_48h()
                if net48 is not None:
                    portes_dispo += 1
                    if net48 >= SEUIL_FLUX_BTC:
                        confirmations.append(f"flux {net48:+.1f} BTC ≥ +5")
                else:
                    indispo_msgs.append("flux INDISPONIBLE")
                # C3 panique 4H ≤ −0,5 %
                portes_dispo += 1
                if chg4h <= -CHG4H_PANIQUE_PCT:
                    confirmations.append(f"chute 4H {chg4h:.2f} % ≤ −0,5")
                # veto négatif seul
                if last_f is not None and last_f <= VETO_FUNDING_NEG:
                    log("aucune entrée", detail="veto funding<=0", regime=regime,
                        funding=last_f, flux48=net48, prix_ref=current_px)
                elif regime == "HAUSSIER" and len(confirmations) >= 2:
                    pos_scout = {"side": "BETA LONG", "entree": current_px,
                                 "mfp": current_px, "ts": z().strftime("%H:%M:%S"),
                                 "t_entree": z(), "confirmations": list(confirmations)}
                    log(f"SCOUT ENTRE -> LONG 200 $ à {current_px:.2f} $",
                        confirmations=confirmations)
                else:
                    log("aucune entrée", detail=f"{len(confirmations)}/3 confirmations (+ {len(indispo_msgs)} indispo), portes dispo {portes_dispo}",
                        regime=regime, funding=last_f, flux48=net48, prix_ref=current_px)

            # ---------- état pour v2conf_live.sh ----------
            etat = {
                "dernier_cycle": z().strftime("%Y-%m-%d %H:%M:%S UTC"),
                "contexte": {
                    "regime": regime,
                    "funding": last_f,
                    "flux48_btc": net48 if net48 is not None else 0.0,
                    "chg24_pct": chg4h,
                    "prix_ref": current_px,
                    "sigma_jour": s4h
                },
                "position": {
                    "side": pos_scout["side"] if pos_scout else (pos_hunter["side"] if pos_hunter else None),
                    "dir": 1 if (pos_scout or pos_hunter) else 0,
                    "entree": (pos_scout["entree"] if pos_scout else
                               (pos_hunter["entree"] if pos_hunter else 0)),
                    "arm": ((pos_scout["entree"] * (1 + SIGMA_ARM_SCOUT * s4h)) if pos_scout else
                            ((pos_hunter["entree"] * (1 - TRAIL_ARM_HUNTER)) if pos_hunter else 0)),
                    "jour": (pos_scout["ts"] if pos_scout else
                             (pos_hunter["ts"] if pos_hunter else "")),
                    "confirmations": (pos_scout.get("confirmations", []) if pos_scout else
                                      ["opposé au Scout stoppé — hard stop 32 bps, max 240 s"] if pos_hunter else [])
                } if (pos_scout or pos_hunter) else None,
                "trades": trades
            }
            ETAT_FILE.write_text(json.dumps(etat, indent=2, ensure_ascii=False))
            deja = getattr(main, "_n_logues", 0)
            if len(trades) > deja:
                with TRADES_FILE.open("a") as f:
                    for t in trades[deja:]:
                        f.write(json.dumps(t, ensure_ascii=False) + "\n")
                main._n_logues = len(trades)

            log("cycle OK", regime=regime, funding=last_f, flux48=net48, prix_ref=current_px)

        except Exception as e:
            log(f"ERREUR cycle: {e}")

        time.sleep(10)

    log("=== FIN PROGRAMMEE DUO LIVE (07h00 locale atteinte) ===")

if __name__ == "__main__":
    main()
