# Hulk DIGEST — 2026-08-22T09:02:23Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.08 | 0.03 | 35621826.11 | 3.99 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.56 | 0.09 | 222971845.7 | 1.32 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 15.8 | 10.14 | 0.01 | 1308885.46 | 2.57 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.88 | -0.1 | 675215.13 | 6.71 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 9.03 | 0.02 | 601319.69 | 13.63 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.08 | -0.04 | 242397.26 | 3.21 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.8 | 0.05 | 154683.39 | 11.51 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.13 | 11.25 | 3.98 | 0.15 | 796224.84 | 10.0 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 8.0 | 6.24 | -0.0 | 490813.74 | 53.29 | n/a |
| KITEUSDT | IDLE | 4.21 | 9.68 | 3.45 | 0.06 | 73406.21 | 10.84 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.05 | 0.01 | 193138.87 | 4.66 | n/a |
| EDELUSDT | IDLE | 2.51 | 4.52 | 3.35 | -0.05 | 86492.4 | 22.4 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 7041.88 | 21.48 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11599.81 | 15.99 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 6.52 | 6.07 | -0.04 | 171931.06 | 36.79 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.68 | -0.03 | 50855.38 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.03 | 57901.18 | 8.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
