# Hulk DIGEST — 2026-09-18T03:05:05Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.94 | 1.82 | 0.43 | 0.0 | 34484115.24 | 2.3 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.24 | 0.16 | 0.01 | 283198196.01 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 1.01 | 0.04 | 0.01 | 416129676.72 | 0.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.95 | 9.75 | 0.01 | 0.13 | 527865.95 | 9.1 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 5.29 | 0.98 | 0.07 | 577267.17 | 3.46 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.37 | 14.0 | 0.0 | 0.16 | 195062.97 | 16.54 | skipped_fast |
| REDUSDT | IDLE | 3.26 | 6.43 | 0.63 | 0.04 | 67386.36 | 16.08 | skipped_fast |
| HBARUSDT | IDLE | 1.65 | 3.28 | 0.12 | 0.03 | 519479.5 | 1.31 | skipped_fast |
| EDELUSDT | IDLE | 0.98 | 10.73 | 2.59 | -0.13 | 288348.59 | 74.19 | skipped_fast |
| WUSDT | IDLE | 0.73 | 1.71 | 0.62 | 0.09 | 317695.09 | 11.03 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.25 | 0.0 | 0.02 | 68821.08 | 7.78 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.69 | 1.21 | 0.02 | 61564.44 | 12.18 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 1.42 | 0.46 | 0.0 | 215229.09 | 34.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 8.39 | 3.66 | -0.04 | 41881.67 | 122.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.06 | 1.54 | -0.03 | 14621.75 | 24.14 | skipped_fast |
| RWAUSDT | IDLE | 1.68 | 3.15 | 1.38 | 0.02 | 60582.78 | 44.28 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 2.17 | 0.26 | 0.02 | 40839.17 | 4.85 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 2.43 | 0.14 | -0.01 | 73745.99 | 41.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.71 | 1.35 | 0.5 | 0.02 | 43566.77 | 30.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.39 | 0.02 | 148.34 | 21.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
