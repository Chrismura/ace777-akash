# Hulk DIGEST — 2026-08-22T00:07:03Z

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
| PYTHUSDT | IDLE | 1.79 | 6.39 | 1.92 | 0.1 | 6265513.9 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 2.06 | 8.23 | 2.64 | 0.14 | 142698783.4 | 4.87 | skipped_fast |
| HBARUSDT | IDLE | 2.82 | 6.36 | 1.89 | 0.08 | 912630.17 | 3.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.13 | 0.12 | 515251.46 | 34.02 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.83 | 0.14 | 643316.58 | 9.77 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.67 | 0.08 | 379923.54 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.37 | 0.04 | 543328.53 | 6.17 | skipped_fast |
| BIOUSDT | IDLE | 2.34 | 5.04 | 1.85 | 0.02 | 187357.79 | 6.29 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | -0.01 | 80059.71 | 11.02 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.59 | 0.13 | 59053.89 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.85 | 6.89 | 0.82 | 0.06 | 190178.36 | 46.45 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.42 | 0.7 | 0.07 | 166741.43 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 2.97 | 0.19 | 157637.83 | 8.92 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.25 | 0.09 | 61468.82 | 10.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54602.64 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 47.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
