# Hulk DIGEST — 2026-10-16T07:07:47Z

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
| WUSDT | IDLE | 2.44 | 6.45 | 1.37 | 0.03 | 2244634.06 | 11.75 | skipped_fast |
| PYTHUSDT | IDLE | 0.57 | 3.5 | 0.56 | 0.11 | 3974967.59 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 0.84 | 1.63 | 0.34 | 0.02 | 31645789.47 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.35 | 0.22 | 0.04 | 220752196.41 | 0.69 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.87 | 0.28 | 0.02 | 413634159.56 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 3.9 | 1.55 | 0.07 | 1166147.36 | 2.41 | skipped_fast |
| CCUSDT | IDLE | 1.87 | 3.67 | 0.52 | 0.01 | 412880.9 | 9.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.13 | 1.3 | 0.05 | 184066.79 | 10.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 6.53 | 3.55 | 0.13 | 189811.78 | 13.9 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 3.44 | 2.1 | 0.03 | 70331.95 | 10.63 | skipped_fast |
| EDELUSDT | IDLE | 0.96 | 2.69 | 0.1 | -0.06 | 211667.98 | 10.09 | skipped_fast |
| RWAINCUSDT | IDLE | 1.53 | 3.31 | 0.0 | 0.03 | 27638.63 | 9.84 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.36 | 0.08 | 0.06 | 67325.85 | 7.7 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 3.22 | 1.01 | -0.05 | 92153.64 | 15.3 | skipped_fast |
| HBARUSDT | IDLE | 1.53 | 3.08 | 0.32 | 0.07 | 155648.11 | 4.62 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 1.73 | 0.28 | 0.05 | 62956.71 | 54.79 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 2.94 | 1.81 | 0.04 | 92293.69 | 33.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.71 | 0.38 | 0.01 | 7843.7 | 21.47 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.88 | 0.24 | 0.02 | 52851.85 | 15.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.37 | 0.3 | 0.01 | 39459.94 | 8.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
