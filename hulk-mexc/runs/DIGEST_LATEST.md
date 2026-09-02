# Hulk DIGEST — 2026-09-02T16:50:41Z

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
| XRPUSDT | IDLE | 1.27 | 2.41 | 0.85 | -0.02 | 39631234.52 | 2.25 | skipped_fast |
| ETHUSDT | IDLE | 1.17 | 2.16 | 1.17 | -0.02 | 407163945.96 | 0.17 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 11.65 | 10.44 | -0.06 | 1026450.73 | 2.48 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 10.66 | 1.77 | 0.16 | 1306152.13 | 3.43 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.58 | 0.36 | -0.0 | 541533962.89 | 0.53 | skipped_fast |
| REDUSDT | IDLE | 2.78 | 5.41 | 1.06 | 0.02 | 159182.46 | 11.31 | skipped_fast |
| WUSDT | IDLE | 1.82 | 3.6 | 0.24 | 0.0 | 366805.95 | 16.61 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.61 | 1.02 | -0.02 | 355143.92 | 10.81 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.66 | 8.53 | 0.29 | -0.04 | 38204.09 | 39.51 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 7.6 | 0.76 | 0.14 | 98273.51 | 12.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.25 | 1.23 | -0.05 | 177078.17 | 17.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.91 | 5.69 | 2.38 | 0.09 | 10441.8 | 37.79 | skipped_fast |
| EDELUSDT | IDLE | 0.67 | 3.61 | 2.11 | 0.07 | 169550.97 | 41.34 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 1.8 | 0.71 | -0.02 | 70012.68 | 3.95 | skipped_fast |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 2.33 | -0.06 | 1836.1 | 21.7 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.64 | 1.0 | -0.01 | 199866.51 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.47 | 0.38 | 0.02 | 51558.08 | 7.56 | skipped_fast |
| TELUSDT | IDLE | 1.7 | 3.24 | 1.05 | 0.0 | 75255.8 | 76.18 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 2.0 | 0.48 | 0.02 | 68612.36 | 4.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.52 | 0.38 | -0.01 | 33060.46 | 48.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
