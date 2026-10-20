# Hulk DIGEST — 2026-10-20T15:17:10Z

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
| XRPUSDT | IDLE | 2.31 | 4.28 | 2.31 | 0.01 | 22125635.94 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 2.15 | 4.03 | 1.86 | 0.01 | 143244498.5 | 1.48 | skipped_fast |
| BTCUSDT | IDLE | 1.37 | 2.55 | 1.3 | 0.0 | 326372445.91 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 4.01 | 9.08 | 3.4 | 0.03 | 960874.03 | 6.58 | skipped_fast |
| WUSDT | IDLE | 3.31 | 6.16 | 3.09 | 0.02 | 743001.79 | 16.02 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 12.27 | 9.93 | -0.02 | 77508.71 | 5.28 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.26 | 10.66 | 0.0 | 72558.74 | 56.82 | skipped_fast |
| ZBCNUSDT | IDLE | 4.11 | 7.67 | 3.63 | 0.01 | 192335.03 | 18.79 | skipped_fast |
| QNTUSDT | IDLE | 3.26 | 6.0 | 3.41 | -0.01 | 643804.07 | 9.62 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 3.65 | 1.81 | 0.0 | 422232.97 | 11.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.7 | 10.03 | 4.72 | 0.11 | 110638.34 | 8.85 | skipped_fast |
| BIOUSDT | IDLE | 3.23 | 6.1 | 2.41 | 0.04 | 63731.39 | 8.21 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 12.37 | 0.4 | 0.3 | 319018.6 | 14.25 | skipped_fast |
| REDUSDT | IDLE | 2.71 | 5.05 | 2.49 | 0.0 | 58749.43 | 15.93 | skipped_fast |
| HBARUSDT | IDLE | 2.53 | 4.66 | 2.72 | 0.01 | 388274.59 | 14.38 | skipped_fast |
| KITEUSDT | IDLE | 2.43 | 4.65 | 1.38 | 0.01 | 90203.5 | 10.59 | skipped_fast |
| IOTAUSDT | IDLE | 3.42 | 6.99 | 2.41 | 0.05 | 89977.66 | 25.63 | skipped_fast |
| LAUSDT | IDLE | 3.22 | 6.1 | 2.33 | 0.02 | 56675.06 | 24.37 | skipped_fast |
| WAXLUSDT | IDLE | 2.95 | 5.42 | 3.15 | -0.05 | 54936.1 | 40.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 2.67 | 0.0 | 0.03 | 4599.67 | 21.45 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.82 | 0.85 | 0.0 | 51468.57 | 39.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.79 | 1.52 | 0.4 | 0.01 | 39742.21 | 14.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
