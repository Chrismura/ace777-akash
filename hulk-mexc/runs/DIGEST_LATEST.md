# Hulk DIGEST — 2026-08-22T04:00:14Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.41 | 0.17 | 9259282.47 | 3.75 | tvl≈112,886,663 |
| XRPUSDT | IDLE | 2.49 | 14.16 | 2.02 | 0.19 | 166178911.75 | 3.19 | n/a |
| HBARUSDT | IDLE | 2.42 | 6.93 | 0.83 | 0.1 | 1014410.79 | 1.21 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.39 | 0.48 | 0.2 | 701958.53 | 10.79 | no_map |
| CHIPUSDT | IDLE | 2.52 | 5.36 | 1.85 | -0.02 | 458836.6 | 3.0 | no_map |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 199180.56 | 3.0 | n/a |
| ZBCNUSDT | IDLE | 1.47 | 5.37 | 1.79 | 0.13 | 537624.04 | 22.92 | n/a |
| WUSDT | IDLE | 1.89 | 6.27 | 0.58 | 0.13 | 425459.76 | 9.84 | tvl≈1,672,612,247 |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80627.46 | 22.47 | no_map |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.44 | 0.1 | 59311.3 | 46.02 | no_map |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.61 | 0.23 | 157698.19 | 10.14 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.28 | 0.13 | 67510.95 | 12.38 | no_map |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.6 | 0.09 | 178542.81 | 11.87 | n/a |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56346.16 | 16.04 | no_map |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.36 | 0.07 | 174191.53 | 35.76 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.24 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
