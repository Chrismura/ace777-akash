# Hulk DIGEST — 2026-08-22T09:31:29Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.57 | 0.04 | 41711657.21 | 10.02 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.81 | 0.1 | 219353014.21 | 5.28 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 15.8 | 9.7 | 0.05 | 1295576.32 | 7.65 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.97 | -0.09 | 665222.65 | 3.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.51 | 0.04 | 594619.26 | 11.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.68 | -0.02 | 237843.27 | 6.47 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 41.27 | 11.13 | 0.06 | 154695.34 | 19.32 | skipped_fast |
| CCUSDT | IDLE | 2.21 | 11.25 | 6.93 | 0.14 | 795401.14 | 10.3 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.63 | -0.02 | 462609.55 | 27.25 | skipped_fast |
| KITEUSDT | IDLE | 4.28 | 9.68 | 4.45 | 0.05 | 73115.9 | 10.03 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.67 | 0.02 | 193223.35 | 10.84 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 4.52 | 3.57 | -0.02 | 79341.85 | 33.61 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.02 | 6973.73 | 13.87 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.69 | 5.92 | -0.01 | 171199.13 | 10.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.02 | 11488.56 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.82 | -0.03 | 49732.62 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.03 | 57706.96 | 8.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
