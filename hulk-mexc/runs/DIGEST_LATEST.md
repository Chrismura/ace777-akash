# Hulk DIGEST — 2026-08-22T17:16:02Z

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
| PYTHUSDT | IDLE | 1.75 | 8.48 | 1.31 | 0.1 | 49171315.22 | 3.84 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.8 | 0.05 | 214070263.59 | 1.36 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 4.25 | 0.69 | 0.1 | 770961.33 | 7.54 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.19 | -0.0 | 1103324.09 | 5.17 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.03 | -0.1 | 631119.72 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.5 | -0.01 | 535602.96 | 11.61 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.89 | -0.08 | 226375.26 | 3.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.21 | -0.01 | 309924.44 | 23.99 | skipped_fast |
| EDELUSDT | IDLE | 1.77 | 3.11 | 2.91 | -0.02 | 74878.75 | 34.46 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.86 | 0.04 | 87747.67 | 13.27 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.29 | -0.13 | 122337.03 | 9.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.63 | 0.37 | 0.05 | 46084.68 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.88 | -0.01 | 181172.08 | 1.57 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.79 | -0.01 | 136271.25 | 37.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.14 | 0.24 | 0.02 | 56120.65 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
