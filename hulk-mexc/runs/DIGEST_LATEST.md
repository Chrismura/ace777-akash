# Hulk DIGEST — 2026-08-21T22:24:02Z

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
| PYTHUSDT | IDLE | 1.37 | 5.17 | 0.43 | 0.11 | 5760957.67 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 5.68 | 0.3 | 0.14 | 133657012.29 | 2.79 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.48 | 0.5 | 0.13 | 647572.13 | 0.89 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.72 | 0.08 | 855979.32 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.21 | 0.08 | 370707.55 | 14.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 4.54 | 1.02 | 0.06 | 534331.05 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.33 | 0.11 | 501790.84 | 24.65 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.03 | 187887.09 | 12.43 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.13 | 0.18 | 156167.08 | 12.92 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.47 | 0.11 | -0.03 | 82648.76 | 10.97 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.62 | 0.06 | 186886.66 | 25.85 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 70.14 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.02 | 0.11 | 61278.21 | 10.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.74 | 0.06 | 56356.12 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.58 | 0.02 | 0.05 | 65371.18 | 4.57 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.75 | 0.33 | 0.04 | 54131.04 | 24.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 8.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
