# Hulk DIGEST — 2026-08-22T11:07:25Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.87 | -0.0 | 51658155.08 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.33 | 0.07 | 218334166.96 | 7.38 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.6 | 0.11 | 814257.37 | 9.51 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.46 | 0.0 | 1255524.36 | 3.88 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.63 | 0.01 | 595584.95 | 12.7 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 5.08 | 4.81 | -0.04 | 425120.79 | 27.99 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.31 | -0.11 | 646301.99 | 3.38 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.15 | -0.04 | 78823.37 | 22.75 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.71 | -0.06 | 240731.39 | 13.06 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.3 | 1.9 | 0.03 | 73628.37 | 9.12 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.56 | -0.04 | 169200.02 | 37.46 | skipped_fast |
| QAITUSDT | IDLE | 2.29 | 4.16 | 2.83 | -0.0 | 2498.14 | 35.86 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.27 | 0.03 | 154363.47 | 17.1 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.07 | -0.01 | 189117.7 | 7.81 | skipped_fast |
| RIZEUSDT | IDLE | 0.68 | 2.89 | 1.31 | -0.0 | 49214.73 | 46.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.34 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57550.76 | 16.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
