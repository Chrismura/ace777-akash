# Hulk DIGEST — 2026-09-26T22:04:22Z

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
| XRPUSDT | IDLE | 1.62 | 3.01 | 1.57 | -0.02 | 41242453.72 | 1.31 | n/a |
| ETHUSDT | IDLE | 0.55 | 1.07 | 0.26 | 0.0 | 114998860.45 | 0.3 | no_map |
| BTCUSDT | IDLE | 0.25 | 0.49 | 0.06 | 0.0 | 328938269.21 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.24 | 6.03 | 0.34 | 0.09 | 1062734.74 | 8.73 | tvl≈174,537,837 |
| CCUSDT | IDLE | 2.52 | 5.25 | 2.91 | 0.06 | 832232.88 | 9.63 | no_map |
| QNTUSDT | IDLE | 0.77 | 5.06 | 1.64 | 0.26 | 1480251.89 | 5.7 | n/a |
| WUSDT | IDLE | 2.61 | 5.22 | 2.56 | 0.06 | 568087.31 | 16.29 | tvl≈1,872,085,231 |
| CHIPUSDT | IDLE | 3.05 | 7.29 | 3.84 | -0.0 | 106302.06 | 20.47 | no_map |
| RWAINCUSDT | IDLE | 3.05 | 10.88 | 4.44 | 0.03 | 9783.8 | 24.4 | no_map |
| BIOUSDT | IDLE | 2.78 | 5.06 | 3.36 | -0.01 | 111908.44 | 9.4 | n/a |
| HBARUSDT | IDLE | 1.99 | 3.64 | 2.27 | -0.01 | 544876.69 | 1.07 | empty_tvl |
| EDELUSDT | IDLE | 2.46 | 4.42 | 3.3 | 0.02 | 170365.42 | 43.24 | no_map |
| ZBCNUSDT | IDLE | 1.98 | 3.66 | 2.01 | -0.02 | 190309.47 | 14.71 | n/a |
| KITEUSDT | IDLE | 1.91 | 7.67 | 0.61 | 0.16 | 122953.0 | 22.95 | no_map |
| REDUSDT | IDLE | 1.62 | 2.99 | 1.63 | -0.03 | 59398.82 | 12.49 | tvl≈3,065,259 |
| RIZEUSDT | IDLE | 1.35 | 3.53 | 0.1 | 0.08 | 48784.94 | 29.3 | no_map |
| TELUSDT | IDLE | 1.49 | 2.89 | 0.55 | -0.01 | 120180.98 | 43.01 | no_map |
| FLUIDUSDT | IDLE | 1.26 | 2.29 | 1.5 | -0.0 | 623.16 | 21.55 | tvl≈2,581,893,939 |
| RWAUSDT | IDLE | 0.61 | 1.15 | 0.5 | 0.03 | 56533.2 | 7.16 | no_map |
| MNSRYUSDT | IDLE | 0.27 | 0.52 | 0.15 | -0.0 | 38844.7 | 38.28 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
