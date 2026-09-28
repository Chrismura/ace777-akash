# Hulk DIGEST — 2026-09-28T17:41:37Z

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
| WUSDT | IDLE | 1.79 | 8.49 | 5.81 | -0.12 | 2728749.94 | 8.76 | skipped_fast |
| XRPUSDT | IDLE | 2.12 | 3.98 | 1.67 | -0.01 | 66612018.99 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 13.13 | 1.03 | 0.38 | 9999263.01 | 3.87 | skipped_fast |
| QNTUSDT | IDLE | 0.64 | 16.43 | 2.57 | 0.35 | 21875575.24 | 4.85 | skipped_fast |
| ETHUSDT | IDLE | 1.33 | 2.55 | 0.78 | 0.0 | 393430491.24 | 1.0 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 2.14 | 0.5 | -0.01 | 817545373.97 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.33 | 5.98 | 3.79 | -0.07 | 1341706.87 | 3.77 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 5.56 | 0.59 | -0.02 | 1373424.2 | 10.57 | skipped_fast |
| CHIPUSDT | IDLE | 2.76 | 6.46 | 4.46 | -0.07 | 69436.9 | 15.91 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.61 | 8.9 | 0.16 | 0.04 | 153960.72 | 25.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 9.21 | 5.66 | 0.12 | 15793.21 | 24.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.53 | 1.29 | -0.04 | 237230.61 | 6.96 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 4.83 | 2.06 | -0.07 | 112593.26 | 3.39 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 6.35 | 1.34 | -0.09 | 101661.52 | 10.76 | skipped_fast |
| REDUSDT | IDLE | 1.95 | 4.49 | 2.19 | -0.05 | 61645.42 | 14.87 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 6.44 | 3.72 | 0.08 | 191027.61 | 27.3 | skipped_fast |
| RIZEUSDT | IDLE | 0.44 | 2.69 | 0.21 | -0.12 | 66984.7 | 50.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 3.66 | 0.0 | -0.04 | 3933.8 | 21.81 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.67 | 0.21 | -0.01 | 61009.75 | 28.55 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.96 | 0.63 | -0.02 | 34401.07 | 29.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
