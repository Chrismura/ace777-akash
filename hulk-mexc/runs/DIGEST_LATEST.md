# Hulk DIGEST — 2026-08-22T04:54:41Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 1.2 | 0.2 | 12639339.11 | 25.39 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 17.46 | 0.54 | 0.26 | 179444392.69 | 3.01 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 9.6 | 0.19 | 0.15 | 1076533.62 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.46 | 0.2 | 740096.81 | 7.39 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.5 | 0.01 | 454149.51 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.62 | 1.02 | 0.15 | 437633.96 | 12.52 | skipped_fast |
| BIOUSDT | IDLE | 2.91 | 7.36 | 0.59 | 0.07 | 200572.51 | 2.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 4.29 | 0.64 | 0.12 | 538062.59 | 20.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.55 | 0.1 | 58586.88 | 44.22 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.28 | -0.02 | 80220.07 | 33.31 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 6.54 | 0.05 | 0.15 | 68151.68 | 8.74 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 8.56 | 4.03 | 0.1 | 182445.49 | 27.95 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.41 | 0.21 | 158170.46 | 19.08 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9533.0 | 103.06 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.35 | 0.1 | 183402.65 | 49.53 | skipped_fast |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.24 | 0.06 | 56535.68 | 23.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 21.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
