# Hulk DIGEST — 2026-09-06T12:30:54Z

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
| XRPUSDT | IDLE | 0.55 | 1.09 | 0.0 | 0.01 | 25667571.05 | 1.4 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.96 | 0.22 | 0.02 | 232696705.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.54 | 0.06 | 0.0 | 406277528.57 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.89 | 7.32 | 3.69 | 0.07 | 406453.8 | 5.05 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 3.1 | 1.0 | 0.02 | 452254.58 | 1.8 | skipped_fast |
| WUSDT | IDLE | 2.31 | 4.39 | 1.52 | 0.03 | 205376.56 | 9.74 | skipped_fast |
| RWAINCUSDT | IDLE | 2.87 | 6.17 | 3.51 | 0.04 | 7549.11 | 25.99 | skipped_fast |
| REDUSDT | IDLE | 2.44 | 4.59 | 1.96 | 0.02 | 61125.43 | 11.68 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.07 | 0.73 | 0.01 | 318705.86 | 9.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.75 | 9.49 | 6.02 | -0.03 | 86749.1 | 59.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 2.37 | 1.87 | -0.01 | 198896.74 | 40.29 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.37 | 2.31 | -0.03 | 65160.17 | 12.67 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.63 | 1.28 | 0.02 | 66961.21 | 18.55 | skipped_fast |
| HBARUSDT | IDLE | 0.72 | 1.37 | 0.47 | 0.01 | 462818.09 | 1.23 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.78 | 0.36 | 0.01 | 92664.3 | 7.17 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.53 | 0.83 | 0.03 | 39339.3 | 4.56 | skipped_fast |
| TELUSDT | IDLE | 0.9 | 1.65 | 0.98 | 0.01 | 69069.67 | 58.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.15 | 0.53 | 0.02 | 42618.5 | 12.07 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.93 | 0.35 | 0.0 | 52629.65 | 14.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
