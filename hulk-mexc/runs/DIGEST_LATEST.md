# Hulk DIGEST — 2026-09-01T18:26:02Z

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
| XRPUSDT | IDLE | 1.33 | 2.32 | 2.25 | -0.02 | 31349779.9 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.01 | 1.67 | -0.02 | 300861708.6 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.98 | 1.72 | 1.65 | -0.02 | 520249627.88 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 11.76 | 5.2 | 0.1 | 512950.23 | 4.73 | skipped_fast |
| PYTHUSDT | IDLE | 1.83 | 3.29 | 2.52 | 0.03 | 652088.65 | 2.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.51 | 6.34 | 4.52 | 0.02 | 211665.23 | 3.77 | skipped_fast |
| WUSDT | IDLE | 2.43 | 4.64 | 1.41 | 0.06 | 301129.5 | 7.25 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 4.19 | 2.79 | -0.02 | 424403.68 | 5.23 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 7.18 | 5.23 | -0.08 | 44859.03 | 51.61 | skipped_fast |
| REDUSDT | IDLE | 2.32 | 5.3 | 0.68 | 0.07 | 75274.45 | 11.49 | skipped_fast |
| KITEUSDT | IDLE | 2.14 | 3.97 | 2.03 | 0.03 | 69453.23 | 10.7 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.86 | 2.28 | -0.03 | 68979.84 | 7.79 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 5.12 | 3.76 | -0.06 | 172014.18 | 17.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.86 | 2.31 | -0.03 | 6350.44 | 23.65 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 2.06 | 2.02 | 0.01 | 238775.78 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 3.0 | 2.39 | -0.01 | 97173.07 | 41.75 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 2.92 | 1.1 | 0.04 | 47304.98 | 3.14 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 2.61 | 2.55 | -0.01 | 155.07 | 21.66 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.23 | 0.91 | -0.02 | 59919.54 | 15.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.13 | 0.89 | -0.01 | 32327.83 | 42.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
