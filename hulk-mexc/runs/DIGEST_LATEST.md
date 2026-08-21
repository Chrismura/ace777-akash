# Hulk DIGEST — 2026-08-21T21:07:42Z

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
| PYTHUSDT | IDLE | 1.22 | 4.51 | 1.83 | 0.09 | 5583638.5 | 2.09 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.59 | 0.1 | 128075233.23 | 2.9 | n/a |
| ZBCNUSDT | IDLE | 2.02 | 8.19 | 5.78 | 0.09 | 480395.95 | 32.35 | n/a |
| CHIPUSDT | IDLE | 1.59 | 4.62 | 3.91 | 0.08 | 514057.68 | 3.1 | no_map |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.31 | 0.1 | 641923.57 | 7.37 | no_map |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.55 | 0.06 | 805870.21 | 1.3 | empty_tvl |
| WUSDT | IDLE | 1.99 | 3.83 | 1.02 | 0.06 | 368155.87 | 13.66 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.48 | 5.2 | 2.86 | 0.01 | 187960.79 | 3.17 | n/a |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.5 | 0.16 | 153373.03 | 12.33 | tvl≈2,358,074 |
| EDELUSDT | IDLE | 2.06 | 4.12 | 2.86 | -0.06 | 82224.93 | 34.03 | no_map |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.01 | 56242.94 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10866.26 | 32.12 | no_map |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.32 | 0.11 | 61171.91 | 11.16 | no_map |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 180483.67 | 32.14 | no_map |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60146.5 | 4.69 | n/a |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 167.13 | no_map |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.91 | 0.03 | 53754.71 | 8.31 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.26 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
