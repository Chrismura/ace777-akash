# Hulk DIGEST — 2026-10-28T23:44:15Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.3 | 2.4 | 1.33 | -0.0 | 22750684.53 | 0.75 | n/a |
| ETHUSDT | IDLE | 1.19 | 2.18 | 1.3 | 0.0 | 205823039.59 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.71 | 1.33 | 0.54 | 0.01 | 324858363.45 | 0.0 | no_map |
| PYTHUSDT | IDLE | 3.03 | 5.82 | 1.63 | 0.01 | 445692.3 | 5.45 | tvl≈164,828,368 |
| WUSDT | IDLE | 1.91 | 3.46 | 2.43 | -0.01 | 397182.1 | 17.32 | tvl≈1,537,539,483 |
| CCUSDT | IDLE | 1.61 | 3.76 | 0.95 | 0.02 | 429402.33 | 9.87 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 6.07 | 5.09 | -0.03 | 39361.13 | 69.29 | no_map |
| QNTUSDT | IDLE | 2.55 | 4.96 | 0.89 | 0.01 | 411938.72 | 1.99 | n/a |
| HBARUSDT | IDLE | 1.78 | 3.13 | 2.84 | -0.02 | 552407.3 | 9.36 | empty_tvl |
| BIOUSDT | IDLE | 2.09 | 3.88 | 2.06 | 0.01 | 88745.63 | 8.76 | n/a |
| ZBCNUSDT | IDLE | 1.43 | 2.72 | 0.91 | 0.02 | 291739.28 | 34.95 | n/a |
| CHIPUSDT | IDLE | 0.93 | 4.24 | 1.87 | -0.09 | 235513.96 | 14.21 | no_map |
| EDELUSDT | IDLE | 1.19 | 2.16 | 1.47 | -0.02 | 174366.26 | 18.64 | no_map |
| KITEUSDT | IDLE | 1.48 | 2.77 | 1.32 | -0.02 | 61505.77 | 9.45 | no_map |
| RWAINCUSDT | IDLE | 1.49 | 5.17 | 4.92 | -0.07 | 33898.0 | 43.23 | no_map |
| REDUSDT | IDLE | 1.43 | 2.55 | 2.02 | -0.03 | 56118.36 | 15.87 | tvl≈3,770,013 |
| IOTAUSDT | IDLE | 2.51 | 4.52 | 3.35 | -0.02 | 79364.84 | 26.48 | no_map |
| LAUSDT | IDLE | 2.08 | 3.83 | 2.15 | -0.03 | 54479.93 | 24.08 | no_map |
| FLUIDUSDT | IDLE | 1.6 | 2.88 | 2.07 | -0.01 | 9287.81 | 21.45 | tvl≈2,238,378,456 |
| RWAUSDT | IDLE | 0.73 | 1.37 | 0.63 | 0.0 | 54618.18 | 47.85 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.07 | 0.01 | 35811.85 | 40.86 | no_map |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
