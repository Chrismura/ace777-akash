# Hulk DIGEST — 2026-08-22T00:33:12Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.54 | 0.11 | 6392292.96 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.98 | 8.23 | 0.2 | 0.16 | 144731060.26 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.56 | 0.07 | 937751.19 | 3.77 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.44 | 0.11 | 538694.7 | 31.34 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 0.4 | 0.14 | 638853.65 | 7.95 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.04 | 0.08 | 387336.37 | 12.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.4 | 0.02 | 557328.14 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 5.04 | 0.37 | 0.02 | 185981.51 | 6.18 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79747.55 | 11.06 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.76 | 0.13 | 59851.29 | 45.1 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 186307.49 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.3 | 0.06 | 170492.01 | 7.57 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.27 | 0.1 | 61002.74 | 9.19 | skipped_fast |
| REDUSDT | IDLE | 0.56 | 5.14 | 0.0 | 0.23 | 157796.36 | 21.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9704.24 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54679.6 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
