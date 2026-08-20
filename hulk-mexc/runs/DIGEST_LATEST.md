# Hulk DIGEST — 2026-08-20T16:13:43Z

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
| XRPUSDT | IDLE | 1.88 | 9.51 | 0.91 | 0.17 | 76150401.73 | 2.39 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 4.1 | 1.96 | 0.1 | 1111009.41 | 2.27 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 12.28 | 5.97 | 0.07 | 253073.31 | 25.63 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.79 | 8.61 | 1.48 | 0.11 | 281864.94 | 9.78 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 3.09 | 2.22 | 0.11 | 493480.34 | 7.79 | skipped_fast |
| BIOUSDT | IDLE | 1.71 | 8.96 | 6.91 | 0.06 | 245878.74 | 6.55 | skipped_fast |
| WUSDT | IDLE | 1.66 | 3.21 | 0.73 | 0.05 | 319455.14 | 12.38 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 8.34 | 6.44 | 0.12 | 200753.24 | 20.09 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.09 | 0.53 | 0.06 | 444584.82 | 1.36 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 9.41 | 0.66 | 0.17 | 163228.86 | 27.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 7.23 | 3.26 | 0.09 | 64548.05 | 46.1 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.69 | 0.05 | 0.03 | 59036.06 | 25.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.54 | 2.95 | 0.83 | 0.02 | 7310.21 | 27.79 | skipped_fast |
| EDELUSDT | IDLE | 0.57 | 2.94 | 0.55 | 0.15 | 100927.88 | 22.1 | skipped_fast |
| QAITUSDT | IDLE | 1.0 | 2.01 | 0.0 | 0.02 | 5651.22 | 46.39 | skipped_fast |
| QNTUSDT | IDLE | 0.96 | 2.09 | 0.82 | 0.06 | 62264.29 | 6.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 1.49 | 0.01 | 0.06 | 3296.15 | 21.99 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.86 | 0.43 | 0.01 | 52178.75 | 17.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
