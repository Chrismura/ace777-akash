# Hulk DIGEST — 2026-08-22T00:10:21Z

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
| PYTHUSDT | IDLE | 1.79 | 6.39 | 2.14 | 0.1 | 6287893.43 | 4.12 | skipped_fast |
| XRPUSDT | IDLE | 2.08 | 8.23 | 2.97 | 0.13 | 143273534.13 | 3.49 | skipped_fast |
| HBARUSDT | IDLE | 2.82 | 6.36 | 2.02 | 0.07 | 912508.36 | 2.53 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.23 | 0.11 | 515632.99 | 32.07 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.43 | 0.12 | 644908.34 | 8.04 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.4 | 0.08 | 380837.75 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.06 | 0.04 | 544844.9 | 6.14 | skipped_fast |
| BIOUSDT | IDLE | 2.33 | 5.04 | 1.72 | 0.02 | 187278.92 | 3.13 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.5 | 1.52 | 0.0 | 79911.03 | 44.15 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.53 | 0.14 | 59041.76 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.88 | 6.89 | 1.23 | 0.05 | 190351.95 | 31.07 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 5.42 | 1.11 | 0.06 | 166718.69 | 42.44 | skipped_fast |
| REDUSDT | IDLE | 0.59 | 4.91 | 3.23 | 0.19 | 157646.71 | 19.48 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.16 | 0.09 | 61474.37 | 12.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.32 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.73 | 0.03 | 54658.68 | 41.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
