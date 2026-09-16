# Hulk DIGEST — 2026-09-16T15:12:23Z

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
| XRPUSDT | IDLE | 1.08 | 2.96 | 2.08 | -0.09 | 81939624.72 | 1.57 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.06 | 1.36 | -0.01 | 424730033.55 | 0.83 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.13 | 0.67 | -0.0 | 565528354.02 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 3.21 | 2.28 | -0.02 | 668074.56 | 1.91 | skipped_fast |
| CCUSDT | IDLE | 1.87 | 3.55 | 1.33 | -0.03 | 452493.94 | 6.6 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 5.94 | 5.08 | -0.05 | 64976.72 | 17.34 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 7.82 | 6.16 | -0.04 | 98794.46 | 24.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.53 | 24.15 | 17.69 | 0.39 | 58360.32 | 63.86 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 9.08 | 8.29 | 0.3 | 414149.75 | 34.69 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.84 | 2.36 | -0.02 | 80488.1 | 4.1 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.34 | 2.37 | -0.06 | 352253.17 | 1.38 | skipped_fast |
| WUSDT | IDLE | 1.04 | 2.33 | 1.06 | -0.07 | 220698.87 | 14.67 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 2.92 | 1.93 | -0.05 | 59597.77 | 13.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 2.59 | 1.2 | -0.01 | 195325.43 | 18.68 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 5.6 | 3.81 | -0.07 | 123214.06 | 42.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 2.31 | 1.51 | -0.03 | 13229.5 | 53.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.17 | 2.13 | -0.06 | 2518.27 | 21.54 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 2.02 | 1.02 | -0.05 | 42749.38 | 5.05 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.76 | 0.08 | -0.01 | 53101.48 | 7.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.08 | -0.02 | 32760.85 | 7.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
