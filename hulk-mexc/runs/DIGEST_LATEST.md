# Hulk DIGEST — 2026-10-15T22:18:59Z

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
| WUSDT | IDLE | 1.31 | 3.68 | 2.24 | -0.04 | 2893489.96 | 12.26 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 5.32 | 1.94 | 0.11 | 4450771.75 | 5.27 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.59 | 0.23 | 0.01 | 502231846.91 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.47 | 0.23 | 0.02 | 313147936.61 | 0.24 | skipped_fast |
| XRPUSDT | IDLE | 0.51 | 0.95 | 0.5 | 0.01 | 47939461.96 | 2.24 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 3.97 | 3.59 | 0.01 | 1356621.33 | 2.91 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.77 | 10.86 | 7.5 | -0.12 | 237484.23 | 74.63 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.98 | 1.84 | -0.07 | 460903.99 | 7.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.22 | 2.84 | 0.01 | 216992.83 | 30.22 | skipped_fast |
| RIZEUSDT | IDLE | 2.04 | 8.01 | 2.58 | 0.03 | 82601.81 | 47.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.81 | 2.56 | 0.02 | 28807.88 | 4.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.82 | 4.2 | 0.54 | -0.09 | 153304.59 | 12.63 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 2.2 | 1.71 | -0.03 | 69041.32 | 10.49 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 2.88 | 0.58 | 0.01 | 300309.55 | 7.06 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 2.5 | 2.4 | -0.0 | 72805.63 | 12.16 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 1.33 | 0.42 | -0.02 | 84463.23 | 11.59 | skipped_fast |
| RWAUSDT | IDLE | 0.96 | 1.76 | 1.1 | 0.01 | 55141.29 | 15.86 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 1.94 | 0.45 | 0.01 | 91426.13 | 39.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 2.38 | 0.85 | -0.04 | 8879.41 | 21.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.13 | -0.0 | 34546.81 | 8.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
