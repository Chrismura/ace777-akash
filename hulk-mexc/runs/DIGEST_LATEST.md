# Hulk DIGEST — 2026-08-31T04:16:04Z

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
| XRPUSDT | IDLE | 2.14 | 3.86 | 2.8 | -0.03 | 35178706.57 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 1.9 | 3.47 | 2.26 | -0.02 | 386902736.17 | 0.58 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.88 | 1.09 | -0.01 | 396515271.97 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.86 | 6.62 | 4.89 | -0.03 | 545929.77 | 2.16 | skipped_fast |
| WUSDT | IDLE | 2.99 | 6.0 | 0.66 | 0.02 | 231703.99 | 6.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.46 | 4.51 | 2.53 | -0.05 | 502347.5 | 5.24 | skipped_fast |
| BIOUSDT | IDLE | 2.59 | 4.9 | 2.04 | -0.04 | 87230.77 | 3.79 | skipped_fast |
| CCUSDT | IDLE | 2.12 | 4.15 | 0.63 | -0.02 | 203873.86 | 5.07 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 5.38 | 1.94 | 0.05 | 87823.43 | 8.27 | skipped_fast |
| KITEUSDT | IDLE | 2.14 | 6.13 | 1.8 | -0.06 | 91093.69 | 11.54 | skipped_fast |
| REDUSDT | IDLE | 2.38 | 4.49 | 1.83 | -0.02 | 62736.22 | 13.81 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.81 | 1.06 | -0.05 | 227002.12 | 9.93 | skipped_fast |
| FLUIDUSDT | IDLE | 3.12 | 5.58 | 4.43 | -0.02 | 3849.88 | 21.59 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 3.78 | 2.07 | -0.02 | 37690.76 | 62.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.97 | 2.89 | -0.01 | 2255.56 | 96.78 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.12 | 1.41 | -0.02 | 196321.88 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.52 | 2.75 | 1.98 | -0.0 | 83520.15 | 29.68 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.12 | 0.85 | -0.02 | 40620.77 | 3.32 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.39 | 0.96 | 0.01 | 52601.01 | 16.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.82 | 1.48 | 1.1 | -0.01 | 30400.41 | 47.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
