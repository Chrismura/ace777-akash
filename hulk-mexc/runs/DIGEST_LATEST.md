# Hulk DIGEST — 2026-08-21T23:32:36Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.71 | 0.11 | 6098095.54 | 8.13 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.64 | 0.15 | 140753533.94 | 2.73 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.29 | 0.53 | 0.09 | 904265.07 | 2.49 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 11.25 | 1.02 | 0.14 | 513118.43 | 35.52 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 0.99 | 0.13 | 645418.88 | 11.57 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.95 | 0.08 | 379587.68 | 14.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.43 | 0.03 | 550068.38 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.65 | 0.02 | 187048.36 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.03 | 82459.4 | 10.91 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 9.82 | 3.59 | 0.13 | 58907.09 | 43.92 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.1 | 0.07 | 187011.91 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10127.55 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.91 | 0.18 | 157768.34 | 12.92 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.01 | 0.07 | 121891.82 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.98 | 0.09 | 61375.83 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54580.51 | 16.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 23.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
