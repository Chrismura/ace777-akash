# Hulk DIGEST — 2026-08-21T20:20:17Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.89 | 0.09 | 5494835.32 | 4.22 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.24 | 4.21 | 2.99 | 0.12 | 129238704.98 | 2.18 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.32 | 0.16 | 153445.31 | 17.99 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.87 | 0.12 | 478024.6 | 11.54 | n/a |
| CCUSDT | IDLE | 1.47 | 3.91 | 1.39 | 0.08 | 632545.21 | 5.58 | no_map |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.91 | 0.06 | 802160.47 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.49 | 0.08 | 510431.63 | 6.18 | no_map |
| WUSDT | IDLE | 2.11 | 3.92 | 2.04 | 0.06 | 367358.02 | 10.6 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.91 | 0.02 | 190111.84 | 3.16 | n/a |
| EDELUSDT | IDLE | 2.73 | 4.77 | 4.55 | -0.05 | 80218.1 | 22.68 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.49 | 0.02 | 56219.9 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | no_map |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.68 | 0.1 | 61168.01 | 11.2 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2801.19 | 67.05 | no_map |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.06 | 0.01 | 183703.41 | 37.81 | no_map |
| QNTUSDT | IDLE | 1.42 | 2.65 | 1.31 | 0.04 | 59914.32 | 3.11 | n/a |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 54473.89 | 16.63 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.52 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
