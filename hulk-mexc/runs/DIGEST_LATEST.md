# Hulk DIGEST — 2026-08-22T06:52:14Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.7 | 0.05 | 20521743.64 | 3.92 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 23.87 | 6.85 | 0.21 | 214614667.37 | 1.9 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.25 | 0.06 | 1392680.8 | 2.51 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.79 | -0.11 | 703344.52 | 6.67 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 17.58 | 6.88 | 0.07 | 617804.16 | 11.25 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.62 | -0.04 | 246844.46 | 3.3 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.31 | 0.05 | 160595.01 | 20.05 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.05 | 0.18 | 784062.94 | 8.33 | no_map |
| ZBCNUSDT | IDLE | 3.16 | 8.47 | 4.96 | 0.04 | 546178.6 | 28.66 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.48 | 0.04 | 200306.33 | 12.34 | n/a |
| KITEUSDT | IDLE | 2.78 | 9.68 | 3.38 | 0.11 | 74466.05 | 9.92 | no_map |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.04 | 87721.21 | 11.14 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.86 | tvl≈2,556,657,142 |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196809.25 | 10.28 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.06 | 0.09 | 59598.12 | 46.13 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 57944.74 | 24.34 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
