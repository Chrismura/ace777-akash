# Hulk DIGEST — 2026-08-22T12:09:20Z

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
| PYTHUSDT | IDLE | 1.74 | 7.83 | 5.09 | 0.01 | 51611386.78 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.23 | 0.11 | 215223030.27 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.4 | 0.03 | 1256808.35 | 5.15 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 8.38 | 4.94 | 0.13 | 775018.43 | 6.84 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.55 | 0.02 | 578556.42 | 14.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 5.77 | 4.2 | -0.04 | 378103.97 | 64.95 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.32 | -0.1 | 613424.81 | 6.69 | skipped_fast |
| KITEUSDT | IDLE | 2.58 | 6.24 | 0.06 | 0.05 | 82681.92 | 8.8 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.03 | 78014.3 | 22.73 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 5.65 | 1.48 | -0.02 | 240641.01 | 3.19 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2385.65 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 5.61 | 4.14 | -0.02 | 164792.91 | 37.36 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.88 | 0.02 | 153585.37 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.52 | 0.01 | 187417.06 | 6.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.32 | -0.05 | 47960.72 | 20.52 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57793.04 | 16.3 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
