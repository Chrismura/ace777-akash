# Hulk DIGEST — 2026-08-21T22:01:27Z

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
| PYTHUSDT | IDLE | 1.25 | 4.74 | 0.37 | 0.1 | 5691768.01 | 2.06 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.65 | 0.12 | 129660000.83 | 2.14 | n/a |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.48 | 0.08 | 833901.7 | 2.53 | empty_tvl |
| CCUSDT | IDLE | 1.31 | 3.95 | 0.01 | 0.11 | 635829.2 | 7.28 | no_map |
| CHIPUSDT | IDLE | 1.54 | 4.54 | 2.5 | 0.04 | 527150.49 | 3.09 | no_map |
| WUSDT | IDLE | 2.1 | 4.19 | 0.09 | 0.07 | 367874.72 | 17.64 | tvl≈1,602,784,605 |
| ZBCNUSDT | IDLE | 1.44 | 6.19 | 0.04 | 0.11 | 493977.58 | 31.56 | n/a |
| BIOUSDT | IDLE | 2.27 | 5.01 | 0.98 | 0.03 | 185628.99 | 3.11 | n/a |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.56 | 0.18 | 153908.4 | 8.95 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 1.95 | 4.12 | 1.21 | -0.04 | 83077.49 | 33.28 | no_map |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.13 | 0.05 | 191553.71 | 25.99 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | no_map |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.03 | 10238.87 | 53.39 | no_map |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.97 | 0.11 | 61247.64 | 12.89 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.54 | 0.05 | 56591.74 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.25 | 2.49 | 0.12 | 0.05 | 62398.83 | 4.63 | n/a |
| RWAUSDT | IDLE | 0.67 | 1.33 | 0.08 | 0.04 | 54149.05 | 16.46 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.06 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
