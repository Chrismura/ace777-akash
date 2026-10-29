# Hulk DIGEST — 2026-10-29T02:47:13Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.01 | 3.53 | 3.31 | -0.03 | 23382520.56 | 0.78 | n/a |
| ETHUSDT | IDLE | 1.9 | 3.36 | 2.96 | -0.02 | 227703076.16 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.22 | 2.14 | 2.04 | -0.01 | 329726338.69 | 0.0 | no_map |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 6.67 | 6.2 | -0.04 | 459005.57 | 8.58 | tvl≈164,828,368 |
| WUSDT | IDLE | 3.0 | 5.32 | 4.47 | -0.04 | 453940.56 | 19.6 | tvl≈1,524,958,205 |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 5.7 | 5.11 | -0.03 | 446571.92 | 9.36 | no_map |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 7.05 | 6.59 | -0.05 | 90729.22 | 4.61 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 6.45 | 5.49 | -0.04 | 451615.13 | 5.74 | n/a |
| HBARUSDT | IDLE | 2.42 | 4.27 | 3.8 | -0.04 | 600642.9 | 9.56 | empty_tvl |
| KITEUSDT | IDLE | 2.63 | 4.61 | 4.29 | -0.05 | 60229.39 | 11.61 | no_map |
| EDELUSDT | IDLE | 2.16 | 3.78 | 3.61 | -0.05 | 176367.46 | 19.19 | no_map |
| CHIPUSDT | IDLE | 1.19 | 5.29 | 4.91 | -0.13 | 233910.76 | 6.28 | no_map |
| ZBCNUSDT | IDLE | 1.48 | 2.6 | 2.45 | -0.01 | 273893.19 | 23.81 | n/a |
| IOTAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 6.0 | 5.57 | -0.06 | 100797.27 | 24.97 | no_map |
| FLUIDUSDT | IDLE | 3.15 | 5.55 | 4.99 | -0.03 | 5957.42 | 21.16 | tvl≈2,233,222,484 |
| RWAINCUSDT | IDLE | 1.4 | 5.51 | 2.68 | -0.04 | 32783.77 | 21.1 | no_map |
| REDUSDT | IDLE | 1.26 | 2.26 | 1.73 | -0.03 | 63099.09 | 8.69 | tvl≈3,770,013 |
| RIZEUSDT | IDLE | 1.14 | 2.13 | 1.29 | -0.03 | 39280.63 | 21.38 | no_map |
| RWAUSDT | IDLE | 0.62 | 1.13 | 0.72 | 0.0 | 54386.0 | 24.07 | no_map |
| MNSRYUSDT | IDLE | 0.69 | 1.22 | 1.12 | -0.0 | 36671.3 | 67.6 | no_map |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
