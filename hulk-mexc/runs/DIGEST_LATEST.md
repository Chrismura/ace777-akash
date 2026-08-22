# Hulk DIGEST — 2026-08-22T10:03:09Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.68 | 16.77 | 9.69 | 0.02 | 51572525.3 | 2.02 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 12.15 | 0.06 | 214925486.99 | 2.01 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.72 | 0.01 | 1259507.66 | 6.45 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.83 | -0.1 | 664489.35 | 3.39 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 16.84 | 9.17 | 0.02 | 593751.39 | 14.79 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.22 | -0.02 | 236828.7 | 6.44 | n/a |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.33 | 0.12 | 809751.29 | 8.72 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 37.92 | 10.42 | 0.05 | 153855.12 | 9.82 | tvl≈2,081,438 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 7.87 | 6.58 | -0.01 | 436733.86 | 17.68 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 9.28 | 5.09 | 0.03 | 73359.49 | 12.89 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.05 | 9.75 | 5.87 | 0.01 | 189413.58 | 10.89 | n/a |
| EDELUSDT | IDLE | 2.7 | 4.76 | 4.32 | -0.04 | 79217.62 | 56.47 | no_map |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 20.02 | tvl≈2,553,890,177 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 6.98 | 6.38 | -0.03 | 170997.47 | 31.71 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.0 | 11462.91 | 59.44 | no_map |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.79 | -0.01 | 49330.97 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.02 | 57570.01 | 32.34 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
