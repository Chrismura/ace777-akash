# Hulk DIGEST — 2026-09-16T09:11:58Z

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
| XRPUSDT | IDLE | 0.79 | 2.76 | 2.0 | -0.08 | 95701190.87 | 2.33 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.23 | 0.36 | -0.03 | 489798625.13 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.97 | 0.32 | -0.01 | 606174916.18 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.0 | 3.54 | 3.1 | -0.04 | 666083.77 | 1.91 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 19.06 | 11.85 | 0.43 | 428122.76 | 22.79 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 31.58 | 1.72 | 0.51 | 44845.95 | 68.99 | skipped_fast |
| REDUSDT | IDLE | 2.27 | 4.47 | 4.27 | -0.06 | 69001.96 | 9.24 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.88 | 1.43 | -0.04 | 372004.79 | 7.68 | skipped_fast |
| WUSDT | IDLE | 1.41 | 3.15 | 2.26 | -0.07 | 206414.27 | 11.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.11 | 3.79 | -0.11 | 117969.89 | 13.67 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 3.09 | 2.44 | -0.06 | 60121.41 | 14.02 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 2.49 | 1.33 | -0.06 | 211557.53 | 5.29 | skipped_fast |
| BIOUSDT | IDLE | 1.35 | 2.45 | 1.71 | -0.02 | 80180.0 | 4.05 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.22 | 0.48 | -0.04 | 464323.73 | 1.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.27 | 1.88 | -0.04 | 15003.91 | 23.2 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 2.94 | 2.41 | -0.06 | 45072.73 | 6.72 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 1.77 | 1.61 | -0.07 | 108010.68 | 54.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 1.98 | 1.65 | -0.06 | 1292.01 | 19.28 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.38 | 0.98 | -0.02 | 52329.11 | 22.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.48 | 0.14 | -0.02 | 30101.11 | 2.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
