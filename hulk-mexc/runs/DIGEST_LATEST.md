# Hulk DIGEST — 2026-09-13T23:41:30Z

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
| XRPUSDT | IDLE | 1.17 | 2.12 | 1.53 | -0.02 | 17761879.05 | 2.98 | n/a |
| ETHUSDT | IDLE | 1.04 | 1.84 | 1.62 | -0.02 | 273281771.63 | 0.16 | no_map |
| BTCUSDT | IDLE | 0.57 | 1.02 | 0.81 | -0.01 | 275595582.16 | 0.0 | no_map |
| WUSDT | IDLE | 3.28 | 5.83 | 4.84 | -0.01 | 220593.56 | 1.02 | tvl≈1,487,342,869 |
| PYTHUSDT | IDLE | 2.29 | 4.44 | 2.63 | 0.03 | 449247.1 | 1.78 | tvl≈129,171,771 |
| RWAINCUSDT | IDLE | 4.19 | 7.78 | 4.01 | 0.0 | 9507.95 | 27.43 | no_map |
| CHIPUSDT | IDLE | 1.98 | 7.68 | 7.11 | -0.14 | 96421.06 | 12.19 | no_map |
| EDELUSDT | IDLE | 1.7 | 5.84 | 1.47 | 0.11 | 199986.39 | 14.93 | no_map |
| BIOUSDT | IDLE | 2.25 | 4.08 | 2.76 | -0.02 | 68436.49 | 7.99 | n/a |
| CCUSDT | IDLE | 1.2 | 2.17 | 1.56 | -0.03 | 316699.75 | 7.38 | no_map |
| ZBCNUSDT | IDLE | 1.76 | 3.32 | 1.4 | 0.01 | 197358.22 | 16.83 | n/a |
| HBARUSDT | IDLE | 2.05 | 3.62 | 3.21 | 0.0 | 246468.78 | 1.33 | empty_tvl |
| REDUSDT | IDLE | 1.55 | 2.74 | 2.34 | -0.01 | 63682.44 | 10.1 | tvl≈2,364,635 |
| KITEUSDT | IDLE | 1.48 | 2.76 | 1.4 | -0.01 | 60248.4 | 10.33 | no_map |
| QNTUSDT | IDLE | 2.43 | 4.29 | 3.86 | -0.01 | 37854.16 | 6.35 | n/a |
| RIZEUSDT | IDLE | 0.76 | 11.14 | 5.82 | -0.05 | 65195.33 | 71.97 | no_map |
| TELUSDT | IDLE | 1.72 | 3.08 | 2.43 | -0.05 | 80774.25 | 25.54 | no_map |
| FLUIDUSDT | IDLE | 1.15 | 2.0 | 1.96 | -0.01 | 1325.28 | 22.21 | tvl≈2,665,467,255 |
| RWAUSDT | IDLE | 0.33 | 0.6 | 0.44 | 0.0 | 54674.02 | 14.86 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.47 | 0.37 | -0.0 | 30379.52 | 23.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
