# Hulk DIGEST — 2026-10-21T02:31:15Z

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
| XRPUSDT | IDLE | 0.58 | 1.03 | 0.91 | 0.02 | 24411565.92 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.91 | 0.75 | 0.02 | 172608823.08 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.59 | 0.58 | 0.01 | 328256772.04 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.92 | 2.73 | 2.25 | 0.09 | 987860.5 | 2.51 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 14.9 | 12.38 | -0.08 | 81528.89 | 5.6 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.58 | 1.98 | 0.02 | 646789.98 | 14.98 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.4 | 1.22 | 0.01 | 819394.17 | 1.53 | skipped_fast |
| CHIPUSDT | IDLE | 1.11 | 3.06 | 2.88 | 0.05 | 446406.71 | 9.06 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 12.41 | 10.79 | 0.04 | 17701.84 | 21.59 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.76 | 1.08 | -0.01 | 368006.8 | 5.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 3.06 | 0.5 | 0.04 | 192933.81 | 29.99 | skipped_fast |
| EDELUSDT | IDLE | 0.32 | 2.52 | 0.06 | 0.32 | 366871.78 | 8.3 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.84 | 1.61 | 0.04 | 61142.22 | 4.08 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.18 | 0.46 | 0.04 | 57970.17 | 15.44 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.33 | 1.3 | 0.0 | 347366.91 | 4.8 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.33 | 0.71 | 0.0 | 73470.17 | 12.31 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 3.01 | 2.44 | 0.0 | 70149.42 | 60.38 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 3.28 | 1.42 | -0.02 | 57061.37 | 14.96 | skipped_fast |
| LAUSDT | IDLE | 1.51 | 3.09 | 0.31 | 0.06 | 55805.7 | 23.41 | skipped_fast |
| IOTAUSDT | IDLE | 0.9 | 1.58 | 1.45 | 0.02 | 75253.81 | 23.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.4 | 0.06 | 0.0 | 39972.09 | 5.7 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.31 | 0.0 | 52957.83 | 31.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
