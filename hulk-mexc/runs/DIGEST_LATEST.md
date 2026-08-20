# Hulk DIGEST — 2026-08-20T21:28:20Z

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
| XRPUSDT | IDLE | 1.88 | 10.14 | 6.38 | 0.13 | 103203808.46 | 1.59 | n/a |
| PYTHUSDT | IDLE | 1.34 | 2.51 | 1.12 | 0.04 | 1350746.84 | 2.27 | tvl≈100,469,598 |
| CCUSDT | IDLE | 2.6 | 4.61 | 3.95 | -0.01 | 472197.47 | 8.09 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 8.28 | 5.58 | -0.0 | 277663.09 | 17.14 | n/a |
| CHIPUSDT | IDLE | 2.03 | 6.28 | 0.94 | 0.09 | 290791.38 | 6.52 | no_map |
| HBARUSDT | IDLE | 2.09 | 3.82 | 2.35 | 0.02 | 486916.62 | 1.38 | empty_tvl |
| QAITUSDT | IDLE | 2.87 | 7.22 | 1.95 | -0.0 | 6010.2 | 66.45 | no_map |
| WUSDT | IDLE | 1.2 | 2.29 | 0.72 | 0.03 | 277822.93 | 13.34 | tvl≈1,499,819,205 |
| BIOUSDT | IDLE | 0.81 | 4.51 | 1.58 | 0.1 | 234691.97 | 3.2 | n/a |
| KITEUSDT | IDLE | 1.7 | 3.0 | 2.65 | -0.0 | 63774.82 | 13.38 | no_map |
| RWAINCUSDT | IDLE | 2.2 | 4.08 | 2.07 | 0.03 | 7947.53 | 44.22 | no_map |
| TELUSDT | IDLE | 2.09 | 10.8 | 6.07 | 0.13 | 180647.12 | 43.45 | no_map |
| EDELUSDT | IDLE | 1.35 | 4.0 | 0.0 | 0.05 | 88423.71 | 10.69 | no_map |
| REDUSDT | IDLE | 0.34 | 2.17 | 1.56 | 0.08 | 186968.21 | 12.48 | tvl≈1,907,253 |
| QNTUSDT | IDLE | 1.97 | 4.04 | 3.12 | 0.05 | 63726.2 | 3.23 | n/a |
| RIZEUSDT | IDLE | 0.61 | 3.22 | 1.89 | 0.04 | 48325.86 | 48.44 | no_map |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.17 | 0.01 | 54518.66 | 17.09 | no_map |
| FLUIDUSDT | IDLE | 1.07 | 2.25 | 0.94 | 0.03 | 1933.85 | 22.51 | tvl≈2,526,351,519 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
