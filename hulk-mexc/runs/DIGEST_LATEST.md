# Hulk DIGEST — 2026-09-13T20:40:28Z

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
| ETHUSDT | IDLE | 0.67 | 1.3 | 0.24 | -0.01 | 254656304.92 | 0.16 | skipped_fast |
| XRPUSDT | IDLE | 0.63 | 1.25 | 0.1 | -0.0 | 14835998.53 | 2.21 | skipped_fast |
| BTCUSDT | IDLE | 0.25 | 0.48 | 0.13 | 0.0 | 261352671.41 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.27 | 32.72 | 21.19 | -0.12 | 67820.61 | 82.14 | skipped_fast |
| PYTHUSDT | IDLE | 2.56 | 4.98 | 0.96 | 0.03 | 424931.1 | 1.76 | skipped_fast |
| RWAINCUSDT | IDLE | 4.19 | 7.78 | 3.95 | 0.02 | 10051.26 | 5.49 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 7.77 | 3.02 | 0.11 | 200298.57 | 22.7 | skipped_fast |
| WUSDT | IDLE | 1.71 | 3.09 | 2.14 | -0.0 | 223124.55 | 12.91 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.55 | 0.02 | -0.01 | 297773.5 | 6.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.1 | 2.18 | 0.2 | 0.02 | 198656.53 | 4.99 | skipped_fast |
| CHIPUSDT | IDLE | 0.97 | 2.65 | 2.19 | -0.1 | 82714.55 | 13.87 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.18 | 1.11 | 0.01 | 63432.36 | 16.75 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.7 | 0.7 | 0.0 | 68706.48 | 7.82 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.54 | 0.82 | 0.01 | 61156.21 | 14.89 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.54 | 0.4 | 0.02 | 198216.35 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.61 | 1.77 | 0.0 | 36228.26 | 1.55 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.65 | 1.12 | -0.04 | 80602.72 | 44.12 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.9 | 0.15 | 0.0 | 53926.31 | 14.81 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 0.89 | 0.88 | -0.01 | 1495.4 | 23.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.46 | 0.39 | -0.0 | 31001.33 | 36.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
