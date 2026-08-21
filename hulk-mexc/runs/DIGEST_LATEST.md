# Hulk DIGEST — 2026-08-21T20:35:01Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.83 | 0.08 | 5530067.54 | 2.11 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.24 | 4.21 | 3.11 | 0.11 | 129133756.8 | 2.91 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.25 | 0.17 | 154057.43 | 9.74 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.46 | 10.86 | 5.15 | 0.12 | 478387.06 | 6.47 | n/a |
| CCUSDT | IDLE | 1.43 | 3.91 | 0.64 | 0.08 | 634108.92 | 11.09 | no_map |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.82 | 0.06 | 799304.26 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.37 | 0.08 | 513828.87 | 3.08 | no_map |
| WUSDT | IDLE | 2.08 | 3.92 | 1.59 | 0.06 | 368300.94 | 7.39 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.42 | 0.02 | 189069.66 | 3.14 | n/a |
| EDELUSDT | IDLE | 2.72 | 5.01 | 3.25 | -0.05 | 80864.83 | 89.99 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10934.71 | 26.77 | no_map |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.45 | 0.02 | 56311.31 | 47.09 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.49 | 0.1 | 60739.47 | 13.04 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | no_map |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.64 | 0.01 | 183179.44 | 10.75 | no_map |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.77 | 0.04 | 59955.28 | 3.13 | n/a |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53878.63 | 16.64 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.26 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
