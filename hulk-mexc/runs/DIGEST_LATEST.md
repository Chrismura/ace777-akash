# Hulk DIGEST — 2026-10-10T12:49:51Z

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
| WUSDT | IDLE | 3.73 | 7.31 | 1.55 | 0.0 | 1072810.7 | 10.83 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.65 | 0.49 | 0.01 | 18959698.23 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.37 | 0.14 | -0.0 | 213545816.18 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.13 | 0.25 | 0.08 | -0.0 | 85311162.77 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 0.97 | 2.72 | 1.86 | -0.07 | 1261535.62 | 3.82 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 3.57 | 0.86 | 0.01 | 1179821.82 | 1.99 | skipped_fast |
| EDELUSDT | IDLE | 3.21 | 7.46 | 4.6 | 0.04 | 238272.21 | 23.29 | skipped_fast |
| KITEUSDT | IDLE | 2.68 | 6.02 | 0.28 | 0.04 | 75450.72 | 9.31 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 1.96 | 1.69 | -0.04 | 404503.38 | 9.19 | skipped_fast |
| ZBCNUSDT | IDLE | 0.62 | 1.19 | 0.38 | -0.02 | 237957.33 | 4.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 3.48 | 2.81 | 0.07 | 96322.97 | 13.38 | skipped_fast |
| REDUSDT | IDLE | 1.38 | 2.64 | 0.85 | 0.03 | 54669.16 | 14.62 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.0 | 1.21 | 0.03 | 76041.18 | 3.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.57 | -0.03 | 9430.91 | 103.02 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.47 | 0.51 | 0.01 | 342840.29 | 3.23 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 3.23 | 2.81 | -0.01 | 105460.05 | 32.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 1.56 | 0.92 | 0.04 | 50209.52 | 53.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.5 | 1.46 | 0.89 | -0.0 | 10257.07 | 17.4 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | -0.01 | 53437.77 | 15.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.69 | 0.34 | -0.0 | 39703.16 | 20.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
