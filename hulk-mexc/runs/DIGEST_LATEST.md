# Hulk DIGEST — 2026-10-19T11:52:38Z

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
| XRPUSDT | IDLE | 1.01 | 1.83 | 1.32 | 0.01 | 33063980.71 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.39 | 0.99 | 0.0 | 149861268.54 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.24 | 0.92 | 0.0 | 334427977.27 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 4.32 | 3.72 | -0.07 | 1003590.46 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 4.09 | 3.08 | 0.0 | 791512.82 | 2.52 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.79 | 1.97 | -0.04 | 519775.63 | 16.51 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.97 | 2.62 | -0.07 | 714436.48 | 4.81 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.55 | 2.37 | 0.02 | 239629.89 | 40.6 | skipped_fast |
| KITEUSDT | IDLE | 2.24 | 4.38 | 0.66 | 0.03 | 62993.34 | 10.95 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.58 | 0.78 | 0.02 | 328883.93 | 7.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.64 | 4.95 | 2.18 | -0.01 | 88843.97 | 5.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.1 | 3.08 | 0.0 | 87088.94 | 9.56 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.54 | 1.97 | -0.02 | 72768.67 | 8.56 | skipped_fast |
| ZBCNUSDT | IDLE | 0.53 | 1.99 | 0.25 | 0.02 | 280241.4 | 20.02 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 2.28 | 1.72 | -0.01 | 77078.73 | 16.96 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 4.84 | 3.68 | -0.05 | 60090.16 | 50.8 | skipped_fast |
| IOTAUSDT | IDLE | 1.74 | 3.11 | 2.51 | -0.02 | 76170.15 | 24.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 3.69 | 3.55 | 0.01 | 6404.42 | 21.47 | skipped_fast |
| WAXLUSDT | IDLE | 1.11 | 4.2 | 3.52 | 0.01 | 78660.0 | 40.33 | skipped_fast |
| LAUSDT | IDLE | 1.27 | 2.27 | 1.86 | -0.02 | 59219.88 | 26.59 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.8 | 0.32 | 0.01 | 55125.46 | 23.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.11 | -0.0 | 40225.92 | 4.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
