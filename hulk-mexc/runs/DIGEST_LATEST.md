# Hulk DIGEST — 2026-08-22T07:01:48Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.13 | 0.04 | 20866457.27 | 1.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 23.87 | 7.24 | 0.21 | 215808601.52 | 3.81 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.13 | 0.05 | 1390328.35 | 6.34 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.03 | -0.1 | 703807.59 | 13.23 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.29 | 0.07 | 618696.35 | 14.38 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.44 | -0.03 | 245997.66 | 3.3 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.09 | 0.06 | 160565.68 | 19.21 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 3.16 | 0.19 | 788909.47 | 9.9 | skipped_fast |
| ZBCNUSDT | IDLE | 3.21 | 8.47 | 4.92 | 0.04 | 544352.02 | 18.28 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.26 | 0.04 | 200283.45 | 4.61 | skipped_fast |
| KITEUSDT | IDLE | 3.41 | 9.68 | 3.23 | 0.11 | 74414.85 | 11.72 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.92 | -0.03 | 87662.28 | 22.27 | skipped_fast |
| FLUIDUSDT | IDLE | 3.34 | 7.38 | 4.29 | 0.05 | 6989.9 | 21.13 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11292.34 | 91.72 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.6 | 0.06 | 196651.62 | 61.48 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.54 | 0.06 | 58718.97 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.04 | 57916.92 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
