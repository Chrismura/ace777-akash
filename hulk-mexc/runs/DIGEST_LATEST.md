# Hulk DIGEST — 2026-08-22T10:41:17Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 16.77 | 10.76 | 0.02 | 51652554.46 | 2.05 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 12.12 | 0.09 | 217907161.77 | 4.02 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.02 | 0.01 | 1250432.43 | 3.88 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.71 | -0.09 | 661952.93 | 6.75 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 16.84 | 9.31 | 0.02 | 597805.45 | 13.75 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.06 | -0.05 | 239305.7 | 6.49 | n/a |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.51 | 0.13 | 810599.66 | 9.5 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.19 | 0.03 | 154365.34 | 13.51 | tvl≈2,031,082 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 9.72 | 7.64 | -0.02 | 423882.49 | 21.97 | n/a |
| KITEUSDT | IDLE | 4.13 | 9.28 | 4.74 | 0.04 | 73480.79 | 12.86 | no_map |
| EDELUSDT | IDLE | 3.34 | 5.96 | 4.86 | -0.04 | 78993.97 | 22.7 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 9.12 | 8.11 | -0.05 | 168551.2 | 37.66 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.44 | 0.0 | 189367.79 | 17.18 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 18.54 | tvl≈2,553,890,177 |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3241.83 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.77 | no_map |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57490.66 | 8.15 | no_map |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.52 | -0.0 | 49234.23 | 46.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
