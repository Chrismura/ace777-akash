# Hulk DIGEST — 2026-09-15T11:45:25Z

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
| XRPUSDT | IDLE | 0.97 | 1.78 | 1.04 | -0.0 | 71585756.3 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.4 | 1.02 | -0.02 | 456702195.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.33 | 1.03 | -0.01 | 553382401.79 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 0.92 | 12.12 | 7.04 | 0.28 | 431098.0 | 37.95 | skipped_fast |
| PYTHUSDT | IDLE | 1.89 | 3.32 | 3.11 | -0.04 | 282537.72 | 1.86 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 4.56 | 1.02 | 0.04 | 212754.31 | 16.8 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.59 | 0.91 | -0.01 | 363515.32 | 4.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.77 | 17.54 | 2.58 | -0.05 | 51259.78 | 74.12 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.84 | 2.66 | -0.04 | 145024.04 | 10.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 3.61 | 2.18 | -0.02 | 81021.38 | 17.17 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.01 | 2.92 | -0.03 | 87981.1 | 4.01 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 6.23 | 1.87 | 0.0 | 122786.03 | 17.36 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 2.85 | 2.77 | -0.02 | 7575.63 | 5.58 | skipped_fast |
| HBARUSDT | IDLE | 1.15 | 2.12 | 1.22 | 0.0 | 365273.25 | 1.3 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 1.48 | 0.87 | 0.01 | 61420.92 | 14.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.82 | 3.18 | 3.08 | -0.03 | 2132.73 | 11.3 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 2.69 | 2.07 | -0.02 | 45611.04 | 3.18 | skipped_fast |
| TELUSDT | IDLE | 1.6 | 4.2 | 3.29 | -0.03 | 93366.53 | 57.86 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.9 | 0.82 | -0.01 | 53625.11 | 15.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.79 | 0.5 | 0.01 | 32164.69 | 26.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
