# Hulk DIGEST — 2026-08-18T06:23:13Z

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
| XRPUSDT | IDLE | 0.74 | 1.4 | 0.54 | -0.01 | 12507154.42 | 2.01 | n/a |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 27.01 | 19.16 | -0.0 | 10907.25 | 149.5 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 31.54 | 5.24 | 0.28 | 70197.57 | 82.83 | tvl≈1,616,182 |
| KITEUSDT | IDLE | 2.35 | 4.36 | 2.25 | -0.01 | 60116.64 | 13.99 | no_map |
| CHIPUSDT | IDLE | 0.92 | 4.55 | 1.47 | -0.05 | 314323.16 | 7.13 | no_map |
| CCUSDT | IDLE | 1.21 | 2.28 | 0.87 | -0.04 | 293442.79 | 9.89 | no_map |
| PYTHUSDT | IDLE | 1.52 | 2.76 | 1.86 | -0.03 | 178505.7 | 2.63 | tvl≈86,707,897 |
| EDELUSDT | IDLE | 1.67 | 2.92 | 2.84 | -0.03 | 67502.88 | 26.56 | no_map |
| ZBCNUSDT | IDLE | 0.93 | 1.7 | 1.12 | -0.0 | 211728.71 | 9.59 | n/a |
| BIOUSDT | IDLE | 1.37 | 2.54 | 1.38 | -0.01 | 82774.38 | 4.12 | n/a |
| WUSDT | IDLE | 1.01 | 1.88 | 0.89 | -0.04 | 137260.72 | 14.72 | tvl≈1,357,117,741 |
| RWAINCUSDT | IDLE | 1.16 | 2.03 | 1.93 | -0.05 | 1105.23 | 41.65 | no_map |
| RIZEUSDT | IDLE | 0.5 | 3.22 | 3.12 | -0.04 | 78599.4 | 49.88 | no_map |
| QNTUSDT | IDLE | 1.19 | 2.12 | 1.77 | 0.0 | 36669.8 | 1.79 | n/a |
| HBARUSDT | IDLE | 0.67 | 1.3 | 0.23 | 0.02 | 140955.83 | 1.52 | empty_tvl |
| TELUSDT | IDLE | 0.88 | 1.88 | 0.36 | -0.04 | 133870.04 | 42.83 | no_map |
| RWAUSDT | IDLE | 0.49 | 0.87 | 0.77 | 0.0 | 50020.37 | 8.68 | no_map |
| FLUIDUSDT | IDLE | 0.56 | 0.99 | 0.82 | -0.05 | 598.38 | 21.76 | tvl≈2,314,876,205 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
