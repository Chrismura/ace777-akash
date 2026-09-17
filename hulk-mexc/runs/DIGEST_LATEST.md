# Hulk DIGEST — 2026-09-17T12:16:26Z

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
| XRPUSDT | IDLE | 0.67 | 1.33 | 0.11 | 0.01 | 56704725.78 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.16 | 0.05 | 0.02 | 365440766.77 | 0.45 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.83 | 0.0 | 0.01 | 477033253.1 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 3.96 | 2.89 | 0.09 | 644946.24 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.7 | 8.24 | 3.98 | 0.02 | 139496.74 | 18.37 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 1.64 | 0.77 | 0.03 | 537193.14 | 5.54 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 6.56 | 2.75 | -0.11 | 206836.99 | 52.28 | skipped_fast |
| REDUSDT | IDLE | 2.12 | 4.14 | 2.88 | 0.01 | 64071.84 | 16.65 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 14.49 | 10.5 | -0.28 | 52448.84 | 66.03 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 4.73 | 4.43 | 0.05 | 67673.34 | 10.53 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.83 | 0.04 | 0.01 | 515290.02 | 1.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.23 | 0.75 | 0.01 | 172019.39 | 11.48 | skipped_fast |
| WUSDT | IDLE | 0.8 | 1.64 | 0.01 | 0.05 | 211482.93 | 11.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 2.93 | 2.73 | -0.0 | 17659.06 | 29.16 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.85 | 0.83 | 0.01 | 68716.19 | 15.87 | skipped_fast |
| RWAUSDT | IDLE | 1.69 | 3.31 | 0.52 | 0.02 | 58828.56 | 37.44 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.2 | 0.39 | 0.03 | 35260.36 | 4.86 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.17 | 0.48 | 0.0 | 106273.09 | 48.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.66 | 0.36 | 0.0 | 870.27 | 21.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.45 | 0.86 | 0.29 | 0.01 | 38847.15 | 74.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
