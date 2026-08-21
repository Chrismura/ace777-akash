# Hulk DIGEST — 2026-08-21T20:16:42Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.24 | 0.08 | 5487042.16 | 2.12 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.3 | 0.11 | 128965227.82 | 2.18 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.37 | 0.16 | 153911.4 | 11.44 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.49 | 10.86 | 6.14 | 0.12 | 477671.12 | 25.65 | n/a |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.83 | 0.08 | 632381.9 | 6.54 | no_map |
| HBARUSDT | IDLE | 1.75 | 3.23 | 2.33 | 0.05 | 796070.05 | 1.31 | empty_tvl |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.88 | 0.08 | 512707.82 | 3.1 | no_map |
| WUSDT | IDLE | 2.14 | 3.92 | 2.37 | 0.05 | 367349.9 | 14.9 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.56 | 5.33 | 3.16 | 0.02 | 190254.99 | 3.17 | n/a |
| EDELUSDT | IDLE | 2.66 | 4.65 | 4.44 | -0.05 | 80210.11 | 22.65 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.65 | 0.01 | 56226.53 | 26.38 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 37.5 | no_map |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.7 | 0.1 | 61348.68 | 11.2 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2806.14 | 67.05 | no_map |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.01 | 0.02 | 183746.06 | 37.81 | no_map |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.48 | 0.04 | 59964.32 | 6.24 | n/a |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54452.5 | 24.95 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.99 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
