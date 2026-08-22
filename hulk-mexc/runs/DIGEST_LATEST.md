# Hulk DIGEST — 2026-08-22T14:56:43Z

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
| PYTHUSDT | IDLE | 1.61 | 7.62 | 2.18 | 0.03 | 51453611.05 | 1.99 | skipped_fast |
| XRPUSDT | IDLE | 1.38 | 7.58 | 5.99 | 0.03 | 213562665.69 | 4.17 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 6.16 | 3.39 | 0.11 | 795929.86 | 8.59 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 3.34 | 3.1 | -0.02 | 1178124.99 | 3.94 | skipped_fast |
| WUSDT | IDLE | 1.12 | 4.43 | 3.39 | -0.02 | 563027.54 | 15.03 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.96 | -0.11 | 614047.57 | 3.42 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.79 | 0.04 | 84519.55 | 9.82 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 4.21 | 1.95 | -0.08 | 324333.39 | 17.37 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 6.58 | 5.92 | -0.06 | 226259.9 | 3.35 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 2.63 | 2.01 | -0.04 | 78966.35 | 34.07 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.42 | 5.1 | 4.85 | -0.03 | 150419.14 | 10.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.47 | 0.03 | 46751.45 | 43.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.4 | 0.85 | 0.01 | 9946.26 | 86.02 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.31 | -0.01 | 188431.87 | 7.89 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 3.24 | 1.78 | 0.01 | 140159.33 | 42.6 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.55 | 0.89 | 0.02 | 57269.12 | 16.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 22.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
