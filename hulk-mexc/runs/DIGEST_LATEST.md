# Hulk DIGEST — 2026-10-22T07:25:30Z

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
| WUSDT | IDLE | 1.57 | 6.27 | 5.76 | -0.01 | 3478846.56 | 16.06 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.5 | 1.42 | -0.01 | 515248717.25 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.23 | 0.86 | 0.0 | 35715384.26 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.13 | 1.0 | -0.01 | 255513949.4 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 5.42 | 3.87 | -0.01 | 1175262.51 | 6.57 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 4.71 | 3.91 | -0.05 | 642576.48 | 3.97 | skipped_fast |
| HBARUSDT | IDLE | 1.85 | 3.34 | 2.35 | -0.03 | 1007078.3 | 1.22 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 8.4 | 7.11 | -0.01 | 369158.9 | 13.34 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 3.67 | 1.96 | -0.0 | 514609.84 | 26.46 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 5.19 | 4.48 | -0.01 | 416714.14 | 7.65 | skipped_fast |
| BIOUSDT | IDLE | 2.0 | 3.63 | 2.9 | -0.03 | 78439.17 | 8.29 | skipped_fast |
| REDUSDT | IDLE | 1.8 | 3.2 | 2.73 | -0.0 | 81890.19 | 16.71 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 2.99 | 1.94 | -0.02 | 59667.89 | 10.82 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 2.22 | 0.03 | -0.02 | 256206.81 | 23.22 | skipped_fast |
| WAXLUSDT | IDLE | 2.41 | 7.51 | 6.28 | -0.08 | 57935.8 | 53.13 | skipped_fast |
| RWAINCUSDT | IDLE | 0.93 | 3.81 | 2.17 | -0.03 | 66574.35 | 22.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 2.32 | 0.17 | 0.05 | 44901.86 | 31.58 | skipped_fast |
| LAUSDT | IDLE | 1.96 | 4.52 | 3.92 | -0.03 | 63700.23 | 25.24 | skipped_fast |
| IOTAUSDT | IDLE | 1.93 | 3.41 | 3.02 | -0.03 | 80036.86 | 26.35 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.31 | -0.0 | 53218.54 | 23.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 0.96 | 0.76 | 0.0 | 39476.04 | 54.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 1.42 | 0.33 | 0.01 | 19811.38 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
