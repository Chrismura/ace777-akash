# Hulk DIGEST — 2026-08-20T22:14:10Z

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
| XRPUSDT | IDLE | 1.88 | 10.14 | 6.35 | 0.12 | 102829459.95 | 1.59 | n/a |
| PYTHUSDT | IDLE | 1.34 | 2.51 | 1.17 | 0.05 | 1355030.55 | 2.27 | tvl≈100,469,598 |
| CCUSDT | IDLE | 2.47 | 4.38 | 3.74 | -0.01 | 483646.43 | 6.07 | no_map |
| ZBCNUSDT | IDLE | 2.72 | 8.01 | 4.63 | 0.02 | 273316.03 | 9.29 | n/a |
| CHIPUSDT | IDLE | 2.07 | 6.45 | 0.52 | 0.11 | 292402.89 | 3.24 | no_map |
| HBARUSDT | IDLE | 2.07 | 3.82 | 2.11 | 0.02 | 471577.16 | 1.37 | empty_tvl |
| RWAINCUSDT | IDLE | 2.13 | 4.08 | 1.2 | 0.03 | 7502.15 | 5.51 | no_map |
| WUSDT | IDLE | 1.05 | 2.05 | 0.38 | 0.04 | 262640.65 | 6.65 | tvl≈1,499,819,205 |
| QAITUSDT | IDLE | 2.51 | 6.4 | 1.2 | -0.0 | 6010.2 | 66.45 | no_map |
| KITEUSDT | IDLE | 1.66 | 3.0 | 2.07 | 0.01 | 62993.95 | 13.3 | no_map |
| BIOUSDT | IDLE | 0.81 | 4.51 | 0.22 | 0.13 | 235668.47 | 34.82 | n/a |
| EDELUSDT | IDLE | 1.14 | 3.28 | 0.64 | 0.06 | 88444.09 | 21.3 | no_map |
| TELUSDT | IDLE | 1.66 | 8.29 | 6.94 | 0.12 | 181682.53 | 43.86 | no_map |
| REDUSDT | IDLE | 0.34 | 2.17 | 1.52 | 0.09 | 187524.52 | 12.46 | tvl≈1,907,253 |
| RIZEUSDT | IDLE | 0.88 | 4.47 | 3.98 | 0.02 | 48612.97 | 47.79 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.17 | 0.0 | 0.01 | 54762.83 | 42.64 | no_map |
| QNTUSDT | IDLE | 0.62 | 1.37 | 0.11 | 0.06 | 64345.13 | 4.83 | n/a |
| FLUIDUSDT | IDLE | 0.54 | 1.07 | 0.94 | 0.03 | 1933.85 | 21.68 | tvl≈2,526,351,519 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
