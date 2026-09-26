# Hulk DIGEST — 2026-09-26T16:01:11Z

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
| XRPUSDT | IDLE | 0.57 | 1.12 | 0.1 | -0.02 | 45847868.89 | 2.58 | n/a |
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.11 | 0.0 | 141582174.93 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.2 | 0.4 | 0.04 | 0.01 | 358983096.26 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.72 | 15.78 | 3.02 | 0.22 | 1211600.07 | 9.46 | n/a |
| PYTHUSDT | IDLE | 1.65 | 4.56 | 1.81 | 0.07 | 1080426.94 | 6.42 | tvl≈176,197,476 |
| CCUSDT | IDLE | 1.71 | 5.28 | 2.24 | 0.11 | 953362.19 | 10.19 | no_map |
| CHIPUSDT | IDLE | 3.49 | 7.71 | 0.54 | 0.06 | 111181.55 | 13.59 | no_map |
| WUSDT | IDLE | 1.6 | 3.23 | 1.59 | 0.07 | 448519.72 | 10.17 | tvl≈1,861,814,996 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 10.66 | 8.51 | -0.05 | 7697.56 | 84.7 | no_map |
| EDELUSDT | IDLE | 2.29 | 4.13 | 3.04 | 0.01 | 162381.56 | 6.59 | no_map |
| KITEUSDT | IDLE | 2.08 | 4.91 | 1.01 | 0.07 | 76066.96 | 10.66 | no_map |
| HBARUSDT | IDLE | 1.21 | 2.42 | 0.0 | 0.02 | 572609.03 | 2.1 | empty_tvl |
| ZBCNUSDT | IDLE | 1.39 | 2.74 | 0.26 | -0.01 | 233681.15 | 13.76 | n/a |
| BIOUSDT | IDLE | 1.62 | 3.04 | 1.36 | 0.02 | 105499.17 | 3.05 | n/a |
| REDUSDT | IDLE | 0.83 | 1.56 | 0.65 | -0.02 | 58123.94 | 6.51 | tvl≈3,085,363 |
| RWAUSDT | IDLE | 1.81 | 3.54 | 0.5 | 0.02 | 55489.72 | 7.16 | no_map |
| RIZEUSDT | IDLE | 0.53 | 2.36 | 0.86 | -0.1 | 42165.68 | 52.01 | no_map |
| TELUSDT | IDLE | 1.15 | 2.15 | 0.99 | -0.03 | 125095.26 | 43.82 | no_map |
| FLUIDUSDT | IDLE | 0.88 | 1.72 | 0.28 | 0.03 | 770.46 | 21.9 | tvl≈2,582,934,248 |
| MNSRYUSDT | IDLE | 0.27 | 0.52 | 0.13 | -0.0 | 39637.11 | 31.88 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
