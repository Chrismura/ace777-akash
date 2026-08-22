# Hulk DIGEST — 2026-08-22T04:27:55Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.9 | 13.61 | 1.27 | 0.19 | 10976396.79 | 5.53 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 12.41 | 0.41 | 0.22 | 170345623.9 | 3.76 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.72 | 0.2 | 731687.28 | 8.24 | no_map |
| HBARUSDT | IDLE | 2.28 | 7.14 | 0.87 | 0.11 | 1033311.62 | 1.2 | empty_tvl |
| CHIPUSDT | IDLE | 2.76 | 5.36 | 1.0 | 0.02 | 442396.41 | 2.97 | no_map |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.11 | 0.07 | 200014.36 | 2.99 | n/a |
| WUSDT | IDLE | 1.95 | 7.18 | 0.26 | 0.14 | 434333.22 | 10.65 | tvl≈1,672,612,247 |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.85 | 0.13 | 536264.57 | 26.5 | n/a |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.98 | 0.09 | 59200.93 | 44.52 | no_map |
| EDELUSDT | IDLE | 2.07 | 4.07 | 3.37 | -0.04 | 80098.24 | 44.89 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.41 | 0.21 | 158512.64 | 19.08 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.61 | 5.55 | 0.7 | 0.13 | 67824.01 | 13.31 | no_map |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9290.79 | 70.63 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.46 | 0.09 | 179112.18 | 5.93 | n/a |
| TELUSDT | IDLE | 1.31 | 3.12 | 0.45 | 0.08 | 176562.61 | 40.57 | no_map |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56285.51 | 8.02 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.69 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
