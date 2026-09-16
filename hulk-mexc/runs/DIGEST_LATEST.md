# Hulk DIGEST — 2026-09-16T18:14:17Z

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
| XRPUSDT | IDLE | 1.95 | 3.69 | 1.37 | -0.08 | 83030018.35 | 3.91 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.56 | 0.84 | -0.01 | 424731765.78 | 1.99 | skipped_fast |
| BTCUSDT | IDLE | 0.88 | 1.66 | 0.72 | -0.01 | 534599502.61 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 36.05 | 21.4 | 0.32 | 60320.37 | 75.47 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 15.0 | 8.54 | -0.01 | 65964.07 | 108.0 | skipped_fast |
| CCUSDT | IDLE | 2.14 | 4.25 | 0.26 | -0.01 | 476712.59 | 5.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.05 | 4.01 | 0.66 | -0.03 | 412672.42 | 28.38 | skipped_fast |
| CHIPUSDT | IDLE | 3.01 | 6.39 | 1.91 | -0.03 | 89825.01 | 18.99 | skipped_fast |
| WUSDT | IDLE | 1.83 | 3.55 | 0.74 | -0.06 | 209275.69 | 22.51 | skipped_fast |
| EDELUSDT | IDLE | 0.7 | 5.84 | 3.2 | 0.12 | 374082.82 | 26.57 | skipped_fast |
| REDUSDT | IDLE | 2.03 | 4.2 | 1.27 | -0.04 | 67006.35 | 4.66 | skipped_fast |
| BIOUSDT | IDLE | 2.14 | 4.05 | 1.48 | -0.03 | 81042.65 | 69.18 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 2.99 | 1.38 | -0.06 | 379060.22 | 8.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.24 | 2.44 | 0.27 | -0.05 | 214119.45 | 31.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.03 | 12246.97 | 11.93 | skipped_fast |
| TELUSDT | IDLE | 1.77 | 4.45 | 1.79 | -0.08 | 122266.64 | 48.87 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 2.45 | 0.66 | -0.04 | 39864.83 | 10.02 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 2.71 | 0.0 | -0.04 | 2585.84 | 22.31 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.14 | 0.0 | 0.0 | 52921.13 | 22.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.62 | 0.47 | -0.02 | 33495.79 | 9.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
