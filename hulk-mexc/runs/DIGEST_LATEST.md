# Hulk DIGEST — 2026-09-01T16:25:44Z

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
| XRPUSDT | IDLE | 1.18 | 2.1 | 1.71 | -0.0 | 30380433.65 | 2.93 | n/a |
| ETHUSDT | IDLE | 0.88 | 1.54 | 1.41 | -0.01 | 289138700.91 | 0.41 | no_map |
| BTCUSDT | IDLE | 0.68 | 1.18 | 1.14 | -0.01 | 520354832.75 | 0.0 | no_map |
| CHIPUSDT | IDLE | 3.47 | 14.78 | 2.44 | 0.12 | 488348.77 | 9.17 | no_map |
| PYTHUSDT | IDLE | 1.64 | 2.96 | 2.07 | 0.07 | 619700.84 | 2.0 | tvl≈112,789,076 |
| ZBCNUSDT | IDLE | 3.49 | 6.8 | 1.16 | 0.07 | 225035.55 | 38.96 | n/a |
| CCUSDT | IDLE | 2.25 | 4.27 | 4.07 | -0.02 | 396102.04 | 6.93 | no_map |
| WUSDT | IDLE | 2.33 | 4.35 | 2.01 | 0.06 | 279975.8 | 14.62 | tvl≈1,536,961,838 |
| KITEUSDT | IDLE | 2.7 | 5.31 | 0.56 | 0.05 | 62101.61 | 12.96 | no_map |
| REDUSDT | IDLE | 2.2 | 4.51 | 1.12 | 0.06 | 66778.76 | 11.61 | tvl≈2,031,843 |
| RIZEUSDT | IDLE | 2.05 | 4.79 | 2.27 | -0.07 | 43696.36 | 17.47 | no_map |
| EDELUSDT | IDLE | 0.93 | 6.17 | 4.38 | -0.07 | 173187.91 | 17.57 | no_map |
| RWAINCUSDT | IDLE | 1.64 | 2.86 | 2.78 | -0.03 | 5922.09 | 23.72 | no_map |
| BIOUSDT | IDLE | 1.24 | 2.26 | 1.48 | -0.02 | 67246.55 | 3.86 | n/a |
| QNTUSDT | IDLE | 2.17 | 4.21 | 0.87 | 0.05 | 37483.28 | 7.85 | n/a |
| HBARUSDT | IDLE | 1.05 | 1.83 | 1.76 | 0.01 | 231837.49 | 1.35 | empty_tvl |
| TELUSDT | IDLE | 1.22 | 2.18 | 1.67 | 0.01 | 96952.75 | 35.17 | no_map |
| RWAUSDT | IDLE | 1.09 | 2.57 | 1.44 | -0.01 | 61132.29 | 7.7 | no_map |
| MNSRYUSDT | IDLE | 0.61 | 1.13 | 0.55 | -0.0 | 32098.69 | 21.75 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.0 | 385.35 | 22.08 | tvl≈2,602,518,957 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
