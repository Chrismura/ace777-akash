# Hulk DIGEST — 2026-10-12T03:32:00Z

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
| WUSDT | IDLE | 2.27 | 43.37 | 3.15 | 0.7 | 7853220.02 | 16.44 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.46 | 0.74 | 0.02 | 202583805.72 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 0.96 | 0.58 | 0.01 | 18276225.27 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.68 | 0.43 | 0.01 | 170199575.38 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.3 | 7.62 | 0.75 | 0.08 | 930980.46 | 3.63 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.64 | 8.35 | -0.05 | 238608.97 | 12.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 4.52 | 0.27 | 0.05 | 250237.43 | 11.36 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.7 | 1.41 | -0.02 | 330249.72 | 23.76 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.1 | 1.01 | 0.01 | 706388.4 | 1.67 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 2.18 | 1.07 | 0.06 | 386395.44 | 3.98 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.96 | 0.4 | 0.05 | 96622.21 | 3.33 | skipped_fast |
| REDUSDT | IDLE | 1.25 | 2.46 | 0.24 | 0.03 | 54858.09 | 15.09 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 1.91 | 0.12 | 0.03 | 63199.35 | 10.1 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 3.36 | 1.33 | -0.01 | 24460.49 | 55.04 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.46 | 0.71 | 0.03 | 304118.62 | 4.26 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.3 | 1.21 | -0.02 | 171875.78 | 34.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 3.75 | 3.02 | 0.06 | 65129.75 | 21.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.78 | 0.2 | 0.0 | 35095.35 | 5.46 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.54 | 0.15 | 0.02 | 52933.99 | 15.46 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 6.64 | 4.24 | 0.07 | 39787.91 | 421.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
