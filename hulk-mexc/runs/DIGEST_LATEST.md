# Hulk DIGEST — 2026-09-08T03:38:26Z

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
| XRPUSDT | IDLE | 0.92 | 1.71 | 0.84 | -0.01 | 32976757.31 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.27 | 0.8 | -0.01 | 303429426.8 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.94 | 0.62 | -0.01 | 440875960.96 | 0.08 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.97 | 0.11 | -0.02 | 448071.18 | 4.65 | skipped_fast |
| RIZEUSDT | IDLE | 3.21 | 9.59 | 4.61 | 0.02 | 52525.8 | 54.12 | skipped_fast |
| PYTHUSDT | IDLE | 1.2 | 2.19 | 1.38 | -0.03 | 413316.93 | 5.57 | skipped_fast |
| WUSDT | IDLE | 1.91 | 3.5 | 2.07 | -0.01 | 239300.94 | 11.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.7 | 4.84 | 4.43 | -0.09 | 190420.13 | 11.53 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 9.19 | 2.58 | -0.07 | 103169.49 | 59.46 | skipped_fast |
| KITEUSDT | IDLE | 2.43 | 4.48 | 2.59 | -0.06 | 63943.91 | 10.86 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 2.54 | 0.85 | -0.04 | 250769.38 | 11.75 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.87 | 1.45 | 0.01 | 508268.96 | 1.22 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.56 | 1.63 | 0.0 | 64177.52 | 3.68 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.09 | 1.35 | 0.04 | 58228.58 | 9.91 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 2.46 | 1.48 | -0.09 | 3716.89 | 30.99 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 1.95 | 1.05 | -0.01 | 79721.63 | 41.07 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.52 | 0.96 | -0.0 | 60489.3 | 6.03 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.51 | -0.01 | 53365.98 | 7.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.71 | 0.31 | -0.01 | 37314.26 | 46.27 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.01 | 818.78 | 21.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
