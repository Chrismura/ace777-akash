# Hulk DIGEST — 2026-09-02T17:30:45Z

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
| XRPUSDT | IDLE | 1.19 | 2.19 | 1.24 | -0.03 | 39486685.57 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 1.09 | 1.93 | 1.62 | -0.02 | 413862881.41 | 0.08 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 10.66 | 3.07 | 0.13 | 1332418.88 | 5.21 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.26 | 0.6 | -0.01 | 543249852.13 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 9.13 | 6.96 | -0.04 | 1037316.65 | 14.66 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.6 | 1.6 | -0.02 | 362952.88 | 13.66 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.56 | 2.22 | -0.04 | 353883.7 | 8.19 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.1 | 9.92 | 0.31 | -0.01 | 38132.9 | 71.98 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 8.17 | 0.27 | 0.17 | 96635.06 | 7.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 2.67 | 2.59 | -0.06 | 176138.11 | 12.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.96 | 5.69 | 2.8 | 0.08 | 10064.32 | 5.43 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 2.43 | 0.72 | 0.03 | 151296.38 | 11.27 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.52 | 2.51 | 0.06 | 169415.79 | 16.63 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.67 | 0.82 | -0.02 | 68520.09 | 3.95 | skipped_fast |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 2.33 | -0.06 | 1836.1 | 21.75 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.46 | 1.15 | -0.02 | 197675.44 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.47 | 0.38 | 0.02 | 51754.1 | 7.56 | skipped_fast |
| TELUSDT | IDLE | 1.56 | 3.0 | 0.76 | 0.01 | 75831.54 | 64.61 | skipped_fast |
| QNTUSDT | IDLE | 0.96 | 1.89 | 0.23 | 0.01 | 63848.96 | 6.19 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.16 | -0.01 | 32405.05 | 19.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
