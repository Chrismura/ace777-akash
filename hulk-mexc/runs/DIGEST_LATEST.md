# Hulk DIGEST — 2026-08-26T03:53:11Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.62 | 5.41 | 1.53 | -0.0 | 2233316.92 | 3.89 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 76.3 | 38.38 | 0.11 | 59362.38 | 63.32 | skipped_fast |
| XRPUSDT | IDLE | 1.02 | 2.06 | 0.94 | -0.05 | 61714622.72 | 1.39 | skipped_fast |
| FLUIDUSDT | IDLE | 4.08 | 23.85 | 3.11 | 0.14 | 8078.62 | 14.28 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.58 | 2.42 | -0.06 | 520396.78 | 9.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 4.71 | 1.49 | -0.01 | 399333.52 | 9.25 | skipped_fast |
| WUSDT | IDLE | 1.54 | 3.09 | 0.27 | -0.01 | 292051.4 | 12.61 | skipped_fast |
| KITEUSDT | IDLE | 2.26 | 4.28 | 1.6 | -0.03 | 60462.36 | 11.51 | skipped_fast |
| REDUSDT | IDLE | 1.96 | 4.97 | 2.6 | 0.0 | 80562.19 | 9.54 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.84 | 0.84 | -0.07 | 625767.76 | 1.28 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.81 | 1.16 | -0.02 | 159121.78 | 13.72 | skipped_fast |
| EDELUSDT | IDLE | 0.7 | 9.87 | 8.98 | 0.04 | 158606.55 | 27.56 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.76 | 1.56 | -0.03 | 94009.62 | 3.45 | skipped_fast |
| QAITUSDT | IDLE | 1.17 | 3.05 | 1.48 | 0.03 | 12825.21 | 30.02 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 1.62 | 1.25 | -0.02 | 2332.29 | 95.94 | skipped_fast |
| QNTUSDT | IDLE | 0.56 | 1.05 | 0.44 | -0.03 | 131847.35 | 3.15 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 1.83 | 1.72 | -0.05 | 55613.5 | 24.97 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.12 | 0.33 | -0.03 | 93521.29 | 43.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
