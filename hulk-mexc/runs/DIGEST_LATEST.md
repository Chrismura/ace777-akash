# Hulk DIGEST — 2026-09-21T02:03:48Z

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
| ETHUSDT | IDLE | 2.01 | 3.72 | 1.95 | 0.01 | 362458292.5 | 1.17 | no_map |
| XRPUSDT | IDLE | 1.85 | 3.39 | 2.07 | 0.01 | 44082408.87 | 2.84 | n/a |
| BTCUSDT | IDLE | 1.0 | 1.82 | 1.18 | -0.0 | 478090069.39 | 0.07 | no_map |
| HBARUSDT | IDLE | 1.47 | 4.3 | 3.42 | 0.04 | 1297883.93 | 2.34 | empty_tvl |
| PYTHUSDT | IDLE | 1.82 | 3.8 | 3.37 | -0.02 | 652726.57 | 3.29 | tvl≈137,703,798 |
| WUSDT | IDLE | 1.85 | 4.3 | 3.87 | 0.01 | 505579.68 | 7.03 | tvl≈1,709,609,638 |
| CCUSDT | IDLE | 2.15 | 4.6 | 0.88 | 0.03 | 408768.8 | 9.88 | no_map |
| ZBCNUSDT | IDLE | 2.82 | 5.29 | 2.3 | -0.0 | 202352.82 | 27.8 | n/a |
| EDELUSDT | IDLE | 1.45 | 19.33 | 4.17 | 0.42 | 182456.14 | 45.85 | no_map |
| CHIPUSDT | IDLE | 2.51 | 5.48 | 2.82 | -0.01 | 87134.39 | 16.39 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 7.06 | 5.1 | -0.03 | 35832.49 | 96.83 | no_map |
| BIOUSDT | IDLE | 1.62 | 2.89 | 2.27 | -0.02 | 80299.07 | 7.26 | n/a |
| KITEUSDT | IDLE | 1.38 | 2.47 | 1.88 | 0.01 | 58375.06 | 13.04 | no_map |
| REDUSDT | IDLE | 1.16 | 2.13 | 1.25 | 0.02 | 81951.72 | 10.56 | tvl≈2,754,986 |
| RWAINCUSDT | IDLE | 0.87 | 1.68 | 0.41 | 0.0 | 6859.16 | 17.83 | no_map |
| TELUSDT | IDLE | 2.0 | 3.68 | 2.13 | 0.03 | 89971.58 | 52.7 | no_map |
| QNTUSDT | IDLE | 1.27 | 2.37 | 1.07 | -0.02 | 114279.5 | 4.64 | n/a |
| FLUIDUSDT | IDLE | 1.34 | 2.33 | 2.27 | -0.01 | 4117.68 | 21.63 | tvl≈2,648,916,893 |
| RWAUSDT | IDLE | 0.92 | 1.77 | 0.51 | 0.01 | 55268.77 | 29.15 | no_map |
| MNSRYUSDT | IDLE | 0.64 | 1.22 | 0.41 | 0.0 | 38209.72 | 33.0 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
