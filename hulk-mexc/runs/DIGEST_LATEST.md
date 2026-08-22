# Hulk DIGEST — 2026-08-22T15:14:44Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.44 | 0.04 | 51474715.99 | 3.95 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.07 | 0.02 | 214504818.54 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.88 | 0.11 | 800956.6 | 7.72 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 2.85 | 2.49 | -0.02 | 1172829.72 | 3.93 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.86 | -0.11 | 614019.31 | 3.42 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.09 | -0.02 | 561788.58 | 11.8 | skipped_fast |
| KITEUSDT | IDLE | 2.82 | 6.37 | 3.0 | 0.02 | 85127.16 | 12.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.59 | -0.07 | 324699.98 | 14.87 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.29 | -0.07 | 226782.77 | 3.33 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.5 | 5.21 | -0.05 | 150606.65 | 13.86 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.52 | 2.23 | -0.05 | 79080.32 | 45.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.37 | 0.03 | 46065.34 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.45 | -0.02 | 188447.83 | 7.9 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.75 | 1.21 | 0.01 | 140996.71 | 47.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.01 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.48 | 0.02 | 57324.85 | 16.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
