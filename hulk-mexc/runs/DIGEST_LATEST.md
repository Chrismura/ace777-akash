# Hulk DIGEST — 2026-08-22T08:34:33Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 10.87 | 0.02 | 29683864.87 | 4.02 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 23.87 | 11.94 | 0.09 | 224286465.85 | 4.01 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 15.8 | 10.51 | 0.02 | 1340922.12 | 3.86 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 13.0 | -0.1 | 683875.94 | 16.9 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.37 | 0.02 | 600895.24 | 12.61 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.05 | -0.05 | 253025.24 | 3.21 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.29 | 0.06 | 155452.51 | 13.27 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.68 | 0.17 | 814568.64 | 9.95 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 8.47 | 6.64 | 0.0 | 533825.68 | 29.18 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 13.91 | 9.49 | 0.02 | 194033.44 | 9.34 | skipped_fast |
| KITEUSDT | IDLE | 3.82 | 9.68 | 4.25 | 0.06 | 73530.97 | 11.8 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.04 | 86934.67 | 22.4 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6716.59 | 21.92 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11110.27 | 112.63 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 5.03 | 4.79 | -0.0 | 173930.15 | 20.74 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.81 | 0.01 | 52238.71 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.04 | 58308.19 | 8.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
