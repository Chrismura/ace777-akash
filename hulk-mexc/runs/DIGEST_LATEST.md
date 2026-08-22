# Hulk DIGEST — 2026-08-22T10:34:53Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.29 | 0.01 | 51646282.96 | 2.06 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 23.87 | 12.85 | 0.08 | 217332123.76 | 4.05 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.87 | 0.0 | 1246639.09 | 6.52 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 22.93 | 12.25 | -0.1 | 663642.68 | 6.78 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 16.84 | 10.08 | 0.01 | 598028.03 | 14.92 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.33 | -0.06 | 238996.05 | 3.29 | n/a |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.72 | 0.12 | 811620.75 | 5.2 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.52 | 0.03 | 154655.23 | 14.41 | tvl≈2,031,082 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 9.72 | 8.34 | -0.03 | 426250.82 | 25.74 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 9.28 | 5.43 | 0.03 | 73143.64 | 9.25 | no_map |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78918.94 | 45.45 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.26 | -0.05 | 168466.77 | 43.1 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 9.75 | 6.79 | -0.0 | 189437.01 | 6.28 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 20.21 | tvl≈2,553,890,177 |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.26 | 0.0 | 49266.97 | 46.66 | no_map |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.02 | 57393.08 | 32.55 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11275.22 | 92.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
