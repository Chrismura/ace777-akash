# Hulk DIGEST — 2026-08-22T04:17:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 13.13 | 0.15 | 0.2 | 10480301.72 | 14.64 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 12.22 | 0.79 | 0.21 | 167629569.18 | 1.89 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.11 | 11.56 | 0.44 | 0.21 | 727216.77 | 5.69 | skipped_fast |
| HBARUSDT | IDLE | 2.26 | 7.14 | 0.43 | 0.12 | 1017239.61 | 8.32 | skipped_fast |
| CHIPUSDT | IDLE | 2.83 | 5.36 | 2.03 | 0.01 | 445933.97 | 6.0 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 199974.83 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.95 | 7.18 | 0.28 | 0.14 | 431109.58 | 17.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.32 | 0.11 | 535471.48 | 15.7 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.47 | -0.05 | 80182.41 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.09 | 0.1 | 59160.53 | 27.37 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.89 | 0.2 | 160295.04 | 12.79 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.55 | 0.72 | 0.13 | 67579.3 | 12.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 3.6 | 2.74 | 0.01 | 9442.75 | 59.44 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.43 | 0.09 | 178527.16 | 5.94 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56291.62 | 16.05 | skipped_fast |
| TELUSDT | IDLE | 1.14 | 2.76 | 0.0 | 0.07 | 173852.84 | 50.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 23.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
