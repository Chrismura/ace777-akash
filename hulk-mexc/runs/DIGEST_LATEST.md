# Hulk DIGEST — 2026-10-24T04:25:44Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.68 | 1.32 | 0.33 | -0.01 | 147082530.94 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 0.56 | 1.06 | 0.41 | -0.02 | 27222871.0 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.85 | 0.41 | -0.01 | 267989092.46 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 4.24 | 0.36 | -0.02 | 867883.1 | 1.4 | skipped_fast |
| WUSDT | IDLE | 1.7 | 4.39 | 1.52 | -0.05 | 923228.56 | 17.74 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 2.84 | 1.01 | -0.04 | 1220316.33 | 1.65 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.03 | 10.45 | 1.52 | 0.05 | 63141.5 | 16.11 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.85 | 0.86 | 0.0 | 628712.3 | 15.54 | skipped_fast |
| CCUSDT | IDLE | 2.31 | 4.47 | 0.99 | 0.0 | 218680.87 | 7.74 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 5.67 | 2.66 | -0.03 | 73608.31 | 16.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.64 | 3.84 | 1.63 | -0.03 | 216930.17 | 28.85 | skipped_fast |
| WAXLUSDT | IDLE | 3.66 | 7.67 | 1.35 | 0.01 | 60981.23 | 63.51 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 3.75 | 0.3 | -0.0 | 57371.35 | 11.71 | skipped_fast |
| BIOUSDT | IDLE | 1.71 | 3.34 | 0.51 | -0.02 | 76500.86 | 8.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.72 | 3.21 | 1.55 | 0.02 | 49521.87 | 21.73 | skipped_fast |
| LAUSDT | IDLE | 2.06 | 9.68 | 3.02 | 0.15 | 68281.65 | 20.46 | skipped_fast |
| HBARUSDT | IDLE | 1.38 | 2.65 | 0.75 | -0.04 | 250246.08 | 7.71 | skipped_fast |
| IOTAUSDT | IDLE | 2.14 | 4.08 | 1.35 | -0.01 | 72727.02 | 13.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.7 | 2.46 | 0.25 | 0.05 | 67395.92 | 63.02 | skipped_fast |
| FLUIDUSDT | IDLE | 1.48 | 2.78 | 1.14 | -0.01 | 5212.72 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.55 | 0.0 | 51467.99 | 15.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.34 | 0.62 | 0.4 | -0.0 | 38939.36 | 63.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
