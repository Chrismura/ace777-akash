# Hulk DIGEST — 2026-09-28T02:15:36Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 90.56 | 28.27 | 0.49 | 14869530.92 | 6.37 | skipped_fast |
| WUSDT | IDLE | 2.18 | 9.22 | 7.34 | 0.1 | 5281437.13 | 8.74 | skipped_fast |
| PYTHUSDT | IDLE | 1.48 | 3.33 | 1.72 | -0.01 | 2018921.76 | 4.79 | skipped_fast |
| XRPUSDT | IDLE | 1.42 | 2.64 | 1.28 | -0.01 | 46698052.51 | 1.98 | skipped_fast |
| ETHUSDT | IDLE | 1.1 | 1.96 | 1.55 | -0.01 | 240562744.48 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 1.0 | 1.78 | 1.46 | -0.01 | 463393438.55 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.5 | 4.83 | 1.15 | 0.03 | 677500.53 | 10.72 | skipped_fast |
| HBARUSDT | IDLE | 2.22 | 4.38 | 0.44 | 0.05 | 906641.41 | 2.06 | skipped_fast |
| KITEUSDT | IDLE | 2.84 | 4.97 | 4.72 | -0.04 | 101090.55 | 8.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 3.83 | 3.17 | -0.03 | 243127.43 | 20.58 | skipped_fast |
| BIOUSDT | IDLE | 2.6 | 4.72 | 3.21 | -0.02 | 86270.47 | 6.38 | skipped_fast |
| EDELUSDT | IDLE | 1.84 | 8.75 | 6.59 | -0.13 | 150674.54 | 31.96 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 4.01 | 2.98 | -0.06 | 95838.77 | 15.27 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.49 | 1.88 | -0.01 | 66951.84 | 13.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 9.55 | 4.62 | -0.22 | 61612.01 | 74.21 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.8 | 0.91 | 0.06 | 176447.03 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.39 | 2.31 | 0.03 | 3556.81 | 20.26 | skipped_fast |
| RWAINCUSDT | IDLE | 0.67 | 6.69 | 2.31 | 0.24 | 30893.82 | 114.42 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.22 | 0.85 | 0.0 | 59462.78 | 57.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.66 | 0.42 | 0.01 | 39645.12 | 34.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
