# Hulk DIGEST — 2026-08-22T04:19:22Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 13.13 | 0.49 | 0.2 | 10536241.12 | 5.51 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 12.22 | 0.61 | 0.21 | 167866484.42 | 1.89 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 11.56 | 0.71 | 0.21 | 729420.51 | 6.52 | no_map |
| HBARUSDT | IDLE | 2.26 | 7.14 | 0.43 | 0.12 | 1017612.98 | 2.38 | empty_tvl |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.35 | 0.01 | 441360.38 | 11.91 | no_map |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.32 | 0.07 | 200025.59 | 6.0 | n/a |
| WUSDT | IDLE | 1.95 | 7.18 | 0.35 | 0.14 | 431255.53 | 16.48 | tvl≈1,672,612,247 |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.41 | 0.12 | 535620.38 | 22.37 | n/a |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.05 | 80181.41 | 22.5 | no_map |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.88 | 0.1 | 59156.84 | 27.37 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.95 | 0.2 | 159868.55 | 11.99 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.64 | 0.13 | 67620.26 | 11.53 | no_map |
| RWAINCUSDT | IDLE | 2.01 | 3.6 | 2.74 | 0.01 | 9375.63 | 59.44 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.55 | 3.8 | 0.66 | 0.09 | 178568.59 | 8.91 | n/a |
| TELUSDT | IDLE | 1.19 | 2.76 | 0.81 | 0.07 | 174910.91 | 30.61 | no_map |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56318.94 | 16.05 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.06 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
