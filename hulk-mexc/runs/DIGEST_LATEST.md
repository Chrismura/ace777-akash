# Hulk DIGEST — 2026-09-11T11:19:47Z

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
| XRPUSDT | IDLE | 1.68 | 2.98 | 2.51 | -0.04 | 39661578.08 | 1.51 | n/a |
| ETHUSDT | IDLE | 0.74 | 1.32 | 1.13 | -0.0 | 463611939.3 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.53 | 0.94 | 0.84 | -0.01 | 522263058.26 | 0.0 | no_map |
| CCUSDT | IDLE | 2.88 | 5.15 | 4.05 | -0.06 | 435736.03 | 11.5 | no_map |
| PYTHUSDT | IDLE | 2.26 | 4.04 | 3.23 | -0.03 | 360613.58 | 1.99 | tvl≈115,923,371 |
| RIZEUSDT | IDLE | 1.14 | 26.96 | 13.97 | -0.16 | 134750.08 | 94.59 | no_map |
| WUSDT | IDLE | 2.07 | 3.67 | 3.08 | -0.02 | 133709.33 | 11.73 | tvl≈1,486,793,382 |
| REDUSDT | IDLE | 2.09 | 3.68 | 3.3 | -0.04 | 59124.53 | 21.01 | tvl≈2,196,779 |
| BIOUSDT | IDLE | 1.78 | 3.16 | 2.67 | -0.05 | 79685.27 | 8.18 | n/a |
| CHIPUSDT | IDLE | 1.2 | 3.62 | 1.93 | -0.06 | 127110.42 | 15.46 | no_map |
| KITEUSDT | IDLE | 1.35 | 2.36 | 2.3 | -0.02 | 57727.04 | 12.18 | no_map |
| EDELUSDT | IDLE | 0.66 | 2.87 | 2.51 | -0.07 | 197895.64 | 19.08 | no_map |
| RWAINCUSDT | IDLE | 1.57 | 3.14 | 0.0 | 0.04 | 3892.07 | 5.48 | no_map |
| ZBCNUSDT | IDLE | 0.76 | 1.38 | 1.0 | -0.03 | 200468.43 | 19.92 | n/a |
| HBARUSDT | IDLE | 1.69 | 2.97 | 2.69 | -0.04 | 194438.12 | 1.36 | empty_tvl |
| FLUIDUSDT | IDLE | 1.8 | 3.15 | 3.05 | -0.03 | 2404.99 | 22.19 | tvl≈2,658,749,875 |
| QNTUSDT | IDLE | 0.99 | 1.73 | 1.7 | -0.03 | 37044.81 | 1.56 | n/a |
| TELUSDT | IDLE | 0.91 | 1.63 | 1.32 | -0.04 | 99321.96 | 34.88 | no_map |
| MNSRYUSDT | IDLE | 0.33 | 0.6 | 0.43 | -0.01 | 37410.6 | 9.79 | no_map |
| RWAUSDT | IDLE | 0.24 | 0.46 | 0.08 | -0.02 | 49447.51 | 22.79 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
