# Hulk DIGEST — 2026-09-07T08:47:20Z

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
| XRPUSDT | IDLE | 1.04 | 1.95 | 0.84 | -0.01 | 31937693.51 | 2.85 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.64 | 0.95 | -0.0 | 307033729.16 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.67 | 1.24 | 0.65 | -0.0 | 412111985.96 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 9.19 | 7.64 | -0.09 | 406810.94 | 18.62 | skipped_fast |
| PYTHUSDT | IDLE | 1.93 | 3.55 | 2.13 | 0.0 | 598839.64 | 1.81 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.49 | 7.96 | 6.83 | -0.03 | 65397.09 | 58.08 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.73 | 1.69 | 0.03 | 451001.31 | 18.34 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.91 | 1.25 | -0.0 | 416470.53 | 10.06 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 3.1 | 3.01 | -0.03 | 56598.28 | 12.15 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 5.5 | 4.51 | 0.06 | 6626.13 | 29.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 9.5 | 0.98 | -0.14 | 72493.67 | 56.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.89 | 1.01 | -0.03 | 159553.3 | 11.82 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.39 | 0.8 | -0.01 | 74066.29 | 3.67 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.25 | 0.81 | -0.0 | 62933.4 | 10.16 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.81 | 1.07 | -0.0 | 366310.09 | 1.24 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 2.46 | 1.6 | 0.01 | 100130.31 | 52.37 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 1.88 | 1.35 | 0.01 | 36459.61 | 4.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.01 | 1152.45 | 20.43 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.65 | 0.43 | -0.01 | 53814.79 | 28.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.23 | 0.09 | 0.0 | 38862.92 | 4.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
