# Hulk DIGEST — 2026-09-02T03:30:50Z

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
| XRPUSDT | IDLE | 1.16 | 2.29 | 0.18 | -0.02 | 37733143.79 | 1.48 | n/a |
| ETHUSDT | IDLE | 0.91 | 1.78 | 0.27 | -0.02 | 368334349.75 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.71 | 1.39 | 0.16 | -0.01 | 534626880.0 | 0.0 | no_map |
| CHIPUSDT | IDLE | 1.28 | 6.05 | 4.14 | 0.12 | 835088.53 | 4.62 | no_map |
| PYTHUSDT | IDLE | 2.09 | 6.9 | 0.18 | 0.08 | 657322.22 | 18.33 | tvl≈118,462,197 |
| WUSDT | IDLE | 1.87 | 3.5 | 1.57 | 0.03 | 417281.72 | 13.52 | tvl≈1,511,415,282 |
| CCUSDT | IDLE | 1.25 | 3.09 | 0.12 | -0.06 | 326717.11 | 6.89 | no_map |
| REDUSDT | IDLE | 1.87 | 4.8 | 4.32 | 0.05 | 143723.19 | 13.48 | tvl≈2,106,717 |
| ZBCNUSDT | IDLE | 1.91 | 4.28 | 0.31 | -0.01 | 193152.95 | 42.55 | n/a |
| RIZEUSDT | IDLE | 2.34 | 6.78 | 5.27 | -0.06 | 42653.19 | 59.48 | no_map |
| EDELUSDT | IDLE | 1.02 | 9.32 | 1.57 | -0.0 | 175781.29 | 26.44 | no_map |
| RWAINCUSDT | IDLE | 2.27 | 4.54 | 0.0 | 0.02 | 5618.96 | 33.8 | no_map |
| KITEUSDT | IDLE | 1.68 | 3.33 | 0.24 | 0.06 | 69008.53 | 10.36 | no_map |
| BIOUSDT | IDLE | 1.23 | 2.43 | 0.23 | -0.03 | 69849.7 | 3.89 | n/a |
| HBARUSDT | IDLE | 0.82 | 1.61 | 0.26 | 0.0 | 257803.72 | 1.35 | empty_tvl |
| TELUSDT | IDLE | 1.79 | 3.54 | 0.29 | -0.0 | 90338.47 | 47.28 | no_map |
| QNTUSDT | IDLE | 1.06 | 2.1 | 0.12 | 0.05 | 47885.89 | 4.65 | n/a |
| FLUIDUSDT | IDLE | 1.07 | 2.04 | 0.7 | -0.04 | 319.05 | 21.78 | tvl≈2,564,747,181 |
| RWAUSDT | IDLE | 0.4 | 0.93 | 0.54 | -0.03 | 57400.13 | 7.7 | no_map |
| MNSRYUSDT | IDLE | 0.37 | 0.7 | 0.21 | -0.02 | 36101.61 | 28.86 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
