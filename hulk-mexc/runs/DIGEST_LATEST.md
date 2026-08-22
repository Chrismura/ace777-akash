# Hulk DIGEST — 2026-08-22T11:56:39Z

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
| PYTHUSDT | IDLE | 2.17 | 9.66 | 7.05 | 0.0 | 51609802.42 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.58 | 0.09 | 216190598.49 | 1.35 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.75 | 0.13 | 780196.3 | 8.57 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.33 | 0.02 | 1257989.05 | 6.46 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.75 | 0.01 | 580784.13 | 13.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 5.93 | 4.54 | -0.03 | 382678.58 | 13.95 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.32 | -0.1 | 617965.83 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.61 | 6.24 | 0.58 | 0.04 | 81727.74 | 8.83 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.04 | 79333.71 | 34.11 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 6.64 | 2.58 | -0.04 | 241403.95 | 3.23 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.36 | -0.03 | 167468.44 | 32.03 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | 0.0 | 2446.18 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.6 | 0.03 | 154707.97 | 9.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.64 | -0.0 | 188344.54 | 9.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.84 | -0.03 | 48636.84 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.28 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57797.56 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
