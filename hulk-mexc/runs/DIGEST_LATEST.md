# Hulk DIGEST — 2026-08-22T03:29:16Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 11.15 | 0.82 | 0.17 | 7797397.19 | 1.88 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.37 | 0.21 | 164405666.13 | 3.17 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 6.38 | 0.0 | 0.11 | 1019696.94 | 1.2 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 8.96 | 2.08 | 0.17 | 681314.49 | 5.98 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.14 | 0.08 | 198168.54 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.99 | 4.43 | 0.12 | -0.02 | 452504.29 | 5.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.4 | 0.12 | 538294.64 | 22.88 | skipped_fast |
| WUSDT | IDLE | 1.8 | 5.79 | 0.18 | 0.12 | 423019.48 | 11.79 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80000.53 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.34 | 0.1 | 59542.9 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.12 | 0.22 | 157829.86 | 10.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9338.84 | 37.87 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 4.5 | 0.18 | 0.12 | 67729.98 | 12.48 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 4.29 | 0.0 | 0.1 | 174222.04 | 4.44 | skipped_fast |
| RWAUSDT | IDLE | 1.36 | 2.72 | 0.0 | 0.06 | 56351.15 | 8.03 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.34 | 0.0 | 0.07 | 173182.43 | 61.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 18.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
