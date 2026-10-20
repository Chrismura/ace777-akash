# Hulk DIGEST — 2026-10-20T21:26:28Z

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
| XRPUSDT | IDLE | 0.81 | 1.58 | 0.3 | 0.02 | 24201633.11 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.28 | 0.12 | 0.02 | 156430709.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.78 | 0.1 | 0.01 | 323518869.12 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 6.24 | 0.75 | 0.1 | 1169348.22 | 5.04 | skipped_fast |
| WUSDT | IDLE | 2.09 | 4.08 | 0.63 | 0.03 | 675697.65 | 15.61 | skipped_fast |
| QNTUSDT | IDLE | 1.74 | 3.39 | 0.61 | 0.01 | 791309.24 | 6.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 5.69 | 3.06 | 0.08 | 395333.34 | 15.56 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.91 | 9.94 | 0.0 | 0.05 | 72156.37 | 9.82 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 9.41 | 5.54 | 0.05 | 75098.39 | 57.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.94 | 3.67 | 1.4 | 0.03 | 191119.23 | 12.12 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.86 | 1.31 | 0.01 | 383372.01 | 7.6 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.76 | 2.79 | 0.33 | 362908.7 | 11.26 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.68 | 1.18 | 0.03 | 59854.85 | 15.66 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.38 | 0.48 | 0.06 | 62703.5 | 8.05 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.8 | 0.33 | 0.02 | 369478.32 | 2.38 | skipped_fast |
| KITEUSDT | IDLE | 0.51 | 0.98 | 0.22 | -0.01 | 83137.29 | 4.08 | skipped_fast |
| IOTAUSDT | IDLE | 1.32 | 2.49 | 0.95 | 0.04 | 72275.1 | 21.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.07 | 6267.92 | 21.43 | skipped_fast |
| LAUSDT | IDLE | 1.27 | 2.54 | 0.04 | 0.04 | 55608.8 | 20.2 | skipped_fast |
| WAXLUSDT | IDLE | 1.44 | 2.61 | 1.81 | -0.03 | 56588.3 | 54.01 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.87 | 0.31 | 0.0 | 51591.01 | 15.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.63 | 0.57 | -0.0 | 39789.49 | 28.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
