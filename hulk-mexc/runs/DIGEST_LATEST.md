# Hulk DIGEST — 2026-09-02T18:52:49Z

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
| XRPUSDT | IDLE | 1.1 | 2.15 | 0.39 | -0.01 | 37194504.01 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 1.04 | 1.93 | 1.03 | -0.0 | 375779629.15 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 10.05 | 2.56 | 0.16 | 1316883.07 | 3.46 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.26 | 0.28 | 0.01 | 519885427.3 | 0.05 | skipped_fast |
| CHIPUSDT | IDLE | 2.03 | 7.69 | 3.77 | -0.01 | 1054261.87 | 4.8 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.55 | 13.06 | 1.05 | 0.02 | 36943.92 | 70.4 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.6 | 0.59 | -0.01 | 340440.07 | 13.54 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 4.3 | 2.8 | -0.03 | 175850.34 | 26.36 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.52 | 2.15 | -0.04 | 357632.78 | 6.4 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 9.23 | 3.03 | 0.17 | 126024.46 | 10.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 4.8 | 2.24 | 0.07 | 9867.05 | 27.2 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 2.07 | 0.52 | 0.02 | 144637.98 | 11.25 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.43 | 0.97 | -0.01 | 68457.74 | 3.93 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.52 | 2.35 | 0.11 | 167449.6 | 33.17 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.4 | 0.9 | 0.03 | 59714.29 | 6.14 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 3.89 | 0.92 | 0.04 | 76919.6 | 52.37 | skipped_fast |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 1.74 | -0.02 | 1871.2 | 21.58 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.44 | 0.28 | -0.0 | 198877.95 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 1.29 | 2.47 | 0.75 | 0.02 | 51543.84 | 7.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.12 | -0.0 | 30472.11 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
