# Hulk DIGEST — 2026-08-22T06:47:42Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.85 | 0.06 | 20359684.43 | 3.93 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 23.87 | 6.68 | 0.22 | 214192868.49 | 3.79 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 15.8 | 7.84 | 0.07 | 1392060.66 | 6.25 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.44 | -0.12 | 701704.81 | 3.36 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.07 | 0.07 | 617158.3 | 14.38 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 12.9 | -0.04 | 246508.57 | 3.31 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.58 | 0.05 | 162465.11 | 11.37 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.03 | 0.18 | 783939.55 | 4.99 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.47 | 5.02 | 0.05 | 546185.28 | 17.3 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.26 | 0.04 | 200325.14 | 7.68 | n/a |
| KITEUSDT | IDLE | 2.8 | 9.68 | 3.79 | 0.11 | 74391.14 | 9.96 | no_map |
| EDELUSDT | IDLE | 2.22 | 4.52 | 2.59 | -0.04 | 87649.14 | 33.43 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 16.77 | tvl≈2,556,657,142 |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | no_map |
| TELUSDT | IDLE | 2.13 | 5.52 | 3.9 | 0.06 | 196871.81 | 15.41 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.06 | 0.09 | 59584.49 | 39.31 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 57981.33 | 16.23 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
