# Hulk DIGEST — 2026-09-15T12:36:09Z

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
| XRPUSDT | IDLE | 0.87 | 1.68 | 0.39 | 0.0 | 72042253.87 | 2.85 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.41 | -0.02 | 457221314.18 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.78 | 0.48 | -0.01 | 557146831.81 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.45 | 4.56 | 2.26 | 0.03 | 212260.78 | 27.45 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 10.5 | 5.48 | 0.3 | 427649.91 | 36.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.74 | 3.12 | 2.34 | -0.03 | 277040.04 | 1.85 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 4.44 | 3.72 | -0.06 | 86118.72 | 17.44 | skipped_fast |
| RIZEUSDT | IDLE | 2.16 | 21.18 | 2.74 | -0.03 | 52378.88 | 97.82 | skipped_fast |
| CCUSDT | IDLE | 0.73 | 1.35 | 0.68 | -0.01 | 360966.55 | 8.41 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 6.23 | 2.75 | -0.01 | 122945.4 | 18.22 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.73 | 1.92 | -0.02 | 88478.4 | 7.97 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.29 | 1.43 | -0.03 | 140473.83 | 15.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 2.85 | 2.71 | -0.02 | 8043.88 | 5.58 | skipped_fast |
| HBARUSDT | IDLE | 1.28 | 2.57 | 0.0 | 0.01 | 381490.56 | 1.28 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.39 | 0.44 | 0.0 | 61223.39 | 10.29 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.91 | 2.82 | -0.03 | 92950.9 | 6.46 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.18 | 1.83 | -0.02 | 45199.81 | 7.98 | skipped_fast |
| FLUIDUSDT | IDLE | 1.47 | 2.57 | 2.5 | -0.04 | 2132.73 | 22.43 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 0.98 | 0.89 | -0.01 | 52996.36 | 7.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.43 | 0.01 | 31510.34 | 24.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
