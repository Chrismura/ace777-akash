# Hulk DIGEST — 2026-10-11T15:22:32Z

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
| XRPUSDT | IDLE | 0.47 | 0.93 | 0.07 | -0.01 | 10002867.17 | 2.14 | n/a |
| ETHUSDT | IDLE | 0.23 | 0.46 | 0.04 | 0.0 | 168303309.48 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.12 | 0.0 | 121460285.94 | 0.0 | no_map |
| WUSDT | IDLE | 1.53 | 2.89 | 1.07 | -0.04 | 938599.79 | 6.28 | tvl≈1,647,121,629 |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 31.62 | 15.89 | 0.06 | 54156.34 | 21.15 | tvl≈2,413,784,266 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 11.9 | 8.78 | -0.02 | 28670.6 | 4.96 | no_map |
| QNTUSDT | IDLE | 1.35 | 2.41 | 2.0 | -0.03 | 985840.05 | 4.98 | n/a |
| PYTHUSDT | IDLE | 1.01 | 1.87 | 1.02 | -0.02 | 725965.58 | 2.61 | tvl≈172,259,825 |
| CCUSDT | IDLE | 2.42 | 4.83 | 0.13 | 0.04 | 308250.46 | 9.58 | no_map |
| CHIPUSDT | IDLE | 1.04 | 10.03 | 1.16 | 0.35 | 415741.32 | 18.63 | no_map |
| TELUSDT | IDLE | 3.9 | 7.16 | 4.2 | -0.04 | 147447.02 | 34.54 | no_map |
| EDELUSDT | IDLE | 1.26 | 2.3 | 1.43 | 0.01 | 389886.23 | 7.76 | no_map |
| RIZEUSDT | IDLE | 2.39 | 6.54 | 2.2 | -0.06 | 35624.91 | 61.51 | no_map |
| BIOUSDT | IDLE | 1.97 | 3.78 | 1.09 | 0.04 | 74337.69 | 16.75 | n/a |
| ZBCNUSDT | IDLE | 1.37 | 2.54 | 1.32 | -0.01 | 161206.18 | 13.19 | n/a |
| REDUSDT | IDLE | 1.49 | 2.87 | 0.72 | 0.0 | 58131.15 | 8.62 | tvl≈3,713,830 |
| KITEUSDT | IDLE | 0.98 | 1.88 | 0.49 | -0.03 | 70818.74 | 10.24 | no_map |
| HBARUSDT | IDLE | 1.12 | 2.22 | 0.15 | -0.0 | 249309.28 | 6.48 | empty_tvl |
| RWAUSDT | IDLE | 0.85 | 1.67 | 0.16 | 0.01 | 51580.44 | 15.64 | no_map |
| MNSRYUSDT | IDLE | 0.36 | 0.73 | 0.0 | -0.01 | 30832.71 | 28.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
