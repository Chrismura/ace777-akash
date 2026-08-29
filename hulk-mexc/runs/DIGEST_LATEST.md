# Hulk DIGEST — 2026-08-29T04:10:04Z

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
| XRPUSDT | IDLE | 0.49 | 0.88 | 0.71 | -0.03 | 44985856.18 | 2.9 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 8.91 | 5.68 | 0.06 | 1146284.95 | 4.95 | skipped_fast |
| PYTHUSDT | IDLE | 0.95 | 1.7 | 1.27 | -0.02 | 538036.71 | 2.11 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 20.42 | 14.09 | -0.0 | 96647.32 | 70.89 | skipped_fast |
| RIZEUSDT | IDLE | 2.4 | 6.2 | 2.51 | -0.03 | 34586.71 | 58.36 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.75 | 1.49 | -0.01 | 249345.81 | 10.87 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 5.81 | 1.58 | -0.09 | 90988.13 | 28.32 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 2.76 | 1.44 | -0.01 | 73793.08 | 10.19 | skipped_fast |
| WUSDT | IDLE | 0.71 | 1.26 | 1.13 | -0.04 | 214353.11 | 12.07 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.23 | 1.17 | -0.03 | 468389.25 | 1.33 | skipped_fast |
| ZBCNUSDT | IDLE | 0.69 | 1.87 | 0.43 | -0.05 | 176578.46 | 18.84 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 2.65 | 0.08 | -0.02 | 60762.78 | 12.8 | skipped_fast |
| BIOUSDT | IDLE | 0.54 | 0.97 | 0.75 | -0.03 | 83770.18 | 3.6 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.12 | 1.74 | -0.06 | 99732.19 | 45.64 | skipped_fast |
| RWAINCUSDT | IDLE | 0.52 | 1.04 | 0.0 | -0.02 | 3438.94 | 82.12 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.61 | 1.58 | -0.04 | 3732.19 | 21.72 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.05 | 0.76 | -0.02 | 41308.49 | 4.91 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.92 | 0.41 | -0.0 | 54371.1 | 16.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
