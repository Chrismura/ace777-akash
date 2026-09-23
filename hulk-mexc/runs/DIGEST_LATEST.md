# Hulk DIGEST — 2026-09-23T01:16:27Z

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
| PYTHUSDT | IDLE | 1.03 | 4.83 | 2.33 | 0.04 | 1757788.83 | 1.5 | skipped_fast |
| XRPUSDT | IDLE | 1.42 | 2.83 | 0.11 | 0.06 | 103968654.91 | 1.88 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.41 | 0.19 | 0.01 | 409544751.67 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.95 | 0.17 | 0.01 | 893465815.54 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 2.43 | 0.81 | 0.08 | 1760188.98 | 1.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.15 | 36.45 | 2.72 | 0.27 | 45384.08 | 42.95 | skipped_fast |
| WUSDT | IDLE | 2.13 | 4.04 | 1.42 | 0.03 | 317257.18 | 1.64 | skipped_fast |
| CHIPUSDT | IDLE | 2.73 | 5.6 | 1.04 | 0.0 | 133182.37 | 21.34 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 2.52 | 0.47 | -0.02 | 426546.73 | 3.46 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 6.94 | 3.32 | -0.01 | 260955.47 | 36.66 | skipped_fast |
| BIOUSDT | IDLE | 1.9 | 3.77 | 0.17 | 0.04 | 138293.12 | 13.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.08 | 2.15 | 0.03 | 0.01 | 202456.24 | 5.88 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.17 | 1.02 | 0.03 | 62607.8 | 9.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 3.01 | 2.71 | 0.02 | 19954.49 | 16.12 | skipped_fast |
| KITEUSDT | IDLE | 0.64 | 2.75 | 0.73 | 0.16 | 112863.69 | 7.18 | skipped_fast |
| QNTUSDT | IDLE | 1.4 | 4.62 | 0.15 | 0.13 | 209446.87 | 5.34 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 4.04 | 0.75 | 0.12 | 104216.68 | 38.01 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.02 | 0.43 | 0.0 | 52625.65 | 14.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.86 | 0.13 | 0.01 | 5479.9 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.29 | 0.0 | 40206.41 | 35.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
