# Hulk DIGEST — 2026-08-21T20:12:55Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.19 | 0.08 | 5478973.6 | 2.11 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.44 | 0.11 | 129075160.47 | 2.92 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.13 | 0.17 | 153961.12 | 12.23 | tvl≈2,358,074 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.86 | 6.52 | 0.11 | 477934.73 | 19.19 | n/a |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.69 | 0.07 | 632484.95 | 4.67 | no_map |
| HBARUSDT | IDLE | 1.76 | 3.23 | 2.41 | 0.05 | 795746.94 | 2.62 | empty_tvl |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 512474.12 | 3.09 | no_map |
| WUSDT | IDLE | 2.13 | 3.92 | 2.33 | 0.05 | 367092.61 | 6.39 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.58 | 5.33 | 3.47 | 0.01 | 189899.79 | 6.36 | n/a |
| EDELUSDT | IDLE | 2.52 | 4.41 | 4.23 | -0.05 | 80160.15 | 11.31 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.58 | 0.02 | 56222.1 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 37.5 | no_map |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.79 | 0.1 | 61310.92 | 14.01 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.0 | 2817.74 | 67.05 | no_map |
| TELUSDT | IDLE | 1.43 | 3.39 | 2.27 | 0.01 | 183520.73 | 43.27 | no_map |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.52 | 0.04 | 59885.52 | 4.68 | n/a |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54370.51 | 16.61 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.57 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
