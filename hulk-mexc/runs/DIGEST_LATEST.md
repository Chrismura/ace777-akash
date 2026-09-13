# Hulk DIGEST — 2026-09-13T13:40:01Z

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
| ETHUSDT | IDLE | 1.3 | 2.32 | 1.83 | -0.03 | 237180945.61 | 0.36 | skipped_fast |
| XRPUSDT | IDLE | 1.14 | 2.03 | 1.63 | -0.02 | 14184768.33 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.88 | 0.62 | -0.01 | 286299774.19 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 14.26 | 9.56 | 0.08 | 203467.67 | 16.13 | skipped_fast |
| PYTHUSDT | IDLE | 1.86 | 3.64 | 0.49 | 0.03 | 451823.93 | 1.82 | skipped_fast |
| CCUSDT | IDLE | 2.11 | 3.79 | 2.83 | -0.03 | 279947.1 | 10.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 8.52 | 7.28 | -0.1 | 82826.21 | 13.73 | skipped_fast |
| WUSDT | IDLE | 1.59 | 2.92 | 1.73 | 0.01 | 249656.24 | 15.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 15.14 | 1.57 | 0.19 | 105182.89 | 37.74 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.24 | 2.48 | -0.04 | 7571.12 | 5.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.07 | 1.9 | 1.65 | -0.05 | 189175.15 | 34.71 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.01 | 1.43 | 0.02 | 63758.1 | 11.98 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.83 | 1.33 | -0.02 | 68038.32 | 7.91 | skipped_fast |
| REDUSDT | IDLE | 0.8 | 1.6 | 0.02 | 0.03 | 60353.9 | 18.21 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 2.56 | 1.62 | -0.06 | 86797.16 | 31.7 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.5 | 0.04 | 0.01 | 179852.39 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 1.96 | 0.81 | -0.01 | 53943.1 | 44.81 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.12 | 0.2 | -0.01 | 37254.41 | 12.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.52 | 0.91 | 0.9 | -0.0 | 1225.97 | 21.15 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.32 | 0.1 | 0.0 | 32349.72 | 22.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
