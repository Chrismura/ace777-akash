# Hulk DIGEST — 2026-10-26T15:23:16Z

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
| ETHUSDT | IDLE | 1.07 | 2.11 | 0.24 | -0.0 | 131793580.29 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.02 | 2.01 | 0.16 | 0.01 | 22606993.32 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.69 | 0.18 | -0.0 | 312960156.24 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.89 | 8.84 | 5.22 | 0.14 | 1500354.89 | 7.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.05 | 0.73 | 0.06 | 919876.06 | 3.95 | skipped_fast |
| WUSDT | IDLE | 3.07 | 5.96 | 1.2 | 0.02 | 559383.36 | 27.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 13.6 | 2.72 | 0.16 | 164839.82 | 25.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.64 | 0.13 | -0.02 | 215515.78 | 21.91 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.74 | 0.28 | -0.0 | 198466.99 | 12.82 | skipped_fast |
| REDUSDT | IDLE | 1.49 | 2.98 | 0.0 | 0.04 | 61318.8 | 15.42 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.78 | 0.04 | 0.01 | 59708.17 | 8.87 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.74 | 0.28 | 0.02 | 53290.06 | 12.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.42 | 0.63 | -0.05 | 64056.47 | 5.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.8 | 3.33 | 1.8 | 0.01 | 34221.04 | 64.89 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 2.24 | 1.23 | 0.08 | 130309.7 | 34.43 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.48 | 0.1 | 0.01 | 224294.7 | 3.85 | skipped_fast |
| WAXLUSDT | IDLE | 1.78 | 3.57 | 0.0 | -0.01 | 53118.6 | 50.97 | skipped_fast |
| LAUSDT | IDLE | 1.32 | 2.81 | 0.46 | 0.03 | 63634.21 | 22.2 | skipped_fast |
| IOTAUSDT | IDLE | 1.24 | 2.44 | 0.32 | 0.0 | 73775.14 | 25.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.99 | 0.34 | -0.02 | 1803.36 | 21.37 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.44 | 0.63 | -0.0 | 54329.25 | 31.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.54 | -0.01 | 42744.91 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
