# Hulk DIGEST — 2026-09-17T02:15:22Z

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
| XRPUSDT | IDLE | 1.26 | 2.36 | 1.04 | 0.01 | 56764423.24 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 1.25 | 2.35 | 0.96 | 0.01 | 380473926.69 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.49 | 0.73 | 0.01 | 516998826.95 | 0.21 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 7.95 | 6.17 | 0.06 | 553822.5 | 8.28 | skipped_fast |
| PYTHUSDT | IDLE | 2.57 | 4.91 | 1.55 | 0.01 | 421104.45 | 5.61 | skipped_fast |
| RWAINCUSDT | IDLE | 4.18 | 7.81 | 3.65 | -0.03 | 21137.2 | 5.83 | skipped_fast |
| WUSDT | IDLE | 2.8 | 5.27 | 2.44 | 0.01 | 227329.82 | 9.86 | skipped_fast |
| CHIPUSDT | IDLE | 3.06 | 7.1 | 2.08 | -0.01 | 81978.26 | 13.59 | skipped_fast |
| REDUSDT | IDLE | 2.2 | 4.49 | 1.75 | -0.01 | 65391.0 | 9.16 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 6.57 | 2.0 | 0.06 | 67018.32 | 10.37 | skipped_fast |
| BIOUSDT | IDLE | 1.94 | 3.74 | 0.9 | 0.03 | 78243.36 | 15.82 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 3.78 | 2.75 | 0.05 | 264897.45 | 38.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.48 | 0.47 | 0.04 | 166290.9 | 19.43 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.27 | 0.78 | -0.0 | 307599.96 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.73 | 10.2 | 5.03 | 0.25 | 62444.65 | 82.73 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.88 | 1.03 | -0.02 | 115655.77 | 41.55 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.32 | 0.93 | 0.0 | 37713.43 | 6.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.47 | 0.94 | 0.03 | -0.0 | 33148.18 | 2.82 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.83 | 0.15 | 0.02 | 55095.16 | 22.4 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1573.23 | 22.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
