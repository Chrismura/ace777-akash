# Hulk DIGEST — 2026-08-18T05:23:00Z

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
| XRPUSDT | IDLE | 0.85 | 1.58 | 0.84 | -0.01 | 12779373.17 | 1.0 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 27.09 | 20.13 | -0.01 | 8290.13 | 62.41 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 32.47 | 9.12 | 0.23 | 62600.74 | 72.73 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.69 | 0.44 | -0.04 | 290888.23 | 7.65 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 4.55 | 1.12 | -0.05 | 321792.89 | 7.1 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 4.36 | 0.41 | 0.01 | 60080.92 | 11.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 2.76 | 2.12 | -0.03 | 173417.21 | 10.58 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.71 | 1.91 | -0.01 | 81589.71 | 4.14 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 1.79 | 1.52 | -0.01 | 198613.21 | 14.11 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.3 | 1.28 | -0.04 | 134977.68 | 11.04 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.78 | 1.68 | -0.01 | 66925.56 | 26.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.16 | 2.03 | 1.93 | -0.05 | 1152.44 | 41.65 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 3.82 | 3.47 | 0.02 | 81156.44 | 47.79 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.2 | 1.74 | 0.01 | 36813.62 | 5.35 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.35 | 0.7 | 0.01 | 140591.63 | 3.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.13 | 1.55 | -0.05 | 601.88 | 21.76 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.88 | 0.85 | -0.05 | 135340.88 | 57.35 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.69 | 0.6 | 0.0 | 49875.19 | 8.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
