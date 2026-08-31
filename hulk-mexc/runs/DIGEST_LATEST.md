# Hulk DIGEST — 2026-08-31T12:17:20Z

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
| XRPUSDT | IDLE | 0.77 | 1.46 | 0.59 | -0.02 | 39613516.08 | 1.45 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.04 | 0.5 | -0.0 | 526612729.85 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.98 | 0.17 | -0.01 | 439344280.45 | 0.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.68 | 4.91 | 4.58 | -0.02 | 599670.75 | 2.51 | skipped_fast |
| PYTHUSDT | IDLE | 0.78 | 1.8 | 1.44 | -0.01 | 520058.89 | 4.23 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.4 | 1.7 | 0.01 | 244563.46 | 6.73 | skipped_fast |
| WUSDT | IDLE | 1.15 | 2.11 | 1.6 | -0.01 | 235024.54 | 11.87 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 2.9 | 0.76 | -0.08 | 233074.21 | 3.34 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.01 | 2.49 | -0.01 | 71018.28 | 11.98 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 1.94 | 1.34 | -0.04 | 85960.75 | 3.78 | skipped_fast |
| KITEUSDT | IDLE | 0.64 | 1.59 | 1.47 | -0.06 | 98100.23 | 12.47 | skipped_fast |
| EDELUSDT | IDLE | 0.4 | 2.43 | 1.88 | 0.01 | 120770.46 | 8.32 | skipped_fast |
| RIZEUSDT | IDLE | 1.35 | 2.63 | 0.48 | -0.0 | 34063.48 | 59.28 | skipped_fast |
| QNTUSDT | IDLE | 2.04 | 3.9 | 1.2 | -0.0 | 47052.05 | 1.62 | skipped_fast |
| RWAUSDT | IDLE | 1.87 | 3.66 | 0.55 | 0.03 | 54216.91 | 15.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 2.35 | 2.29 | -0.02 | 2855.92 | 113.83 | skipped_fast |
| HBARUSDT | IDLE | 0.39 | 0.73 | 0.28 | -0.01 | 241160.23 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.05 | 0.8 | 0.03 | 90818.25 | 17.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.15 | 0.16 | 0.01 | 1733.99 | 21.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.57 | 0.24 | -0.01 | 28195.22 | 31.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
