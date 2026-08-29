# Hulk DIGEST — 2026-08-29T11:07:19Z

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
| CHIPUSDT | IDLE | 2.21 | 10.29 | 6.85 | -0.04 | 1265492.27 | 4.85 | skipped_fast |
| XRPUSDT | IDLE | 0.49 | 0.93 | 0.27 | -0.03 | 40266320.33 | 2.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.3 | 2.32 | 1.87 | -0.03 | 423450.43 | 2.14 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 3.33 | 1.05 | -0.0 | 201918.5 | 9.77 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.47 | 2.37 | -0.05 | 210800.4 | 14.36 | skipped_fast |
| REDUSDT | IDLE | 1.82 | 5.6 | 0.62 | 0.08 | 71123.85 | 16.69 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.92 | 1.77 | -0.07 | 200233.55 | 8.73 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 4.55 | 4.16 | -0.12 | 91644.47 | 39.37 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.82 | 1.65 | -0.04 | 84387.68 | 3.65 | skipped_fast |
| RIZEUSDT | IDLE | 1.58 | 3.21 | 1.81 | -0.01 | 27539.16 | 58.52 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.97 | 0.28 | 0.01 | 62098.84 | 10.94 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.05 | 0.82 | -0.04 | 368590.92 | 1.34 | skipped_fast |
| QAITUSDT | IDLE | 0.45 | 4.07 | 1.73 | -0.02 | 83875.62 | 31.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.28 | 2.23 | -0.03 | 3674.22 | 99.45 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.25 | 0.75 | -0.03 | 40976.03 | 3.27 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 1.45 | 0.68 | -0.04 | 80595.28 | 40.2 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.74 | 0.66 | 0.01 | 57369.84 | 8.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 0.66 | 0.65 | -0.06 | 3665.9 | 21.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
