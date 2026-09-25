# Hulk DIGEST — 2026-09-25T04:42:09Z

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
| XRPUSDT | IDLE | 1.32 | 2.45 | 1.33 | 0.03 | 73348213.08 | 1.95 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.97 | 0.71 | 0.0 | 733359029.37 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.02 | 0.53 | 0.0 | 358573853.17 | 0.37 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 3.1 | 0.85 | 0.06 | 1026187.53 | 4.36 | skipped_fast |
| RIZEUSDT | IDLE | 2.3 | 62.83 | 13.42 | 0.82 | 102393.46 | 323.4 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 2.48 | 1.36 | 0.03 | 924545.01 | 2.15 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.75 | 0.69 | 0.07 | 527556.94 | 9.45 | skipped_fast |
| KITEUSDT | IDLE | 2.97 | 5.3 | 4.28 | -0.03 | 64057.8 | 11.84 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.87 | 1.39 | 0.03 | 266901.19 | 8.51 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 4.29 | 0.16 | 0.09 | 109647.34 | 13.29 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 11.09 | 1.64 | 0.36 | 337975.27 | 12.39 | skipped_fast |
| EDELUSDT | IDLE | 0.57 | 6.2 | 4.08 | 0.07 | 194411.39 | 30.54 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.55 | 0.25 | 0.01 | 241415.37 | 22.36 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 4.81 | 2.6 | 0.1 | 106724.87 | 12.82 | skipped_fast |
| TELUSDT | IDLE | 2.25 | 4.86 | 3.31 | -0.06 | 110911.66 | 18.66 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 2.67 | 0.06 | 0.08 | 89889.2 | 9.65 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 3.2 | 0.05 | 0.19 | 13720.46 | 50.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.41 | 0.53 | 0.01 | 39823.29 | 15.5 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.59 | 0.22 | 0.01 | 59131.18 | 7.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.4 | 0.79 | 0.0 | 0.04 | 1081.64 | 21.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
