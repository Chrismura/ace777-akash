# Hulk DIGEST — 2026-08-22T05:38:30Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.26 | 0.08 | 16828017.56 | 1.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 10.02 | 0.17 | 202557010.58 | 5.89 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.64 | 0.05 | 1359858.41 | 11.45 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.21 | -0.1 | 707467.12 | 16.74 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.59 | 0.07 | 598942.59 | 10.32 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.5 | -0.04 | 219777.42 | 13.22 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.88 | 0.11 | 164320.98 | 14.83 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.97 | 0.18 | 761717.89 | 9.22 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.47 | 5.06 | 0.06 | 547216.19 | 28.18 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 13.91 | 8.9 | 0.04 | 196968.74 | 13.95 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.63 | 0.08 | 73333.51 | 13.87 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 4.52 | 0.76 | -0.01 | 88420.72 | 32.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.33 | 0.06 | 58948.21 | 28.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 70.06 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 39.32 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.86 | 0.07 | 195573.32 | 35.72 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.91 | 0.05 | 57991.65 | 8.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
