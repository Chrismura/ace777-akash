# Hulk DIGEST — 2026-09-09T20:14:06Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.39 | 2.45 | 2.21 | -0.02 | 40299202.33 | 0.71 | n/a |
| ETHUSDT | IDLE | 1.15 | 2.03 | 1.83 | -0.01 | 338126622.32 | 0.41 | no_map |
| BTCUSDT | IDLE | 0.94 | 1.68 | 1.39 | -0.0 | 525825265.88 | 0.0 | no_map |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 7.32 | 6.38 | -0.01 | 619339.08 | 1.87 | tvl≈126,603,020 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 7.68 | 6.58 | -0.03 | 180278.19 | 49.53 | no_map |
| WUSDT | IDLE | 3.24 | 5.91 | 3.81 | -0.01 | 199379.53 | 13.84 | tvl≈1,587,877,496 |
| CCUSDT | IDLE | 1.3 | 2.43 | 1.15 | -0.04 | 592260.7 | 5.75 | no_map |
| CHIPUSDT | IDLE | 1.83 | 6.28 | 5.8 | 0.04 | 112016.63 | 12.76 | no_map |
| ZBCNUSDT | IDLE | 1.73 | 3.25 | 1.4 | 0.03 | 198323.45 | 3.3 | n/a |
| REDUSDT | IDLE | 2.17 | 3.84 | 3.36 | 0.0 | 61376.88 | 17.04 | tvl≈2,456,013 |
| HBARUSDT | IDLE | 1.27 | 2.28 | 1.76 | -0.03 | 420427.34 | 1.29 | empty_tvl |
| BIOUSDT | IDLE | 1.27 | 2.34 | 1.4 | -0.04 | 95273.12 | 3.74 | n/a |
| KITEUSDT | IDLE | 1.48 | 2.7 | 1.67 | 0.01 | 62507.61 | 19.28 | no_map |
| FLUIDUSDT | IDLE | 2.66 | 4.7 | 4.08 | -0.06 | 896.61 | 21.57 | tvl≈2,663,516,293 |
| RWAINCUSDT | IDLE | 1.26 | 2.29 | 1.58 | -0.01 | 7125.32 | 22.08 | no_map |
| RIZEUSDT | IDLE | 0.81 | 8.76 | 7.66 | -0.03 | 71413.94 | 105.82 | no_map |
| TELUSDT | IDLE | 1.65 | 2.95 | 2.33 | 0.03 | 101838.75 | 38.81 | no_map |
| RWAUSDT | IDLE | 1.46 | 2.56 | 2.35 | -0.01 | 54694.38 | 14.59 | no_map |
| QNTUSDT | IDLE | 0.8 | 1.4 | 1.31 | -0.02 | 44213.42 | 4.52 | n/a |
| MNSRYUSDT | IDLE | 0.32 | 0.61 | 0.22 | 0.01 | 24096.3 | 59.86 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
