# Hulk DIGEST — 2026-08-22T07:25:46Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.74 | 0.03 | 21941646.93 | 11.78 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 23.87 | 5.62 | 0.21 | 218841332.85 | 3.12 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 8.99 | 0.05 | 1352613.58 | 5.06 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.68 | -0.09 | 696292.06 | 3.33 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.41 | 0.06 | 618584.6 | 12.35 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.01 | -0.05 | 246536.25 | 6.55 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 42.01 | 9.86 | 0.08 | 160665.17 | 16.35 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.07 | 11.25 | 4.03 | 0.18 | 798669.8 | 6.66 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.56 | 0.05 | 542138.99 | 16.41 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.14 | 0.04 | 198738.54 | 4.61 | n/a |
| KITEUSDT | IDLE | 3.39 | 9.68 | 2.73 | 0.1 | 74225.85 | 8.96 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6900.29 | 21.08 | tvl≈2,556,699,557 |
| EDELUSDT | IDLE | 2.19 | 4.52 | 2.16 | -0.03 | 87194.86 | 66.67 | no_map |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.03 | 11367.66 | 53.65 | no_map |
| TELUSDT | IDLE | 2.07 | 5.36 | 3.65 | 0.04 | 193467.61 | 40.96 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.44 | 0.0 | 55967.68 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58197.79 | 8.09 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
