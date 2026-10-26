# Hulk DIGEST — 2026-10-26T19:30:53Z

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
| ETHUSDT | IDLE | 1.1 | 2.02 | 1.24 | -0.01 | 143218993.26 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.98 | 1.83 | 0.88 | -0.0 | 24410369.05 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.53 | 1.07 | -0.01 | 352347121.94 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.89 | 7.97 | 6.49 | 0.06 | 1433576.26 | 3.43 | skipped_fast |
| PYTHUSDT | IDLE | 2.39 | 4.2 | 3.85 | -0.01 | 913145.23 | 4.05 | skipped_fast |
| WUSDT | IDLE | 3.05 | 6.36 | 0.92 | 0.04 | 654480.0 | 48.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.3 | 18.66 | 4.88 | 0.2 | 311112.3 | 16.61 | skipped_fast |
| RWAINCUSDT | IDLE | 3.12 | 13.37 | 3.74 | -0.07 | 58284.07 | 17.95 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 4.44 | 3.52 | 0.02 | 92813.52 | 24.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.32 | 4.4 | 1.57 | 0.0 | 45591.82 | 9.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 2.78 | 2.1 | -0.06 | 201407.22 | 17.53 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 2.11 | 2.04 | -0.03 | 203486.91 | 7.03 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 3.18 | 2.29 | -0.01 | 59599.66 | 9.02 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 2.9 | 2.18 | 0.01 | 63127.82 | 15.77 | skipped_fast |
| KITEUSDT | IDLE | 1.16 | 2.22 | 0.69 | 0.02 | 54092.68 | 14.0 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.07 | 1.41 | -0.01 | 259839.69 | 3.9 | skipped_fast |
| WAXLUSDT | IDLE | 2.23 | 4.01 | 2.94 | -0.02 | 53401.7 | 64.81 | skipped_fast |
| LAUSDT | IDLE | 1.71 | 3.41 | 2.08 | 0.01 | 64365.37 | 24.08 | skipped_fast |
| IOTAUSDT | IDLE | 1.57 | 2.83 | 2.06 | -0.02 | 84045.26 | 26.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.35 | 2.0 | -0.06 | 702.73 | 21.84 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.28 | 0.63 | 0.0 | 53956.77 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.5 | -0.0 | 42127.53 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
