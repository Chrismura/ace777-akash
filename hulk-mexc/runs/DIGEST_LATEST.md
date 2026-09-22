# Hulk DIGEST — 2026-09-22T17:14:28Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.06 | 18.79 | 10.33 | 0.02 | 1559478.1 | 4.53 | tvl≈142,720,178 |
| XRPUSDT | IDLE | 2.26 | 4.27 | 1.64 | 0.05 | 116314123.64 | 3.83 | n/a |
| ETHUSDT | IDLE | 0.92 | 1.73 | 0.7 | -0.0 | 473553263.43 | 0.4 | no_map |
| BTCUSDT | IDLE | 0.73 | 1.42 | 0.33 | 0.0 | 909265087.42 | 0.22 | no_map |
| HBARUSDT | IDLE | 2.58 | 5.76 | 2.75 | 0.05 | 1363914.38 | 2.08 | empty_tvl |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 6.91 | 5.6 | -0.03 | 484376.38 | 7.08 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 14.26 | 11.62 | -0.0 | 263509.4 | 22.71 | no_map |
| WUSDT | IDLE | 1.98 | 3.87 | 0.54 | 0.03 | 364762.98 | 8.27 | tvl≈1,783,448,022 |
| CHIPUSDT | IDLE | 2.45 | 4.48 | 2.83 | -0.01 | 142683.13 | 17.48 | no_map |
| RIZEUSDT | IDLE | 1.95 | 23.47 | 3.95 | -0.18 | 42644.39 | 69.69 | no_map |
| ZBCNUSDT | IDLE | 1.97 | 3.64 | 2.05 | -0.01 | 238928.14 | 61.79 | n/a |
| BIOUSDT | IDLE | 1.96 | 3.88 | 0.27 | 0.02 | 126875.75 | 10.2 | n/a |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 8.52 | 0.4 | 0.06 | 104836.93 | 34.31 | no_map |
| REDUSDT | IDLE | 1.82 | 3.53 | 0.71 | 0.03 | 66352.84 | 10.15 | tvl≈2,820,552 |
| KITEUSDT | IDLE | 1.36 | 6.05 | 1.13 | 0.16 | 110551.79 | 9.46 | no_map |
| QNTUSDT | IDLE | 1.91 | 6.04 | 2.12 | 0.1 | 188779.74 | 5.47 | n/a |
| RWAINCUSDT | IDLE | 0.84 | 1.61 | 0.49 | 0.04 | 23479.15 | 5.51 | no_map |
| FLUIDUSDT | IDLE | 0.67 | 1.25 | 0.63 | 0.0 | 7959.28 | 21.91 | tvl≈2,653,203,313 |
| RWAUSDT | IDLE | 0.51 | 0.95 | 0.44 | -0.01 | 53957.75 | 36.43 | no_map |
| MNSRYUSDT | IDLE | 0.05 | 0.08 | 0.08 | -0.0 | 40316.13 | 9.02 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
