# Hulk DIGEST — 2026-08-22T06:45:26Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.26 | 0.05 | 20282371.6 | 1.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 23.87 | 6.66 | 0.22 | 213866734.88 | 2.52 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.25 | 0.06 | 1389686.85 | 5.02 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.03 | -0.11 | 701087.51 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.34 | 0.07 | 617159.38 | 7.19 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 12.9 | -0.04 | 245521.19 | 3.32 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.75 | 0.06 | 162346.09 | 11.39 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.33 | 0.18 | 783447.73 | 5.85 | skipped_fast |
| ZBCNUSDT | IDLE | 3.15 | 8.47 | 4.81 | 0.05 | 546127.69 | 24.71 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.33 | 0.04 | 200384.6 | 10.77 | skipped_fast |
| KITEUSDT | IDLE | 2.8 | 9.68 | 3.69 | 0.1 | 74533.7 | 12.69 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.89 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.03 | 87692.19 | 66.89 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 64.66 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 5.52 | 3.85 | 0.06 | 196539.24 | 56.57 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.1 | 0.09 | 59579.2 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 58018.46 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
