# Hulk DIGEST — 2026-08-22T11:42:05Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.99 | 0.01 | 51616045.64 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.57 | 0.08 | 216822782.0 | 2.02 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.5 | 0.13 | 792242.46 | 9.4 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.33 | 0.01 | 1257503.94 | 5.17 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.61 | 0.02 | 584211.84 | 13.75 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 5.93 | 4.15 | -0.03 | 388631.88 | 22.63 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.52 | -0.1 | 636016.43 | 3.36 | skipped_fast |
| KITEUSDT | IDLE | 2.33 | 5.62 | 0.2 | 0.05 | 80474.73 | 10.62 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 4.93 | 3.82 | -0.03 | 79039.27 | 67.8 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.01 | -0.04 | 243488.45 | 3.22 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.66 | -0.03 | 167254.7 | 37.5 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2479.53 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 3.95 | 0.04 | 154739.97 | 12.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10923.76 | 76.09 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.9 | -0.03 | 48679.22 | 29.27 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.78 | 0.0 | 188433.54 | 7.79 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57663.92 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
