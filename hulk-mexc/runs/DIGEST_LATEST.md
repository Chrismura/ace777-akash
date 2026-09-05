# Hulk DIGEST — 2026-09-05T12:24:07Z

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
| XRPUSDT | IDLE | 0.43 | 0.79 | 0.45 | -0.03 | 35857783.51 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.17 | 0.3 | 0.23 | -0.03 | 344966436.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.11 | -0.02 | 479177670.92 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.4 | 25.72 | 12.89 | -0.19 | 153584.3 | 45.71 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 7.2 | 6.17 | 0.02 | 438247.2 | 3.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.28 | 0.38 | -0.01 | 417264.9 | 1.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.66 | 0.63 | -0.05 | 198616.76 | 15.71 | skipped_fast |
| CCUSDT | IDLE | 0.49 | 0.97 | 0.12 | -0.02 | 318779.0 | 5.52 | skipped_fast |
| REDUSDT | IDLE | 1.29 | 2.32 | 1.77 | 0.04 | 65275.51 | 11.88 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.0 | 1.96 | -0.05 | 62802.73 | 10.76 | skipped_fast |
| WUSDT | IDLE | 0.54 | 1.05 | 0.26 | 0.02 | 201848.98 | 5.02 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.5 | 0.8 | -0.0 | 85264.89 | 3.64 | skipped_fast |
| EDELUSDT | IDLE | 0.18 | 3.28 | 1.4 | -0.04 | 221458.39 | 28.37 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.52 | 1.49 | -0.02 | 5598.73 | 5.41 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.6 | 0.37 | 0.02 | 284203.95 | 1.24 | skipped_fast |
| RWAUSDT | IDLE | 1.4 | 2.7 | 0.71 | 0.01 | 53367.49 | 21.47 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 1.9 | 1.28 | -0.03 | 75604.35 | 53.14 | skipped_fast |
| QNTUSDT | IDLE | 0.47 | 0.83 | 0.79 | -0.04 | 39777.1 | 3.14 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 0.96 | 0.0 | -0.01 | 934.67 | 22.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.3 | 0.22 | -0.01 | 36996.02 | 27.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
