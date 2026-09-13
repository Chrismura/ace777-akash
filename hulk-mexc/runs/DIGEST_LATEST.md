# Hulk DIGEST — 2026-09-13T07:38:57Z

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
| XRPUSDT | IDLE | 0.47 | 0.82 | 0.8 | -0.01 | 13007813.65 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.64 | 0.43 | -0.0 | 182770792.84 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.34 | 0.27 | -0.0 | 289185498.28 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 36.22 | 18.14 | 0.12 | 98200.77 | 56.71 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 2.17 | 1.8 | 0.04 | 433904.98 | 1.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.36 | 4.17 | 0.0 | 9474.38 | 5.54 | skipped_fast |
| WUSDT | IDLE | 1.42 | 2.49 | 2.33 | 0.02 | 223172.16 | 6.99 | skipped_fast |
| KITEUSDT | IDLE | 2.19 | 4.29 | 0.57 | 0.04 | 64403.92 | 20.86 | skipped_fast |
| QNTUSDT | IDLE | 3.01 | 5.3 | 4.84 | 0.0 | 40211.24 | 7.8 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.68 | 1.05 | -0.01 | 236068.07 | 4.08 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 2.82 | 2.72 | 0.03 | 54719.31 | 17.55 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 2.15 | 0.57 | -0.01 | 237291.47 | 12.28 | skipped_fast |
| EDELUSDT | IDLE | 1.04 | 2.81 | 0.72 | 0.1 | 174003.48 | 24.24 | skipped_fast |
| RWAUSDT | IDLE | 2.62 | 4.61 | 4.2 | -0.0 | 56492.39 | 7.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 2.32 | 2.0 | -0.02 | 77828.9 | 14.87 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.57 | 0.7 | 0.01 | 72250.68 | 3.9 | skipped_fast |
| FLUIDUSDT | IDLE | 2.17 | 4.0 | 2.28 | 0.01 | 1213.38 | 21.93 | skipped_fast |
| TELUSDT | IDLE | 1.78 | 3.13 | 2.91 | -0.05 | 89394.91 | 37.5 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.24 | 0.18 | 0.01 | 132292.6 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.17 | 0.01 | 33864.59 | 25.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
