# Hulk DIGEST — 2026-08-22T01:33:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.5 | 0.16 | 6751279.61 | 3.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 8.72 | 0.18 | 0.15 | 150318938.23 | 6.74 | skipped_fast |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.52 | 0.08 | 950413.64 | 2.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.85 | 0.1 | 547086.12 | 12.1 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.32 | 0.1 | 0.16 | 661310.69 | 9.59 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 1.05 | 0.09 | 391930.64 | 13.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.58 | -0.01 | 513334.51 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.57 | 1.19 | 0.04 | 186092.65 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79541.2 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.98 | 0.12 | 60721.0 | 20.39 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.51 | 0.17 | 158629.12 | 18.31 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.23 | 0.05 | 181534.73 | 15.55 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.94 | 0.07 | 170105.99 | 6.02 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 4.93 | 0.0 | 0.12 | 61001.83 | 14.36 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 42.83 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54879.49 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
