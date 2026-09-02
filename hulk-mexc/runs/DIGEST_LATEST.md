# Hulk DIGEST — 2026-09-02T08:26:28Z

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
| XRPUSDT | IDLE | 0.71 | 1.26 | 1.12 | -0.02 | 37608760.54 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 0.96 | 0.55 | -0.02 | 364324073.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.66 | 0.63 | -0.01 | 511520963.13 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 7.58 | 0.76 | 0.15 | 954502.39 | 15.24 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 7.01 | 2.34 | 0.12 | 819088.66 | 1.82 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 16.28 | 5.46 | 0.04 | 174008.13 | 32.52 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 4.06 | 3.86 | -0.08 | 340767.84 | 8.94 | skipped_fast |
| WUSDT | IDLE | 2.04 | 3.84 | 1.66 | 0.03 | 411133.88 | 15.5 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.37 | 10.57 | 0.84 | 0.1 | 10312.28 | 90.4 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 9.77 | 0.15 | 0.15 | 75193.69 | 9.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.67 | 1.86 | -0.01 | 215446.57 | 12.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 6.13 | 5.4 | -0.12 | 39305.13 | 78.72 | skipped_fast |
| QNTUSDT | IDLE | 2.53 | 6.12 | 2.67 | 0.07 | 63165.76 | 12.26 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 1.94 | 1.11 | -0.0 | 154716.99 | 9.89 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.18 | 1.01 | -0.03 | 74472.24 | 3.92 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.96 | 0.44 | -0.0 | 232244.28 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.73 | 0.59 | -0.01 | 87325.89 | 23.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.47 | 0.0 | -0.03 | 323.84 | 20.95 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.62 | 0.38 | -0.01 | 50671.97 | 7.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.34 | 0.66 | 0.11 | -0.01 | 35997.57 | 12.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
