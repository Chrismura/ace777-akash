# Hulk DIGEST — 2026-08-22T06:56:39Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.1 | 0.05 | 20609757.8 | 1.97 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 23.87 | 7.88 | 0.2 | 215369689.61 | 0.64 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.26 | 0.05 | 1393837.62 | 6.33 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.06 | -0.11 | 703238.3 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.08 | 0.07 | 618181.57 | 12.3 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.56 | -0.03 | 246373.34 | 9.91 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.47 | 0.06 | 160364.85 | 12.22 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.0 | 11.25 | 3.36 | 0.19 | 787323.41 | 5.78 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.47 | 5.03 | 0.05 | 544305.82 | 9.89 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.42 | 0.04 | 200321.42 | 9.24 | n/a |
| KITEUSDT | IDLE | 2.79 | 9.68 | 3.46 | 0.11 | 74388.57 | 9.03 | no_map |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.92 | -0.04 | 87716.98 | 33.43 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.15 | tvl≈2,556,657,142 |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11421.15 | 91.72 | no_map |
| TELUSDT | IDLE | 2.13 | 5.52 | 3.9 | 0.06 | 196663.27 | 15.41 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.54 | 0.09 | 59570.7 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.04 | 57874.95 | 32.47 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
