# Hulk DIGEST — 2026-10-19T14:53:55Z

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
| ETHUSDT | IDLE | 1.37 | 2.52 | 1.51 | 0.01 | 159587342.43 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.86 | 0.93 | 0.02 | 31095609.8 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.58 | 0.99 | 0.01 | 339057532.95 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.71 | 5.06 | 2.37 | -0.01 | 964272.36 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.94 | 5.54 | 3.77 | 0.04 | 870321.73 | 10.15 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.91 | 0.85 | 0.0 | 496940.26 | 17.7 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 4.43 | 2.13 | 0.05 | 365158.08 | 6.73 | skipped_fast |
| HBARUSDT | IDLE | 1.65 | 3.05 | 2.39 | -0.05 | 598249.25 | 1.21 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 6.71 | 1.9 | 0.06 | 91150.95 | 5.09 | skipped_fast |
| EDELUSDT | IDLE | 1.61 | 3.31 | 1.75 | 0.02 | 233626.69 | 3.71 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 5.36 | 4.06 | -0.0 | 83894.28 | 14.68 | skipped_fast |
| RIZEUSDT | IDLE | 2.43 | 5.45 | 3.74 | -0.05 | 54162.13 | 59.62 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 4.59 | 0.63 | 0.07 | 59279.08 | 9.12 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 2.44 | 1.77 | 0.02 | 265208.85 | 14.18 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 2.67 | 1.43 | 0.01 | 70669.79 | 8.51 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.24 | 0.57 | 0.01 | 71942.83 | 16.78 | skipped_fast |
| LAUSDT | IDLE | 1.8 | 3.27 | 2.18 | 0.01 | 59069.85 | 20.97 | skipped_fast |
| IOTAUSDT | IDLE | 1.53 | 2.91 | 0.99 | 0.01 | 75793.09 | 22.3 | skipped_fast |
| WAXLUSDT | IDLE | 1.04 | 3.81 | 3.09 | 0.06 | 78252.96 | 33.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 3.43 | 2.07 | 0.03 | 5240.03 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.27 | 0.63 | 0.01 | 55054.3 | 15.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.28 | -0.0 | 40542.56 | 25.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
