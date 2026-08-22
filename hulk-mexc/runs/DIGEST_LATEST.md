# Hulk DIGEST — 2026-08-22T00:34:37Z

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
| PYTHUSDT | IDLE | 1.75 | 6.5 | 0.34 | 0.12 | 6403391.8 | 10.11 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 8.47 | 0.0 | 0.16 | 144892103.46 | 6.77 | n/a |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.49 | 0.07 | 938902.99 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 2.99 | 0.12 | 538829.35 | 47.42 | n/a |
| CCUSDT | IDLE | 1.91 | 7.42 | 0.29 | 0.14 | 639690.16 | 7.08 | no_map |
| WUSDT | IDLE | 2.74 | 6.91 | 1.09 | 0.08 | 388013.83 | 12.25 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.13 | 0.02 | 556978.94 | 9.23 | no_map |
| BIOUSDT | IDLE | 2.24 | 5.04 | 0.28 | 0.03 | 186034.0 | 6.17 | n/a |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79691.14 | 11.06 | no_map |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.63 | 0.13 | 59867.21 | 45.1 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.05 | 186232.94 | 36.04 | no_map |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.22 | 0.06 | 170429.45 | 9.07 | n/a |
| REDUSDT | IDLE | 0.63 | 5.79 | 0.0 | 0.24 | 157865.46 | 19.53 | tvl≈2,226,572 |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9678.68 | 59.19 | no_map |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.22 | 0.1 | 60970.59 | 12.84 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54670.3 | 16.42 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.71 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
