# Hulk DIGEST — 2026-09-18T00:04:42Z

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
| XRPUSDT | IDLE | 0.53 | 1.01 | 0.3 | -0.0 | 37218438.12 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.88 | 0.44 | 0.01 | 292195391.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.62 | 0.38 | 0.0 | 412200279.14 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 29.67 | 2.06 | -0.13 | 276950.04 | 30.64 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 3.09 | 0.41 | -0.0 | 518657.66 | 9.84 | skipped_fast |
| PYTHUSDT | IDLE | 0.81 | 1.79 | 0.25 | 0.06 | 544856.64 | 1.78 | skipped_fast |
| WUSDT | IDLE | 1.4 | 3.82 | 1.08 | 0.09 | 335639.75 | 15.02 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.39 | 1.5 | 0.01 | 537224.57 | 1.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 2.69 | 1.1 | 0.04 | 175883.88 | 10.61 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 2.79 | 0.0 | 0.02 | 66767.61 | 15.8 | skipped_fast |
| ZBCNUSDT | IDLE | 0.88 | 1.69 | 0.53 | 0.01 | 200840.18 | 27.25 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 2.02 | 0.66 | -0.02 | 60871.43 | 13.23 | skipped_fast |
| BIOUSDT | IDLE | 0.75 | 1.49 | 0.12 | 0.01 | 67697.87 | 7.93 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 3.26 | 2.82 | -0.02 | 73804.48 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.71 | 0.71 | -0.02 | 14280.51 | 23.85 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 5.38 | 4.04 | -0.04 | 42867.52 | 158.65 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.23 | 0.67 | -0.0 | 40535.04 | 4.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.21 | 0.14 | 0.02 | 43229.04 | 2.8 | skipped_fast |
| RWAUSDT | IDLE | 0.19 | 0.37 | 0.07 | 0.0 | 57012.15 | 22.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.39 | 0.02 | 148.34 | 22.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
