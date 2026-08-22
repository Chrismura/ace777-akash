# Hulk DIGEST — 2026-08-22T02:36:16Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.61 | 10.52 | 1.4 | 0.14 | 7121681.79 | 9.62 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 12.02 | 0.6 | 0.18 | 156044276.0 | 1.96 | n/a |
| HBARUSDT | IDLE | 2.44 | 5.62 | 0.65 | 0.09 | 973276.93 | 12.38 | empty_tvl |
| ZBCNUSDT | IDLE | 2.46 | 9.63 | 2.06 | 0.1 | 543409.4 | 21.13 | n/a |
| CCUSDT | IDLE | 1.76 | 6.75 | 0.09 | 0.15 | 654022.44 | 9.53 | no_map |
| CHIPUSDT | IDLE | 2.32 | 5.26 | 0.69 | -0.0 | 457445.59 | 12.07 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.16 | 8.18 | 1.35 | 0.09 | 193549.43 | 11.9 | n/a |
| WUSDT | IDLE | 1.95 | 5.62 | 0.3 | 0.1 | 403595.34 | 11.98 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 2.44 | 5.02 | 2.5 | -0.04 | 79668.04 | 33.35 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.2 | 0.1 | 61497.29 | 45.81 | no_map |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.92 | 0.17 | 157822.32 | 19.42 | tvl≈2,314,909 |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.31 | 0.08 | 172631.44 | 10.42 | n/a |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.47 | 0.12 | 62407.98 | 9.89 | no_map |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9324.96 | 43.38 | no_map |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.23 | 0.05 | 176327.8 | 56.95 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 20.42 | tvl≈2,599,456,799 |
| RWAUSDT | IDLE | 1.14 | 2.25 | 0.16 | 0.04 | 55167.2 | 32.65 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
