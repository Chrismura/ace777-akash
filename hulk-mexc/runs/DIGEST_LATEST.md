# Hulk DIGEST — 2026-10-19T16:01:20Z

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
| ETHUSDT | IDLE | 1.02 | 1.83 | 1.4 | 0.01 | 163752201.49 | 0.29 | skipped_fast |
| XRPUSDT | IDLE | 0.93 | 1.67 | 1.24 | 0.02 | 29443661.82 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.17 | 0.94 | 0.01 | 352152654.91 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 4.17 | 1.24 | -0.02 | 953663.81 | 4.05 | skipped_fast |
| WUSDT | IDLE | 2.41 | 4.68 | 0.89 | -0.0 | 515942.64 | 15.28 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 4.11 | 3.07 | 0.04 | 866720.28 | 0.51 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 4.43 | 2.8 | 0.04 | 390799.24 | 5.8 | skipped_fast |
| RIZEUSDT | IDLE | 3.08 | 10.92 | 4.57 | -0.07 | 73238.52 | 27.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.92 | 6.71 | 2.69 | 0.0 | 89906.01 | 30.75 | skipped_fast |
| HBARUSDT | IDLE | 1.5 | 2.62 | 2.54 | -0.04 | 554105.71 | 6.1 | skipped_fast |
| KITEUSDT | IDLE | 2.02 | 5.86 | 0.41 | 0.09 | 62403.36 | 1.62 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.86 | 1.35 | 0.02 | 234120.59 | 18.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 4.33 | 2.91 | 0.01 | 79044.07 | 12.2 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.19 | 1.32 | 0.01 | 59761.93 | 8.01 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 2.25 | 1.94 | 0.02 | 264383.58 | 14.23 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.07 | 1.05 | 0.01 | 71365.55 | 8.53 | skipped_fast |
| LAUSDT | IDLE | 1.53 | 2.71 | 2.29 | 0.01 | 56630.98 | 24.93 | skipped_fast |
| IOTAUSDT | IDLE | 1.17 | 2.16 | 1.2 | 0.01 | 75866.19 | 18.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.23 | 3.05 | 2.96 | 0.01 | 5787.49 | 21.56 | skipped_fast |
| WAXLUSDT | IDLE | 1.12 | 3.66 | 3.07 | 0.05 | 77994.0 | 66.95 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.27 | 0.39 | 0.01 | 54972.22 | 31.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.5 | 0.31 | -0.0 | 40239.38 | 29.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
