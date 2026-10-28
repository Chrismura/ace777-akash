# Hulk DIGEST — 2026-10-28T17:35:00Z

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
| ETHUSDT | IDLE | 0.91 | 1.66 | 1.12 | -0.01 | 182473461.07 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.7 | 1.28 | 0.85 | -0.01 | 19217304.54 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.16 | 0.86 | -0.0 | 276577555.19 | 0.02 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 9.73 | 8.74 | -0.01 | 36632.58 | 6.81 | skipped_fast |
| CCUSDT | IDLE | 2.82 | 6.57 | 1.73 | 0.01 | 389957.2 | 8.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 10.65 | 9.28 | -0.11 | 217108.69 | 20.82 | skipped_fast |
| PYTHUSDT | IDLE | 1.46 | 2.57 | 2.27 | -0.02 | 380364.84 | 4.25 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.42 | 1.63 | -0.01 | 425400.77 | 14.24 | skipped_fast |
| QNTUSDT | IDLE | 2.24 | 4.03 | 3.05 | -0.03 | 399426.51 | 5.15 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 3.18 | 1.84 | -0.06 | 259916.39 | 15.54 | skipped_fast |
| EDELUSDT | IDLE | 1.54 | 2.77 | 2.06 | -0.01 | 189118.43 | 12.35 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.07 | 1.76 | -0.02 | 497147.44 | 8.0 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.75 | 1.75 | -0.0 | 84062.55 | 4.46 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.08 | 1.45 | -0.03 | 58605.86 | 9.58 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.71 | 1.12 | -0.02 | 54698.69 | 14.58 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 1.91 | 1.67 | 0.02 | 37769.77 | 38.98 | skipped_fast |
| LAUSDT | IDLE | 1.88 | 3.32 | 2.99 | -0.07 | 57739.82 | 26.17 | skipped_fast |
| IOTAUSDT | IDLE | 1.72 | 3.05 | 2.6 | -0.02 | 73835.31 | 21.87 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.76 | -0.01 | 6687.12 | 21.66 | skipped_fast |
| WAXLUSDT | IDLE | 1.35 | 2.38 | 2.16 | -0.02 | 55947.85 | 72.89 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.12 | 0.95 | -0.01 | 55516.27 | 48.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.51 | 0.51 | 0.01 | 35582.36 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
