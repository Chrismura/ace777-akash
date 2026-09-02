# Hulk DIGEST — 2026-09-02T05:32:16Z

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
| XRPUSDT | IDLE | 1.17 | 2.29 | 0.39 | -0.02 | 38023800.57 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.66 | 0.1 | -0.02 | 367113843.61 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.39 | 0.13 | -0.02 | 518362176.03 | 0.0 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.23 | 8.67 | 1.98 | 0.1 | 756338.4 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 3.99 | 1.49 | 0.12 | 852424.3 | 2.29 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.98 | 0.13 | 0.02 | 425972.96 | 15.46 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.09 | 1.47 | -0.07 | 337113.79 | 9.6 | skipped_fast |
| REDUSDT | IDLE | 2.07 | 5.32 | 4.13 | 0.04 | 143421.28 | 14.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 4.28 | 1.08 | -0.01 | 204397.19 | 29.35 | skipped_fast |
| RWAINCUSDT | IDLE | 2.64 | 5.01 | 1.8 | 0.03 | 5925.98 | 11.41 | skipped_fast |
| KITEUSDT | IDLE | 2.06 | 6.07 | 0.02 | 0.09 | 69120.37 | 25.27 | skipped_fast |
| RIZEUSDT | IDLE | 2.13 | 6.26 | 4.11 | -0.09 | 42923.39 | 45.48 | skipped_fast |
| EDELUSDT | IDLE | 0.98 | 8.88 | 1.74 | -0.03 | 183738.62 | 17.68 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.43 | 0.66 | -0.04 | 71295.27 | 3.91 | skipped_fast |
| TELUSDT | IDLE | 1.79 | 3.54 | 0.24 | -0.02 | 89616.97 | 23.63 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.63 | 0.04 | -0.01 | 265173.79 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 2.21 | 0.0 | 0.05 | 48274.16 | 6.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.53 | 0.09 | -0.03 | 322.16 | 21.72 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.77 | 0.46 | -0.07 | 56268.8 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.04 | -0.02 | 36336.48 | 53.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
