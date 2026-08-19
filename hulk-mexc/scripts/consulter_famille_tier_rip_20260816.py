#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — HULK : respect TIER + RIP (garde-fous typologie) — 16/08/2026.

Protocole §C #9 Multi-Perspective + #5 Confidence-Weighted. Code EXACT injecté.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_TIER_RIP_20260816")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CLAUSE PERMANENTE (Christophe, 16/08 — applicable à TOUS les prompts) :
Ne te contente PAS de corriger ou de valider. Si tu proposes AUTRE CHOSE (approche différente,
autre architecture, autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement.
Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait que « c'est bon »
ou « corrige X » est incomplète.

CONTEXTE (superviseur Buffy, 16/08/2026) — CONSULTATION FAMILLE : fix HULK tier/rip

=== LE SYSTÈME ===
HULK = paper trading dip&rip sur MEXC spot (watchlist CMC « The Hulk Portfolio Picks », ~15 paires
small caps). Mise 20$/trade, stop technique ~6%, cible 2× (+100%) → vente 50% (reste = bag maison),
DCA bags, kill-switch veille, contrat Cortana ADVISORY. DEUX AXES DE CLASSIFICATION (typologie 15/08) :
- TIER = liquidité marché (inventaire MEXC) : A liquide / B spike illiquide (« paper ou taille
  microscopique ») / C skip.
- CLASSE = stratégie (famille 15/08) : A core liquides (stop technique) / B small caps bag
  institutionnel vérifié (pas de stop technique, taille ×0.5, horizon 12 mois). BAG_PAIRS=CCUSDT seul.

=== LE CONSTAT (3 jours) ===
pnl −7.02$ en 4 stops, 0 gain : RIZE −2.48 (tier B, spread 59 bps, stop gapé à −12.25% au lieu de −6%),
EDEL −3.31 (tier B, 22 bps, acheté 3× dont 2 re-entries → stops), ZBCN −1.22 (tier A limite, 24 bps).
Campagne 22-26/07 : −8.36$ en 5 stops (même pattern, docs/CONFRONTATION.md). Pendant ce temps,
RED +32.8% et CHIP +20.7% depuis entry N'ONT PAS ÉTÉ VENDUS (cible 2× à +100% jamais atteinte) →
give-back total.

=== LES BUGS (code exact, vérifié) ===
1. pick_pairs() filtre tier=="A" par défaut MAIS PAPER_PAIRS en dur (15 paires) contourne le filtre
   → QAIT (spread 327 bps !), RIZE, EDEL (tier B) sont tradés.
2. buy() ne réduit la taille que si is_bag() (classe B → ×0.5) : tier B illiquide = pleine mise 20$.
3. rip_pct (rebond cible ~2%) est calculé et stocké mais JAMAIS utilisé pour vendre — manage_open()
   ne fait que 2×→stake_out ou stop. PLAN.md prévoit « Sell rip/spike : rebond ≥ RIP_PCT depuis entry ».
4. Re-entry : cooldown 2h, EDEL racheté 3× sur une paire en chute.

=== LA SPEC (4 blocs, code EXACT) ===
1. Sizing tier B dans buy() (après sizing classe B existant) :
     trade_n = float(notion) if notion is not None else self.current_notional()
     if self.is_bag(pair):
         trade_n = trade_n * self.bag_position_mult
     if self.tier(pair) == "B":
         trade_n = trade_n * self.tier_b_position_mult   # NOUVEAU
     if trade_n < 1.0: return
   Config : TIER_B_POSITION_MULT=0.25
2. pick_pairs() : quand PAPER_PAIRS défini, chaque paire vérifiée contre l'inventaire — tier B et pas
   dans PAPER_EXTRA_PAIRS → exclue (log au boot).
3. RIP dans manage_open() (avant le check 2×) :
     if chg >= float(p.get("rip") or 2.0) and not p.get("rip_done"):
         p["rip_done"] = True
         sell_qty = qty * self.rip_sell_frac
         if sell_qty >= qty * 0.001:
             proceeds = self.sell_trade(pair, price, f"rip_{chg:.1f}pct_sell_{self.rip_sell_frac*100:.0f}pct", qty=sell_qty)
             self.add_pair_cash(pair, proceeds)
             return
   Config : RIP_SELL_FRAC=0.50. (sell_trade gère déjà SELL_PARTIAL + cache stop.)
4. Re-entry borné : STOP_COOLDOWN_HOURS=4 + REENTRY_MAX=1 (compteur par paire incrémenté à chaque
   position fermée ; buy() SKIP si max atteint).

=== VOS 4 QUESTIONS ===
1. TIER_B_POSITION_MULT=0.25 raisonnable ? (ou 0.1, ou watch-only strict ?)
2. RIP_SELL_FRAC=0.50 au 1er franchissement du rip_pct — ou vente par paliers (30% à rip, 30% à 2×rip) ?
3. Le rip doit-il s'appliquer aussi aux tier B (qui spikent fort mais illiquides) ?
4. REENTRY_MAX=1 + cooldown 4h : bons ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « implémenter ces 4 blocs », réserve précisée)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3 hypothèses
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : diagnostic le plus probable + ordre des actions.

Factuel, concis, français. Si une info manque : « information insuffisante ». Vous DONNEZ UN AVIS :
ne touchez à rien, n'écrivez aucun code."""

MODELS = ["gemini", "nvidia", "deepseek-ai/deepseek-v4-flash-0731", "codestral-latest"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m)
                name = m.split("/")[-1].split(":")[0]
                with open(os.path.join(OUT, f"AVIS_{name}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)


if __name__ == "__main__":
    main()
