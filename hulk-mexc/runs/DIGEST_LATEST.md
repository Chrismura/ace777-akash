# Hulk DIGEST — 2026-08-22T00:48:49Z

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
| PYTHUSDT | IDLE | 2.02 | 7.38 | 1.28 | 0.12 | 6482837.66 | 10.12 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.15 | 0.15 | 147506666.5 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.83 | 6.36 | 2.15 | 0.07 | 941155.37 | 5.06 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.38 | 0.11 | 543617.8 | 32.13 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.55 | 0.14 | 641806.19 | 5.37 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.22 | 0.09 | 389677.98 | 12.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.61 | 0.03 | 548366.08 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.62 | 0.64 | 0.03 | 186531.2 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.5 | 0.98 | -0.01 | 79868.62 | 21.91 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.68 | 0.13 | 60112.62 | 45.1 | skipped_fast |
| QAITUSDT | IDLE | 2.26 | 4.22 | 1.99 | -0.01 | 3705.98 | 15.91 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.07 | 184189.01 | 30.9 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.42 | 1.79 | 0.06 | 170526.58 | 7.59 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9754.98 | 21.55 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 8.58 | 0.21 | 0.27 | 159171.46 | 54.89 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.27 | 0.1 | 61003.12 | 11.96 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54890.17 | 16.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 37.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
