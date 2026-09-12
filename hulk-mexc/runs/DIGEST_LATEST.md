# Hulk DIGEST — 2026-09-12T21:38:11Z

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
| XRPUSDT | IDLE | 0.48 | 0.88 | 0.6 | 0.0 | 16337918.07 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.84 | 0.42 | -0.0 | 231474242.78 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.45 | 0.21 | -0.0 | 370091657.85 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.09 | 37.35 | 13.19 | 0.46 | 91259.52 | 39.96 | skipped_fast |
| ZBCNUSDT | IDLE | 2.06 | 5.09 | 2.47 | -0.0 | 220104.18 | 7.76 | skipped_fast |
| PYTHUSDT | IDLE | 1.12 | 3.0 | 1.32 | 0.08 | 398359.21 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 2.4 | 5.89 | 4.11 | 0.03 | 75029.08 | 8.3 | skipped_fast |
| WUSDT | IDLE | 2.06 | 3.72 | 2.6 | 0.03 | 170915.89 | 14.07 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 4.23 | 1.08 | 0.05 | 165336.88 | 25.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.25 | 1.18 | -0.02 | 10649.09 | 10.93 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 1.89 | 1.52 | -0.01 | 212290.33 | 6.19 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 2.18 | 1.5 | 0.02 | 58233.35 | 16.96 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.53 | 1.16 | 0.02 | 70733.16 | 11.78 | skipped_fast |
| KITEUSDT | IDLE | 0.88 | 1.72 | 0.29 | -0.01 | 62663.43 | 10.26 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.36 | 0.61 | 0.0 | 161156.92 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.7 | 1.07 | -0.05 | 89294.85 | 42.28 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 0.92 | 0.92 | -0.0 | 40819.07 | 6.26 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.82 | 0.74 | -0.0 | 53285.52 | 7.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.39 | 0.18 | -0.0 | 25890.99 | 13.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.03 | 1375.44 | 21.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
