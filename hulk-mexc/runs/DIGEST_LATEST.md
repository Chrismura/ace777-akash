# Hulk DIGEST — 2026-09-10T07:14:45Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 193.18 | 54.95 | -0.43 | 72533.76 | 709.49 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.03 | 0.7 | -0.04 | 41854224.76 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.97 | 0.37 | -0.01 | 359510413.62 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.73 | 0.42 | -0.01 | 531383694.4 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.07 | 2.9 | 1.2 | -0.04 | 1032255.67 | 1.9 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 2.12 | 0.19 | -0.03 | 625441.34 | 4.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.61 | 4.99 | 1.59 | 0.03 | 177275.3 | 20.34 | skipped_fast |
| EDELUSDT | IDLE | 1.81 | 6.99 | 2.06 | 0.07 | 245913.63 | 26.28 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.92 | 3.62 | -0.05 | 63435.77 | 18.69 | skipped_fast |
| WUSDT | IDLE | 1.19 | 2.22 | 1.95 | -0.05 | 217970.5 | 7.2 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 2.22 | 0.89 | -0.07 | 103148.68 | 3.92 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.3 | 0.73 | -0.04 | 422846.47 | 1.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.23 | 2.39 | 0.44 | 0.0 | 6087.19 | 5.61 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.59 | 1.41 | -0.02 | 56611.25 | 11.7 | skipped_fast |
| CHIPUSDT | IDLE | 0.41 | 2.42 | 1.19 | -0.12 | 124462.98 | 16.34 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.18 | 1.13 | -0.03 | 41518.76 | 5.96 | skipped_fast |
| TELUSDT | IDLE | 1.07 | 2.09 | 0.33 | 0.02 | 84636.89 | 44.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.91 | 0.49 | -0.06 | 1423.77 | 22.04 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.68 | 0.22 | -0.04 | 53943.45 | 14.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 1.0 | 0.39 | -0.02 | 26713.24 | 63.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
