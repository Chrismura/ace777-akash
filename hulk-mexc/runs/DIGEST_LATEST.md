# Hulk DIGEST — 2026-09-06T21:32:43Z

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
| ETHUSDT | IDLE | 0.83 | 1.6 | 0.37 | 0.01 | 261517225.64 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.41 | 0.2 | 0.0 | 23911710.25 | 1.4 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.52 | 0.15 | 0.0 | 339223672.0 | 0.29 | skipped_fast |
| WUSDT | IDLE | 2.87 | 5.32 | 3.71 | 0.04 | 400598.35 | 12.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 4.94 | 1.55 | 0.0 | 418786.58 | 6.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 3.19 | 0.86 | 0.0 | 552756.58 | 1.82 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 15.39 | 8.18 | -0.11 | 73375.25 | 65.57 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 2.93 | 1.35 | 0.01 | 317599.46 | 10.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.88 | 4.42 | 0.0 | 0.06 | 5671.06 | 30.32 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.49 | 0.46 | -0.01 | 91471.97 | 7.18 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.42 | 1.63 | -0.01 | 59093.94 | 10.36 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.0 | 56890.15 | 47.55 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.91 | 0.13 | 0.01 | 429639.86 | 1.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 1.57 | 0.78 | 0.0 | 162263.18 | 23.65 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.17 | 0.08 | 0.02 | 67298.86 | 18.52 | skipped_fast |
| TELUSDT | IDLE | 1.55 | 3.06 | 0.23 | 0.01 | 70164.06 | 40.01 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.31 | 0.0 | 0.03 | 34846.86 | 1.5 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.87 | 0.43 | -0.03 | 53580.06 | 14.37 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.03 | 369.46 | 35.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.11 | 0.02 | 41212.92 | 8.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
