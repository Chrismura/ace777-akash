# Hulk DIGEST — 2026-10-25T20:09:15Z

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
| ETHUSDT | IDLE | 0.65 | 1.21 | 0.59 | 0.0 | 79398472.45 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.17 | 0.82 | 0.01 | 14082749.35 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.57 | 0.47 | 0.0 | 141672353.04 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.79 | 6.2 | 0.59 | 0.07 | 535390.85 | 5.32 | skipped_fast |
| EDELUSDT | IDLE | 3.21 | 7.36 | 1.2 | 0.05 | 385190.02 | 28.65 | skipped_fast |
| QNTUSDT | IDLE | 2.74 | 8.8 | 2.03 | 0.09 | 620404.2 | 3.06 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.82 | 1.76 | -0.02 | 578588.26 | 19.14 | skipped_fast |
| ZBCNUSDT | IDLE | 3.06 | 5.71 | 3.39 | 0.04 | 198182.97 | 18.39 | skipped_fast |
| CHIPUSDT | IDLE | 2.55 | 4.81 | 1.99 | 0.05 | 91444.12 | 17.68 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 3.92 | 2.49 | -0.01 | 53347.02 | 9.75 | skipped_fast |
| RIZEUSDT | IDLE | 2.41 | 6.05 | 3.28 | 0.01 | 48345.27 | 67.0 | skipped_fast |
| REDUSDT | IDLE | 1.77 | 3.39 | 0.94 | -0.02 | 63020.3 | 15.1 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 2.12 | 0.62 | 0.01 | 176419.05 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.67 | 1.58 | -0.01 | 63488.24 | 11.1 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.52 | 1.19 | -0.02 | 60030.79 | 4.46 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.84 | 0.63 | -0.0 | 121726.41 | 7.73 | skipped_fast |
| WAXLUSDT | IDLE | 1.5 | 2.69 | 2.08 | 0.0 | 53557.28 | 46.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 6.03 | 0.56 | 0.05 | 19243.78 | 21.23 | skipped_fast |
| LAUSDT | IDLE | 0.85 | 3.18 | 1.92 | -0.08 | 71044.52 | 24.41 | skipped_fast |
| IOTAUSDT | IDLE | 0.94 | 1.76 | 0.81 | -0.01 | 63842.32 | 27.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.88 | 1.57 | 1.29 | -0.01 | 37106.69 | 60.17 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.56 | 0.08 | 0.0 | 51371.07 | 15.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
