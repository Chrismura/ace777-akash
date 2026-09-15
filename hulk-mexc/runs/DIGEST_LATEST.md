# Hulk DIGEST — 2026-09-15T10:45:26Z

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
| XRPUSDT | IDLE | 1.07 | 2.01 | 0.93 | 0.0 | 72588676.75 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.4 | 0.85 | -0.02 | 454056026.87 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.33 | 0.89 | -0.01 | 548098720.01 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 14.63 | 9.37 | 0.27 | 432253.91 | 38.35 | skipped_fast |
| ZBCNUSDT | IDLE | 2.38 | 4.56 | 1.37 | 0.04 | 215129.11 | 8.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 2.93 | 2.61 | -0.03 | 284690.13 | 1.85 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 21.1 | 0.91 | -0.03 | 50953.82 | 99.27 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.7 | 0.8 | -0.0 | 365715.21 | 2.1 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 7.83 | 4.71 | -0.01 | 123171.27 | 16.14 | skipped_fast |
| WUSDT | IDLE | 1.65 | 2.91 | 2.6 | -0.05 | 155597.53 | 12.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 3.61 | 2.11 | -0.02 | 79544.14 | 19.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.85 | 2.28 | -0.01 | 7382.94 | 11.16 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.11 | 1.95 | -0.02 | 87716.89 | 7.94 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.12 | 0.69 | 0.01 | 374405.57 | 1.29 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.13 | 0.83 | -0.0 | 63791.71 | 14.06 | skipped_fast |
| FLUIDUSDT | IDLE | 2.41 | 4.22 | 4.05 | -0.03 | 2129.43 | 21.6 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 2.81 | 2.25 | -0.02 | 45587.87 | 4.76 | skipped_fast |
| TELUSDT | IDLE | 1.48 | 3.59 | 2.84 | -0.02 | 93102.36 | 44.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.88 | 0.54 | 0.01 | 32788.31 | 29.16 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.45 | 0.3 | -0.01 | 53994.67 | 14.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
