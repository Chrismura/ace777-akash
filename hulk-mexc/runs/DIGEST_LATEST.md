# Hulk DIGEST — 2026-10-23T16:50:15Z

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
| XRPUSDT | IDLE | 0.92 | 1.69 | 0.96 | -0.0 | 27895843.08 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.6 | 0.32 | 0.02 | 216306703.99 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.36 | 0.01 | 311035599.41 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.63 | 3.17 | 0.62 | -0.03 | 1195054.76 | 0.55 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 4.93 | 1.7 | 0.01 | 467344.01 | 6.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.71 | 0.97 | -0.02 | 707578.59 | 2.79 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.45 | 1.7 | 0.01 | 620264.8 | 16.47 | skipped_fast |
| RIZEUSDT | IDLE | 2.83 | 11.71 | 4.21 | -0.02 | 68035.43 | 56.53 | skipped_fast |
| CCUSDT | IDLE | 1.73 | 3.27 | 1.23 | 0.02 | 195707.71 | 7.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.11 | 4.28 | 1.26 | 0.03 | 115313.4 | 15.64 | skipped_fast |
| REDUSDT | IDLE | 2.36 | 4.69 | 0.15 | 0.03 | 60571.38 | 15.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 3.34 | 1.52 | 0.02 | 197814.89 | 19.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.8 | 3.48 | 0.76 | 0.03 | 51045.61 | 27.27 | skipped_fast |
| LAUSDT | IDLE | 2.73 | 6.91 | 1.27 | 0.09 | 57306.4 | 22.29 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.71 | 0.16 | 0.03 | 71131.99 | 8.26 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.09 | 0.93 | 0.01 | 58034.12 | 9.13 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.2 | 1.6 | -0.0 | 288029.07 | 6.32 | skipped_fast |
| WAXLUSDT | IDLE | 2.03 | 3.95 | 0.69 | 0.02 | 57135.7 | 26.61 | skipped_fast |
| IOTAUSDT | IDLE | 1.52 | 3.01 | 0.2 | 0.03 | 71156.22 | 10.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.76 | 3.53 | 0.0 | 0.01 | 8838.85 | 21.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.32 | 1.02 | -0.01 | 36170.82 | 74.39 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.55 | 0.55 | 0.02 | 52080.21 | 39.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
