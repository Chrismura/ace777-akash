# Hulk DIGEST — 2026-08-22T08:56:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.12 | 0.03 | 34716902.37 | 1.99 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 23.87 | 9.76 | 0.1 | 223555344.84 | 2.61 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.06 | 0.02 | 1314029.03 | 1.28 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.21 | -0.1 | 679827.02 | 3.36 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.09 | 0.02 | 601637.51 | 4.19 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.38 | -0.04 | 254565.4 | 6.37 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.22 | 0.04 | 155142.9 | 11.51 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.8 | 0.15 | 800185.4 | 4.98 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 8.47 | 7.18 | -0.02 | 497341.42 | 24.78 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.1 | 0.01 | 193138.21 | 4.65 | n/a |
| KITEUSDT | IDLE | 3.76 | 9.68 | 3.16 | 0.06 | 73559.12 | 13.51 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 7.38 | 5.12 | 0.02 | 7020.8 | 21.4 | tvl≈2,562,763,298 |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.78 | -0.05 | 86492.45 | 44.84 | no_map |
| RWAINCUSDT | IDLE | 2.38 | 4.48 | 1.88 | 0.03 | 11642.78 | 15.99 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 6.52 | 6.12 | -0.03 | 174070.1 | 36.79 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.87 | 3.73 | 1.59 | 0.01 | 52052.44 | 44.83 | no_map |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.03 | 58153.23 | 24.24 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
