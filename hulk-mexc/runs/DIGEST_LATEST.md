# Hulk DIGEST — 2026-08-22T15:04:16Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.38 | 0.04 | 51465644.6 | 7.9 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.47 | 0.03 | 214013641.0 | 3.46 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 5.65 | 2.34 | 0.11 | 801133.35 | 5.97 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 2.85 | 2.08 | -0.01 | 1172719.98 | 5.22 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.36 | -0.11 | 614305.48 | 3.4 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.71 | -0.02 | 562951.42 | 10.68 | skipped_fast |
| KITEUSDT | IDLE | 2.72 | 6.37 | 1.39 | 0.03 | 83569.07 | 8.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.55 | -0.08 | 323298.18 | 41.4 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.66 | -0.06 | 225316.45 | 3.3 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.04 | 78999.49 | 22.73 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2335.57 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 5.1 | 4.29 | -0.03 | 150736.69 | 10.97 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.47 | 0.04 | 46495.38 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.94 | -0.01 | 188420.11 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.75 | 1.05 | 0.01 | 140922.0 | 53.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 22.36 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.23 | 0.32 | 0.02 | 57320.71 | 24.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
