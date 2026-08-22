# Hulk DIGEST — 2026-08-22T04:52:51Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 1.11 | 0.2 | 12427688.03 | 7.24 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 17.08 | 0.35 | 0.27 | 178824950.24 | 4.82 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 9.21 | 0.01 | 0.14 | 1074513.05 | 1.16 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.3 | 0.2 | 739859.14 | 10.67 | no_map |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.65 | 0.01 | 454075.84 | 2.99 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.62 | 0.79 | 0.15 | 436610.96 | 9.61 | tvl≈1,672,612,247 |
| BIOUSDT | IDLE | 2.92 | 7.36 | 0.85 | 0.06 | 200540.75 | 5.91 | n/a |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.01 | 0.11 | 537995.6 | 22.75 | n/a |
| QNTUSDT | IDLE | 2.42 | 8.56 | 4.02 | 0.1 | 182343.29 | 5.88 | n/a |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.09 | 58589.98 | 37.4 | no_map |
| EDELUSDT | IDLE | 2.02 | 4.07 | 2.61 | -0.03 | 80220.03 | 33.31 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.3 | 0.21 | 158160.35 | 11.12 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.72 | 6.49 | 0.0 | 0.14 | 67966.97 | 16.61 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 92.27 | no_map |
| TELUSDT | IDLE | 1.97 | 5.52 | 0.74 | 0.1 | 183328.1 | 34.8 | no_map |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.16 | 0.06 | 56512.63 | 23.99 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.11 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
