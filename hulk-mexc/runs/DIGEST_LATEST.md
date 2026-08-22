# Hulk DIGEST — 2026-08-22T03:28:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 11.15 | 0.86 | 0.17 | 7773869.68 | 1.88 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.3 | 0.21 | 164328882.09 | 1.9 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 6.29 | 0.02 | 0.11 | 1019042.23 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 8.96 | 1.98 | 0.17 | 682065.18 | 5.12 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.99 | 0.08 | 198120.0 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 4.43 | 0.47 | -0.01 | 452513.72 | 8.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.4 | 0.12 | 538092.69 | 6.67 | skipped_fast |
| WUSDT | IDLE | 1.8 | 5.79 | 0.16 | 0.13 | 423039.14 | 13.76 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80000.56 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.34 | 0.1 | 59533.4 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.13 | 0.21 | 157781.17 | 18.84 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9338.84 | 32.45 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.5 | 0.0 | 0.13 | 67711.38 | 11.59 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 4.26 | 0.09 | 0.09 | 174214.76 | 5.92 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.41 | 0.07 | 173199.63 | 46.12 | skipped_fast |
| RWAUSDT | IDLE | 1.32 | 2.64 | 0.0 | 0.05 | 56233.98 | 32.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 14.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
