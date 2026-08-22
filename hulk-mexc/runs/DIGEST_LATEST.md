# Hulk DIGEST — 2026-08-22T10:58:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 16.77 | 12.26 | -0.01 | 51654049.52 | 2.08 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 23.87 | 12.9 | 0.07 | 218344985.11 | 4.06 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.41 | -0.0 | 1249137.29 | 2.6 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 22.93 | 11.95 | -0.11 | 656195.08 | 3.38 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.67 | 0.01 | 594712.56 | 14.85 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.84 | -0.07 | 240539.32 | 6.54 | n/a |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.73 | 0.12 | 818551.18 | 9.52 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 9.72 | 8.11 | -0.04 | 423661.04 | 15.93 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 37.92 | 10.11 | 0.04 | 154337.78 | 13.35 | tvl≈2,031,082 |
| KITEUSDT | IDLE | 4.11 | 9.28 | 4.45 | 0.03 | 73276.36 | 11.89 | no_map |
| EDELUSDT | IDLE | 3.34 | 5.96 | 4.76 | -0.04 | 78979.54 | 56.72 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 9.12 | 7.32 | -0.04 | 169021.21 | 37.44 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 9.75 | 6.62 | -0.01 | 189136.31 | 7.84 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 21.66 | tvl≈2,553,890,177 |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2438.25 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.83 | no_map |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57441.48 | 8.15 | no_map |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.35 | -0.0 | 49230.1 | 46.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
