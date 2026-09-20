# Hulk DIGEST — 2026-09-20T13:02:21Z

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
| XRPUSDT | IDLE | 0.65 | 1.2 | 0.7 | -0.04 | 49030064.17 | 1.45 | n/a |
| ETHUSDT | IDLE | 0.39 | 0.75 | 0.2 | -0.02 | 243474728.36 | 0.39 | no_map |
| BTCUSDT | IDLE | 0.26 | 0.51 | 0.08 | -0.01 | 486057168.55 | 0.0 | no_map |
| WUSDT | IDLE | 2.18 | 4.01 | 2.38 | -0.03 | 434605.73 | 8.3 | tvl≈1,573,250,115 |
| PYTHUSDT | IDLE | 1.12 | 2.19 | 0.75 | -0.04 | 679376.53 | 5.15 | tvl≈131,634,513 |
| HBARUSDT | IDLE | 1.66 | 3.24 | 0.58 | 0.02 | 808631.99 | 1.22 | empty_tvl |
| EDELUSDT | IDLE | 3.17 | 9.83 | 3.89 | -0.03 | 66893.16 | 24.36 | no_map |
| REDUSDT | IDLE | 2.6 | 4.96 | 1.63 | 0.01 | 75102.79 | 9.25 | tvl≈2,749,932 |
| CCUSDT | IDLE | 0.79 | 2.03 | 0.35 | -0.06 | 363825.51 | 8.6 | no_map |
| ZBCNUSDT | IDLE | 1.04 | 2.87 | 2.47 | 0.02 | 227034.0 | 32.3 | n/a |
| KITEUSDT | IDLE | 1.48 | 2.68 | 1.8 | -0.03 | 69719.51 | 9.78 | no_map |
| CHIPUSDT | IDLE | 1.4 | 2.71 | 2.0 | -0.06 | 89575.08 | 17.03 | no_map |
| BIOUSDT | IDLE | 1.08 | 2.03 | 0.92 | -0.04 | 81300.26 | 3.72 | n/a |
| RWAINCUSDT | IDLE | 0.75 | 1.38 | 1.24 | -0.0 | 10141.37 | 5.98 | no_map |
| RIZEUSDT | IDLE | 0.45 | 1.68 | 0.97 | -0.07 | 35985.1 | 83.23 | no_map |
| TELUSDT | IDLE | 1.06 | 2.07 | 0.34 | -0.03 | 100211.76 | 47.47 | no_map |
| QNTUSDT | IDLE | 0.69 | 1.31 | 0.47 | -0.02 | 55233.56 | 7.83 | n/a |
| RWAUSDT | IDLE | 0.47 | 0.82 | 0.74 | -0.02 | 52254.89 | 29.81 | no_map |
| FLUIDUSDT | IDLE | 0.36 | 0.65 | 0.48 | -0.05 | 2079.84 | 21.26 | tvl≈2,608,117,054 |
| MNSRYUSDT | IDLE | 0.47 | 0.85 | 0.54 | -0.01 | 34563.83 | 66.51 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
