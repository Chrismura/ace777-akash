# Hulk DIGEST — 2026-09-11T15:21:03Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 130.41 | 30.25 | 0.49 | 144468.05 | 114.2 | skipped_fast |
| XRPUSDT | IDLE | 4.19 | 8.82 | 2.94 | 0.03 | 50879322.93 | 2.16 | skipped_fast |
| ETHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.05 | 9.44 | 1.88 | 0.07 | 573014777.74 | 0.54 | skipped_fast |
| BTCUSDT | IDLE | 2.57 | 4.93 | 1.41 | 0.02 | 524578053.43 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 4.01 | 7.68 | 2.31 | -0.01 | 476964.91 | 8.03 | skipped_fast |
| PYTHUSDT | IDLE | 3.93 | 7.72 | 0.89 | 0.03 | 368585.78 | 1.87 | skipped_fast |
| EDELUSDT | IDLE | 4.03 | 7.66 | 2.67 | -0.01 | 195177.45 | 27.43 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.03 | 8.01 | 0.28 | 0.04 | 174288.14 | 22.03 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 8.51 | 6.13 | 0.02 | 10003.35 | 27.63 | skipped_fast |
| REDUSDT | IDLE | 3.84 | 7.46 | 1.41 | 0.03 | 61197.42 | 19.11 | skipped_fast |
| BIOUSDT | IDLE | 3.32 | 6.49 | 0.96 | 0.02 | 81169.18 | 7.79 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.91 | 9.52 | 0.08 | 0.04 | 138075.42 | 14.33 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 5.61 | 0.88 | 0.03 | 175328.04 | 16.45 | skipped_fast |
| TELUSDT | IDLE | 4.15 | 8.79 | 2.21 | 0.02 | 103454.26 | 49.71 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 4.0 | 1.1 | 0.01 | 59453.33 | 12.76 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 5.04 | 1.25 | 0.01 | 207361.05 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 2.77 | 5.19 | 2.27 | -0.0 | 40857.69 | 7.63 | skipped_fast |
| FLUIDUSDT | IDLE | 2.47 | 4.94 | 0.0 | 0.03 | 1301.56 | 22.07 | skipped_fast |
| RWAUSDT | IDLE | 1.64 | 3.2 | 0.59 | 0.02 | 51195.33 | 29.72 | skipped_fast |
| MNSRYUSDT | IDLE | 1.62 | 3.1 | 0.99 | 0.01 | 38291.5 | 46.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
