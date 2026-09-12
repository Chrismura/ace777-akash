# Hulk DIGEST — 2026-09-12T11:36:33Z

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
| ETHUSDT | IDLE | 0.45 | 1.05 | 0.05 | 0.03 | 601990001.67 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.44 | 0.93 | 0.23 | 0.04 | 48492528.24 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.26 | 0.13 | 0.01 | 533917510.7 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.73 | 5.41 | 0.3 | 0.02 | 224207.0 | 30.35 | skipped_fast |
| RWAINCUSDT | IDLE | 3.47 | 6.94 | 3.01 | 0.02 | 16913.03 | 26.72 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.43 | 0.37 | 0.06 | 401185.79 | 5.6 | skipped_fast |
| CCUSDT | IDLE | 0.48 | 0.88 | 0.52 | 0.03 | 334136.89 | 7.08 | skipped_fast |
| EDELUSDT | IDLE | 1.06 | 2.95 | 0.26 | 0.09 | 169632.24 | 17.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 3.08 | 2.08 | 0.05 | 86111.1 | 16.85 | skipped_fast |
| WUSDT | IDLE | 0.71 | 1.34 | 1.14 | 0.04 | 199711.21 | 13.33 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.98 | 0.39 | 0.05 | 77059.8 | 3.9 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 2.63 | 0.18 | 0.09 | 64555.05 | 13.89 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.75 | 0.78 | -0.01 | 61003.26 | 12.25 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.96 | 2.29 | -0.03 | 99267.45 | 18.0 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.78 | 0.31 | 0.01 | 239209.76 | 1.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.13 | 7.88 | 4.18 | 1.02 | 182769.46 | 177.18 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.27 | 0.46 | 0.0 | 42187.16 | 7.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.59 | 1.18 | 0.0 | 0.01 | 26422.7 | 4.16 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.74 | 0.29 | 0.03 | 55265.65 | 22.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.04 | 1356.84 | 22.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
