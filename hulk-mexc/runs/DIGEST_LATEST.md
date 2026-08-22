# Hulk DIGEST — 2026-08-22T01:47:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.79 | 0.16 | 6823991.73 | 3.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 9.76 | 0.13 | 0.16 | 152223625.95 | 2.0 | skipped_fast |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.5 | 0.08 | 960677.92 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.73 | 0.09 | 551595.51 | 1.93 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.17 | 0.17 | 661468.74 | 7.85 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.32 | 0.09 | 391790.28 | 14.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.13 | 0.02 | 512320.83 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.12 | 0.06 | 186309.4 | 3.05 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79491.19 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.98 | 0.11 | 60939.99 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.84 | 0.18 | 158050.66 | 9.59 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.11 | 0.07 | 171695.18 | 1.51 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.13 | 0.13 | 61397.59 | 8.96 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.59 | 0.04 | 182126.96 | 41.58 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 90.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.95 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54653.48 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
