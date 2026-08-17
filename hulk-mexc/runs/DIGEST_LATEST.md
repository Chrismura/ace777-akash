# Hulk DIGEST — 2026-08-17T10:10:46Z

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
| XRPUSDT | IDLE | 0.61 | 1.07 | 1.0 | -0.0 | 10474258.13 | 1.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 14.04 | 9.69 | 0.03 | 346780.75 | 16.87 | skipped_fast |
| RIZEUSDT | IDLE | 2.88 | 29.09 | 2.56 | 0.33 | 66082.35 | 32.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 2.53 | 0.82 | 0.02 | 171882.45 | 13.82 | skipped_fast |
| CCUSDT | IDLE | 0.74 | 1.34 | 0.97 | -0.01 | 254015.14 | 6.31 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 2.94 | 2.4 | -0.06 | 57639.41 | 26.53 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 1.62 | 1.37 | -0.01 | 166583.0 | 2.56 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.6 | 1.32 | 0.0 | 188836.12 | 14.31 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.75 | 0.38 | 0.05 | 55452.68 | 12.8 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.38 | 1.0 | 0.0 | 69872.53 | 8.1 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.39 | 1.79 | -0.02 | 53179.56 | 14.05 | skipped_fast |
| QAITUSDT | IDLE | 1.5 | 3.0 | 0.0 | 0.01 | 2418.08 | 60.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.02 | 1.13 | -0.03 | 2279.51 | 45.79 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.74 | 0.08 | 0.01 | 113382.64 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 1.87 | 1.49 | -0.0 | 87294.19 | 55.17 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.17 | 0.64 | -0.03 | 32010.84 | 1.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.33 | 1.28 | 0.0 | 791.2 | 21.11 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.35 | 0.0 | 49196.06 | 26.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
