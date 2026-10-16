# Hulk DIGEST — 2026-10-16T04:22:45Z

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
| WUSDT | IDLE | 2.81 | 7.08 | 0.17 | 0.03 | 2349086.86 | 15.58 | skipped_fast |
| PYTHUSDT | IDLE | 0.54 | 3.35 | 0.38 | 0.11 | 4248931.09 | 14.75 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.29 | 0.57 | 0.03 | 247194314.3 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.31 | 0.43 | 0.02 | 40686292.23 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.01 | 0.53 | 0.01 | 448936144.52 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 3.35 | 1.47 | 0.06 | 1172260.6 | 1.45 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 3.28 | 0.91 | -0.02 | 431596.86 | 6.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 10.67 | 2.32 | 0.09 | 184645.0 | 9.88 | skipped_fast |
| REDUSDT | IDLE | 2.18 | 6.55 | 4.51 | -0.06 | 94170.53 | 8.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 3.2 | 2.09 | 0.04 | 185871.67 | 18.46 | skipped_fast |
| KITEUSDT | IDLE | 1.93 | 3.44 | 2.86 | 0.01 | 67684.93 | 10.7 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 2.46 | 1.35 | -0.1 | 217423.1 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.54 | 2.9 | 2.81 | 0.0 | 28835.82 | 10.13 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.08 | 0.5 | 0.03 | 73683.03 | 7.74 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 2.26 | 1.45 | 0.04 | 213587.48 | 4.71 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 1.73 | 1.44 | 0.04 | 73082.44 | 53.36 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 1.53 | 0.78 | 0.04 | 83902.52 | 22.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.74 | 0.69 | -0.01 | 9439.62 | 21.6 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.48 | 0.16 | 0.02 | 52542.05 | 7.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.37 | 0.14 | 0.0 | 38267.15 | 23.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
