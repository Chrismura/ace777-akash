# Hulk DIGEST — 2026-08-22T09:58:13Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.3 | 0.03 | 50928311.55 | 2.02 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 11.89 | 0.05 | 215936145.14 | 0.67 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 15.8 | 10.63 | 0.02 | 1261947.63 | 1.29 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.59 | -0.1 | 664450.66 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.54 | 0.03 | 594894.71 | 13.66 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.05 | -0.02 | 236837.99 | 3.21 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.3 | 0.06 | 153908.7 | 11.57 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.25 | 8.06 | 0.12 | 806518.64 | 10.42 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.0 | 7.04 | -0.02 | 438564.64 | 21.3 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 9.68 | 5.08 | 0.04 | 73312.23 | 9.19 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.18 | 0.01 | 191946.3 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 4.64 | 4.32 | -0.04 | 79190.5 | 33.8 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 21.41 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 7.2 | 6.66 | -0.02 | 171046.63 | 31.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.45 | 4.36 | 3.61 | 0.01 | 11477.95 | 81.15 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.79 | -0.0 | 49323.79 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.02 | 57582.17 | 16.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
