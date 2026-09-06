# Hulk DIGEST — 2026-09-06T05:29:51Z

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
| XRPUSDT | IDLE | 0.81 | 1.49 | 0.9 | 0.02 | 24466732.0 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.73 | 1.41 | 0.37 | 0.02 | 201146345.11 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.22 | 0.39 | 0.33 | 0.0 | 379237284.63 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.84 | 5.29 | 2.57 | 0.04 | 430633.34 | 1.8 | tvl≈122,790,024 |
| CHIPUSDT | IDLE | 2.52 | 5.64 | 2.61 | 0.01 | 409507.31 | 1.69 | no_map |
| RWAINCUSDT | IDLE | 2.92 | 5.37 | 3.12 | 0.01 | 9214.25 | 5.36 | no_map |
| CCUSDT | IDLE | 1.36 | 2.52 | 1.32 | 0.02 | 295179.59 | 7.28 | no_map |
| RIZEUSDT | IDLE | 1.93 | 12.58 | 4.55 | 0.11 | 119104.03 | 87.68 | no_map |
| KITEUSDT | IDLE | 2.12 | 4.05 | 1.31 | -0.03 | 64839.07 | 10.07 | no_map |
| WUSDT | IDLE | 1.4 | 2.52 | 1.81 | 0.03 | 175233.08 | 5.95 | tvl≈1,663,803,237 |
| ZBCNUSDT | IDLE | 1.36 | 2.68 | 0.23 | 0.01 | 207830.85 | 14.91 | n/a |
| HBARUSDT | IDLE | 1.37 | 2.59 | 0.94 | 0.03 | 426866.34 | 1.23 | empty_tvl |
| REDUSDT | IDLE | 1.47 | 2.67 | 1.84 | 0.0 | 59281.1 | 10.27 | tvl≈2,345,447 |
| BIOUSDT | IDLE | 0.9 | 1.65 | 0.99 | 0.03 | 97254.16 | 3.57 | n/a |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.57 | 0.02 | 111979.87 | 9.38 | no_map |
| QNTUSDT | IDLE | 1.69 | 3.38 | 0.0 | 0.05 | 37064.4 | 1.49 | n/a |
| MNSRYUSDT | IDLE | 1.37 | 2.64 | 0.72 | 0.02 | 39796.23 | 10.73 | no_map |
| RWAUSDT | IDLE | 1.17 | 2.06 | 1.81 | 0.03 | 53321.1 | 14.18 | no_map |
| FLUIDUSDT | IDLE | 1.18 | 2.33 | 0.14 | 0.04 | 380.96 | 21.93 | tvl≈2,661,977,389 |
| TELUSDT | IDLE | 0.85 | 1.59 | 0.75 | 0.0 | 72465.04 | 35.11 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
