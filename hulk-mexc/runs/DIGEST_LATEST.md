# Hulk DIGEST — 2026-08-18T03:21:18Z

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
| XRPUSDT | IDLE | 0.88 | 1.58 | 1.26 | -0.01 | 12539895.86 | 1.01 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 28.73 | 19.21 | -0.02 | 8231.63 | 9.77 | skipped_fast |
| CHIPUSDT | IDLE | 0.92 | 4.6 | 1.2 | -0.04 | 333730.19 | 3.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 2.84 | 2.38 | -0.03 | 175452.34 | 5.3 | skipped_fast |
| WUSDT | IDLE | 1.69 | 2.98 | 2.69 | -0.05 | 131465.18 | 7.41 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.89 | 0.14 | -0.05 | 286993.35 | 9.89 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 3.04 | 2.02 | -0.0 | 83399.69 | 8.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.06 | 1.87 | 1.72 | -0.01 | 216811.27 | 11.53 | skipped_fast |
| REDUSDT | IDLE | 1.83 | 3.65 | 0.39 | 0.03 | 56674.95 | 24.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 8.14 | 5.38 | 0.06 | 83079.89 | 48.79 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 3.31 | 1.28 | 0.0 | 65962.17 | 52.02 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.07 | 0.71 | -0.02 | 60182.19 | 14.08 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.35 | 1.26 | 0.0 | 141298.37 | 1.53 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 1.95 | 1.88 | -0.0 | 35189.58 | 1.79 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.71 | 0.7 | -0.04 | 851.49 | 52.71 | skipped_fast |
| FLUIDUSDT | IDLE | 1.2 | 2.13 | 1.83 | -0.04 | 621.89 | 22.72 | skipped_fast |
| TELUSDT | IDLE | 0.74 | 1.59 | 0.71 | -0.05 | 134299.73 | 57.22 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.69 | 0.6 | 0.01 | 49492.3 | 8.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
