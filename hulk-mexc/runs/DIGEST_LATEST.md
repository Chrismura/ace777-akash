# Hulk DIGEST — 2026-09-25T05:42:33Z

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
| XRPUSDT | IDLE | 1.36 | 2.45 | 1.84 | 0.01 | 72673629.94 | 1.96 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.02 | 0.66 | -0.0 | 354332106.11 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.97 | 0.68 | 0.0 | 737077138.84 | 0.29 | skipped_fast |
| PYTHUSDT | IDLE | 0.81 | 2.72 | 2.03 | 0.04 | 1018152.58 | 4.41 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.48 | 1.97 | 0.01 | 915794.52 | 3.25 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 62.83 | 19.92 | 0.68 | 105958.1 | 439.98 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 3.32 | 1.64 | 0.06 | 525566.63 | 10.41 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 5.44 | 5.12 | -0.04 | 65511.19 | 4.79 | skipped_fast |
| REDUSDT | IDLE | 2.16 | 6.53 | 2.96 | 0.08 | 135353.21 | 14.6 | skipped_fast |
| WUSDT | IDLE | 1.61 | 2.87 | 2.31 | 0.02 | 269563.73 | 8.59 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 11.09 | 1.54 | 0.33 | 366554.69 | 12.39 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.57 | 0.03 | 0.02 | 226917.69 | 9.7 | skipped_fast |
| CHIPUSDT | IDLE | 0.9 | 4.62 | 3.71 | 0.09 | 107744.67 | 12.98 | skipped_fast |
| EDELUSDT | IDLE | 0.57 | 6.2 | 3.72 | 0.07 | 191100.11 | 37.12 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 2.67 | 1.29 | 0.03 | 90160.38 | 9.77 | skipped_fast |
| TELUSDT | IDLE | 2.62 | 4.86 | 2.53 | -0.05 | 104234.8 | 74.07 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 3.38 | 2.86 | 0.14 | 15018.8 | 9.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.41 | 0.45 | 0.01 | 40301.06 | 18.08 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.59 | 0.22 | 0.01 | 58849.56 | 7.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.33 | 0.66 | 0.0 | 0.04 | 1081.64 | 21.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
