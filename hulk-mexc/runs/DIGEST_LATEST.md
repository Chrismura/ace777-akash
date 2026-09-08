# Hulk DIGEST — 2026-09-08T02:37:45Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.89 | 1.71 | 0.5 | -0.01 | 34714579.78 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.27 | 0.55 | -0.01 | 316572968.68 | 0.16 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.85 | 0.35 | -0.01 | 432507208.01 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 3.62 | 11.02 | 3.72 | 0.02 | 53673.44 | 63.52 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 3.52 | 0.62 | -0.04 | 440581.78 | 10.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 2.29 | 1.59 | -0.05 | 417248.54 | 3.7 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 9.19 | 1.63 | -0.04 | 111071.59 | 19.42 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.5 | 1.66 | -0.01 | 246437.16 | 14.5 | skipped_fast |
| KITEUSDT | IDLE | 2.34 | 4.48 | 1.62 | -0.04 | 62467.01 | 10.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 3.04 | 1.89 | -0.04 | 238757.98 | 15.18 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.83 | 0.58 | 0.01 | 512222.93 | 1.21 | skipped_fast |
| BIOUSDT | IDLE | 1.35 | 2.56 | 0.91 | 0.0 | 64571.77 | 3.66 | skipped_fast |
| CHIPUSDT | IDLE | 0.65 | 2.08 | 1.29 | -0.08 | 203500.47 | 13.03 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.09 | 1.28 | 0.04 | 58350.89 | 18.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.24 | 3.65 | 1.48 | -0.07 | 3948.9 | 30.99 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.52 | 0.88 | -0.01 | 60487.23 | 10.55 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.95 | 0.81 | -0.02 | 80847.4 | 46.81 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.36 | -0.01 | 53027.11 | 14.51 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.65 | -0.02 | 37567.53 | 19.12 | skipped_fast |
| FLUIDUSDT | IDLE | 0.03 | 0.05 | 0.0 | 0.02 | 1077.86 | 22.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
