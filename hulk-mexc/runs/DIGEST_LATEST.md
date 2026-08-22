# Hulk DIGEST — 2026-08-22T03:06:08Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 9.55 | 1.13 | 0.15 | 7466307.94 | 3.82 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.15 | 0.64 | 0.2 | 160100822.09 | 5.18 | n/a |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.34 | 0.1 | 996190.2 | 1.22 | empty_tvl |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.41 | 0.19 | 666040.59 | 5.04 | no_map |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.29 | 0.07 | 195323.53 | 3.0 | n/a |
| CHIPUSDT | IDLE | 1.94 | 4.28 | 0.42 | -0.01 | 445726.35 | 2.99 | no_map |
| WUSDT | IDLE | 1.77 | 5.61 | 0.13 | 0.12 | 417814.14 | 13.79 | tvl≈1,646,654,250 |
| ZBCNUSDT | IDLE | 1.45 | 5.16 | 2.55 | 0.12 | 540171.36 | 55.01 | n/a |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.41 | 0.09 | 61376.41 | 44.22 | no_map |
| EDELUSDT | IDLE | 1.9 | 3.83 | 2.39 | -0.03 | 79885.63 | 22.22 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.29 | 0.2 | 157977.48 | 10.32 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 27.09 | no_map |
| KITEUSDT | IDLE | 1.3 | 4.03 | 0.08 | 0.12 | 63764.82 | 11.63 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3931.36 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.21 | 0.09 | 172784.73 | 5.95 | n/a |
| TELUSDT | IDLE | 0.81 | 1.88 | 0.77 | 0.06 | 172937.48 | 30.91 | no_map |
| RWAUSDT | IDLE | 1.18 | 2.31 | 0.32 | 0.05 | 56145.37 | 24.24 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.67 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
