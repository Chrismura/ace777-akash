# Hulk DIGEST — 2026-08-22T04:24:36Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.9 | 13.61 | 1.29 | 0.19 | 10798214.3 | 14.75 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.11 | 12.23 | 0.04 | 0.22 | 169207921.08 | 3.76 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 11.56 | 1.74 | 0.2 | 730111.72 | 8.24 | skipped_fast |
| HBARUSDT | IDLE | 2.26 | 7.14 | 0.53 | 0.12 | 1034079.86 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.32 | 0.01 | 442530.62 | 5.95 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.99 | 0.08 | 200061.93 | 2.99 | skipped_fast |
| WUSDT | IDLE | 1.95 | 7.18 | 0.14 | 0.14 | 434231.15 | 8.71 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.91 | 0.13 | 536226.07 | 24.15 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.04 | 80098.26 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.06 | 0.09 | 59195.0 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.77 | 0.21 | 158571.69 | 8.78 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.64 | 0.13 | 67782.64 | 12.43 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9394.01 | 70.63 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.49 | 0.09 | 178574.65 | 10.37 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 3.12 | 0.4 | 0.09 | 176554.31 | 40.57 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56325.63 | 16.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
