# Hulk DIGEST — 2026-09-13T21:34:17Z

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
| XRPUSDT | IDLE | 0.73 | 1.42 | 0.31 | -0.0 | 15143304.36 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 1.02 | 0.11 | -0.0 | 251637274.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.38 | 0.05 | 0.0 | 253240009.78 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.76 | 5.64 | 1.21 | 0.04 | 446989.08 | 1.75 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 32.72 | 21.51 | -0.12 | 67793.66 | 82.44 | skipped_fast |
| RWAINCUSDT | IDLE | 4.18 | 7.78 | 3.9 | -0.01 | 9898.19 | 21.99 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 7.43 | 1.55 | 0.13 | 202624.71 | 29.87 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.67 | 1.71 | 0.01 | 218375.61 | 4.94 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.47 | 0.26 | -0.01 | 298156.44 | 10.4 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 1.91 | 0.71 | -0.0 | 197336.53 | 23.4 | skipped_fast |
| CHIPUSDT | IDLE | 0.92 | 2.46 | 1.99 | -0.1 | 82921.82 | 13.87 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.58 | 1.08 | 0.03 | 225448.85 | 1.31 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.7 | 0.5 | 0.0 | 67862.3 | 15.62 | skipped_fast |
| REDUSDT | IDLE | 0.74 | 1.39 | 0.57 | 0.01 | 63920.84 | 17.56 | skipped_fast |
| KITEUSDT | IDLE | 0.56 | 1.11 | 0.11 | 0.0 | 60104.84 | 12.99 | skipped_fast |
| QNTUSDT | IDLE | 1.31 | 2.37 | 1.62 | 0.01 | 35640.23 | 4.65 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.65 | 1.31 | -0.04 | 81180.88 | 25.27 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.75 | 0.07 | 0.01 | 53757.42 | 22.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 1.04 | 0.17 | 0.0 | 1525.44 | 21.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.46 | 0.25 | -0.0 | 30590.89 | 11.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
