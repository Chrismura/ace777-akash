# Hulk DIGEST — 2026-09-17T04:15:25Z

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
| ETHUSDT | IDLE | 1.19 | 2.3 | 0.54 | 0.01 | 382821838.59 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 1.96 | 0.88 | -0.0 | 56153410.35 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.49 | 0.57 | 0.01 | 514913596.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.0 | 5.71 | 1.9 | 0.0 | 483805.39 | 1.87 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 7.04 | 5.58 | 0.06 | 576159.3 | 7.21 | skipped_fast |
| CHIPUSDT | IDLE | 3.06 | 7.0 | 2.71 | -0.03 | 81773.19 | 10.94 | skipped_fast |
| WUSDT | IDLE | 2.29 | 4.37 | 1.55 | 0.02 | 226800.51 | 7.6 | skipped_fast |
| RWAINCUSDT | IDLE | 2.88 | 5.29 | 3.11 | -0.02 | 20468.39 | 5.83 | skipped_fast |
| ZBCNUSDT | IDLE | 2.26 | 4.35 | 1.09 | 0.03 | 169029.83 | 19.45 | skipped_fast |
| REDUSDT | IDLE | 2.12 | 3.88 | 2.36 | -0.01 | 62014.4 | 16.91 | skipped_fast |
| EDELUSDT | IDLE | 0.94 | 3.98 | 3.31 | 0.01 | 258155.62 | 15.41 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.24 | 1.37 | 0.0 | 78137.08 | 11.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.27 | 10.98 | 9.2 | -0.01 | 61524.76 | 96.22 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 3.59 | 1.2 | 0.07 | 66764.27 | 11.24 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 2.44 | 0.51 | -0.01 | 313798.32 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.88 | 1.16 | -0.03 | 115723.02 | 27.72 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.57 | 1.52 | -0.0 | 38194.8 | 3.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.45 | 0.24 | 0.01 | 34432.45 | 35.16 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 0.98 | 0.67 | 0.01 | 55583.87 | 30.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1573.23 | 21.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
