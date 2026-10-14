# Hulk DIGEST — 2026-10-14T09:14:54Z

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
| PYTHUSDT | IDLE | 2.61 | 5.23 | 2.92 | -0.03 | 1818227.59 | 1.23 | skipped_fast |
| WUSDT | IDLE | 0.82 | 5.16 | 2.43 | -0.15 | 3720501.24 | 13.49 | skipped_fast |
| XRPUSDT | IDLE | 0.95 | 1.73 | 1.11 | 0.0 | 29891813.86 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.16 | 0.87 | -0.0 | 119555553.79 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 0.94 | 0.76 | -0.0 | 314059785.56 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 3.02 | 2.62 | -0.05 | 1711001.12 | 1.9 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.9 | 2.46 | 0.01 | 569549.34 | 8.17 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.01 | 3.94 | -0.05 | 80264.27 | 12.38 | skipped_fast |
| KITEUSDT | IDLE | 2.27 | 7.12 | 3.88 | 0.08 | 75798.46 | 10.98 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 2.46 | 0.26 | 0.03 | 216323.36 | 2.89 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.7 | 2.6 | -0.01 | 73343.72 | 8.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.75 | 5.95 | 1.55 | 0.04 | 53203.97 | 38.76 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.83 | 1.51 | -0.01 | 69269.36 | 3.65 | skipped_fast |
| ZBCNUSDT | IDLE | 0.51 | 0.91 | 0.74 | -0.02 | 200168.47 | 14.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.01 | 2.01 | 1.42 | -0.07 | 33134.49 | 5.14 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.61 | 1.27 | -0.01 | 307013.8 | 5.78 | skipped_fast |
| FLUIDUSDT | IDLE | 1.63 | 4.76 | 3.34 | 0.07 | 20286.23 | 21.26 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.91 | 0.88 | 0.03 | 116118.66 | 27.86 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.78 | 0.31 | -0.01 | 56354.14 | 7.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.01 | 0.03 | 0.0 | -0.01 | 37999.61 | 5.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
