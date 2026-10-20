# Hulk DIGEST — 2026-10-20T18:02:29Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.07 | 3.93 | 1.34 | 0.02 | 23511460.74 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 2.04 | 3.91 | 1.17 | 0.02 | 149731672.97 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.33 | 2.55 | 0.78 | 0.01 | 325477279.26 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.3 | 7.6 | 1.87 | 0.06 | 1006511.87 | 3.89 | skipped_fast |
| WUSDT | IDLE | 3.21 | 6.16 | 1.79 | 0.02 | 717014.05 | 15.83 | skipped_fast |
| QNTUSDT | IDLE | 3.25 | 6.0 | 3.29 | 0.0 | 719192.73 | 1.02 | skipped_fast |
| ZBCNUSDT | IDLE | 4.0 | 7.65 | 2.38 | 0.03 | 190290.56 | 15.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.76 | 9.87 | 4.01 | 0.09 | 161868.25 | 10.98 | skipped_fast |
| EDELUSDT | IDLE | 1.63 | 15.52 | 2.52 | 0.32 | 335338.41 | 22.43 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 3.41 | 0.89 | 0.02 | 410311.45 | 7.55 | skipped_fast |
| BIOUSDT | IDLE | 2.91 | 5.72 | 0.72 | 0.07 | 64267.61 | 8.08 | skipped_fast |
| REDUSDT | IDLE | 2.91 | 5.63 | 1.23 | 0.04 | 59270.35 | 15.66 | skipped_fast |
| HBARUSDT | IDLE | 2.52 | 4.66 | 2.55 | 0.02 | 399306.3 | 7.2 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 3.46 | 1.61 | 0.01 | 85705.71 | 10.63 | skipped_fast |
| IOTAUSDT | IDLE | 3.1 | 5.95 | 2.5 | 0.06 | 92506.47 | 21.34 | skipped_fast |
| LAUSDT | IDLE | 3.09 | 6.0 | 1.15 | 0.04 | 56181.13 | 22.25 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 4.0 | 3.74 | -0.05 | 73716.57 | 16.18 | skipped_fast |
| WAXLUSDT | IDLE | 2.97 | 5.42 | 3.44 | -0.04 | 55701.13 | 33.41 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 4.33 | 1.84 | 0.02 | 69665.29 | 60.97 | skipped_fast |
| FLUIDUSDT | IDLE | 2.12 | 4.1 | 1.0 | 0.05 | 4946.21 | 21.01 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.42 | 0.93 | 0.01 | 52095.48 | 15.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.82 | 1.52 | 0.86 | -0.0 | 40130.6 | 19.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
