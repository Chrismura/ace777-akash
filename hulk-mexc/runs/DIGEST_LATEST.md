# Hulk DIGEST — 2026-08-21T23:18:14Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.46 | 0.12 | 6028157.88 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.23 | 0.15 | 138679120.57 | 2.76 | n/a |
| HBARUSDT | IDLE | 2.5 | 5.94 | 0.0 | 0.1 | 893546.85 | 1.24 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 10.56 | 0.15 | 0.15 | 511531.77 | 18.47 | n/a |
| CCUSDT | IDLE | 1.92 | 7.42 | 1.26 | 0.13 | 649857.64 | 7.13 | no_map |
| WUSDT | IDLE | 2.74 | 6.91 | 1.2 | 0.09 | 377630.47 | 11.25 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.28 | 0.05 | 547876.64 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.2 | 0.03 | 187938.37 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82514.67 | 21.83 | no_map |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 9.82 | 0.29 | 0.13 | 59506.92 | 44.31 | no_map |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 32.38 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.65 | 0.19 | 157499.45 | 10.49 | tvl≈2,226,572 |
| TELUSDT | IDLE | 2.69 | 6.62 | 0.0 | 0.07 | 184955.38 | 41.11 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.03 | 0.07 | 118585.68 | 1.5 | n/a |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.29 | 0.09 | 61607.52 | 12.07 | no_map |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.33 | 0.04 | 54450.95 | 16.39 | no_map |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.15 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
