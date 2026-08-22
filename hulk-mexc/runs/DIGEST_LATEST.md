# Hulk DIGEST — 2026-08-22T05:01:22Z

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
| PYTHUSDT | IDLE | 3.18 | 15.45 | 2.01 | 0.18 | 13311013.22 | 7.31 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 17.46 | 0.61 | 0.26 | 180773394.26 | 3.01 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 9.87 | 0.13 | 0.15 | 1110091.42 | 3.47 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.15 | 0.2 | 742648.28 | 8.2 | no_map |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.35 | 0.02 | 446771.17 | 11.93 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.22 | 1.07 | 0.15 | 449058.92 | 12.51 | tvl≈1,672,612,247 |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.02 | 9.0 | 0.0 | 0.08 | 203463.08 | 11.56 | n/a |
| ZBCNUSDT | IDLE | 1.54 | 4.29 | 1.4 | 0.1 | 537211.04 | 21.82 | n/a |
| QNTUSDT | IDLE | 2.72 | 9.16 | 3.84 | 0.11 | 187018.98 | 19.09 | n/a |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | no_map |
| KITEUSDT | IDLE | 1.83 | 6.62 | 0.57 | 0.14 | 68348.37 | 9.64 | no_map |
| REDUSDT | IDLE | 0.98 | 7.96 | 4.93 | 0.2 | 157871.65 | 24.1 | tvl≈2,314,909 |
| EDELUSDT | IDLE | 1.6 | 3.28 | 1.64 | -0.03 | 80245.08 | 33.31 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| RIZEUSDT | IDLE | 1.08 | 4.41 | 3.48 | 0.09 | 58604.54 | 46.02 | no_map |
| TELUSDT | IDLE | 1.98 | 5.52 | 1.04 | 0.09 | 183578.83 | 64.47 | no_map |
| RWAUSDT | IDLE | 1.66 | 3.29 | 0.24 | 0.07 | 56705.54 | 23.95 | no_map |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 21.39 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
