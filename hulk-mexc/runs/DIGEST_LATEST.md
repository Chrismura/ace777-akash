# Hulk DIGEST — 2026-08-22T00:13:11Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.77 | 0.1 | 6299032.84 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.08 | 8.23 | 3.2 | 0.13 | 143402643.25 | 2.8 | skipped_fast |
| HBARUSDT | IDLE | 2.85 | 6.36 | 2.44 | 0.07 | 918676.33 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.06 | 0.11 | 515727.57 | 29.62 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 7.42 | 1.87 | 0.12 | 645332.98 | 8.98 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.33 | 0.08 | 381104.48 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.04 | 544921.08 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 5.04 | 1.38 | 0.02 | 187149.08 | 3.13 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.5 | 1.52 | 0.0 | 79924.12 | 22.03 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.3 | 0.13 | 59444.18 | 43.62 | skipped_fast |
| TELUSDT | IDLE | 2.88 | 6.89 | 1.23 | 0.05 | 190427.87 | 31.06 | skipped_fast |
| QNTUSDT | IDLE | 2.61 | 5.42 | 2.15 | 0.05 | 167488.55 | 25.95 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 3.04 | 0.19 | 157517.6 | 8.92 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.86 | 0.09 | 61480.03 | 12.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10291.34 | 91.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.28 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54735.8 | 32.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
