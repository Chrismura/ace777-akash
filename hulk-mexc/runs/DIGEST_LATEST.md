# Hulk DIGEST — 2026-09-30T22:50:49Z

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
| QNTUSDT | IDLE | 2.01 | 11.96 | 7.01 | 0.09 | 10591544.37 | 9.83 | n/a |
| XRPUSDT | IDLE | 1.08 | 1.95 | 1.43 | -0.0 | 53701717.25 | 2.68 | n/a |
| BTCUSDT | IDLE | 0.61 | 1.1 | 0.78 | 0.0 | 604915018.19 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.57 | 1.1 | 0.29 | 0.0 | 376172394.23 | 0.04 | no_map |
| HBARUSDT | IDLE | 2.68 | 5.29 | 3.79 | 0.03 | 1465061.59 | 9.46 | empty_tvl |
| WUSDT | IDLE | 2.13 | 4.13 | 0.82 | -0.02 | 847911.66 | 9.71 | tvl≈1,805,813,711 |
| CCUSDT | IDLE | 1.64 | 3.26 | 0.2 | 0.02 | 944306.08 | 3.96 | no_map |
| PYTHUSDT | IDLE | 1.74 | 3.31 | 1.17 | -0.02 | 611925.35 | 7.75 | tvl≈173,837,132 |
| ZBCNUSDT | IDLE | 1.19 | 5.38 | 2.06 | 0.06 | 454887.97 | 27.87 | n/a |
| BIOUSDT | IDLE | 2.62 | 4.8 | 2.95 | 0.0 | 91854.05 | 9.7 | n/a |
| CHIPUSDT | IDLE | 2.24 | 4.86 | 2.75 | -0.02 | 69501.81 | 20.72 | no_map |
| EDELUSDT | IDLE | 0.99 | 10.47 | 1.44 | 0.21 | 173227.54 | 24.98 | no_map |
| RWAINCUSDT | IDLE | 1.79 | 3.58 | 3.37 | -0.05 | 10590.61 | 4.36 | no_map |
| KITEUSDT | IDLE | 1.56 | 3.71 | 1.85 | 0.06 | 78072.14 | 9.19 | no_map |
| REDUSDT | IDLE | 1.14 | 4.58 | 3.76 | 0.09 | 76642.43 | 7.96 | tvl≈4,448,230 |
| RIZEUSDT | IDLE | 1.31 | 2.91 | 2.31 | 0.05 | 42689.38 | 55.5 | no_map |
| TELUSDT | IDLE | 1.2 | 3.32 | 2.14 | 0.04 | 248478.41 | 16.85 | no_map |
| FLUIDUSDT | IDLE | 1.4 | 2.45 | 2.37 | -0.0 | 1234.51 | 21.09 | tvl≈2,580,634,308 |
| MNSRYUSDT | IDLE | 0.51 | 0.95 | 0.45 | 0.01 | 38974.48 | 5.16 | no_map |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | -0.0 | 53695.29 | 22.0 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
