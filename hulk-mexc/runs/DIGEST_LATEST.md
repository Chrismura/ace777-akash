# Hulk DIGEST — 2026-08-30T21:14:54Z

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
| XRPUSDT | IDLE | 1.99 | 3.55 | 2.92 | -0.0 | 24436309.78 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 1.65 | 2.95 | 2.37 | 0.01 | 240245629.22 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.48 | 1.15 | 0.0 | 293092377.92 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 5.37 | 3.79 | -0.04 | 569601.86 | 2.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.64 | 4.7 | 3.87 | 0.0 | 406897.1 | 2.07 | skipped_fast |
| ZBCNUSDT | IDLE | 2.86 | 5.98 | 4.38 | -0.04 | 196105.92 | 16.4 | skipped_fast |
| KITEUSDT | IDLE | 3.1 | 5.5 | 4.62 | -0.05 | 62195.93 | 10.52 | skipped_fast |
| WUSDT | IDLE | 2.17 | 3.92 | 2.79 | 0.02 | 231361.03 | 10.72 | skipped_fast |
| REDUSDT | IDLE | 2.21 | 3.94 | 3.2 | -0.01 | 63446.48 | 12.02 | skipped_fast |
| BIOUSDT | IDLE | 2.02 | 3.66 | 2.59 | -0.02 | 85957.78 | 3.69 | skipped_fast |
| EDELUSDT | IDLE | 1.83 | 5.22 | 0.73 | 0.1 | 74368.04 | 24.58 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.5 | 0.57 | -0.0 | 236382.38 | 7.61 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 5.3 | 1.78 | 0.01 | 41766.53 | 61.0 | skipped_fast |
| TELUSDT | IDLE | 2.02 | 3.69 | 2.37 | -0.0 | 89153.48 | 46.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.24 | 2.14 | -0.0 | 1503.99 | 72.52 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.87 | 1.34 | -0.01 | 164500.81 | 2.66 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.4 | 1.82 | -0.0 | 38025.13 | 6.55 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.04 | 1.99 | 0.01 | 3303.62 | 21.07 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.3 | 0.16 | 0.02 | 52679.64 | 16.1 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 0.95 | 0.59 | 0.0 | 31535.63 | 73.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
