# Hulk DIGEST — 2026-08-22T11:40:06Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.86 | 0.01 | 51616748.7 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.49 | 0.08 | 216892311.97 | 2.69 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.54 | 0.13 | 792421.82 | 9.4 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.32 | 0.01 | 1258639.93 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.7 | 0.02 | 584237.39 | 9.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.25 | -0.03 | 388801.68 | 24.72 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.68 | -0.1 | 636348.18 | 6.71 | skipped_fast |
| EDELUSDT | IDLE | 2.73 | 4.93 | 3.49 | -0.03 | 79089.22 | 56.47 | skipped_fast |
| KITEUSDT | IDLE | 2.31 | 5.59 | 0.0 | 0.05 | 79543.91 | 36.36 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.23 | -0.04 | 243530.17 | 6.43 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.66 | -0.03 | 167268.82 | 37.5 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2485.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 3.98 | 0.04 | 155155.76 | 26.85 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10923.76 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.91 | -0.0 | 188532.89 | 14.04 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.8 | -0.03 | 48683.62 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.33 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57719.26 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
