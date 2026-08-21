# Hulk DIGEST — 2026-08-21T07:13:38Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.55 | 9.45 | 0.63 | 0.14 | 2540680.69 | 18.45 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 3.04 | 0.92 | 0.18 | 120994373.77 | 2.29 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 4.04 | 0.85 | 0.01 | 485757.2 | 9.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 7.93 | 4.61 | 0.15 | 468459.41 | 9.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 7.31 | 1.76 | 0.07 | 294972.82 | 31.08 | skipped_fast |
| RIZEUSDT | IDLE | 3.16 | 10.87 | 2.25 | -0.03 | 41371.44 | 70.18 | skipped_fast |
| BIOUSDT | IDLE | 1.79 | 5.07 | 1.79 | 0.05 | 224230.64 | 6.38 | skipped_fast |
| REDUSDT | IDLE | 2.0 | 6.07 | 1.83 | -0.08 | 128193.51 | 20.43 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.61 | 2.85 | 0.01 | 75434.02 | 21.72 | skipped_fast |
| WUSDT | IDLE | 0.87 | 1.69 | 0.38 | 0.06 | 271012.35 | 14.26 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.57 | 0.52 | 0.05 | 526773.06 | 1.33 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 2.63 | 0.0 | 0.06 | 61563.19 | 12.8 | skipped_fast |
| RWAINCUSDT | IDLE | 0.92 | 1.77 | 0.49 | 0.05 | 8620.89 | 54.85 | skipped_fast |
| QAITUSDT | IDLE | 0.95 | 2.36 | 0.78 | -0.02 | 5666.0 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 0.53 | 2.7 | 0.91 | 0.14 | 199346.15 | 37.87 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.62 | 0.34 | 0.03 | 54934.2 | 8.44 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 1.53 | 0.02 | 0.05 | 68775.44 | 6.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.6 | 1.11 | 0.07 | 2647.66 | 21.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
