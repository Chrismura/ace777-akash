# Hulk DIGEST — 2026-09-28T15:25:36Z

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
| WUSDT | IDLE | 1.81 | 8.49 | 6.5 | -0.09 | 3174469.85 | 8.09 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 11.99 | 10.02 | -0.04 | 1351179.36 | 17.93 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 20.16 | 10.59 | 0.27 | 20442875.87 | 10.52 | skipped_fast |
| XRPUSDT | IDLE | 2.2 | 3.98 | 2.81 | -0.02 | 63358767.43 | 2.69 | skipped_fast |
| HBARUSDT | IDLE | 1.5 | 11.78 | 6.01 | 0.26 | 7886420.51 | 11.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.42 | 5.98 | 5.38 | -0.06 | 1477820.13 | 15.35 | skipped_fast |
| ETHUSDT | IDLE | 1.17 | 2.16 | 1.19 | -0.01 | 345256199.25 | 0.83 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.48 | 0.93 | -0.02 | 755469591.27 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 18.24 | 6.06 | 0.02 | 198871.04 | 27.56 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 6.46 | 4.98 | -0.07 | 82681.35 | 13.73 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 4.49 | 3.73 | -0.06 | 61816.98 | 12.55 | skipped_fast |
| BIOUSDT | IDLE | 1.68 | 4.83 | 3.62 | -0.07 | 109898.68 | 3.44 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 5.91 | 4.15 | -0.09 | 100991.18 | 8.9 | skipped_fast |
| TELUSDT | IDLE | 2.97 | 5.63 | 2.1 | -0.02 | 157067.79 | 11.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.31 | 1.68 | -0.05 | 231096.7 | 16.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.51 | 7.29 | 6.6 | -0.09 | 21181.42 | 108.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.33 | 1.95 | 0.57 | -0.14 | 60279.75 | 21.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.54 | 3.49 | 3.37 | -0.06 | 3921.81 | 59.86 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.8 | 0.14 | -0.02 | 60043.65 | 7.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.96 | 0.38 | -0.02 | 34293.43 | 66.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
