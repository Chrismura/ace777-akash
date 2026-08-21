# Hulk DIGEST — 2026-08-21T20:47:36Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.68 | 0.08 | 5554808.02 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.52 | 0.1 | 128760688.08 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.58 | 0.17 | 153381.26 | 18.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.93 | 0.12 | 478731.35 | 23.63 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.35 | 0.1 | 641302.38 | 7.37 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.95 | 0.05 | 811194.74 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 514145.88 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.92 | 1.53 | 0.06 | 367790.16 | 12.67 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.79 | 0.0 | 188326.27 | 6.31 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 5.01 | 4.55 | -0.05 | 81427.46 | 56.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.45 | 0.02 | 56269.29 | 45.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 26.75 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.5 | 0.1 | 61164.05 | 12.11 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.16 | 0.01 | 181696.62 | 26.76 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.86 | 0.03 | 59890.74 | 7.84 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.02 | 2798.65 | 190.78 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54058.23 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
