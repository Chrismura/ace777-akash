# Hulk DIGEST — 2026-08-22T01:22:39Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 10.28 | 0.06 | 0.16 | 6683511.66 | 3.89 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.46 | 0.15 | 149974269.41 | 2.71 | n/a |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.8 | 0.08 | 955236.24 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.85 | 0.1 | 546444.47 | 20.34 | n/a |
| CCUSDT | IDLE | 1.78 | 7.28 | 0.26 | 0.16 | 659730.28 | 6.12 | no_map |
| WUSDT | IDLE | 2.72 | 6.65 | 0.96 | 0.09 | 392100.51 | 10.2 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.25 | -0.0 | 519304.19 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.82 | 0.04 | 186583.82 | 6.15 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79585.27 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.21 | 0.11 | 60573.53 | 45.81 | no_map |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.51 | 0.18 | 159142.82 | 9.54 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.87 | 0.07 | 170252.84 | 3.01 | n/a |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181001.12 | 36.09 | no_map |
| KITEUSDT | IDLE | 1.5 | 4.63 | 0.28 | 0.12 | 60814.12 | 9.02 | no_map |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.02 | 9586.1 | 16.16 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.8 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 55112.09 | 16.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
