# Hulk DIGEST — 2026-08-22T09:03:07Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.62 | 0.04 | 35820839.49 | 6.01 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.05 | 0.1 | 222001401.82 | 7.28 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 15.8 | 10.27 | 0.02 | 1308024.99 | 6.42 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.2 | -0.11 | 675255.04 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.26 | 0.02 | 603089.17 | 4.2 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.65 | -0.04 | 243507.33 | 12.95 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.89 | 0.05 | 154671.54 | 11.53 | skipped_fast |
| CCUSDT | IDLE | 2.14 | 11.25 | 4.29 | 0.15 | 796913.49 | 3.34 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.46 | -0.01 | 481547.54 | 33.78 | skipped_fast |
| KITEUSDT | IDLE | 4.22 | 9.68 | 3.49 | 0.06 | 73405.02 | 10.84 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.25 | 0.02 | 192974.31 | 10.9 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 4.52 | 3.57 | -0.05 | 86487.41 | 33.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11599.81 | 15.99 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 55.06 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 6.52 | 6.07 | -0.04 | 171979.64 | 36.79 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.68 | -0.02 | 50804.04 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.04 | 57865.69 | 16.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
