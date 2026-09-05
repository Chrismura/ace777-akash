# Hulk DIGEST — 2026-09-05T11:22:16Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 57.48 | 33.06 | -0.04 | 220845.34 | 9.34 | skipped_fast |
| XRPUSDT | IDLE | 0.48 | 0.89 | 0.53 | -0.03 | 37972365.59 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.4 | 0.29 | -0.03 | 362954943.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.25 | 0.16 | -0.02 | 496950184.09 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 25.72 | 18.1 | -0.19 | 156089.32 | 70.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 5.87 | 5.53 | -0.01 | 451929.11 | 1.77 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 1.7 | 0.59 | -0.02 | 427432.49 | 1.85 | skipped_fast |
| CCUSDT | IDLE | 0.53 | 0.99 | 0.42 | -0.02 | 330811.25 | 10.14 | skipped_fast |
| WUSDT | IDLE | 0.76 | 1.4 | 0.75 | 0.01 | 204076.5 | 1.01 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 1.42 | 0.18 | -0.04 | 198466.51 | 8.46 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.32 | 1.88 | 0.04 | 65958.96 | 19.81 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.11 | 1.2 | -0.03 | 63435.14 | 8.38 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 1.39 | 1.23 | -0.01 | 85033.3 | 10.98 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.6 | 0.58 | 0.02 | 288076.2 | 1.25 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.38 | 0.36 | 0.01 | 52851.97 | 14.28 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 1.52 | 1.33 | -0.01 | 5271.81 | 107.41 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.72 | 0.87 | -0.03 | 73273.27 | 17.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.92 | 0.0 | -0.01 | 1031.33 | 22.51 | skipped_fast |
| QNTUSDT | IDLE | 0.48 | 0.91 | 0.37 | -0.04 | 44975.88 | 3.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.31 | 0.2 | -0.0 | 36391.52 | 30.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
