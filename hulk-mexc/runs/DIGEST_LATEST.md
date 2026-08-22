# Hulk DIGEST — 2026-08-22T03:33:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.43 | 0.18 | 7883091.25 | 9.34 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 0.98 | 0.21 | 164516355.01 | 5.06 | skipped_fast |
| HBARUSDT | IDLE | 2.38 | 6.93 | 0.05 | 0.12 | 1022503.87 | 1.2 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 8.96 | 1.37 | 0.17 | 687291.72 | 7.63 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.99 | 0.08 | 198719.41 | 5.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 4.43 | 0.09 | -0.01 | 452106.4 | 5.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.54 | 0.12 | 537875.74 | 29.6 | skipped_fast |
| WUSDT | IDLE | 1.8 | 5.79 | 0.21 | 0.13 | 423684.76 | 12.78 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80005.09 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.44 | 0.1 | 59560.19 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.68 | 0.21 | 158054.05 | 8.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.87 | 3.44 | 2.06 | 0.01 | 9331.12 | 16.2 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.5 | 0.09 | 0.12 | 67776.72 | 9.82 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 4.68 | 0.27 | 0.09 | 174302.84 | 10.33 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.45 | 2.89 | 0.0 | 0.06 | 56313.3 | 16.05 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.31 | 0.07 | 173634.84 | 50.97 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
