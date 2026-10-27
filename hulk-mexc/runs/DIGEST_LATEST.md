# Hulk DIGEST — 2026-10-27T17:13:45Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.1 | 2.12 | 0.59 | 0.02 | 19507571.51 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.91 | 1.81 | 0.1 | 0.01 | 177934849.52 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.07 | 0.03 | 0.0 | 312589388.14 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.39 | 7.64 | 4.0 | 0.02 | 695119.99 | 18.7 | skipped_fast |
| QNTUSDT | IDLE | 1.91 | 3.51 | 2.09 | -0.05 | 828119.01 | 3.01 | skipped_fast |
| KITEUSDT | IDLE | 3.27 | 6.38 | 2.17 | 0.04 | 57509.31 | 9.29 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.64 | 1.45 | -0.01 | 460440.78 | 18.44 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.56 | 1.59 | -0.04 | 433289.7 | 2.77 | skipped_fast |
| REDUSDT | IDLE | 3.15 | 6.21 | 0.61 | 0.04 | 59570.79 | 14.3 | skipped_fast |
| CHIPUSDT | IDLE | 2.06 | 5.97 | 2.41 | -0.01 | 187201.85 | 22.38 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 3.51 | 0.93 | -0.01 | 238758.62 | 7.06 | skipped_fast |
| LAUSDT | IDLE | 3.71 | 7.4 | 0.13 | 0.04 | 59023.38 | 31.17 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 3.06 | 0.49 | 0.0 | 58915.37 | 13.37 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 2.12 | 0.12 | 0.03 | 256959.29 | 17.92 | skipped_fast |
| RWAINCUSDT | IDLE | 0.61 | 2.26 | 0.4 | -0.04 | 61626.74 | 20.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 1.34 | 0.3 | -0.02 | 39748.16 | 25.72 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.79 | 0.72 | -0.01 | 220732.78 | 9.2 | skipped_fast |
| WAXLUSDT | IDLE | 1.78 | 3.28 | 1.93 | 0.0 | 54059.61 | 55.38 | skipped_fast |
| RWAUSDT | IDLE | 1.44 | 2.87 | 0.08 | 0.0 | 56756.94 | 23.91 | skipped_fast |
| IOTAUSDT | IDLE | 1.1 | 2.01 | 1.22 | -0.01 | 87899.67 | 23.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.76 | 0.0 | 0.05 | 3234.8 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.77 | 0.51 | 0.0 | 37274.89 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
