# Hulk DIGEST — 2026-10-27T01:36:39Z

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
| XRPUSDT | IDLE | 1.15 | 2.19 | 0.67 | 0.01 | 24790649.41 | 2.3 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.3 | 0.44 | 0.0 | 131444734.32 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.83 | 0.33 | 0.0 | 355735993.12 | 0.19 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 1.99 | 1.32 | 0.07 | 1396321.6 | 2.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.73 | 3.12 | 2.21 | -0.01 | 699590.28 | 2.71 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.99 | 1.43 | 0.04 | 641060.49 | 24.22 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 5.48 | 3.97 | 0.18 | 328629.46 | 17.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.55 | 5.5 | 4.72 | -0.12 | 59972.12 | 12.88 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 2.16 | 1.29 | 0.02 | 172504.34 | 6.21 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.96 | 0.91 | -0.02 | 187616.74 | 7.05 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.95 | 1.88 | 0.02 | 61807.22 | 16.39 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 1.78 | 0.39 | -0.04 | 217942.1 | 28.78 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.19 | 0.67 | -0.0 | 57011.84 | 8.99 | skipped_fast |
| KITEUSDT | IDLE | 0.69 | 1.22 | 1.13 | 0.0 | 54104.46 | 8.8 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.66 | 0.59 | 0.0 | 241417.83 | 7.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 1.4 | 0.88 | -0.01 | 44074.58 | 65.34 | skipped_fast |
| IOTAUSDT | IDLE | 1.47 | 2.75 | 1.3 | -0.0 | 90107.32 | 23.56 | skipped_fast |
| WAXLUSDT | IDLE | 1.66 | 3.11 | 1.43 | -0.03 | 53052.7 | 37.95 | skipped_fast |
| LAUSDT | IDLE | 1.47 | 2.89 | 2.08 | 0.03 | 67811.91 | 35.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 2.68 | 0.18 | 0.04 | 2288.53 | 21.77 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.21 | 0.48 | -0.0 | 53296.08 | 15.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.32 | -0.0 | 41474.48 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
