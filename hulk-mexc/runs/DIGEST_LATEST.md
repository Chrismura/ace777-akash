# Hulk DIGEST — 2026-08-21T22:50:03Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.29 | 0.11 | 5885462.23 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.67 | 6.41 | 0.48 | 0.15 | 135930656.37 | 0.69 | n/a |
| CCUSDT | IDLE | 1.9 | 7.44 | 0.52 | 0.14 | 659391.23 | 7.96 | no_map |
| HBARUSDT | IDLE | 2.17 | 4.73 | 0.11 | 0.08 | 875144.83 | 10.07 | empty_tvl |
| ZBCNUSDT | IDLE | 1.93 | 8.3 | 0.03 | 0.14 | 508311.79 | 6.76 | n/a |
| WUSDT | IDLE | 2.62 | 6.46 | 0.09 | 0.09 | 371584.64 | 9.14 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.08 | 0.05 | 534774.89 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.03 | 188124.41 | 6.22 | n/a |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.6 | 0.17 | 157161.65 | 13.0 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82603.75 | 21.83 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.06 | 186896.0 | 31.04 | no_map |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.11 | 0.11 | 61339.93 | 9.22 | no_map |
| QNTUSDT | IDLE | 2.16 | 4.32 | 0.0 | 0.06 | 86409.07 | 1.51 | n/a |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.98 | 0.06 | 56397.58 | 46.99 | no_map |
| RWAUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.04 | 54111.99 | 8.19 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 22.57 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
