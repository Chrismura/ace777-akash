#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CHECK-UP POST-IMPLÉMENTATION — HULK : SONDE ASPIRATION (16/08/2026 soir).

Le code a été implémenté et tourne (mode observation 48h). On envoie le CODE RÉEL
(plus un plan) au codeur (task code.ia) et à la famille (6 voix) pour check-up.

CLAUSE PERMANENTE (gravée 16/08 par Christophe, applicable à TOUS les prompts) :
« Ne te contente pas de corriger ou de valider : si tu proposes AUTRE CHOSE
(approche différente, autre architecture) ou une AMÉLIORATION qui a du sens,
dis-le explicitement. Corriger n'est pas suffisant : proposer est attendu. »
"""
import json
import os
import sys
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CHECKUP_SONDE_ASPIRATION_20260816")
os.makedirs(OUT, exist_ok=True)

# Clause permanente Christophe (16/08) — doit être dans TOUS les prompts.
CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

# Le CODE RÉEL (extrait des fichiers implémentés) — pas un plan, ce qui tourne.
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
    # correction JUGE : volume absolu min — mur < 500$ = bruit, pas aspiration
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
        # === spoof « rétractable à maintenant » (Christophe) ===
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
        # calibration CSV (mode observation 48h — c'est LÀ qu'on calibre le seuil)
        with self.aspiration_csv.open("a", newline="") as f:
            csv.writer(f).writerow([utc_now(), pair, a["regime"], a.get("aspiration_side"),
                a.get("drop_bid_pct_per_s"), a.get("drop_ask_pct_per_s"),
                a.get("max_drop_pct_per_s"), a.get("spread_bps"),
                a.get("spread_delta_bps"), a.get("wall_bid_usdt"),
                a.get("wall_ask_usdt"), a.get("notional_drop_ok"),
                spoof, a.get("delay_s"), price])
'''

CONTEXTE = f"""\
CHECK-UP POST-IMPLÉMENTATION — SONDE ASPIRATION HULK (16/08/2026 soir)

================
LA DEMANDE (Christophe)
================
« Je veux qu'il sonde comme ACE : voir les murs de liquidité, l'aspiration,
l'historique qui fait parti pris — l'intelligence si c'est possible. »
Et : « pas de 15 minutes, 3-2 s... rétractable à maintenant. »

================
CE QUI A ÉTÉ DÉCIDÉ AVANT (consensus)
================
- Codeur 4/4 : GO-AVEC-RÉSERVE — mode OBSERVATION 48h d'abord, fail-open, limiter
  aux paires actives, seuil calibré sur données réelles.
- Famille 6/6 : GO-AVEC-RÉSERVE — 3 corrections : drop normalisé par temps réel
  (GROK), mur ≥ 500$ (JUGE), croisement spread_delta (JUGE+DEEPSEEK).
- Cortana : GO-RÉSERVES + anti-spoof.
- Christophe : spoof « rétractable à maintenant » = debounce par lecture, PAS de
  ban 15 min (3-2 s sur ce marché = éternité, 15 min = on rate tout).

================
LE CODE RÉEL — CE QUI TOURNE MAINTENANT (extraits)
================
Fichier scripts/ace_sense_mexc.py — aspiration_sense() (DOUBLE lecture) :
{CODE_ASPIRATION_SENSE}

Fichier scripts/paper_diprip.py — probe_aspiration() (mode observation, 0 effet moteur) :
{CODE_PROBE}

Config (config/defaults.env) :
  ASPIRATION_ON=1 · ASPIRATION_DELAY_S=0.5 · ASPIRATION_MIN_NOTIONAL_USDT=500
  ASPIRATION_PROBE_EVERY=3 (cycles) · ASPIRATION_MAX_PAIRS=5 (rate-limit MEXC)

================
VÉRIFICATIONS FAITES (preuves, 16/08 22:53Z)
================
- py_compile OK (paper_diprip.py + ace_sense_mexc.py).
- Config chargée OK (ASPIRATION_ON=1, DELAY=0.5, MIN=500, PROBE_EVERY=3, MAX=5).
- Capteur testé en live sur XRPUSDT/RIZEUSDT : ok=True, side=NONE (marché calme).
- Hulk relancé via watchdog, process stable, run PAPER_V1_20260816_205001.
- CSV runs/ASPIRATION_CALIB_20260816_205001.csv se remplit en direct :
  RIZEUSDT  NONE  drop=0.0   Δspread=-87bps  notional=True spoof=False
  CHIPUSDT  SELL  drop=1.24  Δspread=-3.4bps notional=True spoof=False

================
TA MISSION (4 réponses nettes)
================
1. VERDICT sur le CODE RÉEL : GO / GO AVEC RESERVES / NON + raison courte et nette
   (le JUGE tranche formellement).
2. Angle(s) mort(s) dans CE code (pas dans un plan) : bug, fail-open mal placé,
   spoof mal détecté, rate-limit, CSV, erreur de logique.
3. UNE amélioration concrète GO-sized du code (pas cosmétique).
4. CLAUSE PERMANENTE : propose AUTRE CHOSE si ça a du sens (approche différente,
   autre architecture, autre unité) — ne te contente pas de corriger.
Réponds en français, format court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system + "\n\n" + CLAUSE},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1600,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}", "?"


if __name__ == "__main__":
    import time
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    for nom, task, system in membres:
        content, provider = ask((nom, task), system)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as fh:
            fh.write(f"# AVIS {nom} (provider {provider})\n\n{content}\n")
        print(f"[OK] {nom} ({provider})")
        time.sleep(2)
