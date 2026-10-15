# Hulk DIGEST — 2026-10-15T03:32:58Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 8.91 | 6.47 | -0.1 | 2772859.96 | 14.95 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 6.23 | 4.79 | 0.01 | 2321592.43 | 4.78 | skipped_fast |
| ETHUSDT | IDLE | 2.25 | 4.62 | 2.71 | -0.06 | 294896155.55 | 0.72 | skipped_fast |
| XRPUSDT | IDLE | 2.2 | 4.02 | 2.49 | -0.05 | 53264832.88 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 2.01 | 1.12 | -0.03 | 503597292.68 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.76 | 8.56 | 5.39 | -0.1 | 1151964.26 | 5.11 | skipped_fast |
| HBARUSDT | IDLE | 2.76 | 5.9 | 3.97 | -0.07 | 605307.05 | 11.04 | skipped_fast |
| CCUSDT | IDLE | 1.86 | 6.24 | 4.9 | -0.12 | 428161.52 | 6.36 | skipped_fast |
| EDELUSDT | IDLE | 2.97 | 5.5 | 4.15 | -0.06 | 189544.05 | 21.61 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 13.43 | 11.18 | -0.19 | 113938.09 | 10.67 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 9.92 | 6.92 | -0.11 | 74575.73 | 12.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.87 | 4.79 | 3.27 | -0.07 | 217292.2 | 15.09 | skipped_fast |
| REDUSDT | IDLE | 2.27 | 4.29 | 1.71 | -0.01 | 64300.12 | 15.29 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 5.98 | 5.0 | -0.07 | 87982.46 | 10.73 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.82 | 2.0 | 0.01 | 26817.3 | 20.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 7.12 | 2.32 | -0.01 | 55864.97 | 62.66 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 3.89 | 2.73 | -0.05 | 97464.57 | 35.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.61 | 4.72 | 3.64 | -0.0 | 21070.1 | 21.14 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.62 | 1.11 | -0.03 | 54567.7 | 8.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.14 | 1.1 | -0.02 | 32781.35 | 26.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
