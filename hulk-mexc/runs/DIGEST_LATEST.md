# Hulk DIGEST — 2026-08-21T23:10:07Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.48 | 0.12 | 5989099.76 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.76 | 6.77 | 0.48 | 0.15 | 138426084.38 | 2.07 | n/a |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.92 | 0.13 | 666498.92 | 8.88 | no_map |
| HBARUSDT | IDLE | 2.39 | 5.24 | 0.09 | 0.09 | 890303.68 | 1.25 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.4 | 0.15 | 511344.98 | 35.3 | n/a |
| WUSDT | IDLE | 2.75 | 6.91 | 1.4 | 0.08 | 374774.95 | 11.28 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 0.88 | 0.05 | 544802.32 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.31 | 5.04 | 1.38 | 0.02 | 187388.05 | 3.12 | n/a |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.02 | 82539.69 | 21.81 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10220.57 | 16.16 | no_map |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.18 | 0.18 | 157381.22 | 19.48 | tvl≈2,226,572 |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | no_map |
| TELUSDT | IDLE | 2.66 | 6.51 | 0.26 | 0.07 | 185031.9 | 51.52 | no_map |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.01 | 0.07 | 104730.82 | 1.5 | n/a |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61579.5 | 11.12 | no_map |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54404.92 | 8.2 | no_map |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.24 | tvl≈2,590,200,853 |
| RIZEUSDT | IDLE | 1.17 | 5.54 | 0.3 | 0.09 | 57925.66 | 253.68 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
