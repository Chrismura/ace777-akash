# Hulk DIGEST — 2026-08-22T04:47:56Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.95 | 15.41 | 0.09 | 0.21 | 12020843.29 | 7.17 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 16.25 | 0.0 | 0.26 | 176732084.63 | 2.42 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 8.85 | 0.21 | 0.14 | 1073286.67 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.45 | 0.2 | 737401.21 | 6.57 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.44 | 0.01 | 450980.69 | 8.95 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.05 | 8.03 | 0.08 | 0.15 | 433759.77 | 11.51 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.26 | 0.06 | 200923.2 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.05 | 0.12 | 537911.33 | 29.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.55 | 0.09 | 58569.77 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.44 | 0.21 | 158093.07 | 9.55 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.07 | 2.17 | -0.02 | 80170.38 | 44.4 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.48 | 0.1 | 182401.56 | 36.96 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.28 | 0.14 | 67957.87 | 29.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 48.95 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.59 | 0.1 | 182242.54 | 19.86 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56616.19 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
