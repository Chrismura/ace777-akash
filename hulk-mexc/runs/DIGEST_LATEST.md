# Hulk DIGEST — 2026-09-01T19:26:52Z

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
| XRPUSDT | IDLE | 1.8 | 3.36 | 1.62 | -0.02 | 33259562.38 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 1.68 | 3.13 | 1.51 | -0.03 | 328255092.33 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 1.4 | 2.61 | 1.33 | -0.02 | 537274784.19 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 3.94 | 2.44 | 0.02 | 656655.42 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 8.03 | 2.75 | 0.12 | 535160.6 | 13.82 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 6.37 | 5.18 | 0.01 | 207496.47 | 14.62 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.18 | 5.08 | -0.04 | 44549.7 | 64.47 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 4.19 | 2.95 | -0.06 | 405508.91 | 10.47 | skipped_fast |
| REDUSDT | IDLE | 2.61 | 8.35 | 2.74 | 0.09 | 100422.96 | 0.87 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.59 | 1.18 | 0.06 | 306208.3 | 13.42 | skipped_fast |
| EDELUSDT | IDLE | 1.04 | 7.54 | 6.75 | -0.08 | 171185.13 | 18.32 | skipped_fast |
| BIOUSDT | IDLE | 1.91 | 3.51 | 2.02 | -0.02 | 69766.91 | 3.88 | skipped_fast |
| KITEUSDT | IDLE | 1.76 | 3.35 | 1.08 | 0.04 | 69119.47 | 10.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.53 | 2.86 | 1.33 | -0.02 | 6414.97 | 29.16 | skipped_fast |
| FLUIDUSDT | IDLE | 2.52 | 4.41 | 4.22 | -0.03 | 129.84 | 21.77 | skipped_fast |
| TELUSDT | IDLE | 2.24 | 4.0 | 3.2 | -0.05 | 94183.43 | 54.17 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.11 | 0.81 | 0.01 | 241249.33 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 2.92 | 1.47 | 0.03 | 47102.21 | 1.58 | skipped_fast |
| MNSRYUSDT | IDLE | 0.94 | 1.71 | 1.19 | -0.02 | 33542.9 | 21.95 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.47 | 1.22 | -0.02 | 59317.8 | 23.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
