# Hulk DIGEST — 2026-10-23T19:22:28Z

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
| XRPUSDT | IDLE | 1.03 | 1.8 | 1.73 | -0.01 | 26072660.63 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.6 | 0.91 | 0.0 | 209240637.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.15 | 0.89 | -0.0 | 290019964.88 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 4.16 | 2.27 | -0.04 | 1174703.75 | 2.76 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 4.23 | 3.28 | -0.04 | 736053.42 | 2.81 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.45 | 2.82 | -0.02 | 792251.22 | 15.9 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 4.4 | 3.85 | 0.01 | 511818.98 | 12.63 | skipped_fast |
| CHIPUSDT | IDLE | 2.64 | 5.06 | 3.52 | -0.01 | 107521.47 | 18.14 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 10.14 | 5.52 | 0.03 | 65462.06 | 46.33 | skipped_fast |
| REDUSDT | IDLE | 2.53 | 4.7 | 2.39 | 0.01 | 59735.01 | 17.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.86 | 3.66 | 0.98 | 0.04 | 198470.96 | 16.32 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 3.07 | 2.73 | 0.01 | 179061.92 | 8.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 3.93 | 0.59 | 0.06 | 47342.71 | 21.67 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 3.31 | 0.96 | 0.01 | 57344.79 | 13.26 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.71 | 2.06 | 0.01 | 72662.45 | 8.42 | skipped_fast |
| LAUSDT | IDLE | 2.81 | 7.96 | 0.72 | 0.09 | 57441.82 | 18.56 | skipped_fast |
| HBARUSDT | IDLE | 1.7 | 2.97 | 2.84 | -0.02 | 241707.93 | 3.84 | skipped_fast |
| WAXLUSDT | IDLE | 2.05 | 3.69 | 2.79 | -0.01 | 57017.2 | 20.92 | skipped_fast |
| IOTAUSDT | IDLE | 1.67 | 3.01 | 2.26 | -0.0 | 70713.21 | 13.47 | skipped_fast |
| FLUIDUSDT | IDLE | 1.64 | 3.25 | 0.19 | 0.01 | 4202.87 | 21.5 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | 0.01 | 51384.71 | 15.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.72 | 0.58 | -0.0 | 35933.22 | 68.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
