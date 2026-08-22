# Hulk DIGEST — 2026-08-22T10:46:24Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.2 | 0.02 | 51652508.05 | 2.06 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 23.87 | 11.49 | 0.09 | 217823748.11 | 5.32 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 10.95 | 0.01 | 1250553.55 | 6.46 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.53 | -0.09 | 661457.94 | 6.74 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 16.84 | 9.43 | 0.02 | 596521.67 | 10.59 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.17 | -0.05 | 240500.97 | 6.51 | n/a |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.58 | 0.13 | 816941.07 | 8.65 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 10.99 | 0.04 | 154349.14 | 19.76 | tvl≈2,031,082 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 9.72 | 7.39 | -0.02 | 424435.77 | 24.47 | n/a |
| KITEUSDT | IDLE | 4.12 | 9.28 | 4.59 | 0.04 | 73329.31 | 11.93 | no_map |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78951.51 | 34.03 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 9.12 | 7.81 | -0.04 | 168662.65 | 42.94 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 9.75 | 6.16 | -0.0 | 189250.83 | 6.25 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 21.54 | tvl≈2,553,890,177 |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3237.82 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.77 | no_map |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.4 | -0.0 | 49217.63 | 46.66 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.01 | 57424.05 | 16.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
