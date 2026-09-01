# Hulk DIGEST — 2026-09-01T13:25:03Z

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
| XRPUSDT | IDLE | 1.16 | 2.1 | 1.51 | 0.0 | 30397251.73 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 1.93 | 1.36 | -0.0 | 300903390.63 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.45 | 1.13 | -0.0 | 550294660.06 | 0.34 | skipped_fast |
| PYTHUSDT | IDLE | 2.46 | 5.52 | 2.33 | 0.07 | 590535.33 | 4.01 | skipped_fast |
| CHIPUSDT | IDLE | 3.04 | 6.55 | 0.17 | 0.03 | 385655.12 | 14.52 | skipped_fast |
| CCUSDT | IDLE | 2.64 | 4.64 | 4.21 | -0.02 | 403936.41 | 7.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 3.87 | 2.85 | 0.02 | 204661.65 | 12.51 | skipped_fast |
| WUSDT | IDLE | 1.66 | 3.1 | 1.5 | 0.04 | 237403.4 | 13.68 | skipped_fast |
| REDUSDT | IDLE | 2.14 | 3.89 | 2.64 | 0.02 | 63684.12 | 13.7 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 3.97 | 1.32 | -0.0 | 61049.94 | 10.86 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 5.64 | 4.76 | -0.05 | 177610.86 | 26.33 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 2.84 | 1.78 | -0.01 | 64662.11 | 7.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.49 | 4.79 | 2.54 | -0.09 | 38088.85 | 72.93 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 2.41 | 0.69 | 0.01 | 246629.69 | 1.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.97 | 1.95 | 0.0 | -0.01 | 4940.4 | 23.22 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 3.83 | 0.59 | 0.02 | 38831.92 | 7.98 | skipped_fast |
| RWAUSDT | IDLE | 1.48 | 3.5 | 1.88 | 0.02 | 63374.49 | 7.67 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.76 | 1.21 | 0.0 | 85514.66 | 46.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.56 | 0.43 | -0.0 | 32185.8 | 4.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 990.86 | 21.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
