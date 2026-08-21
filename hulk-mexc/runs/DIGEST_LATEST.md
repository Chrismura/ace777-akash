# Hulk DIGEST — 2026-08-21T22:04:00Z

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
| PYTHUSDT | IDLE | 1.24 | 4.74 | 0.1 | 0.1 | 5696916.03 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.35 | 0.12 | 129574208.24 | 3.55 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.72 | 0.08 | 840735.7 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.95 | 0.05 | 0.11 | 636390.4 | 7.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 4.54 | 2.17 | 0.05 | 531488.31 | 3.08 | skipped_fast |
| WUSDT | IDLE | 2.23 | 4.46 | 0.0 | 0.07 | 368743.25 | 14.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 6.21 | 0.0 | 0.12 | 494720.04 | 22.17 | skipped_fast |
| BIOUSDT | IDLE | 2.25 | 5.01 | 0.65 | 0.04 | 185376.28 | 6.19 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.65 | 0.18 | 153852.42 | 8.95 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 4.12 | 0.66 | -0.04 | 82646.89 | 44.25 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.54 | 6.45 | 1.08 | 0.06 | 186707.29 | 31.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.02 | 10204.87 | 58.74 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.7 | 0.11 | 61290.16 | 11.01 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.77 | 0.06 | 56408.14 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.49 | 0.02 | 0.04 | 62416.35 | 6.16 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.33 | 0.0 | 0.04 | 54110.62 | 32.98 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
