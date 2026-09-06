# Hulk DIGEST — 2026-09-06T19:33:12Z

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
| ETHUSDT | IDLE | 0.76 | 1.48 | 0.32 | 0.0 | 249378403.76 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.35 | 0.45 | -0.01 | 24347675.44 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.96 | 0.17 | -0.0 | 352685482.61 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.5 | 7.14 | 3.01 | 0.05 | 376056.68 | 19.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 3.07 | 1.43 | -0.01 | 538714.42 | 1.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 3.93 | 2.54 | -0.03 | 417671.79 | 1.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.33 | 4.88 | 4.0 | 0.05 | 6294.85 | 10.43 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.71 | 1.43 | -0.02 | 91060.42 | 3.63 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.63 | 0.53 | -0.0 | 314256.25 | 9.12 | skipped_fast |
| EDELUSDT | IDLE | 1.83 | 3.5 | 1.13 | -0.0 | 57609.27 | 47.55 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 1.66 | 1.57 | 0.01 | 168668.08 | 10.26 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.38 | 1.1 | -0.01 | 413041.53 | 1.24 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 2.07 | 0.35 | 0.01 | 66510.47 | 11.73 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.43 | 1.1 | 0.0 | 59505.89 | 11.1 | skipped_fast |
| RIZEUSDT | IDLE | 2.06 | 14.15 | 7.57 | -0.18 | 73066.07 | 564.61 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.76 | 0.32 | 0.01 | 34020.62 | 9.11 | skipped_fast |
| TELUSDT | IDLE | 1.15 | 2.3 | 0.06 | -0.0 | 67043.33 | 57.74 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.08 | 0.64 | -0.02 | 53938.23 | 14.37 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.19 | 0.02 | 41649.12 | 4.03 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.63 | 0.63 | 0.02 | 194.56 | 22.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
