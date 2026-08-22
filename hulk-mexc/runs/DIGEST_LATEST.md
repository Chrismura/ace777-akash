# Hulk DIGEST — 2026-08-22T10:05:50Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 16.77 | 10.38 | 0.02 | 51583020.97 | 4.08 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 23.87 | 12.91 | 0.04 | 215313702.21 | 8.8 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.17 | 0.01 | 1258196.08 | 12.96 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.51 | -0.11 | 664598.05 | 6.81 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.63 | 0.02 | 594661.71 | 7.42 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 10.94 | -0.04 | 236901.46 | 3.24 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 11.25 | 8.7 | 0.11 | 811855.3 | 11.38 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 10.9 | 0.04 | 155605.87 | 17.94 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 7.87 | 7.17 | -0.02 | 435730.73 | 22.88 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 9.28 | 5.39 | 0.03 | 73266.02 | 12.93 | skipped_fast |
| EDELUSDT | IDLE | 2.69 | 4.76 | 4.11 | -0.03 | 79228.52 | 22.55 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.44 | 0.0 | 189407.46 | 18.77 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 7.38 | 6.87 | -0.03 | 171000.71 | 26.55 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 21.55 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.0 | 11462.91 | 64.86 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.5 | -0.0 | 49309.02 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.02 | 57496.73 | 24.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
