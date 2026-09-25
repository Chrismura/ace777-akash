# Hulk DIGEST — 2026-09-25T02:24:37Z

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
| XRPUSDT | IDLE | 1.14 | 2.13 | 0.95 | 0.03 | 71438583.2 | 1.94 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.07 | 0.08 | 0.01 | 722548334.75 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.87 | 0.14 | 0.01 | 354235257.97 | 0.52 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 38.5 | 24.39 | 0.07 | 184616.31 | 57.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.08 | 3.94 | 0.46 | 0.1 | 1013234.99 | 5.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.92 | 34.66 | 17.2 | 0.45 | 93848.08 | 51.09 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 3.01 | 0.11 | 0.05 | 514328.13 | 6.94 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.78 | 0.54 | 0.04 | 888950.38 | 1.07 | skipped_fast |
| KITEUSDT | IDLE | 2.84 | 5.01 | 4.45 | -0.03 | 65952.47 | 10.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 8.35 | 7.05 | 0.1 | 103303.73 | 19.27 | skipped_fast |
| WUSDT | IDLE | 1.05 | 1.93 | 1.2 | 0.04 | 254207.78 | 5.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 2.01 | 0.53 | 0.02 | 223446.7 | 10.18 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 9.66 | 6.13 | 0.27 | 302756.63 | 13.45 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 2.95 | 0.18 | 0.09 | 110237.49 | 28.78 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 2.27 | 1.67 | 0.08 | 91135.65 | 13.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 5.68 | 4.98 | 0.16 | 13031.16 | 56.26 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 3.67 | 3.3 | -0.06 | 111301.75 | 61.96 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.26 | 0.22 | 0.01 | 59028.48 | 7.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.71 | 1.41 | 0.13 | 0.01 | 39596.04 | 16.75 | skipped_fast |
| FLUIDUSDT | IDLE | 0.59 | 1.13 | 0.27 | 0.04 | 1081.64 | 21.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
