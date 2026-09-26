# Hulk DIGEST — 2026-09-26T18:02:17Z

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
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 20.57 | 0.75 | 0.25 | 1357260.19 | 6.45 | skipped_fast |
| XRPUSDT | IDLE | 0.77 | 1.34 | 1.28 | -0.02 | 40189714.23 | 1.96 | skipped_fast |
| ETHUSDT | IDLE | 0.28 | 0.52 | 0.24 | 0.0 | 121328067.88 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.06 | 0.0 | 331651546.05 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.8 | 4.58 | 2.33 | 0.09 | 997847.59 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 3.82 | 2.89 | 0.07 | 928210.38 | 11.0 | skipped_fast |
| CHIPUSDT | IDLE | 4.27 | 8.54 | 4.0 | 0.05 | 114326.94 | 15.96 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.03 | 14.32 | 0.71 | 0.07 | 9368.52 | 28.72 | skipped_fast |
| WUSDT | IDLE | 2.16 | 4.88 | 1.97 | 0.08 | 470431.06 | 10.04 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.02 | 8.03 | 1.82 | 0.09 | 79780.08 | 9.07 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.2 | 1.5 | 0.04 | 164271.43 | 3.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 2.94 | 2.66 | -0.05 | 224934.83 | 15.98 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.42 | 1.33 | 0.01 | 539929.58 | 1.06 | skipped_fast |
| BIOUSDT | IDLE | 1.33 | 2.48 | 1.24 | -0.01 | 109970.59 | 9.2 | skipped_fast |
| REDUSDT | IDLE | 0.69 | 1.37 | 0.04 | -0.03 | 58171.61 | 6.48 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 2.16 | 1.45 | -0.08 | 41500.39 | 99.63 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.63 | 0.36 | 0.03 | 56041.44 | 14.29 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.22 | 0.0 | -0.03 | 125511.87 | 56.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.49 | 0.28 | 0.02 | 579.63 | 21.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.52 | 0.45 | 0.0 | 39894.03 | 48.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
