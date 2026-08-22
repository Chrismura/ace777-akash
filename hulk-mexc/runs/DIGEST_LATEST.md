# Hulk DIGEST — 2026-08-22T15:50:45Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.48 | 0.04 | 51491825.13 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 5.95 | 0.03 | 216084929.75 | 2.08 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.75 | 0.08 | 769000.18 | 11.12 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.42 | -0.02 | 1152806.63 | 3.93 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.13 | -0.1 | 603625.83 | 3.39 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.78 | -0.02 | 554232.28 | 9.62 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.82 | 0.03 | 85497.44 | 10.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 1.96 | -0.05 | 321408.28 | 20.57 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.92 | -0.07 | 219489.7 | 3.31 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.03 | 75031.67 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.5 | -0.16 | 134820.52 | 13.75 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.15 | 0.03 | 56483.32 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.25 | -0.02 | 184197.1 | 3.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140051.9 | 42.69 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57196.86 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
