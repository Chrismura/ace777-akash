# Hulk DIGEST — 2026-10-09T13:30:22Z

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
| WUSDT | IDLE | 1.41 | 8.73 | 4.6 | 0.09 | 2719389.22 | 6.73 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 5.89 | 2.04 | 0.13 | 3469552.1 | 5.83 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 5.14 | 1.76 | 0.03 | 1944833.21 | 10.83 | skipped_fast |
| XRPUSDT | IDLE | 1.06 | 1.91 | 1.42 | -0.01 | 48275302.03 | 2.16 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.29 | 0.98 | -0.02 | 455854282.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.71 | 1.33 | 0.65 | 0.01 | 412781615.15 | 0.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.14 | 9.13 | 1.72 | 0.04 | 623073.44 | 6.41 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 18.08 | 7.71 | -0.11 | 78690.88 | 33.12 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 8.47 | 1.25 | 0.07 | 387711.06 | 15.84 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 7.25 | 5.42 | -0.03 | 100437.62 | 16.67 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 2.03 | 0.58 | -0.02 | 802577.84 | 4.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 6.41 | 5.84 | 0.01 | 241217.6 | 26.15 | skipped_fast |
| FLUIDUSDT | IDLE | 2.37 | 15.69 | 13.0 | 0.04 | 13059.93 | 21.49 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 3.09 | 2.51 | -0.03 | 81447.31 | 3.57 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 6.37 | 1.73 | 0.05 | 10847.13 | 110.13 | skipped_fast |
| KITEUSDT | IDLE | 0.86 | 2.25 | 1.76 | -0.09 | 66996.91 | 12.96 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.69 | 1.36 | -0.02 | 66888.29 | 16.39 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 3.05 | 1.69 | 0.0 | 133668.25 | 42.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.2 | 0.22 | -0.02 | 36412.17 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.23 | -0.03 | 54165.46 | 15.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
