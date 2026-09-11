# Hulk DIGEST — 2026-09-11T20:21:25Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 182.0 | 27.6 | 1.58 | 207268.87 | 388.19 | skipped_fast |
| XRPUSDT | IDLE | 2.2 | 4.4 | 3.02 | 0.01 | 53794972.13 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 1.62 | 3.42 | 2.94 | 0.03 | 627358624.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.39 | 2.5 | 1.83 | 0.0 | 558764995.02 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.63 | 6.68 | 5.76 | -0.01 | 410833.86 | 1.96 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.51 | 10.48 | 0.0 | 0.05 | 163948.61 | 34.25 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 3.53 | 2.62 | -0.01 | 436326.66 | 5.1 | skipped_fast |
| WUSDT | IDLE | 2.54 | 4.84 | 3.68 | 0.01 | 196808.0 | 16.54 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 6.38 | 5.58 | -0.05 | 149041.62 | 12.7 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 3.54 | 3.12 | 0.0 | 188199.03 | 17.99 | skipped_fast |
| BIOUSDT | IDLE | 2.34 | 4.24 | 2.98 | -0.0 | 82882.37 | 11.98 | skipped_fast |
| RWAINCUSDT | IDLE | 2.83 | 6.09 | 0.74 | 0.06 | 12375.79 | 47.89 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 2.92 | 1.98 | -0.01 | 59032.83 | 13.81 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 3.64 | 2.68 | -0.01 | 232045.8 | 1.34 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.54 | 0.61 | 0.05 | 62222.36 | 18.08 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 3.71 | 2.53 | -0.01 | 96623.64 | 39.54 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 2.91 | 2.65 | -0.02 | 41737.02 | 6.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 2.66 | 2.19 | 0.02 | 1301.43 | 20.86 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.35 | 0.74 | 0.02 | 52156.93 | 7.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.83 | 1.45 | 1.36 | 0.0 | 36675.98 | 44.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
