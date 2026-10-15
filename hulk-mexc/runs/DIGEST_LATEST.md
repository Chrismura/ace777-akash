# Hulk DIGEST — 2026-10-15T08:35:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.97 | 9.59 | 0.71 | 0.07 | 2769489.54 | 2.27 | skipped_fast |
| WUSDT | IDLE | 2.11 | 6.39 | 5.44 | -0.12 | 2767463.4 | 17.85 | skipped_fast |
| XRPUSDT | IDLE | 1.43 | 2.73 | 0.84 | -0.05 | 61313737.56 | 2.28 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.9 | 0.55 | -0.06 | 346979617.86 | 0.29 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.5 | 0.55 | -0.03 | 547839564.45 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.63 | 4.53 | 0.27 | -0.06 | 1158638.15 | 1.5 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 3.88 | 3.74 | -0.13 | 454788.67 | 8.42 | skipped_fast |
| RIZEUSDT | IDLE | 2.36 | 16.03 | 8.77 | -0.04 | 65230.59 | 57.45 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 4.59 | 3.48 | -0.08 | 204548.35 | 18.98 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.82 | 0.97 | -0.06 | 602491.0 | 7.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 8.26 | 6.54 | -0.22 | 122291.99 | 13.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.84 | 0.43 | -0.05 | 220211.82 | 18.6 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 3.98 | 2.05 | -0.1 | 84129.92 | 8.06 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.27 | 0.4 | 0.0 | 67239.48 | 13.86 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 3.59 | 1.19 | -0.13 | 68699.09 | 10.73 | skipped_fast |
| RWAINCUSDT | IDLE | 1.07 | 2.37 | 0.96 | 0.01 | 26131.19 | 30.57 | skipped_fast |
| FLUIDUSDT | IDLE | 1.98 | 5.96 | 3.91 | -0.05 | 20373.18 | 19.79 | skipped_fast |
| TELUSDT | IDLE | 1.07 | 2.0 | 0.92 | -0.05 | 100214.74 | 34.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.14 | 0.96 | -0.02 | 31322.77 | 19.99 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.48 | -0.04 | 54917.9 | 16.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
