# Hulk DIGEST — 2026-09-28T09:19:41Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 10.62 | 8.84 | -0.11 | 4174357.42 | 10.85 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.7 | 20.84 | 0.72 | 0.19 | 3614660.67 | 8.86 | skipped_fast |
| QNTUSDT | IDLE | 1.01 | 31.69 | 21.24 | 0.29 | 18206733.07 | 11.8 | skipped_fast |
| PYTHUSDT | IDLE | 2.06 | 5.64 | 2.77 | -0.03 | 1691077.57 | 3.7 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 2.0 | 1.12 | -0.03 | 51328328.92 | 2.02 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.79 | -0.02 | 643330873.46 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.91 | 0.38 | -0.02 | 300013814.54 | 0.11 | skipped_fast |
| CCUSDT | IDLE | 3.24 | 7.77 | 2.64 | 0.02 | 984122.64 | 6.43 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 8.04 | 5.57 | -0.09 | 106171.91 | 10.82 | skipped_fast |
| BIOUSDT | IDLE | 2.12 | 5.16 | 3.64 | -0.07 | 102752.73 | 6.74 | skipped_fast |
| TELUSDT | IDLE | 3.06 | 5.74 | 4.56 | 0.01 | 175082.06 | 44.99 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 3.69 | 2.84 | -0.06 | 62853.65 | 14.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 2.43 | 1.74 | -0.05 | 206108.47 | 26.91 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 5.59 | 2.01 | -0.11 | 181190.12 | 31.63 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 3.8 | 1.68 | -0.1 | 89609.52 | 11.21 | skipped_fast |
| FLUIDUSDT | IDLE | 2.02 | 4.02 | 3.86 | -0.05 | 3627.16 | 22.17 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 6.09 | 5.7 | 0.14 | 31916.21 | 81.93 | skipped_fast |
| RIZEUSDT | IDLE | 0.23 | 1.34 | 0.84 | -0.15 | 59320.3 | 54.55 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.74 | 1.57 | -0.03 | 59203.1 | 43.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.75 | 0.13 | -0.01 | 36465.47 | 56.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
