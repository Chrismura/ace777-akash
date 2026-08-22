# Hulk DIGEST — 2026-08-22T01:55:29Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.9 | 10.86 | 1.64 | 0.14 | 6850401.77 | 3.93 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 10.52 | 1.51 | 0.15 | 153636103.74 | 2.69 | skipped_fast |
| HBARUSDT | IDLE | 3.04 | 6.36 | 1.24 | 0.06 | 946983.28 | 2.51 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.74 | 0.08 | 551401.3 | 2.42 | skipped_fast |
| CCUSDT | IDLE | 1.8 | 7.36 | 0.7 | 0.16 | 661896.33 | 9.65 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.56 | 0.08 | 392993.69 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.06 | 0.02 | 510713.54 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.62 | 5.86 | 0.52 | 0.05 | 185150.77 | 6.11 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79546.13 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.97 | 0.11 | 61043.38 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.07 | 0.16 | 157254.15 | 12.96 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.15 | 0.12 | 61357.71 | 11.66 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.16 | 0.07 | 171367.22 | 7.55 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.23 | 0.05 | 181481.49 | 57.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 96.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.08 | 4799.07 | 19.84 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.03 | 54605.35 | 8.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
