# Hulk DIGEST — 2026-08-22T08:18:35Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.63 | 0.03 | 26896155.58 | 3.92 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 8.73 | 0.15 | 223681351.02 | 1.29 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.28 | 0.04 | 1357171.95 | 5.08 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.5 | -0.1 | 684682.24 | 3.33 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.42 | 0.05 | 610837.93 | 12.35 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 29.98 | 8.66 | -0.03 | 248379.73 | 6.33 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.08 | 0.07 | 154502.8 | 14.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 11.25 | 1.95 | 0.2 | 822746.82 | 8.96 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.12 | 0.03 | 537520.52 | 20.01 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.17 | 0.04 | 194180.79 | 10.77 | skipped_fast |
| KITEUSDT | IDLE | 3.79 | 9.68 | 3.63 | 0.07 | 72771.3 | 11.76 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.68 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 4.52 | 3.57 | -0.02 | 86791.8 | 111.23 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11182.34 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 4.0 | -0.0 | 174131.99 | 20.57 | skipped_fast |
| QAITUSDT | IDLE | 1.4 | 2.71 | 0.54 | 0.02 | 3201.73 | 62.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.73 | 0.0 | 52296.54 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.04 | 58161.16 | 16.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
