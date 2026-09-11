# Hulk DIGEST — 2026-09-11T04:16:01Z

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
| XRPUSDT | IDLE | 0.65 | 1.28 | 0.13 | -0.03 | 40710051.14 | 1.49 | n/a |
| ETHUSDT | IDLE | 0.58 | 1.09 | 0.42 | -0.01 | 433496526.62 | 0.37 | no_map |
| BTCUSDT | IDLE | 0.33 | 0.66 | 0.03 | -0.02 | 557684864.3 | 0.01 | no_map |
| PYTHUSDT | IDLE | 1.29 | 2.35 | 1.56 | -0.02 | 413723.33 | 1.96 | tvl≈116,258,822 |
| CCUSDT | IDLE | 0.91 | 1.83 | 0.4 | -0.05 | 459446.27 | 8.11 | no_map |
| CHIPUSDT | IDLE | 2.29 | 5.36 | 2.5 | -0.04 | 99317.26 | 21.16 | no_map |
| EDELUSDT | IDLE | 1.06 | 4.15 | 3.98 | -0.07 | 207229.3 | 56.55 | no_map |
| ZBCNUSDT | IDLE | 0.96 | 1.81 | 0.75 | -0.05 | 201680.79 | 19.53 | n/a |
| WUSDT | IDLE | 1.05 | 2.09 | 0.02 | -0.02 | 158451.47 | 12.42 | tvl≈1,480,711,690 |
| BIOUSDT | IDLE | 0.92 | 1.83 | 0.08 | -0.01 | 76256.91 | 3.99 | n/a |
| RIZEUSDT | IDLE | 0.72 | 38.0 | 21.02 | -0.45 | 155833.32 | 536.4 | no_map |
| REDUSDT | IDLE | 0.88 | 1.7 | 0.37 | -0.04 | 60213.68 | 18.05 | tvl≈2,196,395 |
| KITEUSDT | IDLE | 0.79 | 1.5 | 0.55 | -0.03 | 57207.06 | 13.81 | no_map |
| TELUSDT | IDLE | 1.64 | 2.88 | 2.69 | -0.03 | 88537.99 | 34.54 | no_map |
| RWAINCUSDT | IDLE | 1.02 | 1.85 | 1.32 | 0.02 | 4139.9 | 89.79 | no_map |
| FLUIDUSDT | IDLE | 1.69 | 3.38 | 0.0 | -0.02 | 1894.98 | 21.61 | tvl≈2,645,331,431 |
| HBARUSDT | IDLE | 0.48 | 0.96 | 0.04 | -0.02 | 175655.78 | 1.33 | empty_tvl |
| QNTUSDT | IDLE | 0.7 | 1.33 | 0.51 | -0.04 | 35093.69 | 6.19 | n/a |
| RWAUSDT | IDLE | 0.57 | 1.07 | 0.53 | -0.02 | 50072.52 | 15.23 | no_map |
| MNSRYUSDT | IDLE | 0.32 | 0.56 | 0.53 | -0.02 | 34824.34 | 16.79 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
