# Hulk DIGEST — 2026-08-30T04:12:34Z

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
| XRPUSDT | IDLE | 0.42 | 0.76 | 0.49 | 0.01 | 16130213.97 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 3.9 | 1.3 | -0.01 | 823233.74 | 4.98 | skipped_fast |
| RIZEUSDT | IDLE | 3.03 | 12.31 | 4.75 | -0.05 | 44872.99 | 61.55 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.18 | 0.64 | 0.09 | 290700.55 | 6.64 | skipped_fast |
| PYTHUSDT | IDLE | 0.92 | 1.62 | 1.45 | 0.0 | 315538.43 | 2.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.24 | 2.31 | 1.15 | -0.03 | 194847.81 | 12.1 | skipped_fast |
| WUSDT | IDLE | 1.06 | 1.97 | 0.96 | 0.0 | 188683.02 | 10.91 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.3 | 0.02 | 0.02 | 76378.73 | 11.74 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.76 | 0.83 | -0.01 | 68688.47 | 7.26 | skipped_fast |
| KITEUSDT | IDLE | 0.65 | 1.71 | 1.15 | 0.01 | 68308.59 | 8.54 | skipped_fast |
| EDELUSDT | IDLE | 0.26 | 5.05 | 0.94 | 0.08 | 121025.89 | 43.42 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.75 | 0.86 | -0.0 | 146101.22 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 2.35 | 0.71 | -0.04 | 71099.48 | 23.71 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.57 | 1.14 | 0.0 | 54415.32 | 32.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.24 | 0.01 | 1482.06 | 23.1 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.09 | 0.42 | 0.01 | 31451.66 | 1.62 | skipped_fast |
| RWAINCUSDT | IDLE | 0.16 | 0.28 | 0.28 | -0.04 | 1577.44 | 101.75 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
