# Hulk DIGEST — 2026-08-22T00:50:39Z

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
| PYTHUSDT | IDLE | 2.01 | 7.38 | 0.82 | 0.12 | 6494547.3 | 8.06 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.1 | 0.15 | 147608868.2 | 4.14 | n/a |
| HBARUSDT | IDLE | 2.83 | 6.36 | 2.14 | 0.07 | 941828.57 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.41 | 0.11 | 543728.5 | 31.65 | n/a |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.43 | 0.14 | 645868.32 | 5.36 | no_map |
| WUSDT | IDLE | 2.74 | 6.91 | 1.05 | 0.09 | 389099.88 | 11.22 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.56 | 3.56 | 0.36 | 0.03 | 548321.78 | 6.11 | no_map |
| BIOUSDT | IDLE | 2.52 | 5.62 | 0.61 | 0.03 | 186521.28 | 3.08 | n/a |
| EDELUSDT | IDLE | 2.54 | 5.5 | 0.76 | -0.01 | 79835.61 | 21.91 | no_map |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.7 | 0.13 | 60125.3 | 45.1 | no_map |
| QAITUSDT | IDLE | 2.26 | 4.22 | 1.99 | -0.01 | 3755.28 | 15.91 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.07 | 184198.83 | 30.9 | no_map |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.49 | 0.06 | 170516.65 | 6.07 | n/a |
| REDUSDT | IDLE | 0.96 | 8.58 | 1.64 | 0.25 | 159733.67 | 17.74 | tvl≈2,226,572 |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9754.98 | 16.16 | no_map |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.19 | 0.1 | 60987.79 | 12.84 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54924.21 | 16.43 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.72 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
