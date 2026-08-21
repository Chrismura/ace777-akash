# Hulk DIGEST — 2026-08-21T19:53:07Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 4.0 | 0.07 | 5433827.56 | 4.25 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.61 | 0.12 | 129239373.49 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.66 | 0.16 | 153976.32 | 19.69 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.29 | 0.07 | 481828.6 | 17.61 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 5.44 | 1.96 | 0.06 | 633492.02 | 2.81 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.09 | 2.99 | 0.05 | 792353.03 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 4.81 | 4.24 | 0.09 | 514419.86 | 6.23 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.85 | 0.05 | 360491.8 | 7.5 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.6 | -0.0 | 190229.25 | 3.22 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 3.06 | 0.02 | 56434.11 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 4.29 | 3.9 | -0.04 | 79609.66 | 33.76 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 3.22 | 0.1 | 61224.17 | 11.26 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 80.49 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.46 | 2.32 | 0.01 | 183402.96 | 32.33 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | 0.0 | 2888.48 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.03 | 0.04 | 59852.97 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54287.11 | 16.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 21.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
