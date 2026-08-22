# Hulk DIGEST — 2026-08-22T04:02:57Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.76 | 11.77 | 0.19 | 0.19 | 9473526.15 | 16.68 | skipped_fast |
| XRPUSDT | IDLE | 2.16 | 12.22 | 2.02 | 0.19 | 166332356.1 | 2.56 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 10.49 | 0.0 | 0.21 | 709933.85 | 13.92 | skipped_fast |
| HBARUSDT | IDLE | 2.12 | 6.03 | 0.77 | 0.11 | 1013561.7 | 1.21 | skipped_fast |
| CHIPUSDT | IDLE | 2.85 | 5.36 | 2.24 | -0.04 | 458919.99 | 6.03 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.46 | 0.07 | 199212.61 | 6.01 | skipped_fast |
| WUSDT | IDLE | 1.98 | 7.18 | 0.92 | 0.14 | 427923.39 | 14.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.56 | 0.13 | 537568.67 | 23.36 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80602.43 | 33.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.7 | 0.1 | 59252.95 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.12 | 0.22 | 157738.61 | 12.55 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.29 | 0.13 | 67539.21 | 10.62 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 3.8 | 0.86 | 0.09 | 178541.84 | 4.46 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56335.44 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.4 | 0.61 | 0.07 | 174319.69 | 35.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 20.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
