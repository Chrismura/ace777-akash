# Hulk DIGEST — 2026-09-26T08:29:41Z

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
| XRPUSDT | IDLE | 0.72 | 1.29 | 1.02 | 0.0 | 109345942.51 | 1.94 | skipped_fast |
| ETHUSDT | IDLE | 0.16 | 0.31 | 0.08 | -0.0 | 277518054.09 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.3 | 0.04 | -0.0 | 582798840.3 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.73 | 3.39 | 0.43 | 0.07 | 1171648.37 | 2.68 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 7.25 | 1.24 | 0.16 | 1046640.89 | 8.7 | skipped_fast |
| WUSDT | IDLE | 1.89 | 3.81 | 0.04 | 0.07 | 473871.83 | 7.12 | skipped_fast |
| QNTUSDT | IDLE | 2.07 | 7.15 | 0.62 | 0.04 | 612874.24 | 33.41 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.42 | 0.55 | 0.01 | 854754.74 | 1.06 | skipped_fast |
| KITEUSDT | IDLE | 2.05 | 4.32 | 4.05 | 0.05 | 78373.74 | 9.69 | skipped_fast |
| RWAINCUSDT | IDLE | 2.31 | 4.42 | 1.27 | -0.03 | 9394.73 | 9.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.82 | 0.71 | 0.04 | 246192.09 | 12.65 | skipped_fast |
| EDELUSDT | IDLE | 1.61 | 3.04 | 1.19 | 0.01 | 177340.13 | 23.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 2.89 | 0.91 | 0.04 | 146758.28 | 16.3 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 1.3 | 0.89 | 0.04 | 123176.23 | 3.08 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.53 | 1.04 | 0.03 | 58971.69 | 14.07 | skipped_fast |
| RIZEUSDT | IDLE | 0.26 | 3.43 | 1.09 | -0.19 | 68107.27 | 25.59 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.61 | 1.1 | -0.01 | 118764.48 | 30.84 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.01 | 3431.02 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.04 | 0.29 | -0.01 | 52906.69 | 7.37 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.11 | 0.01 | 40720.77 | 10.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
