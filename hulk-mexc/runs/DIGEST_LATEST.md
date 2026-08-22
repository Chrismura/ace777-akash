# Hulk DIGEST — 2026-08-22T08:05:48Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.65 | 0.0 | 25218202.3 | 23.79 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 23.87 | 9.85 | 0.17 | 224338741.22 | 2.61 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.19 | 0.03 | 1354722.32 | 16.65 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.97 | -0.09 | 683932.69 | 6.68 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.4 | 0.04 | 608720.6 | 14.56 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.56 | -0.04 | 247570.11 | 12.77 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.2 | 0.07 | 156316.7 | 11.4 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 11.25 | 3.08 | 0.2 | 813994.23 | 9.07 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 8.47 | 6.68 | 0.03 | 537044.16 | 22.65 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.64 | 0.03 | 194291.67 | 3.09 | skipped_fast |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.41 | 0.07 | 72846.37 | 10.96 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 38.74 | skipped_fast |
| EDELUSDT | IDLE | 2.23 | 4.52 | 2.7 | -0.03 | 87042.43 | 55.59 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 123.42 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 4.7 | 3.8 | -0.0 | 173932.2 | 46.33 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.78 | 0.0 | 52291.04 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.05 | 58255.01 | 8.05 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
