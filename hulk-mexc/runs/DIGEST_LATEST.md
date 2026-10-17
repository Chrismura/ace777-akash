# Hulk DIGEST — 2026-10-17T02:52:42Z

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
| PYTHUSDT | IDLE | 1.16 | 3.74 | 3.37 | -0.09 | 1854282.12 | 1.17 | skipped_fast |
| WUSDT | IDLE | 2.15 | 5.35 | 4.88 | -0.04 | 1465885.41 | 18.45 | skipped_fast |
| XRPUSDT | IDLE | 0.47 | 0.88 | 0.46 | -0.02 | 27173852.36 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.73 | 0.21 | -0.01 | 199322928.38 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.49 | 0.39 | -0.01 | 315301654.17 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 3.34 | 2.7 | -0.03 | 752896.51 | 1.0 | skipped_fast |
| RIZEUSDT | IDLE | 3.21 | 7.21 | 3.01 | -0.03 | 50468.61 | 56.76 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 3.37 | 2.58 | -0.01 | 198792.3 | 21.58 | skipped_fast |
| CCUSDT | IDLE | 0.84 | 1.54 | 0.93 | -0.03 | 352352.08 | 7.75 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.27 | 2.86 | -0.05 | 80268.04 | 15.35 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 1.67 | 0.4 | 0.02 | 192336.49 | 13.5 | skipped_fast |
| CHIPUSDT | IDLE | 0.83 | 2.99 | 2.07 | -0.07 | 146323.51 | 13.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 5.31 | 3.54 | -0.1 | 26179.26 | 11.14 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.33 | 0.32 | -0.02 | 326660.33 | 8.3 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.68 | 1.44 | -0.02 | 57352.56 | 9.94 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 1.4 | 1.15 | -0.03 | 66868.93 | 8.0 | skipped_fast |
| TELUSDT | IDLE | 1.29 | 2.27 | 2.05 | -0.03 | 91479.65 | 23.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.3 | 0.56 | -0.0 | 33094.87 | 4.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.39 | 0.91 | 0.02 | 4783.15 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 52424.44 | 15.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
