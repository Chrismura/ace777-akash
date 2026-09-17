# Hulk DIGEST — 2026-09-17T20:17:57Z

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
| ETHUSDT | IDLE | 0.74 | 1.34 | 0.98 | 0.02 | 310255853.87 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.35 | 0.95 | -0.01 | 40916191.67 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.89 | 0.46 | 0.01 | 443816986.68 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 42.03 | 24.37 | -0.27 | 243878.9 | 61.86 | skipped_fast |
| CCUSDT | IDLE | 2.33 | 4.23 | 3.79 | 0.05 | 575479.08 | 9.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 5.12 | 2.98 | 0.07 | 556629.95 | 3.59 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 8.62 | 0.32 | 0.13 | 316236.18 | 12.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 5.34 | 2.98 | 0.07 | 144273.3 | 18.38 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.24 | 1.44 | 0.03 | 550866.68 | 1.32 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.54 | 2.07 | 0.02 | 197202.97 | 13.07 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 3.14 | 0.41 | 0.03 | 62005.58 | 12.32 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.61 | 2.15 | 0.02 | 65397.86 | 13.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.61 | 11.33 | 3.76 | -0.07 | 46094.23 | 109.68 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.8 | 1.14 | 0.02 | 69381.24 | 7.94 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 3.77 | 2.69 | -0.01 | 76322.13 | 55.36 | skipped_fast |
| RWAINCUSDT | IDLE | 0.63 | 1.13 | 0.82 | 0.01 | 22508.83 | 23.72 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 146.13 | 21.72 | skipped_fast |
| QNTUSDT | IDLE | 0.66 | 1.21 | 0.71 | 0.02 | 40610.66 | 4.89 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.13 | 0.07 | 0.01 | 56730.28 | 29.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.11 | 0.22 | 0.04 | 0.02 | 42853.54 | 4.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
