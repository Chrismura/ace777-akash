# Hulk DIGEST — 2026-08-22T08:59:53Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.08 | 0.02 | 35287031.92 | 3.98 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 23.87 | 10.22 | 0.1 | 223102760.51 | 1.31 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.13 | 0.01 | 1309930.31 | 7.69 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.29 | -0.11 | 678417.76 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.96 | 0.01 | 601533.37 | 10.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.56 | -0.05 | 242291.78 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.17 | 0.04 | 154660.79 | 13.27 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.79 | 0.15 | 799140.52 | 8.31 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 8.47 | 7.04 | -0.01 | 495200.02 | 18.7 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.86 | 0.01 | 193072.09 | 1.55 | skipped_fast |
| KITEUSDT | IDLE | 3.78 | 9.68 | 3.44 | 0.05 | 73472.75 | 11.72 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 7.38 | 5.12 | 0.02 | 7020.8 | 19.93 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 4.52 | 3.57 | -0.05 | 86492.39 | 33.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.38 | 4.48 | 1.88 | 0.02 | 11627.69 | 15.99 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 6.52 | 6.07 | -0.04 | 173258.07 | 5.25 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 3.73 | 2.03 | -0.04 | 50961.61 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.04 | 57910.67 | 16.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
