# Hulk DIGEST — 2026-08-21T19:48:24Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 3.98 | 0.07 | 5425929.3 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.16 | 4.21 | 3.37 | 0.11 | 129085052.65 | 0.73 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.58 | 0.16 | 153485.85 | 9.01 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 11.37 | 9.64 | 0.06 | 482192.07 | 31.71 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 5.44 | 1.8 | 0.06 | 631134.48 | 9.34 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.08 | 2.96 | 0.05 | 790391.56 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.0 | 0.09 | 514471.39 | 3.11 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.83 | 0.05 | 360814.18 | 13.9 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.57 | -0.0 | 190287.38 | 3.21 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79601.32 | 22.52 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 2.87 | 0.02 | 56479.52 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.45 | 0.09 | 61015.24 | 11.29 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 75.11 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2917.53 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.46 | 2.26 | 0.01 | 184033.93 | 37.69 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 3.01 | 2.15 | 0.04 | 59834.56 | 9.43 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.16 | 1.07 | 0.04 | 54403.62 | 24.91 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4331.26 | 22.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
