# Hulk DIGEST — 2026-10-09T16:32:03Z

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
| PYTHUSDT | IDLE | 1.17 | 5.17 | 2.87 | 0.13 | 2528175.33 | 2.36 | skipped_fast |
| WUSDT | IDLE | 1.09 | 6.82 | 3.17 | 0.15 | 2346832.42 | 13.7 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 2.41 | 1.74 | 0.02 | 35790058.6 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.71 | 1.14 | 0.03 | 303946228.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.27 | 0.9 | 0.02 | 342852717.47 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 5.57 | 4.34 | 0.06 | 1563685.41 | 8.97 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 23.32 | 8.31 | -0.02 | 81152.22 | 41.67 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 5.42 | 3.8 | 0.05 | 566973.77 | 10.66 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 11.91 | 1.19 | 0.17 | 373301.26 | 22.47 | skipped_fast |
| CHIPUSDT | IDLE | 2.99 | 7.25 | 2.72 | 0.04 | 87851.2 | 10.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.77 | 6.63 | 4.19 | 0.04 | 257745.43 | 20.67 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.45 | 1.83 | 0.01 | 676561.92 | 5.5 | skipped_fast |
| KITEUSDT | IDLE | 2.1 | 3.7 | 3.38 | -0.06 | 68204.16 | 19.11 | skipped_fast |
| FLUIDUSDT | IDLE | 2.37 | 15.69 | 12.63 | 0.1 | 12137.98 | 21.39 | skipped_fast |
| BIOUSDT | IDLE | 1.31 | 2.45 | 1.16 | 0.02 | 74119.88 | 3.56 | skipped_fast |
| TELUSDT | IDLE | 2.33 | 4.41 | 1.64 | 0.03 | 134275.46 | 42.94 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 1.69 | 0.49 | 0.02 | 63709.47 | 16.33 | skipped_fast |
| RWAINCUSDT | IDLE | 1.84 | 4.91 | 3.37 | 0.04 | 9008.53 | 134.68 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.63 | 0.54 | 0.01 | 53646.03 | 7.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.22 | 0.32 | -0.01 | 38414.55 | 35.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
