# Hulk DIGEST — 2026-08-22T01:25:22Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.81 | 10.28 | 0.45 | 0.15 | 6698268.45 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.16 | 8.4 | 0.11 | 0.16 | 150008689.24 | 6.08 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.62 | 0.09 | 951004.97 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.81 | 0.11 | 545742.36 | 14.52 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.28 | 0.3 | 0.16 | 660538.42 | 12.24 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.65 | 1.22 | 0.09 | 391979.3 | 14.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.46 | -0.01 | 516866.29 | 12.35 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.88 | 0.04 | 186093.48 | 6.15 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.03 | 79565.24 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.11 | 60622.09 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.61 | 0.18 | 158977.94 | 9.56 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.96 | 0.07 | 170218.73 | 6.03 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 4.63 | 0.2 | 0.12 | 60855.35 | 10.82 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.06 | 181026.78 | 41.17 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9586.1 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 20.39 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 55102.74 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
