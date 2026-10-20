# Hulk DIGEST — 2026-10-20T13:16:01Z

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
| ETHUSDT | IDLE | 0.58 | 1.09 | 0.45 | -0.01 | 123837381.24 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.56 | 1.05 | 0.44 | -0.01 | 18760143.36 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.53 | 0.41 | -0.01 | 293534329.3 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.92 | 0.88 | 0.01 | 886587.25 | 5.44 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 12.27 | 9.36 | 0.01 | 80624.1 | 15.73 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.49 | 3.25 | -0.02 | 692212.56 | 14.07 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 17.51 | 11.92 | -0.04 | 72690.33 | 43.75 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 2.18 | 1.42 | -0.01 | 455016.7 | 10.63 | skipped_fast |
| QNTUSDT | IDLE | 1.58 | 2.95 | 1.39 | -0.03 | 525874.99 | 1.04 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 5.0 | 2.01 | 0.17 | 299286.86 | 22.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.69 | 4.18 | 3.07 | 0.04 | 93659.12 | 13.77 | skipped_fast |
| KITEUSDT | IDLE | 1.67 | 3.1 | 1.59 | 0.01 | 90625.59 | 9.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 2.14 | 1.45 | -0.03 | 198547.12 | 22.29 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.76 | 1.26 | -0.02 | 361860.79 | 2.43 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 1.84 | 0.5 | 0.01 | 65732.48 | 8.43 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.65 | 1.55 | -0.01 | 57680.02 | 25.18 | skipped_fast |
| WAXLUSDT | IDLE | 1.99 | 3.82 | 3.06 | -0.08 | 56399.26 | 48.83 | skipped_fast |
| LAUSDT | IDLE | 1.15 | 2.06 | 1.56 | -0.03 | 56596.16 | 19.36 | skipped_fast |
| IOTAUSDT | IDLE | 0.86 | 1.67 | 0.35 | 0.02 | 85518.81 | 26.35 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.34 | 0.62 | 0.0 | 50865.64 | 15.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.86 | 1.52 | 1.27 | -0.0 | 39285.36 | 52.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.19 | 0.38 | 0.0 | 0.01 | 4452.44 | 21.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
