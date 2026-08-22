# Hulk DIGEST — 2026-08-22T16:37:21Z

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
| PYTHUSDT | IDLE | 1.76 | 8.66 | 0.21 | 0.08 | 51431207.23 | 5.78 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.34 | 7.64 | 3.98 | 0.05 | 215096832.26 | 2.04 | n/a |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.05 | -0.01 | 1126160.26 | 2.58 | empty_tvl |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.33 | 0.08 | 762160.57 | 7.69 | no_map |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.83 | -0.11 | 627386.07 | 3.35 | no_map |
| WUSDT | IDLE | 0.61 | 2.58 | 0.61 | -0.01 | 543185.44 | 14.79 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.49 | -0.03 | 315168.06 | 17.92 | n/a |
| BIOUSDT | IDLE | 0.96 | 6.58 | 3.97 | -0.06 | 219809.31 | 3.28 | n/a |
| KITEUSDT | IDLE | 1.94 | 4.35 | 2.26 | 0.02 | 85159.66 | 14.36 | no_map |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.03 | 74876.15 | 22.81 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.01 | -0.15 | 130146.26 | 10.03 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.34 | 0.1 | 48882.35 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2317.66 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.28 | -0.01 | 182314.63 | 3.16 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8091.51 | 75.23 | no_map |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.1 | -0.0 | 137110.41 | 53.59 | no_map |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.16 | 0.02 | 56557.48 | 24.34 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 20.87 | tvl≈2,551,700,555 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
