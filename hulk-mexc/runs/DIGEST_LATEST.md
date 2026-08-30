# Hulk DIGEST — 2026-08-30T00:12:34Z

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
| XRPUSDT | IDLE | 0.45 | 0.82 | 0.55 | 0.0 | 16448438.1 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 4.06 | 2.6 | -0.03 | 827647.22 | 7.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.47 | 2.61 | 2.22 | 0.01 | 309183.71 | 2.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 3.44 | 2.7 | -0.03 | 198265.46 | 10.57 | skipped_fast |
| RIZEUSDT | IDLE | 2.4 | 6.95 | 0.3 | -0.03 | 41481.52 | 58.87 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 5.72 | 5.19 | -0.04 | 68293.37 | 60.02 | skipped_fast |
| CCUSDT | IDLE | 0.7 | 1.38 | 0.27 | 0.06 | 231567.13 | 6.73 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 2.61 | 0.61 | 0.02 | 76243.3 | 10.94 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 3.19 | 1.28 | 0.02 | 68123.8 | 12.28 | skipped_fast |
| WUSDT | IDLE | 0.67 | 1.18 | 1.11 | -0.01 | 188011.17 | 8.79 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.25 | 0.69 | -0.02 | 67569.47 | 3.64 | skipped_fast |
| EDELUSDT | IDLE | 0.17 | 3.0 | 1.94 | 0.08 | 124591.94 | 35.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.32 | 2.21 | -0.04 | 1572.72 | 112.93 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.47 | 0.95 | 0.0 | 30279.06 | 4.89 | skipped_fast |
| HBARUSDT | IDLE | 0.24 | 0.45 | 0.25 | -0.01 | 141558.94 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.49 | 0.16 | 0.01 | 54007.69 | 24.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.3 | 0.58 | 0.11 | 0.0 | 1977.22 | 17.5 | skipped_fast |
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
