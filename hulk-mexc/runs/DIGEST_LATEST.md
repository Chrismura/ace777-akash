# Hulk DIGEST — 2026-09-25T01:41:15Z

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
| XRPUSDT | IDLE | 1.36 | 2.5 | 1.45 | 0.03 | 72030705.38 | 1.95 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.96 | 0.39 | 0.0 | 734506132.48 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.79 | 0.49 | -0.0 | 354141979.37 | 0.34 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 38.75 | 24.24 | 0.06 | 187883.45 | 30.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.07 | 3.85 | 1.8 | 0.09 | 1005822.55 | 4.4 | skipped_fast |
| RIZEUSDT | IDLE | 2.0 | 36.45 | 15.63 | 0.47 | 87012.6 | 57.81 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 1.96 | 1.3 | 0.04 | 903902.59 | 1.08 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.96 | 0.16 | 0.05 | 503717.54 | 8.69 | skipped_fast |
| KITEUSDT | IDLE | 2.95 | 5.16 | 4.91 | -0.03 | 65924.11 | 8.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 8.35 | 7.7 | 0.11 | 102837.17 | 15.09 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 13.21 | 5.62 | 0.28 | 299496.4 | 10.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 2.38 | 1.69 | 0.01 | 220354.13 | 16.64 | skipped_fast |
| WUSDT | IDLE | 1.08 | 1.93 | 1.5 | 0.05 | 255496.09 | 5.97 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 2.47 | 0.26 | 0.08 | 123772.97 | 15.37 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 2.63 | 2.24 | 0.08 | 90849.66 | 19.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.37 | 6.64 | 5.33 | 0.15 | 12979.81 | 102.76 | skipped_fast |
| TELUSDT | IDLE | 1.78 | 3.29 | 1.86 | -0.04 | 105932.16 | 55.03 | skipped_fast |
| RWAUSDT | IDLE | 0.94 | 1.77 | 0.73 | 0.01 | 58965.76 | 7.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.59 | 1.13 | 0.27 | 0.04 | 1081.64 | 21.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.25 | -0.0 | 38922.46 | 31.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
