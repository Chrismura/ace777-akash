# Hulk DIGEST — 2026-08-18T07:08:37Z

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
| XRPUSDT | IDLE | 0.59 | 1.16 | 0.2 | -0.01 | 12223478.77 | 2.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 29.58 | 11.59 | 0.19 | 72243.06 | 13.98 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 11.21 | 7.92 | -0.01 | 81678.88 | 26.04 | skipped_fast |
| KITEUSDT | IDLE | 2.4 | 4.36 | 2.94 | -0.02 | 60572.3 | 14.09 | skipped_fast |
| CHIPUSDT | IDLE | 0.92 | 4.55 | 1.47 | -0.12 | 296928.01 | 3.56 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.86 | 0.78 | -0.05 | 293611.27 | 6.58 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 10.79 | 7.86 | -0.03 | 11604.8 | 60.2 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 1.81 | 0.76 | -0.03 | 181049.76 | 5.26 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 1.7 | 0.72 | -0.0 | 215113.18 | 18.48 | skipped_fast |
| WUSDT | IDLE | 0.85 | 1.63 | 0.44 | -0.03 | 143263.36 | 17.13 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.79 | 0.49 | -0.02 | 82267.24 | 4.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 3.2 | 2.87 | -0.04 | 76791.49 | 49.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.03 | 1.75 | -0.04 | 1470.0 | 71.26 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.2 | 0.39 | 0.01 | 140975.62 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.88 | 1.0 | -0.05 | 134231.24 | 43.04 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.65 | 1.38 | -0.0 | 37187.52 | 3.57 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.69 | -0.0 | 49949.56 | 17.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 0.99 | 0.82 | -0.04 | 223.15 | 21.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
