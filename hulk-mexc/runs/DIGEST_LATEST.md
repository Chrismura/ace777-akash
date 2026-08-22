# Hulk DIGEST — 2026-08-22T01:23:44Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 10.28 | 0.25 | 0.16 | 6686351.95 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.57 | 0.15 | 149951693.4 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.82 | 0.08 | 953098.02 | 2.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.92 | 0.11 | 546561.16 | 21.32 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.28 | 0.38 | 0.16 | 659724.69 | 7.88 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.65 | 1.11 | 0.09 | 392011.58 | 15.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.46 | -0.01 | 516945.25 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.57 | 0.94 | 0.04 | 186110.55 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.03 | 79585.22 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.21 | 0.11 | 60592.0 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.51 | 0.18 | 159026.92 | 15.13 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.99 | 0.07 | 170228.67 | 4.53 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 4.63 | 0.34 | 0.12 | 60847.94 | 10.84 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.05 | 181023.5 | 46.24 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.02 | 9586.1 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.82 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 55112.1 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
