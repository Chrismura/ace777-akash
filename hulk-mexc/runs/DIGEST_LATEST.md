# Hulk DIGEST — 2026-08-21T19:54:56Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 3.9 | 0.07 | 5437361.03 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.59 | 0.11 | 129211852.12 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 14.12 | 0.16 | 153948.87 | 20.59 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.39 | 0.07 | 481712.14 | 20.74 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 5.44 | 1.94 | 0.06 | 633474.04 | 5.62 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 3.1 | 2.76 | 0.05 | 792575.85 | 2.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 4.81 | 4.35 | 0.09 | 514400.27 | 3.11 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.57 | -0.0 | 190629.09 | 3.21 | skipped_fast |
| WUSDT | IDLE | 2.14 | 3.92 | 2.71 | 0.05 | 360099.84 | 22.46 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 11.27 | 2.82 | 0.02 | 56450.38 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79634.69 | 33.76 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 3.21 | 0.1 | 61270.28 | 11.26 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 75.11 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.46 | 2.26 | 0.01 | 183456.42 | 32.35 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | 0.0 | 2888.48 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 1.64 | 3.01 | 1.77 | 0.04 | 59887.26 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54203.07 | 24.91 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 22.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
