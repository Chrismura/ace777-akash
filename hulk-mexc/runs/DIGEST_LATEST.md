# Hulk DIGEST — 2026-10-27T15:12:16Z

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
| XRPUSDT | IDLE | 1.23 | 2.38 | 0.49 | 0.01 | 20473695.59 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.96 | 1.88 | 0.33 | 0.0 | 153057426.86 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.22 | 0.19 | -0.0 | 315013987.3 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.5 | 7.8 | 1.86 | 0.05 | 637355.85 | 19.99 | skipped_fast |
| QNTUSDT | IDLE | 2.61 | 4.65 | 3.75 | -0.06 | 896432.76 | 2.52 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.99 | 8.01 | 1.09 | 0.04 | 57160.8 | 10.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.37 | 7.94 | 2.94 | 0.02 | 278317.68 | 15.25 | skipped_fast |
| REDUSDT | IDLE | 3.51 | 7.0 | 0.18 | 0.03 | 61274.16 | 14.3 | skipped_fast |
| CCUSDT | IDLE | 2.32 | 4.46 | 1.21 | -0.02 | 234271.29 | 9.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 1.92 | 1.79 | -0.05 | 447537.73 | 4.16 | skipped_fast |
| EDELUSDT | IDLE | 1.23 | 2.35 | 0.73 | 0.01 | 415792.58 | 6.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.58 | 5.4 | 3.89 | -0.14 | 59170.04 | 6.75 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.62 | 1.03 | -0.02 | 55866.21 | 9.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.68 | 1.87 | 1.24 | 0.0 | 257239.24 | 55.42 | skipped_fast |
| LAUSDT | IDLE | 2.23 | 4.31 | 0.98 | 0.0 | 62549.31 | 20.43 | skipped_fast |
| WAXLUSDT | IDLE | 2.14 | 4.04 | 1.61 | 0.0 | 53958.98 | 61.27 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 1.44 | 1.09 | -0.01 | 40930.45 | 65.56 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.48 | 1.38 | -0.03 | 171826.39 | 5.29 | skipped_fast |
| IOTAUSDT | IDLE | 1.04 | 2.03 | 0.28 | -0.02 | 88503.36 | 26.04 | skipped_fast |
| RWAUSDT | IDLE | 1.19 | 2.29 | 0.64 | -0.01 | 57000.37 | 48.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.86 | 1.55 | 1.11 | 0.03 | 3355.87 | 22.09 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.77 | 0.41 | 0.0 | 37133.64 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
