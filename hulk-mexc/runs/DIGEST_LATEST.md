# Hulk DIGEST — 2026-08-21T09:13:43Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 12.07 | 5.42 | 0.08 | 2985727.09 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 1.52 | 7.96 | 2.52 | 0.18 | 135292102.33 | 0.73 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 4.17 | 2.04 | -0.02 | 509313.7 | 9.73 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.68 | 18.41 | 5.0 | 0.01 | 42123.94 | 45.71 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 6.77 | 4.14 | -0.06 | 200267.57 | 6.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 6.59 | 5.58 | 0.14 | 505141.97 | 6.13 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 9.37 | 0.77 | 0.09 | 376218.2 | 21.95 | skipped_fast |
| WUSDT | IDLE | 2.23 | 4.67 | 1.92 | 0.05 | 293154.21 | 17.28 | skipped_fast |
| HBARUSDT | IDLE | 1.9 | 3.45 | 2.31 | 0.04 | 577626.81 | 1.32 | skipped_fast |
| KITEUSDT | IDLE | 2.54 | 6.07 | 1.14 | 0.08 | 62642.49 | 12.48 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 6.34 | 1.37 | -0.01 | 115637.13 | 11.1 | skipped_fast |
| EDELUSDT | IDLE | 2.18 | 3.94 | 2.74 | 0.04 | 80035.88 | 32.56 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 9.86 | 2.41 | 0.18 | 223810.02 | 46.31 | skipped_fast |
| QAITUSDT | IDLE | 1.6 | 2.91 | 1.94 | -0.04 | 5449.59 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 2.07 | 3.98 | 1.11 | 0.03 | 74321.48 | 14.22 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 1.71 | 1.19 | 0.03 | 8577.73 | 16.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.92 | 3.84 | 0.0 | 0.07 | 2712.83 | 21.65 | skipped_fast |
| RWAUSDT | IDLE | 1.33 | 2.65 | 0.08 | 0.04 | 55173.71 | 16.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
