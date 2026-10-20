# Hulk DIGEST — 2026-10-20T22:25:49Z

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
| ETHUSDT | IDLE | 0.81 | 1.6 | 0.09 | 0.02 | 170060189.54 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.63 | 0.03 | 0.02 | 24349617.64 | 1.49 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.91 | 0.06 | 0.01 | 326239002.36 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 7.56 | 1.11 | 0.08 | 1185359.4 | 1.25 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.99 | 0.35 | 0.02 | 670790.96 | 14.74 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 9.94 | 8.01 | -0.04 | 75887.68 | 5.33 | skipped_fast |
| QNTUSDT | IDLE | 1.78 | 3.39 | 1.08 | 0.0 | 803441.46 | 1.53 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 5.69 | 3.04 | 0.06 | 403451.18 | 13.34 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 3.67 | 2.55 | 0.02 | 201060.57 | 10.85 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.86 | 1.28 | 0.01 | 384478.84 | 9.49 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 8.84 | 5.79 | 0.04 | 75266.58 | 62.03 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 4.76 | 2.11 | 0.34 | 362442.43 | 16.73 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 2.68 | 1.41 | 0.02 | 58795.32 | 17.1 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.34 | 0.96 | 0.05 | 62864.0 | 12.13 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.83 | 0.21 | 0.01 | 365451.22 | 9.49 | skipped_fast |
| KITEUSDT | IDLE | 0.54 | 0.98 | 0.7 | -0.01 | 72426.36 | 12.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.98 | 0.0 | 0.09 | 7267.9 | 21.2 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 3.1 | 2.66 | -0.04 | 56145.65 | 50.75 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 2.56 | 0.26 | 0.03 | 54979.76 | 20.24 | skipped_fast |
| IOTAUSDT | IDLE | 1.09 | 2.06 | 0.79 | 0.03 | 73006.48 | 27.82 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.31 | 0.0 | 52186.68 | 23.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.59 | 0.41 | 0.0 | 39127.67 | 1.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
