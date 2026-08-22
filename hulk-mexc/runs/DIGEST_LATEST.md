# Hulk DIGEST — 2026-08-22T17:28:04Z

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
| PYTHUSDT | IDLE | 1.75 | 8.48 | 1.17 | 0.11 | 49116967.91 | 3.83 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.44 | 0.06 | 213668319.47 | 2.03 | n/a |
| CCUSDT | IDLE | 0.95 | 4.25 | 0.62 | 0.12 | 769190.08 | 9.22 | no_map |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.95 | 0.01 | 1094977.17 | 5.16 | empty_tvl |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.03 | -0.09 | 631344.83 | 3.36 | no_map |
| WUSDT | IDLE | 0.59 | 2.58 | 0.09 | 0.0 | 533091.34 | 11.56 | tvl≈1,557,321,639 |
| BIOUSDT | IDLE | 1.19 | 7.96 | 6.33 | -0.08 | 228236.74 | 3.36 | n/a |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.34 | -0.02 | 306379.29 | 28.11 | n/a |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74910.27 | 34.46 | no_map |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.93 | 0.04 | 89159.87 | 15.1 | no_map |
| REDUSDT | IDLE | 0.53 | 5.67 | 1.7 | -0.13 | 122107.79 | 20.48 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.13 | 2.63 | 0.96 | 0.04 | 46153.35 | 45.71 | no_map |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2321.07 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.96 | -0.01 | 181210.04 | 4.72 | n/a |
| RWAINCUSDT | IDLE | 1.06 | 2.13 | 0.0 | 0.02 | 7571.75 | 101.36 | no_map |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | -0.0 | 131824.9 | 42.83 | no_map |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56279.71 | 16.16 | no_map |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 17.87 | tvl≈2,548,281,440 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
