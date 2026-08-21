# Hulk DIGEST — 2026-08-21T22:24:42Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.27 | 0.11 | 5765106.89 | 6.13 | skipped_fast |
| XRPUSDT | IDLE | 1.56 | 5.68 | 0.5 | 0.14 | 133766653.95 | 4.89 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 6.48 | 0.59 | 0.13 | 647883.42 | 9.83 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.72 | 0.08 | 856011.45 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.3 | 0.08 | 370720.11 | 18.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.18 | 0.06 | 534130.9 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.3 | 0.11 | 502105.13 | 24.64 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.95 | 0.03 | 187883.17 | 12.43 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.01 | 0.18 | 156205.87 | 17.78 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 4.47 | 0.0 | -0.03 | 82580.3 | 10.97 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.56 | 0.06 | 186922.82 | 25.85 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.08 | 0.1 | 61308.28 | 12.92 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 86.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.77 | 0.06 | 56372.15 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 3.68 | 0.0 | 0.05 | 65349.98 | 4.57 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.25 | 0.04 | 54157.92 | 16.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 6.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
