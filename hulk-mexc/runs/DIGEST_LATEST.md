# Hulk DIGEST — 2026-09-03T02:06:18Z

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
| XRPUSDT | IDLE | 1.04 | 1.95 | 0.91 | 0.02 | 35724594.02 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.06 | 0.5 | -0.01 | 340484466.41 | 0.38 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.73 | 0.32 | 0.0 | 489784407.61 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.08 | 3.37 | 0.65 | 0.1 | 1326289.06 | 1.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 4.43 | 1.11 | -0.01 | 885017.82 | 2.34 | skipped_fast |
| REDUSDT | IDLE | 3.01 | 9.52 | 2.09 | 0.09 | 108220.8 | 19.64 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 2.14 | 1.27 | -0.04 | 417248.06 | 6.41 | skipped_fast |
| BIOUSDT | IDLE | 2.22 | 4.26 | 1.22 | 0.03 | 74711.93 | 3.87 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 6.15 | 4.86 | -0.0 | 140902.87 | 8.94 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.83 | 1.18 | 0.03 | 217389.84 | 13.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.34 | 1.17 | 0.0 | 177872.11 | 12.83 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 4.06 | 2.36 | 0.14 | 141429.04 | 10.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 4.38 | 0.0 | 0.11 | 12067.92 | 5.23 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 16.32 | 12.12 | 0.09 | 56001.54 | 269.12 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.14 | 0.56 | 0.03 | 197778.62 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.96 | 1.79 | 0.89 | 0.01 | 61197.2 | 6.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 1.31 | 1.29 | -0.01 | 2783.22 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 1.0 | 0.23 | 0.01 | 51612.42 | 15.21 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.6 | 0.12 | 0.04 | 73933.3 | 64.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.48 | 0.41 | -0.0 | 17869.38 | 4.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
