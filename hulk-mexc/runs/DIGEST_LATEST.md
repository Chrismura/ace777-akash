# Hulk DIGEST — 2026-08-22T04:12:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 13.11 | 0.07 | 0.2 | 10220662.76 | 3.66 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.22 | 1.24 | 0.2 | 166940654.92 | 3.17 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 11.56 | 0.65 | 0.22 | 721471.13 | 13.02 | no_map |
| HBARUSDT | IDLE | 2.09 | 6.07 | 0.0 | 0.11 | 1009011.15 | 2.39 | empty_tvl |
| CHIPUSDT | IDLE | 2.87 | 5.36 | 2.47 | -0.0 | 458979.39 | 6.03 | no_map |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.52 | 0.07 | 200139.9 | 3.01 | n/a |
| WUSDT | IDLE | 1.97 | 7.18 | 0.79 | 0.14 | 428913.55 | 12.65 | tvl≈1,672,612,247 |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.41 | 0.13 | 535931.92 | 21.89 | n/a |
| EDELUSDT | IDLE | 2.07 | 4.07 | 3.37 | -0.04 | 80385.22 | 22.47 | no_map |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.1 | 59138.74 | 44.52 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.85 | 0.21 | 157878.36 | 10.27 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.33 | 0.13 | 67530.41 | 12.38 | no_map |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.22 | 0.01 | 9433.64 | 64.86 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.62 | 0.09 | 178592.16 | 5.94 | n/a |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56356.66 | 32.08 | no_map |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.56 | 0.07 | 173875.38 | 40.9 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 19.53 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
