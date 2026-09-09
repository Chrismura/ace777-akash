# Hulk DIGEST — 2026-09-09T19:14:24Z

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
| XRPUSDT | IDLE | 1.07 | 1.98 | 1.12 | -0.01 | 41001406.19 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.95 | 1.72 | 1.19 | -0.0 | 526464789.34 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.72 | 1.26 | -0.0 | 329013603.67 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.45 | 4.47 | 2.88 | 0.04 | 587986.02 | 1.81 | skipped_fast |
| EDELUSDT | IDLE | 3.26 | 5.88 | 4.26 | -0.0 | 179335.65 | 48.29 | skipped_fast |
| WUSDT | IDLE | 3.01 | 5.91 | 0.75 | 0.03 | 184061.86 | 10.55 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.48 | 1.37 | -0.02 | 545068.0 | 6.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.25 | 0.99 | 0.03 | 199111.85 | 18.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 5.13 | 4.76 | 0.06 | 112368.37 | 10.79 | skipped_fast |
| REDUSDT | IDLE | 1.81 | 3.25 | 2.49 | 0.01 | 61035.18 | 8.46 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.83 | 1.21 | -0.02 | 95735.04 | 3.71 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.7 | 0.98 | 0.01 | 63937.38 | 11.31 | skipped_fast |
| FLUIDUSDT | IDLE | 2.77 | 4.85 | 4.61 | -0.05 | 793.11 | 11.51 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.83 | 0.99 | -0.02 | 408439.68 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.4 | 1.69 | -0.01 | 7252.77 | 11.08 | skipped_fast |
| TELUSDT | IDLE | 2.26 | 4.06 | 3.05 | 0.03 | 101921.5 | 38.64 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 9.03 | 7.4 | -0.02 | 70716.53 | 116.46 | skipped_fast |
| RWAUSDT | IDLE | 1.44 | 2.56 | 2.07 | -0.01 | 54057.34 | 21.81 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.52 | 0.67 | -0.01 | 44596.85 | 5.97 | skipped_fast |
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
