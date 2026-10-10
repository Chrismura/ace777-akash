# Hulk DIGEST — 2026-10-10T11:48:22Z

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
| XRPUSDT | IDLE | 0.4 | 0.73 | 0.49 | -0.0 | 20458651.29 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.37 | 0.07 | -0.01 | 226689130.45 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.14 | 0.27 | 0.04 | -0.01 | 98620811.17 | 0.04 | skipped_fast |
| WUSDT | IDLE | 2.49 | 4.95 | 0.53 | -0.04 | 1157401.27 | 6.33 | skipped_fast |
| PYTHUSDT | IDLE | 1.04 | 2.92 | 1.95 | -0.08 | 1321967.12 | 2.55 | skipped_fast |
| QNTUSDT | IDLE | 1.92 | 3.57 | 1.82 | -0.0 | 1193773.53 | 0.4 | skipped_fast |
| EDELUSDT | IDLE | 2.86 | 7.46 | 1.43 | 0.08 | 229479.2 | 7.53 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.86 | 1.18 | -0.05 | 432726.16 | 9.96 | skipped_fast |
| KITEUSDT | IDLE | 2.28 | 4.52 | 0.28 | 0.02 | 76688.46 | 11.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.03 | 3.65 | 2.72 | -0.03 | 11416.91 | 29.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 4.08 | 3.75 | 0.03 | 97873.16 | 13.44 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.51 | 0.27 | -0.05 | 243453.6 | 0.87 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.32 | 0.93 | 0.01 | 76866.93 | 3.47 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 2.64 | 1.12 | 0.02 | 55295.85 | 13.32 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.47 | 0.62 | 0.0 | 330896.74 | 3.23 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 53210.85 | 7.87 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 2.95 | 1.8 | -0.02 | 115628.76 | 37.81 | skipped_fast |
| RIZEUSDT | IDLE | 0.36 | 1.56 | 1.12 | 0.09 | 52651.52 | 55.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 1.42 | 0.91 | -0.01 | 10666.19 | 19.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.8 | 0.35 | 0.0 | 40546.14 | 23.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
