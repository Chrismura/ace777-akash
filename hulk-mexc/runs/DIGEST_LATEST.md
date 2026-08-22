# Hulk DIGEST — 2026-08-22T09:17:42Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.32 | 0.05 | 38808163.75 | 4.0 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 23.87 | 10.32 | 0.12 | 219445765.13 | 1.97 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 15.8 | 9.85 | 0.04 | 1299830.66 | 1.28 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.85 | -0.08 | 667748.82 | 3.35 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.81 | 0.04 | 599947.19 | 10.44 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.65 | -0.03 | 238966.81 | 3.23 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.86 | 0.05 | 154961.32 | 13.22 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.12 | 0.14 | 796659.02 | 10.31 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 8.0 | 6.02 | -0.0 | 466732.22 | 20.56 | n/a |
| KITEUSDT | IDLE | 4.22 | 9.68 | 3.5 | 0.06 | 73066.13 | 11.74 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.88 | 0.03 | 193016.0 | 7.73 | n/a |
| EDELUSDT | IDLE | 2.57 | 4.52 | 4.11 | -0.03 | 79237.93 | 33.69 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 18.43 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11574.81 | 15.99 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.69 | 6.02 | -0.02 | 171473.69 | 36.79 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.85 | -0.01 | 50331.56 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.03 | 57526.78 | 8.08 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
