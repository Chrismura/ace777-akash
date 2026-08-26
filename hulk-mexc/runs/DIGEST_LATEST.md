# Hulk DIGEST — 2026-08-26T00:10:21Z

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
| PYTHUSDT | IDLE | 2.96 | 5.77 | 3.95 | -0.0 | 2221622.31 | 2.0 | skipped_fast |
| XRPUSDT | IDLE | 2.2 | 5.12 | 3.33 | -0.04 | 74887329.06 | 2.1 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 3.62 | 1.88 | -0.04 | 533284.7 | 4.19 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.5 | 3.17 | -0.02 | 793027.97 | 1.29 | skipped_fast |
| WUSDT | IDLE | 2.38 | 4.36 | 3.13 | -0.03 | 329573.93 | 9.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.79 | 5.18 | 1.66 | -0.03 | 427985.09 | 6.27 | skipped_fast |
| BIOUSDT | IDLE | 2.68 | 5.06 | 1.95 | -0.01 | 113816.08 | 6.87 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 3.76 | 3.62 | -0.01 | 179625.57 | 18.17 | skipped_fast |
| REDUSDT | IDLE | 2.28 | 5.55 | 4.55 | -0.02 | 80439.01 | 10.63 | skipped_fast |
| RIZEUSDT | IDLE | 2.75 | 5.62 | 3.18 | 0.03 | 50586.97 | 46.99 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 15.72 | 13.28 | -0.03 | 164320.31 | 69.81 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 3.71 | 1.23 | -0.03 | 61813.8 | 12.48 | skipped_fast |
| QAITUSDT | IDLE | 2.07 | 5.67 | 0.85 | 0.04 | 12812.87 | 52.12 | skipped_fast |
| RWAINCUSDT | IDLE | 1.16 | 2.03 | 1.99 | -0.03 | 2574.29 | 15.19 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 3.96 | 2.03 | -0.02 | 1065.07 | 21.56 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.13 | 1.74 | -0.02 | 133042.23 | 4.75 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.07 | 0.99 | -0.04 | 94300.28 | 16.62 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.65 | 1.38 | -0.03 | 56692.07 | 16.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
