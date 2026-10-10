# Hulk DIGEST — 2026-10-10T01:36:18Z

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
| WUSDT | IDLE | 1.33 | 5.71 | 1.74 | 0.11 | 2168548.98 | 12.59 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 2.43 | 0.21 | 0.01 | 1666788.28 | 2.46 | skipped_fast |
| XRPUSDT | IDLE | 0.76 | 1.5 | 0.09 | 0.01 | 26049766.5 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.7 | 0.05 | 0.0 | 173686868.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.53 | 0.18 | 0.01 | 282711203.3 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 3.25 | 1.58 | 0.02 | 1419484.15 | 0.81 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 3.23 | 2.27 | 0.02 | 617581.45 | 4.93 | skipped_fast |
| BIOUSDT | IDLE | 2.56 | 4.86 | 1.72 | 0.03 | 64097.4 | 6.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 6.01 | 0.1 | 0.07 | 84618.27 | 9.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.65 | 9.39 | 4.16 | 0.13 | 68762.66 | 36.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 3.07 | 2.32 | -0.05 | 241635.61 | 24.51 | skipped_fast |
| HBARUSDT | IDLE | 1.91 | 3.73 | 0.66 | 0.02 | 328677.5 | 3.26 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.3 | 0.83 | -0.04 | 76084.96 | 11.54 | skipped_fast |
| EDELUSDT | IDLE | 0.75 | 3.43 | 2.83 | 0.14 | 221096.75 | 15.03 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 3.05 | 0.91 | 0.02 | 62411.04 | 16.13 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 4.2 | 0.53 | 0.02 | 108624.62 | 42.74 | skipped_fast |
| RWAINCUSDT | IDLE | 0.75 | 1.59 | 1.57 | -0.01 | 10065.6 | 106.08 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.95 | 0.16 | -0.0 | 52065.46 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.29 | 0.09 | 0.01 | 41208.09 | 35.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 1.99 | 1.95 | 0.03 | 19428.41 | 16.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
