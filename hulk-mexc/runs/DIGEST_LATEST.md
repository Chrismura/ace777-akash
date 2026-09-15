# Hulk DIGEST — 2026-09-15T17:46:13Z

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
| XRPUSDT | IDLE | 3.21 | 6.39 | 3.87 | -0.02 | 81637378.82 | 2.14 | n/a |
| ETHUSDT | IDLE | 1.86 | 4.03 | 2.22 | -0.04 | 505801396.14 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.2 | 2.3 | 0.69 | -0.03 | 587587738.93 | 0.0 | no_map |
| EDELUSDT | IDLE | 1.95 | 32.58 | 1.57 | 0.66 | 475068.42 | 54.61 | no_map |
| ZBCNUSDT | IDLE | 3.74 | 7.83 | 3.12 | 0.0 | 208115.46 | 16.77 | n/a |
| PYTHUSDT | IDLE | 2.21 | 4.28 | 2.11 | -0.05 | 496992.43 | 9.27 | tvl≈120,975,427 |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 10.87 | 5.97 | -0.08 | 97997.71 | 12.98 | no_map |
| CCUSDT | IDLE | 1.89 | 3.41 | 2.49 | -0.04 | 329131.37 | 9.66 | no_map |
| HBARUSDT | IDLE | 2.2 | 4.08 | 2.1 | 0.01 | 456434.9 | 1.28 | empty_tvl |
| KITEUSDT | IDLE | 2.37 | 4.4 | 2.27 | -0.01 | 64152.92 | 10.49 | no_map |
| WUSDT | IDLE | 1.61 | 3.44 | 1.69 | -0.04 | 180594.44 | 13.62 | tvl≈1,433,457,709 |
| BIOUSDT | IDLE | 1.73 | 3.37 | 0.63 | -0.01 | 81111.27 | 11.86 | n/a |
| RWAINCUSDT | IDLE | 2.13 | 3.88 | 2.51 | -0.04 | 8278.0 | 51.71 | no_map |
| REDUSDT | IDLE | 1.02 | 5.38 | 3.23 | -0.03 | 102205.01 | 17.86 | tvl≈2,402,984 |
| RIZEUSDT | IDLE | 1.22 | 10.95 | 8.37 | 0.0 | 53426.52 | 83.45 | no_map |
| TELUSDT | IDLE | 1.27 | 4.37 | 1.27 | -0.03 | 99792.46 | 44.91 | no_map |
| QNTUSDT | IDLE | 1.17 | 2.22 | 0.76 | -0.03 | 50012.52 | 4.78 | n/a |
| FLUIDUSDT | IDLE | 1.46 | 2.63 | 2.02 | -0.06 | 2019.36 | 20.9 | tvl≈2,640,062,984 |
| RWAUSDT | IDLE | 0.74 | 1.35 | 0.89 | -0.01 | 51648.45 | 22.5 | no_map |
| MNSRYUSDT | IDLE | 0.57 | 1.04 | 0.6 | -0.0 | 32407.74 | 39.1 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
