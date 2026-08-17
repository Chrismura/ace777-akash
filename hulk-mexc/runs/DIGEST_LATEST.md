# Hulk DIGEST — 2026-08-17T01:07:12Z

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
| XRPUSDT | IDLE | 0.69 | 1.36 | 0.14 | -0.0 | 7236102.78 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 7.33 | 6.02 | -0.02 | 296126.61 | 18.02 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.26 | 8.75 | 0.63 | 0.05 | 37314.6 | 57.86 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.94 | 1.16 | -0.04 | 333016.33 | 8.39 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.64 | 1.02 | -0.01 | 150581.47 | 2.58 | skipped_fast |
| WUSDT | IDLE | 1.39 | 2.74 | 0.25 | 0.02 | 182777.79 | 20.93 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 3.05 | 1.29 | 0.04 | 56141.35 | 39.09 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.21 | 1.39 | -0.02 | 63118.71 | 8.27 | skipped_fast |
| ZBCNUSDT | IDLE | 0.72 | 1.4 | 0.32 | -0.01 | 189012.93 | 17.78 | skipped_fast |
| REDUSDT | IDLE | 0.77 | 1.42 | 0.81 | -0.03 | 61633.73 | 14.99 | skipped_fast |
| KITEUSDT | IDLE | 0.49 | 0.92 | 0.37 | -0.02 | 54414.1 | 23.48 | skipped_fast |
| QAITUSDT | IDLE | 0.85 | 2.41 | 0.0 | -0.01 | 2196.8 | 61.3 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.53 | 1.63 | -0.03 | 33574.29 | 7.11 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.94 | 0.48 | -0.0 | 95869.46 | 47.77 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 1.31 | 0.34 | 0.04 | 4885.76 | 96.45 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.41 | 0.51 | -0.01 | 95750.6 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.7 | 0.43 | -0.0 | 50481.52 | 17.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.16 | 0.22 | 0.02 | 250.61 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
