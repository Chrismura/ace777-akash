# Hulk DIGEST — 2026-08-29T21:11:59Z

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
| XRPUSDT | IDLE | 0.62 | 1.18 | 0.43 | 0.01 | 17665809.7 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 3.57 | 3.26 | -0.01 | 928628.4 | 2.46 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 9.39 | 6.31 | -0.08 | 40640.65 | 36.3 | skipped_fast |
| ZBCNUSDT | IDLE | 2.67 | 4.74 | 3.96 | -0.02 | 192359.75 | 11.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.93 | 3.52 | 2.2 | 0.03 | 321710.96 | 2.08 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.2 | 0.63 | 0.07 | 217421.67 | 9.29 | skipped_fast |
| KITEUSDT | IDLE | 2.04 | 5.39 | 3.29 | 0.03 | 67873.2 | 11.52 | skipped_fast |
| WUSDT | IDLE | 0.95 | 1.73 | 1.1 | 0.0 | 178864.34 | 15.31 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.83 | 0.09 | 0.01 | 75057.59 | 11.89 | skipped_fast |
| BIOUSDT | IDLE | 0.72 | 1.28 | 1.12 | -0.01 | 65884.68 | 7.28 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 4.14 | 1.86 | 0.08 | 124897.92 | 35.97 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.21 | 1.42 | -0.01 | 68747.19 | 17.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 1.8 | 1.05 | -0.02 | 1994.03 | 112.49 | skipped_fast |
| HBARUSDT | IDLE | 0.36 | 0.7 | 0.18 | -0.01 | 179886.48 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.05 | 0.84 | 0.0 | 28811.19 | 3.27 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.01 | 54564.05 | 24.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.12 | 0.24 | 0.0 | -0.0 | 1851.78 | 22.16 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
