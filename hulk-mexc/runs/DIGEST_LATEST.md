# Hulk DIGEST — 2026-08-21T22:35:20Z

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
| PYTHUSDT | IDLE | 1.38 | 5.17 | 0.71 | 0.11 | 5820917.1 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.59 | 5.91 | 0.28 | 0.14 | 134630857.04 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 6.7 | 0.0 | 0.14 | 659050.17 | 7.09 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 4.71 | 1.02 | 0.08 | 868991.1 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.48 | 5.3 | 0.55 | 0.08 | 370985.68 | 13.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.45 | 0.06 | 533911.02 | 3.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 6.77 | 0.49 | 0.11 | 503019.54 | 23.15 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.48 | 0.03 | 188343.83 | 9.36 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.94 | 0.18 | 155991.03 | 20.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10212.45 | 16.17 | skipped_fast |
| EDELUSDT | IDLE | 2.35 | 5.04 | 1.09 | -0.04 | 82619.35 | 76.97 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.06 | 187121.41 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3825.97 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.28 | 0.11 | 61531.9 | 12.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.79 | 0.06 | 56360.41 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.98 | 3.96 | 0.0 | 0.06 | 73684.3 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.04 | 54137.76 | 8.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
