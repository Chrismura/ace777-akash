# Hulk DIGEST — 2026-08-22T15:13:33Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.5 | 0.04 | 51474792.15 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.1 | 0.02 | 214466871.95 | 6.26 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.83 | 0.11 | 800968.62 | 7.72 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.42 | -0.02 | 1172835.33 | 3.93 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.92 | -0.11 | 614019.67 | 6.84 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.04 | -0.02 | 562276.77 | 10.72 | skipped_fast |
| KITEUSDT | IDLE | 2.82 | 6.37 | 3.04 | 0.02 | 85111.51 | 9.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.57 | -0.07 | 324850.23 | 14.87 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.26 | -0.07 | 226652.54 | 3.33 | skipped_fast |
| REDUSDT | IDLE | 0.5 | 5.31 | 5.04 | -0.05 | 150630.9 | 12.92 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.05 | 79105.41 | 45.61 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.37 | 0.03 | 46057.27 | 21.94 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.51 | -0.02 | 188467.17 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.75 | 1.1 | 0.01 | 141045.19 | 47.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.01 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57307.43 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
