# Hulk DIGEST — 2026-09-24T19:38:41Z

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
| XRPUSDT | IDLE | 1.93 | 3.69 | 1.07 | 0.02 | 69522367.23 | 1.31 | skipped_fast |
| ETHUSDT | IDLE | 1.15 | 2.24 | 0.43 | 0.01 | 345602215.71 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 1.07 | 2.04 | 0.67 | 0.0 | 705655894.06 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.34 | 8.38 | 4.43 | 0.09 | 1305553.71 | 1.47 | skipped_fast |
| CCUSDT | IDLE | 3.04 | 5.97 | 0.67 | 0.05 | 470246.59 | 13.14 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 4.18 | 2.47 | 0.02 | 871433.27 | 1.08 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.53 | 17.27 | 1.53 | 0.15 | 82327.71 | 14.48 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.54 | 14.32 | 1.08 | 0.15 | 9420.06 | 9.46 | skipped_fast |
| BIOUSDT | IDLE | 2.33 | 7.47 | 1.67 | 0.1 | 83687.34 | 6.43 | skipped_fast |
| EDELUSDT | IDLE | 2.2 | 5.99 | 0.6 | 0.02 | 155351.32 | 17.65 | skipped_fast |
| WUSDT | IDLE | 1.75 | 3.36 | 0.95 | 0.04 | 238391.96 | 5.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.8 | 3.59 | 0.12 | 0.03 | 217633.86 | 15.28 | skipped_fast |
| TELUSDT | IDLE | 2.92 | 5.45 | 2.64 | -0.04 | 114056.7 | 18.11 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 3.98 | 1.06 | 0.06 | 100514.7 | 6.22 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.86 | 0.57 | 0.02 | 67050.83 | 9.74 | skipped_fast |
| QNTUSDT | IDLE | 1.6 | 9.89 | 0.54 | 0.21 | 213065.83 | 10.42 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.66 | 20.58 | 1.83 | 0.29 | 54976.54 | 325.3 | skipped_fast |
| FLUIDUSDT | IDLE | 2.41 | 4.77 | 0.28 | 0.05 | 2518.49 | 21.97 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.62 | 0.44 | 0.02 | 54687.2 | 7.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.22 | 0.17 | 0.0 | 37451.07 | 5.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
