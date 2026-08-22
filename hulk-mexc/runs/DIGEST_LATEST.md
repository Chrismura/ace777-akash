# Hulk DIGEST — 2026-08-22T15:00:16Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.34 | 0.04 | 51453340.47 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.58 | 5.13 | 0.03 | 213845492.65 | 1.38 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 6.16 | 3.09 | 0.11 | 798864.73 | 6.85 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 3.34 | 2.84 | -0.01 | 1178461.13 | 5.23 | skipped_fast |
| WUSDT | IDLE | 1.11 | 4.43 | 3.0 | -0.02 | 563143.35 | 13.9 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.36 | -0.1 | 614357.09 | 6.8 | skipped_fast |
| KITEUSDT | IDLE | 2.72 | 6.37 | 1.48 | 0.04 | 84556.64 | 11.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.55 | 4.21 | 1.51 | -0.07 | 323890.79 | 24.39 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.04 | -0.06 | 224465.19 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.63 | 1.67 | -0.04 | 78969.07 | 22.73 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.42 | 5.1 | 4.43 | -0.03 | 150672.4 | 11.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.4 | 0.85 | 0.01 | 9946.26 | 64.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.44 | 0.04 | 46551.02 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.07 | -0.01 | 188422.46 | 4.73 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 3.24 | 1.78 | 0.01 | 140172.98 | 47.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 20.16 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57272.08 | 24.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
