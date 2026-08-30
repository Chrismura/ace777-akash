# Hulk DIGEST — 2026-08-30T06:12:47Z

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
| XRPUSDT | IDLE | 0.38 | 0.72 | 0.24 | 0.01 | 15836957.1 | 2.15 | n/a |
| CHIPUSDT | IDLE | 2.03 | 5.18 | 1.67 | -0.07 | 782226.21 | 2.47 | no_map |
| RIZEUSDT | IDLE | 2.91 | 12.09 | 2.87 | -0.04 | 44210.28 | 60.45 | no_map |
| CCUSDT | IDLE | 1.41 | 3.04 | 1.71 | 0.08 | 304348.63 | 9.23 | no_map |
| ZBCNUSDT | IDLE | 1.34 | 2.56 | 0.74 | -0.02 | 173529.4 | 10.45 | n/a |
| PYTHUSDT | IDLE | 0.56 | 1.01 | 0.67 | 0.0 | 317299.6 | 2.1 | tvl≈107,765,567 |
| WUSDT | IDLE | 1.12 | 2.12 | 0.84 | -0.0 | 194320.99 | 8.7 | tvl≈1,543,188,234 |
| REDUSDT | IDLE | 1.58 | 2.87 | 1.96 | 0.0 | 76909.72 | 11.87 | tvl≈2,022,108 |
| EDELUSDT | IDLE | 0.33 | 6.27 | 1.18 | 0.11 | 121803.42 | 17.08 | no_map |
| BIOUSDT | IDLE | 0.77 | 1.39 | 0.97 | -0.01 | 68381.76 | 3.63 | n/a |
| KITEUSDT | IDLE | 0.72 | 1.87 | 0.62 | 0.03 | 69233.08 | 11.59 | no_map |
| HBARUSDT | IDLE | 0.85 | 1.56 | 0.95 | -0.0 | 139647.26 | 1.34 | empty_tvl |
| RWAINCUSDT | IDLE | 0.65 | 1.3 | 0.0 | -0.03 | 1633.27 | 90.14 | no_map |
| TELUSDT | IDLE | 0.83 | 1.55 | 0.71 | -0.04 | 73005.37 | 23.71 | no_map |
| RWAUSDT | IDLE | 0.82 | 1.57 | 0.41 | 0.0 | 53182.41 | 32.65 | no_map |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.24 | 0.01 | 1463.59 | 20.72 | tvl≈2,614,779,983 |
| QNTUSDT | IDLE | 0.6 | 1.09 | 0.74 | 0.0 | 31137.44 | 8.13 | n/a |
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
