# Hulk DIGEST — 2026-08-22T03:14:42Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 10.96 | 0.47 | 0.17 | 7622779.07 | 16.86 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 11.43 | 0.29 | 0.2 | 160980583.67 | 3.86 | n/a |
| HBARUSDT | IDLE | 2.19 | 5.64 | 0.0 | 0.1 | 1002256.29 | 6.06 | empty_tvl |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.6 | 0.17 | 679266.3 | 7.64 | no_map |
| BIOUSDT | IDLE | 3.03 | 7.36 | 2.7 | 0.06 | 196093.77 | 3.01 | n/a |
| CHIPUSDT | IDLE | 1.96 | 4.28 | 0.8 | -0.01 | 448800.09 | 2.99 | no_map |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.67 | 0.12 | 541089.23 | 29.44 | n/a |
| WUSDT | IDLE | 1.79 | 5.61 | 0.63 | 0.12 | 418160.42 | 13.85 | tvl≈1,646,654,250 |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.34 | 0.1 | 59511.31 | 44.22 | no_map |
| EDELUSDT | IDLE | 1.94 | 3.83 | 3.04 | -0.03 | 80045.99 | 33.61 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.85 | 0.19 | 158065.21 | 10.27 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 21.62 | no_map |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.35 | 0.12 | 67665.3 | 11.63 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3813.17 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.22 | 0.08 | 174151.82 | 7.44 | n/a |
| RWAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.05 | 56241.73 | 16.1 | no_map |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.31 | 0.07 | 173380.38 | 56.34 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.29 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
