# Hulk DIGEST — 2026-08-22T07:29:20Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 19.14 | 8.04 | 0.04 | 22059230.67 | 19.47 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 23.87 | 5.07 | 0.23 | 219908706.08 | 3.72 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 8.83 | 0.05 | 1352710.43 | 8.83 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.62 | -0.09 | 696156.43 | 6.65 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.28 | 0.07 | 618503.18 | 2.06 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 42.01 | 10.1 | 0.08 | 160548.14 | 19.86 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.43 | -0.04 | 247290.15 | 99.03 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 3.44 | 0.19 | 800425.83 | 5.79 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 5.2 | 0.06 | 541380.97 | 29.24 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.11 | 0.04 | 198748.59 | 4.6 | skipped_fast |
| KITEUSDT | IDLE | 3.38 | 9.68 | 2.59 | 0.1 | 74240.54 | 10.76 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6900.29 | 21.1 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.03 | 11367.66 | 53.65 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.55 | 0.05 | 193163.8 | 35.81 | skipped_fast |
| EDELUSDT | IDLE | 2.18 | 4.52 | 1.95 | -0.04 | 87212.61 | 155.56 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.55 | -0.04 | 53894.52 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58136.93 | 16.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
