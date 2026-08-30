# Hulk DIGEST — 2026-08-30T10:13:28Z

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
| XRPUSDT | IDLE | 0.86 | 1.53 | 1.22 | 0.0 | 16507759.34 | 2.16 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 4.09 | 2.9 | -0.02 | 632808.45 | 20.28 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.42 | 1.42 | 0.01 | 320746.77 | 4.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 3.58 | 1.48 | -0.01 | 159901.48 | 12.86 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.65 | 0.25 | 0.03 | 209040.43 | 11.76 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.32 | 1.17 | 0.06 | 294643.98 | 8.45 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 2.79 | 1.8 | -0.03 | 71550.87 | 11.87 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.59 | 1.44 | -0.0 | 67539.05 | 3.66 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 2.13 | 1.7 | -0.0 | 71178.95 | 8.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 4.47 | 2.38 | -0.05 | 46694.24 | 59.28 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 5.09 | 0.92 | 0.15 | 122418.14 | 16.84 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.59 | 1.57 | -0.02 | 1396.06 | 50.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.3 | 0.34 | 0.03 | 3393.64 | 21.78 | skipped_fast |
| HBARUSDT | IDLE | 0.29 | 0.53 | 0.36 | 0.0 | 143529.42 | 1.33 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.24 | 0.01 | 52657.22 | 8.17 | skipped_fast |
| TELUSDT | IDLE | 0.63 | 1.13 | 0.82 | -0.03 | 73067.98 | 29.7 | skipped_fast |
| QNTUSDT | IDLE | 0.44 | 0.85 | 0.24 | 0.01 | 36866.56 | 3.25 | skipped_fast |
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
