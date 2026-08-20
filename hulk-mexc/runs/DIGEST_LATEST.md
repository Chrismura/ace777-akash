# Hulk DIGEST — 2026-08-20T11:23:35Z

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
| XRPUSDT | IDLE | 1.51 | 6.03 | 0.23 | 0.16 | 55713036.4 | 0.86 | n/a |
| BIOUSDT | IDLE | 2.34 | 19.0 | 3.38 | 0.31 | 268166.71 | 27.57 | n/a |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.64 | 8.08 | 0.87 | 0.11 | 250765.97 | 3.36 | no_map |
| PYTHUSDT | IDLE | 1.36 | 5.51 | 1.08 | 0.15 | 439847.48 | 2.27 | tvl≈97,789,379 |
| CCUSDT | IDLE | 1.09 | 4.31 | 1.39 | 0.14 | 451637.32 | 8.69 | no_map |
| WUSDT | IDLE | 1.79 | 3.81 | 1.41 | 0.07 | 319800.07 | 14.92 | tvl≈1,481,956,268 |
| REDUSDT | IDLE | 1.34 | 11.79 | 9.08 | 0.25 | 200245.21 | 11.77 | tvl≈2,044,775 |
| ZBCNUSDT | IDLE | 1.62 | 8.27 | 0.73 | 0.19 | 242976.59 | 19.44 | n/a |
| RIZEUSDT | IDLE | 1.59 | 10.17 | 9.23 | 0.07 | 69580.6 | 47.99 | no_map |
| QAITUSDT | IDLE | 2.12 | 6.03 | 4.42 | -0.01 | 10210.12 | 27.17 | no_map |
| HBARUSDT | IDLE | 1.43 | 2.74 | 0.77 | 0.07 | 408770.25 | 1.38 | empty_tvl |
| KITEUSDT | IDLE | 1.07 | 2.06 | 0.59 | 0.07 | 60855.65 | 13.44 | no_map |
| QNTUSDT | IDLE | 2.2 | 5.5 | 0.66 | 0.09 | 57171.75 | 4.86 | n/a |
| EDELUSDT | IDLE | 0.55 | 4.3 | 1.95 | 0.21 | 102995.19 | 22.12 | no_map |
| RWAINCUSDT | IDLE | 0.64 | 1.88 | 0.45 | 0.05 | 17300.96 | 33.65 | no_map |
| TELUSDT | IDLE | 0.87 | 4.29 | 0.18 | 0.15 | 199474.2 | 23.8 | no_map |
| FLUIDUSDT | IDLE | 1.72 | 4.58 | 0.65 | 0.1 | 3390.06 | 21.55 | tvl≈2,512,177,409 |
| RWAUSDT | IDLE | 0.47 | 0.87 | 0.43 | 0.01 | 52515.45 | 17.26 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
