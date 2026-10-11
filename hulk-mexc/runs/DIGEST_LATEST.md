# Hulk DIGEST — 2026-10-11T23:27:02Z

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
| WUSDT | IDLE | 2.48 | 22.27 | 6.23 | 0.24 | 4618236.73 | 10.06 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.32 | 0.42 | 0.0 | 16027832.61 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 1.04 | 0.25 | 0.01 | 208469454.19 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.24 | 0.01 | 149974015.25 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 4.34 | 1.82 | -0.0 | 906976.52 | 5.09 | skipped_fast |
| QNTUSDT | IDLE | 2.16 | 3.86 | 3.09 | -0.01 | 748961.36 | 1.68 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.81 | 3.18 | -0.03 | 371040.63 | 21.49 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 14.72 | 12.41 | 0.01 | 40130.1 | 47.89 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.32 | 1.58 | 0.06 | 358536.95 | 7.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.17 | 3.84 | 3.31 | -0.01 | 212098.26 | 11.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.03 | 4.07 | 2.38 | -0.01 | 263103.23 | 14.69 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.54 | 1.29 | 0.03 | 95790.41 | 3.34 | skipped_fast |
| TELUSDT | IDLE | 2.5 | 4.51 | 3.23 | -0.04 | 168946.94 | 41.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.52 | 3.98 | 3.73 | -0.01 | 28832.2 | 24.81 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.26 | 0.31 | 0.01 | 65343.27 | 11.66 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 2.13 | 0.52 | 0.02 | 302133.01 | 6.38 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.53 | 0.94 | 0.01 | 56302.42 | 8.58 | skipped_fast |
| RWAUSDT | IDLE | 1.42 | 2.57 | 1.82 | 0.02 | 52882.25 | 7.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.24 | 0.96 | 0.0 | 33381.2 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 2.51 | 0.28 | 0.07 | 61805.39 | 20.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
