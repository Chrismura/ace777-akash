# Hulk DIGEST — 2026-09-25T06:43:00Z

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
| XRPUSDT | IDLE | 1.29 | 2.31 | 1.8 | 0.01 | 71889875.58 | 2.62 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.12 | 1.01 | -0.01 | 355069655.52 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.11 | 1.01 | -0.0 | 730985788.82 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 62.83 | 19.19 | 0.7 | 107743.39 | 51.99 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 2.72 | 1.6 | 0.06 | 1039070.93 | 5.85 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 2.57 | 2.3 | 0.0 | 926076.45 | 1.09 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.98 | 0.43 | 0.07 | 530337.23 | 6.0 | skipped_fast |
| KITEUSDT | IDLE | 2.77 | 4.95 | 4.0 | -0.03 | 67497.56 | 11.12 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.87 | 2.43 | 0.01 | 270230.24 | 8.6 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 5.4 | 4.11 | 0.06 | 135051.54 | 14.76 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 12.97 | 0.86 | 0.38 | 395656.25 | 10.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 5.4 | 4.85 | 0.08 | 105086.77 | 15.32 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 1.66 | 1.35 | 0.0 | 215486.52 | 19.12 | skipped_fast |
| EDELUSDT | IDLE | 0.55 | 5.96 | 3.76 | 0.08 | 187751.03 | 23.75 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 2.67 | 0.9 | 0.04 | 89496.76 | 6.49 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 4.86 | 2.95 | -0.05 | 107587.27 | 62.19 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 3.77 | 3.64 | 0.13 | 16774.76 | 28.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.41 | 0.42 | 0.01 | 40535.33 | 5.16 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.66 | 0.29 | 0.01 | 58880.13 | 7.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.33 | 0.66 | 0.0 | 0.03 | 1075.25 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
