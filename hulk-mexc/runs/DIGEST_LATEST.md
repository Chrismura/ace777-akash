# Hulk DIGEST — 2026-09-20T06:01:24Z

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
| XRPUSDT | IDLE | 1.54 | 2.82 | 1.7 | -0.03 | 55151938.84 | 2.89 | skipped_fast |
| ETHUSDT | IDLE | 1.37 | 2.46 | 1.88 | -0.02 | 253101962.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.45 | 0.98 | -0.01 | 495141456.28 | 0.06 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 6.71 | 5.6 | -0.03 | 730013.65 | 3.41 | skipped_fast |
| WUSDT | IDLE | 2.69 | 4.91 | 3.19 | 0.02 | 503478.38 | 6.35 | skipped_fast |
| HBARUSDT | IDLE | 2.96 | 5.43 | 3.31 | 0.02 | 717589.21 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 4.04 | 2.87 | -0.04 | 322146.81 | 5.7 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 4.53 | 3.38 | 0.01 | 89760.03 | 7.36 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 5.14 | 3.6 | -0.09 | 110968.89 | 19.03 | skipped_fast |
| REDUSDT | IDLE | 2.29 | 4.48 | 0.67 | 0.02 | 93570.37 | 14.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 5.46 | 2.14 | 0.07 | 219349.36 | 13.91 | skipped_fast |
| RIZEUSDT | IDLE | 2.3 | 8.73 | 3.44 | -0.06 | 35382.55 | 99.86 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 5.4 | 4.33 | -0.13 | 94926.89 | 57.13 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 2.33 | 1.24 | -0.0 | 76288.43 | 8.83 | skipped_fast |
| FLUIDUSDT | IDLE | 2.19 | 3.92 | 3.06 | -0.0 | 7907.51 | 21.78 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.11 | 2.86 | 0.02 | 55415.89 | 4.67 | skipped_fast |
| RWAINCUSDT | IDLE | 0.31 | 0.66 | 0.65 | -0.04 | 7111.81 | 5.96 | skipped_fast |
| TELUSDT | IDLE | 1.22 | 2.48 | 1.95 | -0.07 | 106679.38 | 41.12 | skipped_fast |
| RWAUSDT | IDLE | 0.94 | 1.72 | 1.1 | -0.01 | 52796.55 | 22.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.75 | 0.5 | -0.01 | 33869.89 | 50.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
