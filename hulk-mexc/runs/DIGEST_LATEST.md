# Hulk DIGEST — 2026-09-19T16:59:25Z

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
| XRPUSDT | IDLE | 1.34 | 2.5 | 1.22 | 0.04 | 60663517.17 | 2.79 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.91 | 0.1 | 0.01 | 512310787.87 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.9 | 0.07 | 0.02 | 367818370.7 | 0.04 | skipped_fast |
| WUSDT | IDLE | 2.62 | 4.86 | 2.58 | 0.02 | 665953.2 | 2.7 | skipped_fast |
| ZBCNUSDT | IDLE | 3.72 | 15.2 | 2.46 | 0.13 | 223959.57 | 24.41 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 2.14 | 0.8 | 0.01 | 676487.15 | 3.3 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 9.89 | 6.28 | -0.03 | 5773.78 | 90.5 | skipped_fast |
| BIOUSDT | IDLE | 2.85 | 5.34 | 2.46 | 0.04 | 84737.96 | 10.67 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 3.14 | 0.45 | 0.04 | 355418.2 | 6.18 | skipped_fast |
| CHIPUSDT | IDLE | 2.3 | 5.65 | 3.81 | 0.01 | 127482.21 | 22.82 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.37 | 0.24 | 0.05 | 528474.39 | 1.22 | skipped_fast |
| EDELUSDT | IDLE | 1.17 | 6.78 | 3.57 | -0.15 | 171812.54 | 62.16 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.05 | 0.8 | 0.06 | 70923.24 | 12.05 | skipped_fast |
| REDUSDT | IDLE | 0.63 | 2.7 | 2.06 | 0.01 | 133555.04 | 10.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.5 | 6.49 | 5.49 | 0.05 | 38380.15 | 99.13 | skipped_fast |
| TELUSDT | IDLE | 1.36 | 4.13 | 2.43 | -0.01 | 128461.36 | 32.54 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.1 | 1.0 | 0.03 | 47215.86 | 7.65 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.55 | 0.66 | 0.0 | 54082.85 | 7.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.04 | 3.11 | 0.0 | 0.12 | 9838.49 | 23.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.83 | 1.52 | 0.96 | -0.0 | 36519.2 | 63.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
