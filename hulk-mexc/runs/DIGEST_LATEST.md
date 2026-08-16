# Hulk DIGEST — 2026-08-16T22:34:15Z

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
| XRPUSDT | IDLE | 0.71 | 1.26 | 1.03 | -0.01 | 6526156.13 | 2.01 | skipped_fast |
| RIZEUSDT | IDLE | 3.67 | 7.8 | 2.03 | 0.01 | 37390.46 | 59.77 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 3.77 | 2.9 | -0.03 | 146067.14 | 2.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 4.9 | 3.45 | 0.03 | 297121.26 | 7.0 | skipped_fast |
| WUSDT | IDLE | 1.71 | 3.24 | 1.19 | 0.01 | 183517.0 | 9.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.83 | 2.11 | -0.02 | 194160.55 | 9.58 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 3.21 | 2.63 | -0.03 | 67814.56 | 4.15 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.41 | 0.96 | -0.05 | 333960.56 | 7.36 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.65 | 1.6 | -0.03 | 56229.56 | 10.72 | skipped_fast |
| EDELUSDT | IDLE | 1.48 | 2.67 | 1.95 | 0.03 | 60534.8 | 79.16 | skipped_fast |
| QAITUSDT | IDLE | 1.25 | 3.83 | 0.0 | -0.01 | 2289.9 | 61.3 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 1.37 | 0.67 | -0.08 | 65583.21 | 24.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 3.01 | 0.0 | 0.08 | 9960.17 | 73.38 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.09 | 1.78 | -0.03 | 93965.8 | 55.63 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.24 | 0.69 | -0.01 | 104300.89 | 1.54 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.63 | 1.1 | -0.02 | 33963.4 | 5.29 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.61 | 0.61 | -0.0 | 50704.2 | 17.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.62 | 0.11 | 0.02 | 219.43 | 11.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
