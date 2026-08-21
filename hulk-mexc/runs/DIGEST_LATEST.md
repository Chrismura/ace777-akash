# Hulk DIGEST — 2026-08-21T22:40:08Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.31 | 0.11 | 5837624.09 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.59 | 5.94 | 0.28 | 0.14 | 134915015.86 | 1.39 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 7.03 | 0.0 | 0.14 | 660374.81 | 7.07 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.73 | 0.08 | 871643.02 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.47 | 5.48 | 0.09 | 0.09 | 370950.12 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.6 | 0.06 | 533637.79 | 3.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 6.77 | 0.08 | 0.11 | 504892.65 | 11.77 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.14 | 0.03 | 188260.36 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82605.4 | 21.83 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.24 | 0.18 | 156099.91 | 53.34 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10279.27 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 186921.57 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.99 | 0.11 | 61478.31 | 9.21 | skipped_fast |
| QNTUSDT | IDLE | 2.11 | 4.21 | 0.05 | 0.06 | 80789.11 | 1.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.69 | 0.06 | 56369.7 | 45.14 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.04 | 54166.43 | 16.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 18.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
