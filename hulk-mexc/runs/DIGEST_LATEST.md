# Hulk DIGEST — 2026-08-22T00:32:16Z

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
| PYTHUSDT | IDLE | 1.74 | 6.39 | 0.77 | 0.1 | 6384384.82 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.99 | 8.23 | 0.53 | 0.16 | 144566887.47 | 4.77 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.6 | 0.07 | 937738.61 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.47 | 0.12 | 538644.46 | 35.21 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.8 | 0.14 | 638882.02 | 7.08 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.02 | 0.08 | 385532.23 | 14.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.55 | 0.02 | 556213.59 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.55 | 0.02 | 185951.93 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79730.56 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.76 | 0.13 | 59846.09 | 45.1 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 186346.44 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.28 | 0.06 | 170461.62 | 7.56 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 4.91 | 0.07 | 0.23 | 157798.96 | 17.31 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.27 | 0.1 | 61035.39 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9704.24 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54617.58 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
