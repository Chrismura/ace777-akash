# Hulk DIGEST — 2026-10-16T22:06:50Z

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
| PYTHUSDT | IDLE | 1.42 | 5.2 | 0.0 | -0.09 | 1948661.38 | 1.14 | skipped_fast |
| WUSDT | IDLE | 2.33 | 6.24 | 2.36 | -0.02 | 1555531.29 | 12.43 | skipped_fast |
| XRPUSDT | IDLE | 1.01 | 1.98 | 0.33 | -0.02 | 28876102.76 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.65 | 0.44 | -0.02 | 209231486.81 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.21 | 0.06 | -0.01 | 349548018.91 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.71 | 3.24 | 1.25 | -0.02 | 758546.41 | 2.46 | skipped_fast |
| EDELUSDT | IDLE | 2.36 | 4.25 | 3.12 | 0.01 | 189034.72 | 16.95 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 2.47 | 0.56 | -0.03 | 345796.96 | 7.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 8.45 | 4.8 | -0.12 | 28535.59 | 16.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.27 | 1.51 | -0.02 | 190847.61 | 26.68 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 3.7 | 0.82 | -0.07 | 97235.17 | 10.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.66 | 2.6 | 0.37 | -0.04 | 154977.16 | 13.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.04 | 2.21 | 1.86 | -0.01 | 45787.81 | 2.06 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.98 | 0.09 | -0.02 | 57838.0 | 9.87 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.9 | 0.28 | -0.03 | 61752.64 | 11.93 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 5.1 | 0.2 | 0.0 | 7252.3 | 21.09 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.75 | 0.0 | -0.02 | 315212.1 | 4.79 | skipped_fast |
| RWAUSDT | IDLE | 1.43 | 2.76 | 0.71 | -0.0 | 53260.51 | 15.91 | skipped_fast |
| TELUSDT | IDLE | 1.29 | 2.29 | 1.91 | -0.02 | 91154.08 | 40.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.76 | 0.69 | -0.01 | 34112.2 | 27.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
