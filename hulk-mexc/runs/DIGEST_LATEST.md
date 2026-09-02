# Hulk DIGEST — 2026-09-02T06:33:36Z

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
| XRPUSDT | IDLE | 1.23 | 2.29 | 1.1 | -0.03 | 37564457.69 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.7 | 0.33 | -0.02 | 364092758.02 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.39 | 0.38 | -0.02 | 510545347.81 | 0.0 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 8.25 | 1.69 | 0.11 | 810574.69 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 6.75 | 5.03 | 0.08 | 871919.78 | 4.62 | skipped_fast |
| EDELUSDT | IDLE | 2.98 | 17.12 | 2.85 | 0.1 | 205145.61 | 47.39 | skipped_fast |
| WUSDT | IDLE | 2.23 | 4.28 | 1.15 | 0.02 | 428247.4 | 11.31 | skipped_fast |
| RWAINCUSDT | IDLE | 3.83 | 11.68 | 2.48 | 0.09 | 8843.11 | 118.98 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.09 | 2.21 | -0.07 | 340994.79 | 7.91 | skipped_fast |
| ZBCNUSDT | IDLE | 2.07 | 4.28 | 2.59 | -0.03 | 210084.66 | 5.51 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 9.7 | 0.31 | 0.13 | 71037.39 | 9.65 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 3.52 | 2.45 | 0.05 | 144736.49 | 13.46 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.43 | 1.17 | -0.04 | 72682.81 | 15.7 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 3.94 | 0.21 | 0.07 | 48688.89 | 7.62 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.63 | 0.66 | -0.02 | 238950.63 | 1.35 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 2.75 | 1.59 | -0.1 | 41361.67 | 78.03 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.54 | 0.47 | -0.02 | 88225.54 | 47.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 2.81 | 0.0 | -0.03 | 323.84 | 21.73 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.23 | -0.05 | 53856.49 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.7 | 0.1 | -0.01 | 36454.92 | 50.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
