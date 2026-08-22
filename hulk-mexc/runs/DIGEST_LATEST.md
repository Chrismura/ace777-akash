# Hulk DIGEST — 2026-08-22T02:45:34Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.58 | 10.77 | 0.02 | 0.17 | 7220175.04 | 3.78 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 12.02 | 0.25 | 0.19 | 157034986.52 | 3.26 | n/a |
| HBARUSDT | IDLE | 2.45 | 5.91 | 0.0 | 0.09 | 981454.42 | 1.23 | empty_tvl |
| CCUSDT | IDLE | 1.94 | 8.19 | 0.0 | 0.16 | 655507.64 | 0.85 | no_map |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.82 | 0.11 | 540577.51 | 41.72 | n/a |
| CHIPUSDT | IDLE | 2.29 | 5.26 | 0.15 | -0.02 | 456739.38 | 8.99 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.19 | 8.18 | 1.91 | 0.09 | 192918.15 | 5.97 | n/a |
| WUSDT | IDLE | 1.98 | 5.85 | 0.05 | 0.11 | 413608.35 | 12.93 | tvl≈1,646,654,250 |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.0 | 0.1 | 61325.45 | 45.71 | no_map |
| EDELUSDT | IDLE | 2.47 | 5.02 | 2.93 | -0.04 | 79912.94 | 77.99 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.8 | 0.19 | 158033.06 | 8.78 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9400.35 | 5.43 | no_map |
| QNTUSDT | IDLE | 2.33 | 5.48 | 0.18 | 0.08 | 172660.21 | 8.93 | n/a |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.13 | 0.12 | 62496.37 | 11.66 | no_map |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.18 | 0.06 | 174210.83 | 67.31 | no_map |
| RWAUSDT | IDLE | 1.42 | 2.83 | 0.0 | 0.05 | 55859.24 | 24.36 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.08 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
