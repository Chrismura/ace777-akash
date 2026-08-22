# Hulk DIGEST — 2026-08-22T01:52:24Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 10.86 | 1.26 | 0.14 | 6838729.7 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 10.52 | 1.34 | 0.15 | 153291011.22 | 4.03 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.9 | 0.07 | 959817.84 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.73 | 0.08 | 553241.89 | 4.84 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.43 | 0.16 | 661309.25 | 6.12 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.28 | 0.08 | 391454.31 | 14.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.76 | 0.02 | 512100.31 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.59 | 5.86 | 0.18 | 0.06 | 185113.17 | 3.04 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79521.16 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.93 | 0.11 | 61015.54 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.59 | 0.16 | 157202.26 | 8.06 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.43 | 0.12 | 61344.7 | 13.46 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 5.18 | 1.24 | 0.06 | 171672.02 | 6.05 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.18 | 0.05 | 181535.43 | 51.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9215.12 | 69.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 23.42 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54629.0 | 24.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
