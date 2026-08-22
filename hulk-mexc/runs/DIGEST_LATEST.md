# Hulk DIGEST — 2026-08-22T02:10:23Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.42 | 1.33 | 0.13 | 6902750.92 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 10.03 | 0.31 | 0.16 | 154237672.28 | 1.33 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 4.9 | 0.38 | 0.08 | 952908.41 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.25 | 0.08 | 546197.06 | 25.75 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.13 | 0.14 | 654254.44 | 6.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.69 | 3.91 | 0.03 | 0.02 | 515654.66 | 3.03 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 6.88 | 0.24 | 0.09 | 190568.1 | 5.94 | skipped_fast |
| WUSDT | IDLE | 1.74 | 4.41 | 0.54 | 0.08 | 399848.01 | 15.2 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 5.02 | 0.98 | -0.01 | 79621.28 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.77 | 0.11 | 61143.63 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.18 | 0.17 | 156873.12 | 19.45 | skipped_fast |
| QNTUSDT | IDLE | 2.31 | 4.89 | 1.27 | 0.07 | 171311.43 | 3.02 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.49 | 0.12 | 61353.22 | 8.99 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.02 | 9241.73 | 69.8 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.33 | 0.04 | 179069.08 | 67.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.89 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54738.62 | 16.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
