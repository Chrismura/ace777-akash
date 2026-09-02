# Hulk DIGEST — 2026-09-02T04:31:40Z

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
| XRPUSDT | IDLE | 1.21 | 2.29 | 0.88 | -0.03 | 38111116.06 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.78 | 0.55 | -0.03 | 365994559.33 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.39 | 0.44 | -0.02 | 525437226.3 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.09 | 7.79 | 0.04 | 0.1 | 697083.68 | 3.6 | skipped_fast |
| CHIPUSDT | IDLE | 0.95 | 4.55 | 2.56 | 0.14 | 844537.42 | 2.3 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.77 | 1.53 | 0.01 | 423083.37 | 14.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 4.28 | 1.54 | -0.02 | 193372.01 | 2.18 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 3.09 | 1.57 | -0.07 | 329162.78 | 10.48 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 4.92 | 3.97 | 0.05 | 143297.14 | 9.85 | skipped_fast |
| RWAINCUSDT | IDLE | 2.6 | 5.01 | 1.29 | 0.04 | 5766.87 | 34.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 6.78 | 5.19 | -0.07 | 42812.69 | 78.33 | skipped_fast |
| EDELUSDT | IDLE | 1.04 | 9.51 | 1.74 | -0.0 | 178924.23 | 26.51 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 3.06 | 0.81 | 0.06 | 69332.43 | 10.36 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.43 | 0.62 | -0.04 | 71146.19 | 3.91 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.54 | 0.47 | -0.01 | 89476.68 | 23.7 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.45 | 0.5 | -0.01 | 270279.97 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.1 | 0.82 | 0.04 | 48247.04 | 1.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.04 | 0.7 | -0.04 | 310.5 | 21.92 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.77 | 0.46 | -0.06 | 56419.27 | 15.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.7 | 0.1 | -0.02 | 36493.13 | 52.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
