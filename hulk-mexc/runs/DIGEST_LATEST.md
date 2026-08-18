# Hulk DIGEST — 2026-08-18T13:09:31Z

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
| XRPUSDT | IDLE | 0.52 | 0.97 | 0.51 | -0.0 | 11498465.79 | 2.01 | n/a |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 8.85 | 5.9 | -0.02 | 3705.6 | 23.64 | no_map |
| CHIPUSDT | IDLE | 2.17 | 6.39 | 5.47 | -0.08 | 253243.27 | 3.59 | no_map |
| QAITUSDT | IDLE | 2.05 | 27.25 | 17.29 | -0.18 | 15434.82 | 151.58 | no_map |
| REDUSDT | IDLE | 0.99 | 8.44 | 5.6 | 0.18 | 100872.81 | 7.12 | tvl≈1,773,646 |
| CCUSDT | IDLE | 0.92 | 1.77 | 0.52 | -0.02 | 266811.15 | 10.87 | no_map |
| ZBCNUSDT | IDLE | 0.97 | 1.88 | 0.43 | 0.01 | 211409.8 | 16.47 | n/a |
| RIZEUSDT | IDLE | 1.52 | 5.26 | 1.25 | -0.07 | 47021.23 | 47.42 | no_map |
| BIOUSDT | IDLE | 1.01 | 1.95 | 0.49 | -0.0 | 77006.9 | 8.17 | n/a |
| PYTHUSDT | IDLE | 0.44 | 0.87 | 0.1 | -0.02 | 202609.92 | 5.24 | tvl≈85,819,507 |
| KITEUSDT | IDLE | 0.99 | 1.97 | 0.05 | -0.01 | 70195.45 | 14.11 | no_map |
| WUSDT | IDLE | 0.44 | 0.78 | 0.61 | -0.03 | 153229.84 | 14.79 | tvl≈1,358,397,625 |
| EDELUSDT | IDLE | 0.9 | 2.25 | 1.81 | -0.06 | 78543.58 | 52.7 | no_map |
| TELUSDT | IDLE | 1.52 | 2.8 | 1.54 | -0.02 | 125345.19 | 42.58 | no_map |
| HBARUSDT | IDLE | 0.48 | 0.95 | 0.11 | 0.0 | 119362.1 | 1.51 | empty_tvl |
| QNTUSDT | IDLE | 0.37 | 0.72 | 0.18 | -0.01 | 37630.26 | 1.78 | n/a |
| RWAUSDT | IDLE | 0.4 | 0.78 | 0.17 | 0.0 | 50525.37 | 26.03 | no_map |
| FLUIDUSDT | IDLE | 0.23 | 0.41 | 0.31 | -0.03 | 156.46 | 21.02 | tvl≈2,315,920,391 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
