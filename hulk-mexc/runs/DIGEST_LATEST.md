# Hulk DIGEST — 2026-10-23T19:51:09Z

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
| XRPUSDT | IDLE | 1.07 | 1.91 | 1.53 | -0.0 | 25600121.64 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.6 | 0.8 | 0.01 | 194837536.01 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.15 | 0.85 | -0.0 | 287905432.96 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.24 | 4.16 | 2.19 | -0.03 | 1180524.51 | 0.55 | skipped_fast |
| PYTHUSDT | IDLE | 2.39 | 4.23 | 3.73 | -0.04 | 765849.08 | 1.41 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.45 | 2.93 | -0.0 | 799937.05 | 15.16 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 4.54 | 3.85 | 0.01 | 518112.32 | 22.11 | skipped_fast |
| CHIPUSDT | IDLE | 2.65 | 5.06 | 3.72 | -0.01 | 105952.75 | 15.93 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 10.14 | 5.38 | 0.03 | 65372.16 | 59.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 3.66 | 2.3 | 0.03 | 203663.58 | 12.06 | skipped_fast |
| REDUSDT | IDLE | 2.56 | 4.7 | 2.76 | 0.01 | 57417.87 | 10.66 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 3.24 | 2.79 | 0.01 | 185558.37 | 8.78 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 4.04 | 0.22 | 0.05 | 47022.13 | 5.39 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.31 | 1.08 | 0.01 | 57372.27 | 10.8 | skipped_fast |
| LAUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 8.19 | 1.05 | 0.1 | 59465.86 | 18.66 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.71 | 2.1 | 0.01 | 74616.73 | 8.42 | skipped_fast |
| FLUIDUSDT | IDLE | 3.17 | 6.04 | 2.0 | 0.03 | 4490.66 | 21.3 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.02 | 2.71 | -0.01 | 241274.45 | 5.11 | skipped_fast |
| WAXLUSDT | IDLE | 2.09 | 3.69 | 3.25 | -0.01 | 57275.06 | 44.04 | skipped_fast |
| IOTAUSDT | IDLE | 1.66 | 3.01 | 2.04 | 0.01 | 70567.86 | 11.21 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | 0.01 | 51534.66 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.11 | -0.0 | 36159.42 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
