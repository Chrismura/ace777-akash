# Hulk DIGEST — 2026-10-27T12:10:44Z

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
| XRPUSDT | IDLE | 0.72 | 1.37 | 0.44 | 0.01 | 21133284.91 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.17 | 0.45 | -0.01 | 145511299.88 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.8 | 0.32 | -0.01 | 347265817.26 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.29 | 5.78 | 5.04 | -0.07 | 1023345.84 | 2.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.47 | 2.6 | 2.27 | -0.04 | 532260.42 | 6.92 | skipped_fast |
| WUSDT | IDLE | 1.23 | 2.41 | 0.32 | 0.05 | 514267.72 | 26.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 7.49 | 0.76 | 0.12 | 320904.1 | 16.92 | skipped_fast |
| RWAINCUSDT | IDLE | 2.16 | 8.54 | 6.93 | -0.13 | 52305.79 | 26.81 | skipped_fast |
| EDELUSDT | IDLE | 1.21 | 2.29 | 0.92 | 0.01 | 352599.31 | 21.6 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.24 | 0.74 | -0.03 | 223270.13 | 8.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 3.29 | 2.2 | 0.02 | 253667.86 | 40.85 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.85 | 1.52 | -0.01 | 62563.8 | 15.06 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.62 | 1.61 | -0.01 | 56530.98 | 9.11 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.1 | 0.49 | 0.01 | 54092.22 | 11.41 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.89 | 1.57 | -0.02 | 210953.54 | 10.56 | skipped_fast |
| WAXLUSDT | IDLE | 1.83 | 3.31 | 2.37 | 0.0 | 54361.5 | 37.39 | skipped_fast |
| RIZEUSDT | IDLE | 0.6 | 1.1 | 0.72 | -0.03 | 42854.78 | 65.54 | skipped_fast |
| IOTAUSDT | IDLE | 1.07 | 2.0 | 0.9 | -0.02 | 94968.74 | 16.71 | skipped_fast |
| LAUSDT | IDLE | 1.02 | 1.87 | 1.11 | -0.02 | 61657.53 | 22.75 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.16 | 1.38 | 0.03 | 3127.48 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.22 | 0.4 | -0.01 | 56370.74 | 8.04 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.77 | 0.48 | -0.0 | 37220.1 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
