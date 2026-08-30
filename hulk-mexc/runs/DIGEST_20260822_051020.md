# Hulk DIGEST — 2026-08-22T05:10:20Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 15.45 | 7.72 | 0.12 | 14474821.12 | 77.7 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 19.3 | 6.29 | 0.22 | 185284462.57 | 16.97 | skipped_fast |
| HBARUSDT | IDLE | 2.74 | 10.33 | 4.66 | 0.11 | 1176944.58 | 9.67 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.55 | 9.68 | 8.82 | -0.05 | 459377.01 | 58.21 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 11.56 | 3.25 | 0.18 | 752667.37 | 10.05 | skipped_fast |
| WUSDT | IDLE | 2.26 | 8.22 | 4.08 | 0.12 | 458994.81 | 24.83 | skipped_fast |
| BIOUSDT | IDLE | 3.22 | 9.0 | 3.93 | 0.07 | 204110.4 | 24.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 4.29 | 3.53 | 0.08 | 538485.59 | 37.06 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 8.48 | 7.81 | 0.17 | 157618.01 | 14.08 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 6.62 | 2.21 | 0.13 | 68379.83 | 28.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.41 | 4.48 | 2.3 | 0.02 | 10365.52 | 48.04 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 9.16 | 6.7 | 0.07 | 187176.91 | 91.12 | skipped_fast |
| EDELUSDT | IDLE | 1.63 | 3.28 | 2.08 | -0.03 | 81997.78 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 4.41 | 3.88 | 0.09 | 58690.5 | 35.97 | skipped_fast |
| TELUSDT | IDLE | 1.99 | 5.52 | 1.09 | 0.09 | 184380.5 | 64.92 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 3.38 | 0.08 | 0.07 | 56963.17 | 23.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.82 | 2.07 | 1.01 | 0.09 | 3808.6 | 60.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
