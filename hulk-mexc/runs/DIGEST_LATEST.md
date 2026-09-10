# Hulk DIGEST — 2026-09-10T01:14:54Z

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
| XRPUSDT | IDLE | 1.07 | 1.97 | 1.07 | -0.02 | 43184101.06 | 2.16 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.43 | 0.37 | -0.01 | 385148595.72 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.93 | 0.24 | -0.01 | 552110789.43 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.53 | 6.65 | 4.24 | -0.03 | 1043054.68 | 1.91 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.05 | 14.07 | 1.14 | 0.08 | 219108.4 | 26.51 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.75 | 1.4 | -0.04 | 629117.73 | 5.76 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 8.04 | 5.63 | -0.09 | 103478.6 | 11.78 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 13.98 | 9.86 | -0.07 | 124214.28 | 15.91 | skipped_fast |
| WUSDT | IDLE | 2.61 | 5.08 | 2.63 | -0.03 | 210993.38 | 11.08 | skipped_fast |
| REDUSDT | IDLE | 2.79 | 5.33 | 1.67 | 0.02 | 64121.37 | 17.07 | skipped_fast |
| RWAINCUSDT | IDLE | 2.15 | 3.88 | 2.74 | -0.01 | 6032.32 | 5.67 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 3.5 | 1.7 | -0.01 | 57056.15 | 11.49 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.45 | 1.17 | -0.03 | 471634.91 | 1.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 2.1 | 1.25 | 0.02 | 184334.65 | 26.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 10.0 | 1.16 | 0.02 | 75198.97 | 107.06 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.62 | -0.03 | 55293.41 | 7.48 | skipped_fast |
| MNSRYUSDT | IDLE | 1.25 | 2.18 | 2.12 | -0.01 | 26126.59 | 5.54 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.16 | 1.03 | -0.0 | 45269.79 | 5.97 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.84 | 1.54 | 0.0 | 97456.07 | 50.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.75 | 1.72 | -0.08 | 997.13 | 21.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
