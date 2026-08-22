# Hulk DIGEST — 2026-08-22T15:09:25Z

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
| PYTHUSDT | IDLE | 1.6 | 7.62 | 1.89 | 0.04 | 51476124.57 | 3.97 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.04 | 0.02 | 214514085.3 | 4.17 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.53 | 0.11 | 802285.96 | 9.42 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.38 | -0.02 | 1172972.68 | 5.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.52 | -0.11 | 614657.11 | 3.41 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.84 | -0.02 | 562480.41 | 12.85 | skipped_fast |
| KITEUSDT | IDLE | 2.76 | 6.37 | 2.03 | 0.03 | 83705.25 | 10.76 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.43 | -0.07 | 324551.52 | 26.1 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.01 | -0.06 | 225226.17 | 3.32 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 5.1 | 4.7 | -0.04 | 150719.06 | 12.89 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.04 | 79030.42 | 57.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.42 | 0.04 | 46503.03 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.05 | -0.01 | 188428.29 | 7.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 80.62 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.75 | 1.26 | 0.01 | 140817.32 | 53.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.72 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57322.4 | 24.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
