# Hulk DIGEST — 2026-10-14T11:20:37Z

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
| WUSDT | IDLE | 1.42 | 6.53 | 4.5 | -0.16 | 3531425.39 | 5.63 | tvl≈1,647,119,647 |
| PYTHUSDT | IDLE | 2.53 | 5.23 | 1.45 | 0.0 | 1764030.1 | 1.21 | tvl≈181,249,525 |
| ETHUSDT | IDLE | 1.04 | 1.94 | 0.95 | 0.01 | 123393742.4 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.97 | 1.8 | 0.95 | 0.02 | 27466344.77 | 0.73 | n/a |
| BTCUSDT | IDLE | 0.72 | 1.31 | 0.81 | 0.0 | 320719217.25 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.03 | 4.75 | 3.92 | 0.02 | 1525721.37 | 5.3 | n/a |
| CCUSDT | IDLE | 1.7 | 3.38 | 2.87 | -0.01 | 579110.86 | 8.27 | no_map |
| CHIPUSDT | IDLE | 2.79 | 4.99 | 3.95 | -0.04 | 80459.22 | 10.74 | no_map |
| KITEUSDT | IDLE | 2.15 | 6.53 | 4.95 | 0.08 | 78359.81 | 10.37 | no_map |
| EDELUSDT | IDLE | 1.34 | 2.49 | 1.24 | 0.03 | 203271.87 | 11.69 | no_map |
| REDUSDT | IDLE | 1.77 | 3.17 | 2.48 | 0.03 | 61971.2 | 7.74 | tvl≈3,916,642 |
| BIOUSDT | IDLE | 1.37 | 2.47 | 1.8 | 0.01 | 68747.82 | 7.32 | n/a |
| RIZEUSDT | IDLE | 1.46 | 4.98 | 1.12 | 0.06 | 49984.34 | 53.53 | no_map |
| ZBCNUSDT | IDLE | 0.61 | 1.19 | 0.19 | -0.0 | 200260.13 | 13.12 | n/a |
| RWAINCUSDT | IDLE | 1.13 | 2.56 | 2.09 | -0.06 | 34516.11 | 10.42 | no_map |
| HBARUSDT | IDLE | 1.16 | 2.06 | 1.73 | 0.01 | 309300.31 | 3.48 | empty_tvl |
| FLUIDUSDT | IDLE | 2.19 | 6.63 | 3.05 | 0.07 | 18184.15 | 21.52 | tvl≈2,375,848,589 |
| TELUSDT | IDLE | 0.75 | 1.41 | 0.61 | 0.03 | 111862.84 | 22.32 | no_map |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.31 | -0.01 | 55925.57 | 23.34 | no_map |
| MNSRYUSDT | IDLE | 0.21 | 0.39 | 0.2 | -0.01 | 38605.66 | 15.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
