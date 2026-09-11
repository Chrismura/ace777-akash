# Hulk DIGEST — 2026-09-11T18:20:53Z

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
| ETHUSDT | IDLE | 3.23 | 7.02 | 4.44 | 0.04 | 630912848.01 | 1.22 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 6.32 | 5.15 | 0.01 | 52887713.06 | 2.94 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 110.08 | 11.25 | 0.98 | 187965.1 | 112.99 | skipped_fast |
| BTCUSDT | IDLE | 2.14 | 3.79 | 3.24 | 0.0 | 551644125.34 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.07 | 5.7 | 4.6 | 0.01 | 399511.6 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 2.84 | 5.15 | 3.56 | 0.0 | 461924.18 | 4.06 | skipped_fast |
| RWAINCUSDT | IDLE | 4.16 | 8.51 | 4.0 | 0.04 | 11185.18 | 5.41 | skipped_fast |
| CHIPUSDT | IDLE | 3.29 | 10.12 | 4.2 | 0.02 | 149519.62 | 18.76 | skipped_fast |
| EDELUSDT | IDLE | 3.67 | 6.74 | 4.0 | -0.02 | 155646.45 | 36.97 | skipped_fast |
| WUSDT | IDLE | 2.84 | 5.63 | 2.58 | 0.02 | 193475.06 | 6.15 | skipped_fast |
| REDUSDT | IDLE | 3.1 | 6.07 | 0.89 | 0.06 | 60630.86 | 17.34 | skipped_fast |
| ZBCNUSDT | IDLE | 2.1 | 3.73 | 3.11 | -0.0 | 189177.08 | 26.62 | skipped_fast |
| BIOUSDT | IDLE | 2.33 | 4.18 | 3.24 | 0.0 | 82303.92 | 7.96 | skipped_fast |
| TELUSDT | IDLE | 3.46 | 6.91 | 4.63 | -0.01 | 96273.75 | 62.16 | skipped_fast |
| HBARUSDT | IDLE | 2.37 | 4.19 | 3.66 | -0.01 | 229718.68 | 2.69 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 3.06 | 2.15 | -0.02 | 59765.21 | 13.81 | skipped_fast |
| FLUIDUSDT | IDLE | 2.57 | 4.94 | 1.3 | 0.01 | 1302.75 | 21.68 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 2.97 | 2.79 | -0.02 | 40162.34 | 6.24 | skipped_fast |
| RWAUSDT | IDLE | 1.46 | 2.81 | 0.67 | 0.02 | 51699.81 | 22.35 | skipped_fast |
| MNSRYUSDT | IDLE | 1.29 | 2.27 | 2.03 | 0.0 | 37039.43 | 48.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
