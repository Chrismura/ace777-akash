# Hulk DIGEST — 2026-08-19T21:19:38Z

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
| XRPUSDT | IDLE | 1.98 | 5.58 | 0.45 | 0.1 | 33900057.41 | 0.9 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.92 | 8.59 | 0.78 | 0.1 | 314604.91 | 9.06 | no_map |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.15 | 8.37 | 1.99 | -0.0 | 46610.01 | 43.14 | no_map |
| PYTHUSDT | IDLE | 2.61 | 7.83 | 0.84 | 0.1 | 289673.99 | 9.45 | tvl≈90,381,317 |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 11.59 | 6.2 | 0.02 | 108276.15 | 11.4 | tvl≈1,739,280 |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.7 | 14.81 | 0.22 | 0.2 | 80409.54 | 22.3 | no_map |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.71 | 0.82 | 0.17 | 214080.03 | 28.5 | n/a |
| WUSDT | IDLE | 1.63 | 3.48 | 0.77 | 0.07 | 218775.63 | 12.76 | tvl≈1,418,339,777 |
| BIOUSDT | IDLE | 1.41 | 6.93 | 3.58 | 0.15 | 144290.52 | 3.53 | n/a |
| CHIPUSDT | IDLE | 1.21 | 3.92 | 1.15 | 0.08 | 185895.19 | 10.61 | no_map |
| HBARUSDT | IDLE | 1.7 | 3.35 | 0.28 | 0.07 | 288132.74 | 2.82 | empty_tvl |
| KITEUSDT | IDLE | 1.37 | 2.78 | 0.4 | 0.06 | 57872.4 | 11.36 | no_map |
| RWAINCUSDT | IDLE | 1.15 | 3.23 | 2.4 | 0.03 | 17083.2 | 5.72 | no_map |
| TELUSDT | IDLE | 1.7 | 8.16 | 1.64 | 0.11 | 182500.92 | 49.41 | no_map |
| QAITUSDT | IDLE | 1.16 | 3.04 | 1.69 | 0.03 | 11273.06 | 62.16 | no_map |
| QNTUSDT | IDLE | 1.78 | 3.49 | 0.42 | 0.06 | 40190.87 | 5.08 | n/a |
| FLUIDUSDT | IDLE | 2.08 | 6.09 | 0.26 | 0.1 | 2888.06 | 43.21 | tvl≈2,416,918,092 |
| RWAUSDT | IDLE | 0.62 | 1.22 | 0.17 | 0.01 | 54426.97 | 17.29 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
