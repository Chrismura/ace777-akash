# Hulk DIGEST — 2026-08-22T15:34:37Z

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
| PYTHUSDT | IDLE | 1.57 | 7.62 | 0.86 | 0.04 | 51501920.24 | 1.96 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.49 | 5.18 | 0.03 | 214965306.29 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 5.65 | 3.58 | 0.07 | 795500.95 | 7.78 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.4 | -0.02 | 1160022.08 | 6.55 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.09 | -0.09 | 604319.37 | 3.39 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.57 | -0.02 | 557096.09 | 11.73 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.91 | 0.03 | 85190.71 | 10.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.72 | -0.05 | 321513.64 | 4.1 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.82 | -0.07 | 221122.06 | 6.61 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.04 | 78974.99 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.04 | -0.07 | 147833.58 | 13.81 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.27 | 0.03 | 56480.9 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.08 | -0.02 | 185220.46 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140566.18 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.67 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.65 | 0.02 | 57381.8 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
