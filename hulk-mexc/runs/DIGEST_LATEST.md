# Hulk DIGEST — 2026-08-22T08:29:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.92 | 0.03 | 28540999.2 | 11.94 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 23.87 | 10.64 | 0.12 | 224107020.32 | 0.66 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.18 | 0.02 | 1343021.35 | 7.68 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.47 | -0.1 | 684285.99 | 3.36 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.62 | 0.03 | 600485.25 | 14.59 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.61 | -0.04 | 253484.04 | 12.76 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.75 | 0.07 | 155715.98 | 9.68 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.07 | 11.25 | 3.1 | 0.18 | 822744.73 | 13.21 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.1 | 0.02 | 537912.86 | 10.99 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.08 | 0.03 | 193995.36 | 13.98 | n/a |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.33 | 0.06 | 73359.9 | 10.92 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6716.59 | 21.14 | tvl≈2,562,763,298 |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.92 | -0.04 | 86866.59 | 55.9 | no_map |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11182.34 | 107.24 | no_map |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | 0.01 | 173438.91 | 20.57 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.8 | 0.0 | 52279.31 | 46.13 | no_map |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.2 | 0.04 | 58322.26 | 32.21 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
