# Hulk DIGEST — 2026-09-09T18:12:43Z

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
| XRPUSDT | IDLE | 1.28 | 2.36 | 1.39 | -0.01 | 41874056.23 | 1.41 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 2.04 | 1.26 | -0.0 | 525115398.88 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.09 | 2.0 | 1.22 | -0.0 | 337599475.98 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.4 | 4.47 | 2.23 | 0.03 | 581017.79 | 1.79 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 2.98 | 2.8 | -0.04 | 539440.33 | 7.76 | skipped_fast |
| EDELUSDT | IDLE | 3.25 | 5.88 | 4.16 | -0.02 | 182963.39 | 28.97 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 22.82 | 17.63 | -0.01 | 70814.95 | 94.09 | skipped_fast |
| WUSDT | IDLE | 2.63 | 5.15 | 0.72 | 0.01 | 178701.54 | 3.86 | skipped_fast |
| ZBCNUSDT | IDLE | 2.57 | 4.92 | 1.83 | 0.03 | 197304.28 | 22.8 | skipped_fast |
| BIOUSDT | IDLE | 1.71 | 3.2 | 1.42 | -0.03 | 96931.66 | 7.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 5.22 | 2.69 | 0.07 | 109702.19 | 12.25 | skipped_fast |
| REDUSDT | IDLE | 1.77 | 3.39 | 1.01 | 0.02 | 60464.76 | 18.13 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.7 | 0.94 | 0.01 | 64480.97 | 11.31 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.03 | 1.37 | -0.02 | 405512.66 | 2.56 | skipped_fast |
| TELUSDT | IDLE | 2.38 | 4.29 | 3.16 | 0.03 | 102075.38 | 27.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.4 | 1.69 | -0.0 | 7484.98 | 11.08 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 3.56 | 3.29 | -0.04 | 414.4 | 7.31 | skipped_fast |
| RWAUSDT | IDLE | 1.41 | 2.56 | 1.78 | -0.01 | 54490.4 | 14.51 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.26 | 1.37 | -0.02 | 45652.98 | 8.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.57 | 0.27 | 0.01 | 23095.93 | 43.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
