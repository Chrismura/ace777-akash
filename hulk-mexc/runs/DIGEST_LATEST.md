# Hulk DIGEST — 2026-09-19T10:57:26Z

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
| XRPUSDT | IDLE | 1.0 | 2.12 | 1.39 | 0.06 | 67962305.56 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.54 | 0.74 | 0.05 | 564372477.83 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.7 | 0.29 | 0.04 | 625654278.27 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.09 | 3.35 | 0.75 | 0.06 | 975252.72 | 3.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.69 | 3.13 | 1.61 | 0.01 | 720258.98 | 3.33 | skipped_fast |
| EDELUSDT | IDLE | 2.35 | 13.4 | 8.64 | -0.12 | 191007.42 | 86.5 | skipped_fast |
| HBARUSDT | IDLE | 1.66 | 3.25 | 0.5 | 0.03 | 603744.86 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.05 | 0.92 | 0.02 | 417601.48 | 8.13 | skipped_fast |
| KITEUSDT | IDLE | 2.45 | 4.7 | 1.27 | 0.05 | 70379.29 | 13.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 15.44 | 10.08 | -0.07 | 38811.09 | 101.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 5.26 | 3.97 | 0.03 | 144087.93 | 17.87 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 6.26 | 2.88 | 0.07 | 131426.79 | 14.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.46 | 0.61 | 0.01 | 179323.08 | 8.19 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.73 | 0.33 | 0.01 | 75898.89 | 10.94 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.02 | 0.35 | 0.02 | 75168.17 | 6.19 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.67 | 1.02 | 0.03 | 5364.76 | 62.55 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 2.32 | 1.58 | 0.04 | 121391.09 | 25.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.85 | 3.19 | 0.6 | 0.13 | 11029.54 | 21.86 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.41 | 0.73 | 0.0 | 56812.43 | 29.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.17 | 0.04 | 39690.34 | 2.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
