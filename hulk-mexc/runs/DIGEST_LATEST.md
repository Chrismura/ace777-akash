# Hulk DIGEST — 2026-08-21T20:24:15Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.13 | 0.08 | 5505314.81 | 2.11 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.23 | 4.21 | 2.75 | 0.12 | 129104685.62 | 2.17 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.91 | 0.16 | 153497.79 | 17.9 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.45 | 0.11 | 478146.4 | 27.44 | n/a |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.27 | 0.08 | 632809.31 | 4.64 | no_map |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.91 | 0.06 | 801715.88 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.46 | 0.08 | 510272.03 | 3.09 | no_map |
| WUSDT | IDLE | 2.11 | 3.92 | 1.95 | 0.06 | 366771.61 | 13.79 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.91 | 0.01 | 189876.02 | 3.16 | n/a |
| EDELUSDT | IDLE | 2.73 | 4.77 | 4.55 | -0.05 | 80268.05 | 22.68 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.68 | 0.01 | 56228.72 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.48 | 0.1 | 61051.62 | 9.32 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2801.19 | 67.05 | no_map |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.01 | 0.01 | 183617.24 | 32.4 | no_map |
| QNTUSDT | IDLE | 1.41 | 2.65 | 1.17 | 0.04 | 59942.47 | 6.23 | n/a |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 54283.75 | 24.95 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.52 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
