# Hulk DIGEST — 2026-08-22T05:52:19Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.79 | 0.09 | 17445930.4 | 3.93 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 23.87 | 9.24 | 0.17 | 205469960.41 | 2.59 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 15.8 | 8.65 | 0.06 | 1368551.93 | 13.86 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.85 | -0.09 | 710658.19 | 6.67 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.06 | 0.08 | 604977.81 | 12.3 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.72 | -0.03 | 245351.69 | 13.07 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.17 | 0.1 | 164920.8 | 14.88 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.77 | 0.18 | 766682.83 | 3.33 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 6.06 | 0.04 | 547497.28 | 17.49 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 13.91 | 8.55 | 0.04 | 197058.76 | 12.34 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.85 | 0.08 | 74186.7 | 12.98 | no_map |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.62 | -0.02 | 88559.96 | 32.95 | no_map |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.28 | 0.06 | 58994.36 | 31.52 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.0 | 11600.95 | 64.66 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5403.29 | 19.6 | tvl≈2,592,362,987 |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | no_map |
| TELUSDT | IDLE | 2.09 | 5.52 | 3.11 | 0.07 | 196697.08 | 20.35 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 58013.7 | 8.11 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
