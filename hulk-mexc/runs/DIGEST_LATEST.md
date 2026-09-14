# Hulk DIGEST — 2026-09-14T02:41:16Z

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
| XRPUSDT | IDLE | 1.27 | 2.46 | 0.49 | -0.0 | 21076798.77 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 2.06 | 0.58 | -0.01 | 297393836.7 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.68 | 0.26 | 0.0 | 318075432.84 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.2 | 4.62 | 0.71 | 0.05 | 461428.63 | 1.74 | skipped_fast |
| REDUSDT | IDLE | 3.73 | 7.46 | 0.0 | 0.05 | 88273.47 | 10.88 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 42.83 | 29.99 | 0.26 | 68483.22 | 1145.15 | skipped_fast |
| WUSDT | IDLE | 2.17 | 4.21 | 0.86 | -0.01 | 194125.47 | 3.98 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 3.0 | 0.4 | -0.01 | 323300.05 | 6.2 | skipped_fast |
| EDELUSDT | IDLE | 1.8 | 6.04 | 2.63 | 0.09 | 214391.36 | 29.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 3.08 | 0.26 | 0.02 | 202652.51 | 22.26 | skipped_fast |
| BIOUSDT | IDLE | 1.91 | 3.72 | 0.62 | 0.0 | 68400.35 | 7.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 6.15 | 2.23 | -0.11 | 96949.51 | 21.2 | skipped_fast |
| HBARUSDT | IDLE | 1.95 | 3.62 | 1.87 | 0.01 | 266506.5 | 1.32 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 3.24 | 0.37 | 0.01 | 59301.28 | 12.04 | skipped_fast |
| QNTUSDT | IDLE | 1.92 | 3.53 | 2.01 | -0.02 | 41224.94 | 9.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.35 | 0.61 | 0.6 | -0.03 | 9145.19 | 5.49 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | 0.01 | 1513.53 | 21.9 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.12 | 0.69 | -0.04 | 82721.58 | 31.7 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.67 | 0.37 | -0.0 | 52993.44 | 7.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.46 | 0.39 | -0.0 | 30182.84 | 12.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
