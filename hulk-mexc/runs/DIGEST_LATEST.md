# Hulk DIGEST — 2026-09-27T23:12:40Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 105.87 | 19.2 | 1.04 | 12918528.04 | 34.78 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 4.8 | 3.99 | 0.03 | 2310856.19 | 3.61 | skipped_fast |
| WUSDT | IDLE | 1.37 | 7.72 | 4.29 | 0.19 | 5065727.09 | 14.18 | skipped_fast |
| XRPUSDT | IDLE | 1.41 | 2.51 | 2.03 | -0.01 | 42126542.18 | 1.99 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.1 | 0.87 | -0.01 | 208088797.41 | 0.64 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.83 | 0.77 | -0.0 | 429571629.11 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 2.98 | 2.82 | -0.01 | 632858.37 | 11.1 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 24.16 | 18.24 | -0.24 | 53936.36 | 66.15 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 5.08 | 4.4 | -0.03 | 216663.53 | 25.91 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 8.26 | 7.63 | -0.15 | 141374.5 | 3.93 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 2.03 | 1.13 | 0.01 | 782268.64 | 1.06 | skipped_fast |
| CHIPUSDT | IDLE | 2.0 | 3.74 | 3.4 | -0.06 | 99209.23 | 17.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.98 | 20.76 | 0.69 | 0.26 | 28941.8 | 116.37 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 2.87 | 2.19 | 0.01 | 65318.2 | 14.1 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 2.05 | 0.26 | 0.0 | 118884.88 | 10.43 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.88 | 1.16 | -0.01 | 81750.49 | 6.33 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 2.96 | 0.53 | 0.14 | 178178.81 | 59.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 2.07 | 1.35 | 0.03 | 2838.49 | 20.28 | skipped_fast |
| RWAUSDT | IDLE | 0.08 | 0.14 | 0.14 | 0.01 | 58844.56 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.41 | 0.13 | 0.01 | 39937.69 | 34.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
