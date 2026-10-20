# Hulk DIGEST — 2026-10-20T15:00:35Z

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
| XRPUSDT | IDLE | 2.19 | 4.36 | 0.1 | 0.03 | 20890569.48 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 2.12 | 4.21 | 0.14 | 0.03 | 138176017.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.28 | 2.55 | 0.13 | 0.01 | 320457976.23 | 0.0 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.83 | 9.08 | 0.52 | 0.06 | 947550.66 | 14.09 | skipped_fast |
| WUSDT | IDLE | 3.14 | 6.16 | 0.75 | 0.03 | 734009.38 | 17.88 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 12.27 | 9.88 | -0.02 | 77881.05 | 47.33 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 17.37 | 10.66 | -0.03 | 72606.3 | 66.13 | skipped_fast |
| QNTUSDT | IDLE | 3.05 | 6.0 | 0.73 | 0.02 | 631928.57 | 3.47 | skipped_fast |
| ZBCNUSDT | IDLE | 3.94 | 7.67 | 1.42 | 0.04 | 194634.87 | 75.88 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 3.99 | 0.11 | 0.02 | 421453.47 | 7.5 | skipped_fast |
| CHIPUSDT | IDLE | 2.63 | 10.03 | 4.41 | 0.11 | 106454.45 | 17.67 | skipped_fast |
| BIOUSDT | IDLE | 3.13 | 6.23 | 0.2 | 0.06 | 63918.03 | 8.05 | skipped_fast |
| REDUSDT | IDLE | 2.54 | 5.05 | 0.2 | 0.03 | 58806.51 | 7.79 | skipped_fast |
| KITEUSDT | IDLE | 2.33 | 4.65 | 0.05 | 0.03 | 90022.38 | 10.47 | skipped_fast |
| HBARUSDT | IDLE | 2.33 | 4.66 | 0.02 | 0.03 | 372924.89 | 9.34 | skipped_fast |
| EDELUSDT | IDLE | 0.91 | 5.99 | 0.21 | 0.23 | 304772.21 | 18.07 | skipped_fast |
| IOTAUSDT | IDLE | 3.26 | 6.99 | 0.15 | 0.07 | 87384.05 | 24.92 | skipped_fast |
| LAUSDT | IDLE | 3.09 | 6.1 | 0.48 | 0.03 | 56651.96 | 22.08 | skipped_fast |
| WAXLUSDT | IDLE | 2.78 | 5.42 | 0.91 | -0.03 | 54787.86 | 61.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 2.67 | 0.0 | 0.03 | 4599.67 | 21.31 | skipped_fast |
| RWAUSDT | IDLE | 0.96 | 1.82 | 0.62 | 0.01 | 51425.99 | 31.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.79 | 1.52 | 0.37 | 0.0 | 39654.97 | 9.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
