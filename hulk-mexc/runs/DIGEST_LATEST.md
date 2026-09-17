# Hulk DIGEST — 2026-09-17T15:16:33Z

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
| XRPUSDT | IDLE | 1.29 | 2.29 | 1.9 | 0.02 | 57550903.4 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.22 | 2.25 | 1.33 | 0.02 | 394849816.53 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.48 | 1.11 | 0.01 | 499514902.45 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.48 | 1.24 | 0.05 | 588216.42 | 7.29 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 4.1 | 0.5 | 0.13 | 611013.98 | 5.86 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.82 | 20.66 | 7.25 | -0.14 | 47347.52 | 101.18 | skipped_fast |
| EDELUSDT | IDLE | 2.41 | 7.02 | 2.62 | -0.04 | 185778.68 | 24.08 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 4.65 | 1.99 | 0.03 | 195888.55 | 14.74 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.28 | 1.62 | 0.04 | 597081.58 | 1.33 | skipped_fast |
| CHIPUSDT | IDLE | 2.2 | 7.14 | 4.07 | 0.06 | 139750.46 | 12.99 | skipped_fast |
| REDUSDT | IDLE | 2.65 | 5.24 | 3.23 | 0.04 | 66231.82 | 18.29 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.85 | 1.61 | 0.05 | 212152.11 | 11.8 | skipped_fast |
| RWAINCUSDT | IDLE | 1.95 | 3.46 | 2.94 | -0.01 | 21339.33 | 23.68 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.66 | 3.42 | 0.04 | 68703.5 | 8.75 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.09 | 1.45 | 0.03 | 65874.72 | 11.96 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 4.13 | 1.48 | 0.04 | 90852.85 | 61.45 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.09 | 1.05 | 0.03 | 36536.83 | 4.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.89 | 1.7 | 0.54 | 0.01 | 40477.2 | 9.78 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.06 | 0.97 | 0.0 | 58160.49 | 22.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 143.49 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
