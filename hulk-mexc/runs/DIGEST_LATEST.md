# Hulk DIGEST — 2026-08-22T00:22:04Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.63 | 0.1 | 6334890.64 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 8.23 | 1.95 | 0.14 | 143674426.08 | 0.69 | n/a |
| HBARUSDT | IDLE | 2.82 | 6.36 | 1.89 | 0.07 | 930555.38 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.31 | 0.1 | 519215.48 | 18.0 | n/a |
| CCUSDT | IDLE | 1.98 | 7.42 | 2.13 | 0.11 | 647946.77 | 8.09 | no_map |
| WUSDT | IDLE | 2.74 | 6.91 | 0.99 | 0.08 | 384542.53 | 13.27 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.79 | 0.05 | 545186.49 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.02 | 186172.72 | 6.21 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.01 | 79863.1 | 22.15 | no_map |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 3.09 | 0.14 | 59817.43 | 45.2 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.56 | 0.06 | 188892.81 | 36.04 | no_map |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.57 | 0.06 | 170998.13 | 6.07 | n/a |
| REDUSDT | IDLE | 0.56 | 4.91 | 1.9 | 0.2 | 157734.19 | 17.64 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.08 | 3.12 | 0.56 | 0.09 | 61281.33 | 11.05 | no_map |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9727.87 | 59.19 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54748.25 | 32.84 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 49.21 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
