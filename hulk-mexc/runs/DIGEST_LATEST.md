# Hulk DIGEST — 2026-10-26T21:32:30Z

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
| ETHUSDT | IDLE | 0.77 | 1.38 | 1.13 | -0.01 | 147565824.45 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.76 | 1.38 | 0.9 | -0.0 | 24466234.54 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.93 | 0.61 | -0.01 | 361914068.5 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 5.55 | 4.43 | 0.06 | 1430698.12 | 6.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.24 | 3.99 | 3.3 | -0.02 | 823237.49 | 2.72 | skipped_fast |
| WUSDT | IDLE | 2.01 | 3.87 | 2.72 | 0.03 | 668930.17 | 31.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 12.19 | 9.6 | 0.16 | 324084.65 | 21.32 | skipped_fast |
| RWAINCUSDT | IDLE | 2.43 | 9.85 | 6.18 | -0.12 | 55553.41 | 18.96 | skipped_fast |
| EDELUSDT | IDLE | 2.22 | 3.98 | 3.1 | 0.01 | 105281.11 | 31.03 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.6 | 2.33 | -0.03 | 186711.58 | 7.11 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 4.4 | 2.3 | -0.0 | 44756.99 | 65.34 | skipped_fast |
| WAXLUSDT | IDLE | 3.16 | 5.59 | 4.93 | -0.04 | 53569.6 | 34.14 | skipped_fast |
| ZBCNUSDT | IDLE | 1.09 | 2.16 | 0.89 | -0.07 | 220796.87 | 37.37 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.46 | 2.05 | -0.01 | 58564.18 | 9.09 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 2.34 | 1.89 | -0.0 | 62950.38 | 16.48 | skipped_fast |
| FLUIDUSDT | IDLE | 2.72 | 5.19 | 1.72 | -0.02 | 1901.58 | 21.64 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.85 | 0.65 | 0.01 | 53686.9 | 11.41 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.45 | 1.03 | -0.01 | 260086.96 | 9.14 | skipped_fast |
| IOTAUSDT | IDLE | 1.34 | 2.34 | 2.24 | -0.02 | 85689.95 | 28.61 | skipped_fast |
| LAUSDT | IDLE | 1.33 | 2.76 | 0.87 | 0.04 | 64632.46 | 22.05 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.88 | 0.48 | -0.0 | 53978.01 | 15.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.47 | -0.0 | 41865.97 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
