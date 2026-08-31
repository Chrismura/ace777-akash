# Hulk DIGEST — 2026-08-31T10:16:48Z

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
| XRPUSDT | IDLE | 1.16 | 2.25 | 0.53 | -0.01 | 39145358.48 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.7 | 0.3 | -0.0 | 429816934.32 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.65 | 0.39 | 0.01 | 509487750.86 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 25.32 | 18.72 | 0.01 | 120224.45 | 41.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.79 | 5.66 | 2.2 | 0.01 | 572700.51 | 5.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.25 | 3.18 | 0.23 | 0.01 | 529051.8 | 4.21 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.51 | 2.31 | -0.01 | 231784.73 | 9.72 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 2.46 | 1.12 | 0.01 | 235382.19 | 5.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 3.89 | 1.06 | -0.08 | 232938.57 | 13.42 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 3.47 | 2.71 | -0.01 | 69782.34 | 10.11 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.65 | 2.57 | -0.06 | 97111.36 | 9.97 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.55 | 0.97 | -0.03 | 86825.75 | 7.53 | skipped_fast |
| FLUIDUSDT | IDLE | 2.51 | 5.02 | 0.0 | 0.01 | 1731.05 | 14.94 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 4.12 | 0.46 | 0.03 | 95553.6 | 40.38 | skipped_fast |
| QNTUSDT | IDLE | 2.0 | 3.85 | 1.06 | 0.01 | 38511.64 | 9.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 1.87 | 0.25 | -0.01 | 33687.43 | 34.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.23 | 2.18 | -0.01 | 2681.98 | 119.42 | skipped_fast |
| HBARUSDT | IDLE | 0.53 | 1.03 | 0.26 | -0.01 | 233851.7 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.71 | 0.08 | 0.02 | 53696.78 | 8.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.91 | 0.51 | -0.01 | 29427.52 | 51.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
