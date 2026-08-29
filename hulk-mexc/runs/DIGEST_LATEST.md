# Hulk DIGEST — 2026-08-29T00:09:03Z

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
| XRPUSDT | IDLE | 0.69 | 1.37 | 0.01 | -0.04 | 51749138.31 | 2.16 | n/a |
| CHIPUSDT | IDLE | 0.77 | 4.9 | 1.9 | 0.06 | 1156197.46 | 9.65 | no_map |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 33.82 | 23.79 | -0.14 | 83646.13 | 46.02 | no_map |
| PYTHUSDT | IDLE | 1.38 | 3.06 | 0.42 | -0.04 | 689851.36 | 2.1 | tvl≈105,141,896 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 13.86 | 10.17 | -0.12 | 91585.02 | 19.36 | no_map |
| ZBCNUSDT | IDLE | 1.8 | 4.64 | 3.43 | -0.08 | 171594.07 | 19.4 | n/a |
| CCUSDT | IDLE | 1.2 | 2.34 | 0.4 | -0.01 | 305483.44 | 8.07 | no_map |
| REDUSDT | IDLE | 1.4 | 3.51 | 0.74 | -0.01 | 64104.37 | 12.04 | tvl≈1,963,374 |
| RIZEUSDT | IDLE | 1.77 | 4.74 | 3.15 | 0.01 | 35033.04 | 57.37 | no_map |
| RWAINCUSDT | IDLE | 2.28 | 4.28 | 1.92 | -0.02 | 3438.94 | 98.25 | no_map |
| WUSDT | IDLE | 0.64 | 1.53 | 0.05 | -0.05 | 208880.79 | 10.89 | tvl≈1,524,659,841 |
| HBARUSDT | IDLE | 0.71 | 1.29 | 0.86 | -0.03 | 469355.11 | 1.31 | empty_tvl |
| KITEUSDT | IDLE | 1.25 | 2.49 | 0.0 | -0.01 | 79146.8 | 18.61 | no_map |
| BIOUSDT | IDLE | 0.58 | 1.41 | 0.07 | -0.05 | 85086.19 | 3.58 | n/a |
| TELUSDT | IDLE | 0.95 | 2.26 | 1.75 | -0.08 | 99980.97 | 17.27 | no_map |
| QNTUSDT | IDLE | 0.58 | 1.16 | 0.05 | -0.03 | 42536.92 | 6.53 | n/a |
| RWAUSDT | IDLE | 0.29 | 0.58 | 0.0 | 0.0 | 54650.89 | 8.29 | no_map |
| FLUIDUSDT | IDLE | 0.2 | 0.41 | 0.0 | -0.06 | 4553.01 | 22.13 | tvl≈2,598,079,405 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
