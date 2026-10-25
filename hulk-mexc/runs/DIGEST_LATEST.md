# Hulk DIGEST — 2026-10-25T06:59:04Z

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
| XRPUSDT | IDLE | 0.92 | 1.62 | 1.5 | 0.01 | 26893484.62 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.84 | 1.49 | 1.3 | -0.02 | 127265822.77 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.41 | 0.73 | 0.64 | -0.0 | 224773470.83 | 0.0 | no_map |
| WUSDT | IDLE | 1.18 | 2.16 | 1.35 | -0.05 | 831613.24 | 17.27 | tvl≈1,507,919,191 |
| PYTHUSDT | IDLE | 1.34 | 2.41 | 1.81 | -0.01 | 501058.53 | 1.42 | tvl≈157,798,291 |
| EDELUSDT | IDLE | 0.87 | 2.01 | 1.84 | -0.07 | 597463.25 | 10.02 | no_map |
| KITEUSDT | IDLE | 2.42 | 4.24 | 4.05 | -0.06 | 59480.02 | 11.61 | no_map |
| CCUSDT | IDLE | 1.06 | 1.87 | 1.62 | -0.03 | 209438.24 | 8.98 | no_map |
| QNTUSDT | IDLE | 1.55 | 2.9 | 1.35 | -0.0 | 372835.88 | 2.73 | n/a |
| ZBCNUSDT | IDLE | 0.74 | 1.65 | 1.17 | 0.01 | 235156.56 | 12.54 | n/a |
| BIOUSDT | IDLE | 1.39 | 2.45 | 2.26 | -0.04 | 64863.44 | 4.45 | n/a |
| CHIPUSDT | IDLE | 1.18 | 3.36 | 2.81 | 0.04 | 90399.16 | 15.81 | no_map |
| REDUSDT | IDLE | 1.18 | 2.94 | 1.61 | -0.02 | 81358.67 | 15.55 | tvl≈3,765,526 |
| RWAINCUSDT | IDLE | 1.01 | 1.86 | 1.13 | -0.01 | 57635.91 | 5.44 | no_map |
| WAXLUSDT | IDLE | 2.24 | 4.04 | 3.5 | -0.01 | 54748.22 | 43.52 | no_map |
| HBARUSDT | IDLE | 1.1 | 1.98 | 1.53 | -0.0 | 207857.57 | 14.21 | empty_tvl |
| LAUSDT | IDLE | 0.95 | 5.32 | 3.48 | -0.12 | 97438.86 | 25.23 | no_map |
| RIZEUSDT | IDLE | 0.41 | 1.16 | 0.3 | -0.04 | 41520.52 | 62.38 | no_map |
| IOTAUSDT | IDLE | 1.13 | 1.99 | 1.84 | -0.02 | 66461.41 | 32.35 | no_map |
| RWAUSDT | IDLE | 0.82 | 1.52 | 0.79 | -0.0 | 52697.18 | 47.51 | no_map |
| FLUIDUSDT | IDLE | 0.74 | 1.28 | 1.27 | -0.04 | 9992.03 | 21.4 | tvl≈2,192,910,804 |
| MNSRYUSDT | IDLE | 0.4 | 0.76 | 0.23 | -0.01 | 37576.71 | 77.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
