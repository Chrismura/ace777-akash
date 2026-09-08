# Hulk DIGEST — 2026-09-08T08:48:06Z

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
| XRPUSDT | IDLE | 0.63 | 1.2 | 0.39 | -0.01 | 30969700.43 | 2.15 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.04 | 0.59 | -0.01 | 602298828.56 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 1.0 | 0.21 | -0.0 | 290028211.32 | 0.12 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 3.28 | 2.71 | -0.04 | 444980.32 | 0.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 5.06 | 4.27 | -0.06 | 115727.21 | 13.82 | skipped_fast |
| HBARUSDT | IDLE | 1.58 | 2.84 | 2.09 | -0.01 | 553477.01 | 1.25 | skipped_fast |
| PYTHUSDT | IDLE | 1.0 | 1.84 | 1.05 | -0.03 | 381872.96 | 1.86 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 6.43 | 4.92 | -0.08 | 49246.5 | 61.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 3.17 | 1.65 | -0.05 | 213990.11 | 14.7 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.39 | 0.63 | 0.04 | 57288.93 | 16.55 | skipped_fast |
| WUSDT | IDLE | 0.85 | 1.68 | 0.07 | -0.0 | 193046.26 | 12.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.96 | 7.39 | 5.79 | -0.1 | 5168.41 | 104.89 | skipped_fast |
| EDELUSDT | IDLE | 1.1 | 2.39 | 0.97 | -0.02 | 87652.16 | 39.02 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.8 | 1.03 | -0.03 | 63908.22 | 13.44 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.48 | 0.26 | 0.0 | 66636.7 | 7.32 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.01 | 80349.19 | 69.44 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 1.51 | 0.12 | 0.01 | 59201.34 | 4.51 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.43 | 0.01 | 54215.96 | 21.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.29 | -0.01 | 35408.24 | 36.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.17 | 0.3 | 0.29 | 0.01 | 733.81 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
