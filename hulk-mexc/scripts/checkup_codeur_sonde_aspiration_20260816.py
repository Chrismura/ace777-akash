#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CHECK-UP POST-IMPLÉMENTATION — CODEUR (task code.ia) : SONDE ASPIRATION (16/08/2026).

Le code a été implémenté et tourne (mode observation 48h). On envoie le CODE RÉEL
au codeur via le task officiel code.ia (chaîne provider/fallback/secondary du hub).

CLAUSE PERMANENTE (gravée 16/08 par Christophe, applicable à TOUS les prompts) :
« Ne te contente pas de corriger ou de valider : si tu proposes AUTRE CHOSE
(approche différente, autre architecture) ou une AMÉLIORATION qui a du sens,
dis-le explicitement. Corriger n'est pas suffisant : proposer est attendu. »
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CHECKUP_SONDE_ASPIRATION_20260816")
os.makedirs(OUT, exist_ok=True)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CODE_ASPIRATION_SENSE = '''\
def aspiration_sense(pair, http_json, delay_s=0.5, min_notional_usdt=500.0, limit=20):
    """ASPIRATION (inspiration ACE V8) — DOUBLE lecture du carnet à ~delay_s d'écart.
    Métaphore « verre d'eau » (Christophe) : un mur qui fond = vide créé → le prix
    est aspiré vers lui. Mode OBSERVATION : renvoie les mesures, n'agit PAS sur le
    moteur. Fail-open : si la 2e lecture échoue → lecture simple, jamais de blocage."""
    q = urllib.parse.urlencode({"symbol": pair, "limit": limit})
    def _one():
        j = http_json(f"https://api.mexc.com/api/v3/depth?{q}")
        bids = [(float(p), float(q_)) for p, q_ in j.get("bids", [])]
        asks = [(float(p), float(q_)) for p, q_ in j.get("asks", [])]
        if not bids or not asks:
            return {"ok": False, "reason": "empty_book"}
        best_bid, best_ask = bids[0][0], asks[0][0]
        mid = (best_bid + best_ask) / 2.0
        spread_bps = (best_ask - best_bid) / mid * 10000.0 if mid > 0 else 9999.0
        wall_bid = max((p * q_ for p, q_ in bids), default=0.0)
        wall_ask = max((p * q_ for p, q_ in asks), default=0.0)
        return {"ok": True, "spread_bps": spread_bps,
                "wall_bid_usdt": wall_bid, "wall_ask_usdt": wall_ask}
    try:
        d1 = _one()
        if not d1.get("ok"):
            return {"ok": False, "reason": d1.get("reason", "book1_fail")}
        t1 = time.time()
        time.sleep(delay_s)
        d2 = _one()
        t2 = time.time()
        if not d2.get("ok"):
            return {"ok": False, "reason": d2.get("reason", "book2_fail"), "partial": True}
    except Exception as e:
        return {"ok": False, "reason": f"asp_err:{e}", "partial": True}
    dt = max(t2 - t1, 0.05)
    def _drop(m1, m2):
        if m1 <= 0: return 0.0
        return (m1 - m2) / m1 * 100.0
    drop_bid = _drop(d1["wall_bid_usdt"], d2["wall_bid_usdt"])
    drop_ask = _drop(d1["wall_ask_usdt"], d2["wall_ask_usdt"])
    drop_bid_per_s = drop_bid / dt   # NORMALISÉ par le temps réel (correction GROK)
    drop_ask_per_s = drop_ask / dt
    max_drop = max(drop_bid, drop_ask)
    max_drop_per_s = max_drop / dt
    aspiration_side = "BUY" if drop_ask >= drop_bid else "SELL"
    if max_drop <= 0.0:
        aspiration_side = "NONE"
    spread_delta_bps = d2["spread_bps"] - d1["spread_bps"]
    ref_wall = d1["wall_ask_usdt"] if aspiration_side == "BUY" else d1["wall_bid_usdt"]
    notional_drop_ok = ref_wall >= min_notional_usdt
    return {"ok": True, "reason": "ok", "spread_bps": round(d2["spread_bps"], 2),
            "spread_delta_bps": round(spread_delta_bps, 2),
            "drop_bid_pct": round(drop_bid, 2), "drop_ask_pct": round(drop_ask, 2),
            "drop_bid_pct_per_s": round(drop_bid_per_s, 2),
            "drop_ask_pct_per_s": round(drop_ask_per_s, 2),
            "max_drop_pct_per_s": round(max_drop_per_s, 2),
            "aspiration_side": aspiration_side,
            "wall_bid_usdt": round(d1["wall_bid_usdt"], 2),
            "wall_ask_usdt": round(d1["wall_ask_usdt"], 2),
            "notional_drop_ok": notional_drop_ok, "delay_s": round(dt, 3)}
'''

CODE_PROBE = '''\
def probe_aspiration(self, n_cycle):
    """Sonde aspiration — MODE OBSERVATION. Double lecture du carnet sur les paires
    ACTIVES (régime COOLING/IMPULSE) seulement, max ASPIRATION_MAX_PAIRS par probe,
    toutes les ASPIRATION_PROBE_EVERY cycles (rate-limit MEXC). ZÉRO effet sur le
    moteur : log + radar + CSV calibration. Spoof « rétractable à maintenant »
    (Christophe) : mur fond puis reconstruit → spoof pour CETTE lecture, réévalué à
    chaque échantillon (debounce, pas de ban, pas de timer)."""
    if not self.aspiration_on or n_cycle % self.aspiration_probe_every != 0:
        return
    active = [p for p in self.pairs
              if (self.scores.get(p) or {}).get("regime") in ("COOLING", "IMPULSE")]
    if not active:
        return
    active = active[: self.aspiration_max_pairs]
    for pair in active:
        try:
            price = last_price(pair)
        except Exception:
            price = 0.0
        try:
            a = aspiration_sense(pair, http_json, delay_s=self.aspiration_delay_s,
                                 min_notional_usdt=self.aspiration_min_notional)
        except Exception as e:
            a = {"ok": False, "reason": f"probe_err:{e}", "partial": True}
        if not a.get("ok"):
            continue
        spoof = False
        prev = self.aspiration_prev.get(pair)
        drop_now = max(abs(float(a.get("drop_bid_pct_per_s") or 0)),
                       abs(float(a.get("drop_ask_pct_per_s") or 0)))
        if prev and drop_now >= 15.0:
            side = a.get("aspiration_side")
            if side == "BUY":
                w_prev, w_now = prev.get("wall_ask_usdt", 0), float(a.get("wall_ask_usdt") or 0)
            elif side == "SELL":
                w_prev, w_now = prev.get("wall_bid_usdt", 0), float(a.get("wall_bid_usdt") or 0)
            else:
                w_prev, w_now = 0.0, 0.0
            if w_prev > 0 and abs(w_now - w_prev) / w_prev <= 0.10:
                spoof = True
        self.aspiration_prev[pair] = {
            "wall_bid_usdt": float(a.get("wall_bid_usdt") or 0),
            "wall_ask_usdt": float(a.get("wall_ask_usdt") or 0),
            "ts": time.time()}
        a["spoof"] = spoof
        a["price"] = price
        a["regime"] = (self.scores.get(pair) or {}).get("regime", "?")
        self.aspiration[pair] = a
        with self.aspiration_csv.open("a", newline="") as f:
            csv.writer(f).writerow([utc_now(), pair, a["regime"], a.get("aspiration_side"),
                a.get("drop_bid_pct_per_s"), a.get("drop_ask_pct_per_s"),
                a.get("max_drop_pct_per_s"), a.get("spread_bps"),
                a.get("spread_delta_bps"), a.get("wall_bid_usdt"),
                a.get("wall_ask_usdt"), a.get("notional_drop_ok"),
                spoof, a.get("delay_s"), price])
'''

BRIEF = f"""\
CONTEXTE (superviseur Buffy, 16/08/2026 soir) — CHECK-UP CODEUR post-implémentation :
SONDE ASPIRATION HULK — le code RÉEL tourne, vérifie-le (pas un plan).

=== LE SYSTÈME ===
HULK = paper trading dip&rip sur MEXC spot (~15 paires small caps). Le moteur
(scripts/paper_diprip.py) importe scripts/ace_sense_mexc.py : book_sense() (1 lecture
carnet : spread, profondeur, imbalance, murs wall_bid_usdt/wall_ask_usdt) + tension_score()
+ entry_gate() + aspiration_sense() (NOUVEAU, double lecture). Config ASPIRATION_* dans
config/defaults.env.

=== LA DEMANDE (Christophe, 16/08) ===
« Je veux qu'il sonde comme ACE : voir les murs de liquidité, l'aspiration, l'historique
qui fait parti pris — l'intelligence si c'est possible. »
« pas de 15 minutes, 3-2 s... rétractable à maintenant » (spoof = debounce par lecture,
PAS de ban/timer — réévalué à chaque échantillon).

=== CE QUI A ÉTÉ DÉCIDÉ AVANT (consensus) ===
Codeur 4/4 GO-AVEC-RÉSERVE · Famille 6/6 GO-AVEC-RÉSERVE (drop normalisé par temps réel,
mur ≥ 500$, croisement spread_delta) · Cortana GO-RÉSERVES + anti-spoof · Christophe :
spoof « rétractable à maintenant ». Décision finale : MODE OBSERVATION 48h, zéro effet
sur les entrées, seuil calibré sur données réelles après.

=== LE CODE RÉEL (extraits des fichiers implémentés, ce qui tourne) ===
aspiration_sense() dans ace_sense_mexc.py :
{CODE_ASPIRATION_SENSE}

probe_aspiration() dans paper_diprip.py (appelée dans la boucle run(), radar + CSV) :
{CODE_PROBE}

Config (config/defaults.env) :
  ASPIRATION_ON=1 · ASPIRATION_DELAY_S=0.5 · ASPIRATION_MIN_NOTIONAL_USDT=500
  ASPIRATION_PROBE_EVERY=3 · ASPIRATION_MAX_PAIRS=5
Radar : ligne « asp=SIDE drop=X.XX%/s Δspread=Y.Ybps [<500$] [SPOOF] » par paire active.
CSV calibration : runs/ASPIRATION_CALIB_*.csv (ts, pair, regime, side, drops, spread,
walls, notional_ok, spoof, delay_s, price).

=== VÉRIFICATIONS FAITES (preuves) ===
- py_compile OK (paper_diprip.py + ace_sense_mexc.py).
- Capteur testé live XRPUSDT/RIZEUSDT : ok=True, side=NONE (marché calme).
- Hulk relancé via watchdog, run PAPER_V1_20260816_205001, CSV calibration se remplit.
- Échantillons réels du CSV (22:53Z) :
    RIZEUSDT  COOLING  NONE  drop=0.0   Δspread=-87.15  notional=True spoof=False
    CCUSDT    COOLING  NONE  drop=0.0   Δspread=0.0     notional=True spoof=False
    BIOUSDT   COOLING  NONE  drop=-0.02 Δspread=4.1     notional=True spoof=False
    CHIPUSDT  IMPULSE  SELL  drop=1.24  Δspread=-3.39   notional=True spoof=False
  (drop = %/s du mur qui fond ; notional_ok = mur ≥ 500$.)

=== TA MISSION (5 réponses nettes) ===
1. VERDICT : GO / GO AVEC RESERVES / NON sur CE code (pas le concept) + raison nette.
2. BUGS ou angles morts dans CE code : fail-open, spoof (seuil 15%/s, tolérance 10%),
   rate-limit MEXC (5 paires × 2 lectures × toutes les 3 cycles), CSV, radar, boucle.
3. UNE amélioration concrète GO-sized (pas cosmétique).
4. CLAUSE PERMANENTE : propose AUTRE CHOSE si ça a du sens (approche différente,
   autre architecture, autre unité) — ne te contente pas de corriger.
5. Ce qui changerait ton avis (le(s) fait(s) qui feraient basculer).
Factuel, concis, français. Tu DONNES UN AVIS : ne touche à rien, n'écris aucun code.
"""


def ask_codeur():
    payload = json.dumps({
        "task": "code.ia",
        "messages": [
            {"role": "system", "content": (
                "Tu es le CODEUR de la famille ACE777. Tu écris et vérifies le code. "
                "Tu es factuel, tu repères les bugs réels, tu refuses la fiction."
            ) + "\n\n" + CLAUSE},
            {"role": "user", "content": BRIEF},
        ],
        "max_tokens": 2400,
        "temperature": 0.3,
    }).encode("utf-8")
    req = urllib.request.Request(
        HUB, data=payload,
        headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    return (
        d["choices"][0]["message"]["content"].strip(),
        d.get("provider", "?"),
        round(time.time() - t0, 1),
    )


def main():
    for attempt in (1, 2, 3):
        try:
            content, provider, secs = ask_codeur()
            with open(os.path.join(OUT, "AVIS_CODEUR.md"), "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS CODEUR (task code.ia, provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] CODEUR (provider {provider}, {secs}s)")
            return
        except Exception as e:
            print(f"[ERR] CODEUR (tentative {attempt}): {e}")
            time.sleep(5)
    print("[FAIL] codeur injoignable après 3 tentatives")


if __name__ == "__main__":
    main()
