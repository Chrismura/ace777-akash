# Hulk DIGEST — 2026-09-20T08:02:04Z

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
| XRPUSDT | IDLE | 0.66 | 1.27 | 0.32 | -0.02 | 54221309.62 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.03 | 0.5 | -0.02 | 260858799.88 | 0.31 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.6 | 0.33 | -0.01 | 503534443.81 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.53 | 4.54 | 3.46 | 0.02 | 514326.22 | 5.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.08 | 1.93 | 1.52 | -0.02 | 693535.35 | 6.85 | skipped_fast |
| HBARUSDT | IDLE | 1.92 | 3.67 | 1.07 | 0.04 | 768300.16 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.88 | 2.57 | -0.05 | 350311.0 | 5.77 | skipped_fast |
| REDUSDT | IDLE | 2.66 | 5.23 | 0.66 | 0.04 | 89491.34 | 15.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 7.45 | 3.38 | -0.07 | 34865.78 | 50.58 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 3.32 | 1.23 | 0.05 | 224521.6 | 13.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 3.11 | 1.79 | -0.07 | 103958.82 | 19.17 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 3.83 | 0.61 | -0.08 | 81027.7 | 25.54 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.78 | 1.5 | 0.0 | 89197.69 | 3.7 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 2.16 | 0.33 | -0.01 | 74762.82 | 18.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.85 | 1.35 | -0.04 | 10049.32 | 23.77 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.22 | 1.96 | 0.01 | 57061.57 | 4.69 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.37 | 2.07 | -0.01 | 8031.79 | 21.87 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.65 | 1.02 | -0.07 | 103814.43 | 54.83 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.12 | 0.74 | -0.01 | 52408.83 | 22.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.61 | -0.01 | 33118.47 | 31.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
