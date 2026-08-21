# Hulk DIGEST — 2026-08-21T22:21:02Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.29 | 0.11 | 5749135.68 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 5.68 | 0.25 | 0.14 | 132407634.91 | 6.97 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 6.48 | 0.61 | 0.13 | 647377.67 | 11.63 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 4.71 | 0.26 | 0.09 | 854265.5 | 1.26 | skipped_fast |
| WUSDT | IDLE | 2.45 | 5.3 | 0.1 | 0.08 | 370940.73 | 13.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.18 | 0.06 | 534108.76 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.0 | 0.11 | 500511.29 | 52.14 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.58 | 0.03 | 187911.09 | 3.1 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.95 | 0.19 | 156233.26 | 20.19 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 4.24 | 0.0 | -0.03 | 82312.11 | 22.0 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.5 | 6.45 | 0.31 | 0.06 | 186864.74 | 36.13 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 70.14 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.81 | 0.11 | 61240.08 | 13.81 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.65 | 0.06 | 56393.22 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.8 | 3.58 | 0.14 | 0.05 | 65396.79 | 4.57 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.41 | 0.04 | 54126.15 | 16.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 16.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
