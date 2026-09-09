# Hulk DIGEST — 2026-09-09T19:13:54Z

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
| XRPUSDT | IDLE | 1.07 | 1.98 | 1.1 | -0.01 | 41013958.44 | 2.82 | skipped_fast |
| ETHUSDT | IDLE | 0.96 | 1.72 | 1.29 | -0.0 | 329249706.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.95 | 1.72 | 1.21 | 0.0 | 526421830.91 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.45 | 4.47 | 2.82 | 0.04 | 587962.36 | 1.8 | skipped_fast |
| EDELUSDT | IDLE | 3.26 | 5.88 | 4.26 | -0.0 | 179335.65 | 48.29 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.48 | 1.42 | -0.03 | 545046.32 | 6.72 | skipped_fast |
| WUSDT | IDLE | 3.0 | 5.91 | 0.65 | 0.03 | 184082.22 | 16.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.25 | 1.0 | 0.03 | 199093.73 | 15.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 5.13 | 4.76 | 0.06 | 112366.47 | 12.58 | skipped_fast |
| REDUSDT | IDLE | 1.81 | 3.25 | 2.49 | 0.01 | 61022.17 | 19.95 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.83 | 1.25 | -0.02 | 95708.52 | 3.71 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.7 | 1.15 | 0.01 | 63918.06 | 11.31 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.83 | 1.03 | -0.02 | 406268.22 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.4 | 1.69 | -0.01 | 7252.77 | 16.62 | skipped_fast |
| TELUSDT | IDLE | 2.26 | 4.06 | 3.05 | 0.03 | 101921.5 | 33.11 | skipped_fast |
| FLUIDUSDT | IDLE | 2.77 | 4.85 | 4.61 | -0.05 | 793.11 | 51.9 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 9.03 | 7.4 | -0.03 | 70718.21 | 116.46 | skipped_fast |
| RWAUSDT | IDLE | 1.44 | 2.56 | 2.07 | -0.01 | 54023.83 | 21.81 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.52 | 0.67 | -0.01 | 44604.3 | 5.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.45 | 0.38 | 0.0 | 23524.28 | 43.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
