# VERDICT FAMILLE — HULK tier/rip (garde-fous typologie) — 16/08/2026

**Consultation :** 4/4 avis reçus (gemini 3.7s · nvidia 147.5s · deepseek-v4 102.3s · codestral 3.8s).
**Statut :** ✅ **GO-AVEC-RÉSERVE** (4/4) — consensus fort (confiance 65-90%).

## Réponses aux 4 questions

| # | Question | Consensus | Décision retenue |
|---|---|---|---|
| 1 | TIER_B_POSITION_MULT ? | **0.25 OK partout** (0.1 trop restrictif + frais ; watch-only trop peu informatif) | **0.25** |
| 2 | RIP 50% unique ou paliers ? | **50% unique** (3/4 — gemini, nvidia, deepseek : les paliers complexifient, le spike peut être one-shot ; codestral réserve) | **RIP_SELL_FRAC=0.50** unique |
| 3 | Rip sur tier B ? | **OUI mais conditionné** (nvidia + deepseek : ne vendre que si **spread < 100 bps** au moment de la vente, sinon slippage massif) | **Rip tier B seulement si spread < 100 bps** |
| 4 | REENTRY_MAX=1 + 4h ? | **GO** (3/4 — EDEL ×3 = aberration ; codestral suggère 2 mais reste GO) + **reset après gain** (nvidia) | **REENTRY_MAX=1, cooldown 4h, reset si gain** |

## Réserves famille intégrées (au-delà de la spec)

1. **Check spread au buy** (gemini, nvidia, codestral) : si `spread_bps > 100` → SKIP, **même tier A**
   (protège contre les paires mal classées — ex. QAIT à 327 bps). Source : `self.inv` (inventaire chargé).
2. **Priorité d'implémentation** (nvidia) : le bloc 2 (`pick_pairs`) est le **bug racine** (PAPER_PAIRS
   en dur contourne le filtre tier) → à faire en premier, vérifié au boot.
3. **Log tier + spread à chaque buy/sell** (nvidia, deepseek) : pour l'audit post-campagne.
4. **Surveillance** : après 10 trades avec les 4 blocs → comparer PnL vs ancien système, ajuster
   RIP_SELL_FRAC si besoin (nvidia) ; si tier B restent négatifs à 0.25 → watch-only (deepseek).

## Ce qui changerait l'avis

- Inventaire MEXC incohérent avec les spreads réels (QAIT 327 bps classé…) → NO-GO (nvidia).
- Backtest montrant que le rip_pct aurait capturé ≥ 50% des gains manqués (RED +32%, CHIP +20%) → GO+ (nvidia).

## SYNTHÈSE

Diagnostic partagé : le système trade des paires illiquides (tier B) à pleine taille, ne vend
jamais les gains (give-back RED/CHIP), et re-entre en chute (EDEL ×3). Ordre d'actions :
**(1) pick_pairs (bug racine) → (2) sizing tier B → (3) rip avec garde spread → (4) re-entry borné**.
Surveiller les 10 prochains trades, puis A/B tier B 0.25 vs watch-only.
