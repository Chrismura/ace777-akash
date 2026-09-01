# Hulk DIGEST — 2026-09-01T23:24:03Z

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
| XRPUSDT | IDLE | 1.1 | 1.99 | 1.36 | -0.02 | 35195132.44 | 2.23 | n/a |
| ETHUSDT | IDLE | 0.9 | 1.74 | 0.42 | -0.02 | 341595702.42 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.74 | 1.44 | 0.29 | -0.02 | 527942100.8 | 0.0 | no_map |
| CHIPUSDT | IDLE | 2.25 | 11.2 | 3.59 | 0.14 | 737270.97 | 2.26 | no_map |
| PYTHUSDT | IDLE | 2.91 | 5.74 | 0.5 | 0.05 | 693794.71 | 1.93 | tvl≈113,597,849 |
| WUSDT | IDLE | 2.27 | 4.18 | 3.52 | 0.04 | 409598.34 | 1.04 | tvl≈1,509,553,891 |
| ZBCNUSDT | IDLE | 2.31 | 4.07 | 3.6 | -0.01 | 205658.19 | 15.36 | n/a |
| REDUSDT | IDLE | 1.88 | 5.85 | 2.89 | 0.1 | 117451.91 | 9.58 | tvl≈2,090,812 |
| CCUSDT | IDLE | 0.87 | 1.94 | 1.3 | -0.07 | 326765.42 | 8.81 | no_map |
| RIZEUSDT | IDLE | 1.98 | 4.22 | 1.98 | -0.06 | 40834.69 | 18.08 | no_map |
| KITEUSDT | IDLE | 1.44 | 2.78 | 0.73 | 0.04 | 68161.4 | 10.57 | no_map |
| BIOUSDT | IDLE | 1.06 | 1.9 | 1.44 | -0.05 | 69689.73 | 3.94 | n/a |
| FLUIDUSDT | IDLE | 2.56 | 4.47 | 4.28 | -0.03 | 229.45 | 14.95 | tvl≈2,574,882,028 |
| RWAINCUSDT | IDLE | 1.41 | 2.61 | 1.45 | -0.02 | 5822.68 | 29.4 | no_map |
| TELUSDT | IDLE | 2.16 | 3.91 | 2.77 | -0.05 | 94582.21 | 48.43 | no_map |
| EDELUSDT | IDLE | 0.7 | 5.41 | 4.6 | -0.09 | 144077.52 | 119.76 | no_map |
| HBARUSDT | IDLE | 0.87 | 1.58 | 1.07 | 0.0 | 249203.73 | 1.35 | empty_tvl |
| QNTUSDT | IDLE | 1.52 | 2.91 | 0.93 | 0.05 | 46104.26 | 7.83 | n/a |
| MNSRYUSDT | IDLE | 0.79 | 1.46 | 0.83 | -0.02 | 34401.67 | 31.56 | no_map |
| RWAUSDT | IDLE | 0.4 | 0.93 | 0.54 | -0.03 | 58809.96 | 7.71 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
