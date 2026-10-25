# Hulk DIGEST — 2026-10-25T16:05:33Z

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
| ETHUSDT | IDLE | 0.55 | 1.05 | 0.31 | 0.02 | 95874345.66 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.82 | 0.25 | 0.03 | 15350916.26 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.67 | 0.27 | 0.01 | 152965701.39 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.49 | 2.96 | 0.18 | -0.01 | 652346.02 | 22.32 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 21.0 | 6.49 | 0.03 | 18441.87 | 21.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.13 | 1.07 | 0.06 | 439111.26 | 1.39 | skipped_fast |
| EDELUSDT | IDLE | 1.7 | 3.37 | 0.17 | 0.0 | 428236.32 | 13.33 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 4.52 | 1.08 | 0.06 | 459156.7 | 3.75 | skipped_fast |
| KITEUSDT | IDLE | 2.7 | 5.12 | 1.8 | 0.02 | 54478.85 | 11.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 4.83 | 3.19 | 0.07 | 99194.35 | 18.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.55 | 0.61 | 0.06 | 206907.68 | 14.58 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 3.52 | 0.99 | 0.03 | 189562.72 | 9.78 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.22 | 0.66 | 0.01 | 60450.77 | 4.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 2.0 | 1.58 | -0.01 | 58768.15 | 16.57 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 1.93 | 0.67 | -0.01 | 66689.69 | 16.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.14 | 2.61 | 1.51 | -0.03 | 39891.71 | 62.78 | skipped_fast |
| WAXLUSDT | IDLE | 2.04 | 4.07 | 0.02 | 0.03 | 53682.77 | 72.61 | skipped_fast |
| HBARUSDT | IDLE | 0.56 | 1.1 | 0.16 | 0.01 | 168542.18 | 6.48 | skipped_fast |
| LAUSDT | IDLE | 0.9 | 3.73 | 1.05 | -0.07 | 70228.85 | 36.52 | skipped_fast |
| IOTAUSDT | IDLE | 0.77 | 1.48 | 0.44 | 0.01 | 61601.6 | 25.61 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.36 | 0.48 | 0.0 | 50850.18 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.36 | -0.0 | 36889.04 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
