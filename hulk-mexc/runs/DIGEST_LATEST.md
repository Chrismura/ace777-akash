# Hulk DIGEST — 2026-08-21T21:49:32Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.51 | 0.09 | 5667171.28 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.47 | 0.11 | 129984380.53 | 1.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.04 | 527438.37 | 6.19 | skipped_fast |
| HBARUSDT | IDLE | 1.97 | 4.28 | 0.01 | 0.08 | 824335.76 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 3.84 | 0.0 | 0.11 | 645884.02 | 3.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 8.19 | 2.92 | 0.11 | 493469.13 | 53.33 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.91 | 0.0 | 0.07 | 368819.9 | 10.4 | skipped_fast |
| BIOUSDT | IDLE | 2.39 | 5.2 | 1.44 | 0.03 | 187334.34 | 6.23 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.28 | 0.17 | 154162.71 | 9.01 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 4.12 | 0.99 | -0.04 | 83609.02 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 0.87 | 0.04 | 55827.28 | 47.31 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.22 | 0.12 | 61265.05 | 11.96 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 4.81 | 1.41 | 0.03 | 184207.38 | 52.77 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.65 | 0.35 | 0.04 | 62604.94 | 6.17 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.03 | 53926.1 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
