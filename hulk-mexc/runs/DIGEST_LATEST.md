# Hulk DIGEST — 2026-10-18T17:05:56Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 8.52 | 5.72 | -0.07 | 1416372.89 | 2.66 | skipped_fast |
| XRPUSDT | IDLE | 1.41 | 2.52 | 1.95 | -0.01 | 24002147.3 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 1.39 | 2.48 | 1.94 | -0.01 | 99299592.64 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.34 | 1.09 | -0.0 | 218452017.21 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.73 | 4.1 | 2.81 | -0.04 | 971257.74 | 16.08 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 18.85 | 14.92 | -0.0 | 59457.2 | 59.57 | skipped_fast |
| HBARUSDT | IDLE | 2.65 | 5.07 | 3.9 | 0.05 | 715553.04 | 2.32 | skipped_fast |
| QNTUSDT | IDLE | 3.53 | 6.34 | 4.81 | -0.04 | 499130.88 | 1.58 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 12.83 | 9.24 | -0.02 | 37394.97 | 85.11 | skipped_fast |
| ZBCNUSDT | IDLE | 2.59 | 4.78 | 4.0 | -0.05 | 198055.61 | 18.73 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 5.34 | 4.91 | -0.08 | 71730.42 | 4.96 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 2.97 | 2.09 | -0.04 | 242189.58 | 10.05 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.77 | 2.48 | -0.08 | 235856.66 | 7.59 | skipped_fast |
| REDUSDT | IDLE | 2.19 | 3.89 | 3.25 | -0.03 | 96529.06 | 17.81 | skipped_fast |
| BIOUSDT | IDLE | 1.99 | 3.55 | 2.84 | -0.03 | 84624.37 | 8.61 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 3.07 | 2.48 | -0.03 | 69466.0 | 11.51 | skipped_fast |
| LAUSDT | IDLE | 2.44 | 5.77 | 4.84 | -0.07 | 58504.61 | 27.21 | skipped_fast |
| IOTAUSDT | IDLE | 1.81 | 3.24 | 2.47 | -0.04 | 68287.5 | 27.24 | skipped_fast |
| WAXLUSDT | IDLE | 1.68 | 7.51 | 4.75 | -0.02 | 73466.26 | 73.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.67 | 2.96 | 2.53 | -0.03 | 3613.52 | 21.54 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.53 | 0.71 | -0.01 | 49335.18 | 15.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.59 | 0.2 | -0.01 | 34757.1 | 36.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
