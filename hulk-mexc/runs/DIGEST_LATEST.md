# Hulk DIGEST — 2026-09-26T19:02:11Z

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
| XRPUSDT | IDLE | 1.33 | 2.35 | 2.01 | -0.03 | 40315669.25 | 0.66 | skipped_fast |
| QNTUSDT | IDLE | 2.5 | 17.82 | 2.96 | 0.23 | 1414292.09 | 9.91 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.47 | 0.38 | -0.0 | 114372572.34 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.17 | 0.32 | 0.19 | 0.0 | 334223091.07 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.14 | 5.3 | 4.79 | 0.02 | 901081.63 | 5.24 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 3.33 | 1.8 | 0.06 | 977317.3 | 2.6 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 7.96 | 5.07 | 0.01 | 114985.99 | 16.09 | skipped_fast |
| WUSDT | IDLE | 2.18 | 5.01 | 0.97 | 0.08 | 543322.91 | 9.93 | skipped_fast |
| RWAINCUSDT | IDLE | 4.12 | 14.32 | 2.97 | 0.06 | 9600.94 | 53.23 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.03 | 8.92 | 0.61 | 0.1 | 83439.84 | 15.04 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.2 | 1.85 | 0.02 | 168605.51 | 3.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 3.55 | 3.3 | -0.05 | 208646.72 | 35.95 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.23 | 2.03 | -0.01 | 529932.71 | 1.07 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.45 | 2.21 | -0.02 | 109466.91 | 3.1 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.65 | 1.55 | -0.04 | 57829.21 | 8.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 2.16 | 1.37 | -0.01 | 49477.89 | 52.28 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 3.67 | 0.79 | -0.02 | 129976.34 | 67.71 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.23 | 0.78 | 0.03 | 56371.05 | 7.18 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.54 | 0.19 | -0.0 | 39605.35 | 38.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.49 | 0.28 | 0.01 | 559.59 | 19.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
