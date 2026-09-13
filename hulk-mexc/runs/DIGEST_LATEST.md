# Hulk DIGEST — 2026-09-13T18:34:01Z

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
| ETHUSDT | IDLE | 1.04 | 2.05 | 0.23 | -0.01 | 254508210.35 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.97 | 1.92 | 0.1 | -0.01 | 14568010.2 | 2.21 | n/a |
| BTCUSDT | IDLE | 0.54 | 1.07 | 0.06 | 0.0 | 291206211.93 | 0.0 | no_map |
| RIZEUSDT | IDLE | 2.47 | 35.81 | 21.29 | -0.11 | 80052.5 | 16.47 | no_map |
| PYTHUSDT | IDLE | 2.77 | 5.33 | 1.34 | 0.03 | 453961.26 | 1.76 | tvl≈125,127,118 |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 9.26 | 1.35 | 0.11 | 201641.3 | 30.37 | no_map |
| WUSDT | IDLE | 1.87 | 3.69 | 0.31 | 0.02 | 264049.75 | 7.85 | tvl≈1,479,548,087 |
| CHIPUSDT | IDLE | 2.17 | 6.14 | 5.35 | -0.11 | 85015.97 | 13.84 | no_map |
| ZBCNUSDT | IDLE | 1.5 | 2.96 | 0.24 | 0.01 | 199067.49 | 21.69 | n/a |
| CCUSDT | IDLE | 0.57 | 1.13 | 0.02 | -0.02 | 296169.63 | 9.39 | no_map |
| REDUSDT | IDLE | 1.56 | 2.79 | 2.17 | -0.0 | 61170.08 | 16.83 | tvl≈2,402,466 |
| BIOUSDT | IDLE | 1.18 | 2.3 | 0.39 | 0.0 | 68617.67 | 3.9 | n/a |
| KITEUSDT | IDLE | 1.24 | 2.22 | 1.76 | 0.01 | 63779.51 | 14.95 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.42 | 1.23 | -0.03 | 6825.53 | 5.65 | no_map |
| HBARUSDT | IDLE | 1.09 | 2.14 | 0.25 | 0.03 | 204273.08 | 1.31 | empty_tvl |
| QNTUSDT | IDLE | 1.41 | 2.77 | 0.38 | 0.01 | 35879.79 | 6.12 | n/a |
| TELUSDT | IDLE | 0.74 | 1.46 | 0.19 | -0.04 | 80273.25 | 37.66 | no_map |
| RWAUSDT | IDLE | 0.64 | 1.27 | 0.0 | 0.0 | 54950.82 | 22.23 | no_map |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.01 | 1479.56 | 21.95 | tvl≈2,662,766,843 |
| MNSRYUSDT | IDLE | 0.13 | 0.25 | 0.07 | -0.0 | 32298.2 | 13.9 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
