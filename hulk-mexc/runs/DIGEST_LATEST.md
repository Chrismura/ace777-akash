# Hulk DIGEST — 2026-10-20T08:11:34Z

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
| ETHUSDT | IDLE | 0.81 | 1.41 | 1.36 | -0.02 | 128747517.45 | 0.21 | skipped_fast |
| XRPUSDT | IDLE | 0.66 | 1.17 | 1.05 | -0.01 | 20222800.43 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.09 | 1.04 | -0.01 | 299723901.34 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.09 | 2.26 | -0.04 | 1019100.51 | 2.77 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.83 | 2.23 | 0.02 | 728614.71 | 17.67 | skipped_fast |
| CCUSDT | IDLE | 2.48 | 4.36 | 4.02 | 0.0 | 477567.14 | 5.8 | skipped_fast |
| QNTUSDT | IDLE | 2.65 | 4.71 | 4.0 | -0.04 | 655702.2 | 1.57 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 12.65 | 0.1 | 0.14 | 271130.59 | 9.61 | skipped_fast |
| CHIPUSDT | IDLE | 2.52 | 6.6 | 1.89 | 0.03 | 92776.08 | 11.36 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.15 | 2.59 | 0.06 | 78589.09 | 9.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.41 | 2.03 | -0.03 | 166857.87 | 19.78 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.88 | 1.78 | -0.02 | 404395.31 | 7.26 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.84 | 1.72 | -0.01 | 66181.44 | 4.27 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 1.86 | 1.76 | -0.01 | 58681.06 | 8.06 | skipped_fast |
| RWAINCUSDT | IDLE | 0.93 | 1.66 | 1.28 | 0.02 | 75357.73 | 5.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.5 | 1.85 | 1.58 | -0.08 | 67183.01 | 35.53 | skipped_fast |
| IOTAUSDT | IDLE | 1.21 | 2.17 | 1.71 | 0.01 | 91839.6 | 26.46 | skipped_fast |
| LAUSDT | IDLE | 1.21 | 2.15 | 1.75 | -0.01 | 56042.44 | 28.71 | skipped_fast |
| WAXLUSDT | IDLE | 1.46 | 2.98 | 2.21 | -0.06 | 56523.43 | 71.75 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.38 | 1.4 | -0.01 | 4470.46 | 21.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.04 | -0.0 | 39995.12 | 5.7 | skipped_fast |
| RWAUSDT | IDLE | 0.2 | 0.39 | 0.08 | 0.01 | 52114.18 | 31.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
