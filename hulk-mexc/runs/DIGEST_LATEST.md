# Hulk DIGEST — 2026-10-12T22:49:39Z

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
| PYTHUSDT | IDLE | 2.12 | 8.11 | 5.8 | 0.05 | 3407738.27 | 2.42 | tvl≈187,390,750 |
| WUSDT | IDLE | 1.06 | 15.92 | 13.32 | -0.13 | 15336789.59 | 6.82 | tvl≈1,726,512,433 |
| XRPUSDT | IDLE | 1.13 | 2.08 | 1.24 | -0.04 | 30067851.25 | 2.21 | n/a |
| ETHUSDT | IDLE | 1.06 | 1.87 | 1.71 | -0.02 | 221417993.24 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.55 | 0.99 | 0.68 | -0.01 | 298457970.98 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.71 | 3.36 | 1.41 | -0.04 | 822988.63 | 1.31 | n/a |
| EDELUSDT | IDLE | 1.55 | 6.93 | 2.14 | -0.1 | 289504.79 | 11.82 | no_map |
| RIZEUSDT | IDLE | 2.22 | 14.0 | 8.23 | -0.06 | 73063.51 | 88.7 | no_map |
| HBARUSDT | IDLE | 1.39 | 2.65 | 1.86 | -0.06 | 600250.93 | 6.78 | empty_tvl |
| CCUSDT | IDLE | 0.85 | 1.5 | 1.31 | -0.04 | 394674.39 | 8.27 | no_map |
| KITEUSDT | IDLE | 2.21 | 4.06 | 2.46 | -0.02 | 65559.54 | 10.34 | no_map |
| REDUSDT | IDLE | 0.67 | 4.24 | 2.92 | 0.02 | 266613.96 | 7.1 | tvl≈3,971,098 |
| ZBCNUSDT | IDLE | 0.89 | 1.65 | 0.9 | 0.02 | 266426.29 | 9.07 | n/a |
| BIOUSDT | IDLE | 1.52 | 3.0 | 2.42 | -0.07 | 75135.31 | 7.19 | n/a |
| CHIPUSDT | IDLE | 0.77 | 3.53 | 2.74 | -0.15 | 160837.2 | 13.73 | no_map |
| RWAINCUSDT | IDLE | 0.77 | 2.2 | 0.15 | 0.01 | 32262.5 | 4.9 | no_map |
| FLUIDUSDT | IDLE | 1.95 | 3.58 | 2.17 | -0.01 | 15558.91 | 21.62 | tvl≈2,382,838,546 |
| TELUSDT | IDLE | 1.5 | 2.79 | 1.41 | 0.02 | 120155.37 | 22.94 | no_map |
| MNSRYUSDT | IDLE | 0.5 | 0.92 | 0.59 | -0.01 | 41253.36 | 33.03 | no_map |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.15 | 0.0 | 52290.7 | 15.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
