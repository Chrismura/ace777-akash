# Hulk DIGEST — 2026-10-15T18:15:39Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 25.14 | 8.42 | 0.13 | 4383342.3 | 2.16 | skipped_fast |
| WUSDT | IDLE | 2.65 | 7.78 | 3.51 | -0.05 | 2667063.75 | 9.61 | skipped_fast |
| ETHUSDT | IDLE | 2.93 | 5.73 | 0.81 | 0.0 | 344860523.82 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.53 | 4.95 | 0.79 | 0.0 | 52545905.71 | 2.99 | skipped_fast |
| BTCUSDT | IDLE | 1.78 | 3.48 | 0.6 | 0.01 | 500340598.68 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 3.76 | 11.92 | 3.28 | 0.01 | 1305766.63 | 1.91 | skipped_fast |
| REDUSDT | IDLE | 4.19 | 13.25 | 4.15 | 0.01 | 72418.14 | 6.96 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 10.86 | 9.32 | -0.13 | 245863.35 | 17.3 | skipped_fast |
| ZBCNUSDT | IDLE | 3.62 | 7.09 | 1.01 | 0.02 | 200453.91 | 26.36 | skipped_fast |
| KITEUSDT | IDLE | 3.59 | 7.56 | 1.5 | -0.03 | 70107.94 | 10.44 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 4.95 | 2.72 | -0.09 | 427896.26 | 9.29 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 11.39 | 9.08 | -0.02 | 81261.49 | 55.67 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 12.89 | 3.44 | -0.12 | 150458.01 | 10.79 | skipped_fast |
| BIOUSDT | IDLE | 2.81 | 6.87 | 0.92 | -0.03 | 85443.15 | 7.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.24 | 5.54 | 4.54 | 0.04 | 27856.87 | 14.86 | skipped_fast |
| TELUSDT | IDLE | 3.32 | 7.28 | 0.62 | -0.01 | 95134.24 | 22.56 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 4.52 | 0.51 | -0.0 | 311734.87 | 8.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.98 | 5.11 | 1.0 | -0.03 | 9052.6 | 21.5 | skipped_fast |
| MNSRYUSDT | IDLE | 1.46 | 2.77 | 1.03 | -0.01 | 32702.69 | 36.67 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.02 | 0.63 | -0.0 | 54829.26 | 31.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
