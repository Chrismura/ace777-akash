# Hulk DIGEST — 2026-08-22T02:36:44Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.52 | 1.0 | 0.15 | 7131944.53 | 19.16 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 12.02 | 0.71 | 0.18 | 156289593.69 | 5.23 | skipped_fast |
| HBARUSDT | IDLE | 2.44 | 5.62 | 0.65 | 0.08 | 975919.01 | 2.47 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.8 | 0.1 | 542919.56 | 33.08 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.75 | 0.12 | 0.15 | 653157.5 | 6.93 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 5.26 | 0.84 | -0.01 | 456603.41 | 6.04 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.16 | 8.18 | 1.29 | 0.09 | 193553.43 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.95 | 5.62 | 0.23 | 0.1 | 410701.34 | 11.98 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 5.02 | 2.28 | -0.03 | 79767.33 | 44.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.2 | 0.1 | 61497.29 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.95 | 0.17 | 157820.18 | 23.45 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.31 | 0.08 | 172628.96 | 5.95 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.47 | 0.12 | 62454.06 | 11.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9324.96 | 43.38 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 176306.02 | 56.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.12 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.25 | 0.16 | 0.04 | 55214.67 | 32.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
