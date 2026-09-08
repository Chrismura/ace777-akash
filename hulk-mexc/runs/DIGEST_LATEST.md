# Hulk DIGEST — 2026-09-08T05:48:17Z

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
| ETHUSDT | IDLE | 0.77 | 1.35 | 1.31 | -0.01 | 294104087.73 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.73 | 1.28 | 1.14 | -0.02 | 32682286.21 | 0.72 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.15 | 1.04 | -0.01 | 442716799.98 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 6.96 | 5.68 | -0.08 | 137918.07 | 11.7 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 9.25 | 7.2 | -0.06 | 50215.87 | 70.71 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.4 | 1.64 | -0.04 | 461014.81 | 7.56 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.95 | 8.28 | 1.91 | -0.04 | 89395.09 | 38.91 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.19 | 0.94 | -0.03 | 405311.93 | 1.85 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.82 | 2.11 | -0.01 | 235263.32 | 12.63 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 3.95 | 3.14 | -0.05 | 64156.86 | 9.22 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.37 | 1.96 | 0.0 | 500636.37 | 1.23 | skipped_fast |
| ZBCNUSDT | IDLE | 0.86 | 2.23 | 1.81 | -0.05 | 251723.19 | 5.09 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 2.33 | 1.34 | -0.01 | 63476.65 | 7.34 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 1.98 | 1.46 | 0.03 | 57611.01 | 9.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.43 | 4.15 | 3.98 | -0.11 | 3606.38 | 86.02 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.26 | 1.08 | -0.01 | 60189.44 | 7.56 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.53 | 1.22 | -0.02 | 78673.91 | 41.19 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.38 | 0.65 | 0.0 | 54449.08 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.16 | -0.01 | 36751.14 | 47.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.17 | 0.3 | 0.29 | 0.02 | 789.42 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
