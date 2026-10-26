# Hulk DIGEST — 2026-10-26T22:32:12Z

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
| ETHUSDT | IDLE | 0.78 | 1.38 | 1.21 | -0.02 | 145500787.9 | 0.56 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.25 | 1.07 | -0.01 | 24090442.58 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.89 | 0.76 | -0.01 | 359871370.51 | 0.56 | skipped_fast |
| QNTUSDT | IDLE | 1.31 | 5.55 | 4.36 | 0.06 | 1440195.07 | 3.94 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 3.75 | 3.03 | -0.03 | 785751.14 | 4.08 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.36 | 2.94 | 0.03 | 646064.0 | 18.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 12.1 | 10.37 | 0.15 | 325179.58 | 17.65 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 9.21 | 7.3 | -0.13 | 57078.66 | 38.39 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 3.98 | 3.49 | 0.0 | 116608.38 | 3.12 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.58 | 1.92 | -0.03 | 183566.82 | 4.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 4.28 | 1.96 | 0.0 | 44745.18 | 48.87 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.46 | 2.09 | -0.02 | 57213.01 | 4.55 | skipped_fast |
| WAXLUSDT | IDLE | 2.89 | 5.14 | 4.28 | -0.04 | 53718.73 | 51.18 | skipped_fast |
| REDUSDT | IDLE | 1.29 | 2.34 | 1.66 | 0.0 | 63102.92 | 16.46 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 1.65 | 0.25 | -0.06 | 220600.79 | 46.31 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 4.86 | 1.72 | -0.0 | 1743.21 | 21.56 | skipped_fast |
| KITEUSDT | IDLE | 0.67 | 1.24 | 0.67 | 0.01 | 53821.64 | 14.05 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.34 | 0.94 | -0.01 | 234113.83 | 10.45 | skipped_fast |
| IOTAUSDT | IDLE | 1.39 | 2.44 | 2.24 | -0.02 | 86419.0 | 26.24 | skipped_fast |
| LAUSDT | IDLE | 1.04 | 2.07 | 1.25 | 0.03 | 65995.39 | 24.0 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.37 | 0.63 | -0.0 | 53742.15 | 7.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.59 | -0.0 | 41367.34 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
