# Hulk DIGEST — 2026-08-30T08:12:41Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.67 | 1.21 | 0.8 | 0.01 | 16132000.12 | 0.72 | n/a |
| CHIPUSDT | IDLE | 2.65 | 4.83 | 3.11 | -0.03 | 698470.27 | 2.5 | no_map |
| CCUSDT | IDLE | 1.23 | 2.21 | 1.9 | 0.06 | 303433.01 | 9.29 | no_map |
| PYTHUSDT | IDLE | 0.6 | 1.06 | 1.0 | 0.02 | 300025.99 | 2.11 | tvl≈107,765,567 |
| REDUSDT | IDLE | 1.59 | 2.8 | 2.5 | -0.0 | 75602.4 | 11.93 | tvl≈2,022,108 |
| BIOUSDT | IDLE | 1.39 | 2.59 | 1.3 | -0.01 | 71335.94 | 3.66 | n/a |
| WUSDT | IDLE | 0.81 | 1.43 | 1.21 | 0.01 | 200378.83 | 9.83 | tvl≈1,544,365,094 |
| ZBCNUSDT | IDLE | 0.78 | 1.55 | 0.11 | -0.02 | 170767.24 | 1.56 | n/a |
| KITEUSDT | IDLE | 0.79 | 1.87 | 1.41 | 0.01 | 70211.89 | 11.68 | no_map |
| EDELUSDT | IDLE | 0.29 | 5.46 | 1.17 | 0.14 | 122657.69 | 42.35 | no_map |
| RIZEUSDT | IDLE | 0.9 | 3.72 | 1.05 | -0.04 | 43679.62 | 58.56 | no_map |
| RWAINCUSDT | IDLE | 0.91 | 1.59 | 1.57 | -0.03 | 1551.94 | 67.95 | no_map |
| HBARUSDT | IDLE | 0.63 | 1.18 | 0.52 | 0.0 | 143042.45 | 1.34 | empty_tvl |
| QNTUSDT | IDLE | 0.56 | 1.01 | 0.74 | 0.01 | 33581.81 | 1.63 | n/a |
| TELUSDT | IDLE | 0.66 | 1.19 | 0.82 | -0.03 | 74362.56 | 35.61 | no_map |
| RWAUSDT | IDLE | 0.67 | 1.32 | 0.16 | 0.01 | 52912.97 | 24.5 | no_map |
| FLUIDUSDT | IDLE | 0.01 | 0.02 | 0.02 | 0.01 | 1354.07 | 21.49 | tvl≈2,615,224,529 |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
