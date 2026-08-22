# Hulk DIGEST — 2026-08-22T01:26:30Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.81 | 10.28 | 0.49 | 0.16 | 6707983.78 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 8.42 | 0.03 | 0.16 | 150048376.64 | 2.03 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.62 | 0.09 | 951179.21 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.78 | 0.11 | 545830.93 | 10.64 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 7.28 | 0.2 | 0.16 | 660746.55 | 6.11 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.65 | 1.1 | 0.09 | 391904.03 | 15.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.55 | -0.01 | 519693.06 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.79 | 0.04 | 186100.46 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79565.28 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.11 | 60631.67 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.58 | 0.18 | 159008.78 | 9.56 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.97 | 0.07 | 170183.46 | 7.54 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 4.63 | 0.28 | 0.12 | 60901.01 | 10.82 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.87 | 0.05 | 181120.96 | 46.45 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9552.36 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.84 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 55040.36 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
