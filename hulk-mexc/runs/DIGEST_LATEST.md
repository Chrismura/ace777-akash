# Hulk DIGEST — 2026-08-22T11:41:04Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.95 | 0.01 | 51616687.52 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.75 | 0.08 | 216860699.52 | 2.02 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.54 | 0.13 | 792259.36 | 9.41 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.41 | 0.02 | 1257581.77 | 6.46 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.72 | 0.02 | 584180.5 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.2 | -0.03 | 388820.05 | 29.83 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.62 | -0.1 | 636324.67 | 3.35 | skipped_fast |
| EDELUSDT | IDLE | 2.73 | 4.93 | 3.6 | -0.03 | 79089.27 | 56.47 | skipped_fast |
| KITEUSDT | IDLE | 2.32 | 5.59 | 0.2 | 0.05 | 79885.74 | 14.15 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.11 | -0.04 | 243533.64 | 6.43 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.66 | -0.03 | 167271.33 | 53.59 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | -0.0 | 2480.73 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 3.9 | 0.04 | 155237.77 | 24.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10923.76 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.78 | 0.0 | 188438.0 | 9.35 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.9 | -0.03 | 48685.93 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57689.01 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
