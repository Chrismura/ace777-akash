# Hulk DIGEST — 2026-08-12T21:28:15Z

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
| XRPUSDT | IDLE | 0.55 | 0.98 | 0.76 | -0.01 | 15035223.33 | 0.99 | n/a |
| RIZEUSDT | IDLE | 2.4 | 19.45 | 11.03 | 0.13 | 46826.8 | 43.0 | no_map |
| CHIPUSDT | IDLE | 2.92 | 6.56 | 4.13 | 0.05 | 104988.69 | 8.62 | no_map |
| PYTHUSDT | IDLE | 1.44 | 2.56 | 2.1 | -0.04 | 323378.72 | 2.5 | tvl≈91,244,786 |
| EDELUSDT | IDLE | 2.33 | 8.52 | 4.55 | 0.08 | 72136.83 | 49.3 | no_map |
| CCUSDT | IDLE | 1.21 | 2.15 | 1.84 | -0.02 | 217020.49 | 8.11 | no_map |
| BIOUSDT | IDLE | 1.81 | 3.18 | 3.0 | -0.04 | 62775.68 | 12.54 | n/a |
| REDUSDT | IDLE | 1.78 | 3.11 | 3.02 | -0.02 | 60453.62 | 15.34 | tvl≈1,565,896 |
| QNTUSDT | IDLE | 2.93 | 5.12 | 4.87 | 0.01 | 60943.02 | 5.17 | n/a |
| ZBCNUSDT | IDLE | 1.16 | 2.08 | 1.57 | -0.04 | 190210.27 | 30.36 | n/a |
| WUSDT | IDLE | 1.02 | 1.8 | 1.6 | -0.03 | 181686.11 | 12.4 | tvl≈1,366,104,275 |
| RWAINCUSDT | IDLE | 2.12 | 4.03 | 1.36 | -0.01 | 1626.25 | 52.88 | no_map |
| KITEUSDT | IDLE | 1.15 | 2.28 | 0.12 | -0.02 | 60065.71 | 14.73 | no_map |
| QAITUSDT | IDLE | 0.68 | 2.51 | 1.67 | -0.04 | 4599.13 | 60.51 | no_map |
| TELUSDT | IDLE | 0.97 | 1.8 | 0.88 | 0.01 | 96931.76 | 31.8 | no_map |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.02 | 52005.43 | 16.63 | no_map |
| HBARUSDT | IDLE | 0.37 | 0.65 | 0.65 | -0.01 | 83737.09 | 3.05 | empty_tvl |
| FLUIDUSDT | IDLE | 0.37 | 0.64 | 0.64 | -0.02 | 553.46 | 20.27 | tvl≈2,329,356,792 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
