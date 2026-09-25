# Hulk DIGEST — 2026-09-25T00:41:18Z

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
| XRPUSDT | IDLE | 1.29 | 2.5 | 0.51 | 0.03 | 72033154.69 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.9 | 0.31 | 0.0 | 355151758.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.87 | 0.1 | 0.0 | 734075166.61 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 39.74 | 24.47 | 0.05 | 192487.6 | 94.5 | skipped_fast |
| PYTHUSDT | IDLE | 0.84 | 3.14 | 0.73 | 0.1 | 1008736.83 | 4.39 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.77 | 0.55 | 0.04 | 484188.18 | 11.35 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.09 | 0.84 | 0.04 | 827422.65 | 1.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.96 | 23.61 | 6.03 | 0.39 | 72120.48 | 109.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 10.18 | 5.32 | 0.14 | 100431.45 | 14.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.78 | 3.19 | 2.52 | 0.01 | 220938.75 | 13.21 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 13.31 | 5.45 | 0.28 | 294984.03 | 11.11 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.75 | 0.34 | 0.05 | 253640.14 | 5.9 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 2.93 | 2.13 | -0.01 | 64703.86 | 9.88 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 2.33 | 0.61 | 0.07 | 123462.61 | 9.87 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 2.02 | 1.89 | 0.08 | 87276.62 | 9.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.43 | 7.19 | 3.87 | 0.17 | 12945.96 | 106.9 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.02 | 1.56 | -0.05 | 103944.48 | 36.61 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.77 | 0.8 | 0.01 | 57927.45 | 7.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.63 | 1.13 | 0.92 | 0.04 | 1151.51 | 21.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.13 | -0.0 | 38242.44 | 16.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
