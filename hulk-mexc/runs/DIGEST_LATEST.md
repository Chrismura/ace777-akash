# Hulk DIGEST — 2026-08-22T15:41:33Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.38 | 0.04 | 51500372.77 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.4 | 7.64 | 6.41 | 0.02 | 215758532.13 | 2.1 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.66 | 0.09 | 794317.93 | 7.7 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.33 | -0.02 | 1157163.64 | 7.85 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.32 | -0.09 | 605248.18 | 3.4 | skipped_fast |
| WUSDT | IDLE | 0.77 | 3.17 | 1.53 | -0.02 | 553424.42 | 11.75 | skipped_fast |
| KITEUSDT | IDLE | 2.77 | 6.37 | 2.16 | 0.03 | 85349.34 | 10.76 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.84 | -0.05 | 319878.48 | 22.61 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.17 | -0.07 | 220998.22 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.04 | 79049.71 | 11.4 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.16 | -0.11 | 144107.77 | 13.86 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.32 | 0.03 | 56462.69 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.24 | -0.02 | 185104.69 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.52 | -0.01 | 140444.5 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 23.23 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.65 | 0.02 | 57434.27 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
