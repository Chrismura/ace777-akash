# Hulk DIGEST — 2026-08-22T04:55:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 0.97 | 0.2 | 12780995.23 | 3.62 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 17.46 | 0.86 | 0.26 | 179788188.69 | 5.43 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 9.63 | 0.2 | 0.15 | 1077150.45 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.18 | 0.2 | 740273.54 | 6.55 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.41 | 0.01 | 454149.51 | 5.97 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.62 | 0.68 | 0.15 | 446399.59 | 14.39 | skipped_fast |
| BIOUSDT | IDLE | 2.92 | 7.8 | 0.0 | 0.07 | 200832.62 | 14.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 4.29 | 0.66 | 0.12 | 538143.3 | 17.95 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 8.56 | 3.96 | 0.1 | 182956.84 | 10.28 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.28 | -0.02 | 80245.05 | 33.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 7.71 | 4.36 | 0.1 | 58580.16 | 44.22 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 6.54 | 0.03 | 0.15 | 68211.4 | 9.61 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.31 | 0.21 | 158090.12 | 11.92 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.35 | 0.1 | 183402.65 | 14.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9533.0 | 92.17 | skipped_fast |
| RWAUSDT | IDLE | 1.57 | 3.13 | 0.08 | 0.06 | 56547.79 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 17.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
