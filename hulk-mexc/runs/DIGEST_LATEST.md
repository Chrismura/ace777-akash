# Hulk DIGEST — 2026-10-18T23:11:34Z

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
| XRPUSDT | IDLE | 1.91 | 3.76 | 0.44 | 0.0 | 27705073.42 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 1.49 | 2.94 | 0.3 | -0.0 | 121664799.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.39 | 0.12 | 0.0 | 239385299.0 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 5.31 | 1.34 | -0.06 | 1290581.85 | 1.35 | skipped_fast |
| WUSDT | IDLE | 1.4 | 3.71 | 0.66 | -0.06 | 895112.04 | 12.35 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 5.25 | 0.57 | 0.01 | 818798.2 | 8.2 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 9.75 | 8.19 | -0.01 | 61152.07 | 21.6 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.67 | 0.16 | -0.02 | 276417.36 | 7.91 | skipped_fast |
| QNTUSDT | IDLE | 2.01 | 4.8 | 0.77 | -0.03 | 577337.43 | 1.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.06 | 5.27 | 0.7 | -0.04 | 238009.83 | 4.89 | skipped_fast |
| EDELUSDT | IDLE | 1.81 | 4.42 | 1.35 | -0.06 | 253007.87 | 15.18 | skipped_fast |
| REDUSDT | IDLE | 2.17 | 4.32 | 0.15 | -0.01 | 94839.93 | 16.0 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 13.36 | 7.81 | -0.0 | 80247.22 | 53.95 | skipped_fast |
| BIOUSDT | IDLE | 1.97 | 4.03 | 0.21 | -0.03 | 82360.04 | 8.53 | skipped_fast |
| CHIPUSDT | IDLE | 1.68 | 5.38 | 0.22 | -0.05 | 76038.73 | 7.34 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 3.04 | 0.13 | -0.01 | 67175.65 | 14.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 3.9 | 3.07 | -0.04 | 58280.65 | 39.58 | skipped_fast |
| IOTAUSDT | IDLE | 2.0 | 4.78 | 0.2 | -0.04 | 67916.57 | 17.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.88 | 3.56 | 2.55 | -0.06 | 4305.44 | 21.87 | skipped_fast |
| LAUSDT | IDLE | 1.54 | 4.02 | 0.48 | -0.06 | 58712.39 | 24.84 | skipped_fast |
| RWAUSDT | IDLE | 1.42 | 2.65 | 1.25 | 0.01 | 49632.5 | 7.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.7 | 0.51 | -0.01 | 35078.52 | 25.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
