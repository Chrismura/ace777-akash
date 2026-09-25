# Hulk DIGEST — 2026-09-25T20:45:48Z

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
| XRPUSDT | IDLE | 1.47 | 2.71 | 1.53 | 0.02 | 116398707.06 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.1 | 0.25 | 0.0 | 333721399.92 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.07 | -0.0 | 703305963.82 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 4.66 | 0.95 | 0.09 | 1218764.29 | 4.07 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 8.06 | 2.19 | 0.13 | 827924.62 | 9.26 | skipped_fast |
| HBARUSDT | IDLE | 1.82 | 3.62 | 0.2 | 0.03 | 920994.64 | 1.04 | skipped_fast |
| WUSDT | IDLE | 2.17 | 4.31 | 0.19 | 0.05 | 396924.24 | 8.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.47 | 21.84 | 15.48 | 0.05 | 118663.22 | 98.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.73 | 2.26 | 0.06 | 248169.06 | 13.73 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 5.1 | 1.34 | 0.13 | 578941.22 | 4.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 4.27 | 0.04 | 0.04 | 152350.18 | 14.1 | skipped_fast |
| KITEUSDT | IDLE | 1.79 | 3.49 | 0.56 | -0.0 | 79677.16 | 10.53 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 4.42 | 0.87 | 0.06 | 114549.4 | 9.09 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.68 | 3.63 | 0.04 | 230135.85 | 16.93 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 3.08 | 0.49 | 0.09 | 136393.99 | 13.73 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.77 | 0.9 | 0.0 | 114935.86 | 12.12 | skipped_fast |
| RWAINCUSDT | IDLE | 0.49 | 1.85 | 0.51 | -0.07 | 17423.9 | 70.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.24 | 2.46 | 0.16 | 0.03 | 3384.99 | 21.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.37 | 0.81 | 0.02 | 41294.17 | 10.18 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.33 | 0.88 | -0.01 | 54912.8 | 29.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
