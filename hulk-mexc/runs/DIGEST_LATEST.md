# Hulk DIGEST — 2026-09-11T03:16:39Z

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
| XRPUSDT | IDLE | 1.04 | 1.93 | 0.97 | -0.04 | 40932250.65 | 1.49 | n/a |
| ETHUSDT | IDLE | 0.62 | 1.16 | 0.57 | -0.01 | 426940107.23 | 0.57 | no_map |
| BTCUSDT | IDLE | 0.5 | 0.93 | 0.42 | -0.02 | 536708614.26 | 0.09 | no_map |
| RIZEUSDT | IDLE | 0.97 | 51.94 | 24.65 | -0.46 | 146852.45 | 71.56 | no_map |
| CHIPUSDT | IDLE | 3.3 | 7.69 | 3.75 | -0.03 | 99486.29 | 14.75 | no_map |
| PYTHUSDT | IDLE | 1.66 | 2.97 | 2.28 | -0.02 | 415887.61 | 1.96 | tvl≈116,258,822 |
| CCUSDT | IDLE | 1.23 | 2.31 | 1.62 | -0.06 | 451092.66 | 11.24 | no_map |
| EDELUSDT | IDLE | 1.48 | 6.03 | 4.09 | -0.04 | 206988.45 | 37.11 | no_map |
| ZBCNUSDT | IDLE | 0.96 | 1.81 | 0.79 | -0.02 | 206644.68 | 23.99 | n/a |
| WUSDT | IDLE | 1.02 | 1.89 | 0.96 | -0.03 | 163770.14 | 10.48 | tvl≈1,480,711,690 |
| BIOUSDT | IDLE | 0.98 | 1.87 | 0.64 | -0.03 | 76999.4 | 12.05 | n/a |
| KITEUSDT | IDLE | 0.9 | 1.72 | 0.58 | -0.03 | 57774.88 | 10.11 | no_map |
| REDUSDT | IDLE | 0.84 | 1.51 | 1.1 | -0.05 | 59893.23 | 10.77 | tvl≈2,196,395 |
| TELUSDT | IDLE | 1.73 | 3.03 | 2.88 | -0.03 | 88239.23 | 5.71 | no_map |
| RWAINCUSDT | IDLE | 0.59 | 1.18 | 0.0 | 0.03 | 4182.63 | 5.54 | no_map |
| HBARUSDT | IDLE | 0.79 | 1.45 | 0.84 | -0.02 | 179700.12 | 1.33 | empty_tvl |
| FLUIDUSDT | IDLE | 1.69 | 3.38 | 0.0 | -0.02 | 1894.98 | 22.69 | tvl≈2,645,931,768 |
| QNTUSDT | IDLE | 0.94 | 1.69 | 1.24 | -0.04 | 35584.08 | 7.77 | n/a |
| RWAUSDT | IDLE | 0.57 | 1.07 | 0.53 | -0.02 | 50388.19 | 22.86 | no_map |
| MNSRYUSDT | IDLE | 0.32 | 0.56 | 0.52 | -0.01 | 35352.24 | 18.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
