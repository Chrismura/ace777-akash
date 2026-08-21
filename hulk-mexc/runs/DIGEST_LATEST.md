# Hulk DIGEST — 2026-08-21T20:38:47Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5538899.84 | 2.11 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.37 | 0.1 | 128965437.05 | 3.64 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.62 | 0.17 | 153971.92 | 12.96 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.56 | 0.11 | 478677.69 | 66.02 | n/a |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.36 | 0.09 | 638677.1 | 4.6 | no_map |
| HBARUSDT | IDLE | 1.73 | 3.23 | 2.0 | 0.05 | 808361.89 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.46 | 0.08 | 514905.09 | 3.09 | no_map |
| WUSDT | IDLE | 2.09 | 3.92 | 1.69 | 0.06 | 368468.37 | 11.63 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.04 | 0.01 | 189554.32 | 3.16 | n/a |
| EDELUSDT | IDLE | 2.79 | 5.01 | 4.23 | -0.05 | 81393.99 | 22.65 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10892.53 | 26.77 | no_map |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.62 | 0.02 | 56289.18 | 47.09 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.6 | 0.1 | 60825.19 | 9.32 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | no_map |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 183215.71 | 26.83 | no_map |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.75 | 0.04 | 59923.55 | 7.83 | n/a |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53933.63 | 8.32 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 45.98 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
