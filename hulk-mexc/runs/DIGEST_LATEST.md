# Hulk DIGEST — 2026-08-21T21:50:28Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.53 | 0.09 | 5667921.43 | 2.06 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.57 | 0.11 | 129941209.2 | 1.42 | n/a |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.05 | 527416.64 | 3.09 | no_map |
| HBARUSDT | IDLE | 2.05 | 4.49 | 0.39 | 0.08 | 825798.39 | 11.39 | empty_tvl |
| CCUSDT | IDLE | 1.29 | 3.86 | 0.0 | 0.11 | 641417.13 | 4.55 | no_map |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.68 | 0.11 | 491037.9 | 56.74 | n/a |
| WUSDT | IDLE | 1.96 | 3.91 | 0.02 | 0.07 | 368811.32 | 13.52 | tvl≈1,602,784,605 |
| BIOUSDT | IDLE | 2.39 | 5.2 | 1.44 | 0.03 | 187305.57 | 3.12 | n/a |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.28 | 0.17 | 154128.01 | 9.01 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 1.92 | 4.12 | 0.88 | -0.04 | 83659.08 | 22.17 | no_map |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.04 | 0.04 | 55820.96 | 47.31 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | no_map |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.14 | 0.12 | 61290.32 | 9.19 | no_map |
| TELUSDT | IDLE | 1.9 | 4.81 | 0.89 | 0.03 | 185326.42 | 42.15 | no_map |
| QNTUSDT | IDLE | 1.36 | 2.65 | 0.48 | 0.04 | 62631.51 | 10.82 | n/a |
| RWAUSDT | IDLE | 0.59 | 1.17 | 0.08 | 0.03 | 53956.32 | 16.52 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.9 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
