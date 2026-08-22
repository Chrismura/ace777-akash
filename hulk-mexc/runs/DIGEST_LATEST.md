# Hulk DIGEST — 2026-08-22T00:53:19Z

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
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.6 | 0.12 | 6508529.51 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.17 | 0.14 | 147677545.38 | 3.45 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.87 | 0.07 | 941898.4 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.49 | 0.1 | 543513.2 | 18.53 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.4 | 0.14 | 645531.26 | 8.03 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.86 | 0.09 | 390557.65 | 11.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.02 | 547422.49 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.62 | 0.76 | 0.03 | 186588.09 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79720.15 | 44.3 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.67 | 0.13 | 60137.07 | 45.1 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.06 | 183942.02 | 15.46 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.58 | 2.64 | 0.23 | 159658.29 | 10.16 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.24 | 0.06 | 170514.79 | 3.02 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.22 | 1.48 | -0.01 | 3832.89 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 3.49 | 0.0 | 0.1 | 60905.69 | 12.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9710.61 | 48.56 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54965.38 | 16.43 | skipped_fast |
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
