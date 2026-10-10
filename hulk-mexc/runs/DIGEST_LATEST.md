# Hulk DIGEST — 2026-10-10T22:04:09Z

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
| ETHUSDT | IDLE | 0.32 | 0.58 | 0.4 | 0.01 | 109160165.33 | 0.44 | skipped_fast |
| XRPUSDT | IDLE | 0.26 | 0.48 | 0.3 | 0.01 | 13191751.17 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.14 | 0.01 | 166465693.03 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.06 | 3.34 | 2.29 | 0.04 | 1252294.88 | 14.16 | skipped_fast |
| CHIPUSDT | IDLE | 3.4 | 28.8 | 3.59 | 0.3 | 231919.86 | 13.48 | skipped_fast |
| QNTUSDT | IDLE | 0.99 | 1.74 | 1.66 | -0.03 | 1241369.29 | 2.09 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 1.64 | 0.69 | -0.02 | 779781.99 | 5.07 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.71 | 2.7 | -0.03 | 241039.58 | 72.46 | skipped_fast |
| RWAINCUSDT | IDLE | 2.21 | 4.24 | 1.16 | -0.02 | 9523.81 | 29.51 | skipped_fast |
| CCUSDT | IDLE | 0.67 | 1.3 | 0.25 | -0.02 | 293200.16 | 6.72 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 3.01 | 0.81 | 0.05 | 87368.69 | 13.56 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 2.37 | 1.85 | 0.07 | 61258.55 | 12.48 | skipped_fast |
| ZBCNUSDT | IDLE | 0.58 | 1.14 | 0.18 | 0.02 | 207544.93 | 27.28 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 3.46 | 1.76 | -0.02 | 136176.96 | 27.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 1.82 | 1.29 | -0.03 | 33827.79 | 56.32 | skipped_fast |
| REDUSDT | IDLE | 0.56 | 1.05 | 0.5 | 0.03 | 55102.95 | 14.58 | skipped_fast |
| HBARUSDT | IDLE | 0.43 | 0.79 | 0.46 | 0.02 | 311586.26 | 4.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.0 | 8504.7 | 21.34 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.0 | 53485.19 | 7.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.98 | 0.49 | -0.0 | 36505.46 | 72.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
