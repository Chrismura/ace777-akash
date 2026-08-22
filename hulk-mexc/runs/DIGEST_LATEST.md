# Hulk DIGEST — 2026-08-22T05:19:14Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.5 | 0.08 | 15654731.08 | 24.03 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.15 | 0.15 | 194115349.99 | 11.28 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.88 | 0.04 | 1331184.0 | 48.57 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.38 | -0.09 | 658340.15 | 13.45 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.76 | 0.06 | 569300.34 | 18.82 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.33 | -0.04 | 213448.74 | 39.62 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.2 | 0.11 | 163365.02 | 86.58 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 11.56 | 5.28 | 0.16 | 759384.59 | 35.8 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 7.1 | 0.03 | 543857.17 | 60.4 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 13.91 | 9.1 | 0.04 | 193225.77 | 10.85 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.42 | 0.08 | 73313.47 | 12.09 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.41 | 0.0 | -0.0 | 87189.45 | 21.67 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 7.9 | 5.99 | 0.04 | 5406.56 | 40.05 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 4.48 | 3.55 | 0.01 | 11281.01 | 91.37 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.0 | 5.52 | 1.28 | 0.09 | 191839.3 | 39.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 4.03 | 0.09 | 58702.52 | 42.81 | skipped_fast |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.05 | 57547.74 | 24.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
