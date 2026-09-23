# Hulk DIGEST — 2026-09-23T21:24:59Z

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
| XRPUSDT | IDLE | 0.96 | 2.64 | 1.81 | -0.05 | 112142339.27 | 2.01 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.7 | 0.29 | -0.03 | 494165210.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.24 | 0.24 | -0.02 | 841976995.2 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 5.45 | 1.47 | -0.05 | 1316734.48 | 3.2 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 2.29 | 1.06 | -0.09 | 1339831.15 | 1.11 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 3.34 | 0.02 | -0.03 | 542091.31 | 6.39 | skipped_fast |
| WUSDT | IDLE | 1.39 | 3.74 | 3.24 | -0.07 | 393657.16 | 6.27 | skipped_fast |
| KITEUSDT | IDLE | 2.23 | 4.29 | 3.52 | -0.05 | 174544.47 | 9.91 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 5.55 | 4.02 | -0.07 | 177467.05 | 21.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 5.01 | 3.11 | -0.07 | 220408.44 | 16.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 3.17 | 1.07 | 0.0 | 229520.85 | 27.7 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.42 | 3.14 | -0.05 | 59252.89 | 15.92 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 3.85 | 1.92 | -0.04 | 95414.67 | 7.11 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 3.04 | 2.79 | -0.05 | 174953.45 | 4.25 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 3.08 | 1.72 | -0.06 | 152156.48 | 29.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.68 | 3.58 | 1.97 | -0.05 | 4742.51 | 16.25 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.31 | 0.59 | -0.03 | 20364.86 | 59.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 7.08 | 4.49 | 0.16 | 70858.7 | 178.97 | skipped_fast |
| RWAUSDT | IDLE | 1.13 | 2.19 | 0.52 | -0.03 | 56384.08 | 14.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.75 | 0.04 | -0.01 | 40969.59 | 27.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
