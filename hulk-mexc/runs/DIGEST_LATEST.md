# Hulk DIGEST — 2026-09-06T20:46:03Z

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
| XRPUSDT | IDLE | 0.62 | 1.23 | 0.04 | 0.0 | 23427579.07 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.13 | 0.1 | 0.01 | 250932595.2 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.71 | 0.01 | 0.0 | 339099833.38 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.03 | 5.82 | 4.6 | 0.04 | 394329.39 | 11.67 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.71 | 0.63 | -0.0 | 528185.31 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 3.93 | 0.38 | -0.01 | 417472.15 | 3.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.44 | 5.16 | 3.8 | 0.03 | 5737.86 | 25.93 | skipped_fast |
| BIOUSDT | IDLE | 1.78 | 3.4 | 1.11 | -0.01 | 89718.06 | 7.23 | skipped_fast |
| CCUSDT | IDLE | 0.83 | 1.65 | 0.03 | 0.01 | 300892.35 | 7.25 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 3.5 | 1.59 | -0.01 | 56520.8 | 28.56 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 2.42 | 2.24 | -0.01 | 59271.05 | 8.02 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 1.57 | 0.74 | -0.0 | 165970.81 | 9.67 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.87 | 0.58 | 0.01 | 67175.03 | 10.16 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 14.15 | 11.66 | -0.19 | 71994.57 | 279.38 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.25 | 0.0 | 0.0 | 418090.71 | 1.23 | skipped_fast |
| TELUSDT | IDLE | 1.22 | 2.36 | 0.58 | 0.0 | 67791.95 | 34.66 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 1.81 | 0.08 | 0.03 | 33577.31 | 3.01 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.87 | 0.5 | -0.02 | 53763.28 | 14.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 1.06 | 0.0 | 0.03 | 392.79 | 21.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.16 | 0.01 | 41292.36 | 17.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
