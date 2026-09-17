# Hulk DIGEST — 2026-09-17T21:17:54Z

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
| ETHUSDT | IDLE | 0.73 | 1.31 | 1.03 | 0.02 | 305580668.94 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.71 | 1.26 | 1.03 | 0.0 | 38920076.91 | 2.32 | n/a |
| BTCUSDT | IDLE | 0.36 | 0.63 | 0.59 | 0.01 | 436213211.35 | 0.0 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.5 | 40.67 | 16.55 | -0.19 | 267273.85 | 47.21 | no_map |
| CCUSDT | IDLE | 1.83 | 3.34 | 2.21 | 0.04 | 562674.61 | 6.0 | no_map |
| PYTHUSDT | IDLE | 1.48 | 3.64 | 3.34 | 0.06 | 548296.09 | 3.6 | tvl≈124,148,312 |
| WUSDT | IDLE | 1.9 | 6.12 | 2.7 | 0.1 | 327806.61 | 13.22 | tvl≈1,477,858,174 |
| HBARUSDT | IDLE | 1.25 | 2.24 | 1.68 | 0.03 | 555150.15 | 1.33 | empty_tvl |
| CHIPUSDT | IDLE | 1.49 | 4.75 | 3.3 | 0.05 | 144631.89 | 15.89 | no_map |
| ZBCNUSDT | IDLE | 1.07 | 1.92 | 1.47 | 0.01 | 199440.0 | 18.78 | n/a |
| REDUSDT | IDLE | 1.48 | 2.61 | 2.37 | 0.0 | 65454.29 | 13.88 | tvl≈2,360,052 |
| BIOUSDT | IDLE | 0.91 | 1.6 | 1.45 | 0.01 | 68932.8 | 7.97 | n/a |
| KITEUSDT | IDLE | 0.87 | 1.63 | 0.77 | 0.03 | 62017.18 | 12.37 | no_map |
| RIZEUSDT | IDLE | 1.37 | 9.66 | 3.02 | -0.08 | 45684.68 | 147.53 | no_map |
| TELUSDT | IDLE | 2.14 | 3.77 | 3.43 | -0.0 | 75889.15 | 55.71 | no_map |
| RWAINCUSDT | IDLE | 0.6 | 1.07 | 0.88 | 0.02 | 22635.26 | 23.68 | no_map |
| QNTUSDT | IDLE | 0.8 | 1.4 | 1.3 | 0.0 | 40219.75 | 3.29 | n/a |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 146.13 | 21.81 | tvl≈2,613,778,993 |
| RWAUSDT | IDLE | 0.38 | 0.75 | 0.07 | 0.01 | 57328.33 | 29.85 | no_map |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.03 | 0.02 | 42870.78 | 4.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
