# Hulk DIGEST — 2026-09-01T17:23:51Z

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
| XRPUSDT | IDLE | 1.02 | 1.89 | 1.03 | -0.01 | 30861128.11 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.59 | 0.96 | -0.01 | 291828422.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.41 | 1.03 | -0.01 | 519450758.89 | 0.19 | skipped_fast |
| CHIPUSDT | IDLE | 3.44 | 14.28 | 4.77 | 0.1 | 500501.89 | 2.36 | skipped_fast |
| ZBCNUSDT | IDLE | 3.63 | 6.8 | 3.13 | 0.03 | 217241.54 | 22.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.96 | 0.72 | 0.05 | 633722.83 | 1.97 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 4.86 | 3.34 | -0.03 | 416304.55 | 10.45 | skipped_fast |
| WUSDT | IDLE | 2.22 | 4.35 | 0.54 | 0.07 | 283945.98 | 11.32 | skipped_fast |
| REDUSDT | IDLE | 2.35 | 5.3 | 1.23 | 0.06 | 74870.47 | 11.55 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 5.19 | 4.2 | -0.06 | 43545.76 | 15.29 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 3.97 | 1.22 | 0.04 | 70213.51 | 12.23 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.26 | 1.71 | -0.02 | 67154.48 | 3.87 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 5.12 | 3.59 | -0.06 | 172599.98 | 70.67 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.05 | 1.32 | 0.01 | 231265.53 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.91 | 3.79 | 0.2 | 0.04 | 43160.25 | 9.38 | skipped_fast |
| RWAINCUSDT | IDLE | 1.51 | 2.86 | 1.1 | -0.03 | 6195.38 | 122.06 | skipped_fast |
| TELUSDT | IDLE | 1.07 | 1.89 | 1.68 | 0.01 | 97286.93 | 41.19 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.62 | 1.44 | -0.02 | 60648.37 | 15.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.13 | 0.77 | -0.01 | 32679.63 | 39.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 266.03 | 21.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
