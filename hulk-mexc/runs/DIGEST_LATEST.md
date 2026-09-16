# Hulk DIGEST — 2026-09-16T11:12:47Z

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
| ETHUSDT | IDLE | 0.63 | 1.23 | 0.17 | -0.03 | 485553599.97 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 1.91 | 1.01 | -0.08 | 94579490.93 | 2.33 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.97 | 0.18 | -0.02 | 589350441.89 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 2.7 | 2.59 | -0.04 | 670612.06 | 1.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.65 | 21.64 | 1.38 | 0.42 | 48364.76 | 51.22 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 8.04 | 2.19 | 0.47 | 439388.41 | 40.26 | skipped_fast |
| REDUSDT | IDLE | 2.18 | 4.02 | 2.27 | -0.03 | 67857.93 | 17.56 | skipped_fast |
| CCUSDT | IDLE | 0.58 | 1.04 | 0.82 | -0.05 | 384802.81 | 8.8 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 2.77 | 2.39 | -0.07 | 60184.83 | 6.02 | skipped_fast |
| WUSDT | IDLE | 0.91 | 2.06 | 1.25 | -0.08 | 207151.56 | 11.23 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 2.49 | 1.48 | -0.08 | 204111.23 | 27.04 | skipped_fast |
| CHIPUSDT | IDLE | 0.88 | 2.55 | 1.79 | -0.11 | 102495.9 | 13.6 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.22 | 0.57 | -0.04 | 443924.72 | 1.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.32 | 2.39 | 1.71 | -0.04 | 14496.78 | 23.22 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 1.63 | 0.12 | -0.01 | 82416.58 | 8.04 | skipped_fast |
| TELUSDT | IDLE | 1.53 | 2.97 | 2.75 | -0.07 | 112004.78 | 13.78 | skipped_fast |
| QNTUSDT | IDLE | 0.98 | 1.77 | 1.33 | -0.05 | 44605.0 | 6.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.62 | 1.59 | -0.06 | 1534.48 | 20.31 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.53 | -0.01 | 52047.32 | 45.66 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.47 | 0.08 | -0.02 | 32990.43 | 5.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
