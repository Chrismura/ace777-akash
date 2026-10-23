# Hulk DIGEST — 2026-10-23T23:53:53Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.33 | 2.46 | 1.39 | -0.01 | 26185565.67 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.26 | 2.38 | 1.0 | 0.0 | 157601887.59 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.39 | 0.57 | -0.0 | 308043293.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 4.14 | 7.72 | 3.7 | -0.02 | 843648.32 | 1.41 | skipped_fast |
| WUSDT | IDLE | 2.89 | 7.18 | 4.54 | -0.03 | 913577.14 | 12.44 | skipped_fast |
| QNTUSDT | IDLE | 2.2 | 4.02 | 2.57 | -0.03 | 1241231.13 | 0.55 | skipped_fast |
| ZBCNUSDT | IDLE | 3.53 | 6.52 | 4.78 | -0.01 | 204742.36 | 20.65 | skipped_fast |
| CHIPUSDT | IDLE | 3.58 | 8.86 | 3.72 | -0.01 | 84703.56 | 20.45 | skipped_fast |
| EDELUSDT | IDLE | 1.79 | 3.3 | 1.84 | -0.0 | 531323.69 | 18.7 | skipped_fast |
| BIOUSDT | IDLE | 3.59 | 6.67 | 3.39 | -0.0 | 77896.21 | 8.56 | skipped_fast |
| REDUSDT | IDLE | 2.89 | 5.41 | 2.5 | -0.0 | 55880.22 | 15.68 | skipped_fast |
| CCUSDT | IDLE | 2.1 | 3.84 | 2.39 | -0.01 | 189046.75 | 6.91 | skipped_fast |
| KITEUSDT | IDLE | 2.44 | 4.52 | 2.43 | -0.02 | 57138.78 | 12.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.09 | 3.65 | 3.47 | 0.02 | 51841.46 | 5.52 | skipped_fast |
| WAXLUSDT | IDLE | 3.75 | 6.93 | 3.85 | -0.02 | 60103.47 | 57.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.77 | 6.92 | 5.17 | -0.01 | 69804.33 | 25.21 | skipped_fast |
| HBARUSDT | IDLE | 2.2 | 4.12 | 1.92 | -0.03 | 264863.76 | 7.75 | skipped_fast |
| LAUSDT | IDLE | 2.0 | 8.07 | 2.93 | 0.13 | 65612.18 | 26.04 | skipped_fast |
| IOTAUSDT | IDLE | 2.2 | 4.13 | 1.82 | 0.0 | 72701.44 | 29.39 | skipped_fast |
| FLUIDUSDT | IDLE | 2.12 | 3.77 | 3.19 | 0.02 | 6496.13 | 63.39 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.78 | 0.01 | 51064.82 | 15.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.15 | 0.74 | -0.0 | 37509.43 | 63.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
