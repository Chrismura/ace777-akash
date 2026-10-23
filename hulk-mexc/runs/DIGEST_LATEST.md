# Hulk DIGEST — 2026-10-23T22:53:11Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.23 | 2.15 | 2.05 | -0.01 | 147063312.57 | 0.21 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 1.95 | 1.76 | -0.01 | 24568157.28 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.33 | 1.27 | -0.01 | 291251483.32 | 0.0 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 6.78 | 6.21 | -0.04 | 886016.72 | 15.05 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 5.86 | 5.37 | -0.03 | 780518.08 | 2.87 | skipped_fast |
| QNTUSDT | IDLE | 1.99 | 3.52 | 3.02 | -0.03 | 1230905.01 | 3.33 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 3.74 | 2.51 | -0.01 | 523501.43 | 3.14 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 7.88 | 7.31 | -0.04 | 84974.25 | 18.91 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 5.55 | 5.07 | -0.01 | 205083.77 | 30.36 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 5.95 | 5.49 | -0.02 | 76693.42 | 8.74 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 5.36 | 5.09 | -0.02 | 57476.18 | 9.48 | skipped_fast |
| KITEUSDT | IDLE | 2.27 | 3.96 | 3.81 | -0.03 | 57352.78 | 11.17 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 2.86 | 2.78 | -0.01 | 176765.61 | 10.86 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.45 | 6.04 | 5.7 | -0.04 | 59889.19 | 26.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.79 | 7.15 | 4.29 | -0.0 | 69709.92 | 29.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.42 | 2.45 | 0.03 | 50907.13 | 16.4 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.09 | 2.93 | -0.04 | 260162.83 | 9.11 | skipped_fast |
| IOTAUSDT | IDLE | 2.44 | 4.27 | 4.01 | -0.01 | 71049.9 | 20.66 | skipped_fast |
| LAUSDT | IDLE | 2.17 | 8.69 | 3.66 | 0.13 | 64985.25 | 34.48 | skipped_fast |
| FLUIDUSDT | IDLE | 2.16 | 3.77 | 3.63 | 0.02 | 5543.51 | 21.44 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.71 | 0.39 | 0.01 | 51148.14 | 39.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.15 | 0.78 | -0.01 | 37054.62 | 63.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
