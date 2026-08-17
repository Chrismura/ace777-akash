# Hulk DIGEST — 2026-08-17T10:06:58Z

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
| XRPUSDT | IDLE | 0.61 | 1.07 | 1.04 | -0.0 | 10468502.16 | 2.01 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 14.04 | 8.96 | 0.04 | 347019.54 | 10.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.88 | 29.09 | 2.31 | 0.34 | 65484.25 | 47.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 2.53 | 0.64 | 0.03 | 171728.78 | 15.68 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 2.94 | 2.72 | -0.06 | 57636.3 | 18.15 | skipped_fast |
| CCUSDT | IDLE | 0.72 | 1.34 | 0.68 | -0.01 | 253058.53 | 5.25 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 1.62 | 1.31 | -0.01 | 166652.86 | 2.56 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.6 | 1.29 | 0.0 | 189691.54 | 16.69 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.38 | 1.16 | 0.0 | 69851.85 | 4.06 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.75 | 0.26 | 0.06 | 55477.77 | 12.78 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.39 | 1.74 | -0.02 | 53130.72 | 16.19 | skipped_fast |
| QAITUSDT | IDLE | 1.5 | 3.0 | 0.0 | 0.01 | 2418.08 | 60.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.02 | 1.13 | -0.03 | 2279.51 | 45.79 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.74 | 0.17 | 0.01 | 113335.31 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 1.87 | 1.49 | -0.0 | 87341.48 | 48.33 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.17 | 0.64 | -0.03 | 32023.92 | 1.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.33 | 1.28 | 0.0 | 791.2 | 21.12 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.26 | 0.01 | 49096.45 | 26.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
