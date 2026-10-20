# Hulk DIGEST — 2026-10-20T21:03:08Z

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
| XRPUSDT | IDLE | 0.75 | 1.5 | 0.06 | 0.03 | 24087637.28 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.66 | 1.28 | 0.29 | 0.02 | 149636936.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.7 | 0.09 | 0.01 | 320393750.97 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 6.24 | 0.17 | 0.11 | 1160173.12 | 6.27 | skipped_fast |
| WUSDT | IDLE | 1.66 | 3.32 | 0.02 | 0.03 | 645753.36 | 14.12 | skipped_fast |
| QNTUSDT | IDLE | 1.49 | 2.98 | 0.0 | 0.02 | 792116.8 | 3.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 5.69 | 2.41 | 0.09 | 372920.95 | 17.66 | skipped_fast |
| RIZEUSDT | IDLE | 2.36 | 9.41 | 6.15 | 0.04 | 75035.57 | 59.81 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.86 | 1.39 | 0.01 | 383754.11 | 8.55 | skipped_fast |
| ZBCNUSDT | IDLE | 1.98 | 3.67 | 1.94 | 0.03 | 191144.41 | 42.66 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.76 | 2.79 | 0.34 | 363631.96 | 16.85 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.68 | 1.05 | 0.03 | 59558.36 | 0.71 | skipped_fast |
| BIOUSDT | IDLE | 1.22 | 2.38 | 0.36 | 0.06 | 62435.74 | 8.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 3.35 | 1.31 | -0.02 | 68811.99 | 26.43 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.62 | 0.0 | 0.03 | 366384.11 | 8.3 | skipped_fast |
| KITEUSDT | IDLE | 0.47 | 0.93 | 0.1 | 0.0 | 82630.91 | 10.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.07 | 6267.92 | 21.36 | skipped_fast |
| IOTAUSDT | IDLE | 1.31 | 2.49 | 0.93 | 0.05 | 72532.22 | 23.48 | skipped_fast |
| WAXLUSDT | IDLE | 1.42 | 2.61 | 1.59 | -0.04 | 56595.58 | 57.72 | skipped_fast |
| LAUSDT | IDLE | 1.14 | 2.26 | 0.07 | 0.04 | 55754.22 | 25.8 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.55 | 0.0 | 0.0 | 51816.39 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.63 | 0.26 | 0.0 | 39814.17 | 34.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
