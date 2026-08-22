# Hulk DIGEST — 2026-08-22T08:07:51Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.24 | 0.0 | 25582288.74 | 7.89 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 9.07 | 0.17 | 224916731.52 | 1.3 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.76 | 0.04 | 1356621.98 | 3.83 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.97 | -0.09 | 683367.88 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.3 | 0.04 | 609214.38 | 10.39 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.15 | -0.04 | 247109.52 | 6.37 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.52 | 0.06 | 156184.24 | 9.64 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.06 | 11.25 | 2.62 | 0.2 | 815595.27 | 13.12 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 8.47 | 6.66 | 0.03 | 537130.31 | 17.61 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.6 | 0.03 | 194179.72 | 13.89 | n/a |
| KITEUSDT | IDLE | 3.84 | 9.68 | 4.51 | 0.06 | 72901.58 | 9.12 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.15 | tvl≈2,556,699,557 |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.68 | -0.04 | 87198.11 | 100.5 | no_map |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.75 | no_map |
| TELUSDT | IDLE | 1.86 | 4.7 | 4.15 | -0.01 | 173917.31 | 30.91 | no_map |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.86 | 0.0 | 52291.16 | 44.42 | no_map |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58291.47 | 8.04 | no_map |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
