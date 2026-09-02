# Hulk DIGEST — 2026-09-02T18:54:16Z

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
| XRPUSDT | IDLE | 1.1 | 2.15 | 0.37 | -0.01 | 37110322.81 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 1.04 | 1.93 | 1.04 | -0.01 | 374855795.63 | 0.13 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 10.05 | 2.56 | 0.16 | 1317166.98 | 3.46 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.26 | 0.3 | 0.0 | 517489169.3 | 0.3 | skipped_fast |
| CHIPUSDT | IDLE | 2.04 | 7.69 | 3.86 | -0.01 | 1054595.94 | 2.4 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.55 | 13.06 | 0.97 | 0.03 | 36941.78 | 70.4 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.6 | 0.64 | -0.01 | 340411.0 | 14.58 | skipped_fast |
| ZBCNUSDT | IDLE | 2.35 | 4.3 | 2.69 | -0.03 | 175886.75 | 18.48 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.04 | 357617.72 | 4.57 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 9.23 | 2.95 | 0.17 | 126036.14 | 7.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 4.8 | 2.24 | 0.07 | 9867.05 | 27.2 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 2.07 | 0.5 | 0.02 | 144649.11 | 11.23 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.43 | 0.93 | -0.01 | 68491.11 | 3.93 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.52 | 2.35 | 0.1 | 167453.16 | 33.14 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.4 | 0.99 | 0.03 | 59511.43 | 6.15 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 3.89 | 0.92 | 0.04 | 76948.49 | 52.37 | skipped_fast |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 1.74 | -0.02 | 1871.2 | 22.36 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.44 | 0.32 | -0.0 | 198778.52 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 1.29 | 2.47 | 0.75 | 0.02 | 51573.71 | 7.59 | skipped_fast |
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
