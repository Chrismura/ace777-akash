# Hulk DIGEST — 2026-08-30T17:14:09Z

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
| ETHUSDT | IDLE | 1.56 | 3.05 | 0.46 | 0.03 | 205066165.53 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 2.44 | 0.18 | 0.02 | 20096148.36 | 1.41 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.58 | 0.3 | 0.01 | 270978932.52 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.33 | 5.86 | -0.03 | 525173.89 | 2.5 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 9.26 | 5.55 | -0.06 | 194655.63 | 17.71 | skipped_fast |
| PYTHUSDT | IDLE | 3.0 | 5.66 | 2.33 | 0.03 | 399533.43 | 4.08 | skipped_fast |
| WUSDT | IDLE | 1.51 | 3.01 | 0.03 | 0.05 | 222958.63 | 11.45 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 5.99 | 3.63 | 0.07 | 72562.44 | 58.55 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.13 | 0.01 | 256919.39 | 10.13 | skipped_fast |
| REDUSDT | IDLE | 1.08 | 2.02 | 0.92 | 0.02 | 61618.92 | 13.56 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.65 | 0.18 | 0.0 | 79462.26 | 3.62 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.67 | 1.14 | -0.02 | 60877.01 | 8.59 | skipped_fast |
| TELUSDT | IDLE | 2.2 | 4.37 | 0.17 | 0.0 | 83558.74 | 34.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 3.06 | 2.09 | -0.06 | 38359.45 | 61.18 | skipped_fast |
| HBARUSDT | IDLE | 0.58 | 1.17 | 0.0 | 0.0 | 131158.65 | 2.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.01 | 32297.53 | 2.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.98 | 0.0 | 0.02 | 52680.02 | 8.09 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.97 | 0.19 | 0.01 | 38430.37 | 4.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
