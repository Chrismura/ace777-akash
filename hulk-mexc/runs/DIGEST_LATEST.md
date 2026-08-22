# Hulk DIGEST — 2026-08-22T02:24:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 9.45 | 0.56 | 0.15 | 6971999.58 | 1.93 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.44 | 0.73 | 0.17 | 154780110.08 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 2.33 | 5.05 | 0.32 | 0.08 | 962244.73 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.73 | 0.09 | 543143.29 | 8.71 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.32 | 0.1 | 0.15 | 656468.18 | 11.3 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 5.07 | 0.72 | -0.01 | 474685.26 | 6.04 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.09 | 8.18 | 0.0 | 0.1 | 192910.58 | 5.86 | skipped_fast |
| WUSDT | IDLE | 1.85 | 5.09 | 0.11 | 0.1 | 402109.31 | 20.04 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 5.02 | 3.15 | -0.03 | 79693.24 | 44.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.89 | 0.11 | 61340.51 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 8.27 | 6.77 | 0.17 | 157000.88 | 11.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9379.52 | 32.54 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.74 | 0.11 | 61808.49 | 11.72 | skipped_fast |
| QNTUSDT | IDLE | 2.23 | 4.89 | 0.09 | 0.08 | 171135.77 | 8.96 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.28 | 0.04 | 178535.2 | 72.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.08 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54867.91 | 16.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
