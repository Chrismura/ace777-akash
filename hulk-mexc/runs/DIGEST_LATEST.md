# Hulk DIGEST — 2026-09-11T23:22:12Z

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
| RIZEUSDT | IDLE | 1.59 | 108.76 | 44.74 | 0.67 | 218783.13 | 96.26 | skipped_fast |
| ETHUSDT | IDLE | 1.19 | 2.5 | 2.12 | 0.03 | 655967533.22 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.67 | 1.02 | 0.01 | 54814904.8 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.83 | 0.52 | 0.01 | 596048318.38 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.17 | 8.94 | 3.5 | 0.04 | 166357.26 | 8.83 | skipped_fast |
| PYTHUSDT | IDLE | 1.96 | 3.73 | 2.36 | -0.02 | 408701.45 | 1.97 | skipped_fast |
| CCUSDT | IDLE | 1.26 | 2.28 | 1.6 | -0.01 | 435018.0 | 10.29 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 3.81 | 2.83 | 0.01 | 196361.64 | 5.57 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.46 | 4.27 | 0.01 | 14427.98 | 5.51 | skipped_fast |
| WUSDT | IDLE | 1.7 | 3.24 | 2.37 | 0.01 | 200189.95 | 11.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 4.93 | 3.08 | -0.01 | 139952.27 | 17.09 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.94 | 1.23 | 0.01 | 78824.33 | 8.03 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.27 | 0.5 | 0.05 | 63721.37 | 18.03 | skipped_fast |
| KITEUSDT | IDLE | 0.75 | 1.35 | 0.94 | -0.0 | 59349.01 | 10.18 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 4.27 | 3.2 | -0.02 | 103922.44 | 63.64 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 2.77 | 2.34 | -0.03 | 46700.0 | 4.76 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.2 | 0.72 | -0.01 | 257155.2 | 1.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 2.66 | 2.19 | 0.04 | 1265.76 | 22.54 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.9 | 0.22 | 0.03 | 53157.35 | 7.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.47 | 0.85 | 0.61 | 0.0 | 35658.6 | 26.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
