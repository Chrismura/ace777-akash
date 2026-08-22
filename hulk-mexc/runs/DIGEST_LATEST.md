# Hulk DIGEST — 2026-08-22T04:46:32Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.95 | 15.22 | 0.52 | 0.21 | 11919674.15 | 12.63 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 16.18 | 0.36 | 0.25 | 175997506.86 | 2.43 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 8.85 | 0.44 | 0.13 | 1072032.68 | 9.37 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.51 | 0.2 | 737102.99 | 8.22 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.62 | 0.01 | 450933.51 | 14.94 | skipped_fast |
| WUSDT | IDLE | 2.03 | 7.75 | 0.48 | 0.15 | 433584.53 | 16.4 | skipped_fast |
| BIOUSDT | IDLE | 2.96 | 7.36 | 1.52 | 0.06 | 201397.25 | 14.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.05 | 0.12 | 537906.42 | 41.75 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.33 | 0.1 | 182348.74 | 5.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.5 | 0.09 | 58573.98 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.78 | 0.2 | 158136.62 | 10.39 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.45 | 0.13 | 68031.61 | 13.27 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.71 | -0.03 | 80170.39 | 66.59 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 32.66 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.64 | 0.1 | 182039.19 | 24.82 | skipped_fast |
| RWAUSDT | IDLE | 1.53 | 3.05 | 0.08 | 0.06 | 56644.17 | 8.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
