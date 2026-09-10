# Hulk DIGEST — 2026-09-10T09:18:00Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.99 | 209.6 | 62.1 | -0.65 | 82068.07 | 125.21 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.17 | 0.72 | -0.03 | 41812286.44 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.44 | 0.82 | 0.39 | -0.01 | 339709005.63 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.79 | 0.49 | -0.02 | 510682748.17 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 2.82 | 2.26 | -0.05 | 1029146.9 | 1.92 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.13 | 2.03 | -0.04 | 644359.2 | 4.85 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 6.32 | 5.94 | -0.07 | 56945.76 | 33.91 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 5.35 | 2.07 | 0.1 | 243043.43 | 43.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.05 | 2.35 | -0.01 | 172152.33 | 25.78 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.66 | 2.32 | -0.06 | 224859.99 | 13.46 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 3.96 | 3.1 | -0.08 | 65066.6 | 17.84 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.35 | 1.36 | -0.07 | 101804.46 | 3.94 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.44 | 1.2 | -0.04 | 380998.37 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 0.48 | 2.71 | 2.44 | -0.16 | 112246.06 | 14.48 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.1 | 0.56 | -0.0 | 5575.55 | 44.62 | skipped_fast |
| QNTUSDT | IDLE | 1.01 | 1.81 | 1.45 | -0.03 | 39259.65 | 1.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.91 | 1.15 | -0.07 | 1427.85 | 17.89 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 1.34 | 0.28 | 0.01 | 84866.66 | 33.24 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.36 | -0.02 | 25677.92 | 4.14 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.3 | -0.03 | 53925.08 | 14.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
