# Hulk DIGEST — 2026-09-16T09:01:51Z

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
| XRPUSDT | IDLE | 0.8 | 2.76 | 2.08 | -0.08 | 95588474.02 | 1.56 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.23 | 0.36 | -0.03 | 489174695.52 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.97 | 0.46 | -0.02 | 602347280.27 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 2.0 | 3.54 | 3.03 | -0.04 | 665287.19 | 1.9 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 19.06 | 11.88 | 0.43 | 427692.3 | 11.37 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.88 | 1.4 | -0.04 | 374313.2 | 8.78 | skipped_fast |
| REDUSDT | IDLE | 2.26 | 4.47 | 4.07 | -0.06 | 68803.56 | 12.27 | skipped_fast |
| WUSDT | IDLE | 1.43 | 3.15 | 2.53 | -0.08 | 206191.58 | 13.49 | skipped_fast |
| RIZEUSDT | IDLE | 2.9 | 31.58 | 2.31 | 0.56 | 44377.29 | 300.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.11 | 3.79 | -0.11 | 117951.74 | 8.2 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.09 | 2.37 | -0.07 | 60556.46 | 13.01 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.45 | 1.95 | -0.03 | 80181.17 | 8.12 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 2.49 | 1.71 | -0.06 | 212686.8 | 25.96 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.22 | 0.86 | -0.04 | 464887.94 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.27 | 1.88 | -0.04 | 15003.91 | 28.99 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 2.94 | 2.41 | -0.06 | 45019.34 | 6.72 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 1.77 | 1.61 | -0.07 | 107956.7 | 40.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 1.98 | 1.94 | -0.06 | 1282.03 | 22.0 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.38 | 1.29 | -0.02 | 52226.42 | 22.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.48 | 0.14 | -0.02 | 29798.54 | 2.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
