# Hulk DIGEST — 2026-08-22T07:42:08Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.83 | 0.02 | 22674038.23 | 15.72 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 23.87 | 6.7 | 0.22 | 222331270.28 | 5.68 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.21 | 0.05 | 1357749.13 | 10.16 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.74 | -0.1 | 695280.5 | 3.33 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.04 | 0.05 | 616659.59 | 8.29 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.79 | -0.03 | 247715.41 | 3.2 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.94 | 0.06 | 160740.08 | 22.69 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 11.25 | 3.64 | 0.19 | 801304.6 | 6.63 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.56 | 0.04 | 537954.46 | 0.5 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.49 | 0.04 | 195703.42 | 13.89 | skipped_fast |
| KITEUSDT | IDLE | 3.42 | 9.68 | 3.46 | 0.09 | 74317.05 | 20.76 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.03 | 87115.4 | 66.89 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6890.3 | 21.16 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.36 | 3.9 | 0.0 | 178667.87 | 46.21 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 59.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.45 | -0.04 | 52676.02 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58439.43 | 8.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
