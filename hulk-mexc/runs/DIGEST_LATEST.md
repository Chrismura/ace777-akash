# Hulk DIGEST — 2026-10-11T03:04:38Z

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
| XRPUSDT | IDLE | 0.42 | 0.75 | 0.54 | -0.01 | 11609112.09 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.42 | 0.11 | 0.01 | 137006081.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.1 | 0.01 | 144890957.73 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.16 | 3.66 | 2.48 | 0.02 | 1219236.93 | 6.83 | skipped_fast |
| QNTUSDT | IDLE | 1.18 | 2.14 | 1.53 | -0.05 | 1303524.52 | 0.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 3.68 | 0.0 | -0.01 | 782564.95 | 1.25 | skipped_fast |
| RIZEUSDT | IDLE | 3.16 | 6.26 | 4.83 | -0.06 | 33318.56 | 39.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.03 | 9.26 | 6.09 | 0.29 | 279149.77 | 8.85 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 2.98 | 1.49 | -0.04 | 282836.53 | 13.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.85 | 1.29 | 0.01 | 171745.73 | 13.98 | skipped_fast |
| CCUSDT | IDLE | 0.69 | 1.33 | 0.28 | -0.02 | 228284.41 | 8.37 | skipped_fast |
| BIOUSDT | IDLE | 1.22 | 2.18 | 1.76 | 0.0 | 89660.54 | 6.9 | skipped_fast |
| KITEUSDT | IDLE | 0.78 | 1.53 | 1.03 | 0.05 | 75200.88 | 10.23 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 1.16 | 1.14 | -0.01 | 57200.73 | 14.73 | skipped_fast |
| TELUSDT | IDLE | 1.66 | 3.29 | 2.35 | -0.05 | 136910.59 | 28.63 | skipped_fast |
| RWAINCUSDT | IDLE | 0.73 | 1.29 | 1.08 | -0.03 | 13812.56 | 4.92 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.1 | 0.81 | -0.01 | 306766.13 | 8.69 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.35 | 2.19 | 0.0 | 7833.02 | 21.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.81 | 1.51 | 0.79 | -0.01 | 35475.28 | 60.1 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 53733.24 | 15.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
