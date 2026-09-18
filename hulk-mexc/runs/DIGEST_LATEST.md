# Hulk DIGEST — 2026-09-18T12:28:14Z

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
| XRPUSDT | IDLE | 1.01 | 1.81 | 1.35 | 0.01 | 40998810.82 | 2.27 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.42 | 0.64 | 0.01 | 381035522.98 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.17 | 0.58 | 0.01 | 564949755.91 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 6.0 | 4.51 | 0.07 | 648267.83 | 6.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 4.64 | 3.82 | 0.08 | 681115.24 | 3.41 | skipped_fast |
| WUSDT | IDLE | 0.97 | 2.78 | 1.65 | 0.09 | 428349.98 | 13.69 | skipped_fast |
| CHIPUSDT | IDLE | 1.68 | 7.51 | 6.45 | 0.1 | 162303.11 | 14.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 2.84 | 1.27 | 0.03 | 272442.69 | 0.56 | skipped_fast |
| BIOUSDT | IDLE | 1.86 | 4.65 | 3.75 | 0.05 | 86730.54 | 7.5 | skipped_fast |
| HBARUSDT | IDLE | 1.51 | 2.74 | 1.83 | 0.02 | 490408.66 | 1.3 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.87 | 1.61 | 0.06 | 64398.53 | 15.66 | skipped_fast |
| TELUSDT | IDLE | 2.98 | 6.08 | 0.59 | 0.04 | 88722.13 | 39.76 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 5.21 | 2.62 | -0.06 | 256667.22 | 34.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.61 | 3.15 | 0.53 | -0.01 | 11045.38 | 11.83 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.35 | 0.67 | 0.05 | 76580.49 | 11.78 | skipped_fast |
| FLUIDUSDT | IDLE | 2.44 | 4.83 | 0.4 | 0.06 | 248.11 | 21.58 | skipped_fast |
| RIZEUSDT | IDLE | 0.24 | 3.05 | 1.79 | 0.17 | 53560.73 | 75.5 | skipped_fast |
| RWAUSDT | IDLE | 1.36 | 2.39 | 2.18 | 0.0 | 58884.33 | 44.68 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 2.11 | 1.33 | 0.01 | 45901.2 | 11.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.01 | 0.03 | 42128.03 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
