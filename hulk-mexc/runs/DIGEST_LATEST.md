# Hulk DIGEST — 2026-10-19T09:56:20Z

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
| ETHUSDT | IDLE | 0.55 | 1.07 | 0.15 | 0.01 | 141288443.52 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.54 | 1.02 | 0.46 | 0.01 | 30897752.76 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.81 | 0.2 | 0.01 | 320015222.75 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 3.01 | 1.66 | -0.06 | 997960.12 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 5.6 | 0.32 | 0.03 | 742151.81 | 3.94 | skipped_fast |
| WUSDT | IDLE | 1.21 | 2.17 | 1.7 | -0.05 | 515768.17 | 17.94 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.04 | 2.66 | 0.03 | 237168.23 | 18.45 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.69 | 0.97 | -0.03 | 799283.66 | 4.74 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.62 | 0.77 | 0.01 | 316069.5 | 6.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 5.06 | 0.83 | -0.0 | 83679.04 | 5.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 2.33 | 0.56 | 0.02 | 299398.49 | 14.48 | skipped_fast |
| KITEUSDT | IDLE | 1.7 | 3.34 | 0.36 | 0.03 | 63469.6 | 12.73 | skipped_fast |
| CHIPUSDT | IDLE | 0.96 | 2.54 | 1.6 | -0.0 | 78845.85 | 11.76 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.53 | 0.55 | -0.01 | 79319.97 | 8.43 | skipped_fast |
| REDUSDT | IDLE | 0.8 | 1.41 | 1.23 | -0.03 | 76893.04 | 10.25 | skipped_fast |
| WAXLUSDT | IDLE | 0.94 | 3.7 | 2.06 | 0.01 | 79015.68 | 27.65 | skipped_fast |
| LAUSDT | IDLE | 1.13 | 2.17 | 0.63 | -0.02 | 59555.92 | 20.66 | skipped_fast |
| IOTAUSDT | IDLE | 1.04 | 1.88 | 1.32 | -0.02 | 69355.74 | 22.29 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.83 | 1.56 | 0.0 | 55339.89 | 15.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 3.26 | 1.49 | -0.05 | 58804.02 | 139.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.04 | 2.65 | 1.87 | 0.01 | 6399.52 | 21.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.1 | -0.0 | 39889.41 | 24.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
