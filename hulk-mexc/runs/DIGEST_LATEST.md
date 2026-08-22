# Hulk DIGEST — 2026-08-22T09:53:03Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.43 | 0.02 | 48046210.52 | 18.19 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 11.84 | 0.06 | 217089464.7 | 3.34 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.68 | 0.02 | 1265909.84 | 7.73 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.71 | -0.11 | 665225.57 | 3.39 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.58 | 0.02 | 592891.35 | 21.07 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.77 | -0.03 | 237718.63 | 12.94 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.1 | 0.05 | 154063.5 | 9.78 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.25 | 8.05 | 0.12 | 804172.25 | 9.56 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.0 | 7.07 | -0.02 | 438556.83 | 18.77 | skipped_fast |
| KITEUSDT | IDLE | 4.31 | 9.68 | 4.93 | 0.04 | 73210.45 | 12.84 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.29 | 0.01 | 192011.05 | 1.55 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.03 | 79207.65 | 44.89 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 21.4 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 7.2 | 6.71 | -0.03 | 171092.62 | 42.24 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.84 | -0.01 | 49337.47 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.02 | 57579.28 | 24.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
