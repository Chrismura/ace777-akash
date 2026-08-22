# Hulk DIGEST — 2026-08-22T00:25:51Z

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
| PYTHUSDT | IDLE | 1.75 | 6.39 | 1.13 | 0.1 | 6355406.31 | 2.04 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 8.23 | 1.55 | 0.14 | 143851566.33 | 1.38 | n/a |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.87 | 0.07 | 931064.32 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.58 | 0.11 | 518885.8 | 1.93 | n/a |
| CCUSDT | IDLE | 1.97 | 7.42 | 1.65 | 0.12 | 647245.7 | 10.73 | no_map |
| WUSDT | IDLE | 2.71 | 6.91 | 0.54 | 0.08 | 384635.16 | 10.16 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.4 | 0.04 | 545186.62 | 3.05 | no_map |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.58 | 0.02 | 185893.5 | 3.1 | n/a |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79841.25 | 22.12 | no_map |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 3.11 | 0.14 | 59830.11 | 43.62 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.56 | 0.06 | 188818.87 | 46.28 | no_map |
| QNTUSDT | IDLE | 2.56 | 5.42 | 1.39 | 0.06 | 170964.04 | 4.54 | n/a |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.48 | 0.09 | 61234.3 | 12.89 | no_map |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9718.83 | 59.19 | no_map |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.38 | 0.22 | 157820.28 | 25.3 | tvl≈2,226,572 |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54729.8 | 16.42 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 19.7 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
