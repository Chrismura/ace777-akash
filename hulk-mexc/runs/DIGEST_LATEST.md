# Hulk DIGEST — 2026-08-22T06:27:01Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.09 | 19.14 | 7.42 | 0.08 | 19743762.51 | 11.61 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 23.87 | 8.27 | 0.19 | 210314393.01 | 14.76 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.84 | 0.05 | 1385783.58 | 6.31 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.74 | -0.09 | 690555.43 | 3.33 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.46 | 0.07 | 615629.95 | 12.35 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 12.99 | -0.04 | 245832.49 | 3.32 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 42.58 | 11.03 | 0.1 | 166200.36 | 20.01 | tvl≈2,081,438 |
| CCUSDT | IDLE | 1.98 | 11.25 | 2.56 | 0.19 | 771424.0 | 8.22 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.47 | 5.46 | 0.03 | 545723.62 | 21.87 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.56 | 0.04 | 200346.46 | 3.09 | n/a |
| KITEUSDT | IDLE | 2.83 | 9.68 | 4.56 | 0.09 | 74840.37 | 14.62 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.22 | tvl≈2,556,657,142 |
| EDELUSDT | IDLE | 2.31 | 4.52 | 3.89 | -0.03 | 88176.64 | 56.09 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11473.33 | 64.66 | no_map |
| TELUSDT | IDLE | 2.13 | 5.52 | 3.8 | 0.06 | 196547.98 | 30.83 | no_map |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.54 | 0.09 | 59535.71 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.04 | 58252.0 | 8.11 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
