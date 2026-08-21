# Hulk DIGEST — 2026-08-21T19:39:04Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 4.04 | 0.06 | 5421059.2 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.14 | 4.21 | 2.66 | 0.12 | 129180374.49 | 2.17 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 26.97 | 13.28 | 0.16 | 153686.17 | 12.27 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 11.37 | 9.57 | 0.06 | 480983.41 | 40.57 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 5.44 | 2.21 | 0.06 | 630410.51 | 10.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.03 | 0.09 | 519195.75 | 6.21 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.88 | 0.04 | 360271.46 | 14.98 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.6 | -0.0 | 190493.09 | 3.21 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 2.85 | 2.3 | 0.06 | 751964.87 | 1.3 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 11.27 | 4.0 | 0.01 | 56478.52 | 33.74 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79608.0 | 11.25 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.52 | 0.09 | 60888.28 | 13.18 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.3 | 1.27 | 0.05 | 10999.86 | 113.06 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2950.35 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 4.46 | 2.05 | 0.03 | 184110.92 | 37.62 | skipped_fast |
| QNTUSDT | IDLE | 1.64 | 3.01 | 1.85 | 0.04 | 59902.33 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.9 | 0.04 | 54234.02 | 16.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4341.25 | 19.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
