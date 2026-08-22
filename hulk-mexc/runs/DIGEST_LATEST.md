# Hulk DIGEST — 2026-08-22T06:54:34Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.1 | 0.04 | 20579699.25 | 3.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 23.87 | 7.9 | 0.2 | 215348449.61 | 5.11 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.01 | 0.05 | 1393751.59 | 1.27 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.82 | -0.11 | 703193.13 | 3.34 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.13 | 0.07 | 618191.7 | 11.29 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.67 | -0.03 | 246449.02 | 9.91 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.63 | 0.05 | 160388.79 | 11.37 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.01 | 0.18 | 784468.53 | 6.65 | skipped_fast |
| ZBCNUSDT | IDLE | 3.16 | 8.47 | 4.99 | 0.05 | 544649.81 | 33.63 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.46 | 0.04 | 200313.97 | 7.7 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 9.68 | 3.46 | 0.11 | 74454.78 | 10.84 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87672.36 | 22.3 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.15 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196649.47 | 10.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.54 | 0.09 | 59578.86 | 22.29 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.04 | 57891.6 | 16.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
