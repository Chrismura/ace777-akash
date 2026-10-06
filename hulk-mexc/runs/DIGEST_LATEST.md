# Hulk DIGEST — 2026-10-06T10:41:44Z

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
| QNTUSDT | IDLE | 1.64 | 2.94 | 2.23 | -0.0 | 2557582.68 | 3.15 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.31 | 0.23 | -0.01 | 28595373.54 | 1.99 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.25 | 0.17 | 0.0 | 545500453.76 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 1.05 | 0.17 | 0.0 | 318515266.72 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.51 | 4.92 | 0.63 | 0.0 | 548058.25 | 1.25 | skipped_fast |
| WUSDT | IDLE | 2.52 | 4.95 | 0.56 | 0.01 | 391542.6 | 8.87 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 2.44 | 0.21 | 0.03 | 480821.55 | 9.28 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.9 | 1.46 | 0.03 | 371137.49 | 15.99 | skipped_fast |
| BIOUSDT | IDLE | 2.16 | 5.0 | 1.54 | 0.02 | 106247.24 | 3.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 5.18 | 4.28 | 0.06 | 109988.35 | 7.56 | skipped_fast |
| KITEUSDT | IDLE | 1.76 | 3.49 | 0.23 | -0.01 | 63076.89 | 8.48 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.48 | 0.73 | 0.0 | 287190.77 | 14.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 3.49 | 1.81 | -0.04 | 18290.47 | 17.17 | skipped_fast |
| REDUSDT | IDLE | 1.08 | 2.05 | 0.76 | -0.03 | 59506.77 | 12.03 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.16 | 0.08 | -0.02 | 442107.27 | 3.96 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 8.53 | 0.39 | 0.3 | 107410.19 | 88.91 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.81 | 1.42 | -0.03 | 129274.89 | 15.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.99 | 5.18 | 0.69 | 0.09 | 119009.72 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.25 | 0.44 | 0.0 | 51035.8 | 14.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.77 | 1.43 | 0.72 | 0.0 | 45348.94 | 36.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
