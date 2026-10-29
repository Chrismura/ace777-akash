# Hulk DIGEST — 2026-10-29T10:19:12Z

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
| XRPUSDT | IDLE | 0.74 | 1.31 | 1.2 | -0.03 | 23967712.18 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.27 | 0.7 | -0.02 | 234485359.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.86 | 0.5 | -0.02 | 342547189.62 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 2.97 | 2.38 | -0.04 | 446820.27 | 4.3 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.52 | 1.36 | -0.03 | 492850.49 | 77.15 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.41 | 0.6 | -0.07 | 406039.63 | 7.25 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.45 | 2.1 | -0.04 | 195245.55 | 9.64 | skipped_fast |
| LAUSDT | IDLE | 3.18 | 5.7 | 4.4 | -0.04 | 57822.94 | 19.35 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.61 | 1.84 | -0.05 | 426139.32 | 3.64 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.54 | 0.85 | -0.04 | 567039.05 | 4.06 | skipped_fast |
| CHIPUSDT | IDLE | 0.69 | 3.55 | 1.9 | -0.12 | 242898.1 | 14.73 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.85 | 2.21 | -0.04 | 64105.13 | 15.68 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.85 | 1.21 | -0.04 | 68131.81 | 9.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.43 | 0.8 | -0.01 | 253745.56 | 30.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 4.82 | 2.72 | -0.09 | 31563.35 | 7.16 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.51 | 1.17 | -0.04 | 60001.26 | 14.3 | skipped_fast |
| FLUIDUSDT | IDLE | 2.33 | 4.39 | 3.46 | -0.06 | 6151.7 | 21.19 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 1.83 | 0.42 | -0.03 | 39419.27 | 49.3 | skipped_fast |
| WAXLUSDT | IDLE | 1.74 | 4.01 | 2.69 | -0.07 | 54142.67 | 54.64 | skipped_fast |
| IOTAUSDT | IDLE | 1.14 | 2.11 | 1.55 | -0.06 | 98967.95 | 17.52 | skipped_fast |
| RWAUSDT | IDLE | 1.11 | 2.01 | 1.34 | -0.0 | 56510.02 | 40.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.03 | -0.01 | 37394.69 | 16.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
