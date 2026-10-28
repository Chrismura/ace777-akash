# Hulk DIGEST — 2026-10-28T20:42:39Z

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
| ETHUSDT | IDLE | 1.5 | 2.74 | 1.67 | 0.0 | 198379315.39 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.45 | 2.71 | 1.22 | 0.01 | 23341628.33 | 0.75 | n/a |
| BTCUSDT | IDLE | 0.91 | 1.7 | 0.84 | 0.01 | 321728851.97 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.95 | 5.45 | 3.0 | -0.01 | 423676.89 | 4.16 | tvl≈157,338,990 |
| CCUSDT | IDLE | 1.86 | 4.22 | 1.92 | 0.02 | 430183.42 | 9.97 | no_map |
| WUSDT | IDLE | 1.83 | 3.26 | 2.63 | -0.01 | 417948.07 | 18.93 | tvl≈1,518,887,873 |
| QNTUSDT | IDLE | 2.57 | 4.89 | 1.69 | -0.0 | 410552.0 | 3.01 | n/a |
| HBARUSDT | IDLE | 1.74 | 3.13 | 2.32 | -0.01 | 579081.95 | 7.97 | empty_tvl |
| CHIPUSDT | IDLE | 1.61 | 7.31 | 3.48 | -0.09 | 237796.32 | 14.11 | no_map |
| BIOUSDT | IDLE | 2.37 | 4.39 | 2.32 | 0.01 | 88757.57 | 8.78 | n/a |
| RWAINCUSDT | IDLE | 2.11 | 5.32 | 4.92 | -0.05 | 34779.42 | 20.68 | no_map |
| ZBCNUSDT | IDLE | 1.26 | 2.42 | 0.73 | -0.03 | 283937.05 | 28.87 | n/a |
| EDELUSDT | IDLE | 1.47 | 2.56 | 2.47 | -0.01 | 185823.19 | 28.05 | no_map |
| KITEUSDT | IDLE | 1.65 | 3.01 | 1.92 | -0.02 | 59892.76 | 11.23 | no_map |
| RIZEUSDT | IDLE | 1.96 | 3.51 | 2.78 | 0.0 | 39573.14 | 65.12 | no_map |
| REDUSDT | IDLE | 1.45 | 2.65 | 1.71 | -0.03 | 53794.8 | 15.18 | tvl≈3,762,710 |
| IOTAUSDT | IDLE | 2.65 | 4.9 | 2.6 | 0.0 | 77302.03 | 28.61 | no_map |
| LAUSDT | IDLE | 2.02 | 3.83 | 1.4 | -0.03 | 56980.63 | 37.54 | no_map |
| WAXLUSDT | IDLE | 2.05 | 3.82 | 1.91 | -0.01 | 55047.17 | 47.2 | no_map |
| RWAUSDT | IDLE | 0.76 | 1.37 | 1.03 | -0.0 | 55472.34 | 8.01 | no_map |
| FLUIDUSDT | IDLE | 0.96 | 3.23 | 0.0 | 0.01 | 6418.19 | 21.44 | tvl≈2,229,648,766 |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.17 | 0.01 | 35493.93 | 40.86 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
