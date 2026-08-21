# Hulk DIGEST — 2026-08-21T23:53:28Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.67 | 0.1 | 6207932.21 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.14 | 0.15 | 142061359.8 | 2.74 | skipped_fast |
| HBARUSDT | IDLE | 2.63 | 6.36 | 1.18 | 0.09 | 909446.43 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.33 | 0.11 | 514582.25 | 82.21 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.14 | 0.13 | 644458.28 | 8.01 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.94 | 0.08 | 378972.95 | 14.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.2 | 3.56 | 1.7 | 0.03 | 545090.96 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.02 | 187263.9 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | 0.01 | 80172.99 | 11.01 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.91 | 0.12 | 58859.06 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.07 | 191399.51 | 20.53 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.1 | 0.18 | 157807.46 | 11.35 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.08 | 154056.25 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 53.56 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.14 | 0.09 | 61379.28 | 11.12 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54494.75 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
