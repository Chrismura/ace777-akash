# Hulk DIGEST — 2026-09-18T02:18:07Z

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
| XRPUSDT | IDLE | 0.81 | 1.58 | 0.22 | 0.01 | 34987266.97 | 2.3 | n/a |
| ETHUSDT | IDLE | 0.51 | 1.0 | 0.13 | 0.02 | 283666490.25 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.36 | 0.71 | 0.03 | 0.01 | 409957792.52 | 0.0 | no_map |
| CCUSDT | IDLE | 2.82 | 7.38 | 0.0 | 0.11 | 497424.91 | 11.2 | no_map |
| PYTHUSDT | IDLE | 2.15 | 5.29 | 0.65 | 0.09 | 569628.31 | 1.73 | tvl≈127,354,141 |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 26.52 | 1.91 | -0.11 | 279570.71 | 47.73 | no_map |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.16 | 12.39 | 0.74 | 0.13 | 194103.69 | 19.39 | no_map |
| REDUSDT | IDLE | 3.23 | 6.43 | 0.23 | 0.05 | 67249.66 | 16.77 | tvl≈2,362,540 |
| WUSDT | IDLE | 0.98 | 2.47 | 0.82 | 0.09 | 317686.68 | 17.05 | tvl≈1,480,477,875 |
| HBARUSDT | IDLE | 1.11 | 2.18 | 0.25 | 0.02 | 505676.16 | 2.65 | empty_tvl |
| BIOUSDT | IDLE | 1.57 | 3.09 | 0.31 | 0.01 | 68891.6 | 3.91 | n/a |
| KITEUSDT | IDLE | 1.54 | 2.93 | 1.05 | 0.01 | 61583.04 | 10.29 | no_map |
| ZBCNUSDT | IDLE | 0.81 | 1.52 | 0.64 | 0.0 | 207290.0 | 35.29 | n/a |
| RWAINCUSDT | IDLE | 0.88 | 1.56 | 1.36 | -0.03 | 14193.01 | 24.11 | no_map |
| TELUSDT | IDLE | 1.8 | 3.28 | 2.07 | -0.02 | 73673.92 | 56.46 | no_map |
| QNTUSDT | IDLE | 1.1 | 2.17 | 0.18 | 0.02 | 40795.92 | 11.29 | n/a |
| RIZEUSDT | IDLE | 0.54 | 2.58 | 1.72 | -0.05 | 39460.75 | 148.87 | no_map |
| MNSRYUSDT | IDLE | 0.7 | 1.35 | 0.36 | 0.02 | 43730.38 | 27.79 | no_map |
| RWAUSDT | IDLE | 0.51 | 0.98 | 0.3 | 0.0 | 58349.61 | 37.33 | no_map |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.39 | 0.02 | 148.34 | 21.45 | tvl≈2,608,674,879 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
