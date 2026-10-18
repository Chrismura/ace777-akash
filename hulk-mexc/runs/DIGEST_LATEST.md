# Hulk DIGEST — 2026-10-18T16:04:58Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 8.52 | 5.88 | -0.1 | 1501165.17 | 13.32 | skipped_fast |
| XRPUSDT | IDLE | 1.48 | 2.59 | 2.46 | -0.02 | 24441562.91 | 1.58 | skipped_fast |
| ETHUSDT | IDLE | 1.27 | 2.24 | 2.06 | -0.02 | 95664514.12 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.38 | 1.26 | -0.0 | 221316984.97 | 0.04 | skipped_fast |
| WUSDT | IDLE | 1.72 | 4.1 | 2.71 | -0.06 | 991475.16 | 14.54 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 18.12 | 15.34 | -0.01 | 58881.2 | 48.91 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.08 | 12.83 | 1.74 | 0.09 | 29901.1 | 9.73 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 5.39 | 4.48 | 0.03 | 701086.18 | 8.16 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 6.26 | 5.4 | -0.06 | 479795.99 | 3.17 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 3.07 | 2.51 | -0.06 | 250485.42 | 7.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 5.03 | 4.53 | -0.08 | 74146.99 | 9.89 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 3.72 | 2.69 | -0.03 | 95230.24 | 16.96 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.46 | 3.01 | -0.05 | 83942.51 | 4.31 | skipped_fast |
| EDELUSDT | IDLE | 1.53 | 3.69 | 2.26 | -0.08 | 228666.15 | 34.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.68 | 1.96 | -0.03 | 196795.1 | 25.13 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 3.07 | 2.46 | -0.04 | 70865.86 | 13.27 | skipped_fast |
| FLUIDUSDT | IDLE | 2.67 | 4.71 | 4.17 | -0.03 | 3613.52 | 21.46 | skipped_fast |
| LAUSDT | IDLE | 2.24 | 4.74 | 4.27 | -0.07 | 58045.93 | 27.0 | skipped_fast |
| IOTAUSDT | IDLE | 1.95 | 3.46 | 2.95 | -0.05 | 68473.88 | 27.24 | skipped_fast |
| WAXLUSDT | IDLE | 1.71 | 7.51 | 5.68 | -0.03 | 73614.57 | 50.04 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.53 | 0.87 | -0.01 | 50262.25 | 16.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.59 | 0.27 | -0.01 | 35093.45 | 55.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
