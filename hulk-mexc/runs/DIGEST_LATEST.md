# Hulk DIGEST — 2026-09-02T06:32:59Z

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
| XRPUSDT | IDLE | 1.23 | 2.29 | 1.09 | -0.03 | 37550651.47 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.7 | 0.31 | -0.02 | 364065339.76 | 0.41 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.39 | 0.37 | -0.02 | 510405327.2 | 0.03 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 8.25 | 1.42 | 0.11 | 810329.09 | 1.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 6.75 | 5.03 | 0.08 | 872073.66 | 2.31 | skipped_fast |
| EDELUSDT | IDLE | 2.98 | 17.12 | 2.92 | 0.09 | 205190.21 | 7.92 | skipped_fast |
| WUSDT | IDLE | 2.22 | 4.28 | 1.13 | 0.02 | 428198.66 | 22.61 | skipped_fast |
| RWAINCUSDT | IDLE | 3.85 | 11.68 | 2.91 | 0.09 | 8843.11 | 54.26 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.09 | 2.22 | -0.07 | 340966.91 | 8.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.07 | 4.28 | 2.59 | -0.03 | 210061.33 | 4.96 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 9.7 | 0.56 | 0.13 | 70991.48 | 17.84 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 3.52 | 2.52 | 0.05 | 144664.49 | 19.73 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.43 | 1.17 | -0.04 | 72901.75 | 3.93 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 3.94 | 0.21 | 0.06 | 48703.87 | 6.1 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.63 | 0.67 | -0.01 | 238932.23 | 1.35 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 2.75 | 1.59 | -0.1 | 41361.67 | 78.03 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.54 | 0.47 | -0.02 | 88222.68 | 41.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 2.81 | 0.0 | -0.03 | 323.84 | 21.72 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.54 | 0.15 | -0.05 | 53882.45 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.7 | 0.1 | -0.01 | 36465.72 | 50.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
