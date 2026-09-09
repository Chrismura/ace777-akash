# Hulk DIGEST — 2026-09-09T22:14:14Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.87 | 3.37 | 2.44 | -0.02 | 42387164.18 | 0.72 | n/a |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 11.52 | 9.31 | -0.03 | 978460.2 | 5.8 | tvl≈126,603,020 |
| ETHUSDT | IDLE | 1.26 | 2.23 | 1.95 | -0.01 | 372990904.6 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.82 | 1.44 | 1.27 | -0.01 | 535866315.29 | 0.0 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 8.4 | 6.3 | -0.03 | 202069.68 | 13.18 | tvl≈1,561,358,286 |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 19.09 | 14.58 | -0.06 | 122590.05 | 16.1 | no_map |
| REDUSDT | IDLE | 3.88 | 7.07 | 4.56 | -0.0 | 62604.83 | 18.04 | tvl≈2,456,013 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.04 | 8.64 | 6.52 | -0.09 | 99446.74 | 3.94 | n/a |
| CCUSDT | IDLE | 1.25 | 2.25 | 1.6 | -0.03 | 610519.65 | 9.68 | no_map |
| EDELUSDT | IDLE | 2.82 | 4.99 | 4.28 | -0.03 | 176460.69 | 19.84 | no_map |
| HBARUSDT | IDLE | 2.01 | 3.61 | 2.69 | -0.03 | 448095.87 | 1.31 | empty_tvl |
| KITEUSDT | IDLE | 2.23 | 4.1 | 2.42 | -0.01 | 59953.74 | 38.07 | no_map |
| RWAINCUSDT | IDLE | 2.3 | 4.1 | 3.39 | -0.0 | 6800.93 | 28.29 | no_map |
| ZBCNUSDT | IDLE | 1.17 | 2.22 | 0.8 | 0.03 | 198719.28 | 24.02 | n/a |
| RWAUSDT | IDLE | 2.75 | 4.85 | 4.27 | -0.03 | 55507.82 | 29.76 | no_map |
| FLUIDUSDT | IDLE | 2.2 | 3.92 | 3.77 | -0.08 | 951.16 | 22.17 | tvl≈2,651,250,217 |
| RIZEUSDT | IDLE | 0.6 | 7.16 | 1.6 | 0.02 | 72458.76 | 111.85 | no_map |
| QNTUSDT | IDLE | 1.15 | 2.16 | 0.95 | 0.0 | 44866.28 | 22.53 | n/a |
| TELUSDT | IDLE | 1.22 | 2.18 | 1.69 | 0.02 | 102064.39 | 72.28 | no_map |
| MNSRYUSDT | IDLE | 1.1 | 1.94 | 1.79 | -0.01 | 25060.53 | 56.52 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
