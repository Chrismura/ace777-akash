# Hulk DIGEST — 2026-10-14T19:26:10Z

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
| PYTHUSDT | IDLE | 2.53 | 6.23 | 0.84 | 0.04 | 2120622.77 | 3.63 | skipped_fast |
| WUSDT | IDLE | 1.04 | 4.46 | 2.79 | -0.08 | 2741104.13 | 9.23 | skipped_fast |
| XRPUSDT | IDLE | 1.29 | 2.34 | 1.54 | -0.03 | 44559134.2 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.91 | 1.64 | 1.22 | -0.02 | 430483764.03 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.64 | 0.87 | -0.03 | 198386756.82 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 1.99 | 4.17 | 3.01 | -0.07 | 1173189.04 | 2.44 | skipped_fast |
| ZBCNUSDT | IDLE | 2.98 | 5.26 | 4.65 | -0.04 | 183062.5 | 17.36 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 3.38 | 2.21 | -0.08 | 435891.22 | 8.56 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 13.1 | 5.77 | 0.08 | 18315.44 | 21.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.15 | 6.35 | 4.31 | -0.07 | 106807.84 | 11.31 | skipped_fast |
| REDUSDT | IDLE | 2.54 | 4.95 | 0.82 | 0.01 | 61889.17 | 8.3 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 3.61 | 2.31 | -0.03 | 167196.98 | 35.94 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 5.41 | 4.03 | -0.0 | 86065.3 | 8.62 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 6.57 | 1.78 | -0.07 | 29886.96 | 10.38 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.18 | 1.69 | -0.04 | 526294.14 | 4.78 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.71 | 1.97 | -0.05 | 64904.63 | 3.79 | skipped_fast |
| TELUSDT | IDLE | 2.91 | 5.61 | 1.42 | 0.02 | 102470.71 | 38.88 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 4.08 | 2.72 | -0.01 | 49229.41 | 61.51 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.51 | 1.41 | -0.02 | 56369.63 | 7.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.73 | 0.5 | -0.01 | 36962.87 | 7.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
