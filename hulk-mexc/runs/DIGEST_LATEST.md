# Hulk DIGEST — 2026-10-12T12:30:19Z

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
| WUSDT | IDLE | 1.37 | 25.87 | 18.9 | 0.49 | 15500745.22 | 15.51 | skipped_fast |
| PYTHUSDT | IDLE | 2.92 | 13.74 | 2.69 | 0.15 | 2286371.3 | 3.4 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.61 | 1.53 | 0.01 | 265035644.9 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.92 | 1.63 | 1.46 | 0.0 | 24831774.15 | 2.15 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.45 | 1.38 | 0.0 | 250477191.03 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 21.03 | 13.6 | 0.11 | 182315.08 | 13.37 | skipped_fast |
| QNTUSDT | IDLE | 2.9 | 5.08 | 4.83 | -0.05 | 852276.46 | 1.74 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.0 | 11.51 | 6.39 | 0.03 | 30582.43 | 43.7 | skipped_fast |
| EDELUSDT | IDLE | 2.23 | 3.97 | 3.29 | -0.05 | 222858.5 | 19.05 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.43 | 1.44 | 0.03 | 418015.37 | 8.81 | skipped_fast |
| KITEUSDT | IDLE | 2.43 | 4.44 | 2.82 | 0.03 | 64174.23 | 3.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.44 | 4.33 | 3.06 | -0.04 | 185226.14 | 15.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.25 | 0.96 | 0.05 | 280687.62 | 16.63 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.34 | 1.98 | 0.01 | 454719.43 | 3.24 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.51 | 1.98 | -0.01 | 101566.08 | 13.68 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 3.54 | 1.06 | 0.04 | 174430.17 | 11.32 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 6.62 | 3.66 | 0.14 | 48496.06 | 78.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.22 | 2.14 | 2.03 | 0.01 | 22012.72 | 19.38 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.31 | 0.03 | 51858.32 | 7.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.11 | 0.0 | 39529.77 | 5.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
