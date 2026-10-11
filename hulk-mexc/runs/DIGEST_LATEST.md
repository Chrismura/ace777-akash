# Hulk DIGEST — 2026-10-11T20:23:54Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.6 | 33.42 | 1.08 | 0.3 | 3283818.71 | 19.06 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 1.97 | 1.32 | 0.0 | 14968431.03 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.95 | 0.73 | 0.01 | 206599983.01 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.27 | 0.61 | 0.01 | 154532642.5 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.39 | 4.5 | 1.86 | -0.0 | 876395.92 | 1.27 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 21.91 | 11.66 | 0.01 | 40589.41 | 47.35 | skipped_fast |
| EDELUSDT | IDLE | 2.74 | 4.96 | 3.53 | -0.03 | 406906.41 | 18.46 | skipped_fast |
| ZBCNUSDT | IDLE | 2.93 | 5.28 | 3.84 | 0.0 | 200149.72 | 15.64 | skipped_fast |
| TELUSDT | IDLE | 4.0 | 7.35 | 4.36 | -0.05 | 179432.58 | 17.33 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.0 | 1.79 | 0.0 | 787227.44 | 0.41 | skipped_fast |
| CCUSDT | IDLE | 1.39 | 2.76 | 1.79 | 0.06 | 333867.83 | 6.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.31 | 5.39 | 1.51 | 0.06 | 321188.61 | 12.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.49 | 4.08 | 2.39 | 0.0 | 28742.66 | 19.62 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.09 | 1.28 | 0.01 | 57960.26 | 13.84 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.68 | 0.1 | 0.03 | 88532.49 | 3.3 | skipped_fast |
| KITEUSDT | IDLE | 0.69 | 1.28 | 0.61 | -0.0 | 73047.47 | 8.62 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.76 | 0.26 | 0.02 | 284486.55 | 6.4 | skipped_fast |
| RWAUSDT | IDLE | 1.69 | 3.13 | 1.67 | 0.02 | 52635.64 | 23.19 | skipped_fast |
| MNSRYUSDT | IDLE | 0.89 | 1.78 | 0.0 | -0.0 | 31519.1 | 4.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.33 | 2.54 | 0.61 | 0.07 | 59627.59 | 20.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
