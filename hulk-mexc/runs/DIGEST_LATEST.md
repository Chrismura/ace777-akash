# Hulk DIGEST — 2026-09-13T08:39:53Z

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
| XRPUSDT | IDLE | 0.91 | 1.59 | 1.54 | -0.01 | 13057915.94 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.18 | 1.09 | -0.01 | 194301173.25 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.6 | 0.59 | -0.01 | 282712594.73 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.9 | 30.17 | 14.19 | 0.18 | 101515.41 | 13.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.09 | 3.65 | 3.52 | 0.02 | 460294.97 | 5.59 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.15 | 3.68 | -0.03 | 273694.54 | 14.67 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 3.99 | 2.12 | 0.02 | 62295.46 | 12.92 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 5.68 | 5.31 | -0.0 | 36572.77 | 9.42 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.26 | 3.01 | 0.03 | 55470.98 | 16.83 | skipped_fast |
| WUSDT | IDLE | 1.01 | 1.77 | 1.73 | 0.02 | 232389.88 | 10.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 3.27 | 3.12 | -0.04 | 77704.06 | 19.37 | skipped_fast |
| ZBCNUSDT | IDLE | 0.7 | 1.97 | 1.63 | -0.01 | 234540.65 | 1.13 | skipped_fast |
| TELUSDT | IDLE | 2.86 | 5.03 | 4.55 | -0.07 | 88821.0 | 38.05 | skipped_fast |
| EDELUSDT | IDLE | 1.04 | 2.55 | 2.09 | 0.07 | 173222.07 | 24.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.47 | 2.57 | 2.51 | -0.02 | 10144.49 | 5.59 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 1.69 | 1.59 | 0.0 | 70752.37 | 7.86 | skipped_fast |
| FLUIDUSDT | IDLE | 2.2 | 4.0 | 2.71 | 0.01 | 1217.06 | 22.17 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.24 | 1.15 | 0.01 | 151077.7 | 1.33 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.05 | 0.96 | -0.01 | 56111.77 | 7.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.36 | 0.28 | 0.01 | 33946.99 | 23.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
