# Hulk DIGEST — 2026-09-14T18:35:23Z

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
| XRPUSDT | IDLE | 2.37 | 5.52 | 0.11 | 0.07 | 54110501.53 | 1.37 | skipped_fast |
| BTCUSDT | IDLE | 1.14 | 2.28 | 0.05 | 0.02 | 511739688.0 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.11 | 2.21 | 0.03 | 0.01 | 364991572.63 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.3 | 4.48 | 0.79 | -0.01 | 460372.78 | 1.77 | skipped_fast |
| REDUSDT | IDLE | 2.47 | 8.59 | 5.69 | 0.07 | 183616.85 | 18.6 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 6.39 | 4.16 | 0.1 | 267060.0 | 20.71 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 4.25 | 1.89 | -0.03 | 90262.74 | 19.03 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.14 | 0.24 | 0.01 | 292887.62 | 9.26 | skipped_fast |
| WUSDT | IDLE | 1.42 | 2.84 | 0.0 | -0.01 | 212818.27 | 12.91 | skipped_fast |
| BIOUSDT | IDLE | 1.87 | 3.73 | 0.04 | 0.02 | 89521.94 | 3.82 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 2.81 | 0.13 | 0.0 | 209348.43 | 18.87 | skipped_fast |
| RIZEUSDT | IDLE | 0.98 | 10.72 | 9.14 | -0.03 | 55369.25 | 67.97 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 3.03 | 0.11 | 0.03 | 313716.7 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.84 | 1.03 | 0.03 | 10163.74 | 5.47 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.06 | 0.69 | -0.01 | 61454.4 | 10.37 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 1.97 | 1.05 | -0.02 | 41674.14 | 7.79 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.54 | 0.09 | 0.03 | 1029.98 | 21.51 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.95 | 0.06 | 0.02 | 92346.1 | 49.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.79 | 1.58 | 0.06 | 0.01 | 29429.11 | 45.55 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | 0.0 | 55176.69 | 29.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
