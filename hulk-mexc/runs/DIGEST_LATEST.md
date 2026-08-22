# Hulk DIGEST — 2026-08-22T16:57:57Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.19 | 0.19 | 0.09 | 49201657.68 | 9.49 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.15 | 0.06 | 214667151.09 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.89 | -0.01 | 1131695.69 | 6.45 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.14 | 1.22 | 0.1 | 769448.12 | 13.5 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.66 | -0.1 | 629730.6 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.52 | -0.01 | 545007.81 | 12.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.22 | -0.02 | 312575.28 | 10.21 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.67 | -0.07 | 225794.17 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.45 | 0.03 | 86694.29 | 11.57 | skipped_fast |
| EDELUSDT | IDLE | 1.68 | 3.0 | 2.35 | -0.03 | 74915.22 | 34.31 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.62 | -0.14 | 127115.5 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 3.47 | 0.39 | 0.06 | 46438.49 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.88 | -0.01 | 181184.09 | 3.14 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7603.75 | 113.06 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | -0.0 | 136242.16 | 64.34 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.23 | 0.08 | 0.02 | 56381.25 | 8.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
