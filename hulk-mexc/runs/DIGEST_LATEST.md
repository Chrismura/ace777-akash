# Hulk DIGEST — 2026-08-22T08:17:59Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.35 | 0.03 | 26791678.77 | 3.91 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 8.73 | 0.15 | 223867789.53 | 3.87 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.26 | 0.04 | 1357193.55 | 2.54 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.5 | -0.09 | 684721.35 | 6.64 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.3 | 0.05 | 610749.78 | 10.28 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 29.98 | 8.29 | -0.02 | 247540.13 | 3.15 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.04 | 0.07 | 154434.61 | 12.22 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 11.25 | 1.98 | 0.2 | 822752.06 | 8.96 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 5.97 | 0.03 | 537521.19 | 17.48 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.17 | 0.04 | 194178.03 | 9.22 | skipped_fast |
| KITEUSDT | IDLE | 3.79 | 9.68 | 3.63 | 0.07 | 72825.98 | 12.65 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 4.52 | 3.46 | -0.03 | 86799.11 | 33.46 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 20.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11216.08 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 4.7 | 4.15 | -0.01 | 174170.96 | 25.71 | skipped_fast |
| QAITUSDT | IDLE | 1.4 | 2.71 | 0.54 | 0.02 | 3199.73 | 62.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.9 | 0.0 | 52289.35 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.04 | 58158.94 | 16.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
