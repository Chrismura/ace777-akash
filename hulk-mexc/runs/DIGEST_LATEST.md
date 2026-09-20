# Hulk DIGEST — 2026-09-20T03:00:48Z

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
| XRPUSDT | IDLE | 2.08 | 3.66 | 3.4 | -0.03 | 57901334.5 | 3.65 | skipped_fast |
| ETHUSDT | IDLE | 1.57 | 2.77 | 2.41 | -0.02 | 227052044.25 | 2.68 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.36 | 1.27 | -0.01 | 441247840.9 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 6.69 | 5.89 | -0.05 | 745184.13 | 6.84 | skipped_fast |
| WUSDT | IDLE | 3.06 | 5.5 | 4.09 | -0.0 | 515808.37 | 11.9 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 5.42 | 5.0 | 0.0 | 657080.32 | 3.76 | skipped_fast |
| CCUSDT | IDLE | 2.59 | 5.19 | 4.45 | -0.07 | 328822.78 | 6.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 7.88 | 7.29 | 0.04 | 213240.13 | 29.7 | skipped_fast |
| BIOUSDT | IDLE | 2.78 | 4.9 | 4.35 | -0.02 | 89521.69 | 11.1 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 6.39 | 5.64 | -0.1 | 115140.45 | 16.76 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 6.25 | 5.89 | -0.11 | 108965.03 | 20.46 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.39 | 2.38 | 0.02 | 104845.82 | 14.14 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 2.87 | 2.5 | -0.01 | 80309.95 | 9.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 4.68 | 2.88 | 0.0 | 40564.37 | 87.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.63 | 1.37 | 1.18 | -0.04 | 7539.95 | 23.74 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 2.64 | 2.38 | 0.01 | 55786.86 | 9.3 | skipped_fast |
| TELUSDT | IDLE | 1.29 | 2.67 | 2.34 | -0.08 | 102991.24 | 47.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 1.88 | 1.75 | 0.01 | 7917.81 | 21.82 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.04 | 0.95 | 0.0 | 52622.74 | 36.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.4 | -0.01 | 34955.81 | 27.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
