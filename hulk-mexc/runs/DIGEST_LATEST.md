# Hulk DIGEST — 2026-10-25T13:03:19Z

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
| ETHUSDT | IDLE | 0.69 | 1.29 | 0.57 | -0.01 | 131133844.73 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.09 | 0.53 | 0.01 | 22492613.11 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.75 | 0.31 | -0.0 | 201070367.25 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.12 | 2.96 | -0.05 | 816432.27 | 16.9 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 3.1 | 1.17 | 0.01 | 508754.74 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 1.78 | 3.37 | 1.33 | -0.04 | 496674.55 | 26.98 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 10.5 | 7.65 | -0.02 | 17354.35 | 21.32 | skipped_fast |
| REDUSDT | IDLE | 2.22 | 3.98 | 3.06 | -0.04 | 67100.12 | 9.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.7 | 2.64 | 0.05 | 99334.72 | 15.76 | skipped_fast |
| QNTUSDT | IDLE | 1.6 | 3.07 | 0.93 | 0.01 | 399200.93 | 1.1 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 2.03 | 0.16 | -0.0 | 191632.29 | 8.91 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 1.62 | 0.87 | 0.02 | 229640.1 | 17.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.5 | 1.08 | -0.03 | 57815.05 | 10.95 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.09 | 0.8 | -0.04 | 65177.94 | 8.98 | skipped_fast |
| KITEUSDT | IDLE | 0.89 | 1.7 | 0.51 | -0.05 | 59278.15 | 9.85 | skipped_fast |
| WAXLUSDT | IDLE | 2.23 | 4.31 | 0.95 | 0.01 | 53516.2 | 26.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 2.14 | 0.8 | -0.03 | 39995.0 | 67.22 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.79 | 1.38 | -0.0 | 192393.0 | 13.05 | skipped_fast |
| LAUSDT | IDLE | 0.83 | 3.57 | 3.34 | -0.12 | 71302.15 | 8.92 | skipped_fast |
| IOTAUSDT | IDLE | 1.13 | 2.09 | 1.13 | -0.03 | 64261.16 | 25.67 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.43 | 1.18 | -0.0 | 51816.94 | 23.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.13 | -0.0 | 37651.93 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
