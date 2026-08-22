# Hulk DIGEST — 2026-08-22T09:01:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.21 | 0.02 | 35387688.23 | 3.99 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 23.87 | 9.97 | 0.1 | 223187857.23 | 1.96 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.13 | 0.01 | 1311405.64 | 5.12 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.73 | -0.11 | 677508.0 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.8 | 0.02 | 601555.27 | 10.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.53 | -0.05 | 242156.35 | 9.59 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.74 | 0.04 | 154676.29 | 11.49 | skipped_fast |
| CCUSDT | IDLE | 2.12 | 11.25 | 3.71 | 0.15 | 798057.39 | 9.13 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 8.0 | 6.11 | -0.01 | 495377.35 | 62.67 | skipped_fast |
| KITEUSDT | IDLE | 4.19 | 9.68 | 3.01 | 0.05 | 73432.78 | 11.7 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.15 | 0.01 | 193095.65 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 4.52 | 3.57 | -0.05 | 86467.37 | 33.61 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.12 | 0.02 | 7020.8 | 20.74 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 6.52 | 5.92 | -0.04 | 173255.04 | 5.25 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11601.18 | 15.99 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.68 | -0.04 | 50961.61 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.03 | 57909.99 | 16.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
