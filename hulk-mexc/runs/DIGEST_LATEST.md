# Hulk DIGEST — 2026-08-22T00:52:49Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.58 | 0.12 | 6505819.63 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.23 | 0.15 | 147682230.2 | 4.83 | skipped_fast |
| HBARUSDT | IDLE | 2.82 | 6.36 | 1.98 | 0.07 | 941904.72 | 2.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.49 | 0.1 | 543637.0 | 14.13 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.29 | 0.14 | 645507.59 | 11.6 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.05 | 0.09 | 389094.09 | 15.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.49 | 0.02 | 547389.14 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.62 | 0.89 | 0.03 | 186550.91 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79775.09 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.67 | 0.13 | 60136.57 | 45.1 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.72 | 0.06 | 183942.02 | 25.75 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.58 | 2.87 | 0.22 | 159644.03 | 12.46 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.54 | 0.06 | 170514.79 | 7.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9710.61 | 21.55 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 3.12 | 0.01 | 0.1 | 60851.46 | 10.97 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.22 | 1.48 | -0.01 | 3822.88 | 189.27 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54965.54 | 16.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
