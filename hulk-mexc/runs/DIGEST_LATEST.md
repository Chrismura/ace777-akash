# Hulk DIGEST — 2026-10-14T20:22:17Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.32 | 8.33 | 0.09 | 0.09 | 1888707.85 | 2.35 | skipped_fast |
| WUSDT | IDLE | 1.0 | 4.46 | 1.38 | -0.09 | 2562347.38 | 11.69 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.49 | 1.03 | -0.03 | 45002540.06 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.33 | 0.83 | -0.03 | 202949376.43 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.68 | 0.14 | -0.02 | 433911625.57 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.36 | 4.53 | 1.24 | -0.05 | 1142958.63 | 2.4 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 5.26 | 3.7 | -0.04 | 195296.8 | 7.74 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 3.38 | 2.39 | -0.08 | 418272.86 | 9.43 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 11.33 | 5.84 | 0.08 | 18479.93 | 20.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 5.83 | 3.8 | -0.08 | 104380.86 | 13.18 | skipped_fast |
| RWAINCUSDT | IDLE | 2.24 | 6.51 | 1.38 | -0.07 | 28843.74 | 5.19 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.61 | 2.75 | -0.04 | 166999.18 | 39.14 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 5.27 | 3.99 | -0.01 | 86347.06 | 10.19 | skipped_fast |
| REDUSDT | IDLE | 2.23 | 4.43 | 0.15 | 0.02 | 61929.5 | 14.6 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.29 | 0.88 | -0.04 | 526308.08 | 3.55 | skipped_fast |
| TELUSDT | IDLE | 2.86 | 5.3 | 2.85 | 0.01 | 103634.91 | 28.18 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.71 | 1.67 | -0.04 | 66016.18 | 7.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 2.68 | 0.94 | -0.0 | 48999.49 | 61.33 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.64 | 0.4 | -0.03 | 56523.07 | 15.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.61 | 0.31 | -0.01 | 36423.24 | 29.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
