# Hulk DIGEST — 2026-09-02T19:56:41Z

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
| XRPUSDT | IDLE | 0.91 | 1.76 | 0.39 | -0.01 | 36536673.04 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.58 | 0.96 | -0.01 | 363499525.82 | 0.21 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.06 | 0.48 | -0.0 | 508257332.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.74 | 7.5 | 2.49 | 0.14 | 1320000.27 | 1.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 6.15 | 0.19 | -0.04 | 1054215.54 | 2.35 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 16.69 | 5.19 | 0.02 | 40604.74 | 72.93 | skipped_fast |
| WUSDT | IDLE | 2.3 | 4.59 | 0.13 | -0.0 | 338213.6 | 14.36 | skipped_fast |
| ZBCNUSDT | IDLE | 3.03 | 8.19 | 3.09 | -0.05 | 181671.82 | 53.94 | skipped_fast |
| KITEUSDT | IDLE | 2.0 | 9.23 | 6.52 | 0.12 | 131324.99 | 9.46 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 2.52 | 1.88 | -0.04 | 382358.22 | 5.47 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.39 | 1.36 | -0.01 | 68174.57 | 3.94 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 1.97 | 1.06 | 0.01 | 119161.3 | 11.31 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 4.33 | 3.17 | 0.08 | 167080.06 | 42.07 | skipped_fast |
| QNTUSDT | IDLE | 1.74 | 3.14 | 2.24 | 0.01 | 60766.68 | 4.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 4.48 | 0.91 | 0.05 | 9870.83 | 119.7 | skipped_fast |
| FLUIDUSDT | IDLE | 1.85 | 3.5 | 1.38 | -0.01 | 2397.59 | 21.61 | skipped_fast |
| TELUSDT | IDLE | 1.67 | 3.03 | 2.08 | 0.02 | 75508.48 | 58.93 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.44 | 0.43 | -0.01 | 186391.38 | 4.06 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.23 | 1.28 | 0.01 | 51738.36 | 7.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.12 | -0.0 | 28234.32 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
