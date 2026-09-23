# Hulk DIGEST — 2026-09-23T08:18:13Z

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
| XRPUSDT | IDLE | 2.14 | 4.47 | 2.63 | 0.06 | 118963211.02 | 1.24 | skipped_fast |
| PYTHUSDT | IDLE | 0.69 | 3.18 | 1.88 | 0.05 | 1796208.16 | 1.5 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 4.3 | 2.93 | 0.03 | 1782554.47 | 2.04 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.93 | 1.48 | 0.01 | 412786641.46 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.46 | 1.16 | 0.01 | 871987576.58 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 4.03 | 3.19 | -0.06 | 404555.0 | 9.74 | skipped_fast |
| CHIPUSDT | IDLE | 2.97 | 5.37 | 3.76 | -0.05 | 204329.42 | 13.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.32 | 5.53 | 3.36 | 0.04 | 219710.83 | 16.96 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.62 | 1.2 | 0.04 | 316749.56 | 10.55 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 4.78 | 3.41 | 0.07 | 142453.58 | 9.58 | skipped_fast |
| BIOUSDT | IDLE | 1.58 | 2.92 | 1.63 | 0.05 | 112724.09 | 9.95 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.1 | 1.84 | -0.05 | 260568.33 | 19.75 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 12.5 | 3.88 | 0.48 | 63803.95 | 64.91 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 2.07 | 0.07 | 0.02 | 59728.7 | 15.41 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 2.57 | 1.04 | 0.11 | 241882.62 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 4.92 | 4.26 | 0.12 | 118091.71 | 38.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 1.68 | 0.69 | 0.04 | 20999.46 | 64.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 1.78 | 1.75 | 0.01 | 2938.19 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.65 | 0.01 | 53469.67 | 7.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.55 | 0.51 | 0.01 | 39838.41 | 26.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
