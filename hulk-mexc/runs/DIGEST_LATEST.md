# Hulk DIGEST — 2026-09-05T16:27:03Z

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
| XRPUSDT | IDLE | 0.68 | 1.28 | 0.49 | 0.01 | 21467565.45 | 1.42 | n/a |
| ETHUSDT | IDLE | 0.24 | 0.48 | 0.01 | 0.0 | 170943279.23 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.0 | 0.0 | 338265685.53 | 0.0 | no_map |
| CHIPUSDT | IDLE | 2.04 | 7.32 | 0.0 | 0.09 | 425487.39 | 3.37 | no_map |
| KITEUSDT | IDLE | 2.68 | 6.21 | 4.87 | -0.03 | 60811.46 | 12.67 | no_map |
| PYTHUSDT | IDLE | 1.6 | 2.99 | 1.39 | 0.02 | 329531.65 | 1.83 | tvl≈123,328,192 |
| CCUSDT | IDLE | 1.35 | 2.71 | 0.0 | 0.04 | 281265.72 | 8.98 | no_map |
| RIZEUSDT | IDLE | 1.23 | 11.89 | 3.66 | 0.12 | 153610.09 | 33.0 | no_map |
| WUSDT | IDLE | 1.43 | 2.58 | 1.87 | 0.03 | 158356.97 | 10.09 | tvl≈1,553,862,506 |
| ZBCNUSDT | IDLE | 1.23 | 2.18 | 1.84 | -0.0 | 183580.28 | 7.96 | n/a |
| BIOUSDT | IDLE | 1.47 | 2.86 | 0.5 | 0.04 | 78546.89 | 3.58 | n/a |
| RWAINCUSDT | IDLE | 1.78 | 3.17 | 2.6 | -0.02 | 7443.22 | 16.19 | no_map |
| REDUSDT | IDLE | 1.38 | 2.48 | 1.91 | 0.02 | 62092.28 | 10.4 | tvl≈2,313,270 |
| EDELUSDT | IDLE | 0.27 | 4.89 | 1.96 | -0.01 | 183681.67 | 28.59 | no_map |
| HBARUSDT | IDLE | 1.01 | 1.81 | 1.46 | 0.04 | 310468.85 | 1.25 | empty_tvl |
| RWAUSDT | IDLE | 1.22 | 2.37 | 0.49 | 0.03 | 51653.05 | 28.19 | no_map |
| TELUSDT | IDLE | 1.11 | 2.14 | 0.52 | -0.01 | 69866.65 | 46.76 | no_map |
| QNTUSDT | IDLE | 0.59 | 1.15 | 0.22 | -0.0 | 39869.02 | 3.11 | n/a |
| FLUIDUSDT | IDLE | 0.81 | 1.43 | 1.31 | 0.01 | 867.92 | 21.82 | tvl≈2,640,471,476 |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.08 | 0.0 | 38258.91 | 27.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
