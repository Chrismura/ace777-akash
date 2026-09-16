# Hulk DIGEST — 2026-09-16T16:14:00Z

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
| XRPUSDT | IDLE | 1.1 | 2.96 | 2.35 | -0.08 | 80805249.26 | 2.37 | n/a |
| ETHUSDT | IDLE | 1.13 | 2.06 | 1.36 | -0.01 | 411389541.38 | 0.08 | no_map |
| BTCUSDT | IDLE | 0.61 | 1.13 | 0.65 | -0.01 | 545790590.54 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.77 | 3.21 | 2.19 | -0.02 | 670913.25 | 3.83 | tvl≈117,736,442 |
| CCUSDT | IDLE | 1.9 | 3.55 | 1.6 | -0.03 | 465859.02 | 7.73 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 7.82 | 5.48 | -0.03 | 97309.51 | 19.21 | no_map |
| REDUSDT | IDLE | 2.91 | 5.14 | 4.5 | -0.04 | 64502.88 | 17.39 | tvl≈2,418,556 |
| EDELUSDT | IDLE | 0.91 | 10.01 | 6.52 | 0.37 | 409670.4 | 56.59 | no_map |
| RIZEUSDT | IDLE | 2.22 | 36.05 | 19.19 | 0.36 | 61285.47 | 352.73 | no_map |
| KITEUSDT | IDLE | 2.03 | 4.12 | 0.42 | -0.03 | 59157.3 | 13.87 | no_map |
| HBARUSDT | IDLE | 1.71 | 3.61 | 2.47 | -0.07 | 354347.2 | 1.37 | empty_tvl |
| BIOUSDT | IDLE | 1.64 | 2.92 | 2.44 | -0.02 | 81269.27 | 4.09 | n/a |
| WUSDT | IDLE | 1.07 | 2.33 | 1.64 | -0.06 | 186817.43 | 14.75 | tvl≈1,403,113,998 |
| ZBCNUSDT | IDLE | 0.98 | 2.59 | 1.26 | -0.03 | 207192.33 | 21.62 | n/a |
| RWAINCUSDT | IDLE | 1.27 | 2.31 | 1.51 | -0.02 | 12779.8 | 53.36 | no_map |
| TELUSDT | IDLE | 1.69 | 5.1 | 3.48 | -0.08 | 121869.03 | 35.4 | no_map |
| FLUIDUSDT | IDLE | 1.65 | 3.0 | 1.97 | -0.06 | 2518.27 | 21.61 | tvl≈2,621,549,794 |
| QNTUSDT | IDLE | 1.08 | 2.11 | 0.27 | -0.04 | 39190.98 | 5.0 | n/a |
| RWAUSDT | IDLE | 0.89 | 1.76 | 0.08 | -0.0 | 52883.65 | 7.53 | no_map |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.24 | -0.01 | 32934.42 | 7.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
