# Hulk DIGEST — 2026-09-19T05:00:34Z

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
| XRPUSDT | IDLE | 1.22 | 2.45 | 0.85 | 0.07 | 69377828.58 | 2.12 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.09 | 0.85 | 0.04 | 742359390.09 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.12 | 0.49 | 0.06 | 627028983.7 | 0.04 | skipped_fast |
| WUSDT | IDLE | 1.22 | 3.75 | 2.98 | 0.07 | 962273.71 | 8.31 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 19.02 | 14.51 | 0.06 | 99000.08 | 8.97 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 3.89 | 2.21 | 0.0 | 698613.87 | 9.9 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 2.99 | 1.78 | 0.03 | 564766.0 | 6.27 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 7.81 | 4.33 | 0.06 | 148388.48 | 17.56 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.89 | 1.06 | 0.03 | 681854.97 | 1.27 | skipped_fast |
| EDELUSDT | IDLE | 1.8 | 8.37 | 2.73 | -0.04 | 174676.43 | 36.4 | skipped_fast |
| KITEUSDT | IDLE | 1.68 | 3.11 | 1.64 | 0.03 | 72234.13 | 13.31 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.47 | 0.75 | 0.01 | 210812.7 | 11.05 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.85 | 1.6 | 0.02 | 84347.31 | 11.07 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.21 | 1.19 | 0.05 | 6539.34 | 11.44 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 4.1 | 1.95 | -0.1 | 38727.65 | 115.12 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 3.3 | 3.01 | 0.1 | 126911.7 | 44.35 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.14 | 0.58 | 0.01 | 73442.13 | 7.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 3.4 | 0.0 | 0.18 | 5299.2 | 21.73 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.89 | 0.37 | -0.0 | 54953.68 | 22.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.01 | 0.01 | 0.01 | 0.04 | 40596.83 | 2.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
