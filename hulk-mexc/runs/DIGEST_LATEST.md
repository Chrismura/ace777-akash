# Hulk DIGEST — 2026-08-22T03:43:56Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.2 | 0.18 | 8232019.74 | 1.87 | skipped_fast |
| XRPUSDT | IDLE | 2.51 | 14.16 | 2.57 | 0.19 | 165134233.86 | 5.14 | skipped_fast |
| HBARUSDT | IDLE | 2.44 | 6.93 | 1.19 | 0.1 | 1031655.63 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 9.25 | 0.14 | 0.19 | 692564.02 | 9.18 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 5.36 | 1.71 | -0.03 | 453544.29 | 2.99 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 199155.37 | 3.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 5.16 | 2.83 | 0.12 | 537087.06 | 34.32 | skipped_fast |
| WUSDT | IDLE | 1.82 | 5.83 | 0.51 | 0.12 | 424137.25 | 11.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.08 | 0.11 | 59532.73 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.23 | 0.21 | 157900.45 | 19.05 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 4.71 | 0.06 | 0.12 | 67749.41 | 11.57 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 3.95 | 2.28 | -0.02 | 80381.97 | 99.83 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 4.68 | 0.65 | 0.09 | 174981.02 | 7.42 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3808.79 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.5 | 2.97 | 0.16 | 0.06 | 56241.61 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.51 | 0.07 | 173663.08 | 40.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 16.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
