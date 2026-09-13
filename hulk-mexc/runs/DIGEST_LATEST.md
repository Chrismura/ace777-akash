# Hulk DIGEST — 2026-09-13T06:38:18Z

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
| XRPUSDT | IDLE | 0.3 | 0.54 | 0.35 | 0.0 | 13366799.51 | 2.93 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.34 | 0.26 | 0.0 | 189508333.34 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.1 | 0.19 | 0.07 | 0.0 | 278562864.65 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.09 | 34.95 | 19.33 | 0.11 | 94459.35 | 170.03 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 2.49 | 1.38 | 0.05 | 426173.71 | 1.82 | skipped_fast |
| WUSDT | IDLE | 1.8 | 3.25 | 2.36 | 0.03 | 223891.46 | 12.93 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.36 | 4.17 | -0.0 | 9552.41 | 27.56 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 3.65 | 0.5 | 0.03 | 63801.46 | 10.03 | skipped_fast |
| QNTUSDT | IDLE | 3.02 | 5.3 | 4.9 | 0.0 | 40879.33 | 6.25 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.68 | 0.97 | -0.01 | 237779.99 | 9.18 | skipped_fast |
| REDUSDT | IDLE | 1.66 | 3.11 | 1.41 | 0.04 | 55642.21 | 8.28 | skipped_fast |
| EDELUSDT | IDLE | 1.01 | 2.81 | 0.4 | 0.09 | 174629.27 | 16.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 2.77 | 2.03 | 0.0 | 77866.47 | 14.81 | skipped_fast |
| ZBCNUSDT | IDLE | 0.64 | 2.02 | 0.06 | 0.0 | 228446.91 | 2.23 | skipped_fast |
| RWAUSDT | IDLE | 2.62 | 4.61 | 4.2 | -0.0 | 56306.03 | 22.25 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.73 | 0.5 | 0.02 | 72856.33 | 3.89 | skipped_fast |
| FLUIDUSDT | IDLE | 2.2 | 4.0 | 2.63 | 0.01 | 1136.27 | 20.23 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 2.93 | 2.43 | -0.05 | 90918.9 | 68.43 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.22 | 0.15 | 0.02 | 123213.35 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.07 | -0.0 | 33260.39 | 16.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
