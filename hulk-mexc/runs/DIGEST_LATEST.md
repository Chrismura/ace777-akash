# Hulk DIGEST — 2026-08-21T23:02:30Z

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
| PYTHUSDT | IDLE | 1.55 | 5.77 | 0.3 | 0.12 | 5941363.71 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.74 | 6.54 | 0.87 | 0.15 | 137664736.21 | 3.47 | n/a |
| HBARUSDT | IDLE | 2.38 | 5.03 | 0.36 | 0.09 | 886643.57 | 2.51 | empty_tvl |
| CCUSDT | IDLE | 1.89 | 7.42 | 0.48 | 0.14 | 662428.74 | 10.62 | no_map |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.07 | 0.44 | 0.15 | 509449.75 | 31.99 | n/a |
| WUSDT | IDLE | 2.74 | 6.91 | 1.21 | 0.08 | 376369.62 | 15.33 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.09 | 0.05 | 543963.1 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.03 | 187903.18 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.35 | 5.15 | 0.33 | -0.03 | 82542.93 | 21.83 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.79 | 0.18 | 157253.7 | 11.31 | tvl≈2,226,572 |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | no_map |
| TELUSDT | IDLE | 2.67 | 6.45 | 0.72 | 0.06 | 185764.72 | 46.5 | no_map |
| QNTUSDT | IDLE | 2.47 | 5.02 | 0.0 | 0.07 | 94098.62 | 1.5 | n/a |
| KITEUSDT | IDLE | 1.1 | 3.12 | 1.03 | 0.1 | 61419.76 | 10.18 | no_map |
| RIZEUSDT | IDLE | 1.05 | 4.7 | 2.03 | 0.06 | 56389.93 | 46.99 | no_map |
| RWAUSDT | IDLE | 1.03 | 2.0 | 0.41 | 0.04 | 54243.68 | 24.58 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.82 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
