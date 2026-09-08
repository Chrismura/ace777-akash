# Hulk DIGEST — 2026-09-08T05:39:08Z

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
| ETHUSDT | IDLE | 0.76 | 1.34 | 1.18 | -0.01 | 294239395.37 | 0.48 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.28 | 1.05 | -0.02 | 32573054.26 | 2.16 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.15 | 0.93 | -0.01 | 440844951.67 | 0.15 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 9.25 | 5.6 | -0.04 | 49699.87 | 34.94 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 6.96 | 5.61 | -0.08 | 139987.5 | 11.71 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 2.4 | 1.44 | -0.04 | 460195.21 | 9.43 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.95 | 8.28 | 1.91 | -0.04 | 89395.09 | 38.91 | skipped_fast |
| PYTHUSDT | IDLE | 1.18 | 2.19 | 1.16 | -0.03 | 405578.15 | 1.86 | skipped_fast |
| WUSDT | IDLE | 1.56 | 2.82 | 1.98 | -0.01 | 234871.82 | 14.55 | skipped_fast |
| KITEUSDT | IDLE | 2.2 | 3.95 | 2.95 | -0.05 | 63975.18 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.37 | 1.98 | 0.0 | 500060.96 | 1.23 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 2.23 | 1.38 | -0.05 | 251627.83 | 14.1 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.33 | 1.3 | -0.01 | 63307.1 | 3.67 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 1.98 | 1.38 | 0.03 | 57732.61 | 10.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.32 | 3.7 | 3.52 | -0.1 | 3606.96 | 75.27 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.26 | 1.08 | -0.01 | 60227.82 | 9.07 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.53 | 1.22 | -0.02 | 78498.94 | 41.19 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.38 | 0.57 | 0.0 | 54454.8 | 21.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.43 | -0.01 | 36878.42 | 46.27 | skipped_fast |
| FLUIDUSDT | IDLE | 0.17 | 0.3 | 0.29 | 0.02 | 789.42 | 20.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
