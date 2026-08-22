# Hulk DIGEST — 2026-08-22T02:27:49Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 9.45 | 0.88 | 0.15 | 6999206.69 | 1.93 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 10.44 | 0.27 | 0.17 | 154946555.15 | 1.32 | n/a |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.73 | 0.09 | 542013.62 | 1.45 | n/a |
| HBARUSDT | IDLE | 2.33 | 5.19 | 0.1 | 0.09 | 966186.24 | 3.71 | empty_tvl |
| CCUSDT | IDLE | 1.7 | 6.33 | 0.1 | 0.15 | 654427.84 | 4.35 | no_map |
| CHIPUSDT | IDLE | 2.22 | 5.07 | 0.39 | -0.01 | 474458.14 | 3.01 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.12 | 8.18 | 0.59 | 0.1 | 193282.29 | 14.76 | n/a |
| WUSDT | IDLE | 1.85 | 5.09 | 0.04 | 0.1 | 401790.91 | 12.02 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 2.48 | 5.02 | 3.04 | -0.03 | 79673.06 | 22.37 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.93 | 0.1 | 61336.72 | 28.76 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.14 | 0.17 | 156889.74 | 19.42 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.36 | 4.09 | 0.83 | 0.11 | 61882.45 | 9.02 | no_map |
| QNTUSDT | IDLE | 2.23 | 4.92 | 0.0 | 0.08 | 171093.96 | 8.95 | n/a |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9345.09 | 37.95 | no_map |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.28 | 0.04 | 178506.5 | 67.48 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.77 | tvl≈2,599,456,799 |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54972.61 | 8.18 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
