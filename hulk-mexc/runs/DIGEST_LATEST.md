# Hulk DIGEST — 2026-09-17T01:14:58Z

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
| XRPUSDT | IDLE | 1.63 | 2.98 | 1.9 | 0.0 | 56665039.5 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.63 | 0.43 | 0.01 | 371170891.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.14 | 0.29 | 0.01 | 508874104.3 | 0.05 | skipped_fast |
| CCUSDT | IDLE | 2.78 | 10.41 | 3.5 | 0.09 | 535993.54 | 6.04 | skipped_fast |
| RWAINCUSDT | IDLE | 4.2 | 7.81 | 3.88 | -0.03 | 21035.01 | 17.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.48 | 2.92 | 0.23 | 0.0 | 416928.53 | 1.88 | skipped_fast |
| WUSDT | IDLE | 2.25 | 4.35 | 1.03 | 0.0 | 208283.49 | 13.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 5.73 | 1.59 | -0.01 | 81585.81 | 10.96 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 6.57 | 0.67 | 0.07 | 67049.81 | 14.89 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 3.46 | 3.16 | 0.09 | 265391.12 | 15.38 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 2.89 | 0.04 | 0.02 | 77901.73 | 11.88 | skipped_fast |
| ZBCNUSDT | IDLE | 0.89 | 1.7 | 0.5 | 0.02 | 179151.91 | 17.29 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 2.58 | 0.07 | -0.03 | 64594.46 | 19.2 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.97 | 0.73 | -0.01 | 287020.83 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 9.65 | 5.53 | 0.25 | 60934.73 | 89.74 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.35 | 0.73 | 0.0 | 37601.9 | 3.29 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.88 | 1.03 | -0.03 | 115601.17 | 62.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.94 | 0.08 | -0.0 | 32343.44 | 21.19 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.15 | 0.02 | 55554.95 | 44.84 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1573.23 | 22.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
