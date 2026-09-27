# Hulk DIGEST — 2026-09-27T14:09:39Z

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
| WUSDT | IDLE | 2.08 | 12.35 | 9.58 | 0.14 | 3587777.39 | 15.31 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 6.03 | 4.77 | 0.08 | 2105520.93 | 2.38 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 15.85 | 9.65 | 0.54 | 5781626.06 | 9.15 | skipped_fast |
| XRPUSDT | IDLE | 0.89 | 1.64 | 0.98 | -0.01 | 42193666.23 | 3.27 | skipped_fast |
| ETHUSDT | IDLE | 0.41 | 0.77 | 0.39 | 0.01 | 170326902.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.67 | 0.17 | 0.01 | 440836572.35 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.55 | 2.93 | -0.03 | 533481.86 | 9.65 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 2.98 | 1.61 | 0.01 | 687163.9 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.84 | 4.75 | -0.08 | 142074.69 | 27.98 | skipped_fast |
| CHIPUSDT | IDLE | 2.34 | 5.73 | 3.83 | -0.01 | 121726.67 | 12.52 | skipped_fast |
| REDUSDT | IDLE | 1.96 | 3.51 | 2.75 | 0.0 | 64603.88 | 6.5 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.86 | 3.2 | 0.09 | 176230.24 | 8.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 1.9 | 1.21 | -0.01 | 226229.68 | 11.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.78 | 10.17 | 3.0 | 0.21 | 6030.77 | 57.33 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.61 | 1.61 | -0.02 | 98213.25 | 6.3 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 5.45 | 0.0 | 0.16 | 136570.43 | 43.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.3 | 1.11 | 0.59 | -0.04 | 46009.95 | 51.53 | skipped_fast |
| FLUIDUSDT | IDLE | 1.0 | 1.9 | 0.72 | 0.02 | 1384.47 | 22.17 | skipped_fast |
| RWAUSDT | IDLE | 0.94 | 1.71 | 1.12 | 0.01 | 55776.22 | 70.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.71 | 0.3 | 0.01 | 39771.05 | 5.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
