# Hulk DIGEST — 2026-10-12T13:30:47Z

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
| WUSDT | IDLE | 1.51 | 28.11 | 21.48 | 0.44 | 15905550.09 | 10.43 | skipped_fast |
| PYTHUSDT | IDLE | 2.23 | 10.07 | 4.94 | 0.13 | 2595155.39 | 4.63 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 2.14 | 2.1 | -0.01 | 26565136.14 | 1.45 | skipped_fast |
| BTCUSDT | IDLE | 1.04 | 1.81 | 1.76 | -0.01 | 268322693.42 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.99 | 1.74 | 1.57 | 0.01 | 273311533.82 | 0.55 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 21.02 | 17.19 | 0.06 | 188545.37 | 16.51 | skipped_fast |
| QNTUSDT | IDLE | 3.09 | 5.57 | 4.01 | -0.05 | 860470.47 | 6.03 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 11.51 | 5.53 | -0.04 | 23837.56 | 29.04 | skipped_fast |
| CHIPUSDT | IDLE | 2.1 | 6.9 | 6.06 | -0.08 | 186716.76 | 14.58 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 3.97 | 3.48 | -0.05 | 214681.55 | 21.81 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.16 | 1.99 | 0.0 | 384151.6 | 5.66 | skipped_fast |
| KITEUSDT | IDLE | 2.48 | 4.42 | 3.62 | 0.02 | 66109.68 | 8.59 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.02 | 2.8 | -0.0 | 465493.33 | 1.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.63 | 2.35 | 0.03 | 283517.3 | 34.12 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 2.69 | 2.62 | -0.03 | 98178.61 | 13.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.77 | 9.65 | 4.08 | 0.17 | 51997.65 | 76.57 | skipped_fast |
| TELUSDT | IDLE | 1.64 | 3.18 | 0.67 | 0.03 | 168412.79 | 11.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.31 | 2.93 | 0.0 | 24191.54 | 52.05 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.54 | 0.46 | 0.01 | 52040.87 | 23.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.11 | 0.0 | 40260.24 | 8.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
