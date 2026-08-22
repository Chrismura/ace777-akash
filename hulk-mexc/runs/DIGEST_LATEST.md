# Hulk DIGEST — 2026-08-22T01:18:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.73 | 9.41 | 0.22 | 0.15 | 6656515.52 | 1.96 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 8.4 | 0.37 | 0.15 | 150032685.15 | 4.07 | n/a |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.88 | 0.08 | 955143.05 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.62 | 10.08 | 3.34 | 0.1 | 546853.35 | 33.59 | n/a |
| CCUSDT | IDLE | 1.77 | 7.18 | 0.36 | 0.16 | 659981.0 | 10.52 | no_map |
| WUSDT | IDLE | 2.71 | 6.65 | 0.86 | 0.09 | 392482.31 | 7.13 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.65 | 3.56 | 1.61 | -0.01 | 522822.43 | 6.18 | no_map |
| BIOUSDT | IDLE | 2.5 | 5.57 | 0.73 | 0.03 | 186455.58 | 15.35 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79585.32 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.11 | 60528.23 | 45.81 | no_map |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.56 | 0.18 | 159638.31 | 15.14 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.91 | 0.07 | 170446.16 | 6.03 | n/a |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.05 | 181118.28 | 41.22 | no_map |
| KITEUSDT | IDLE | 1.47 | 4.48 | 0.31 | 0.11 | 60857.56 | 9.02 | no_map |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9620.22 | 16.16 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.68 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 55200.44 | 16.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
